import rstviewer
import tempfile
import unittest
from unittest.mock import patch

class TestRstViewer(unittest.TestCase):
    @patch('webbrowser.open')
    def _run_viewer(self):
        with patch(sys, 'argv', [self._f.name]):
            rstviewer.main()

    def setUp(self):
        self._f = tempfile.NamedTemporaryFile(delete=False)
        
    def test_launch(self):
        self._run_viewer()


if __name__ == "__main__":
    unittest.main()
