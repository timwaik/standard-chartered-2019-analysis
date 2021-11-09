import PyPDF2

# Enter your pdf file name here:
pdf_file_name = "scklm18_fm.pdf"
output_file = "Standard_Chartered_Marathon_2018_FM_Results.csv"

# Open file and pass to PdfFileReader function
pdf_file = open(pdf_file_name, "rb")
pdfreader = PyPDF2.PdfFileReader(pdf_file)

# Gets number of pages in the pdf
number_of_pages = pdfreader.numPages

# Parse text information in the PDF page by page, splits each line into a list
final_staging = []
for page in range(number_of_pages):
    pdf_page = pdfreader.getPage(page)
    page_staging = pdf_page.extractText().splitlines()
    if page != 0:
        page_staging = page_staging[7:]  # Remove header if not the first page
    for x in page_staging:
        final_staging.append(x.strip())  # Append to final staging, remove whitespace

# Write list into .txt file specified as "output_file"
write_to_file = open(output_file, "w")

# Insert comma after every element, insert newline after every 7th element, then close file
counter = 1
for entry in final_staging:
    if counter != 7:
        entry = entry + ","
        counter += 1
    else:
        entry = entry + "\n"
        counter = 1
    write_to_file.write(entry)
write_to_file.close()
