product = {"1. Shampoo", "2. Toothpaste", "3. Soap"}
category = [{"1. Loreal": 65, "2. Pantene": 60, "3. Head & Shoulder": 75}, {"1. Colgate": 45, "2. OralB": 75, "3. Close Up": 70}, {"1. Dove": 25, "2. Pears": 20, "3. Nivea": 30}]
cartItem = []
cartPrice = []
totalQuantity = []
cart = {}
amount = []
stop = False
try:
    while not stop:
        print("Available Items:")
        for productName in product:
            print(productName)
        productInput = int(input("Select a product number from above list: "))
        productInput=productInput-1
        for x, y in category[productInput].items():
            print(str(x) + ': ' + str(y))
        x = category[productInput]
        item = list(x.keys())
        categoryInput = int(input("Select a category number from above list: "))
        categoryInput = categoryInput - 1
        item = item[categoryInput]
        quantity = int(input("Quantity purchased: "))
        cartItem.append(item[3:])
        totalQuantity.append(quantity)
        cartPrice.append(category[productInput][item]*quantity)
        amount.append(category[productInput][item])
        continuationInput = input("Do you want to purchase another item?\nType 'y' for yes and any other key to exit: ").lower()
        if continuationInput == 'y':
            stop = False
        else:
            stop = True
        print(list(zip(cartItem, totalQuantity, amount, cartPrice)), 'Total: ₹%.2f' % sum(cartPrice))
    print('Grant Total: ₹%.2f' % sum(cartPrice))
except Exception as e:
    print(e)
