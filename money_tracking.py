import csv
import os
from datetime import datetime

FILE_NAME = "expense tracker.csv" 
#create csv file if not exists
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode = "w", newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(["Date","Category","Amount","Due","Status"])
#adding data
def adding_entries():
    date = datetime.now().strftime("%d/%m/%Y")
    category = input(str("Enter Category:"))
    amount = float(input("Enter Amount(if no amount enter 0):"))
    due = float(input("Enter Due(if no due enter 0):"))
    status = input(str("Enter Payment Status(Pending/Completed):"))

    with open(FILE_NAME, mode = 'a', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow([date,category,amount,due,status])

    print("Entries are added succesfully!")

#viewing data
def view_data():
    try:
        with open(FILE_NAME, mode = 'r') as file:
            reader = csv.reader(file)
            print("\n......Details Of Entries......")

            for row in reader:
                print(row)

            print()
    except FileNotFoundError:
        print("The Entry file is not found.\n")
#searching entries
def search_by_category():
    search_category = input(str("Enter Category to Search:"))
    found =  False

    with open(FILE_NAME, mode = 'r') as file:
            reader = csv.reader(file)
            print("\n....Search Result....")
            next(reader)
            for row in reader:
                if search_category.lower() == row[1].lower():
                    print(row)
                    found = True
    if not found:
        print("No Entry is found for this category.")
    print()

def search_by_date():
    search_date = input("Enter date to Search(DD/MM/YYYY):")
    found =  False

    with open(FILE_NAME, mode = 'r') as file:
            reader = csv.reader(file)
            
            print("\n....Search Result....")
            next(reader)
            for row in reader:
                if search_date == row[0]:
                    print(row)
                    found = True
    if not found:
        print("No Entry is found for this Date.")
    print()

def totalAmount():
     total_amount = 0 
     with open(FILE_NAME, mode = 'r') as file:
            reader = csv.reader(file)

            next(reader)
            for row in reader:
                 total_amount += float(row[2])
            print(f"\nTotal Amount = ${total_amount}\n")
def totalDue():
     total_due = 0 
     with open(FILE_NAME, mode = 'r') as file:
            reader = csv.reader(file)

            next(reader)
            for row in reader:
                 total_due += float(row[3])
            print(f"\nTotal Due = ${total_due}\n")
#main menu
def menu():
     create_file()
     while True:
          print("=====Money Tracking=====")
          print("1.Add Entry")
          print("2.View Entry")
          print("3.Search Entry by Category")
          print("4.Search Entry by Date")
          print("5.View Total Amount")
          print("6.View Total Due")
          print("7.Exit Money Tracking")

          choice = input("Enter your choice:")
          if choice == '1':
               adding_entries()
          elif choice == '2':
               view_data()
          elif choice == '3':     
               search_by_category()
          elif choice == '4':
               search_by_date() 
          elif choice == '5':
               totalAmount()
          elif choice == '6':
               totalDue()
          elif choice == '7':
               print("Exiting Money Tracking.....")
               break
          else:
               print("InValid Choice.Try Again.\n")

menu()                 