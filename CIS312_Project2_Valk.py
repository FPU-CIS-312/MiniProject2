#Joshua Valk CIS 312

cookies=input("In whole numbers, How many cookies you making?")#Nobody wants half a cookie
rec=int(cookies)

#Calculations based off one cookie
butter=rec*.04 
sugar=rec*.04
brown_sugar=rec*.04
rpb=rec*.04
egg=rec*.08
vanilla=rec*.04
flour=rec*.08 
bakingso=rec*.04
salt=rec*.02
reesepiece=rec*.08

#Statment that appears near top based on number of cookies entered
if rec < 2:
    print("Seriously, just one cookie? Why?")
if 100 >= rec >= 2:
    print("Have fun making Them")
if rec > 100:
    print("Wow that's a lot of cookies!")

print("You're going to need:")
print()
print(butter, "Cup(s) of Butter")
print(sugar, "Cup(s) of Sugar")
print(brown_sugar, "Cup(s) of Brown Sugar")
print(rpb, "Cup(s) of Reeces Peanut Butter")
print(butter, "Cup(s) of Butter")
print(egg, "Egg(s)")
print(vanilla, "Teaspoon(s) of Vanilla Extract")
print(flour, "Cup(s) of Flour")
print(bakingso, "Teaspoon(s) of Baking Soda")
print(salt, "teaspoon(s) of Butter")
print(reesepiece, "Cup(s) of Reese's Pieces")
print()
print("That's gonna cost:")

buttercost=rec*.07 #total cost of butter
sugarcost=rec*.01 #total cost of sugar
brown_sugarcost=rec*.01 #total cost of brown sugar
rpbcost=rec*.07 #total cost of peanut butter
eggcost=rec*.02 #total cost of eggs
vanillacost=rec*.01 #total cost of vanilla
flourcost=rec*.01 #total cost of butter flour
bakingsocost=rec*.01 #total cost of baking soda
saltcost=rec*.01 #total cost of salt
reesepiececost=rec*.14 #total cost of reeces pieces
total=buttercost+sugarcost+brown_sugarcost+rpbcost+eggcost+vanillacost+flourcost+bakingsocost+saltcost+reesepiececost

#total cost of ingredients for each user
print()
print("$""%.2f"%buttercost, "Dollar(s) for the Butter!") 
print("$""%.2f"%sugarcost, "Dollar(s) for the Sugar!")
print("$""%.2f"%brown_sugarcost, "Dollar(s) for the Brown Sugar!")
print("$""%.2f"%rpbcost, "Dollar(s) for the Reeces Peanut Butter!")
print("$""%.2f"%buttercost, "Dollar(s) for the Butter!")
print("$""%.2f"%eggcost, "Dollar(s) for the Egg(s)!")
print("$""%.2f"%vanillacost, "Dollar(s) for the Vanilla Extract!")
print("$""%.2f"%flourcost,"Dollar(s) for the Flour!")
print("$""%.2f"%bakingsocost, "Dollar(s) for the Baking Soda!")
print("$""%.2f"%saltcost, "Dollar(s) for the salt!")
print("$""%.2f"%reesepiececost, "Dollar(s) for the Reese's Pieces!")
print()
print("That's a total of $", "%.2f"%total, "Dollar(S)") #Total cost displayed for user
print("Have fun with that")
print()
print("https://www.hersheys.com/recipes/en_US/recipes/8736/reeses-pieces-peanut-butter-cookies.html")

