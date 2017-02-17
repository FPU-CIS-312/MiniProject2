#Jose De La Rosa Final

#This program will give the user a list of ingredients, amount needed, price per ingridient, total price, and directions on how to make the desired amount
#of sugar cookies. 

regularBatchOfSugarCookies = 60 #Gives the user the total amount of cookies made with one batch.
cupsOfButterPer60Cookies = 1.5 #Gives the user the amount of butter needed to make one batch.
costOfButterPer60Cookies = 1.0 #Gives the user the cost of butter to make one batch.
cupsOfWhiteSugarPer60Cookies = 2.0 #Gives the user the amount of white sugar needed to make one batch.
costOfWhiteSugarPer60Cookies = 2.0 #Gives the user the cost of white sugar to make one batch.
teaspoonsOfVanillaPer60Cookies = 1.0 #Gives the user the amount of vanilla needed to make one batch.
costOfVanillaPer60Cookies = .79 #Gives the user the cost of vanilla per batch.
eggsPer60Cookies = 4.0 #Gives the user the amount of eggs needed to make one batch.
costOfEggsPer60Cookies = 0.68 #Gives the user the cost of eggs needed to make batch.
cupsOfFlourPer60Cookies = 5.0 #Gives the user the amount of flour needed to make one batch.
costOfFlourPer60Cookies = 2.0 #Gives the user the cost of flour needed to make one batch.
teaspoonsOfBakingSodaPer60Cookies = 2.0 #Gives the user the amount of baking soda needed to make one batch.
costOfBakingSodaPer60Cookies = .04 #Gives the user the cost of bakin soda to make one batch.
teaspoonsOfSaltPer60Cookies = 1.0 #Gives the user the amount of salt needed to make one batch.
costOfSaltPer60Cookies = .04 #Gives the user the cost of salt to make one batch.


#Calculates the amount of ingredients needed to make the desired amount of cookies.

userNumberOfCookies = float( input( "How many sugar cookies do you want to make: " )) #Asks the user for how many cookies cookies they would like to make.
expectedCupsOfButter = ( userNumberOfCookies / regularBatchOfSugarCookies )*cupsOfButterPer60Cookies  #Calculates the amount of butter needed.
expectedCupsOfWhiteSugar = ( userNumberOfCookies / regularBatchOfSugarCookies )*cupsOfWhiteSugarPer60Cookies #Calculates the amount of white sugar needed.
expectedTeaspoonsOfVanilla = ( userNumberOfCookies / regularBatchOfSugarCookies )*teaspoonsOfVanillaPer60Cookies #Calculates the amount of vanilla needed.
expectedEggs = ( userNumberOfCookies / regularBatchOfSugarCookies )*eggsPer60Cookies #Calculates the amount of eggs needed.
expectedCupsOfFlour = ( userNumberOfCookies / regularBatchOfSugarCookies )*cupsOfFlourPer60Cookies  #Calculates the amount of flour needed.
expectedTeaspoonsOfBakingSoda = ( userNumberOfCookies / regularBatchOfSugarCookies )*teaspoonsOfBakingSodaPer60Cookies #Calculates the amount of baking soda needed.
expectedTeaspoonsOfSalt = ( userNumberOfCookies / regularBatchOfSugarCookies )*teaspoonsOfSaltPer60Cookies #Calculates the amount of salt needed.

#Calculates the cost of each ingredient needed to make the desired amount of cookies.

expectedCostOfButter = ( userNumberOfCookies / regularBatchOfSugarCookies )*costOfButterPer60Cookies #Calculates the cost of butter needed.
expectedCostOfWhiteSugar = ( userNumberOfCookies / regularBatchOfSugarCookies )*costOfWhiteSugarPer60Cookies #Calculates the cost of white sugar needed.
expectedCostOfVanilla = ( userNumberOfCookies / regularBatchOfSugarCookies )*costOfVanillaPer60Cookies #Calculates the cost of vanilla needed.
expectedCostOfEggs = ( userNumberOfCookies / regularBatchOfSugarCookies )*costOfEggsPer60Cookies #Calculates the cost of eggs needed.
expectedCostOfFlour = ( userNumberOfCookies / regularBatchOfSugarCookies )*costOfFlourPer60Cookies #Calculates the cost of flour needed.
expectedCostOfBakingSoda = ( userNumberOfCookies / regularBatchOfSugarCookies )*costOfBakingSodaPer60Cookies #Calculates the cost of baking soda needed.
expectedCostOfSalt = ( userNumberOfCookies / regularBatchOfSugarCookies )*costOfSaltPer60Cookies #Calculates the cost of salt needed.

#Calculates the TOTAL COST of ingridients to make the desired amount of cookies.

Total_Cost = (expectedCostOfButter)+(expectedCostOfWhiteSugar)+(expectedCostOfVanilla)+(expectedCostOfEggs)+(expectedCostOfFlour)+(expectedCostOfBakingSoda)+\
             (expectedCostOfSalt)

print( "\nTOTAL = " + format(Total_Cost, ".2f") )

address = 'http://allrecipes.com/recipe/10402/the-best-rolled-sugar-cookies/' #Gives user access to the web site with the cookie recipe, reviews and other dessert ideas.

#Displays ingredient amounts, and the cost for each individual ingredient for the whatever amount of cookies input by the user.

print( "\nFor " + str(userNumberOfCookies ) + " cookies, you will need:\n " + \
    
    format( expectedCupsOfButter, ".2f" ) + " cups of butter;           \t$ " + \
    format( expectedCostOfButter, ".2f" ) + " approximate cost. \n " + \
    format( expectedCupsOfWhiteSugar, ".2f" ) + " cups of white sugar;            \t$ " + \
    format( expectedCostOfWhiteSugar, ".2f" ) + " approximate cost. \n " + \
    format( expectedTeaspoonsOfVanilla, ".2f" ) + " teaspoons of vanilla;       \t$ " + \
    format( expectedCostOfVanilla, ".2f" ) + " approximate cost. \n " + \
    format( expectedEggs, ".2f" ) + " eggs;                         \t$ " + \
    format( expectedCostOfEggs, ".2f" ) + " approximate cost. \n " + \
    format( expectedCupsOfFlour, ".2f" ) + " cups of flour;                 \t$ " + \
    format( expectedCostOfFlour, ".2f" ) + " approximate cost. \n " + \
    format( expectedTeaspoonsOfBakingSoda, ".2f" ) + " teaspoons of baking soda;    \t$ " + \
    format( expectedCostOfBakingSoda, ".2f" ) + " approximate cost. \n " + \
    format( expectedTeaspoonsOfSalt, ".2f" ) + " teaspoons of salt;             \t$ " + \
    format( expectedCostOfSalt, ".2f" ) + " approximate cost. \n " + "\n\nDirections:\n 1 - Heat oven to 400°F. In large bowl, stir white sugar and butter until blended.\n     Stir in vanilla and eggs until light and fluffy. Stir in flour, baking soda and salt.\n 2 - Cover, and chill dough for at least one hour.\n 3 - Bake 6 to 8 minutes in preheated oven. Cool completley." )

#If statement number one, just trying to be funny, it only costs about $7 to make 60 cookies, but the time and effort it takes is priceless. 
print("\n")
if 60 < userNumberOfCookies :
    print("If you need more than 60 cookies, then you might as well just a cake!")

#If statement number two, 
if 100 < userNumberOfCookies < 1000 :
    print("If you need in between 100 to 1000 Go to Costco, and save up to 25%!")
elif 1000 < userNumberOfCookies :
    print("If you need more than 1000 cookies, Get help. and THEN go to Costco!")

#Displays the link to the "All recipes," website where I got my cookie recipe from. 

print( "\n\nGo to the following link: " + \
        str( address) + "\nFor the sugar cookie recipe, other cookie recipes, and great cake recipes as well, to help\nyou avoid having to make more than 60 cookies.")


       
