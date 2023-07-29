#merging two pdf 

import PyPDF2
pdfiles=["C:\\Users\\pranj\\Documents\\python\\python_projects\\1.pdf","C:\\Users\\pranj\\Documents\\python\\python_projects\\2.pdf"]
merger=PyPDF2.PdfMerger()
for filename in pdfiles:
    pdfFile=open(filename,'rb')
    pdfReader=PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write("merged.pdf")








