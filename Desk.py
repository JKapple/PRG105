
import Chair
import FileCab

class officeFurniture:
    def __init__(self,material,length,height,price):
        self.typeOfMaterial = material
        self.sizeOfLength = length
        self.heightOfDesk = height
        self.priceOfDesk = price
    def Desk(self):
        return "This Desk is made of " + self.typeOfMaterial + "\n This Desk's length is" + " " + self.sizeOfLength + "\n This Desk's height is" + " " + self.heightOfDesk + "\n This Desk's price is" + " " + self.priceOfDesk


class location_of_drawers(officeFurniture):
    def __init__(self,location,drawers):
        self.location = location
        self.number_of_drawers = drawers


    def get_officeFurniture(self):
        return "The drawer is in the " + self.location + " location" + "\n There is " + self.number_of_drawers + " drawers."

x = officeFurniture("wood","five feet","three feet","$200")
y = location_of_drawers("Left", "2")

print (x.Desk())
print (y.get_officeFurniture())




