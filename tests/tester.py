import unittest
import os
from app.hwinfo_analyze import main

class MainTestCase(unittest.TestCase):
    """Test if the analyzer works without fails."""

    def test_ALL_THE_CSVS(self):
        """Test all the csv files."""
        for csv in os.listdir("testfiles"):
            main(os.path.join("testfiles", csv))



unittest.main()
