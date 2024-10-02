# test_pascal_triangle.py

import unittest
import importlib.util
import sys

# Dynamically load the module
module_name = "0-pascal_triangle"
file_path = "./0-pascal_triangle.py"  # Adjust the path if necessary

spec = importlib.util.spec_from_file_location(module_name, file_path)
pascal_module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = pascal_module
spec.loader.exec_module(pascal_module)

# Now you can access the pascal_triangle function
pascal_triangle = pascal_module.pascal_triangle

class TestPascalTriangle(unittest.TestCase):
    
    def test_zero(self):
        self.assertEqual(pascal_triangle(0), [])
    
    def test_one(self):
        self.assertEqual(pascal_triangle(1), [[1]])
    
    def test_two(self):
        self.assertEqual(pascal_triangle(2), [[1], [1, 1]])
    
    def test_three(self):
        self.assertEqual(pascal_triangle(3), [[1], [1, 1], [1, 2, 1]])
    
    def test_four(self):
        self.assertEqual(pascal_triangle(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])
    
    def test_five(self):
        self.assertEqual(pascal_triangle(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])

if __name__ == '__main__':
    unittest.main()
