"""Offline integrity checks for the shipped skill, using only Python's stdlib.

Set ENGINEERING_SKILL_ROOT to validate another copy of the bundle. These checks
verify package invariants; realistic agent exercises are documented separately.
"""

import html
import json
import os
from pathlib import Path, PureWindowsPath
import re
import stat
import unicodedata
import unittest
from urllib.parse import unquote, urlsplit


REPO = Path(__file__).resolve().parents[1]
SKILL = Path(os.environ.get(
    "ENGINEERING_SKILL_ROOT",
    str(REPO / "skills" / "software-engineering-build-standard"),
)).resolve()
LINK = re.compile(r"\[[^\]\n]*\]\(([^)\n]+)\)")


def regular_files(root, skip_names=frozenset()):
    """Inventory regular files, refusing unsafe nodes before reading or descending.

    pathlib's recursive glob can descend into Windows junctions before yielding
    them. Check each node's lstat metadata first; never enumerate a linked folder.
    This is a static package check, not a defense against concurrent path changes.
    """
    metadata = root.lstat()
    if stat.S_ISLNK(metadata.st_mode):
        raise AssertionError("Source tree contains a symlink: {}".format(root))
    if getattr(metadata, "st_file_attributes", 0) & 0x400:
        raise AssertionError("Source tree contains a Windows reparse point: {}".format(root))
    if stat.S_ISREG(metadata.st_mode):
        yield root
    elif stat.S_ISDIR(metadata.st_mode):
        for child in sorted(root.iterdir(), key=lambda path: path.name):
            if child.name not in skip_names:
                yield from regular_files(child, skip_names)
    else:
        raise AssertionError("Source tree contains a nonregular node: {}".format(root))


def markdown_lines(text):
    """Instruction prose outside YAML frontmatter and fenced code examples."""
    fence = None
    frontmatter = text.startswith("---\n") or text.startswith("---\r\n")
    for number, line in enumerate(text.splitlines()):
        if frontmatter:
            if number and line == "---":
                frontmatter = False
            yield ""
            continue
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = None
            yield ""
        elif marker:
            fence = marker[1]
            yield ""
        else:
            yield line


def heading_ids(text):
    """GitHub-style IDs for this package's ATX and single-line Setext headings.

    Handles inline emphasis/code/links, Unicode, entity decoding and duplicate IDs.
    This is not a general Markdown renderer: raw HTML IDs/headings and custom anchor
    extensions are not supported. Local fragments must name a recognized heading.
    """
    identifiers = set()
    previous = ""
    for line in markdown_lines(text):
        atx = re.match(r"^ {0,3}#{1,6}[ \t]+(.+?)\s*#*\s*$", line)
        setext = previous and re.fullmatch(r" {0,3}(?:=+|-+)\s*", line)
        heading = atx[1] if atx else previous.strip() if setext else None
        previous = line if not atx and not setext else ""
        if heading is None:
            continue
        heading = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", heading)
        heading = re.sub(r"<[^>]*>", "", heading)
        heading = re.sub(r"(?<!\w)_{1,3}(.+?)_{1,3}(?!\w)", r"\1", heading)
        heading = html.unescape(heading).replace("*", "").replace("`", "")
        heading = heading.strip().lower().replace("\t", " ")
        base = "".join(character for character in heading
                       if character in " _-" or unicodedata.category(character)[0] in "LNM")
        base = base.replace(" ", "-")
        identifier = base
        suffix = 0
        while identifier in identifiers:
            suffix += 1
            identifier = "{}-{}".format(base, suffix)
        identifiers.add(identifier)
    return identifiers


def checked_local_path(path, boundary):
    """Check each component below the selected root before following the path.

    The explicitly selected root may be an installation alias. Links and reparse
    points below its resolved boundary are package resources, so refuse them even
    in directories omitted from the repository inventory, such as .git.
    """
    if not path.is_relative_to(boundary):
        raise AssertionError("Link escapes package: {}".format(path))
    current = boundary
    parts = path.relative_to(boundary).parts
    for index, part in enumerate(parts):
        if part == "..":
            current = current.parent
            if not current.is_relative_to(boundary):
                raise AssertionError("Link escapes package: {}".format(path))
            continue
        current = current / part
        try:
            metadata = current.lstat()
        except FileNotFoundError:
            raise AssertionError("Missing link: {}".format(current)) from None
        if stat.S_ISLNK(metadata.st_mode):
            raise AssertionError("Local link contains a symlink: {}".format(current))
        if getattr(metadata, "st_file_attributes", 0) & 0x400:
            raise AssertionError("Local link contains a Windows reparse point: {}".format(current))
        if not (stat.S_ISREG(metadata.st_mode) or stat.S_ISDIR(metadata.st_mode)):
            raise AssertionError("Nonregular local link target: {}".format(current))
        if index < len(parts) - 1 and not stat.S_ISDIR(metadata.st_mode):
            raise AssertionError("Non-directory local link component: {}".format(current))
    return current


def local_links(document, boundary):
    """Validate simple inline Markdown links and heading fragments, without network I/O.

    For this repository's instruction bundles, a local directory link resolves its
    README.md; it is not enough that a directory exists. URI paths/fragments are
    decoded once; local paths must be relative, and every component (including a
    directory README) must stay inside boundary without linked resources. This
    scoped check is not a general Markdown/HTML link parser.
    """
    selected_boundary = boundary.absolute()
    boundary = selected_boundary.resolve()
    document = document.absolute()
    if document.is_relative_to(selected_boundary):
        document = boundary / document.relative_to(selected_boundary)
    if not document.is_relative_to(boundary):
        raise AssertionError("Document escapes package: {}".format(document))
    document = checked_local_path(document, boundary)
    if not stat.S_ISREG(document.lstat().st_mode):
        raise AssertionError("Nonregular Markdown document: {}".format(document))
    text = "\n".join(markdown_lines(document.read_text(encoding="utf-8")))
    # Inline code is an example, not a navigable link.
    text = re.sub(r"(`+).*?\1", "", text)
    for match in LINK.finditer(text):
        url = urlsplit(match.group(1).strip().strip("<>"))
        if url.scheme == "file" or (len(url.scheme) == 1 and url.scheme.isalpha()):
            raise AssertionError("Nonportable local link: {} -> {}".format(document, match.group(1)))
        if url.scheme or url.netloc:
            continue
        local_path = unquote(url.path)
        if Path(local_path).is_absolute() or PureWindowsPath(local_path).anchor:
            raise AssertionError("Nonportable local link: {} -> {}".format(document, url.path))
        target = checked_local_path(document.parent / local_path, boundary) if local_path else document
        if not target.is_relative_to(boundary):
            raise AssertionError("Link escapes package: {} -> {}".format(document, url.path))
        if target.is_dir():
            target = checked_local_path(target / "README.md", boundary)
            if not target.is_relative_to(boundary):
                raise AssertionError("Directory README escapes package: {} -> {}".format(document, url.path))
            if not target.is_file():
                raise AssertionError("Missing directory README: {} -> {}".format(document, url.path))
        if not target.exists():
            raise AssertionError("Missing link: {} -> {}".format(document, url.path))
        if not stat.S_ISREG(target.lstat().st_mode):
            raise AssertionError("Nonregular local link target: {} -> {}".format(document, url.path))
        if url.fragment:
            if target.suffix.lower() != ".md":
                raise AssertionError("Unsupported local fragment target: {} -> {}".format(document, url.path))
            fragment = unquote(url.fragment)
            if fragment not in heading_ids(target.read_text(encoding="utf-8")):
                raise AssertionError("Missing heading fragment: {} -> {}#{}".format(document, url.path, fragment))
        yield target


def simple_string(value):
    """Read the simple quoted/bare string fields used by this package.

    This is deliberately not a general YAML validator. Use an Agent Skills
    frontmatter validator as well when changing the YAML representation.
    """
    value = value.strip()
    if value.startswith('"'):
        return json.loads(value)
    if value.startswith("'"):
        if not value.endswith("'"):
            raise AssertionError("Unclosed YAML string")
        return value[1:-1].replace("''", "'")
    return value


class SkillPackageTests(unittest.TestCase):
    def setUp(self):
        # Every check, including direct entrypoint and metadata reads, starts
        # behind this guard; one failed resource test must not leave the other
        # independent unittest cases free to read linked external content.
        self.bundle_files = list(regular_files(SKILL))

    def test_frontmatter_identity_and_description(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        header = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", text, re.S)
        self.assertIsNotNone(header, "SKILL.md must have closed YAML frontmatter")
        fields = {}
        for line in header.group(1).splitlines():
            key, separator, value = line.partition(":")
            self.assertTrue(separator, "Malformed frontmatter field")
            self.assertNotIn(key, fields, "Duplicate frontmatter field")
            fields[key] = simple_string(value)
        name = fields["name"]
        self.assertEqual(name, SKILL.name)
        self.assertRegex(name, r"\A[a-z0-9]+(?:-[a-z0-9]+)*\Z")
        self.assertLessEqual(len(name), 64)
        description = fields["description"]
        self.assertIsInstance(description, str)
        self.assertTrue(description.strip())
        self.assertLessEqual(len(description), 1024)
        self.assertLessEqual(len(text.splitlines()), 500)

    def test_ui_metadata_mentions_the_shipped_skill(self):
        text = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertRegex(text, r"(?m)^interface:\s*$")
        fields = dict(re.findall(r"(?m)^  ([a-z_]+):\s*(.+)$", text))
        summary = simple_string(fields["short_description"])
        self.assertGreaterEqual(len(summary), 25)
        self.assertLessEqual(len(summary), 64)
        self.assertIn("$" + SKILL.name, simple_string(fields["default_prompt"]))

    def test_bundle_contains_only_readable_instruction_resources(self):
        paths = self.bundle_files
        self.assertTrue(paths)
        for path in paths:
            with self.subTest(path=path.relative_to(SKILL)):
                self.assertIn(path.suffix, {".md", ".yaml"})
                text = path.read_text(encoding="utf-8")
                self.assertNotIn("\x00", text)

    def test_all_bundled_markdown_links_resolve_inside_the_skill(self):
        for document in self.bundle_files:
            if document.suffix != ".md":
                continue
            with self.subTest(document=document.relative_to(SKILL)):
                list(local_links(document, SKILL))

    def test_all_references_are_reachable_from_the_entrypoint(self):
        pending = [SKILL / "SKILL.md"]
        visited = set()
        while pending:
            document = pending.pop().resolve()
            if document in visited:
                continue
            visited.add(document)
            for target in local_links(document, SKILL):
                if target.is_dir():
                    target = target / "README.md"
                if target.suffix == ".md":
                    self.assertTrue(target.is_file())
                    pending.append(target)
        references = set(path.resolve() for path in self.bundle_files
                         if path.suffix == ".md" and path.is_relative_to(SKILL / "references"))
        self.assertFalse(references - visited, "Unreachable references: {}".format(references - visited))

    def test_tree_chooser_links_each_example_once(self):
        chooser = SKILL / "references" / "trees" / "README.md"
        examples = [path for path in local_links(chooser, SKILL) if path.suffix == ".md"]
        expected = {path for path in self.bundle_files if path.parent == chooser.parent and path.suffix == ".md"} - {chooser}
        self.assertEqual(set(examples), expected)
        self.assertEqual(len(examples), len(set(examples)))

    def test_single_app_snapshots_keep_a_consistent_source_root(self):
        for document in self.bundle_files:
            if document.parent != SKILL / "references" / "trees" or document.suffix != ".md":
                continue
            if document.name in {"README.md", "ai-service.md", "monorepo.md"}:
                continue
            text = document.read_text(encoding="utf-8")
            blocks = re.findall(r"(?ms)^```[^\n]*\n(.*?)^```\s*$", text)
            single_app_blocks = [block for block in blocks if not re.search(r"(?m)^  apps/", block)]
            roots = set(re.findall(r"(?m)^  ((?:[^/\s]+/)*src)/(?=\s|$)", "\n".join(single_app_blocks)))
            with self.subTest(example=document.name):
                self.assertEqual(roots, {"src"}, "A single-app example must not move its source root between stages")

    def test_single_app_day_one_examples_include_the_starter_kit(self):
        required = {"README.md", "CHANGELOG.md", ".gitignore", "docs/scope.md", "src/", "tests/"}
        for document in self.bundle_files:
            if document.parent != SKILL / "references" / "trees" or document.suffix != ".md":
                continue
            if document.name in {"README.md", "ai-service.md", "monorepo.md"}:
                continue
            first = re.search(r"(?ms)^```[^\n]*\n(.*?)^```\s*$", document.read_text(encoding="utf-8"))
            self.assertIsNotNone(first)
            pieces = set(re.findall(r"(?m)^  (\S+)", first.group(1)))
            with self.subTest(example=document.name):
                self.assertFalse(required - pieces, "Missing day-one pieces: {}".format(required - pieces))

    def test_rule_citations_use_existing_stable_ids(self):
        known = set(range(1, 66)) | {73}
        for document in self.bundle_files:
            if document.suffix != ".md":
                continue
            text = document.read_text(encoding="utf-8")
            cited = set(int(value) for value in re.findall(r"§(\d+)", text))
            for start, end in re.findall(r"§(\d+)[–-]§?(\d+)", text):
                self.assertLessEqual(int(start), int(end))
                cited.update(range(int(start), int(end) + 1))
            with self.subTest(document=document.relative_to(SKILL)):
                self.assertFalse(cited - known, "Unknown rule IDs: {}".format(cited - known))

    def test_all_repository_markdown_links_resolve(self):
        # Finish the inventory first: an early README can link to a later FIFO
        # or other unsafe node before a lazy walk would otherwise discover it.
        documents = list(regular_files(REPO, skip_names={".git"}))
        for document in documents:
            if document.suffix != ".md":
                continue
            with self.subTest(document=document.relative_to(REPO)):
                list(local_links(document, REPO))


if __name__ == "__main__":
    unittest.main()
