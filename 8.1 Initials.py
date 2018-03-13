def main():
    name = input('Please type your first, middle, and last name. Then press ENTER.')
    name_list = name.split()
    print(name_list)
    first = name_list[0][0]
    middle = name_list[1][0]
    last = name_list[2][0]
    print(first.upper(),'.', middle.upper(),'.', last.upper())
main()
