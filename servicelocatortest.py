import unittest
from lib.servicelocator import ServiceLocator

class ServiceLocatorTest(unittest.TestCase):

    def test_has_service(self):
        serviceLocator = ServiceLocator()
        serviceLocator.testKey = "key"
        self.assertTrue(serviceLocator.hasService('testKey'))

if __name__ == '__main__':
    unittest.main()
