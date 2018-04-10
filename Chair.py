

class officeFurniture:
    def __init__(self,material,length,height,price):
        self.typeOfMaterial = material
        self.sizeOfLength = length
        self.heightOfChair = height
        self.priceOfChair = price
    def chair(self):
        return "This Chair is made of " + self.typeOfMaterial + "\n This Chair's length is" + " " + self.sizeOfLength + "\n This Chair's height is" + " " + self.heightOfChair + "\n This Chair's price is" + " " + self.priceOfChair

x = officeFurniture("metal","four feet","four feet",'$100')


print (x.chair())



        





