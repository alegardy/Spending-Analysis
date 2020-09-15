from csv import writer
from csv import reader
from matplotlib import pyplot as plt
import pandas as pd

path = "/Users/alegardy/Documents/Personal/Finances/Checkings_Statements/2020/"


# Categories
#food_file = open("fast_food.txt", newline=" ")
#fast_food = reader(food_file)

df = pd.read_csv(path + "version-1.csv", delimiter=",")
print(df)


#entertainment_file = ("entertainment.txt", "r")
#entertainment = reader(entertainment_file)

gas_file = open("gas.txt", "r")
read = reader(gas_file)
gas = list(read)
#print(gas)






#household_file = open("household_items.txt", "r")
#household_items = reader(household_file)

##car = car_file.readlines()

#improvement_file = open("self_improvement.txt", "r")
#self_improvement = reader(improvement_file)

#utilities_file = open("utilities.txt", "r")
#utilities = reader(utilities_file)

#tithe_file = open("tithe.txt", "r")
#tithe = reader(tithe_file)


# All categories in one dictionary
"""
categories = {
    "Fast food": fast_food,
    "Groceries" : groceries_stores,
    "Gas" : gas,
    "Car" : car,
    "Entertainment" : entertainment,
    "Self Improvement" : self_improvement,
    "Toiletries": household_items,
    "Tithe" : tithe,
    "Utilities" : utilities
}
"""


def categorize(line):
    line = line.upper()  # Capitalize everything to match case of list

    for item in fast_food:
        if item in line:
            return "Fast food"

    for item in groceries_stores:
        if item in line:
            return "Groceries"

    for item in gas:
        if item in line:
            return "Gas"

    for item in car:
        if item in line:
            return "Car"

    for item in entertainment:
        if item in line:
            return "Entertainment"

    for item in self_improvement:
        if item in line:
            return "Self Improvement"

    for item in household_items:
        if item in line:
            return "Household Items"

    for item in tithe:
        if item in line:
            return "Tithe"

    for item in utilities:
        if item in line:
            return "Utilities"
    return "other"


def plot_finances_barh():

    plt.barh(x, amounts, color="teal")
    plt.ylabel("Categories")
    plt.xlabel("Amount of Money")
    plt.title("Spending Analysis")
    plt.show()


def plot_finances_pie(y, data):
    plt.pie(y, labels=data)


def analyze(read_file, write_file):
    with open(path+read_file, "r") as read_obj, \
            open(path+write_file, "w", newline='') as write_obj:

        # Create read and write objects for parsing
        csv_reader = reader(read_obj)
        csv_writer = writer(write_obj)

        # add the title row
        csv_writer.writerow(["Date", "Amount", "item", "Category"])

        for row in csv_reader:
            del row[2:4]  # get rid of the * and ""
            cat = categorize(row[2])
            row.append(cat)
            csv_writer.writerow(row)

x = ["Rent", "Groceries", "Gas", "Fast Food", "Car", "Entertainment", "Self Improvement", "Household Items", "Tithe",
         "Utilities", "Other"]
amounts = [820.00, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

#analyze("August-WF-copy.csv", "version-2.csv")
# print(str(round(((1 - (acc/82)) * 100))) + "% accuracy")


