import PyPDF2
import os

# Enter your pdf file name here:
current_path = os.getcwd()
output_path = current_path + "\\outputfiles"
pdf_file_names = (
    "scklm19_fm.pdf",
    "scklm18_fm.pdf",
    "scklm16_fm.pdf",
    "scklm14_fm.pdf",
)
output_files = (
    "Standard_Chartered_Marathon_2019_FM_Results.csv",
    "Standard_Chartered_Marathon_2018_FM_Results.csv",
    "Standard_Chartered_Marathon_2016_FM_Results.csv",
    "Standard_Chartered_Marathon_2014_FM_Results.csv",
)

for pdf_file_name, output_file in zip(pdf_file_names, output_files):
    if pdf_file_name == "scklm14_fm.pdf":
        header_columns = 6
    else:
        header_columns = 7

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
            page_staging = page_staging[
                header_columns:
            ]  # Remove header if not the first page
        for x in page_staging:
            final_staging.append(
                x.strip()
            )  # Append to final staging, remove whitespace

    # Write list into .csv file specified as "output_file"
    os.chdir(output_path)
    write_to_file = open(output_file, "w")

    # Insert comma after every element, insert newline after every 7th element, then close file
    counter = 1
    for entry in final_staging:
        if counter != header_columns:
            entry = entry + ","
            counter += 1
        else:
            entry = entry + "\n"
            counter = 1
        write_to_file.write(entry)
    write_to_file.close()

    os.chdir(current_path)
