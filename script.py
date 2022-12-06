import pdfplumber
import pandas as pd
import re

# The length variable of the current campaign ID for Twitter. 
LEN_OF_CAMP_ID_FOR_TWIITER = 8
# The document name variable.
document = 'sample_invoice_from_twitter.pdf'

# Open an invoice from Twitter Ads.
with pdfplumber.open(document) as pdf:
    text = []                               # an array to store the text values.
    for i in range(0, len(pdf.pages)):      # a for loop to iterate over the pages of the pdf.
        pages = pdf.pages[i]                # a variable declaration 
        text.append(pages.extract_text())   # extract text, using the .extract_text() method,
                                            # from the page and add it to the text array.
data = pd.DataFrame(text).values.tolist()   # create a pandas dataframe from the text array.

# Get the text string from the first page of the data extracted from the pdf.
text = data[0][0]
# Split the text string into list elements by row, '\n'.
list_of_rows = text.split('\n')

# Declare list to store camp_id.
camp_id_list = []
# Declare list to store amount.
amount_list = []

def create_df_with_camp_id_and_amount():
    
    global df
    
    # Empty the df in case there something already in it ? not sure if it works like that.
    df = pd.DataFrame()
    df = df.iloc[0:0]
    
    for row in list_of_rows:
        # If # and $ are in the same row, it is the row we want for the camp_id and amount extraction.
        if (('#' in row) & ('$' in row)):
            # Find the index of '#' in the row. 
            camp_id_idx = row.find('#')
            # Slice the row to get only camp_id and amount in the row, from the camp_id_idx to the end.
            camp_id_and_amount = row[camp_id_idx + 1 : ] # Expected returned string = "12345678  $100.00"
            # Remove white space characters, ' '. 
            camp_id_and_amount_trimmed1 = camp_id_and_amount.replace(' ', '') # Expected returned string = "12345678$100.00"
            # Split the string containing the camp_id and amount and store it in a list.
            camp_id_and_amount_trimmed2 = camp_id_and_amount_trimmed1.split('$') # Expected returned list = [12345678, 100.00]
            # Split and store the individual values from the list above. 
            camp_id = camp_id_and_amount_trimmed2[0]
            amount = camp_id_and_amount_trimmed2[1]
            # Store camp_id and amount seperately, type conversion to int & float.
            camp_id_list.append(int(camp_id))
            amount_list.append(float(amount))

    # Create a DataFrame object from the lists:[camp_id, amount] with columns: 'camp_id', 'amount' 
    df = pd.DataFrame({'camp_id': camp_id_list, 'amount': amount_list})
    
    
    # FOR FUTURE
    
    # Add columns [invoice_number, invoice_date, invoice_client, project_id].
    # Test it with a pdf with multiple pages where different invoices for different billing addresses are merged in one file.
