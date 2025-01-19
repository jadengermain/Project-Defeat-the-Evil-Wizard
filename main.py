# main.py

import random
from characters.warrior import Warrior
from characters.mage import Mage
from characters.archer import Archer
from characters.paladin import Paladin
from utils.battle_system import BattleSystem

def main():
    print("Welcome to Hero vs Evil Wizard!")
    player_class = choose_character_class()
    player = create_character(player_class)
    wizard_health = 100
    battle_system = BattleSystem()

    while player.health > 0 and wizard_health > 0:
        action = choose_action()
        if action == '1':
            damage = player.attack()
            wizard_health -= damage
            print(f"You dealt {damage} damage to the Evil Wizard!")
        elif action == '2':
            player.heal()
            print("You healed yourself!")
        elif action == '3':
            use_special_ability(player)
        elif action == '4':
            display_stats(player, wizard_health)

        if wizard_health > 0:
            wizard_damage = battle_system.wizard_attack()
            player.health -= wizard_damage
            print(f"The Evil Wizard dealt {wizard_damage} damage to you!")

    if player.health <= 0:
        print("You have been defeated by the Evil Wizard!")
    else:
        print("Congratulations! You have defeated the Evil Wizard!")

def choose_character_class():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")
    choice = input("Enter the number of your choice: ")
    return choice

def create_character(choice):
    if choice == '1':
        return Warrior()
    elif choice == '2':
        return Mage()
    elif choice == '3':
        return Archer()
    elif choice == '4':
        return Paladin()

def choose_action():
    print("Choose your action:")
    print("1. Attack")
    print("2. Heal")
    print("3. Use Special Ability")
    print("4. View Stats")
    return input("Enter the number of your choice: ")

def use_special_ability(player):
    if hasattr(player, 'special_ability'):
        player.special_ability()
    else:
        print("You have no special abilities!")

def display_stats(player, wizard_health):
    print(f"Your Health: {player.health}")
    print(f"Evil Wizard's Health: {wizard_health}")

if __name__ == "__main__":
    main()