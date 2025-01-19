class Mage(BaseCharacter):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=15)
        self.mana = 50

    def cast_spell(self, target):
        if self.mana >= 10:
            damage = random.randint(10, 20)
            target.take_damage(damage)
            self.mana -= 10
            return f"{self.name} casts a spell on {target.name} for {damage} damage!"
        else:
            return f"{self.name} does not have enough mana to cast a spell!"

    def heal(self):
        heal_amount = random.randint(15, 25)
        self.health = min(self.max_health, self.health + heal_amount)
        return f"{self.name} heals for {heal_amount} health!"