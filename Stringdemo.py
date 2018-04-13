quote_1 = 'single quoted'
quote_2 = "double quoted"
print(quote_1, quote_2)
why_1 = 'She said,"Hello!"'
why_2 = "It's mine!"
print(why_1, why_2)
why_not_1 = "She said, \"Hello!\""
why_not_2 = 'It\'s mine!'
print(why_not_1, why_not_1)
# Special escape sequences exist
new_line = 'line1\nline2\nline3\n'
print(new_line)
tab_char = 'col1\tcol2\tcol3\t'
print(tab_char)
backslash = 'the backslash: \\'
print(backslash)
# Raw strings prevent escape sequence interpretation
raw_new_line = r'line1\nline2\nline3\n'
print(raw_new_line)
raw_tab_char = r'col1\tcol2\tcol3\t'
print(raw_tab_char)
raw_backslash = r'the backslash: \\'
print(raw_backslash)
# Sequence Objects can use several operators and functions
sub_text = 'double'
print('sub_text =', sub_text)
print(sub_text + sub_text)
print(' ' * 40)
print('len(sub_text) returns', len(sub_text))
print('min(sub_text) returns', min(sub_text))
print('max(sub_text) returns', max(sub_text))
print('sub text not in quote_1 returns', sub_text not in quote_1)
print('sub text in quote_2', sub_text in quote_2)
# String objects have many available methods like:
print('why_1.count("e") returns', why_1.count('e'))
print('why_1.index("e") returns', why_1.index('e'))
print('why_1.index("e",3,18) returns', why_1.index('e', 3, 18))
print('why_1.find("X") returns', why_1.find('X'))
print('why_1.startswith("She") returns', why_1.startswith("She"))
print('why_1.endswith("!\\"") returns', why_1.endswith("!\""))
print('why_1.lower() returns', why_1.lower())
print('why_1.upper() returns', why_1.upper())
csv = 'a,b,c'
print('csv.split(",") returns', csv.split(","))
print('",".join(["a", "b", "c"])', ",".join(["a", "b", "c"]))
print('sub_text.isalpha() returns', sub_text.isalpha())
print('sub_text.isdigit() returns', sub_text.isdigit())


# *************

s1 = "Py" + 'thon'
print(s1)
s2 = 'Python is amazing'
print(s2)
s3 = r'Python\nis\namazing'
print(s3)
s4 = r'Python\tis\tamazing'
print(s4)

print(s2)
rs1 = r'Python\nis\namazing'
print(rs1)
rs2 = r'Python\tis\tamazing'
print(rs2)
s = 'INfinity'
print('check if \'s\' has only alphabets', s.isalpha())
print('check if \'s\' has only digits', s.isdigit())
print('determine the length of \'s\'', len(s))
print('Convert all characters of \'s\' into upper case', s.upper())
print('Convert all characters of \'s\' into lower case', s.lower())
print('find how many \'i\' s are there in \'s\'', s.count('i'))
print('find the index position of character \'t\' in s', s.index('t'))

s = 'INfinity'
print(s.isalpha())
print(s.isdigit())
print(len(s))
print(s.upper())
print(s.lower())
print(s.count('i'))
print(s.index('t'))

s = 'INfinity'
s1 = s.isalpha()
s2 = s.isdigit()
s3 = len(s)
s4 = s.upper()
s5 = s.lower()
s6 = s.count('i')
s7 = s.index('t')

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)
print(s7)


