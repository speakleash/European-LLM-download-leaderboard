import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from leaderboard_common import validate_config
from resolve_model_repos import build_manifest


class ModelScopeTests(unittest.TestCase):
    def setUp(self):
        self.path = ROOT / 'european-llm-hf-download-leaderboard.json'
        self.config = json.loads(self.path.read_text())

    def test_scope_on_full_current_catalog(self):
        old = json.loads((ROOT / 'data/manifest/latest.json').read_text())
        ids = old['all_repo_ids'] + old.get('excluded_repos_by_scope', [])
        orgs = {}
        for repo in ids:
            orgs.setdefault(repo.split('/')[0], []).append(repo)
        result = build_manifest(self.config, self.path, orgs)
        self.assertEqual(result['all_repo_ids'], old['all_repo_ids'])
        self.assertGreaterEqual(len(result['excluded_repos_by_scope']), 13)
        self.assertEqual(set(result['rows']), {key for key, row in self.config['models'].items() if row.get('active', True)})
        self.assertTrue(any('Mistral' in repo for repo in result['all_repo_ids']))
        self.assertFalse(any('dflash' in repo.lower() for repo in result['all_repo_ids']))
        self.assertNotIn('BSC-LT/salamandra-7b-instruct-guard', result['all_repo_ids'])

    def test_multimodal_and_quantizations_remain(self):
        config = copy.deepcopy(self.config)
        config['models'] = {'test': {'display_name': 'Test', 'official_org': 'test', 'regex': ['^test/']}}
        keep = ['test/vision-instruct', 'test/base-GGUF', 'test/base-MLX', 'test/lora-merged']
        drop = ['test/base-DFlash', 'test/base-DFlash2-FP8', 'test/base-DFlash-GGUF']
        result = build_manifest(config, self.path, {'test': keep + drop})
        self.assertEqual(result['all_repo_ids'], sorted(keep))
        self.assertEqual(result['excluded_repos_by_scope'], sorted(drop))

    def test_reviewed_catalog_admission_and_negative_controls(self):
        cases = json.loads((ROOT / 'tests/fixtures/model_scope_cases.json').read_text())
        orgs = {}
        for repo in list(cases['include']) + cases['exclude']:
            orgs.setdefault(repo.split('/')[0], []).append(repo)
        result = build_manifest(self.config, self.path, orgs)
        self.assertEqual(set(result['all_repo_ids']), set(cases['include']))
        for repo, row_id in cases['include'].items():
            self.assertIn(repo, result['rows'][row_id]['repos'])

    def test_general_purpose_boundary(self):
        cases = json.loads((ROOT / 'tests/fixtures/model_scope_cases.json').read_text())
        self.assertIn('mistralai/Pixtral-12B-2409', cases['include'])
        self.assertIn('mistralai/Voxtral-Mini-3B-2507', cases['include'])
        self.assertIn('mistralai/Magistral-Small-2509', cases['include'])
        for specialist in ['lightonai/LightOnOCR-2-1B', 'Voicelab/vlt5-base-keywords',
                           'speakleash/Bielik-One-4B-r1', 'mistralai/Mathstral-7B-v0.1',
                           'PleIAs/Pleias-Pico', 'domyn/Domyn-Edge-Teacher-IF']:
            self.assertIn(specialist, cases['exclude'])
            self.assertNotIn(specialist, cases['include'])

    def test_reviewed_repositories_have_one_matching_family(self):
        import re
        cases = json.loads((ROOT / 'tests/fixtures/model_scope_cases.json').read_text())
        for repo, expected in cases['include'].items():
            matches = [key for key, row in self.config['models'].items()
                       if any(re.match(pattern, repo) for pattern in row['regex'])]
            self.assertEqual(matches, [expected], repo)

    def test_invalid_exclusions_fail_validation(self):
        for value in ['x', [None], [''], ['[']]:
            with self.subTest(value=value):
                config = copy.deepcopy(self.config)
                config['exclude_repo_regex'] = value
                self.assertTrue(validate_config(config, warn=False))

    def test_optional_exclusions_preserve_legacy_config(self):
        self.config.pop('exclude_repo_regex')
        self.assertEqual(validate_config(self.config, warn=False), [])

if __name__ == '__main__':
    unittest.main()
