#Moises J. Mendoza
#CIS 312
#Created on February 15, 2017

#This program will calculate the amounts of recipe items needed in order
#to bake the desired number of batches of cookies
batch=input('How many batches of peanut butter cookies do you want to make? (1 batch = 24 cookies):')
cookies=(int(batch))

#Establishing the variables as the base ingredients:
#Also establishing the lowest recordable unit for ingredients in either cups or teaspoons
wSugar=(cookies)*1
bSugar=(cookies)*1
butter=(cookies)*1
pButter=(cookies)*1
eggs=(cookies)*2
flour=(cookies)*2.5
bPowder=(cookies)*1
salt=(cookies)*0.5
bSoda=(cookies)*1.5

#This will establish the price of the variables in dollars and cents
#Calculations previously done in BOM project
wSugar_price=float(wSugar*0.25)
bSugar_price=float(bSugar*0.23)
butter_price=float(butter*2.60)
pButter_price=float(pButter*1.10)
egg_price=float(eggs*0.27)
flour_price=float(flour*0.22)
bPowder_price=float(bPowder*0.04)
salt_price=float(salt*0.02)
bSoda_price=float(bSoda*0.01)

#This is a sum of all ingredients in order to get a total cost
total= wSugar_price + bSugar_price + butter_price + pButter_price + egg_price + flour_price + bPowder_price + salt_price + bSoda_price

#The following are the print statements for the itemized output                            
print("\n") #This will create a separation in between statements
print("To make",cookies," batches of peanut butter cookies you will need:")
print("\n") #Another line separation
#These print statements will display the amount of the ingredients as well as cost
print("- "+str(wSugar)+" cups of white sugar, which will cost approximately ${:.2f}". format(wSugar_price,""))
print("- "+str(bSugar)+" cups of brown sugar, which will cost approximately ${:.2f}". format(bSugar_price,""))
print("- "+str(butter)+" cups of butter, which will cost approximately ${:.2f}". format(butter_price,""))
print("- "+str(pButter)+" cups of crunchy peanut butter, which will cost approximately ${:.2f}". format(pButter_price))
print("- "+str(eggs)+" eggs, which will cost approximately ${:.2f}". format(egg_price,""))
print("- "+str(flour)+" cups of flour, which will cost approximately ${:.2f}". format(flour_price,""))
print("- "+str(bPowder)+" teaspoons of baking powder, which will cost approximately ${:.2f}". format(bPowder_price,""))
print("- "+str(salt)+" teaspoons of salt, which will cost approximately ${:.2f}". format(salt_price,"and"))
print("- "+str(bSoda)+" teaspoons of baking soda, which will cost approximately ${:.2f}". format(bSoda_price,""))
print("\n")
#The total cost for the desired number of cookie batches
print("The total expected cost of all ingredients is ${:.2f}". format(total,""))
print("\n")

#First condition relates to price (with parameters)
#Offers cost saving option
if 26 < total < 75 :
    print("*You can save 5% by purchasing these ingredients with your Red Card at Target!*")
    
#Second condition relates to number of batches (with parameters)
#Offers coupon codes depending on order size
if 25 < cookies < 50 :
    print("*For medium bulk orders use coupon code: SMART15 at Save Mart and get 15% off*")
elif 100 < cookies:
    print("*For large bulk orders use coupon code: COOKIE MONSTER at Save Mart and get 25% off*")

#Third condition relates the number of eggs being equal to a dozen
#This is somewhat of a hidden easter egg, so to speak
if eggs==12 :
    print("--You may find this recipe to be EGGScellent!--")
else:
    print("\n")
    print("...AND THAT'S THE WAY THE COOKIE CRUMBLES...")    


print("\n")
#The actual recipe is located at the link below
print("Full recipe can be found at http://allrecipes.com/recipe/10275/classic-peanut-butter-cookies/")





