import PyPDF2
import sys
import glob
#your path in Windows or Mac
pdfs = glob.glob('Your Path/*.pdf')
inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    marger = PyPDF2.PdfFileMerger()
    for pdf in pdfs:
      marger.append(pdf)
    marger.write('New.pdf')

pdf_combiner(inputs)
