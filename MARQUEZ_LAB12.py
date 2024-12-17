#MENU
Menu = [' ', "Cookies", "Crinkles", "Cupcake", "Cake", "Bentocake"]
Price = [' ', 29, 8, 49, 599, 349]
May_I_repeat_your_order = []
Item_price = []

#MAY I TAKE YOUR ORDER
while True:
    print("\nMENU / PRICE")
    for x in range(1, len(Menu)):
        print(f"{x}. {Menu[x]} ${Price[x]:.2f}")

    print(f"\n(press '0' to stop, '{len(Menu)}' to add menu)")
    while True:
        whatsyourorder = int(input(f"\nEnter your order: "))
        if whatsyourorder in range(1, len(Menu)):
            quantity = int(input("Quantity: "))
            Item_price.append(quantity * Price[whatsyourorder])
            May_I_repeat_your_order.append(f"{quantity, Menu[whatsyourorder]}")

        elif whatsyourorder == 0:

            #ORDER OUTPUT
            print("\nYour Order: \nQUANTITY / ITEM / PRICE")
            for x in range(len(May_I_repeat_your_order)):
                print(f"{May_I_repeat_your_order[x]} ${Item_price[x]:.2f}")

            print(f"\nTotal: ${sum(Item_price):.2f}")

            #PAYMENT
            payment = float(input("\nPlease Input Payment: "))
            while payment < sum(Item_price):
                print("Payment insufficient")
                payment = float(input("\nPlease Input Payment: "))

            print(f"\nYour change: ${payment - sum(Item_price):.2f}\nThank you, come again!")
            May_I_repeat_your_order.clear()
            Item_price.clear()

            #ORDER AGAIN?
            print("\nOrder again?\n1. Yes\n2. No")
            order_again = int(input("= "))
            if order_again == 1:
                break

            elif order_again == 2:
                exit()

            else:
                print("Invalid Input")
            
        #ADD NEW ITEM
        elif whatsyourorder in range(1 + len(Menu)):
            new_product = str(input("Add new product: "))
            new_product_price = float(input("New product price: "))
            Menu.append(new_product)
            Price.append(new_product_price)
            break

        else:
            print("Invalid Input\n")
            continue

    