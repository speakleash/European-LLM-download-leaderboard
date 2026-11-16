import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from render_timeseries_charts import org_daily_deltas, org_totals_per_day


class OrganizationHistoryTests(unittest.TestCase):
    def test_late_publisher_has_gaps_and_no_false_first_day_growth(self):
        records = [
            {'snapshot_date': '2026-11-14', 'rows': {'a': {'downloads_30d': 10, 'downloads_all_time': 100}}},
            {'snapshot_date': '2026-11-15', 'rows': {'a': {'downloads_30d': 12, 'downloads_all_time': 110},
                                                  'b': {'downloads_30d': 500, 'downloads_all_time': 10000}}},
            {'snapshot_date': '2026-11-16', 'rows': {'a': {'downloads_30d': 13, 'downloads_all_time': 120},
                                                  'b': {'downloads_30d': 505, 'downloads_all_time': 10007}}},
        ]
        dates, rolling, lifetime = org_totals_per_day(records, {'a': {'official_org': 'old'}, 'b': {'official_org': 'new'}})
        self.assertEqual(len(dates), 3)
        self.assertEqual(rolling['new'], [None, 500, 505])
        self.assertEqual(lifetime['new'], [None, 10000, 10007])
        self.assertEqual(org_daily_deltas(dates, lifetime)['new'], [None, None, 7])
        self.assertEqual(org_daily_deltas(dates, lifetime)['old'], [None, 10, 10])

    def test_gap_resets_daily_comparison_but_zero_is_a_measurement(self):
        records = [
            {'snapshot_date': '2026-11-13', 'rows': {'a': {'downloads_30d': 0, 'downloads_all_time': 0}}},
            {'snapshot_date': '2026-11-14', 'rows': {}},
            {'snapshot_date': '2026-11-15', 'rows': {'a': {'downloads_30d': 4, 'downloads_all_time': 30}}},
            {'snapshot_date': '2026-11-16', 'rows': {'a': {'downloads_30d': 8, 'downloads_all_time': 34}}},
        ]
        dates, rolling, lifetime = org_totals_per_day(records, {'a': {'official_org': 'org'}})
        self.assertEqual(rolling['org'], [0, None, 4, 8])
        self.assertEqual(org_daily_deltas(dates, lifetime)['org'], [None, None, None, 4])

if __name__ == '__main__':
    unittest.main()
