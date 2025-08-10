import unittest
import sys
from unittest.mock import patch, MagicMock, call
import pandas as pd
import numpy as np
import os

# Import the refactored script to test its functions
import statistical_exploration as se

class TestStatisticalExploration(unittest.TestCase):

    def setUp(self):
        """Set up a sample DataFrame for use in all tests."""
        self.sample_data = {
            'popularity': [10, 20, 80, 90, 15, 25, 85, 95],
            'explicit':   [0,  0,  1,  1,  0,  0,  1,  1],
            'energy':     [0.2, 0.3, 0.8, 0.9, 0.25, 0.35, 0.85, 0.95],
            'mood_cluster': ['Calm', 'Calm', 'Energetic', 'Energetic', 'Sad', 'Sad', 'Happy', 'Happy'],
            'danceability': [0.1, 0.2, 0.8, 0.9, 0.15, 0.25, 0.85, 0.95],
            'valence':    [0.1, 0.2, 0.8, 0.9, 0.11, 0.22, 0.88, 0.99]
        }
        self.df = pd.DataFrame(self.sample_data)

    @patch('builtins.print')
    def test_perform_t_test(self, mock_print):
        """
        Test the t-test function with data where a significant difference is expected.
        """
        # In our sample data, explicit songs (mean pop ~87.5) are much more popular
        # than non-explicit songs (mean pop ~17.5).
        t_stat, p_value = se.perform_t_test(self.df)
        sys.stdout.flush() # Flush stdout to ensure all prints are captured by mock_print

        self.assertLess(p_value, 0.05, "P-value should be significant for this sample data.")
        self.assertGreater(t_stat, 0, "T-statistic should be positive as explicit group mean is higher.")
        # Check that the correct conclusion was printed
        mock_print.assert_any_call("Result: Reject the null hypothesis. The difference is statistically significant.")

    @patch('builtins.print')
    def test_perform_anova(self, mock_print):
        """
        Test the ANOVA function with data where a significant difference is expected.
        """
        # The 'energy' values are clearly different across the 'mood_cluster' groups.
        f_stat, p_value = se.perform_anova(self.df)

        sys.stdout.flush() # Flush stdout to ensure all prints are captured by mock_print
        self.assertLess(p_value, 0.05, "P-value should be significant for this sample data.")
        mock_print.assert_any_call("Result: Reject the null hypothesis. A significant difference exists.")

    @patch('matplotlib.pyplot.savefig')
    @patch('matplotlib.pyplot.close')
    @patch('os.makedirs')
    @patch('builtins.print')
    def test_perform_correlation_test(self, mock_print, mock_makedirs, mock_close, mock_savefig):
        """
        Test the correlation function with highly correlated data.
        """
        # 'danceability' and 'valence' are almost perfectly correlated in our sample data.
        r_value, p_value = se.perform_correlation_test(self.df, output_dir='test_outputs')

        sys.stdout.flush() # Flush stdout to ensure all prints are captured by mock_print
        self.assertAlmostEqual(r_value, 1.0, places=2, msg="Correlation coefficient should be close to 1.")
        self.assertLess(p_value, 0.05, "P-value should be significant for this sample data.")
        mock_savefig.assert_called_once() # Verify that the plot saving was attempted.
        mock_print.assert_any_call("Result: Reject the null hypothesis. The correlation is statistically significant.")

    @patch('statistical_exploration.perform_correlation_test')
    @patch('statistical_exploration.perform_anova')
    @patch('statistical_exploration.perform_t_test')
    @patch('statistical_exploration.load_and_prepare_data')
    def test_main_flow(self, mock_load_data, mock_t_test, mock_anova, mock_corr_test):
        """
        Test the main function to ensure it orchestrates the calls correctly.
        """
        # We don't want to actually run the tests, just check they are called.
        mock_load_data.return_value = self.df

        se.main()

        mock_load_data.assert_called_once()
        mock_t_test.assert_called_once_with(self.df, 0.05)
        mock_anova.assert_called_once_with(self.df, 0.05)
        mock_corr_test.assert_called_once_with(self.df, 0.05, output_dir="analysis_outputs")

if __name__ == '__main__':
    unittest.main()
