#write a program to print the current date
from datetime import date
today = date.today()
print("current date = ", today.strftime("%d/%m/%Y"))