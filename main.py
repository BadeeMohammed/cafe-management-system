f = open("sales_record.txt", "a")
menu = {
        'pizza':299,
        'burger':289,
        'pasta':189,
        'sandwich':159,
        'icecream':399,
        'coffee': 119,
        'tea': 99,
}
print("**Welcome to BM CAFE AND RESTAURANT!**\n\nHere's the menu:")
print("Pizza: Rs299\nBurger: Rs289\nPasta: Rs189\nSandwich: Rs159\nIcecream: Rs399\nCoffee: Rs119\nTea: Rs99")

total_bill = 0
item_count = 0
item_1 = input("Please enter what you wanna order(order 1 dish at a time): ")

if item_1 not in menu:
    print(f"Sorry! {item_1} is not available yet.")

else:
    total_bill += menu[item_1]
    print(f"{item_1} has been added to your order.\n")
    item_count += 1

another_order = input("Do you want to order anything else? (yes/no): ")

while another_order != "no":
    # if another_order == "yes":
    item_2 = input("Enter another item that you wanna order: ")

    if item_2 not in menu:
        print(f"Sorry! {item_2} is not available.")
        break

    else:
        total_bill += menu[item_2]
        print(f"{item_2} has been added to your order.\n")
        item_count += 1
        another_order = input("Do you want to order anything else? (yes/no): ") 
       

print("Order placed successfully!")        
print(f"Your total bill is: {total_bill}\nYou have ordered {item_count} item/s.")

earning = total_bill

f.write(f"No.of items ordered = {item_count}\n")
f.write(f"Earning: {earning}\n")

f.close()