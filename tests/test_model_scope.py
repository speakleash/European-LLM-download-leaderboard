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
        self.assertEqual(len(result['all_repo_ids']), 565)
        self.assertEqual(len(result['excluded_repos_by_scope']), 13)
        self.assertEqual(len(result['rows']), 207)
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
