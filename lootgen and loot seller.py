
from random import randint, choice, choices
import string


def title():
    print("                                                                                      ")
    print("     ##### /                                           # ###                          ")
    print("  ######  /                                          /  /###  /                       ")
    print(" /#   /  /                                 #        /  /  ###/                        ")
    print("/    /  /                                 ##       /  ##   ##                         ")
    print("    /  /                                  ##      /  ###                              ")
    print("   ## ##              /###     /###     ######## ##   ##            /##  ###  /###    ")
    print("   ## ##             / ###  / / ###  / ########  ##   ##   ###     / ###  ###/ #### / ")
    print("   ## ##            /   ###/ /   ###/     ##     ##   ##  /###  / /   ###  ##   ###/  ")
    print("   ## ##           ##    ## ##    ##      ##     ##   ## /  ###/ ##    ### ##    ##   ")
    print("   ## ##           ##    ## ##    ##      ##     ##   ##/    ##  ########  ##    ##   ")
    print("   #  ##           ##    ## ##    ##      ##      ##  ##     #   #######   ##    ##   ")
    print("      /            ##    ## ##    ##      ##       ## #      /   ##        ##    ##   ")
    print("  /##/           / ##    ## ##    ##      ##        ###     /    ####    / ##    ##   ")
    print(" /  ############/   ######   ######       ##         ######/      ######/  ###   ###  ")
    print("/     #########      ####     ####         ##          ###         #####    ###   ### ")
    print("#                                                                                     ")
    print(" ##                                                                                   ")


gem_data = {
    "Gem1": {"gems": ["Banded Agate", "Eye Agate", "Moss Agate", "Azurite", "Blue Quartz", "Hematite", "Lapis Lazuli", "Malachite", "Obsidian", "Rhodochrosite", "Tiger Eye", "Turquoise", "Freshwater (irregular) Pearl"], "rolls": 4, "multiplier": 1, "weight": 100},
    "Gem2": {"gems": ["Bloodstone", "Carnelian", "Chalcedony", "Chrysoprase", "Citrine", "Iolite", "Jasper", "Moonstone", "Onyx", "Peridot", "Rock Crystal (clear Quartz)", "Sard", "Sardonyx", "Rose Quartz", "Smoky Quartz", "Star Rose Quartz"], "rolls": 2, "multiplier": 10, "weight": 50},
    "Gem3": {"gems": ["Zircon", "Amber", "Amethyst", "Chrysoberyl", "Coral", "Red Garnet", "Brown-Green Garnet", "Jade", "Jet", "White Pearl", "Golden Pearl", "Pink Pearl", "Silver Pearl", "Red Spinel", "Red-Brown Spinel", "Deep Green Spinel", "Tourmaline"], "rolls": 4, "multiplier": 10, "weight": 20},
    "Gem4": {"gems": ["Alexandrite", "Aquamarine", "Violet Garnet", "Black Pearl", "Deep Blue Spinel", "Golden Yellow Topaz"], "rolls": 2, "multiplier": 100, "weight": 15},
    "Gem5": {"gems": ["Emerald", "White Opal", "Black Opal", "Fire Opal", "Blue Sapphire", "Fiery Yellow Corundum", "Rich Purple Corundum", "Blue Star Sapphire", "Black Star Sapphire", "Star Ruby"], "rolls": 4, "multiplier": 100, "weight": 10},
    "Gem6": {"gems": ["Clearest Bright Green Emerald", "Blue-White Diamond", "Canary Diamond", "Pink Diamond", "Brown Diamond", "Blue Diamond", "Jacinth"], "rolls": 2, "multiplier": 1000, "weight": 5},
    "none": {"gems": "", "weight": 100}
}
item_data = {
    "Earrings": {"price": 0.2, "weight": 5}, "Hairpin": {"price": 0.1, "weight": 5}, "Hatpin": {"price": 0.5, "weight": 1}, "Coronet": {"price": 10, "weight": 1}, "Tiara": {"price": 7, "weight": 1}, "Diadem": {"price": 3, "weight": 1}, "Circlet": {"price": 8, "weight": 1}, "Necklace": {"price": 5, "weight": 5}, "Torc": {"price": 8, "weight": 2}, "Pendant": {"price": 6, "weight": 5}, "Bangle": {"price": 4, "weight": 5}, "Bracelet": {"price": 5, "weight": 5}, "Ring": {"price": 1, "weight": 10}, "Brooch": {"price": 2, "weight": 5}, "Anklet": {"price": 3, "weight": 1}, "Amulet": {"price": 5, "weight": 1}, "Prayer jewellery": {"price": 4, "weight": 3}, "Signet ring": {"price": 1, "weight": 1}, "Thumb ring": {"price": 1, "weight": 1}, "Locket": {"price": 1, "weight": 2}, "Medallion": {"price": 2, "weight": 3}, "Pendant (small)": {"price": 2, "weight": 1}
}
condition_data = {
    "Shoddy": {"price": 0.2, "weight": 2}, "Poor": {"price": 0.7, "weight": 4}, "Good": {"price": 1, "weight": 8}, "Excellent": {"price": 1.5, "weight": 2}, "Flawless": {"price": 2, "weight": 1}
}
Jewellery_materials = {
    "Gold": {"price": 10, "weight": 10},
    "Silver": {"price": 5, "weight": 8},
    "Copper": {"price": 1, "weight": 6},
    "Platinum": {"price": 20, "weight": .1},
    "Bronze": {"price": 2, "weight": 6},
    "Orichalcum": {"price": 30, "weight": .1},
    "Brass": {"price": 3, "weight": 6},
    "Steel": {"price": 1, "weight": 3},
    "wooden": {"price": .1, "weight": 1}
}
conjunctions = [
    ", inlaid with ", ", studded with ", ", decorated with ", ", ornamented with ", ", covered in ", ", streaked with ", ", adorned with ", ", encrusted with ", ", embellished with ", ", festooned with ", ", festooned in ", ", lavished with ", ", richly set with ", ", set with ", ", inset with ", ", accented with ", ", beautified with ", ", bedecked with ", ", beset with ", ", bejeweled with ", ", decked in ", ", gilded with ", ", highlighted with ", ", jewelled with ", ", lavished in ", ", ornamented in ", ", overlaid with ", ", rimmed with ", ", trimmed with ",
]

provenanced = {
    "": 250,
    "An unmistakable sigil marks this item as once belonging to a prominent local figure.": 1,
    f"Upon close examination, faint initials, likely of the previous owner, can be found etched into the item.: {choice(string.ascii_uppercase)}.{choice(string.ascii_uppercase)}.": 2,
    "A mysterious engraving on the inside of the item suggests it was gifted by a particular individual of great importance.": 2,
    "Attached to this item is a small, weathered tag that perhaps once bore the name or crest of its previous owner.": 1,
    "Subtle scratches etched into the item suggest that it was wielded often and with great care by its previous owner.": 2,
    "This item has been uniquely modified or repaired, making it unmistakably one-of-a-kind.": 2,
    "A symbol or emblem is emblazoned upon the item, linking it to a particular group or organization with a storied history.": 3,
    "Within this item, an ancient script tells the tale of its previous owner and the remarkable deeds that this item witnessed.": 1,
    "The intricate etchings on this item suggest the skilled hand of a Dwarven master craftsman.": 1,
    "A subtle glow emanates from the surface of this item, hinting at the Gnomish ingenuity used to create it.": 1,
    "The surface of this item bears the marks of a previous owner, whose identity can only be guessed at by an experienced appraiser.": 4,
    "The delicate filigree on this item is reminiscent of the work of the Elven jewelers of old.": 1,
    "Faint runes are etched into this item, revealing the ancient magic that once imbued it.": 2,
    "The elaborate designs on this item suggest that it was crafted for a noble purpose, and has a storied history.": 2,
    "The intricate engravings on this item reveal the attention to detail and skill of its previous owner, whoever they may have been.": 5,
    "A subtle yet unmistakable scent clings to this item, hinting at its previous use and the adventures it has been on.": 3,
    "Faded colors suggest it has been passed down through generations, carrying the stories of those who owned it before.": 3,
    "The smooth, worn surface hints at a history of many hands that have held it, each adding to its provenance.": 3,
    "A beautiful patina has formed on this item, evidence of its many travels and the hands that have held it.": 2,
    "The smooth surface of this item bears the imprint of countless stories, passed down through the generations.": 3,
    "This item bears the scars of long journeys through treacherous terrain, a testament to the resilience of its previous owners.": 2,
    "Deep grooves and nicks tell the tale of this item's storied past, a history marked by battles won and lost.": 1,
    "This item's intricate patterns are evidence of the skill of its maker, whose artistry has stood the test of time.": 3,
    "The intricate knotwork adorning this item speaks of a rich history steeped in magic and mystery.": 2,
    "Elaborate carvings testify to this item's noble lineage, a possession once treasured by a powerful and wise ruler.": 3,
    "A faint aroma lingers on this item, a reminder of the fire it has survived and the memories it carries.": 2,
    "The precise and delicate craftsmanship of this item attests to the care and love with which it was made and cherished.": 3,
    "Fine details betray the skill of this item's maker, whose legacy lives on through their exquisite creations.": 1,
    "This item's faded emblem bears witness to its storied past, once belonging to a guild of great renown.": 2,
    "Subtle engravings hint at this item's hidden history, a past shrouded in mystery and secrecy.": 3,
    "Faint traces of dust suggest the item has long remained untouched in a hidden location.": 1,
    "The item is intricately detailed, but bears no maker's mark. Perhaps it was crafted by a humble hand, or one that values anonymity.": 2,
    "The item's craftsmanship exhibits a style and finesse that marks it as the work of an esteemed artisan.": 3,
    "An ornate design, perhaps of ancient origin, is expertly engraved upon the item.": 2,
    "The item's well-worn appearance hints at a rich history of use and wear.": 1,
    "Subtle variations in the item's color and texture suggest a unique and individualized origin.": 2,
    "Delicate filigree work adorns the item, hinting at the skilled hand of an artisan in a bygone era.": 3,
    "A slight, but noticeable, weight imbalance in the item suggests it was crafted for a specific purpose or owner.": 1
}

material_dict = {
    "": {"": {"price": 1, "rarity": 1}},
    "metal": {
        "iron ": {"price": 1, "rarity": 5},
        "bronze ": {"price": 1.5, "rarity": 4},
        "copper ": {"price": 2, "rarity": 4},
        "silver ": {"price": 10, "rarity": 4},
        "gold ": {"price": 20, "rarity": 1},
        "platinum ": {"price": 50, "rarity": 0.02},
        "electrum ": {"price": 30, "rarity": 0.5},
        "adamantine ": {"price": 100, "rarity": 0.01},
        "mithril ": {"price": 200, "rarity": 0.02},
        "steel ": {"price": 5, "rarity": 2}
    },

    "stone": {
        "granite ": {"price": 1, "rarity": 5},
        "marble ": {"price": 1.5, "rarity": 3},
        "limestone ": {"price": 2, "rarity": 4},
        "sandstone ": {"price": 3, "rarity": 5},
        "obsidian ": {"price": 5, "rarity": 3},
        "jade ": {"price": 20, "rarity": 1},
    },

    "wood": {
        "oak ": {"price": 1, "rarity": 5},
        "pine ": {"price": 1.5, "rarity": 8},
        "maple ": {"price": 2, "rarity": 7},
        "ebony ": {"price": 20, "rarity": 1},
        "rosewood ": {"price": 30, "rarity": 2},
        "teak ": {"price": 10, "rarity": 7},
        "mahogany ": {"price": 15, "rarity": 5},
        "elm ": {"price": 1.5, "rarity": 6},
        "willow ": {"price": 1.2, "rarity": 6},
        "cedar ": {"price": 3, "rarity": 8},
    },

    "fabric": {
        "wool ": {"price": 1, "rarity": 5},
        "linen ": {"price": 1.5, "rarity": 7},
        "silk ": {"price": 10, "rarity": 1},
        "cotton ": {"price": 2, "rarity": 4},
        "velvet ": {"price": 7, "rarity": 2},
        "satin ": {"price": 6, "rarity": 3},
        "tartan ": {"price": 3, "rarity": 6},
        "sack cloth ": {"price": 3, "rarity": 6}
    },

    "fur": {
        "rabbit fur ": {"price": 1, "rarity": 7},
        "sheepskin ": {"price": 2, "rarity": 6},
        "lambskin ": {"price": 1.5, "rarity": 5},
        "squirrel fur ": {"price": 3, "rarity": 5},
        "marten fur ": {"price": 5, "rarity": 4},
        "ermine fur ": {"price": 10, "rarity": 2},
        "beaver fur ": {"price": 7, "rarity": 3},
        "fox fur ": {"price": 4, "rarity": 6},
        "otter fur ": {"price": 6, "rarity": 5},
        "lynx fur ": {"price": 12, "rarity": 1},
        "bearskin ": {"price": 20, "rarity": 0.5},
        "wolf fur ": {"price": 5, "rarity": 4},
        "seal fur ": {"price": 8, "rarity": 3},
        "leopard fur ": {"price": 25, "rarity": 0.1},
        "sable fur ": {"price": 30, "rarity": 0.1},
        "mink fur ": {"price": 15, "rarity": 2}
    },

    "natural hard material": {
        "ivory ": {"price": 8, "rarity": 0.1},
        "bone ": {"price": 2, "rarity": 5},
        "antler ": {"price": 3, "rarity": 2},
        "turtle shell ": {"price": 5, "rarity": 0.5},
        "amber ": {"price": 10, "rarity": 0.05},
        "coral ": {"price": 7, "rarity": 0.1},
        "horn ": {"price": 3, "rarity": 2}
    }}
Qaals_tokens = [
    "Anchor Token", "Bird Token", "Fan Token", "Swan Boat Token", "Tree Token", "Whip Token"]
Valhalla_horns = {
    "Silver": 40, "Brass": 35,  "Bronze": 15, "Iron": 10}
Fig_wondrous = {
    "Bronze Griffon": 1, "Ebony Fly": 1, "Golden Lions": 1, "Ivory Goats": 1, "Marble Elephant": 1, "Onyx Dog": 2, "Serpentine Owl": 1
}
Belt_f_s = [
    "Belt of Frost Giant Strength", "Belt of stone Giant Strength"]
magic_armour = {
    "Half Plate, +2": 2, "Plate, +2": 2, "Studded Leather, +3": 2, "Breastplate, +3": 2, "Splint, +3": 2, "Half Plate, +3": 1, "Plate, +3": 1
}
Legendary_crystal_ball = [
    "Crystal Ball of Mind Reading", "Crystal Ball of Telepathy", "Crystal Ball of True Seeing"]
demons = {"type 1": ["Barlgura", "Shadow demon", "Vrock"],
          "type 2": ["Chasme", "Hezrou"],
          "type 3": ["Glabrezu", "Yochlol"],
          "type 4": ["Nalfeshnee"],
          "type 5": ["Marilith"],
          "type 6": ["Balor", "Goristro"]}
devils = {"greater": ["Horned devil", "Erinyes", "Ice devil", "Pit fiend"],
          "lesser": ["Imp", "Spined devil", "Bearded devil", "Barbed devil", "Chain devil", "Bone devil"]
          }
elementals = ["Air", "Earth", "Fire", "Water"]
Iron_flask = {
    "Empty": 50, "Arcanaloth": 1, "Cambion": 1, "Dao": 2, f"Demon ({choice(demons['type 1'])})": 3, f"Demon ({choice(demons['type 2'])})": 3, f"Demon ({choice(demons['type 3'])})": 2, f"Demon ({choice(demons['type 4'])})": 2, f"Demon ({choice(demons['type 5'])})": 1, f"Demon ({choice(demons['type 6'])})": 1, "Deva": 1, f"Greater Devil ({choice(devils['greater'])})": 2, f"Lesser Devil ({choice(devils['lesser'])})": 3, "Djinni": 2, "Efreeti": 2, f"{choice(elementals)} Elemental": 2, "Githyanki knight": 1, "Githzerai zerth": 1, "Invisible stalker": 2, "Marid": 2, "Mezzoloth": 2, "Night hag": 2, "Nycaloth": 2, "Planetar": 1, "Salamander": 2, "Slaad": 2, "Solar": 1, "Succubus/incubus": 2, "Ultroloth": 1, "Xorn": 1}
toadstool = ["the eater must succeed on a DC 15 Constitution saving throw or take 5d6 poison damage and become Poisoned for 1 hour.",
             "the eater gains 5d6 Temporary Hit Points for 1 hour."]
geyser = ["water", "beer", "berry juice", "tea", "vinegar", "wine", "oil"]
treant = ["The Treant is chaotic evil and attacks!",
          "The Treat is not hostile"]
potions = [
    'Healing',
    'Greater Healing',
    'Superior Healing',
    'Supreme Healing',
    'Invisibility',
    'Greater Invisibility',
    'Flying',
    'Swiftness',
    'Giant Strength',
    'Shrinking',
    'Enlarging',
    'Regeneration',
    'Haste',
    'Slow',
    'Charm',
    'Confusion',
    'Levitation',
    'Water Breathing',
    'Spider Climb',
    'Mind Reading',
    'Teleportation',
    'Invisibility'
]
bag_of_beans_potions_num = randint(1, 8)


def bag_of_beans_potions(bag_of_beans_potions_num):
    potions_string = ""
    for _ in range(bag_of_beans_potions_num):
        potions_string += choice(potions)+" ,"
    potions_string = potions_string[:-2]
    return potions_string


potions_string = bag_of_beans_potions(bag_of_beans_potions_num)
num_beans = randint(1, 4)+randint(1, 4)+randint(1, 4)
bean_num = (randint(1, 4))+(randint(1, 4))+(randint(1, 4))
bag_of_beans = {"type": {f"{(randint(1,4))+(randint(1,4))+(randint(1,4))+(randint(1,4))+(randint(1,4))} toadstools sprout. If a creature eats a toadstool, {(choice([toadstool]))}": 1, f"A geyser erupts and spouts {choice(geyser)} 30 feet into the air for {randint(1,12)} rounds.": 9, f"A Treant sprouts (see the Monster Manual for statistics). {choice(treant)}.": 10, "An animate, immobile stone statue in your likeness rises. It makes verbal threats against you. If you leave it and others come near, it describes you as the most heinous of villains and directs the newcomers to find and Attack you. If you are on the same plane of existence as the statue, it knows where you are. The statue becomes inanimate after 24 hours.": 10, "A campfire with blue flames springs forth and burns for 24 hours (or until it is extinguished).": 10, f"{randint(1,6) + 6} shriekers sprout (see the Monster Manual for statistics).": 10, f"{randint(1,4) + 8} bright pink toads crawl forth. Whenever a toad is Touched, it transforms into a Large or smaller monster of the DM's choice. The monster remains for 1 minute, then disappears in a puff of bright pink smoke.": 10, "A hungry Bulette (see the Monster Manual for statistics) burrows up and attacks.": 10,
                         f"A fruit tree grows. It has {randint(1,10)+20} fruit, {bag_of_beans_potions_num} of which act as randomly determined magic potions: {potions_string}, while one acts as an ingested poison of the DM's choice. The tree vanishes after 1 hour. Picked fruit remains, retaining any magic for 30 days.": 10, f"A nest of {randint(1,4) + 3} eggs springs up. Any creature that eats an egg must make a DC 20 Constitution saving throw. On a successful save, a creature permanently increases its lowest ability score by 1, randomly choosing among equally low scores. On a failed save, the creature takes {randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6)} force damage from an internal magical explosion.": 10, "A pyramid with a 60-foot-square base bursts upward. Inside is a sarcophagus containing a Mummy Lord (see the Monster Manual for statistics). The pyramid is treated as the mummy lord's lair, and its sarcophagus contains Treasure of the DM's choice.": 10, "A giant beanstalk sprouts, growing to a height of the DM's choice. The top leads where the DM chooses, such as to a great view, a cloud giant's castle, or a different plane of existence.": 1}}


def beans(bean_num):
    string_beans = ""
    for _ in range(bean_num):
        string_beans = choices(list(bag_of_beans["type"].keys()), weights=list(
            bag_of_beans["type"].values()))[0]+" ,"
    string_beans = string_beans[:-2]
    return string_beans


string_beans = beans(bean_num)
domt = {"material": ["Vellum", "Ivory"], "cards": {
    "Thirteen cards": 0.75, "Twenty-Two cards": 0.25}}
candle_invokation = {"Lawful Good: Tyrael, God of Justice and Honor": 3,
                     "Neutral Good: Anora, Goddess of Healing and Protection": 2,
                     "Chaotic Good: Kaelar, God of Freedom and Adventure": 3,
                     "Lawful Neutral: Auriel, God of Order and Discipline": 2,
                     "True Neutral: Arin, God of Balance and Equilibrium": 2,
                     "Chaotic Neutral: Zephyr, God of Change and Uncertainty": 2,
                     "Lawful Evil: Azazel, God of Control and Domination": 2,
                     "Neutral Evil: Drogath, God of Deception and Manipulation": 2,
                     "Chaotic Evil: Malphas, God of Violence and Anarchy": 2}
spells = {
    "cantrips": ["Acid Splash", "Blade Ward", "Booming Blade", "Chill Touch", "Control Flames", "Create Bonfire", "Dancing Lights", "Encode Thoughts", "Fire Bolt", "Friends", "Frostbite", "Green-Flame Blade", "Gust", "Infestation", "Light", "Lightning Lure", "Mage Hand", "Mending", "Message", "Mind Sliver", "Minor Illusion", "Mold Earth", "Poison Spray", "Prestidigitation", "Ray of Frost", "Sapping Sting", "Shape Water", "Shocking Grasp", "Sword Burst", "Thunderclap", "Toll The Dead", "True Strike"],

    "1st": ["Absorb Elements", "Alarm", "Burning Hands", "Catapult", "Cause Fear", "Charm Person", "Chromatic Orb", "Color Spray", "Comprehend Languages", "Detect Magic", "Disguise Self", "Distort Value", "Earth Tremor", "Expeditious Retreat", "False Life", "Feather Fall", "Find Familiar", "Fog Cloud", "Frost Fingers", "Gift of Alacrity", "Grease", "Guiding Hand", "Healing Elixir", "Ice Knife", "Id Insinuation", "Identify", "Illusory Script", "Jump", "Longstrider", "Mage Armor", "Magic Missile", "Magnify Gravity", "Protection from Evil", "Protection from Good", "Puppet", "Ray of Sickness", "Sense Emotion", "Shield", "Silent Image", "Silvery Barbs", "Sleep", "Snare", "Sudden Awakening", "Tasha's Caustic Brew", "Tasha's Hideous Laughter", "Tenser's Floating Disk", "Thunderwave", "Unseen Servant", "Witch Bolt"],

    "2nd": ["Aganazzar's Scorcher", "Alter Self", "Arcane Lock", "Blindness / Deafness", "Blur", "Borrowed Knowledge", "Cloud of Daggers", "Continual Flame", "Crown of Madness", "Darkness", "Darkvision", "Detect Thoughts", "Dragon's Breath", "Dust Devil", "Earthbind", "Enlarge / Reduce", "Flaming Sphere", "Fortune's Favor", "Gentle Repose", "Gift of Gab", "Gust of Wind", "Hold Person", "Immovable Object", "Invisibility", "Jim's Glowing Coin", "Kinetic Jaunt", "Knock", "Levitate", "Locate Object", "Magic Mouth", "Magic Weapon", "Maximilian's Earthen Grasp", "Melf's Acid Arrow", "Mental Barrier", "Mind Spike", "Mirror Image", "Misty Step", "Nathair's Mischief", "Nystul's Magic Aura", "Phantasmal Force", "Pyrotechnics", "Ray of Enfeeblement", "Rime's Binding Ice", "Rope Trick", "Scorching Ray", "See Invisibility", "Shadow Blade", "Shatter", "Skywrite", "Snilloc's Snowball Swarm", "Spider Climb", "Suggestion", "Tasha's Mind Whip ", "Vortex Warp", "Warding Wind", "Web", "Wither and Bloom", "Wristpocket"],

    "3rd": ["Animate Dead", "Ashardalon's Stride", "Bestow Curse", "Blink", "Catnap", "Clairvoyance", "Conjure Lesser Demon", "Counterspell", "Dispel Magic", "Enemies Abound", "Erupting Earth", "Fast Friends", "Fear", "Feign Death", "Fireball", "Flame Arrows", "Fly", "Gaseous Form", "Glyph of Warding", "Haste", "Hypnotic Pattern", "Incite Greed", "Intellect Fortress", "Leomund's Tiny Hut", "Life Transference", "Lightning Bolt", "Magic Circle", "Major Image", "Melf's Minute Meteors", "Nondetection", "Phantom Steed", "Protection from Energy", "Pulse Wave", "Remove Curse", "Sending", "Sleet Storm", "Slow", "Spirit Shroud", "Stinking Cloud", "Summon Fey", "Summon Lesser Demon", "Summon Shadowspawn", "Summon Undead", "Thunder Step", "Tidal Wave", "Tiny Servant", "Tongues", "Vampiric Touch", "Wall of Sand", "Wall of Water", "Water Breathing"],

    "4th": ["Arcane Eye", "Banishment", "Blight", "Charm Monster", "Cold Shield", "Confusion", "Conjure Barlgura", "Conjure Minor Elementals", "Conjure Shadow Demon", "Control Water", "Dimension Door", "Ego Whip", "Elemental Bane", "Evard's Black Tentacles", "fabricate", "Fire Shield", "Gravity Sinkhole", "Greater Invisibility", "Hallucinatory Terrain", "Ice Storm", "Leomund's Secret Chest", "Locate Creature", "Mordenkainen's Faithful Hound", "Mordenkainen's Private Sanctum", "Otiluke's Resilient Sphere", "Phantasmal Killer", "Polymorph", "Raulothim's Psychic Lance", "Sickening Radiance", "stone Shape", "stoneskin", "Storm Sphere", "Summon Aberration", "Summon Construct", "Summon Elemental", "Summon Greater Demon", "Vitriolic Sphere", "Wall of Fire", "Watery Sphere"],

    "5th": ["Animate Objects", "Bigby's Hand", "Cloudkill", "Cone of Cold", "Conjure Elemental", "Conjure Vrock", "Contact Other Plane", "Control Winds", "Creation", "Danse Macabre", "Dawn", "Dominate Person", "Dream", "Enervation", "Far Step", "Geas", "Hold Monster", "Immolation", "Infernal Calling", "Legend Lore", "Mislead", "Modify Memory", "Negative Energy Flood", "Passwall", "Planar Binding", "Rary's Telepathic Bond", "Scrying", "Seeming", "Skill Empowerment", "Steel Wind Strike", "Summon Draconic Spirit", "Synaptic Static", "Telekinesis", "Teleportation Circle", "Transmute Rock", "Wall of Force", "Wall of Light", "Wall of stone"],

    "6th": ["Arcane Gate", "Chain Lightning", "Circle of Death", "Contingency", "Create Homunculus", "Create Undead", "Disintegrate", "Drawmij's Instant Summons", "Eyebite", "Fizban's Platinum Shield", "Flesh to stone", "Globe of Invulnerability", "Gravity Fissure", "Guards and Wards", "Investiture of Flame", "Investiture of Ice", "Investiture of stone", "Investiture of Wind", "Magic Jar", "Mass Suggestion", "Mental Prison", "Move Earth", "Otiluke's Freezing Sphere", "Otto's Irresistible Dance", "Programmed Illusion", "Scatter", "Soul Cage", "Summon Fiend", "Sunbeam", "Tasha's Otherworldly Guise", "Tenser's Transformation", "True Seeing", "Wall of Ice"],

    "7th": ["Conjure Hezrou", "Create Magen", "Crown of Stars", "Delayed Blast Fireball", "Draconic Transformation", "Dream of the Blue Veil ", "Etherealness", "Finger of Death", "Forcecage", "Mirage Arcane", "Mordenkainen's Magnificent Mansion", "Mordenkainen's Sword", "Plane Shift", "Power Word Pain", "Prismatic Spray", "Project Image", "Reverse Gravity", "Sequester", "Simulacrum", "Symbol", "Teleport", "Tether Essence", "Whirlwind"],

    "8th": ["Abi-Dalzim's Horrid Wilting", "Animal Shapes", "Antimagic Field", "Antipathy / Sympathy", "Clone", "Control Weather", "Dark Star", "Demiplane", "Dominate Monster", "Earthquake", "Feeblemind", "Glibness", "Holy Aura", "Illusory Dragon", "Incendiary Cloud", "Maddening Darkness", "Maze", "Mighty Fortress", "Mind Blank", "Power Word Stun", "Reality Break", "Sunburst", "Telepathy", "Tsunami"],

    "9th": ["Astral Projection", "Blade of Disaster", "Foresight", "Gate", "Imprisonment", "Invulnerability", "Mass Heal", "Mass Polymorph", "Meteor Swarm", "Power Word Heal", "Power Word Kill", "Prismatic Wall", "Psychic Scream", "Ravenous Void", "Shapechange", "Storm of Vengeance", "Time Ravage", "Time Stop", "True Polymorph", "True Resurrection", "Weird", "Wish"]
}
armour = {
    "l": ["Padded", "Leather", "Padded Leather"],
    "m1": ["Hide"],
    "m2": ["Chain Shirt", "Scale Mail", "Breastplate", "Half Plate"],
    "h": ["Ring Mail", "Chain Mail", "Splint", "Plate"]
}
weapon = {
    "s": {"Club": 1, "Dagger": 20, "Greatclub": 2, "Handaxe": 50, "Javelin": 5, "Light Hammer": 20, "Mace": 50, "Quarterstaff": 2, "Sickle": 10, "Spear": 10, "Light Crossbow": 250, "Dart (10)": 5, "Shortbow": 250, "Sling": 1},
    "m": {"Battleaxe": 100, "Flail": 100, "Glaive": 200, "Greataxe": 300, "Greatsword": 500, "Halberd": 200, "Lance": 100, "Longsword": 150, "Maul": 100, "Morningstar": 150, "Pike": 50, "Rapier": 250, "Scimitar": 250, "Shortsword": 100, "Trident": 50, "War Pick": 50, "Warhammer": 150, "Whip": 20, "Blowgun": 100, "Hand Crossbow": 750, "Heavy Crossbow": 500, "Longbow": 500, "Net": 10}, "sword": ["Greatsword", "Longsword", "Rapier", "Scimitar", "Shortsword"], "axe": ["Handaxe", "Battleaxe", "Greataxe"]
}
monster = [
    'of a beholder', 'of a dragon', 'of a kraken', 'of a hippogriff', 'of a chimera', 'of a hell hound', 'of a pegasus', 'of a cockatrice', 'of a basilisk', 'of a owlbear', 'of a manticore', 'of a rust monster', 'of a gelatinous cube', 'of a unicorn']
animal = [
    'of a horse', 'of a lion', 'of a tiger', 'of a bear', 'of a wolf', 'of a deer', 'of a goat', 'of a dog', 'of a cat', 'of a bird of prey', 'of a fish', 'of a whale', 'of a serpent', 'of a butterfly', 'of a cow', 'of a sheep', 'of farm animals', f'{choice(monster)}', 'of an extinct or imaginary animal']
marine = [
    'of a dolphin', 'of a whale', 'of a shark', 'of a seahorse', 'of an octopus', 'of a mermaid or merman', 'of a giant squid', 'of a sea turtle', 'of a narwhal', 'of a giant crab', 'of a giant lobster', 'of a hippocampus', 'of a sahuagin', 'of a giant sea serpent', 'of a giant eel', 'of a kraken', 'of a triton', 'of a water elemental', 'of a chuul', 'of a aboleth']
pet = [
    'dog', 'cat', 'bird', 'ferret', 'tortoise', 'snake', 'lizard', 'horse', 'duck', 'goose', 'crow', 'bird of prey', 'owl']
painting = [
    'of a religious scene', 'of a mythological figure', 'of a portrait', 'of a landscape', 'of a seascape', 'of a still life', 'of a historical event', 'of an allegorical scene', 'of a female nude', f'{choice(animal)} portrait', 'of a hunting scene', 'of architecture', 'of a botanical illustration', 'of a battle scene', 'of courtly life', f'{choice(marine)}', 'of a barbarian', 'of a soldier', 'of a knight', 'of a paladin']
tapestry = [
    'of a hunting scene', 'of a battle scene', 'of a religious story', 'of a mythological figure', 'of a biblical story', 'of a historical event', 'of courtly life', 'of a natural landscape', 'of a cityscape', 'of a garden', f'{choice(animal)} portrait', 'of a royal or noble family tree', 'of a celestial map', 'of a divine symbol', 'of a landscape with architectural ruins', 'of a seascape', 'of a genre scene with musicians', 'of a natural disaster', 'of a tapestry weaver in action']
bust = [
    'of a famous historical figure', 'of a wizard', 'of a bard', 'of a king', 'of a military hero', 'of a queen', 'of a sculptor', 'of a fictional character', f'of a beloved pet {choice(pet)}', 'of a wealthy female patron', 'of a barbarian', 'of a soldier', 'of a knight', 'of a paladin', "of Aurilis, the Sun God", "of Gorin, the Mountain God", "of Lyriel, the Forest Goddess", "of Oneiros, the Dream God", "of Freya, the Hearth Goddess"]
sculpture = [
    'of a religious figure', 'of a mythological figure', f'{choice(bust)}', 'of a full-body nude', f'{choice(animal)}', 'of a building', 'of a historical figure', 'of a child', 'of a religious symbol', 'of a military hero', 'of a wizard', 'of a bard', 'of a dancer', f'{choice(marine)}', 'of an abstract or geometric form', 'of a fictional character', 'of a barbarian', 'of a soldier', 'of a knight', 'of a paladin']
mundane_data = {
    "Candelabra": {
        "base_price": 100,
        "materials": {"metal": 0.7, "natural hard material": 0.3, "wood": 1},
        "weight": 2
    },
    "Goblet": {
        "base_price": 10,
        "materials": {"metal": 1, "stone": 0.2},
        "weight": 2
    },
    f"Oil Painting {choice(painting)}": {
        "base_price": 1000,
        "materials": {"": 1},
        "weight": 1
    },
    f"Tapestry {choice(tapestry)}": {
        "base_price": 1000,
        "materials": {"fabric": 1},
        "weight": 1
    },
    f"Statuette {choice(animal)}": {
        "base_price": 2000,
        "materials": {"natural hard material": 1},
        "weight": 1
    },
    f"Statuette {choice(monster)}": {
        "base_price": 2000,
        "materials": {"natural hard material": 1},
        "weight": 1
    },
    "Carpet": {
        "base_price": 3000,
        "materials": {"fabric": 0.7, "fur": 0.3},
        "weight": 1
    },
    "Chandelier": {
        "base_price": 5000,
        "materials": {"metal": 0.5, "wood": 0.5},
        "weight": 1
    },
    f"Small Sculpture {choice(sculpture)}": {
        "base_price": 200,
        "materials": {"natural hard material": 1},
        "weight": 1
    },
    "Scarf": {
        "base_price": 50,
        "materials": {"fabric": 0.7, "fur": 0.3},
        "weight": 2
    },
    "Chess Set": {
        "base_price": 1000,
        "materials": {"natural hard material": 0.7, "metal": 0.3, "stone": 1},
        "weight": 1
    },
    f"Bust {choice(bust)}": {
        "base_price": 5000,
        "materials": {"stone": 1, "metal": 0.2},
        "weight": 1
    },
    "Vase": {
        "base_price": 1000,
        "materials": {"metal": 0.5, "stone": 0.8},
        "weight": 1
    },
    "Robe": {
        "base_price": 200,
        "materials": {"fabric": 0.7, "fur": 0.3},
        "weight": 1
    },
    "Candlestick holder": {
        "base_price": 10,
        "materials": {"metal": 0.8, "natural hard material": 0.2, "wood": 1.2},
        "weight": 2
    },
    "Mirror": {
        "base_price": 1500,
        "materials": {"metal": 1},
        "weight": 1
    },
    "Parasol": {
        "base_price": 100,
        "materials": {"": 1},
        "weight": 2
    },
    "Cloak": {
        "base_price": 1000,
        "materials": {"fabric": 0.7, "fur": 0.3},
        "weight": 1
    },
    "Chalice": {
        "base_price": 1000,
        "materials": {"metal": 0.7, "natural hard material": 0.3},
        "weight": 1
    },
    f"Antique Portrait {choice(bust)}": {
        "base_price": 2500,
        "materials": {"": 1},
        "weight": 1
    },
    "Decorative Box": {
        "base_price": 1500,
        "materials": {"wood": 0.4, "metal": 0.5, "stone": 0.1},
        "weight": 2
    },
    "Music Box": {
        "base_price": 500,
        "materials": {"natural hard material": 0.5, "metal": 0.4, "wood": 0.1},
        "weight": 1
    },
    "Ornate Picture Frame": {
        "base_price": 500,
        "materials": {"wood": 0.9, "metal": 0.1},
        "weight": 3
    },
    f"Sculpted Figurine {choice(bust)}": {
        "base_price": 1200,
        "materials": {"wood": 0.3, "metal": 0.5, "stone": 1},
        "weight": 2
    },
    f"Sculpted Figurine {choice(monster)}": {
        "base_price": 1200,
        "materials": {"wood": 0.8, "metal": 0.5, "stone": 1},
        "weight": 2
    },
    "Altar to Aurilis, depicting a sunrise": {
        "base_price": 250,
        "materials": {"stone": 0.2, "wood": 0.8},
        "weight": 0.6
    },
    "Altar to Lyriel, adorned with flowers and vines": {
        "base_price": 300,
        "materials": {"wood": 1},
        "weight": 0.7
    },
    "Carving of Glimmer, depicting a mischievous grin": {
        "base_price": 150,
        "materials": {"wood": 0.9, "stone": 0.1},
        "weight": 0.3
    },
    "Tapestry of Oneiros, showing a fantastical dream world": {
        "base_price": 500,
        "materials": {"fabric": 0.1},
        "weight": 0.8
    },
    "Statue of Gorin, hewn from a single block": {
        "base_price": 1000,
        "materials": {"stone": 1.0},
        "weight": 0.9
    },
    "Carving of Freya, inlaid with gold and silver": {
        "base_price": 400,
        "materials": {"wood": 0.8, "metal": 0.2},
        "weight": 0.7
    },
    "Tome of Ancient Wisdom, inscribed with runes of Tiamat": {
        "base_price": 800,
        "materials": {"": 1},
        "weight": 0.1
    }
}


def provenances():
    provenance = choices(list(provenanced.keys()),
                         weights=list(provenanced.values()))[0]
    return provenance


def mundane():

    condition = choices(list(condition_data.keys()), [
                        conditions["weight"] for conditions in condition_data.values()])[0]
    condition_price = condition_data[condition]["price"]
    item = choices(list(mundane_data.keys()), [
                   items["weight"] for items in mundane_data.values()])[0]
    item_material_type = choices(list(mundane_data[item]["materials"].keys(
    )), weights=list(mundane_data[item]["materials"].values()))[0]
    item_material = choices(list(material_dict[item_material_type].keys()), [
                            materials["rarity"] for materials in material_dict[item_material_type].values()])[0]
    item_price = mundane_data[item]["base_price"]
    if item_material != "":
        material_price = material_dict[item_material_type][item_material]["price"]
        mundane_price = (item_price*material_price*condition_price)/100
    else:
        mundane_price = (item_price*condition_price)
    provenance = provenances()
    provenance_m = provenance
    return item, condition, item_material, mundane_price, provenance_m

# def weapons_armour():
    lol


def jewellery():
    condition = choices(list(condition_data.keys()), [
                        conditions["weight"] for conditions in condition_data.values()])[0]
    condition_price = condition_data[condition]["price"]
    gem_list = choices(list(gem_data.values()),  [
                       gems["weight"] for gems in gem_data.values()])[0]
    if gem_list["gems"] != "":
        gem = choice(gem_list["gems"])
        gem_price = sum(randint(1, 4) for _ in range(
            gem_list["rolls"]+1)) * gem_list["multiplier"]
    else:
        gem = ""
        gem_price = 1
    item = choices(list(item_data.keys()), [
                   items["weight"] for items in item_data.values()])[0]
    item_price = item_data[item]["price"]
    condition = choices(list(condition_data.keys()), [
                        conditions["weight"] for conditions in condition_data.values()])[0]
    condition_price = condition_data[condition]["price"]
    material = choices(list(Jewellery_materials.keys()), [
                       materials["weight"] for materials in Jewellery_materials.values()])[0]
    material_price = Jewellery_materials[material]["price"]
    if gem != "":
        conjunction = choice(conjunctions)
    else:
        conjunction = ""
    provenance = provenances()
    provenance_j = provenance
    jewellery_price = (item_price*material_price)+(gem_price*condition_price)
    return gem, condition, item, conjunction, material, jewellery_price, provenance_j


def gems():
    condition = choices(list(condition_data.keys()), [
                        conditions["weight"] for conditions in condition_data.values()])[0]
    condition_price = condition_data[condition]["price"]
    gem_list = choices(list(gem_data.values()),  [
                       gems["weight"] for gems in gem_data.values()])[0]
    if gem_list["gems"] != "":
        gem_ = choice(gem_list["gems"])
        gem_price = (sum(randint(1, 4) for _ in range(
            gem_list["rolls"]+1)) * gem_list["multiplier"])*condition_price
    else:
        gem_ = ""
        gem_price = 1
    return condition, gem_, gem_price


def magical(challenge):

    magic_A = {
        "Potion of Healing": 50, f"Spell scroll ({choice(spells['cantrips'])})": 9, "Potion of Climbing": 9, f"Spell scroll ({choice(spells['1st'])})": 9, f"Spell scroll ({choice(spells['2nd'])})": 3, "Potion of Greater Healing": 3, "Bag of Holding": 1, "Driftglobe": 1
    }
    magic_B = {
        "Potion of Greater Healing": 15, "Potion of Fire Breath": 6, "Potion of Resistance": 6, "Arrows (5), +1": 4, "Potion of Animal Friendship": 4, "Potion of Hill Giant Strength": 4, "Potion of Growth": 4, "Potion of Water Breathing": 4, f"Spell scroll ({choice(spells['2nd'])})": 4, f"Spell scroll ({choice(spells['3rd'])})": 4, "Bag of Holding": 2, "Keoghtom's Ointment": 2, "Oil of Slipperiness": 2, "Dust of Disappearance": 1, f"Dust of Dryness ({randint(1,6)+4} uses)": 1, "Dust of Sneezing and Choking": 1, "Elemental Gem": 1, "Philter of Love": 1, "Alchemy Jug": 1, "Cap of Water Breathing": 1, "Cloak of the Manta Ray": 1, "Driftglobe": 1, "Goggles of Night": 1, "Helm of Comprehending Languages": 1, "Immovable Rod": 1, "Lantern of Revealing": 1, f"Mariner's {choice(armour['h']+armour['m2']+armour['m1']+armour['l'])}": 1, f"Mithral {choice(armour['m2']+armour['h'])}": 1, "Potion of Poison": 1, "Ring of Swimming": 1, "Robe of Useful Items": 1, "Rope of Climbing": 1, "Saddle of the Cavalier": 1, "Wand of Magic Detection": 1, "Wand of Secrets": 1
    }
    magic_C = {
        "Potion of Superior Healing": 15, f"Spell scroll ({choice(spells['4th'])})": 7, "Arrows (5), +2": 4, "Potion of Clairvoyance": 4, "Potion of Diminution": 4, "Potion of Gaseous Form": 4, "Potion of Frost Giant Strength": 4, "Potion of stone Giant Strength": 4, "Potion of Heroism": 4, "Potion of Invulnerability": 4, "Potion of Mind Reading": 4, f"Spell scroll ({choice(spells['5th'])})": 4, "Elixir of Health": 2, "Oil of Etherealness": 2, "Potion of Fire Giant Strength": 2, f"Quaal's Feather Token ({choice(Qaals_tokens)})": 2, "Scroll of Protection": 2, f"Bag of Beans ({bean_num}: {string_beans})": 2, "Bead of Force": 2, "Chime of Opening": 1, "Decanter of Endless Water": 1, "Eyes of Minute Seeing": 1, "Folding Boat": 1, "Heward's Handy Haversack": 1, "Horseshoes of Speed": 1, f"Necklace of Fireballs ({randint(1,6)+3} beads left)": 1, "Periapt of Health": 1, "Sending stones": 1
    }
    magic_D = {
        "Potion of Supreme Healing": 20, "Potion of Invisibility": 10, "Potion of Speed": 10, f"Spell scroll ({choice(spells['6th'])})": 10, f"Spell scroll ({choice(spells['7th'])})": 7, "Arrows (5), +3": 5, "Oil of Sharpness": 5, "Potion of Flying": 5, "Potion of Cloud Giant Strength": 5, "Potion of Longevity": 5, "Potion of Vitality": 5, f"Spell scroll ({choice(spells['8th'])})": 5, "Horseshoes of a Zephyr": 3, f"Nolzur's Marvelous Pigments ({randint(1,4)} pots)": 3, "Bag of Devouring": 1, "Portable Hole": 1
    }
    magic_E = {
        f"Spell scroll ({choice(spells['8th'])})": 30, "Potion of Storm Giant Strength": 25, "Potion of Supreme Healing": 15, f"Spell scroll ({choice(spells['9th'])})": 15, "Universal Solvent": 8, "Arrow of Slaying": 5, "Sovereign Glue": 2
    }
    magic_F = {
        f"{choice(list(weapon['m'].keys())+list(weapon['s'].keys()))} +1": 15, "Shield +1": 3, "Sentinel Shield": 3, "Amulet of Proof Against Detection and Location": 2, "Boots of Elvenkind": 2, "Boots of Striding and Springing": 2, "Bracers of Archery": 2, "Brooch of Shielding": 2, "Broom of Flying": 2, "Cloak of Elvenkind": 2, "Cloak of Protection": 2, "Gauntlets of Ogre Power": 2, "Hat of Disguise": 2, "Javelin of Lightning": 2, "Pearl of Power": 2, "Rod of the Pact Keeper +1": 2, "Slippers of Spider Climbing": 2, "Staff of the Adder": 2, "Staff of the Python": 2, f"{choice(weapon['sword'])} of Vengeance": 2, "Trident of Fish Command": 2, "Wand of Magic Missiles": 2, "Wand of the War Mage +1": 2, "Wand of Web": 2, f"{choice(list(weapon['m'].keys())+list(weapon['s'].keys()))} of Warning": 2, "Adamantine armor (Chain Mail)": 1, "Adamantine armor (Chain Shirt)": 1, "Adamantine armor (Scale Mail)": 1, "Bag of Tricks (gray)": 1, "Bag of Tricks (rust)": 1, "Bag of Tricks (tan)": 1, "Boots of the Winterlands": 1, "Circlet of Blasting": 1, f"Deck of Illusions ({34-(randint(1,20)-1)} cards)": 1, "Eversmoking Bottle": 1, "Eyes of Charming": 1, "Eyes of the Eagle": 1, "Figurine of Wondrous Power (silver raven)": 1, "Gem of Brightness": 1, "Gloves of Missile Snaring": 1, "Gloves of Swimming and Climbing": 1, "Gloves of Thievery": 1, "Headband of Intellect": 1, "Helm of Telepathy": 1, "Instrument of the Bards (Doss Lute)": 1, "Instrument of the Bards (Fochlucan Bandore)": 1, "Instrument of the Bards (Mac-Fuimidh Cittern)": 1, "Medallion of Thoughts": 1, "Necklace of Adaptation": 1, "Periapt of Wound Closure": 1, "Pipes of Haunting": 1, "Pipes of the Sewers": 1, "Ring of Jumping": 1, "Ring of Mind Shielding": 1, "Ring of Warmth": 1, "Ring of Water Walking": 1, "Quiver of Ehlonna": 1, "stone of Good Luck (Luckstone)": 1, "Wind Fan": 1, "Winged Boots": 1,
    }
    magic_G = {
        f"{choice(list(weapon['m'].keys())+list(weapon['s'].keys()))}, +2": 11, f"Figurine of Wondrous Power ({choices(list(Fig_wondrous.keys()), weights=list(Fig_wondrous.values()))[0]})": 3, "Adamantine armor (Breastplate)": 1, "Adamantine armor (Splint)": 1, "Amulet of Health": 1, "Plate Armor of Vulnerability": 1, "Arrow-Catching Shield": 1, "Belt of Dwarvenkind": 1, "Belt of Hill Giant Strength": 1, "Berserker Axe": 1, "Boots of Levitation": 1, "Boots of Speed": 1, "Bowl of Commanding Water Elementals": 1, "Bracers of Defense": 1, "Brazier of Commanding Fire Elementals": 1, "Cape of the Mountebank": 1, "Censer of Controlling Air Elementals": 1, "Chainmail, +1": 1, "Armor of Resistance (Chain Mail)": 1, "Armor of Resistance (Chain Shirt)": 1, "Chain Shirt, +1": 1, "Cloak of Displacement": 1, "Cloak of the Bat": 1, "Cube of Force": 1, "Daern's Instant Fortress": 1, "Dagger of Venom": 1, "Dimensional Shackles": 1, f"Dragon Slayer ({choice(weapon['sword'])})": 1, "Elven Chain": 1, f"Flame Tongue ({choice(weapon['sword'])})": 1, "Gem of Seeing": 1, f"Giant Slayer ({choice(weapon['axe']+weapon['sword'])})": 1, "Glamoured Studded Leather": 1, "Helm of Teleportation": 1, "Horn of Blasting": 1, f"Horn of Valhalla ({choices(list(Valhalla_horns.keys()), weights=list(Valhalla_horns.values()))[0]})": 1, "Instrument of the Bards (Canaith Mandolin)": 1, "Instrument of the Bards (Cii Lyre)": 1, "Ioun stone (Awareness)": 1, "Ioun stone (Protection)": 1, "Ioun stone (Reserve)": 1, "Ioun stone (Sustenance)": 1, "Iron Bands of Bilarro": 1, "Leather Armour, +1": 1, "Armor of Resistance (Leather)": 1, "Mace of Disruption": 1, "Mace of Smiting": 1, "Mace of Terror": 1, "Mantle of Spell Resistance": 1, "Necklace of Prayer Beads": 1, "Periapt of Proof Against Poison": 1, "Ring of Animal Influence": 1, "Ring of Evasion": 1, "Ring of Feather Falling": 1, "Ring of Free Action": 1, "Ring of Protection": 1, "Ring of Resistance": 1, "Ring of Spell Storing": 1, "Ring of the Ram": 1, "Ring of X-ray Vision": 1, "Robe of Eyes": 1, "Rod of Rulership": 1, "Rod of the Pact Keeper, +2": 1, "Rope of Entanglement": 1, "Armor +1 (Scale Mail)": 1, "Armor of Resistance (Scale Mail)": 1, "Shield +2": 1, "Shield of Missile Attraction": 1, "Staff of Charming": 1, "Staff of Healing": 1, "Staff of Swarming Insects": 1, "Staff of the woodlands": 1, "Staff of Withering": 1, "stone of Controlling Earth Elementals": 1, "Sun Blade": 1, f"{choice(weapon['sword'])} of Life Stealing": 1, f"{choice(weapon['sword'])} of Wounding": 1, "Tentacle Rod": 1, f"Vicious {choice(list(weapon['m'].keys())+list(weapon['s'].keys()))}": 1, "Wand of Binding": 1, "Wand of Enemy Detection": 1, "Wand of Fear": 1, "Wand of Fireballs": 1, "Wand of Lightning Bolts": 1, "Wand of Paralysis": 1, "Wand of the War Mage +2": 1, "Wand of Wonder": 1, "Wings of Flying": 1
    }
    magic_H = {
        f"{choice(list(weapon['m'].keys())+list(weapon['s'].keys()))} +3": 10, "Amulet of the Planes": 3, "Carpet of Flying": 2, "Crystal Ball": 2, "Ring of Regeneration": 2, "Ring of Shooting Stars": 2, "Ring of Telekinesis": 2, "Robe of Scintillating Colors": 2, "Robe of Stars": 2, "Rod of Absorption": 2, "Rod of Alertness": 2, "Rod of Security": 2, "Rod of the Pact Keeper +3": 2, "Scimitar of Speed": 2, "Shield +3": 2, "Staff of Fire": 2, "Staff of Frost": 2, "Staff of Power": 2, "Staff of Striking": 2, "Staff of Thunder and Lightning": 2, f"{choice(weapon['sword'])} of Sharpness": 2, "Wand of Polymorph": 2, "Wand of the War Mage +3": 2, "Adamantine armor (Half Plate)": 2, "Adamantine armor (Plate)": 1, "Animated shield": 1, "Belt of Fire Giant Strength": 1, f"{choice(Belt_f_s)}": 1, "Breastplate, +1": 1, "Armor of Resistance (Breastplate)": 1, f"Candle of Invocation ({choices(list(candle_invokation.keys()), weights=list(candle_invokation.values()))[0]})": 1, "Chain Mail, +2": 1, "Chain Shirt, +2": 1, "Cloak of Arachnida": 1, f"Dancing {choice(weapon['sword'])}": 1, "Demon Armor": 1, "Dragon Scale Mail": 1, "Dwarven Plate": 1, "Dwarven Throwing Hammer": 1, "Efreeti Bottle": 1, "Figurine of Wondrous Power (Obsidian Steed)": 1, "Frost Brand": 1, "Helm of Brilliance": 1, "Horn of Valhalla (Bronze)": 1, "Instrument of the Bards (Anstruth Harp)": 1, "Ioun stone (Absorption)": 1, "Ioun stone (Agility)": 1, "Ioun stone (Fortitude)": 1, "Ioun stone (Insight)": 1, "Ioun stone (Intellect)": 1, "Ioun stone (Leadership)": 1, "Ioun stone (Strength)": 1, "Leather Armour, +2": 1, "Manual of Bodily Health": 1, "Manual of Gainful Exercise": 1, "Manual of Golems": 1, "Manual of Quickness of Action": 1, "Mirror of Life Trapping": 1, "Nine Lives Stealer": 1, "Oathbow": 1, "Scale Mail, +2": 1, "Spellguard Shield": 1, "Splint Armour, +1": 1, "Armor of Resistance (Splint)": 1, "Studded Leather, +1": 1, "Armor of Resistance (Studded Leather)": 1, "Tome of Clear Thought": 1, "Tome of Leadership and Influence": 1, "Tome of Understanding": 1,
    }
    magic_I = {
        f"Defender ({choice(weapon['sword'])})": 5, "Hammer of Thunderbolts": 5, f"Luck Blade ({choice(weapon['sword'])})": 5, "Sword of Answering": 5, f"Holy Avenger ({choice(weapon['sword'])})": 3, "Ring of Djinni Summoning": 3, "Ring of Invisibility": 3, "Ring of Spell Turning": 3, "Rod of Lordly Might": 3, "Staff of the Magi": 3, f"Vorpal {choice(weapon['sword'])}": 3, "Belt of Cloud Giant Strength": 2, "Breastplate, +2": 2, "Chain Mail, +3": 2, "Chain Shirt, +3": 2, "Cloak of Invisibility": 2, f"Crystal Ball ({choice(Legendary_crystal_ball)})": 2, "Half Plate, +1": 2, f"Iron Flask ({choices(list(Iron_flask.keys()), weights=list(Iron_flask.values()))[0]})": 2, "Leather Armour, +3": 2, "Plate, +1": 2, "Robe of the Archmagi": 2, "Rod of Resurrection": 2, "Scale Mail, +1": 2, "Scarab of Protection": 2, "Splint Armour, +2": 2, "Studded Leather, +2": 2, "Well of Many Worlds": 2, f"{choices(list(magic_armour.keys()), weights=list(magic_armour.values()))[0]}": 1, "Apparatus of Kwalish": 1, "Armor of Invulnerability": 1, "Belt of Storm Giant Strength": 1, "Cubic Gate": 1, f"Deck of Many Things ({choice(domt['material'])}, {choices(list(domt['cards'].keys()), weights=list(domt['cards'].values()))[0]})": 1, "Efreeti Chain": 1, "Armor of Resistance (Half Plate)": 1, "Horn of Valhalla (Iron)": 1, "Instrument of the Bards (Ollamh Harp)": 1, "Ioun stone (Greater Absorption)": 1, "Ioun stone (Mastery)": 1, "Ioun stone (Regeneration)": 1, "Plate Armor of Etherealness": 1, "Armor of Resistance (Plate)": 1, "Ring of Air Elemental Command": 1, "Ring of Earth Elemental Command": 1, "Ring of Fire Elemental Command": 1, "Ring of Three Wishes": 1, "Ring of Water Elemental Command": 1, "Sphere of Annihilation": 1, "Talisman of Pure Good": 1, "Talisman of the Sphere": 1, "Talisman of Ultimate Evil": 1, "Tome of the Stilled Tongue": 1,
    }

    if challenge < 6:
        magic_choices = [
            (magic_A, 0.25),
            (magic_B, 0.15),
            (magic_C, 0.1),
            (magic_F, 0.12),
            (magic_G, 0.03),
            (None, 0.35)
        ]
        magic_dict, weight = choices(magic_choices, weights=[
                                     w for d, w in magic_choices])[0]
        if magic_dict is not None:
            magic_item = choices(list(magic_dict.keys()),
                                 weights=list(magic_dict.values()))[0]
        else:
            return None

    elif challenge < 11:
        magic_choices = [
            (magic_A, 0.15),
            (magic_B, 0.18),
            (magic_C, 0.1),
            (magic_F, 0.1),
            (magic_G, 0.03),
            (magic_H, 0.02),
            (None, 0.28)
        ]
        magic_dict, weight = choices(magic_choices, weights=[
                                     w for d, w in magic_choices])[0]
        if magic_dict is not None:
            magic_item = choices(list(magic_dict.keys()),
                                 weights=list(magic_dict.values()))[0]
            return magic_item, magic_dict is magic_H, magic_dict is magic_D
        else:
            return None, False, False

    elif challenge < 16:
        magic_choices = [
            (magic_A, 0.13),
            (magic_B, 0.13),
            (magic_C, 0.2),
            (magic_D, 0.15),
            (magic_E, 0.07),
            (magic_F, 0.07),
            (magic_G, 0.07),
            (magic_H, 0.09),
            (magic_I, 0.07),
            (None, 0.15)
        ]
        magic_dict, weight = choices(magic_choices, weights=[
                                     w for d, w in magic_choices])[0]
        if magic_dict is not None:
            magic_item = choices(list(magic_dict.keys()),
                                 weights=list(magic_dict.values()))[0]
            return magic_item, magic_dict is magic_E, magic_dict is magic_F, magic_dict is magic_I
        else:
            return None, False, False, False

    elif challenge > 16:
        magic_choices = [
            (magic_A, 0),
            (magic_B, 0),
            (magic_C, 0.12),
            (magic_D, 0.32),
            (magic_E, 0.22),
            (magic_F, 0),
            (magic_G, 0.04),
            (magic_H, 0.08),
            (magic_I, 0.20),
            (None, 0.02)
        ]
        magic_dict, weight = choices(magic_choices, weights=[
                                     w for d, w in magic_choices])[0]
        if magic_dict is not None:
            magic_item = choices(list(magic_dict.keys()),
                                 weights=list(magic_dict.values()))[0]
            return magic_item
        else:
            return None

    return magic_item


def coins(challenge):
    if challenge < 6:
        copper = sum(randint(0, 6) for _ in range(0, 6)) * \
            round(100*(randint(75, 125)/100))
        silver = sum(randint(0, 6) for _ in range(0, 3)) * \
            round(100*(randint(75, 125)/100))
        electrum = sum(randint(0, 4) for _ in range(0, 2))
        gold = sum(randint(0, 6) for _ in range(0, 2)) * \
            round(10*(randint(75, 105)/100))
        platinum = sum(randint(0, 2) for _ in range(0, 1))
        total = (platinum*10)+gold+(electrum/2)+(silver/10)+(copper/100)
        print(
            f"\nCoins:\n{copper}cp, {silver}sp, {electrum}ep, {gold}gp, {platinum}pp")
        print(f"Total: {total:,.2f}gp\n")
    elif challenge < 11:
        copper = sum(randint(1, 6) for _ in range(0, 2)) * \
            round(100*(randint(75, 125)/100))
        silver = sum(randint(1, 6) for _ in range(0, 2)) * \
            round(1000*(randint(75, 125)/100))
        electrum = sum(randint(1, 6) for _ in range(0, 6))
        gold = sum(randint(1, 6) for _ in range(0, 6)) * \
            round(100*(randint(75, 125)/100))
        platinum = sum(randint(0, 6) for _ in range(0, 3)) * \
            round(10*(randint(75, 105)/100))
        total = (platinum*10)+gold+(electrum/2)+(silver/10)+(copper/100)
        print(
            f"\nCoins:\n{copper}cp, {silver}sp, {electrum}ep, {gold}gp, {platinum}pp")
        print(f"Total: {total:,.2f}gp\n")
    elif challenge < 16:
        copper = sum(randint(1, 6) for _ in range(0, 4)) * \
            round(100*(randint(75, 105)/100))
        silver = sum(randint(1, 6) for _ in range(0, 4)) * \
            round(100*(randint(75, 105)/100))
        electrum = sum(randint(1, 6) for _ in range(0, 4)) * \
            round(10*(randint(75, 125)/100))
        gold = sum(randint(1, 6) for _ in range(0, 4)) * \
            round(900*(randint(75, 125)/100))
        platinum = sum(randint(1, 6) for _ in range(0, 5)) * \
            round(100*(randint(75, 105)/100))
        total = (platinum*10)+gold+(electrum/2)+(silver/10)+(copper/100)
        print(
            f"\nCoins:\n{copper}cp, {silver}sp, {electrum}ep, {gold}gp, {platinum}pp")
        print(f"Total: {total:,.2f}gp\n")
    elif challenge > 16:
        copper = 0
        silver = 0
        electrum = 0
        gold = sum(randint(1, 6) for _ in range(0, 12)) * \
            round(1000*(randint(75, 125)/100))
        platinum = sum(randint(1, 6) for _ in range(0, 8)) * \
            round(1000*(randint(72, 105)/100))
        total = (platinum*10)+gold+(electrum/2)+(silver/10)+(copper/100)
        print(
            f"\nCoins:\n{copper}cp, {silver}sp, {electrum}ep, {gold}gp, {platinum}pp")
        print(f"Total: {total:,.2f}gp\n")
    return total


def select():

    while True:
        try:
            challenge = int(input("\nEnter Challenge Rating: "))
            return challenge
        except (ValueError, IndexError):
            print("Invalid input. Please choose a valid option.")
            continue


def hoard(challenge):
    if challenge < 6:
        print("\nTreasure Hoard A")
        coin_total = coins(challenge)
        print("Gems:\n")
        gem_total = 0
        for _ in range(0, randint(0, 6)):
            condition, gem_, gem_price = gems()
            if gem_ != "":
                print(f"{condition} quality {gem_}: {gem_price:,.2f}gp")
                gem_total += gem_price
        print(f"\nTotal value of gems: {gem_total:,.2f}gp")
        print("")
        print("Jewellery:\n")
        jewels_total = 0
        for _ in range(0, randint(0, 6)):
            gem, condition, item, conjunction, material, jewellery_price, provenance_j = jewellery()
            print(
                f"{condition} quality {material} {item}{conjunction}{gem}: {jewellery_price:,.2f}gp")
            jewels_total += jewellery_price
            if provenance_j != "":
                print(f"{provenance_j}")
        print(f"\nTotal value of Jewellery: {jewels_total:,.2f}gp")
        print("")
        print("Mundane items:\n")
        mundane_total = 0
        for _ in range(0, randint(0, 2)):
            for _ in range(0, 6):
                item, condition, item_material, mundane_price, provenance_m = mundane()
                print(
                    f"{condition} quality {item_material}{item}: {mundane_price:,.2f}gp")
                mundane_total += mundane_price
                if provenance_m != "":
                    print(f"{provenance_m}")
        print(f"\nTotal value of mundane items: {mundane_total:,.2f}gp")
        print(
            f"\nTotal Hoard value: {gem_total+coin_total+jewels_total+mundane_total:,.2f}gp")
        print("")
        print("Magic items:\n")
        for _ in range(0, randint(0, 6)):
            magic_item = magical(challenge)
            if magic_item != None:
                print(f"{magic_item}")
        print("")

    elif challenge < 11:
        print("\nTreasure Hoard B")
        coin_total = coins(challenge)
        print("Gems:\n")
        gem_total = 0
        for _ in range(0, randint(0, 3)):
            for _ in range(0, randint(0, 6)):
                condition, gem_, gem_price = gems()
                if gem_ != "":
                    print(f"{condition} quality {gem_}: {gem_price:,.2f}gp")
                    gem_total += gem_price
        print(f"\nTotal value of gems: {gem_total:,.2f}gp")
        print("")
        print("Jewellery:\n")
        jewels_total = 0
        for _ in range(0, 2):
            for _ in range(0, randint(0, 6)):
                gem, condition, item, conjunction, material, jewellery_price, provenance_j = jewellery()
                print(
                    f"{condition} quality {material} {item}{conjunction}{gem}: {jewellery_price:,.2f}gp")
                jewels_total += jewellery_price
                if provenance_j != "":
                    print(f"{provenance_j}")
        print(f"\nTotal value of Jewellery: {jewels_total:,.2f}gp")
        print("")
        print("Mundane items:\n")
        mundane_total = 0
        for _ in range(0, randint(0, 3)):
            for _ in range(0, 6):
                item, condition, item_material, mundane_price, provenance_m = mundane()
                print(
                    f"{condition} quality {item_material}{item}: {mundane_price:,.2f}gp")
                mundane_total += mundane_price
                if provenance_m != "":
                    print(f"{provenance_m}")
        print(f"\nTotal value of mundane items: {mundane_total:,.2f}gp")
        print(
            f"\nTotal Hoard value: {gem_total+coin_total+jewels_total+mundane_total:,.2f}gp")
        print("")
        print("Magic items:\n")
        for _ in range(0, randint(1, 6)):
            magic_item, from_H, from_D = magical(challenge)
            if from_H or from_D:
                print(f"Special item!: {magic_item}")
                break
            elif magic_item != None:
                print(f"{magic_item}")
        print("")

    elif challenge < 16:
        print("\nTreasure Hoard C")
        coin_total = coins(challenge)
        print("Gems:\n")
        gem_total = 0
        for _ in range(0, randint(1, 4)):
            for _ in range(0, randint(0, 6)):
                condition, gem_, gem_price = gems()
                if gem_ != "":
                    print(f"{condition} quality {gem_}: {gem_price:,.2f}gp")
                    gem_total += gem_price
        print(f"\nTotal value of gems: {gem_total:,.2f}gp")
        print("")
        print("Jewellery:\n")
        jewels_total = 0
        for _ in range(1, 2):
            for _ in range(0, randint(0, 6)):
                gem, condition, item, conjunction, material, jewellery_price, provenance_j = jewellery()
                print(
                    f"{condition} quality {material} {item}{conjunction}{gem}: {jewellery_price:,.2f}gp")
                jewels_total += jewellery_price
                if provenance_j != "":
                    print(f"{provenance_j}")
        print(f"\nTotal value of Jewellery: {jewels_total:,.2f}gp")
        print("")
        print("Mundane items:\n")
        mundane_total = 0
        for _ in range(0, randint(1, 3)):
            for _ in range(0, 6):
                item, condition, item_material, mundane_price, provenance_m = mundane()
                print(
                    f"{condition} quality {item_material}{item}: {mundane_price:,.2f}gp")
                mundane_total += mundane_price
                if provenance_m != "":
                    print(f"{provenance_m}")
        print(f"\nTotal value of mundane items: {mundane_total:,.2f}gp")
        print(
            f"\nTotal Hoard value: {gem_total+coin_total+jewels_total+mundane_total:,.2f}gp")
        print("")
        print("Magic items:\n")
        for _ in range(0, randint(1, 6)):
            magic_item, from_E, from_F, from_I = magical(challenge)
            if from_E or from_F or from_I:
                print(f"Special item!: {magic_item}")
                break
            elif magic_item != None:
                print(f"{magic_item}")
        print("")

    elif challenge > 16:
        print("\nTreasure Hoard D")
        coin_total = coins(challenge)
        print("Gems:\n")
        gem_total = 0
        for _ in range(0, randint(1, 4)):
            for _ in range(0, randint(0, 6)):
                condition, gem_, gem_price = gems()
                if gem_ != "":
                    print(f"{condition} quality {gem_}: {gem_price:,.2f}gp")
                    gem_total += gem_price
        print(f"\nTotal value of gems: {gem_total:,.2f}gp")
        print("")
        print("Jewellery:\n")
        jewels_total = 0
        for _ in range(0, 2):
            for _ in range(0, randint(1, 8)):
                gem, condition, item, conjunction, material, jewellery_price, provenance_j = jewellery()
                print(
                    f"{condition} quality {material} {item}{conjunction}{gem}: {jewellery_price:,.2f}gp")
                jewels_total += jewellery_price
                if provenance_j != "":
                    print(f"{provenance_j}")
        print(f"\nTotal value of Jewellery: {jewels_total:,.2f}gp")
        print("")
        print("Mundane items:\n")
        mundane_total = 0
        for _ in range(0, randint(1, 3)):
            for _ in range(1, 10):
                item, condition, item_material, mundane_price, provenance_m = mundane()
                print(
                    f"{condition} quality {item_material}{item}: {mundane_price:,.2f}gp")
                mundane_total += mundane_price
                if provenance_m != "":
                    print(f"{provenance_m}")
        print(f"\nTotal value of mundane items: {mundane_total:,.2f}gp")
        print(
            f"\nTotal Hoard value: {gem_total+coin_total+jewels_total+mundane_total:,.2f}gp")
        print("")
        print("Magic items:\n")
        for _ in range(0, randint(1, 6)):
            magic_item = magical(challenge)
            if magic_item != None:
                print(f"{magic_item}")
        print("")

    while True:
        answer = input("\nRoll for more treasure? y/n: ")
        if answer == "y":
            lootgen()
            break
        elif answer == "n":
            print("\nWhat Would Gygax Do?")
            exit()
        else:
            print("\nInvalid input, try again.")
            continue


def lootgen():
    challenge = select()
    # generate=["Coins", "Gems", "Jewellery", "Mundane items", "Magic items", "Hoards"]
    # for i, v in enumerate(generate):
    #     print(i,v)
    # while True:
    #     choose=input("Choose a generator: ")

    hoard(challenge)


title()
lootgen()
