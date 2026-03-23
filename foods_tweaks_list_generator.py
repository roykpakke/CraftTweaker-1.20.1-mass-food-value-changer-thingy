# Version: Minecraft 1.20.1
# First version 22.03.2026 @ 16:24PM for CraftTweaker Forge 1.20.1

# Utilized to easily mass-modify food values with CraftTweaker, specifically contents of Pam's Harvestcraft 2

# pamhc2foodcore
phc2fc_fruits = ["apple", "melon", "chorus", "sweetberry", "glowberry"]

# pamhc2foodextended
phc2fe_fruits = ["blackberry","blueberry","cactusfruit","candleberry","cranberry","elderberry",
          "huckleberry","juniperberry","mulberry","raspberry","strawberry","cantaloupe",
          "grape","greengrape","kiwi","pineapple","cherry","orange",
          "peach","pear","plum","pawpaw","soursop","apricot",
          "banana","date","dragonfruit","fig","grapefruit","mango",
          "papaya","persimmon","pomegranate","starfruit","breadfruit","jackfruit",
          "guava","lychee","passionfruit","rambutan","tamarind","gooseberry",
          "durian","lemon","lime"]

# pamhc2trees
phc2t_fruits = ["avocado","candlenut","cherry","chestnut","gooseberry","lemon",
          "nutmeg","orange","peach","pear","plum","walnut",
          "hazelnut","pawpaw","soursop","acorn","almond","apricot",
          "banana","cashew","cinnamon","coconut","date","dragonfruit",
          "durian","fig","grapefruit","lime","mango","olive",
          "papaya","pecan","peppercorn","persimmon","pistachio","pomegranate",
          "starfruit","vanillabean","breadfruit","guava","jackfruit","lychee",
          "passionfruit","rambutan","tamarind"]

phc2t_roastedfruits = ["chestnut","hazelnut","walnut","almond","cashew","pecan","pistachio","pinenut","acorn",]

mod = "pamhc2foodcore"

if mod == "pamhc2foodcore":
    for i in phc2fc_fruits:
        print(f"<item:pamhc2foodcore:{i}jellyitem>.food = (FoodProperties.create(2, 0.1));")
        print(f"<item:pamhc2foodcore:{i}jellytoastitem>.food = (FoodProperties.create(5, 0.4));")
        print(f"<item:pamhc2foodcore:{i}juiceitem>.food = (FoodProperties.create(2, 0.1));")
        print(f"<item:pamhc2foodcore:{i}smoothieitem>.food = (FoodProperties.create(3, 0.2));")

    
if mod == "pamhc2foodextended":
    for i in phc2fe_fruits:
        print(f"<item:pamhc2foodextended:{i}jellyitem>.food = (FoodProperties.create(2, 0.1));")
        print(f"<item:pamhc2foodextended:{i}jellysandwichitem>.food = (FoodProperties.create(6, 0.5));")
        print(f"<item:pamhc2foodextended:{i}jellytoastitem>.food = (FoodProperties.create(5, 0.4));")
        print(f"<item:pamhc2foodextended:{i}juiceitem>.food = (FoodProperties.create(2, 0.1));")
        print(f"<item:pamhc2foodextended:{i}smoothieitem>.food = (FoodProperties.create(3, 0.2));")

if mod == "pamhc2trees":
    for i in phc2t_fruits:
        print(f"<item:pamhc2trees:{i}item>.food = (FoodProperties.create(1, 0.1));")
    for j in phc2t_roastedfruits:
        print(f"<item:pamhc2trees:roasted{j}item>.food = (FoodProperties.create(2, 0.1));")
