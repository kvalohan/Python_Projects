import shelve
# print(dir())
# # print(dir(__builtins__))
#
# for funct in dir(__builtins__):
#     print(funct)

print(dir())
print()
print(dir(shelve))

for obj in dir(shelve.Shelf):
    if obj[0] != '_':
        print(obj)
    else:
        print(obj)