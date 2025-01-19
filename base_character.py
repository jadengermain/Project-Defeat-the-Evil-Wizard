class BaseCharacter:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power

    def attack(self):
        import random
        damage = random.randint(1, self.attack_power)
        return damage

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)

    def is_alive(self):
        return self.health > 0

    def special_ability_1(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def special_ability_2(self):
        raise NotImplementedError("This method should be overridden by subclasses.")