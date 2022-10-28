Race = 'Elf'
Subraces = ['high elf', 'wood elf', 'Drow', 'eladrin']
ability_improve = ['Dex +2']
speed = 30
darkvision = 60

languages = ['common', 'elvish']
features = ["Fey Ancestry: You have advantage on saving throws against being charmed, and magic can't put you to sleep.",
            "Trance: Elves do not sleep. Instead they meditate deeply, remaining semi-conscious, for 4 hours a day. The Common word for this meditation is 'trance.' While meditating, you dream after a fashion; such dreams are actually mental exercises that have become reflexive after years of practice. After resting in this way, you gain the same benefit a human would from 8 hours of sleep.",
            "Keen Senses: You have proficiency in the Perception skill."]


def highelf_edit():
    sub_featurs = ["Extra Cantrip: You know one cantrip of your choice from the Wizard spell list. Intelligence is your spellcasting ability for it",
                   "Elf Weapon Training: You have proficiency with the longsword, shortsword, shortbow, and longbow."]
    ability_improve.append(' int +1')
    languages.append(['choice'])
    features.append(sub_featurs)


def woodelf_edit():
    global speed
    sub_featurs = ["Mask of the Wild: You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.",
                   "Elf Weapon Training: You have proficiency with the longsword, shortsword, shortbow, and longbow."]
    ability_improve.append(' wis +1')
    features.append(sub_featurs)
    speed += 5


def drowelf_edit():
    global darkvision
    sub_featurs = ["Drow Magic. You know the Dancing Lights cantrip. When you reach 3rd level, you can cast the Faerie Fire spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the Darkness spell onceand regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells.",
                   "Drow Weapon Training. You have proficiency with rapiers, shortswords, and hand crossbows",
                   "Sunlight Sensitivity. You have disadvantage on attack rolls and Wisdom (Perception) checks that rely on sight when you, the target of the attack, or whatever you are trying to perceive is in direct sunlight."]
    ability_improve.append(' chr +1')
    darkvision += 60
    features.append(sub_featurs)


def eladrin_edit():
    sub_featurs = [
        "Fey Step. As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. Once you use this trait, you cant do so again until you finish a short or long rest."]
    ability_improve.append(' chr +1')
    features.append(sub_featurs)


def give_info(subrace):
    if subrace == 'high elf':
        highelf_edit()
    
    elif subrace == 'wood elf':
        woodelf_edit()
    
    elif subrace == 'Drow':
        drowelf_edit()
    
    elif subrace == 'eladrin':
        eladrin_edit()
    
    complied_data={'race':'Elf',
                    'subrace':subrace,
                    'ability score':ability_improve,
                    'speed':speed,
                    'darkvision':darkvision,
                    'features':features,
                    'language':languages}
    
    return complied_data

