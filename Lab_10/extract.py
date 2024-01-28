import re

# Input string
input_string = "if (5)>v goto (345)"

# Regular expression pattern to extract text after 'goto'
pattern = r'goto\s*\(\s*(\d+)\s*\)'

# Using re.search() to find the pattern in the input string
match = re.search(pattern, input_string)

# Extracted number as a string
extracted_text = match.group(1) if match else None

# Remove parentheses and convert to an integer if needed
if extracted_text is not None:
    extracted_text = extracted_text.replace('(', '').replace(')', '')
    extracted_number = int(extracted_text)

print("Extracted number:", extracted_number)
