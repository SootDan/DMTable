from random import randint, seed


def roll_dice(dice_eyes=20, dice_type="standard", dice_rolls=1, modifier=0):
    """Dice roll. Takes into account eyes, type, rolls, and modifier."""

    seed()
    output = []
    if dice_type == "advantage" or dice_type == "disadvantage":
        # Advantage and disadvantage rolls are always rolled twice.
        dice_rolls = 2

    for dice in range(dice_rolls):
        output.append(randint(1, dice_eyes) + modifier)

    if dice_type == "advantage":
        return max(output)
    if dice_type == "disadvantage":
        return min(output)
    return sum(output)


def hit_chance(armor_class=10, dice_eyes=20, dice_type="standard", dice_rolls=1, modifier=0):
    """Calculates hit chance in percent. Check source for formula in README."""

    if dice_type == "advantage" or dice_type == "disadvantage":
        dice_rolls = 2
    if dice_type == "disadvantage":
        chance = ((dice_rolls + 1 + modifier - armor_class)
                  ** dice_rolls) / dice_eyes ** dice_rolls
    elif dice_type == "advantage":
        chance = 1 - (armor_class - modifier - 1) ** dice_rolls / \
            dice_eyes ** dice_rolls
    else:
        chance = (((dice_eyes + 1) - (armor_class - modifier)) /
                  dice_eyes) * dice_rolls
    return int(chance * 100)


def hp_calc(level=1, char_class="barbarian", con_modifier=1,
            is_hill_dwarf=False, is_tough=False, is_draconic=False):
    """Only calculates average HP, no rolls."""

    ...
