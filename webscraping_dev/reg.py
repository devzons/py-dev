import re

p = re.compile("ca.e")

def print_match(m):
    if m:
        print("m.group(): ", m.group())
        print("m.string: ", m.string)
        print("m.start(): ", m.start())
        print("m.end(): ", m.end())
        print("m.span(): ", m.span())
    else:
        print("Not matched")

# m = p.match("careful")
# print_match(m)

# m = p.search("good care")
# print_match(m)

# lst = p.findall("good care cafe")
# print(lst)
