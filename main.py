product = ["Shampoo", "Toothpaste", "Soap"]
category = [{"1. L'Oreal": 65, "2. Pantene": 60, "3. Head & Shoulder": 75}, {"1. Colgate": 45, "2. OralB": 75, "3. Close Up": 70}, {"1. Dove": 25, "2. Pears": 20, "3. Nivea": 30}]
cartItem = []
cartPrice = []
totalQuantity = []
rate = []
try:
    while True:
        print("Available Items:")
        for i, productName in enumerate(product):
            print("%s. %s" % (i+1, productName))
        productInput = int(input("Select a product number from above list: "))
        productInput = productInput - 1
        for x, y in category[productInput].items():
            print(str(x) + " : " + str(y))
        x = category[productInput]
        item = list(x.keys())
        categoryInput = int(input("Select a category number from above list: "))
        categoryInput = categoryInput - 1
        item = item[categoryInput]
        quantity = int(input("Quantity you want to purchase: "))
        cartItem.append(item[3:])
        totalQuantity.append(quantity)
        cartPrice.append(category[productInput][item] * quantity)
        rate.append(category[productInput][item])
        print(list(zip(cartItem, totalQuantity, rate, cartPrice)), 'Total: ₹%.2f' % sum(cartPrice))
        continuationInput = input("Do you want to purchase another item?\nType 'y' for yes and any other key to exit: ").lower()
        if continuationInput == 'y':
            continue
        else:
            break
    for a, b, c, d in list(zip(cartItem, totalQuantity, rate, cartPrice)):
        print('Item : {}, Quantity : {}, Rate : {}, Amount : {}'.format(a, b, c, d))
    print('Grand Total: ₹%.2f' % sum(cartPrice))
except Exception as e:
    print(e)
