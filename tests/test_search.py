import unittest
from unittest.mock import patch, MagicMock
import sys
import json
import os

# Add parent directory to path to import search.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import search

class TestFlightSearch(unittest.TestCase):

    @patch('search.get_flights')
    def test_search_output(self, mock_get_flights):
        # Mock the Result object
        mock_result = MagicMock()
        mock_result.current_price = "low"
        
        # Mock Flight object
        mock_flight = MagicMock()
        mock_flight.name = "Delta"
        mock_flight.price = "$100"
        mock_flight.duration = "5h"
        mock_flight.departure = "10:00 AM"
        mock_flight.arrival = "3:00 PM"
        mock_flight.stops = 0
        
        mock_result.flights = [mock_flight]
        mock_get_flights.return_value = mock_result
        
        # Capture stdout
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Run main with args
        sys.argv = ['search.py', 'SFO', 'JFK', '2026-03-01']
        search.main()
        
        sys.stdout = sys.__stdout__
        
        # Verify JSON
        output = json.loads(captured_output.getvalue())
        self.assertEqual(output['current_price'], "low")
        self.assertEqual(output['flights'][0]['name'], "Delta")
        self.assertEqual(len(output['flights']), 1)

    def test_missing_args(self):
        sys.argv = ['search.py']
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output
        
        search.main()
        sys.stdout = sys.__stdout__
        
        output = json.loads(captured_output.getvalue())
        self.assertIn("error", output)
        self.assertIn("Usage", output['error'])

if __name__ == '__main__':
    unittest.main()
