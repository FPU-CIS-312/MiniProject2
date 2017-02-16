# CIS-312 Mini-Project #2 Python Programming Jesus Carrillo
# Snickerdoodle Cookie Receipe

# Bulk or commercial thresholds
bulk = 312
commercial = 311

# Advise user of bulk vs commercial
print('If making 312 snickerdoodles or more, order is considered bulk anything less than 312 is considered commercial')
print('Cost estimate is based on 2/14/17 pricing')
print('')

# Ingredients
cookies = int(24)   # Receipe cookie amount
butter = 1          # cup of butter
sugar = 1.5         # cups of sugar
eggs = 2            # large eggs
flour = 2.75        # cups of flour
tartar = 2          # teaspoons cream of tartar
bakingSoda = 1      # teaspoon of baking soda
salt = .25          # teaspoon of salt
sugarMix = 3        # tablespoons of sugar for topping
cinnamon = 3        # teaspoons of cinnamon
total = int ( input ('Enter amount of snickerdoodle cookies desired '))
print('')

# Display whether bulk or commercial
if total >= bulk:
    print("This is considered a bulk order buy ingredients at Sam's Club")
    print('')
else:
    if total <= commercial:
        print('This is a small commercial order buy ingredients at Food-4-Less')
        print('')

# Cost based on getting ingredients from Food-4-Less Madera
costButter = 1.99          # cost of butter per cup
costSugar = .41         # cost of 1.5 cups of sugar
costEggs = .15            # cost of 2 large egg
costFlour = .47         # cost of 2.75 cups of flour
costTartar = 1.20       # cost of 2 teaspoons of cream of tartar
costBakingsoda = .09    # cost of 1 teaspoon of baking soda
costSalt = .99          # cost of .25 teaspoon of salt
costSugarmix = .02      # cost of 3 tablespoons of sugar for topping
costCinnamon = .27      # cost of 3 teaspoons of cinnamon for topping

# Cost based on getting ingredients from Sam's club (bulk)
bulkButter = 1.19       # cost of butter per cup
bulkSugar = .65         # cost of 1.5 cups of sugar
bulkEggs = .22          # cost of each large egg
bulkFlour = .63         # cost of 2.75 cups of flour
bulkTartar = .08        # cost of 2 teaspoons of cream of tartar
bulkBakingsoda = .05    # cost of 1 teaspon of baking soda
bulkSalt = .01          # cost of .25 teaspoon of salt
bulkSugarmix = .15      # cost of 3 tablespoons of sugar for topping
bulkCinnamon = .66      # cost of 3 teaspoons of cinnamon for topping


# Working factor calculation
factor = total / cookies

# New ingredient totals
newButter = butter * factor
newSugar = sugar * factor
newEggs = eggs * factor
newFlour = flour * factor
newTartar = tartar * factor
newBakingsoda = bakingSoda * factor
newSalt = salt * factor
newSugarmix = sugarMix * factor
newCinnamon = cinnamon * factor

# Display new ingredient totals
print('To make', total, 'Snickerdoodle cookies, you will need the following ingredients;')
print(format(newButter, '.2f'), 'cup(s) of butter')
print(format(newSugar, '.2f'), 'cup(s) of sugar')
print(int(newEggs),'large eggs')
print(format(newFlour, '.2f'), 'cup(s) of flour')
print(format(newTartar, '.2f'), 'teaspoon(s) of tartar')
print(format(newBakingsoda, '.2f'), 'teaspoon(s) of bakingsoda')
print(format(newSalt, '.2f'), 'teaspoon(s) of salt')
print(format(newSugarmix, '.2f'), 'tablespoon(s) of sugar for topping')
print(format(newCinnamon, '.2f'), 'teaspoon(s) of cinnamon for topping')
print('')

# Cost calculation of ingredients from Food-4-Less
food4lesscostButter = costButter * factor           # cost of butter
food4lesscostSugar = costSugar * factor             # cost of sugar
food4lesscostEggs = costEggs * factor               # cost of eggs
food4lesscostFlour = costFlour * factor             # cost of flour
food4lesscostTartar = costTartar * factor           # cost of cream of tartar
food4lesscostBakingsoda = costBakingsoda * factor   # cost of baking soda
food4lesscostSalt = costSalt * factor               # cost of salt
food4lesscostCinnamon = costCinnamon * factor       # cost of 3 teaspoons of cinnamon for topping
costTotal = food4lesscostButter + food4lesscostSugar + food4lesscostEggs + food4lesscostFlour + \
            food4lesscostTartar + food4lesscostBakingsoda + food4lesscostSalt + food4lesscostCinnamon
food4lessPerCookie = costTotal / total

# Cost calculation of ingredients from Sam's Club
samsButter = bulkButter * factor           # cost of butter
samsSugar = bulkSugar * factor             # cost of sugar
samsEggs = bulkEggs * factor               # cost of eggs
samsFlour = bulkFlour * factor             # cost of flour
samsTartar = bulkTartar * factor           # cost of cream of tartar
samsBakingsoda = bulkBakingsoda * factor   # cost of baking soda
samsSalt = bulkSalt * factor               # cost of salt
samsCinnamon = bulkCinnamon * factor       # cost of 3 teaspoons of cinnamon for topping
samsTotal = samsButter + samsSugar + samsEggs + samsFlour + samsTartar + samsBakingsoda + samsSalt + samsCinnamon
samsPerCookie = samsTotal / total
      
# Determine bulk or commercial
if total >= bulk:
    # Display cost of ingredients from Sam's Club
    print('Cost of', total, "snickerdoodles ingredients from Sam's Club")
    print('Cost of butter     $', format(samsButter, '.2f'), sep='')
    print('Cost of sugar      $', format(samsSugar, '.2f'), sep='')
    print('Cost of eggs       $', format(samsEggs, '.2f'), sep='')
    print('Cost of flour      $', format(samsFlour, '.2f'), sep='')
    print('Cost of tartar     $', format(samsTartar, '.2f'), sep='')
    print('Cost of bakingsoda $', format(samsBakingsoda, '.2f'), sep='')
    print('Cost of salt for   $', format(samsSalt, '.2f'), sep='')
    print('Cost of cinnamon   $', format(samsCinnamon, '.2f'), sep='')
    print("Total estimated cost from Sam's Club $", format(samsTotal, '.2f'), sep='') 
    print("Cost per cookie from Sam's club $", format(samsPerCookie, '.2f'), sep='')
    print('Note: Cost is estimated and multiplied by standard recipe for serving of 24 snickerdoodle cookies')
    print('')
else:
     if total <= commercial:
        # Display cost of ingredients from Food-4-Less
        print('Cost of', total, 'snickerdoodles ingredients from Food-4-Less')
        print('Cost of butter     $', format(food4lesscostButter, '.2f'), sep='')
        print('Cost of sugar      $', format(food4lesscostSugar, '.2f'), sep='')
        print('Cost of eggs       $', format(food4lesscostEggs, '.2f'), sep='')
        print('Cost of flour      $', format(food4lesscostFlour, '.2f'), sep='')
        print('Cost of tartar     $', format(food4lesscostTartar, '.2f'), sep='')
        print('Cost of bakingsoda $', format(food4lesscostBakingsoda, '.2f'), sep='')
        print('Cost of salt for   $', format(food4lesscostSalt, '.2f'), sep='')
        print('Cost of cinnamon   $', format(food4lesscostCinnamon, '.2f'), sep='')
        print('Total estimated cost from Food-4-Less $', format(costTotal, '.2f'), sep='')
        print('Cost per cookie from Food-4-Less $', format(food4lessPerCookie, '.2f'), sep='')
        print('Note: Cost is estimated and multiplyed by standard recipe for serving of 24 snickerdoodle cookies')
        print('')


# directions
# http://www.food.com/recipe/soft-snickerdoodle-cookies-97496?scaleto=24.0&st=null&mode=us
print('Directions')
print('1. Preheat oven to 350° F')
print('2. Mix butter', newButter, 'cup(s) of sugar and', int(newEggs), 'eggs thoroughly in a large bowl')
print('3. Combine flour, cream of tartar, baking soda, and salt in a separate bowl')
print('4. Blend dry ingredients into butter mixture')
print('5. Chill dough and chill an ungreased cookie sheet for about 10-15 minutes in fridge')
print('6. Meanwhile, mix', newSugarmix, 'tablespoons sugar and', newCinnamon, 'teaspoons of cinnamon in a small bowl')
print('7. Scoop 1 inch globs of dough into the sugar/cinnamon mixture')
print('8. Coat by gently rolling balls of dough in the sugar mixture')
print('9. Place on chilled ungreased cookie sheet and bake 10 minutes')
print('')
print('http://www.food.com/recipe/soft-snickerdoodle-cookies-97496?scaleto=24.0&st=null&mode=us')
      


