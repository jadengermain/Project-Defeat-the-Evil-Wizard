class Archer(BaseCharacter):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=15)
        self.abilities = {
            "Quick Shot": self.quick_shot,
            "Evade": self.evade
        }
        self.evade_active = False

    def quick_shot(self, target):
        damage = random.randint(self.attack_power, self.attack_power * 2)
        target.take_damage(damage)
        return damage

    def evade(self):
        self.evade_active = True

    def attack(self, target):
        if self.evade_active:
            self.evade_active = False
            print(f"{self.name} evaded the attack!")
            return 0
        else:
            return super().attack(target)

    def heal(self):
        heal_amount = random.randint(10, 20)
        self.health = min(self.max_health, self.health + heal_amount)
        return heal_amount