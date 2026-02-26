import unittest
import matplotlib
import sea_level_predictor as slp


class TestSeaLevelPredictor(unittest.TestCase):

    def test_draw_plot(self):
        fig = slp.draw_plot()
        self.assertIsInstance(fig, matplotlib.figure.Figure)


if __name__ == "__main__":
    unittest.main()