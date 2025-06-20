Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> for word in ["apple", "orange", "kiwi"]:
...     　print(word, len(word))
...     
SyntaxError: invalid non-printable character U+3000
>>> for word in ["apple", "orange", "kiwi"]:
...     print(word, len(word))
... 
...     
