class Warrior(BaseCharacter):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=15)
        self.abilities = {
            "Shield Bash": self.shield_bash,
            "Battle Cry": self.battle_cry
        }

    def shield_bash(self, target):
        damage = self.attack_power + 5  # Extra damage for shield bash
        target.take_damage(damage)
        return f"{self.name} uses Shield Bash on {target.name} for {damage} damage!"

    def battle_cry(self):
        self.attack_power += 5  # Increase attack power temporarily
        return f"{self.name} shouts a battle cry, increasing attack power!"

    def attack(self, target):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        target.take_damage(damage)
        return f"{self.name} attacks {target.name} for {damage} damage!"