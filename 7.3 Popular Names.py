def main():
    input_file = open('BoyNames.txt', 'r')
    record = input_file.readline()
    record = record.rstrip('\n')
    while record != "":
        print(record)
        record = input_file.readline()
        record = record.rstrip('\n-------|-------')
    input_file.close()
main()
def line_count():
    print(line_count('BoyNames.txt'))

def main():
    input_file = open('GirlNames.txt', 'r')
    record = input_file.readline()
    record = record.rstrip('\n-------|-------')
    while record != "":
        print(record)
        record = input_file.readline()
        record = record.rstrip('\n')
    input_file.close()
main()
def line_count():
    print(line_count('GirlNames.txt'))
