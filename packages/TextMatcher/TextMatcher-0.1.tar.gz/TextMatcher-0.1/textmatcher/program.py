import difflib
import re
from io import BytesIO, StringIO

import requests
from bs4 import BeautifulSoup
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage


def pdf_to_text(file_data):
    text_data = ''
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    codec = 'utf-8'
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    with BytesIO(file_data) as bp:
        for page in PDFPage.get_pages(bp):
            interpreter.process_page(page)

        text_data = retstr.getvalue()

    return text_data


def get_text_data(url):
    """ Retrieve data in a text format from a given url """
    response = requests.get(url)

    if response.headers['Content-Type'] == 'application/pdf':
        text_data = pdf_to_text(response.content)
    elif response.headers['Content-Type'] == 'text/html':
        soup = BeautifulSoup(response.text.encode(encoding=response.encoding), 'html.parser')
        text_data = soup.get_text()
    else:
        raise NotImplementedError('There is no implementation for {}!'.format(response.headers['Content-Type']))

    return text_data


def make_single_line(text):
    """ Replaces newlines, spaces and tabs with a single space """
    return re.sub(r'[\n\s\t]+', ' ', text).strip()


def exact_match(single_line, single_line_compare):
    """
    Look for an exact match within the compare parameter
    @:return: Boolean value indicating a match was found or not.
    """
    # Text could contain characters that are used for regex patterns
    pattern = re.escape(single_line)
    matches = re.search(pattern, single_line_compare)

    if matches:
        return True

    return False


def diff_lines_match(single_line, single_line_compare):
    """
    Construct a SequenceMatcher out the single line and a blob that has been constructed out the closest matches
    between single_line and single_line_compare.
    Both parameters are split up in a list by using the dot as separator.

    @:param single_line: A string that will be the seq1 of the SequenceMatcher
    @:param single_line_compare: Another string used to construct a blob which will become seq2 of SequenceMatcher
    @:return: A SequenceMatcher(single_line, blob)
    """

    text_lines = single_line.split('.')
    data_lines = single_line_compare.split('.')
    close_matches = []
    for line in text_lines:
        if line:
            close_matches.extend(difflib.get_close_matches(line, data_lines, n=1))

    blob = "".join(close_matches).strip()

    return difflib.SequenceMatcher(None, single_line, blob)


def match(url, text):
    """
    Extract data from an web-page or PDF-document and match it with the given text parameter

    @param url: An URL to a web-page or PDF-document.
    @param text: The text to find.
    @return: A `float` between 0 and 1, indicating the matching percentage
    """
    text_data = get_text_data(url)

    single_line_text = make_single_line(text)
    single_line_data = make_single_line(text_data)

    if exact_match(single_line_text, single_line_data):
        return 1

    return diff_lines_match(single_line_text, single_line_data).ratio()
