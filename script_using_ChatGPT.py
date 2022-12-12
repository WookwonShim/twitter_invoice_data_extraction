# Import the required libraries
import os
import PyPDF2

# Set the path to the PDF file with multiple pages merged into one.
pdf_file = 'Binder1.pdf'

# Create a list to store text data from each page as an element.
list_of_page_text =[]

# Open the PDF file in read-binary mode
with open(pdf_file, 'rb') as f:
    # Create a PyPDF2 reader object
    reader = PyPDF2.PdfFileReader(f)
    
    # Loop through all pages of the PDF
    for page in range(reader.numPages):
        # Get the page object
        page_obj = reader.getPage(page)
        
        # Extract the text from the page
        page_text = page_obj.extractText()
        list_of_page_text.append(page_text)
        
import re
import pandas as pd        
        
# to loop over each page
i = 0

# loop over list_of_page_text
for page_text in list_of_page_text:

    # regex pattern for an invoice #
    pattern1 = re.compile(r"\d{15}")     
    # regex pattern for a date
    pattern2 = re.compile(r"\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{1,2},\s+\d{4}\b") # match pattern for date
    # regex pattern to detect camp_id and amount
    pattern3 = re.compile(r"#(\d+) \$(\d+\.\d+)")

    # match object for the invoice # in the page
    match1 = re.search(pattern1, list_of_text[i])
    # match object for the date in the page
    match2 = re.search(pattern2, list_of_text[i])
    # match object for camp_id and amount
    matches3 = pattern3.finditer(list_of_text[i])

    # variables to store invoice number and date.
    invoice_number = str(match1.group(0))
    invoice_date = str(match2.group(0))

    # loop over matches3
    for match in matches3:
    
        new_row = {"invoice_number": invoice_number, 
                   "invoice_date": invoice_date, 
                   "campaign_id": match.group(1), 
                   "amount": match.group(2)}

        # add a row to the DataFrame
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    # inrement
    i += 1

