class Person:
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone


    def set_name(self,name):
        self.__name = name
    def set_address(self,address):
        self.__address = address
    def set_age(self,age):
        self.__age = age
    def set_phone(self,phone):
        self.__phone = phone



    def get_name(self):
        reurn self.__name
    def get_address(self):
        reurn self.__address
    def get_age(self):
        reurn self.__age
    def get_phone(self):
        reurn self.__phone

def main():

main()
