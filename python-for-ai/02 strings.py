'''
F Strings
    These are used to dynamically inject any information into 
    a string.
'''

content = 'F String'
string = f"Hello there, Now I am studying about {content}"


'''
Built-in String Function Types:
    - Case changing functions
    - Cleaning spaces
    - Find and Replace
'''
# Case changing functions
content.lower()
content.upper()
content.title()

# Cleaning spaces
content.strip()
content.rstrip()
content.lstrip()

# Find and Replace
content.startswith("F")
content.endswith("F")