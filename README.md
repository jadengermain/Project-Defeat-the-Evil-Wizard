# Hero vs Evil Wizard

## Overview
In this mini-project, you will embark on an adventure to create a hero character and battle the powerful Evil Wizard. Utilizing Object-Oriented Programming (OOP) principles, you will extend the starter code, customize your character, and add new functionalities. 

## Project Structure
The project is organized as follows:

```
hero-vs-evil-wizard
├── src
│   ├── main.py                # Entry point of the game
│   ├── characters             # Contains character classes
│   │   ├── base_character.py  # Abstract base class for characters
│   │   ├── warrior.py         # Warrior character class
│   │   ├── mage.py            # Mage character class
│   │   ├── archer.py          # Archer character class
│   │   └── paladin.py         # Paladin character class
│   └── utils                  # Utility functions
│       └── battle_system.py   # Battle system logic
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Gameplay Mechanics
- **Character Classes**: Choose from four character classes: Warrior, Mage, Archer, and Paladin. Each class has unique abilities and attack styles.
- **Turn-Based Battle System**: Engage in a turn-based battle against the Evil Wizard. Players can choose to attack, heal, use special abilities, or view stats.
- **Special Abilities**: Each character class has two unique abilities that can turn the tide of battle.
- **Healing Mechanic**: Players can heal themselves during battle, restoring health without exceeding the maximum limit.
- **Victory/Defeat Conditions**: The game concludes with a victory message if the player defeats the Evil Wizard or a defeat message if the wizard wins.

## Setup Instructions
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```
4. Run the game by executing:
   ```
   python src/main.py
   ```

## Contribution
Feel free to contribute to the project by adding new features, character classes, or improving the gameplay mechanics. 

## License
This project is open-source and available for modification and distribution.