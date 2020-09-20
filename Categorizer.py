from csv import writer
from csv import reader
from matplotlib import pyplot as plt
import pandas as pd

# User submitted file path
path = "/Users/alegardy/Documents/Personal/Finances/Checkings_Statements/2020/"

# Storage to application layer
df = pd.read_csv("data.csv", delimiter=",")
gas = df["Gas"].tolist()
entertainment = df["Entertainment"].tolist()
fast_food = df["Fast Food"].tolist()
car = df["Car"].tolist()
groceries = df["Groceries"].tolist()
household_items = df["Household Items"].tolist()
self_improvement = df["Self Improvement"].tolist()
investment = df["Investment"].tolist()
utilities = df["Utilities"].tolist()
charity = df["Charity"].tolist()


def remove_nulls(mylist):
    for i in range(len(mylist)):
        if type(mylist[i]) == str:
            continue
        else:
            del mylist[i:]
            break


# remove nulls from all lists
remove_nulls(gas)
remove_nulls(entertainment)
remove_nulls(fast_food)
remove_nulls(car)
remove_nulls(groceries)
remove_nulls(household_items)
remove_nulls(self_improvement)
remove_nulls(investment)
remove_nulls(utilities)
remove_nulls(charity)


# application layer begins

def categorize(line):
    line = line.upper()  # Capitalize everything to match case of list

    for item in fast_food:
        if item in line:
            return "Fast food"

    for item in groceries:
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

    for item in charity:
        if item in line:
            return "Charity"

    for item in utilities:
        if item in line:
            return "Utilities"
    return "other"


def analyze(read_file, write_file):
    with open(path+read_file, "r") as read_obj, \
            open(path+write_file, "w", newline='') as write_obj:

        # Create read and write objects for parsing
        csv_reader = reader(read_obj)
        csv_writer = writer(write_obj)

        # add the title row
        csv_writer.writerow(["Date", "Amount", "item", "Category"])

        for row in csv_reader:
            del row[2:4]  # get rid of the * and "" this will need to be updated.
            cat = categorize(row[2])
            row.append(cat)
            csv_writer.writerow(row)


# Presentation Layer

def plot_finances_barh():
    plt.show()


def plot_finances_pie(y, data):
    plt.pie(y, labels=data)



x = ["Rent", "Groceries", "Gas", "Fast Food", "Car", "Entertainment", "Self Improvement", "Household Items", "Charity", "Utilities", "Other"]

analyze("August-WF-copy.csv", "version-3.csv")
chart = pd.read_csv(path+"version-3.csv")


# print(str(round(((1 - (acc/82)) * 100))) + "% accuracy")


