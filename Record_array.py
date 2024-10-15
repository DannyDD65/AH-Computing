class product:
    def __init__(self, productName, stockNumber, price):
        self.productName = productName
        self.stockNumber = stockNumber
        self.price = price

productInventory = []

usbCable = product("USB Cable", 624, 1.74)
hdmiAdaptor = product("HDMI Adaptor", 523, 5)
dvdRWPack = product("DVD-RW Pack", 124, 10.99)

productInventory.append(usbCable)
productInventory.append(hdmiAdaptor)
productInventory.append(dvdRWPack)

for x in range(len(productInventory)):
    print(productInventory[x].productName)
    print(productInventory[x].stockNumber)
    print("£" + str(productInventory[x].price))

