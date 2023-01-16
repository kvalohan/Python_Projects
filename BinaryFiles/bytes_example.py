# equation = bytes((207, 128, 114, 194, 178))

# The commented codes were for test purpose to test the function `os.path.getsize()`
# import os.path
#
# # path = 'C:/Users/Kenneth Alohan/Desktop/Post Graduation/Canadian Citizenship/Useful Link.txt'
# path = 'C:/Users/Kenneth Alohan/Desktop/Post Graduation/Canadian Citizenship'
# # path = 'Useful Link.txt'
# dir_name = os.path.getsize(path)
# print(dir_name)

equation = b'\xcf\x80r\xc2\xb2'
print(equation)
print(type(equation))
print(len(equation))

for b in equation:
    print(b, end=', ')

print()
print(equation.decode('utf-8'))