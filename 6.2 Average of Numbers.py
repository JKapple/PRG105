def main():
    input_file = open('numbers.txt', 'r')
    record = input_file.readline()
    record = record.rstrip('\n')
    while record != "":
        print(record)
        record = input_file.readline()
        record = record.rstrip('\n')
    input_file.close()
main()
