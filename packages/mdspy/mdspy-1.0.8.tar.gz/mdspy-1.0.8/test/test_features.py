# -*- coding: utf-8 -*-

import unittest

from mdspy.data_creation import create_simple_data
from mdspy.features import fe_get_day_of_week, feature_creators


class Features_test(unittest.TestCase):
    """Basic test cases."""

    def test_feature_day_of_week(self):
        df = create_simple_data(10, 50, 0, timeseries=True)
        func_dow = fe_get_day_of_week('dow')
        run = feature_creators([func_dow], history_size=2)
        res = run(df)
        expected_shape = (9, 1)
        actual_shape = res.shape
        self.assertEqual(expected_shape, actual_shape)
        self.assertEqual(28, res['dow'].sum())
