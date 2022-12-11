# --------------------------------------------------------------------------------------------------------

# Interactions with ChatGPT to write the script. 
# Questions are asked in parts to get what I need, and small modifications made to produce a complete script.

# FIRST QUESTION:
# "Write me a Python code to parse a text data from a pdf."

# FOURTH QUESTION (for update):
# "How to merge a list of string into one string variable?"

# --------------------------------------------------------------------------------------------------------
# Import the required libraries
import os
import PyPDF2

# Set the path to the PDF file with multiple pages merged into one.
pdf_file = 'Binder1.pdf'

# Create a list to store text data from each page as an element.
list_of_text =[]

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
        list_of_text.append(page_text)

# Check the type
type(pages_text[0]) # the index 0 element is a type of string

# Join the string elements into one string variable. Related to Q4.
pages_text = ' '.join(list_of_text)

# --------------------------------------------------------------------------------------------------------

# SECOND QUESTION:
# "What is the regex to capture #33333333 and $33.00?"

# THIRD QUESTION:
# "How to append a row to a Pandas DataFrame in Python using .concat() method?"

# --------------------------------------------------------------------------------------------------------

import re
import pandas as pd

# The text to search
pages_text

# Compile the regular expression
pattern = re.compile(r"#(\d+) \$(\d+\.\d+)")

# Search for matches in the text
matches = pattern.finditer(pages_text)

# Create a Pandas DataFrame
df = pd.DataFrame(columns=["campaign_id", "amount"])

# Loop through all matches
for match in matches: 
    # Print the captured values 
    new_row = {"campaign_id": match.group(1), "amount": match.group(2)}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

# Print the updated DataFrame
print(df)

# --------------------------------------------------------------------------------------------------------
