import re
def validate_password(password):
    pattern = r"""
        ^                       # start of string
        (?=.*[A-Z])             # at least one uppercase letter
        (?=.*[a-z])             # at least one lowercase letter
        (?=.*\d)                # at least one digit
        (?=.*[@$!%*?&])         # at least one special character
        .{8,}                   # minimum 8 characters
        $                       # end of string
    """

    if re.match(pattern, password, re.VERBOSE):
        print("Password is STRONG")
    else:
        print("Password is WEAK")

#re.IGNORECASE
text = """Python is powerful.
PYTHON is easy.
python is popular.
"""
pattern_ignore = r"python"
matches = re.findall(pattern_ignore, text, re.IGNORECASE)
print("Matches with IGNORECASE:", matches)

#re.MULTILINE
pattern_multiline = r"^python"
matches = re.findall(pattern_multiline, text, re.IGNORECASE | re.MULTILINE)
print("Matches with MULTILINE:", matches)

#re.DOTALL
dot_text = "Python\nProgramming"
pattern_dotall = r"Python.*Programming"
match = re.search(pattern_dotall, dot_text)
print("Without DOTALL:", match)

match = re.search(pattern_dotall, dot_text, re.DOTALL)
print("With DOTALL:", match.group())