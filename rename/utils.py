#!/usr/bin/env python3

from PyPDF2 import PdfFileReader
from slugify import slugify
import pdftotext


def extract_from_metadata(filename):
    try:
        pdf_toread = PdfFileReader(open(filename, "rb"))
    except:
        return
    pdf_info = pdf_toread.getDocumentInfo()

    name = pdf_info.get('/Title')
    if not name:
        return 

    new_name = slugify(name)

    if not new_name:
        return 

    if not new_name.endswith(".pdf"):
        new_name += ".pdf"
    return new_name


def extract_from_title(filename):
    with open(filename, "rb") as f:
        try:
            pdf = pdftotext.PDF(f)
        except:
            return

    try:
        text = pdf[0][:64].splitlines()[0]
        new_name = slugify(text)
        return new_name + ".pdf"
    except:
        return