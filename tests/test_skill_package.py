"""Offline integrity checks for the shipped skill, using only Python's stdlib.

Set ENGINEERING_SKILL_ROOT to validate another copy of the bundle. These checks
verify package invariants; realistic agent exercises are documented separately.
"""

import json
import os
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit


REPO = Path(__file__).resolve().parents[1]
SKILL = Path(os.environ.get(
    "ENGINEERING_SKILL_ROOT",
    str(REPO / "skills" / "software-engineering-build-standard"),
)).resolve()
LINK = re.compile(r"\[[^\]\n]*\]\(([^)\n]+)\)")


def local_links(document, boundary):
    """Resolve this bundle's Markdown links, including links between references."""
    for match in LINK.finditer(document.read_text(encoding="utf-8")):
        url = urlsplit(match.group(1).strip().strip("<>"))
        if url.scheme or url.netloc or not url.path:
            continue
        target = (document.parent / unquote(url.path)).resolve()
        if not target.is_relative_to(boundary.resolve()):
            raise AssertionError("Link escapes package: {} -> {}".format(document, url.path))
        if not target.exists():
            raise AssertionError("Missing link: {} -> {}".format(document, url.path))
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
        paths = list(SKILL.rglob("*"))
        self.assertTrue(paths)
        for path in paths:
            with self.subTest(path=path.relative_to(SKILL)):
                self.assertFalse(path.is_symlink(), "Review any new symlink explicitly")
                if path.is_file():
                    self.assertIn(path.suffix, {".md", ".yaml"})
                    text = path.read_text(encoding="utf-8")
                    self.assertNotIn("\x00", text)

    def test_all_bundled_markdown_links_resolve_inside_the_skill(self):
        for document in SKILL.rglob("*.md"):
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
        references = set(path.resolve() for path in (SKILL / "references").rglob("*.md"))
        self.assertFalse(references - visited, "Unreachable references: {}".format(references - visited))

    def test_tree_chooser_links_each_example_once(self):
        chooser = SKILL / "references" / "trees" / "README.md"
        examples = [path for path in local_links(chooser, SKILL) if path.suffix == ".md"]
        expected = set(chooser.parent.glob("*.md")) - {chooser}
        self.assertEqual(set(examples), expected)
        self.assertEqual(len(examples), len(set(examples)))

    def test_single_app_snapshots_keep_a_consistent_source_root(self):
        for document in (SKILL / "references" / "trees").glob("*.md"):
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
        for document in (SKILL / "references" / "trees").glob("*.md"):
            if document.name in {"README.md", "ai-service.md", "monorepo.md"}:
                continue
            first = re.search(r"(?ms)^```[^\n]*\n(.*?)^```\s*$", document.read_text(encoding="utf-8"))
            self.assertIsNotNone(first)
            pieces = set(re.findall(r"(?m)^  (\S+)", first.group(1)))
            with self.subTest(example=document.name):
                self.assertFalse(required - pieces, "Missing day-one pieces: {}".format(required - pieces))

    def test_rule_citations_use_existing_stable_ids(self):
        known = set(range(1, 66)) | {73}
        for document in SKILL.rglob("*.md"):
            text = document.read_text(encoding="utf-8")
            cited = set(int(value) for value in re.findall(r"§(\d+)", text))
            for start, end in re.findall(r"§(\d+)[–-]§?(\d+)", text):
                self.assertLessEqual(int(start), int(end))
                cited.update(range(int(start), int(end) + 1))
            with self.subTest(document=document.relative_to(SKILL)):
                self.assertFalse(cited - known, "Unknown rule IDs: {}".format(cited - known))

    def test_readme_local_links_resolve(self):
        list(local_links(REPO / "README.md", REPO))


if __name__ == "__main__":
    unittest.main()
