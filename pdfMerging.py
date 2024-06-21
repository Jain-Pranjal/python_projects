from pypdf import PdfReader,PdfWriter

reader = PdfReader("2.pdf")
print (reader.pages[0].extract_text())   # this will extract the text from the first page of the pdf file

for i in range(len(reader.pages)):
    print(reader.pages[i].extract_text())
# here we can extract the text from the pdf file from iterating from all the pages of the pdf file


# for writing the extracted text into the file 
with open("sample.txt","w") as file:
    for i in range(len(reader.pages)):
        file.write(reader.pages[i].extract_text())


# for merging the pdf files
merger = PdfWriter()
for pdf in ["1.pdf", "2.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
