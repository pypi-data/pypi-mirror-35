from os import path
from unittest import TestCase, mock

from requests.models import Response

import textmatcher


class PDFMatchTest(TestCase):
    def setUp(self):
        self.mock_response = mock.create_autospec(Response)
        self.mock_response.encoding = None
        self.mock_response.status_code = 200
        self.mock_response.headers = {'Content-Type': 'application/pdf'}

        self.pdf_1500_words = path.abspath(path.join(path.dirname(__file__), 'data', '1500_words_pdf.pdf'))
        self.pdf_pdfminder_doc = path.abspath(path.join(path.dirname(__file__), 'data', 'pdfminer-docs.pdf'))

    @mock.patch('textmatcher.program.requests.get')
    def test_perfect_match(self, mock_get):
        text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras mollis luctus lacus, id tristique magna
vehicula in. Fusce vel neque a metus malesuada scelerisque sit amet auctor nibh. In luctus viverra
libero, malesuada cursus enim rhoncus a. Vivamus eu dictum augue, in dignissim elit. Phasellus
rhoncus rhoncus cursus. Quisque elementum erat in tempus placerat. Morbi arcu tortor, sodales eget
commodo eget, dictum in diam."""

        text_data = b''

        with open(self.pdf_1500_words, 'rb') as fp:
            text_data = fp.read(-1)

        self.mock_response.content = text_data
        mock_get.return_value = self.mock_response

        ratio = textmatcher.match('http://someurl.com', text)
        mock_get.assert_called()
        self.assertEqual(ratio, 1.0)

    @mock.patch('textmatcher.program.requests.get')
    def test_exact_match_weird_format(self, mock_get):
        """ Same paragraph as above but with unnecessary enters, tabs and spaces added """
        text = """   Lorem ipsum
         
           \n dolor sit amet, consectetur\t\t\t      adipiscing elit. Cras mollis luctus lacus, id tristique magna
vehicula in. Fusce vel neque a metus malesuada scelerisque sit amet auctor nibh. In luctus viverra
libero, malesuada\n\n cursus enim rhoncus a. Vivamus eu dictum augue, in dignissim elit. Phasellus
rhoncus rhoncus cursus.\t\t Quisque elementum erat in tempus placerat. Morbi arcu tortor, sodales eget
commodo eget, dictum in diam."""

        text_data = b''
        with open(self.pdf_1500_words, 'rb') as fp:
            text_data = fp.read(-1)

        self.mock_response.content = text_data
        mock_get.return_value = self.mock_response

        ratio = textmatcher.match('http://someurl.com', text)
        mock_get.assert_called()
        self.assertEqual(ratio, 1.0)

    @mock.patch('textmatcher.program.requests.get')
    @mock.patch('textmatcher.program.exact_match')
    def test_percentage_match(self, mock_match, mock_get):
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
        text_data = b''

        with open(self.pdf_1500_words, 'rb') as fp:
            text_data = fp.read(-1)

        self.mock_response.content = text_data
        mock_get.return_value = self.mock_response
        mock_match.return_value = False

        ratio = textmatcher.match('http://someurl.com', text)
        mock_get.assert_called()
        self.assertEqual(ratio, 0.75)

    @mock.patch('textmatcher.program.requests.get')
    def test_first_line_of_multiple_paragraphs_match(self, mock_get):
        text = """
        
        Donec consectetur sit amet turpis id suscipit.
        Cras nulla metus, egestas ut viverra sed, tempor vel neque.
        Proin suscipit, nunc in feugiat dignissim, lectus eros fringilla velit, sed semper ex purus id purus.
        Vestibulum accumsan dui sed sem convallis maximus.
        Phasellus et ante justo.
        Donec sapien urna, condimentum vel congue ut, finibus in leo.
        """
        text_data = b''

        with open(self.pdf_1500_words, 'rb') as fp:
            text_data = fp.read(-1)

        self.mock_response.content = text_data
        mock_get.return_value = self.mock_response

        ratio = textmatcher.match('http://someurl.com', text)
        mock_get.assert_called()
        self.assertGreaterEqual(ratio, 0.95)
        self.assertLessEqual(ratio, 1.00)

    @mock.patch('textmatcher.program.requests.get')
    def test_no_match(self, mock_get):
        text = """This text should not be in the PDF. The result will 0.0, unless.. this text is within the PDF-Document.
        """
        text_data = b''

        with open(self.pdf_1500_words, 'rb') as fp:
            text_data = fp.read(-1)

        self.mock_response.content = text_data
        mock_get.return_value = self.mock_response

        ratio = textmatcher.match('http://someurl.com', text)
        mock_get.assert_called()
        self.assertEqual(ratio, 0.0)

    @mock.patch('textmatcher.program.requests.get')
    def test_text_with_block_match(self, mock_get):
        """ This part of text resides within a 'text' block"""
        text = """mkdir pdfminer\cmap
python tools\conv_cmap.py -c B5=cp950 -c UniCNS-UTF8=utf-8 pdfminer\cmap
˓ → Adobe-CNS1 cmaprsrc\cid2code_Adobe_CNS1.txt"""
        text_data = b''

        with open(self.pdf_pdfminder_doc, 'rb') as fp:
            text_data = fp.read(-1)

        self.mock_response.content = text_data
        mock_get.return_value = self.mock_response

        ratio = textmatcher.match('http://someurl.com', text)
        mock_get.assert_called()
        self.assertGreaterEqual(ratio, .89)

    @mock.patch('textmatcher.program.requests.get')
    def test_text_different_format_match(self, mock_get):
        """ Within the PDF(pdfminer-docs) this text has a different styling format """
        text = "-o filename"
        text_data = b''

        with open(self.pdf_pdfminder_doc, 'rb') as fp:
            text_data = fp.read(-1)

        self.mock_response.content = text_data
        mock_get.return_value = self.mock_response

        ratio = textmatcher.match('http://someurl.com', text)
        mock_get.assert_called()
        self.assertEqual(ratio, 1.0)

    @mock.patch('textmatcher.program.requests.get')
    def test_text_list_item_match(self, mock_get):
        """ This line is part of a list within the PDF(pdfminer-docs) """
        text = "• exact : preserve the exact location of each individual character (a large and messy HTML)."
        text_data = b''

        with open(self.pdf_pdfminder_doc, 'rb') as fp:
            text_data = fp.read(-1)

        self.mock_response.content = text_data
        mock_get.return_value = self.mock_response

        ratio = textmatcher.match('http://someurl.com', text)
        mock_get.assert_called()
        self.assertEqual(ratio, 1.0)
