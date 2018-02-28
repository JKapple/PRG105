def main():
    input_file = open('names.txt', 'r')
    record = input_file.readline()
    record = record.rstrip('\n')
    while record != "":
        print(record)
        record = input_file.readline()
        record = record.rstrip('\n')
    input_file.close()
main()
def line_count():
    print(line_count('names.txt'))








