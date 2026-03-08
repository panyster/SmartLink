# test_smartlink.py
"""
Tests for SmartLink module.
"""

import unittest
from smartlink import SmartLink

class TestSmartLink(unittest.TestCase):
    """Test cases for SmartLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SmartLink()
        self.assertIsInstance(instance, SmartLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SmartLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
