import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.state import State
from models.place import Place

class TestConsole(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_with_params(self, mock_stdout):
        """Test create command with parameters."""
        hbnb_command = HBNBCommand()

        hbnb_command.onecmd('create State name="California"')
        result = mock_stdout.getvalue().strip()
        self.assertIsInstance(storage.all()["State." + result], State)
        self.assertEqual(storage.all()["State." + result].name, "California")

        hbnb_command.onecmd('create State name="Arizona"')
        result = mock_stdout.getvalue().strip()
        self.assertIsInstance(storage.all()["State." + result], State)
        self.assertEqual(storage.all()["State." + result].name, "Arizona")

        hbnb_command.onecmd('all State')
        result = mock_stdout.getvalue().strip()
        self.assertIn("'name': 'California'", result)
        self.assertIn("'name': 'Arizona'", result)

        hbnb_command.onecmd('create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
        result = mock_stdout.getvalue().strip()
        self.assertIsInstance(storage.all()["Place." + result], Place)
        self.assertEqual(storage.all()["Place." + result].name, "My little house")
        self.assertEqual(storage.all()["Place." + result].number_rooms, 4)

        hbnb_command.onecmd('all Place')
        result = mock_stdout.getvalue().strip()
        self.assertIn("'name': 'My little house'", result)
        self.assertIn("'number_rooms': 4", result)
        self.assertIn("'number_bathrooms': 2", result)
        self.assertIn("'max_guest': 10", result)
        self.assertIn("'price_by_night': 300", result)
        self.assertIn("'latitude': 37.773972", result)
        self.assertIn("'longitude': -122.431297", result)

if __name__ == '__main__':
    unittest.main()

