
class officeFurniture:
    def __init__(self ,material ,length ,height ,price):
        self.typeOfMaterial = material
        self.sizeOfLength = length
        self.heightOfFC = height
        self.priceOfFC = price
    def filing_cabinet(self):
        return "This Filing Cabinet is made of " + self.typeOfMaterial + "\n This Filing Cabinet's length is" + " " + self.sizeOfLength + "\n This Filing Cabinet's height is" + " " + self.heightOfFC + "\n This Filing Cabinet's price is" + " " + self.priceOfFC

x = officeFurniture("metal" ,"four feet" ,"four feet" ,'$100')


print (x.filing_cabinet())











