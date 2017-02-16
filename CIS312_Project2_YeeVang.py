#CIS312_Project2_YeeVang
#February 2017

#This program will determine how much money and ingredients it will take for a
#user to make a certain number of breakfast burritos based on the user input 
#and current cost for making 12 breakfast burritos.

#Cost and amount variables. Cost and amount can make 12 burritos
unitCostEgg = float(2.99)
unitCostPotatoe = float(1.00)
unitCostCheese = float(4.99)
unitCostTortilla = float(3.75)
unitCostSausage = float(8.30)

unitAmountEgg = float(12)
unitAmountPotatoe = float(8)
unitAmountCheese = float(16)
unitAmountTortilla = float(12)
unitAmountSausage = float(32)

#List ingredients needed and ask the user to enter the number of burritos desired
print ('==================================================')
print ('Ingredients to make 12 breakfast burritos and the\n'\
       'approximate costs of the required ingredients:\n')
print ('12 large eggs\t\t\t$', unitCostEgg)
print ('8 oz of tater tots\t\t$', unitCostPotatoe)
print ('16 oz cheddar cheese\t\t$', unitCostCheese)
print ('12 whole tortilla (10 inch)\t$', unitCostTortilla)
print ('32 oz sausage\t\t\t$', unitCostSausage)
print ('===================================================\n')

#Ask the user to enter a number of burrito(s) to make.  First loop
#if user enters a string.  Will next loop if user enters any value less
#than 1.  Loop will break and value excepted if user enters a number that
#is greater than 1
while True:
        try: #ask the program try the statements between 'try' and 'except'.  If an exception is detected, the program goes to the test the 'except' clause
            numberBurritos = float(input('How many Burritos do you want to make? ')) #ask for a number from the user
            while numberBurritos < 1: #if the input is a number then the program goes through another loop to test if the number is less than 1
                print ("I'm sorry Dave, I cannot allow that.  You must make at least 1 burrito.") #for as long as the number is less than 1, the user will be asked over and over
                numberBurritos = float(input('How many burritos did you want to make? ')) #asks the user again when numberBurritos is less than one
            break #the loop is broken and program is allowed to continue to run if numberBurritos doesn't cause an exception.  Without break here, the user will be asked to enter the number over and over
        except ValueError: print("Ermmm...That's an invalid amount...AGAIN!!!")#if input numberBurritos is not a float as expected, the print statement excecutes and the loop starts over again


#Calculate amounts per item and total cost
costEgg = float(numberBurritos*unitCostEgg/12)
costPotatoe = float(numberBurritos*unitCostPotatoe/12)
costCheese = float(numberBurritos*unitCostCheese/12)
costTortilla = float(numberBurritos*unitCostTortilla/12)
costSausage = float(numberBurritos*unitCostSausage/12)

totalCost = float(costEgg+costPotatoe+costCheese+costTortilla+costSausage)

amountEgg = float(numberBurritos*unitAmountEgg/12)
amountPotatoe = float(numberBurritos*unitAmountPotatoe/12)
amountCheese = float(numberBurritos*unitAmountCheese/12)
amountTortilla = float(numberBurritos*unitAmountTortilla/12)
amountSausage = float(numberBurritos*unitAmountSausage/12)

#Prints a list of cost and amount needed per ingredient based on number of burritos being made
print()
print ('The ingredient costs and amounts required for', numberBurritos, '\n'\
       'breakfast burrito(s) will be:\n')
print ('Eggs: \t\t$', format(costEgg,',.2f'), '\t',format(amountEgg,',.2f'), 'whole egg(s)\n'\
       'Potatoes: \t$', format(costPotatoe,',.2f'),'\t',format(amountPotatoe,',.2f'), 'oz\n'\
       'Cheese: \t$', format(costCheese,',.2f'), '\t',format(amountCheese,',.2f'), 'oz\n'\
       'Tortilla: \t$', format(costTortilla,',.2f'),'\t',format(amountTortilla,',.2f'),'Tortilla(s)\n'\
       'Sausage: \t$', format(costSausage,',.2f'),'\t',format(amountSausage,',.2f'), 'oz\n')

#Print the total cost of ingrediants and a message depending on how many
#burritos are being made
if numberBurritos >= 10000:
    print ('Congratulations! You get a $5000.00 discount for ordering \n' \
           'at least 10,000 burritos!\n\n',\
           '\tTotal cost:\t\t', ' $',format(totalCost,',.2f'),' \n',\
           '\tYour discount:\t\t','-$ 5000.00 \n',\
           '\tFinal Total cost:\t',' $',format((totalCost-5000),',.2f'),'\n')
    print ('WOW! hope your legion appreciates all your hard work!\n')
elif numberBurritos == 300:
    print ('Congratulations! You get a $300.00 discount for ordering\n' \
           'FOR...SPAR...TA!!!!\n\n',\
           '\tTotal cost:\t\t', ' $',format(totalCost,',.2f'),' \n',\
           '\tYour discount:\t\t','-$ 300.00 \n',\
           '\tFinal Total cost:\t',' $',format((totalCost-300),',.2f'),'\n')
elif numberBurritos == 1:
    print ("Onnnnnneeee...is the loneliest number that you'll ever do...\n"\
           "Twoooooo....can be as bad as one....\n")
    print ('Total cost: \t$', format(totalCost,',.2f'),'\n')
else:
    print ('Total cost: \t$', format(totalCost,',.2f'),'\n')
print ('More information and complete recipe guide can be found at:')
print ('http://www.food.com/recipe/angels-easy-breakfast-burritos-161872')

