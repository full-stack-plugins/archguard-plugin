import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class VersionTests(unittest.TestCase):
    def test_cli_version_matches_installed_manifest(self):
        process = subprocess.run(
            [sys.executable, str(ROOT / 'scripts/archguard_bridge.py'), 'version', '--json'],
            capture_output=True, text=True,
        )
        result = json.loads(process.stdout)
        self.assertEqual(result['pluginVersion'], json.loads((ROOT / 'plugin.json').read_text())['version'])
        self.assertEqual(process.returncode, result['exitCode'])
