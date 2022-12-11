# --------------------------------------------------------------------------------------------------------

# Interactions with ChatGPT to write the script. 
# Questions are asked in segments to get what I need and, I modified it to produce a complete script.

# FIRST QUESTION:
# "Write me a Python code to parse a text data from a pdf."

# --------------------------------------------------------------------------------------------------------

# Import the required libraries
import os
import PyPDF2

# Set the path to the PDF file
pdf_file_path = 'sample_twitter_invoice.pdf'

# Open the PDF file in read-binary mode
with open(pdf_file_path, 'rb') as f:
    # Create a PyPDF2 reader object
    reader = PyPDF2.PdfFileReader(f)
    
    # Loop through all pages of the PDF
    for page in range(reader.numPages):
        # Get the page object
        page_obj = reader.getPage(page)
        
        # Extract the text from the page
        page_text = page_obj.extractText()
        
        # Print the page text
        print(page_text)
        
# Check what the return type is.
print(type(page_text))

# --------------------------------------------------------------------------------------------------------

# SECOND QUESTION:
# "What is the regex to capture #33333333 and $33.00?"

# THIRD QUESTION:
# "How to append a row to a Pandas DataFrame in Python using .concat() method?"

# --------------------------------------------------------------------------------------------------------

import re
import pandas as pd

# The text to search
page_text

# Compile the regular expression
pattern = re.compile(r"#(\d+) \$(\d+\.\d+)")

# Search for matches in the text
matches = pattern.finditer(page_text)

# Create a Pandas DataFrame
df = pd.DataFrame(columns=["campaign_id", "amount"])

# Loop through all matches
for match in matches:
    # Store the captured values in the Pandas DataFrame.
    # This is the part where I modified from the answer from the third question, combined with 2nd question.
    new_row = {"campaign_id": match.group(1), "amount": match.group(2)}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

# Print the updated DataFrame
print(df)

# --------------------------------------------------------------------------------------------------------
