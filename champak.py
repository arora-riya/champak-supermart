import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector as m
import sys

# Connect to MySQL database
mycon = m.connect(
    host="localhost",
    user="root",
    passwd="",
    database="project_champak"
)

if not mycon.is_connected():
    sys.exit("Sorry, Unable to connect to MySQL database...")

mycur = mycon.cursor()
main_choice = "yes"

while main_choice == "yes":
    print("-" * 100)
    print("\t\t\t\t\tCHAMPAK SUPERMART")
    print("\t\t\t\t\t   welcomes you!")
    print("\t\t*** Project By: Riya Arora***")
    print("\nWelcome! Bienvenidos! Herzlich willkommen! Swaagatam! Yokoso!\n")
    print("-" * 100)

    choicel = input("Are you a customer or staff member? (C/S): ").strip().upper()
    if choicel == "S":
        choice2s = input("Enter your Staff ID: ")
        q1 = "SELECT staff_name FROM staff WHERE staff_id = %s"
        mycur.execute(q1, (choice2s,))
        data = mycur.fetchone()
        if data is None:
            print("We have no such staff member. ACCESS DENIED.")
            choices3s = input("Should the program be reloaded? (Y/N): ").strip().upper()
            if choices3s != "Y":
                break
        else:
            print("Welcome", data[0])
            print("\t\t\t\tOptions:")
            print("1 = Generate Bill for customer")
            print("2 = Display stock details")
            print("3 = Delete stock records")
            print("4 = Add items to stock records")
            print("5 = Edit item details in stock records")
            choice4s = int(input("Enter the desired option: "))
            
            # Option: Display stock details
            if choice4s == 2:
                print("The Stock Details are:")
                q2 = "SELECT * FROM stock"
                mycur.execute(q2)
                data = mycur.fetchall()
                print("\nitem_code\titem_name\tcompany\tavailability\tprice")
                print("_" * 90)
                for row in data:
                    print("\t".join(map(str, row)))
                print("_" * 90)

            # Option: Generate Bill
            elif choice4s == 1:
                name = input("Please enter customer's name: ")
                choice8s = int(input("How many items has the customer purchased? "))
                col_list = ['Item Name', 'Company', 'Price', 'Quantity', 'Amount']
                bill = pd.DataFrame(columns=col_list)

                for i in range(choice8s):
                    item_code = input(f"Enter Item Code of item {i+1}: ")
                    quantity = int(input(f"Enter Quantity of item {i+1}: "))
                    
                    q5 = "SELECT item_name, company, price FROM stock WHERE item_code = %s"
                    mycur.execute(q5, (item_code,))
                    item_data = mycur.fetchone()

                    if item_data:
                        item_name, company, price = item_data
                        bill.loc[i] = [item_name, company, price, quantity, price * quantity]
                    else:
                        print("Invalid item code. Skipping item.")

                tax = float(input("Tax (in %): "))
                total = bill['Amount'].sum()
                tax_amt = total * (tax / 100)
                net_pay = total + tax_amt

                print("\n\n")
                print("_" * 90)
                print("*** BILL ***")
                print("\nCustomer Name:", name)
                mycur.execute("SELECT CURDATE();")
                date = mycur.fetchone()
                print("Date:", date[0])
                print("_" * 90)
                print(bill)
                print("\nTotal Amount: Rs.", total)
                print("Tax Amount: Rs.", tax_amt)
                print("Net Payable Amount: Rs.", net_pay)
                print("_" * 90)
                print("Thanks... We'd love to see you again!!")
            
            # Add logic for other options like editing or deleting stock records, etc.

    elif choicel == "C":
        print("Hi! How could we help you?")
        print("\nOPTIONS:")
        print("1: About Us")
        print("2: Products Available")
        print("3: Discounts & Offers")
        print("4: Register yourself as a member")
        choice2c = int(input("Enter Option number: "))

        if choice2c == 1:
            print("\nCHAMPAK SUPERMART")
            print("Need Something? You are exactly where you'll get it!")
            print("Contact us at: +91 XXXXXXXXXX, champaksupermart@champak.com")
        
        elif choice2c == 2:
            print("\nPRODUCTS AVAILABLE")
            mycur.execute("SELECT item_name FROM stock;")
            products = mycur.fetchall()
            for product in products:
                print(product[0])
        
        elif choice2c == 3:
            print("\nDISCOUNTS & OFFERS")
            print("* Shop for above Rs. 1000 & get a free item worth Rs.100")
            print("* Shop for above Rs. 5000 & get a free item worth Rs.400")
        
        elif choice2c == 4:
            print("Please provide the following details:")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            address = input("Address: ")
            phone = input("Phone: ")
            mycur.execute("INSERT INTO members VALUES (%s, %s, %s, %s, %s);", 
                          (first_name, last_name, dob, address, phone))
            mycon.commit()
            print("Thanks for registering! Welcome to the Champak family.")

    main_choice = input("Do you want the program to reload? (yes/no): ").strip().lower()

if main_choice == 'no':
    print("Goodbye!")
