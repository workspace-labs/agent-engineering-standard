"""Adversarial fixture checks for the package validator, not an agent behavior exam."""

import os
from pathlib import Path
import stat
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest import mock
from urllib.parse import quote

import test_skill_package as package


def directory_link(link, target):
    """A no-admin junction on Windows, a directory symlink on POSIX."""
    if os.name == "nt":
        environment = dict(os.environ, ENGINEERING_TEST_LINK=str(link), ENGINEERING_TEST_TARGET=str(target))
        command = Path(os.environ["SystemRoot"]) / "System32" / "cmd.exe"
        # A fixed command line avoids Python's list quoting being interpreted a
        # second time by cmd. Fixture paths enter only through quoted variables;
        # delayed expansion and startup scripts are disabled.
        subprocess.run(
            '"{}" /d /v:off /c mklink /J "%ENGINEERING_TEST_LINK%" "%ENGINEERING_TEST_TARGET%"'.format(command),
            executable=str(command), env=environment, check=True, capture_output=True, text=True,
        )
    else:
        link.symlink_to(target, target_is_directory=True)


def remove_directory_link(link):
    if os.name == "nt":
        link.rmdir()  # the fixture's junction only; its target remains intact
    else:
        link.unlink()


class MarkdownLinkRegressions(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="engineering-links-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()

    def write(self, name, text):
        document = self.root / name
        document.parent.mkdir(parents=True, exist_ok=True)
        document.write_text(text, encoding="utf-8")
        return document

    def links(self, document):
        return list(package.local_links(document, self.root))

    def test_missing_path_fragment_is_refused(self):
        self.write("guide.md", "# Existing heading\n")
        document = self.write("README.md", "[guide](guide.md#missing-heading)\n")
        with self.assertRaisesRegex(AssertionError, "fragment"):
            self.links(document)

    def test_missing_pure_fragment_is_refused(self):
        document = self.write("README.md", "# Existing heading\n[here](#missing-heading)\n")
        with self.assertRaisesRegex(AssertionError, "fragment"):
            self.links(document)

    def test_directory_link_without_readme_is_refused(self):
        (self.root / "guides").mkdir()
        document = self.write("README.md", "[guides](guides/)\n")
        with self.assertRaisesRegex(AssertionError, "README"):
            self.links(document)

    def test_directory_readme_and_fragment_are_resolved(self):
        target = self.write("guides/README.md", "# Guide overview\n")
        document = self.write("README.md", "[guides](guides/#guide-overview)\n")
        self.assertEqual(self.links(document), [target.resolve()])

    def test_encoded_path_and_non_ascii_duplicate_headings(self):
        target = self.write("guide notes.md", "# Café العربية\n# Café العربية\n# Café العربية-1\n")
        document = self.write("README.md", "[guide](guide%20notes.md#caf%C3%A9-%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9-1)\n")
        self.assertEqual(self.links(document), [target.resolve()])
        document.write_text("[guide](guide%20notes.md#café-العربية-1-1)\n", encoding="utf-8")
        self.assertEqual(self.links(document), [target.resolve()])

    def test_valid_same_document_atx_and_setext_headings(self):
        document = self.write("README.md", "# **Build** `tools` &amp; tests\n\nSetext title\n============\n\n[one](#build-tools--tests)\n[two](#setext-title)\n")
        self.assertEqual(self.links(document), [document.resolve(), document.resolve()])

    def test_fenced_example_heading_is_not_a_fragment(self):
        document = self.write("README.md", "# Actual heading\n\n```markdown\n# Example only\n```\n\n[bad](#example-only)\n")
        with self.assertRaisesRegex(AssertionError, "fragment"):
            self.links(document)

    def test_existing_files_and_external_links_remain_valid(self):
        target = self.write("guide.md", "# Guide\n")
        document = self.write("README.md", "[guide](guide.md)\n[web](https://example.test/a#anything)\n[mail](mailto:reader@example.test)\n")
        self.assertEqual(self.links(document), [target.resolve()])

    def test_fenced_and_inline_code_links_are_examples(self):
        document = self.write("README.md", "# Actual\n\n```markdown\n[example](not-a-file.md)\n```\n\n`[also an example](not-a-file.md)`\n")
        self.assertEqual(self.links(document), [])

    def test_local_file_urls_are_not_portable_external_links(self):
        for link in ("file:///outside/private.md", "file:../private.md", "C:/outside/private.md"):
            with self.subTest(link=link):
                document = self.write("README.md", "[local]({})\n".format(link))
                with self.assertRaisesRegex(AssertionError, "local link"):
                    self.links(document)

    def test_absolute_paths_inside_boundary_are_not_portable_links(self):
        target = self.write("guide.md", "# Guide\n")
        for link in (target.as_posix(), quote(target.as_posix(), safe="")):
            with self.subTest(link=link):
                document = self.write("README.md", "[guide]({}#guide)\n".format(link))
                with self.assertRaisesRegex(AssertionError, "Nonportable local link"):
                    self.links(document)

    def test_relative_parent_links_inside_boundary_remain_valid(self):
        target = self.write("guide.md", "# Guide\n")
        document = self.write("docs/README.md", "[guide](../guide.md#guide)\n")
        self.assertEqual(self.links(document), [target.resolve()])

    def test_explicit_root_alias_remains_supported(self):
        target = self.write("bundle/guide.md", "# Guide\n")
        self.write("bundle/README.md", "[guide](guide.md#guide)\n")
        alias = self.root / "selected-root"
        directory_link(alias, self.root / "bundle")
        try:
            self.assertEqual(list(package.local_links(alias / "README.md", alias)), [target.resolve()])
        finally:
            remove_directory_link(alias)

    def test_non_markdown_fragment_is_explicitly_unsupported(self):
        self.write("picture.svg", '<svg id="shape"></svg>')
        document = self.write("README.md", "[shape](picture.svg#shape)\n")
        with self.assertRaisesRegex(AssertionError, "Unsupported local fragment"):
            self.links(document)

    def test_directory_readme_link_cannot_escape_the_boundary(self):
        boundary = self.root / "bundle"
        guides = boundary / "guides"
        guides.mkdir(parents=True)
        outside = self.root / "outside"
        outside.mkdir()
        document = self.write("bundle/README.md", "[guide](guides/)\n")
        linked_readme = guides / "README.md"
        directory_link(linked_readme, outside)
        try:
            with self.assertRaisesRegex(AssertionError, "symlink|reparse point"):
                list(package.local_links(document, boundary))
        finally:
            remove_directory_link(linked_readme)

    def test_documents_beyond_the_repository_readme_are_checked(self):
        self.write("README.md", "# Repository\n")
        self.write("docs/guide.md", "# Guide\n[missing](#does-not-exist)\n")
        check = package.SkillPackageTests("test_all_repository_markdown_links_resolve")
        result = unittest.TestResult()
        with mock.patch.object(package, "REPO", self.root):
            check.run(result)
        self.assertEqual(result.errors, [])
        self.assertTrue(result.failures, "a broken link outside README must fail package validation")

    def test_repository_inventory_finishes_before_reading_any_markdown(self):
        self.write("README.md", "[pipe](zzz-pipe.md#heading)\n")
        unsafe = self.write("zzz-pipe.md", "# Heading\n")
        native_lstat, native_read = Path.lstat, Path.read_text
        reads = []

        def fixture_lstat(path, *args, **kwargs):
            if path == unsafe:
                return SimpleNamespace(st_mode=stat.S_IFIFO | 0o600)
            return native_lstat(path, *args, **kwargs)

        def trapped_read(path, *args, **kwargs):
            reads.append(path)
            if path == unsafe:
                raise AssertionError("unsafe target read intercepted; no real FIFO was opened")
            return native_read(path, *args, **kwargs)

        # A regular placeholder plus synthetic FIFO metadata is portable and
        # cannot hang even if the read trap or the safety check regresses.
        check = package.SkillPackageTests("test_all_repository_markdown_links_resolve")
        result = unittest.TestResult()
        with mock.patch.object(package, "REPO", self.root), \
                mock.patch.object(Path, "lstat", fixture_lstat), \
                mock.patch.object(Path, "read_text", trapped_read):
            check.run(result)
        self.assertEqual(reads, [], "the full inventory must reject the later FIFO before reading README or its target")
        self.assertEqual(result.errors, [])
        self.assertTrue(result.failures)

    def test_fragment_target_must_be_regular_before_reading_it(self):
        document = self.write("README.md", "[pipe](zzz-pipe.md#heading)\n")
        unsafe = self.write("zzz-pipe.md", "# Heading\n")
        native_lstat, native_read = Path.lstat, Path.read_text
        reads = []

        def fixture_lstat(path, *args, **kwargs):
            if path == unsafe:
                return SimpleNamespace(st_mode=stat.S_IFIFO | 0o600)
            return native_lstat(path, *args, **kwargs)

        def trapped_read(path, *args, **kwargs):
            reads.append(path)
            if path == unsafe:
                raise AssertionError("unsafe target read intercepted; no real FIFO was opened")
            return native_read(path, *args, **kwargs)

        with mock.patch.object(Path, "lstat", fixture_lstat), \
                mock.patch.object(Path, "read_text", trapped_read):
            with self.assertRaisesRegex(AssertionError, "[Nn]onregular"):
                self.links(document)
        self.assertEqual(reads, [document.resolve()])

    def test_fragment_under_skipped_git_directory_is_checked_before_read(self):
        document = self.write("README.md", "[pipe](.git/zzz-pipe.md#heading)\n")
        unsafe = self.write(".git/zzz-pipe.md", "# Heading\n")
        native_lstat, native_read = Path.lstat, Path.read_text
        reads = []

        def fixture_lstat(path, *args, **kwargs):
            if path == unsafe:
                return SimpleNamespace(st_mode=stat.S_IFIFO | 0o600)
            return native_lstat(path, *args, **kwargs)

        def trapped_read(path, *args, **kwargs):
            reads.append(path)
            if path == unsafe:
                raise AssertionError("unsafe skipped-subtree read intercepted; no real FIFO was opened")
            return native_read(path, *args, **kwargs)

        check = package.SkillPackageTests("test_all_repository_markdown_links_resolve")
        result = unittest.TestResult()
        with mock.patch.object(package, "REPO", self.root), \
                mock.patch.object(Path, "lstat", fixture_lstat), \
                mock.patch.object(Path, "read_text", trapped_read):
            check.run(result)
        self.assertEqual(reads, [document.resolve()], "a target omitted from the inventory still needs its own file-type check")
        self.assertEqual(result.errors, [])
        self.assertTrue(result.failures)
        self.assertIn("Nonregular local link target", result.failures[0][1])

    def test_native_link_under_skipped_git_is_refused_before_read(self):
        document = self.write("README.md", "[guide](.git/linked/guide.md#guide)\n")
        target = self.write("guides/guide.md", "# Guide\n")
        (self.root / ".git").mkdir()
        linked_directory = self.root / ".git" / "linked"
        directory_link(linked_directory, target.parent)
        native_read = Path.read_text
        reads = []

        def tracked_read(path, *args, **kwargs):
            reads.append(path)
            return native_read(path, *args, **kwargs)

        check = package.SkillPackageTests("test_all_repository_markdown_links_resolve")
        result = unittest.TestResult()
        try:
            with mock.patch.object(package, "REPO", self.root), \
                    mock.patch.object(Path, "read_text", tracked_read):
                check.run(result)
            # The ordinary guide is read later by repository validation, but the
            # README's linked route must fail before it reads that guide itself.
            self.assertEqual(reads, [document.resolve(), target.resolve()])
            self.assertEqual(result.errors, [])
            self.assertTrue(result.failures)
            self.assertRegex(result.failures[0][1], "symlink|reparse point")
            self.assertEqual(target.read_text(encoding="utf-8"), "# Guide\n")
        finally:
            remove_directory_link(linked_directory)

    def test_skipped_reparse_file_and_directory_readme_are_refused_before_read(self):
        for link, filename in ((".git/guide.md#guide", ".git/guide.md"),
                               (".git/guides/#guide", ".git/guides/README.md")):
            with self.subTest(link=link):
                document = self.write("README.md", "[guide]({})\n".format(link))
                unsafe = self.write(filename, "# Guide\n")
                native_lstat, native_read = Path.lstat, Path.read_text
                reads = []

                def fixture_lstat(path, *args, **kwargs):
                    if path == unsafe:
                        return SimpleNamespace(st_mode=stat.S_IFREG | 0o600, st_file_attributes=0x400)
                    return native_lstat(path, *args, **kwargs)

                def tracked_read(path, *args, **kwargs):
                    reads.append(path)
                    return native_read(path, *args, **kwargs)

                check = package.SkillPackageTests("test_all_repository_markdown_links_resolve")
                result = unittest.TestResult()
                with mock.patch.object(package, "REPO", self.root), \
                        mock.patch.object(Path, "lstat", fixture_lstat), \
                        mock.patch.object(Path, "read_text", tracked_read):
                    check.run(result)
                self.assertEqual(reads, [document.resolve()])
                self.assertEqual(result.errors, [])
                self.assertTrue(result.failures)
                self.assertIn("reparse point", result.failures[0][1])

    def test_missing_file_and_encoded_escape_are_refused(self):
        for link in ("missing.md", "%2e%2e/outside.md"):
            with self.subTest(link=link):
                document = self.write("README.md", "[bad]({})\n".format(link))
                with self.assertRaises(AssertionError):
                    self.links(document)


class ResourceBoundaryRegressions(unittest.TestCase):
    @staticmethod
    def resource_result(bundle, method="test_bundle_contains_only_readable_instruction_resources"):
        check = package.SkillPackageTests(method)
        result = unittest.TestResult()
        with mock.patch.object(package, "SKILL", bundle):
            check.run(result)
        return result

    @staticmethod
    def fake_bundle(node):
        bundle = mock.Mock(spec=Path)
        bundle.lstat.return_value = SimpleNamespace(st_mode=stat.S_IFDIR | 0o755)
        bundle.iterdir.return_value = [node]
        bundle.rglob.return_value = [node]  # exercise the old traversal in fail-first runs
        return bundle

    def test_windows_junction_metadata_is_refused_portably(self):
        node = mock.Mock(spec=Path)
        node.is_symlink.return_value = False
        node.is_file.return_value = False
        node.relative_to.return_value = Path("linked-directory")
        node.lstat.return_value = SimpleNamespace(
            st_mode=stat.S_IFDIR | 0o755,
            st_file_attributes=0x400,  # FILE_ATTRIBUTE_REPARSE_POINT
            st_reparse_tag=0xA0000003,  # IO_REPARSE_TAG_MOUNT_POINT
        )
        bundle = self.fake_bundle(node)
        result = self.resource_result(bundle)
        self.assertEqual(result.errors, [])
        self.assertTrue(result.failures, "a directory junction must not pass the source-only resource check")

    def test_nonregular_node_is_refused_without_reading_it(self):
        node = mock.Mock(spec=Path)
        node.is_symlink.return_value = False
        node.is_file.return_value = False
        node.relative_to.return_value = Path("fixture.pipe")
        node.lstat.return_value = SimpleNamespace(st_mode=stat.S_IFIFO | 0o600)
        bundle = self.fake_bundle(node)
        result = self.resource_result(bundle)
        self.assertEqual(result.errors, [])
        self.assertTrue(result.failures, "a special node must not pass as a readable instruction resource")
        node.read_text.assert_not_called()

    def test_junction_is_refused_before_enumerating_its_children(self):
        node = mock.Mock(spec=Path)
        node.is_symlink.return_value = False
        node.is_file.return_value = False
        node.relative_to.return_value = Path("linked-directory")
        node.lstat.return_value = SimpleNamespace(st_mode=stat.S_IFDIR | 0o755, st_file_attributes=0x400)
        bundle = self.fake_bundle(node)

        def recursive_glob(pattern):
            node.iterdir()  # the descent Windows pathlib may perform before yielding
            return [node]

        bundle.rglob.side_effect = recursive_glob
        result = self.resource_result(bundle)
        node.iterdir.assert_not_called()
        self.assertEqual(result.errors, [])
        self.assertTrue(result.failures)

    def test_rule_checks_do_not_read_a_linked_external_child(self):
        node = mock.Mock(spec=Path)
        node.lstat.return_value = SimpleNamespace(st_mode=stat.S_IFDIR | 0o755, st_file_attributes=0x400)
        bundle = self.fake_bundle(node)
        external = mock.Mock(spec=Path)
        external.read_text.return_value = "# Synthetic external document\n"
        external.relative_to.return_value = Path("linked-directory/external.md")
        bundle.rglob.return_value = [external]
        result = self.resource_result(bundle, "test_rule_citations_use_existing_stable_ids")
        external.read_text.assert_not_called()
        node.iterdir.assert_not_called()
        self.assertEqual(result.errors, [])
        self.assertTrue(result.failures)

    def test_native_entrypoint_link_is_refused_before_any_text_read(self):
        with tempfile.TemporaryDirectory(prefix="engineering-entry-link-") as temporary:
            root = Path(temporary)
            bundle = root / "bundle"
            bundle.mkdir()
            outside = root / "outside"
            outside.mkdir()
            linked_entry = bundle / "SKILL.md"
            directory_link(linked_entry, outside)
            try:
                with mock.patch.object(Path, "read_text", side_effect=AssertionError("unexpected linked text read")) as read:
                    result = self.resource_result(bundle, "test_frontmatter_identity_and_description")
                read.assert_not_called()
                self.assertEqual(result.errors, [])
                self.assertTrue(result.failures)
            finally:
                remove_directory_link(linked_entry)

    def test_native_directory_link_is_refused_and_target_preserved(self):
        with tempfile.TemporaryDirectory(prefix="engineering-resource-") as temporary:
            root = Path(temporary)
            bundle = root / "bundle"
            bundle.mkdir()
            target = root / "external"
            target.mkdir()
            sentinel = target / "sentinel.md"
            sentinel.write_text("synthetic external sentinel\n", encoding="utf-8")
            link = bundle / "linked-directory"
            directory_link(link, target)
            try:
                result = self.resource_result(bundle)
                self.assertEqual(result.errors, [])
                self.assertTrue(result.failures, "the native directory link must be refused")
                self.assertEqual(sentinel.read_text(encoding="utf-8"), "synthetic external sentinel\n")
            finally:
                remove_directory_link(link)


if __name__ == "__main__":
    unittest.main()
