"""

text = input("Text 1: ")
text2 = input("Text 2: ")

print(f"Text 1 är \"{text}\"\nText 2 är \'{text2}\'")

text = "'" + (input("Text 1: ")) + "'"
text2 ='"' + (input("Text 2: ")) + '"'
text3 = f"Text 1 är {text}\nText 2 är {text2}"
print(text3)

A
tal_1 = int(input("Tal 1: "))
tal_2 = int(input("Tal 2: "))



diff = tal_1-tal_2
produkt = tal_1*tal_2
kvot = tal_1/tal_2

print(f"\nMellan tal {tal_1} och {tal_2}\nDifferensen är : {diff}\nProdukten är: {produkt}\nKvot är: {kvot}")


string_1 = input("String 1: ")
string_2 = input("String 2: ")
string_3 = string_1 + string_2

print("String ett är " + string_1 + "\nString två är " + string_2 + "\nString 3 är " + string_3)
print("\nNu lägger jag till string_3 med procent formatering. %s." %(string_3)) 
print("\nNu lägger jag till string_3 med .format formateringen. {}".format(string_3))


 Typomvandlar en Integer till en String.

"""

"""
string_1 = "Jag tYcker om äGg"
string_1 = string_1.title()
string_1 = string_1.swapcase()
spam = "SPAM"
string_1 = string_1.replace("äGG",spam)

mel = " "
inte = "inte"

string_2 = string_1.rsplit(" ",2)
string_4 = string_2[1]
string_5 = string_2[0]
string_6 = string_2[2]

del_inte = inte.title()
del2_inte = del_inte.swapcase()

print(string_5 + mel + del2_inte + mel + string_4 + mel + string_6)

"""
from metodLib import fisk

fisk()




