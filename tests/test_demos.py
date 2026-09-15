"""Keep the live demos offline, referenced, and syntactically sound."""
import json
import re
import shutil
import subprocess
import unittest
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
DEMOS = ROOT / "demos"

PRIVATE_REPOS = ("ai-strategy-lab", "tradingview-ai", "utility-apps", "retro-games", "tradingview-ai-server", "adaptive-trader-ai", "mission-control", "WissoAI", "YazAI", "mediahub")


def load_portfolio():
    """Evaluate portfolio-data.js in Node and return the parsed configuration."""
    if not shutil.which("node"):
        return None
    source = (ROOT / "portfolio-data.js").read_text(encoding="utf-8")
    wrapper = "var window = {};\n" + source + "\nprocess.stdout.write(JSON.stringify(window.PORTFOLIO));"
    proc = subprocess.run(["node", "-e", wrapper], capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr)
    return json.loads(proc.stdout)


class DemoPresentationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.portfolio = load_portfolio()
        if cls.portfolio is None:
            raise unittest.SkipTest("node not available")

    def test_each_project_has_source_and_demo(self):
        self.assertTrue(self.portfolio["projects"])
        for project in self.portfolio["projects"]:
            with self.subTest(project=project["name"]):
                self.assertIn("repo", project)
                self.assertIn("demo", project)
                self.assertTrue(project["repo"].startswith("https://github.com/Yasar101/"), "repo must be a direct public source")

    def test_demo_files_exist(self):
        for project in self.portfolio["projects"]:
            with self.subTest(project=project["name"]):
                target = (ROOT / project["demo"]).resolve()
                self.assertTrue(target.exists(), f"demo file missing: {project['demo']}")
                self.assertTrue(target.is_relative_to(ROOT), "demo must live inside the repository")

    def test_no_private_repository_references(self):
        text_extensions = {".py", ".js", ".html", ".css", ".md", ".txt", ".json", ".yml", ".yaml", ".toml", ".svg"}
        haystack = ""
        source = Path(__file__).resolve()
        for path in ROOT.rglob("*"):
            if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
                continue
            if path == source or path.name == "test_demos.py":
                continue
            if path.suffix.lower() not in text_extensions:
                continue
            haystack += path.read_text(encoding="utf-8", errors="ignore") + "\n"
        for name in PRIVATE_REPOS:
            with self.subTest(repository=name):
                self.assertNotIn(name, haystack, f"private repository {name} leaked into the portfolio")

    def test_demos_are_offline(self):
        def assert_offline(file, url):
            host = urlsplit(url).netloc.lower().split(":", 1)[0]
            offline = host == "github.com" or host in ("localhost", "127.0.0.1")
            with self.subTest(file=file, url=url):
                self.assertTrue(offline, "demo must not call external services")
        for path in sorted(DEMOS.rglob("*.html")):
            text = path.read_text(encoding="utf-8")
            for url in re.findall(r"https?://[^\s\"'<>()]+", text):
                assert_offline(path.name, url)
        for script in ("demo.js",):
            path = DEMOS / script
            text = path.read_text(encoding="utf-8")
            for url in re.findall(r"https?://[^\s\"'<>()]+", text):
                assert_offline(script, url)

    def test_inline_scripts_are_valid_javascript(self):
        if not shutil.which("node"):
            self.skipTest("node not available")
        checked = 0
        for path in sorted(DEMOS.rglob("*.html")):
            for index, source in enumerate(re.findall(r"<script(?:[^>]*)>(.*?)</script>", path.read_text(encoding="utf-8"), re.S)):
                if not source.strip():
                    continue
                proc = subprocess.run(["node", "--check"], input=source, text=True, capture_output=True)
                with self.subTest(file=path.name, block=index):
                    self.assertEqual(proc.returncode, 0, proc.stderr)
                checked += 1
        self.assertGreater(checked, 0, "no inline scripts were found to check")

    def test_static_presentation_renders(self):
        if not shutil.which("node"):
            self.skipTest("node not available")
        proc = subprocess.run(["node", "--check", str(ROOT / "script.js")], capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        proc = subprocess.run(["node", "--check", str(ROOT / "portfolio-data.js")], capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)


if __name__ == "__main__":
    unittest.main()