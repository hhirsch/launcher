import unittest
from config import Config

class TestConfig(unittest.TestCase):

    def test_hasValue(self):
        config = Config()
        config.setValue("foo", "bar")
        self.assertTrue(config.hasValue("foo"))

    def test_hasNotValue(self):
        config = Config()
        config.setValue("foo", "bar")
        self.assertFalse(config.hasValue("baz"))
        
if __name__ == '__main__':
    unittest.main()
