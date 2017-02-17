# Program written by Gustavo J. Cazares

# This program generates a list of detailed ingredients and the ammount needed, plus the cost to make an amount of cookies requested by the user

regularBatchOfCookies = 42 # defines the amount of cookies in a batch

cupsOfBrownSugarPer42Cookies = 1.5 # defines the amount of brown sugar needed per batch
costOfBrownSugarPer42Cookies = .78 # defines the cost of sugar per batch

cupsOfButterPer42Cookies = 1.0 # defines the amount of butter needed per batch
costOfButterPer42Cookies = 1.0 # define the cost of butter per batch

teaspoonsOfVanillaPer42Cookies = 1.0 # defines the amount of vanilla needed per batch
costOfVanillaPer42Cookies = .79 # defines the cost of vanilla per batch

eggsPer42Cookies = 1.0 # defines the amount of eggs per batch
costOfEggsPer42Cookies = .17 # defines the cost of eggs per batch

cupsOfOatsPer42Cookies = 2.0 # defines the amount of oats needed per batch
costOfOatsPer42Cookies = 1.19 # define the cost of oats per batch

cupsOfFlourPer42Cookies = 1.5 # defines the amount of flour needed per batch
costOfFlourPer42Cookies = .40 # defines the cost of flour needed per batch

teaspoonsOfBakingSodaPer42Cookies = 1.0 # defines the amount of baking soda needed per batch
costOfBakingSodaPer42Cookies = .02 # defines the cost of bakin soda per batch

teaspoonsOfSaltPer42Cookies = .25 # defines the amount of salt needed per batch
costOfSaltPer42Cookies = .01 # defines the cost of salt per batch

cupsOfSemiSweetChocolateChipsPer42Cookies = 1. # defines the amount of semi sweet chocolate chips needed per batch
costOfSemiSweetChocolateChipsPer42Cookies = .94 # defines the cost of semi sweet chocolate chips per batch

cupsOfChoppedNutsPer42Cookies = 1. # defines the amount of chopped nuts needed per batch
costOfChoppedNutsPer42Cookies = 4.48 # definest the amount of chopped nuts per batch


address = 'http://www.bettycrocker.com/recipes/oatmeal-chocolate-chip-cookies/' # defines the web address for cookie recipe

# Calculates the amount of ingredients needed to completed the desired amount of cookies

userNumberOfCookies = float( input( "How many cookies do you want to make: " )) # request input on the amount of cookies needed
expectedCupsOfBrownSugar = ( userNumberOfCookies / regularBatchOfCookies )*cupsOfBrownSugarPer42Cookies # calculates the amount of brown sugar needed
expectedCupsOfButter = ( userNumberOfCookies / regularBatchOfCookies )*cupsOfButterPer42Cookies  # calculates the amount of butter needed
expectedTeaspoonsOfVanilla = ( userNumberOfCookies / regularBatchOfCookies )*teaspoonsOfVanillaPer42Cookies # calculates the amount of vanilla needed
expectedEggs = ( userNumberOfCookies / regularBatchOfCookies )*eggsPer42Cookies # calculates the amount of eggs needed
expectedCupsOfOats = ( userNumberOfCookies / regularBatchOfCookies )*cupsOfOatsPer42Cookies # calculates the amount of oats needed
expectedCupsOfFlour = ( userNumberOfCookies / regularBatchOfCookies )*cupsOfFlourPer42Cookies  # calculates the amount of flour needed
expectedTeaspoonsOfBakingSoda = ( userNumberOfCookies / regularBatchOfCookies )*teaspoonsOfBakingSodaPer42Cookies # calculates the amount of baking soda needed
expectedTeaspoonsOfSalt = ( userNumberOfCookies / regularBatchOfCookies )*teaspoonsOfSaltPer42Cookies # calculates the amount of salt needed
expectedCupsOfSemiSweetChocolateChips = ( userNumberOfCookies / regularBatchOfCookies )*cupsOfSemiSweetChocolateChipsPer42Cookies # calculates the amount of semi sweet chocolate chips needed
expectedCupsOfChoppedNuts = ( userNumberOfCookies / regularBatchOfCookies )*cupsOfChoppedNutsPer42Cookies # calculates the amount of raisins needed

# Calculates the cost of each ingredient needed to complete the desired amount of cookies

expectedCostOfBrownSugar = ( userNumberOfCookies / regularBatchOfCookies )*costOfBrownSugarPer42Cookies # caculates the cost of brown sugar needed 
expectedCostOfButter = ( userNumberOfCookies / regularBatchOfCookies )*costOfButterPer42Cookies # calculates the cost of butter needed
expectedCostOfVanilla = ( userNumberOfCookies / regularBatchOfCookies )*costOfVanillaPer42Cookies # calculates the cost of vanilla needed
expectedCostOfEggs = ( userNumberOfCookies / regularBatchOfCookies )*costOfEggsPer42Cookies # calculates the cost of eggs needed
expectedCostOfOats = ( userNumberOfCookies / regularBatchOfCookies )*costOfOatsPer42Cookies # calculates the cost of oats needed
expectedCostOfFlour = ( userNumberOfCookies / regularBatchOfCookies )*costOfFlourPer42Cookies # calculates the cost of flour needed
expectedCostOfBakingSoda = ( userNumberOfCookies / regularBatchOfCookies )*costOfBakingSodaPer42Cookies # calculates the cost of baking soda needed
expectedCostOfSalt = ( userNumberOfCookies / regularBatchOfCookies )*costOfSaltPer42Cookies # calculates the cost of salt needed
expectedCostOfSemiSweetChocolateChips = ( userNumberOfCookies / regularBatchOfCookies )*costOfSemiSweetChocolateChipsPer42Cookies # calculates the cost of semi sweet chocolate chips needed
expectedCostOfChoppedNuts = ( userNumberOfCookies / regularBatchOfCookies )*costOfChoppedNutsPer42Cookies # calculates the cost of chopped nuts needed



# Displays ingredient amounts as well as cost for each ingredient for the desired amount of cookies needed by user

if userNumberOfCookies < regularBatchOfCookies:
    print( "For less than 42 cookies, just go to Save Mart!" ) # Displays this message if less than a batch of 42 cookies is selected by the user
elif userNumberOfCookies >= regularBatchOfCookies:
    
    print( "\nFor " + str(userNumberOfCookies ) + " cookies, you will need:\n " + \
    format( expectedCupsOfBrownSugar, ".2f" ) + " cups of brown sugar;             \t$ " + \
    format( expectedCostOfBrownSugar, ".2f" ) + " would be the approximate cost. \n " + \
    format( expectedCupsOfButter, ".2f" ) + " cups of butter;                  \t$ " + \
    format( expectedCostOfButter, ".2f" ) + " would be the approximate cost. \n " + \
    format( expectedTeaspoonsOfVanilla, ".2f" ) + " teaspoons of vanilla;            \t$ " + \
    format( expectedCostOfVanilla, ".2f" ) + " would be the approximate cost. \n " + \
    format( expectedEggs, ".2f" ) + " eggs;                              \t$ " + \
    format( expectedCostOfEggs, ".2f" ) + " would be the approximate cost. \n " + \
    format( expectedCupsOfOats, ".2f" ) + " cups of oats;                         \t$ " + \
    format( expectedCostOfOats, ".2f" ) + " would be the approximate cost. \n " + \
    format( expectedCupsOfFlour, ".2f" ) + " cups of flour;                        \t$ " + \
    format( expectedCostOfFlour, ".2f" ) + " would be the approximate cost. \n " + \
    format( expectedTeaspoonsOfBakingSoda, ".2f" ) + " teaspoons of baking soda;            \t$ " + \
    format( expectedCostOfBakingSoda, ".2f" ) + " would be the approximated cost. \n " + \
    format( expectedTeaspoonsOfSalt, ".2f" ) + " teaspoons of salt;                   \t$ " + \
    format( expectedCostOfSalt, ".2f" ) + " would be the approximate cost. \n " + \
    format( expectedCupsOfSemiSweetChocolateChips, ".2f" ) + " cups of semi sweet chocolate chips;\t$ " + \
    format( expectedCostOfSemiSweetChocolateChips, ".2f" ) + " would be the approximate cost. \n " + \
    format( expectedCupsOfChoppedNuts, ".2f" ) +  " cups of chopped nuts;                \t$ " + \
    format( expectedCostOfChoppedNuts, ".2f" ) + " would be the approximate cost." + "\n\nDirections:\n 1 - Heat oven to 350°F. In large bowl, stir brown sugar and butter until blended.\n     Stir in vanilla and egg until light and fluffy.\n     Stir in oats, flour, baking soda and salt;\n     Stir in chocolate chips and nuts.\n 2 - Onto ungreased cookie sheet, drop dough by rounded tablespoonfuls about 2 inches apart.\n 3 - Bake 10 to 12 minutes or until golden brown. Cool slightly; remove from cookie sheet to wire rack." )
     

     
# Displays link to Betty Crocker website containing cookie recipe

print( "\n\nGo to the following link: " + \
        str( address) + " for complete, detailed cookie recipe, Expert Tips, and Nutrional Information.")




       
