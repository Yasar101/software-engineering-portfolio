"""Keep the employer's offline examples and relative navigation reproducible."""
from pathlib import Path
import re
import subprocess
import sys
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class DocumentationTests(unittest.TestCase):
    def test_project_examples(self):
        readmes = sorted((ROOT / "projects").glob("*/README.md"))
        self.assertEqual(len(readmes), 10)
        for readme in readmes:
            with self.subTest(project=readme.parent.name):
                snippets = re.findall(r"```python\n(.*?)\n```", readme.read_text(), re.S)
                self.assertTrue(snippets, "each project needs an offline example")
                for snippet in snippets:
                    result = subprocess.run([sys.executable, "-c", snippet], cwd=ROOT,
                                            capture_output=True, text=True, timeout=15)
                    self.assertEqual(result.returncode, 0, result.stderr)

    def test_relative_markdown_links(self):
        for document in ROOT.rglob("*.md"):
            if ".git" in document.parts:
                continue
            for link in re.findall(r"\]\(([^\s)]+)\)", document.read_text()):
                if urlsplit(link).scheme:
                    continue
                path, _, anchor = unquote(link).partition("#")
                target = (document.parent / path).resolve() if path else document
                with self.subTest(document=str(document.relative_to(ROOT)), link=link):
                    self.assertTrue(target.exists(), "broken relative link")
                    if anchor and target.is_file() and target.suffix == ".md":
                        headings = re.findall(r"^#+\s+(.+)$", target.read_text(), re.M)
                        slugs = [re.sub(r"[^\w\- ]", "", h.lower()).replace(" ", "-") for h in headings]
                        self.assertIn(anchor, slugs, "missing heading anchor")
