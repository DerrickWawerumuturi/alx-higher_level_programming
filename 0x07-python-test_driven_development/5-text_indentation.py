#!/usr/bin/python3
"""
defines a function
"""
def text_indentation(text):
    """
    defines a function that splits  a string
    purpose: prints a text with 2 new lines 
    after each of these characters: ., ? and :
    
    Parameter: 
    text: stirng to be split
    
    Exception:
    
    TypeError: if text is not a string
    """
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    split_text  = ""
    
    newline_char = {'.', '?', ':'}
    
    for char in text:
        split_text += char
        
        if char in newline_char:
            split_text += '\n\n'
            
    lines = [lines.strip() for line in split_text('\n')]
    
    for line in lines:
        print(line)
