import os
from cStringIO import StringIO

from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import TextConverter

from emplocity import BIN_DIR

# If file is in root directory put only file name
default_pdf_file_path = os.path.join(BIN_DIR, 'page-1.pdf')


def parse_pdf(file_path=default_pdf_file_path):
    manager = PDFResourceManager()
    string = StringIO()
    codec = 'utf-8'
    params = LAParams()
    device = TextConverter(manager, string, codec=codec, laparams=params)
    pdf_file = file(file_path, 'rb')
    interpreter = PDFPageInterpreter(manager, device)
    password = ""
    caching = True
    pagenos = set()
    pages = 0

    for page in PDFPage.get_pages(pdf_file, pagenos, maxpages=0,
                                  password=password,caching=caching,
                                  check_extractable=True):
        pages += 1
        interpreter.process_page(page)

    data = string.getvalue()

    pdf_file.close()
    device.close()
    string.close()

    characters = len(data)
    words = len(data.split())
    lines = len(data.split('\n'))

    return {
        'name': file_path,
        'pages': pages,
        'data': data,
        'characters': characters,
        'words': words,
        'lines': lines
    }
