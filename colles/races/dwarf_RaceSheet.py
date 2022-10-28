Race = 'Dwarf'
Subraces = ['hill dwarf', 'mountain elf', 'Duergar', 'Mark of Warding']
ability_improve = ['Con +2']
speed = 25
darkvision = 60

languages = ['common', 'dwarvish']
features = ['Dwarven Resilience. You have advantage on saving throws against poison, and you have resistance against poison damage.',
            'Dwarven Combat Training. You have proficiency with the battleaxe, handaxe, light hammer, and warhammer.',
            "Tool Proficiency. You gain proficiency with the artisan's tools of your choice: smith's tools, brewer's supplies, or mason's tools.",
            "Stonecunning. Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus."]


def hilldwarf_edit():
    sub_featurs = [
        "Dwarven Toughness. Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."]
    ability_improve.append(' Wis +1')
    features.append(sub_featurs)


def mountaindwarf_edit():
    global speed
    sub_featurs = [
        "Dwarven Armor Training. You have proficiency with light and medium armor."]
    ability_improve.append(' Str +2')
    features.append(sub_featurs)


def Duergar_edit():
    global darkvision
    sub_featurs = ["Duergar Resilience. You have advantage on saving throws against illusions and against being charmed or paralyzed.",
                   "Duergar Magic. When you reach 3rd level, you can cast the Enlarge/Reduce spell on yourself once with this trait, using only the spell's enlarge option. When you reach 5th level, you can cast the Invisibility spell on yourself once with this trait. You don't need material components for either spell, and you can't cast them while you're in direct sunlight, although sunlight has no effect on them once cast. You regain the ability to cast these spells with this trait when you finish a long rest. Intelligence is your spellcasting ability for these spells.",
                   "Sunlight Sensitivity. You have disadvantage on Attack rolls and Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight."]
    ability_improve.append(' Str +1')
    darkvision += 60
    features.append(sub_featurs)


def Markofwarding_edit():
    sub_featurs = [
        "Warder's Intuition. Whenever you make an Intelligence (Investigation) check or an Ability Check involving Thieve's Tools, you can roll a d4 and add the number rolled to the total ability check.",
        "Wards and Seals. You can cast the Alarm and Mage Armor spells with this trait. Starting at 3rd level, you can also cast the Arcane Lock spell with it. Once you cast either spell with this trait, you can't cast that spell again until you finish a Long Rest. Intelligence is your Spellcasting Ability for these spells, and you don't require material components when you cast them with this trait.",
        "Spells of the Mark. If you have the Spellcasting or Pact Magic class feature, the spells on the Mark of Warding Spells table are added to the spell list of your Spellcasting class."]
    ability_improve.append(' Int +1')
    features.append(sub_featurs)


def give_info(subrace):
    if subrace == 'hill dwarf':
        hilldwarf_edit()

    elif subrace == 'mountain dwarf':
        mountaindwarf_edit()

    elif subrace == 'Duergar':
        Duergar_edit()

    elif subrace == 'Mark of Warding':
        Markofwarding_edit()

    complied_data = {'race': 'Dwarf',
                     'subrace': subrace,
                     'ability score': ability_improve,
                     'speed': speed,
                     'darkvision': darkvision,
                     'features': features,
                     'language': languages}

    return complied_data
