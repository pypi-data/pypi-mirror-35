from os import path
from unittest import TestCase, mock

from requests.models import Response

import textmatcher


class MatchWebPageTest(TestCase):
    def setUp(self):
        web_page = path.abspath(path.join(path.dirname(__file__), 'data', 'difflib_python_3.6.6_docs.html'))
        with open(web_page, mode='r', encoding='ISO-8859-1') as fp:
            text_data = fp.read(-1)

        self.mock_response = mock.create_autospec(Response)
        self.mock_response.encoding = 'ISO-8859-1'
        self.mock_response.status_code = 200
        self.mock_response.headers = {'Content-Type': 'text/html'}
        self.mock_response.text = text_data

    @mock.patch('textmatcher.program.requests.get')
    def test_exact_match(self, mock_get):
        text = "This is a class for comparing sequences of lines of text, and producing human-readable differences" \
               " or deltas. Differ uses SequenceMatcher both to compare sequences of lines, and to compare sequences" \
               " of characters within similar (near-matching) lines."

        mock_get.return_value = self.mock_response

        ratio = textmatcher.match('http://someurl.com', text)
        mock_get.assert_called()
        self.assertEqual(ratio, 1.0)

    @mock.patch('textmatcher.program.requests.get')
    def test_exact_match_weird_format(self, mock_get):
        """ Same paragraph as above but with unnecessary enters, tabs and spaces added """
        text = """
        This is a class  \t\t    for comparing sequences of lines of text, and producing human-readable differences
               or deltas. Differ\n uses SequenceMatcher both      to compare sequences of lines, and to compare sequences
               of characters within similar (near-matching) lines.
        """
        mock_get.return_value = self.mock_response

        ratio = textmatcher.match('http://someurl.com', text)
        mock_get.assert_called()
        self.assertEqual(ratio, 1.0)

    @mock.patch('textmatcher.program.requests.get')
    @mock.patch('textmatcher.program.exact_match')
    def test_percentage_match(self, mock_exact, mock_get):
        """
        From the ratio docstring:
        Where T is the total number of elements in both sequences, and
        M is the number of matches, this is 2.0*M / T.
        ---

        text = '012345'     len(6)
        line = '0123456789' len(10)

        2.0 * 6 / 16 = 0.75
        """
        text = "012345"
        mock_get.return_value = self.mock_response
        mock_exact.return_value = 0.0

        ratio = textmatcher.match('http://someurl.com', text)
        mock_get.assert_called()
        mock_exact.assert_called()
        self.assertEqual(ratio, 0.75)

    @mock.patch('textmatcher.program.requests.get')
    def test_no_match(self, mock_get):
        text = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed commodo ex eget nibh posuere, non condimentum 
        lectus scelerisque. Etiam ac viverra justo, sit amet placerat justo. Sed sed neque vitae velit egestas gravida 
        eu vitae tellus. Aenean id gravida ligula. Interdum et malesuada fames ac ante ipsum primis in faucibus. 
        Maecenas porttitor sit amet nibh a tincidunt. In dignissim turpis posuere, tincidunt ligula non, pellentesque 
        magna. Nulla et tincidunt est. Etiam in lacus id magna laoreet suscipit sit amet fermentum eros.
        """
        mock_get.return_value = self.mock_response

        ratio = textmatcher.match('http://someurl.com', text)
        mock_get.assert_called()
        self.assertEqual(ratio, 0.0)
