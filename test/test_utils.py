import unittest
from src.utils import read_data, process_data

class TestUtils(unittest.TestCase):
    
    def test_read_data(self):
        data = read_data("src/data.txt")
        self.assertEqual(data, "Sample data in a text file.\n")
    
    def test_process_data(self):
        data = "Sample data in a text file."
        processed_data = process_data(data)
        self.assertEqual(processed_data, ["Sample", "data", "in", "a", "text", "file."])

if __name__ == "__main__":
    unittest.main()
