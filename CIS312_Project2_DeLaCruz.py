Oatmeal_rasin_cookies = 42  # these are the assigned ingredients and their values

#ingredients needed with quantity
Cups_of_sugar_per42_cookies = .75
Cups_of_Brownsugar_per42_cookies = .25
Cups_of_Butter_per42_cookies = .5
Tspoon_of_vanilla_per42_cookies = .5
Eggs_per42_cookies = 1
Cups_of_flour_per42_cookies = .75
Tspoon_of_bakingsoda_per42_cookies = .5
Tspoon_of_cinnamon_per42_cookies = .5
Tspoon_of_salt_per42_cookies = .25
Cups_of_oats_per42_cookies = 1.5
Cups_of_rasins_per42_cookies = .5

#cost of ingredients
Cost_of_sugar_per42_cookies = .07
Cost_of_Brownsugar_per42_cookies = .13
Cost_of_Butter_per42_cookies = .5
Cost_of_vanilla_per42_cookies = .23
Cost_of_Eggs_per42_cookies = .17
Cost_of_flour_per42_cookies = .20
Cost_of_bakingsoda_per42_cookies = .01
Cost_of_cinnamon_per42_cookies = .31
Cost_of_salt_per42_cookies = .01
Cost_of_oats_per42_cookies = .94
Cost_of_rasins_per42_cookies = .72

#Question for user to input the amount of cookies they would like to make.
userNumberOfCookies = int( input( "How many cookies do you want to make? " ))

#expected amounts of ingredients depending on quantity of cookies.
expectedCupsOfSugar = ( userNumberOfCookies / Oatmeal_rasin_cookies )*Cups_of_sugar_per42_cookies
expectedCupsOfBrownSugar = ( userNumberOfCookies / Oatmeal_rasin_cookies )*Cups_of_Brownsugar_per42_cookies
expectedCupsOfButter = ( userNumberOfCookies / Oatmeal_rasin_cookies )*Cups_of_Butter_per42_cookies
expectedTspoonOfVanilla = ( userNumberOfCookies / Oatmeal_rasin_cookies )*Tspoon_of_vanilla_per42_cookies
expectedCountOfEggs = ( userNumberOfCookies / Oatmeal_rasin_cookies )*Eggs_per42_cookies
expectedCupsOfFlour = ( userNumberOfCookies / Oatmeal_rasin_cookies )*Cups_of_flour_per42_cookies
expectedTspoonOfBakingsoda = ( userNumberOfCookies / Oatmeal_rasin_cookies )*Tspoon_of_bakingsoda_per42_cookies
expectedTspoonOfCinnamon = ( userNumberOfCookies / Oatmeal_rasin_cookies )*Tspoon_of_cinnamon_per42_cookies
expectedTspoonOfSalt = ( userNumberOfCookies / Oatmeal_rasin_cookies )*Tspoon_of_salt_per42_cookies
expectedCupsOfOats = ( userNumberOfCookies / Oatmeal_rasin_cookies )*Cups_of_oats_per42_cookies
expectedCupsOfRasins = ( userNumberOfCookies / Oatmeal_rasin_cookies )*Cups_of_rasins_per42_cookies

#expected cost of cookies based on number of cookies.
expectedCostofSugar = ( userNumberOfCookies / Oatmeal_rasin_cookies )*Cost_of_sugar_per42_cookies
expectedCostofBrownSugar = ( userNumberOfCookies / Oatmeal_rasin_cookies )*Cost_of_Brownsugar_per42_cookies
expectedCostofButter = ( userNumberOfCookies / Oatmeal_rasin_cookies )*Cost_of_Butter_per42_cookies
expectedCostofVanilla =( userNumberOfCookies / Oatmeal_rasin_cookies )*Cost_of_vanilla_per42_cookies
expectedCostofEggs = ( userNumberOfCookies / Oatmeal_rasin_cookies )*Cost_of_Eggs_per42_cookies
expectedCostofFlour = ( userNumberOfCookies / Oatmeal_rasin_cookies )*Cost_of_flour_per42_cookies
expectedCostofBakingsoda =( userNumberOfCookies / Oatmeal_rasin_cookies )*Cost_of_bakingsoda_per42_cookies
expectedCostofCinnamon = ( userNumberOfCookies / Oatmeal_rasin_cookies )*Cost_of_cinnamon_per42_cookies
expectedCostofSalt = ( userNumberOfCookies / Oatmeal_rasin_cookies )*Cost_of_salt_per42_cookies
expectedCostofOats =( userNumberOfCookies / Oatmeal_rasin_cookies )*Cost_of_oats_per42_cookies
expectedCostofRasins = ( userNumberOfCookies / Oatmeal_rasin_cookies )*Cost_of_rasins_per42_cookies

#display area to show amount of ingredients needed to fullfil suggested order.
#display will also show the approximate cost for suggested cookies.
print( "\nFor " + str(userNumberOfCookies ) + " cookies you will need: \n\n" + \
    format( expectedCupsOfSugar, ".2f" ) + " cups of sugar\t\t\t$" +\
    format( expectedCostofSugar, ".2f" ) + " would be the apporximate cost. \n" +\
    format( expectedCupsOfBrownSugar, ".2f" ) + " cups of Brown sugar \t\t$" +\
    format( expectedCostofBrownSugar, ".2f" ) + " would be the approximate cost. \n" +\
    format( expectedCupsOfButter, ".2f" ) + " cups of Butter   \t\t\t$" +\
    format( expectedCostofButter, ".2f" ) + " would be the approximate cost. \n" +\
    format( expectedTspoonOfVanilla, ".2f" ) + " teaspoons of Vanilla \t\t$" +\
    format( expectedCostofVanilla, ".2f" ) + " would be the appoximate cost. \n" +\
    format( expectedCountOfEggs, ".2f" ) + " Eggs    \t\t\t\t$" +\
    format( expectedCostofEggs, ".2f" ) + " would be the approximate cost. \n" +\
    format( expectedCupsOfFlour, ".2f" ) + " cups of Flour \t\t\t$" +\
    format( expectedCostofFlour, ".2f" ) + " would be the apporximate cost. \n" +\
    format( expectedTspoonOfBakingsoda, ".2f" ) + " teaspoons of Baking soda \t\t$" +\
    format( expectedCostofBakingsoda, ".2f" ) + " would be the approximate cost. \n" +\
    format( expectedTspoonOfCinnamon, ".2f" ) + " teaspoons of Cinnamon \t\t$" +\
    format( expectedCostofCinnamon, ".2f" ) + " would be the approximate cost. \n" +\
    format( expectedTspoonOfSalt, ".2f" ) + " teaspoons of Salt \t\t$" +\
    format( expectedCostofSalt, ".2f" ) + " would be the approximate cost. \n" +\
    format( expectedCupsOfOats, ".2f" ) + " cups of Oats \t\t\t$" +\
    format( expectedCostofOats, ".2f" ) + " would be the approximate cost. \n" +\
    format( expectedCupsOfRasins, ".2f" ) + " cups of Rasins    \t\t$" +\
    format(expectedCostofRasins, ".2f" ) + " would be the approximate cost." )

#defined the varialbe "Total_cost" to determine the overall cost of the order.
Total_cost = (expectedCostofSugar)+(expectedCostofBrownSugar)+(expectedCostofButter)+(expectedCostofVanilla)+(expectedCostofEggs)+(expectedCostofFlour)+\
             (expectedCostofBakingsoda)+(expectedCostofCinnamon)+(expectedCostofSalt)+(expectedCostofOats)+(expectedCostofRasins)
#will display the total cost of the order.
print( "\nTotal cost = " + format(Total_cost, ".2f") )

#if, elif, and else statements to inform user of a discount or that they received a free gift for ordering.
#else statement is a generic text to thank the customer.
if Total_cost > 250:
    print("\nFor spending more than $250, you save 25% on your next order.")
elif userNumberOfCookies > 500:
    print("\nCongratulations!!!!! You win 2 free orders on your next visit.")
else:
    print("\nThank you for ordering...")
#included in the output is the link to the website for more information.
print ("\nFor more information and directions click on the link provided.")
print ("http://www.bettycrocker.com/recipes/oatmeal-raisin-cookies")

