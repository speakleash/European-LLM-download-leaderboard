import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from render_timeseries_charts import model_daily_delta_series, org_daily_deltas, org_totals_per_day


class OrganizationHistoryTests(unittest.TestCase):
    def test_late_publisher_has_gaps_and_no_false_first_day_growth(self):
        records = [
            {'snapshot_date': '2026-11-14', 'rows': {'a': {'downloads_30d': 10, 'downloads_all_time': 100}}},
            {'snapshot_date': '2026-11-15', 'rows': {'a': {'downloads_30d': 12, 'downloads_all_time': 110},
                                                  'b': {'downloads_30d': 500, 'downloads_all_time': 10000}}},
            {'snapshot_date': '2026-11-16', 'rows': {'a': {'downloads_30d': 13, 'downloads_all_time': 120},
                                                  'b': {'downloads_30d': 505, 'downloads_all_time': 10007}}},
        ]
        for record in records:
            record['manifest_hash'] = 'stable-catalog'
        dates, rolling, lifetime = org_totals_per_day(records, {'a': {'official_org': 'old'}, 'b': {'official_org': 'new'}})
        self.assertEqual(len(dates), 3)
        self.assertEqual(rolling['new'], [None, 500, 505])
        self.assertEqual(lifetime['new'], [None, 10000, 10007])
        self.assertEqual(org_daily_deltas(records, lifetime)['new'], [None, None, 7])
        self.assertEqual(org_daily_deltas(records, lifetime)['old'], [None, 10, 10])

    def test_gap_resets_daily_comparison_but_zero_is_a_measurement(self):
        records = [
            {'snapshot_date': '2026-11-13', 'rows': {'a': {'downloads_30d': 0, 'downloads_all_time': 0}}},
            {'snapshot_date': '2026-11-14', 'rows': {}},
            {'snapshot_date': '2026-11-15', 'rows': {'a': {'downloads_30d': 4, 'downloads_all_time': 30}}},
            {'snapshot_date': '2026-11-16', 'rows': {'a': {'downloads_30d': 8, 'downloads_all_time': 34}}},
        ]
        for record in records:
            record['manifest_hash'] = 'stable-catalog'
        dates, rolling, lifetime = org_totals_per_day(records, {'a': {'official_org': 'org'}})
        self.assertEqual(rolling['org'], [0, None, 4, 8])
        self.assertEqual(org_daily_deltas(records, lifetime)['org'], [None, None, None, 4])

    def test_new_models_do_not_turn_lifetime_downloads_into_daily_growth(self):
        records = [
            {'snapshot_date': '2026-11-14', 'manifest_hash': 'old',
             'rows': {'base': {'downloads_30d': 100, 'downloads_all_time': 1000}}},
            {'snapshot_date': '2026-11-15', 'manifest_hash': 'expanded',
             'rows': {'base': {'downloads_30d': 101, 'downloads_all_time': 1010},
                      'new': {'downloads_30d': 50000, 'downloads_all_time': 8000000}}},
            {'snapshot_date': '2026-11-16', 'manifest_hash': 'expanded',
             'rows': {'base': {'downloads_30d': 102, 'downloads_all_time': 1020},
                      'new': {'downloads_30d': 50005, 'downloads_all_time': 8000005}}},
        ]
        _, _, lifetime = org_totals_per_day(records, {'base': {'official_org': 'org'}, 'new': {'official_org': 'org'}})
        self.assertEqual(org_daily_deltas(records, lifetime)['org'], [None, None, 15])
        self.assertEqual(model_daily_delta_series(records, 'base')[1], [None, None, 10])
        self.assertEqual(model_daily_delta_series(records, 'new')[1], [None, None, 5])

    def test_equal_repo_counts_do_not_establish_a_stable_catalog(self):
        records = [
            {'snapshot_date': '2026-11-15', 'manifest_hash': 'old',
             'rows': {'a': {'downloads_30d': 20, 'downloads_all_time': 100, 'repo_count': 1}}},
            {'snapshot_date': '2026-11-16', 'manifest_hash': 'replacement',
             'rows': {'a': {'downloads_30d': 50, 'downloads_all_time': 8000000, 'repo_count': 1}}},
        ]
        _, _, lifetime = org_totals_per_day(records, {'a': {'official_org': 'org'}})
        self.assertEqual(org_daily_deltas(records, lifetime)['org'], [None, None])
        self.assertEqual(model_daily_delta_series(records, 'a')[1], [None, None])

    def test_missing_catalog_identity_is_not_assumed_comparable(self):
        records = [
            {'snapshot_date': '2026-11-15', 'rows': {'a': {'downloads_30d': 20, 'downloads_all_time': 100}}},
            {'snapshot_date': '2026-11-16', 'rows': {'a': {'downloads_30d': 30, 'downloads_all_time': 100000}}},
        ]
        _, _, lifetime = org_totals_per_day(records, {'a': {'official_org': 'org'}})
        self.assertEqual(org_daily_deltas(records, lifetime)['org'], [None, None])
        self.assertEqual(model_daily_delta_series(records, 'a')[1], [None, None])

    def test_incomplete_fetch_does_not_create_a_recovery_spike(self):
        records = [
            {'snapshot_date': '2026-11-13', 'manifest_hash': 'stable',
             'rows': {'a': {'downloads_30d': 100, 'downloads_all_time': 5000000, 'complete': True}}},
            {'snapshot_date': '2026-11-14', 'manifest_hash': 'stable',
             'rows': {'a': {'downloads_30d': 0, 'downloads_all_time': 0, 'complete': False}}},
            {'snapshot_date': '2026-11-15', 'manifest_hash': 'stable',
             'rows': {'a': {'downloads_30d': 110, 'downloads_all_time': 5000020, 'complete': True}}},
            {'snapshot_date': '2026-11-16', 'manifest_hash': 'stable',
             'rows': {'a': {'downloads_30d': 120, 'downloads_all_time': 5000030, 'complete': True}}},
        ]
        _, _, lifetime = org_totals_per_day(records, {'a': {'official_org': 'org'}})
        self.assertEqual(org_daily_deltas(records, lifetime)['org'], [None, None, None, 10])
        self.assertEqual(model_daily_delta_series(records, 'a')[1], [None, None, None, 10])

if __name__ == '__main__':
    unittest.main()
