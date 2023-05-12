import unittest
import methods
import pandas as pd
from pandas.testing import assert_frame_equal

import os

test_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(test_dir)


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.data = methods.get_data()

    def test_get_categories(self):
        expected = ['Clothing', 'Entertainment', 'Food', 'Gas', 'Other', 'Rent']
        actual = methods.get_categories(self.data)
        actual.sort()  # sort the actual list of categories
        self.assertEqual(actual, expected)

    def test_get_category_data(self):
        self.assertEqual(methods.get_category_data(self.data, 'Food').shape, (5, 4))

    def test_get_category_totals(self):
        self.assertEqual(methods.get_category_totals(self.data).loc['Food', 'Amount'], 100.0)

    def test_get_category_averages(self):
        expected_df = pd.DataFrame(
            {'Average Amount': [40.0, 35.0, 20.0, 55.0, 15.0, 500.0], 'Transaction Count': [2, 2, 5, 2, 2, 2]},
            index=['Clothing', 'Entertainment', 'Food', 'Gas', 'Other', 'Rent'],
        )
        expected_df = expected_df.rename_axis('Category')

        actual_df = methods.get_category_averages(self.data).set_index('Category')
        # print(expected_df)
        # print(actual_df)
        assert_frame_equal(expected_df, actual_df)

    def test_get_category_counts(self):
        self.assertEqual(methods.get_category_counts(self.data).loc['Food', 'Amount'], 5)

    def test_get_category_stats(self):
        self.assertEqual(methods.get_category_stats(self.data).loc['Food', 'Amount'], 100.0)
        self.assertEqual(methods.get_category_stats(self.data).loc['Food', 'Amount_x'], 20.0)
        self.assertEqual(methods.get_category_stats(self.data).loc['Food', 'Amount_y'], 5)

    def test_get_category_stats_by_month(self):
        a = methods.get_category_stats_by_month(self.data)

        self.assertEqual(a.loc[2018,1,"Clothing"][0], 50.0)
        self.assertEqual(a.loc[2018, 1, "Clothing"][1], 50.0)
        self.assertEqual(a.loc[2018, 1, "Clothing"][2], 1.0)

        self.assertEqual(a.loc[2018, 2, "Food"][0], 50.0)
        self.assertEqual(a.loc[2018, 2, "Food"][1], 16.666666666666668)
        self.assertEqual(a.loc[2018, 2, "Food"][2], 3.0)

    def test_get_category_stats_by_year(self):
        a = methods.get_category_stats_by_year(self.data)

        self.assertEqual(a.loc[0,"Amount"], 80.0)
        self.assertEqual(a.loc[0, "Amount_x"], 40.0)
        self.assertEqual(a.loc[0, "Amount_y"], 2.0)

        self.assertEqual(a.loc[4, "Amount"], 30.0)
        self.assertEqual(a.loc[4, "Amount_x"], 15.0)
        self.assertEqual(a.loc[4, "Amount_y"], 2.0)


    def get_category_stats_by_month(data):
        gb = data.groupby(['Category', data['Date'].dt.month])
        return gb.agg({'Amount': 'sum', 'Amount': 'mean', 'Amount': 'count'}).rename(columns={'Amount': 'Total Amount'})

    def get_category_stats_by_year(data):
        gb = data.groupby(['Category', data['Date'].dt.year])
        return gb.agg({'Amount': 'sum', 'Amount': 'mean', 'Amount': 'count'}).rename(columns={'Amount': 'Total Amount'})

