class Paladin(BaseCharacter):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=15)
        self.special_abilities = {
            "Holy Strike": self.holy_strike,
            "Divine Shield": self.divine_shield
        }
        self.shield_active = False

    def holy_strike(self, target):
        damage = self.attack_power + 10  # Bonus damage
        target.take_damage(damage)
        return f"{self.name} uses Holy Strike on {target.name} for {damage} damage!"

    def divine_shield(self):
        self.shield_active = True
        return f"{self.name} activates Divine Shield and will block the next attack!"

    def take_damage(self, damage):
        if self.shield_active:
            self.shield_active = False
            return f"{self.name} blocks the attack with Divine Shield!"
        else:
            super().take_damage(damage)
            return f"{self.name} takes {damage} damage! Current health: {self.health}"

    def heal(self):
        heal_amount = 20
        self.health = min(self.max_health, self.health + heal_amount)
        return f"{self.name} heals for {heal_amount} health! Current health: {self.health}"