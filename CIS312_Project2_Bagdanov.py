# CIS312 Final Project
# Created by Seth Bagdanov 2/7/2017
# Calculates and displays a recipe based on the batch size
# Python v3.6
#
# REFERENCES -----
# PRICING: http://grocery.walmart.com/, https://www.dutchvalleyfoods.com/
# RECIPE: http://www.bettycrocker.com/recipes/ultimate-chocolate-chip-cookies/77c14e03-d8b0-4844-846d-f19304f61c57

# save instruction string for future use
ingredientString = "\nYour batch ingredients are as follows: "

# Welcome message
print("CIS312 COOKIE RECIPE CALCULATOR --------------------")

# Set minimum for regular batch to become bulk batch
bulkBatchSizeMin = 192

# Set base quantity variables for standard batch
standardBatch = 24  # base recipe size

numGSaltedButter = 150.0 / standardBatch
numGBrownSugar = 80.0 / standardBatch
numGWhiteSugar = 80.0 / standardBatch
numTspVanilla = 2.0 / standardBatch
numEaEgg = 1.0 / standardBatch
numGWhiteFlour = 225.0 / standardBatch
numTspBakingSoda = 0.25 / standardBatch
numTspSalt = 0.25 / standardBatch
numGChocolateChip = 200 / standardBatch

# Set regular pricing variables for items
unitCostSaltedButter = 0.006158940397
unitCostBrownSugar = 0.002560706402
unitCostWhiteSugar = 0.001719955899
unitCostVanilla = 0.406666666667
unitCostEgg = 0.131666666667
unitCostWhiteFlour = 0.001128747795
unitCostBakingSoda = 0.002202643172
unitCostSalt = 0.005384615385
unitCostChocolateChip = 0.008058823529

# Set bulk pricing variables for items
unitBulkCostSaltedButter = 0.006158940397
unitBulkCostBrownSugar = 0.002560706402
unitBulkCostWhiteSugar = 0.001719955899
unitBulkCostVanilla = 0.034192708333
unitBulkCostEgg = 0.131666666667
unitBulkCostWhiteFlour = 0.001128747795
unitBulkCostBakingSoda = 0.001902149950
unitBulkCostSalt = 0.000997372088
unitBulkCostChocolateChip = 0.005703804300

# Take input from user as to how many cookies
batchSize = int(input('Please enter the batch quantity:  '))

# Determine batch size, regular or bulk

# Size is under min, proceed with regular pricing
if 0 < batchSize < bulkBatchSizeMin:
    print(ingredientString)
    print("      COST   QUANTITY  UNIT  ITEM")  # table header
    # Salted Butter
    print("{:10.2f}".format(unitCostSaltedButter * batchSize * numGSaltedButter)
          , "{:10.2f}".format(numGSaltedButter * batchSize)
          , " g  "
          , "  Salted Butter")
    # Brown Sugar
    print("{:10.2f}".format(unitCostBrownSugar * batchSize * numGBrownSugar)
          , "{:10.2f}".format(numGBrownSugar * batchSize)
          , " g  "
          , "  Brown Sugar")
    # White Sugar
    print("{:10.2f}".format(unitCostWhiteSugar * batchSize * numGWhiteSugar)
          , "{:10.2f}".format(numGWhiteSugar * batchSize)
          , " g  "
          , "  White Sugar")
    # Vanilla
    print("{:10.2f}".format(unitCostVanilla * batchSize * numTspVanilla)
          , "{:10.2f}".format(numTspVanilla * batchSize)
          , " tsp"
          , "  Vanilla")
    # Egg
    print("{:10.2f}".format(unitCostEgg * batchSize * numEaEgg)
          , "{:10.0f}".format(numEaEgg * batchSize)
          , " ea "
          , "  Eggs")
    # White Flour
    print("{:10.2f}".format(unitCostWhiteFlour * batchSize * numGWhiteFlour)
          , "{:10.2f}".format(numGWhiteFlour * batchSize)
          , " g  "
          , "  White Flour")
    # Baking Soda
    print("{:10.2f}".format(unitCostBakingSoda * batchSize * numTspBakingSoda)
          , "{:10.2f}".format(numTspBakingSoda * batchSize)
          , " tsp"
          , "  Baking Soda")
    # Salt
    print("{:10.2f}".format(unitCostSalt * batchSize * numTspSalt)
          , "{:10.2f}".format(numTspSalt * batchSize)
          , " tsp"
          , "  Salt")
    # Chocolate Chip
    print("{:10.2f}".format(unitCostChocolateChip * batchSize * numGChocolateChip)
          , "{:10.2f}".format(numGChocolateChip * batchSize)
          , " g  "
          , "  Chocolate Chips")
    # TOTAL COST
    print("=" * 44)  # separator
    print("$"
          , "{:8.2f}".format(unitCostSaltedButter * batchSize * numGSaltedButter
                             + unitCostBrownSugar * batchSize * numGBrownSugar
                             + unitCostWhiteSugar * batchSize * numGWhiteSugar
                             + unitCostVanilla * batchSize * numTspVanilla
                             + unitCostEgg * batchSize * numEaEgg
                             + unitCostWhiteFlour * batchSize * numGWhiteFlour
                             + unitCostBakingSoda * batchSize * numTspBakingSoda
                             + unitCostSalt * batchSize * numTspSalt
                             + unitCostChocolateChip * batchSize * numGChocolateChip)
          , "    TOTAL COST OF BATCH")


# Size is over minimum, use bulk pricing
elif batchSize >= bulkBatchSizeMin:
    print(ingredientString)
    print("      COST   QUANTITY  UNIT  ITEM")  # table header
    # Salted Butter
    print("{:10.2f}".format(unitBulkCostSaltedButter * batchSize * numGSaltedButter)
          , "{:10.2f}".format(numGSaltedButter * batchSize)
          , " g  "
          , "  Salted Butter")
    # Brown Sugar
    print("{:10.2f}".format(unitBulkCostBrownSugar * batchSize * numGBrownSugar)
          , "{:10.2f}".format(numGBrownSugar * batchSize)
          , " g  "
          , "  Brown Sugar")
    # White Sugar
    print("{:10.2f}".format(unitBulkCostWhiteSugar * batchSize * numGWhiteSugar)
          , "{:10.2f}".format(numGWhiteSugar * batchSize)
          , " g  "
          , "  White Sugar")
    # Vanilla
    print("{:10.2f}".format(unitBulkCostVanilla * batchSize * numTspVanilla)
          , "{:10.2f}".format(numTspVanilla * batchSize)
          , " tsp"
          , "  Vanilla")
    # Egg
    print("{:10.2f}".format(unitBulkCostEgg * batchSize * numEaEgg)
          , "{:10.0f}".format(numEaEgg * batchSize)
          , " ea "
          , "  Eggs")
    # White Flour
    print("{:10.2f}".format(unitBulkCostWhiteFlour * batchSize * numGWhiteFlour)
          , "{:10.2f}".format(numGWhiteFlour * batchSize)
          , " g  "
          , "  White Flour")
    # Baking Soda
    print("{:10.2f}".format(unitBulkCostBakingSoda * batchSize * numTspBakingSoda)
          , "{:10.2f}".format(numTspBakingSoda * batchSize)
          , " tsp"
          , "  Baking Soda")
    # Salt
    print("{:10.2f}".format(unitBulkCostSalt * batchSize * numTspSalt)
          , "{:10.2f}".format(numTspSalt * batchSize)
          , " tsp"
          , "  Salt")
    # Chocolate Chip
    print("{:10.2f}".format(unitBulkCostChocolateChip * batchSize * numGChocolateChip)
          , "{:10.2f}".format(numGChocolateChip * batchSize)
          , " g  "
          , "  Chocolate Chips")
    # TOTAL COST
    print("=" * 44)  # separator
    print("$"
          , "{:8.2f}".format(unitBulkCostSaltedButter * batchSize * numGSaltedButter
                             + unitBulkCostBrownSugar * batchSize * numGBrownSugar
                             + unitBulkCostWhiteSugar * batchSize * numGWhiteSugar
                             + unitBulkCostVanilla * batchSize * numTspVanilla
                             + unitBulkCostEgg * batchSize * numEaEgg
                             + unitBulkCostWhiteFlour * batchSize * numGWhiteFlour
                             + unitBulkCostBakingSoda * batchSize * numTspBakingSoda
                             + unitBulkCostSalt * batchSize * numTspSalt
                             + unitBulkCostChocolateChip * batchSize * numGChocolateChip)
          , "    TOTAL COST OF BATCH")

# batchSize entered was out of range, error!
else:
    print("**ERROR!  You made a mistake in your entry!")

# Display recipe directions ---------------------------------------------------
if batchSize > 0:  # only display if batchSize was valid
    # print cookie ascii
    print("""\n                       _,._
                  __.o`   o`”-.
               .-O o `"-.o   O )_,._
              ( o   O  o )--.-"`O   o"-.
               '--------'  (   o  O    o)
                            `----------`""")
    print("1.\tHeat oven to 375ºF.")  # step 1
    print("2.\tMix sugars, butter, vanilla and egg in large bowl. Stir in flour, "
          "\n\t\tbaking soda and salt (dough will be stiff)."
          "\n\t\tStir in nuts and chocolate chips.")  # step 2
    print("3.\tDrop dough by rounded tablespoonfuls onto cookie sheet.")  # step 3
    print("4.\tBake 8 to 10 minutes or until light brown (centers will be soft)."
          "\n\t\tCool slightly; remove from cookie sheet. Cool on wire rack.")  # step 4
    print("\nFor additional details, visit: "
          , "\nhttp://www.bettycrocker.com/recipes/ultimate-chocolate-chip-cookies/77c14e03-d8b0-4844-846d-f19304f61c57")
else:  # batchSize was incorrect
    print("Please try again.")
