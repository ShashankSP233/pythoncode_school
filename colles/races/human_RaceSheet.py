Race = 'Human'
Subraces = ['Standard', 'Variant']
ability_improve = []
speed = 30
darkvision = 0

languages = ['common', 'any']
features = ["Fey Ancestry: You have advantage on saving throws against being charmed, and magic can't put you to sleep.",
            "Trance: Elves do not sleep. Instead they meditate deeply, remaining semi-conscious, for 4 hours a day. The Common word for this meditation is 'trance.' While meditating, you dream after a fashion; such dreams are actually mental exercises that have become reflexive after years of practice. After resting in this way, you gain the same benefit a human would from 8 hours of sleep.",
            "Keen Senses: You have proficiency in the Perception skill."]


def standard_edit():
    sub_featurs = ["all ability score +1"]
    ability_improve.append('dex +1',' str +1',' con +1',' wis +1',' int +1','chr +1')
    features.append(sub_featurs)


def Variant_edit():
    sub_featurs = ["Skills. You gain proficiency in one skill of your choice.",
                   "Feat. You gain one Feat of your choice."]
    ability_improve.append(' any +1', ' any +1')
    features.append(sub_featurs) 
