import unittest
from src.model.pipeline import DataPipeline

class TestPipeline(unittest.TestCase):
    def setUp(self):
        self.pipeline = DataPipeline()

    def test_pipeline(self):
        result = self.pipeline.run_pipeline('./data/sample.pdf')
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
