"""Independent portable identity, not private-runtime/version inheritance."""
import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

class PortableIdentityTests(unittest.TestCase):
    def test_independent_candidate(self):
        identity = json.loads((ROOT / 'TEMPLATE-IDENTITY.json').read_text())
        self.assertEqual(identity['templateName'], 'MDAAI 2.0')
        self.assertEqual(identity['releaseVersion'], (ROOT / 'VERSION').read_text().strip())
        self.assertEqual(identity['releaseStatus'], 'RELEASE')
        self.assertIsNone(identity['protocolVersion'])
        self.assertEqual(identity['origin']['sourceVersion'], '2.0.0')
        self.assertNotEqual(identity['releaseVersion'], identity['origin']['sourceVersion'])
        manifest = json.loads((ROOT / 'export-manifest.json').read_text())
        self.assertEqual(manifest['releaseIdentity'], identity)
        for e in manifest['files']:
            if e['path'] in ['VERSION', 'TEMPLATE-IDENTITY.json']:
                self.assertIsNone(e['sourceRevision'])
                self.assertTrue(e['sourceSha256'] == e['sha256'] or e.get('publicReleaseAdaptation'))

if __name__ == '__main__':
    unittest.main()
