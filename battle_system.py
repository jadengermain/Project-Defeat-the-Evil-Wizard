class BattleSystem:
    def __init__(self, player, wizard):
        self.player = player
        self.wizard = wizard

    def player_attack(self):
        damage = self.player.attack()
        self.wizard.health -= damage
        print(f"{self.player.name} attacks the Evil Wizard for {damage} damage!")

    def wizard_attack(self):
        damage = self.wizard.attack()
        self.player.health -= damage
        print(f"The Evil Wizard attacks {self.player.name} for {damage} damage!")

    def player_heal(self):
        heal_amount = self.player.heal()
        self.player.health += heal_amount
        print(f"{self.player.name} heals for {heal_amount} health!")

    def check_victory(self):
        if self.wizard.health <= 0:
            print(f"{self.player.name} has defeated the Evil Wizard!")
            return True
        return False

    def check_defeat(self):
        if self.player.health <= 0:
            print(f"The Evil Wizard has defeated {self.player.name}!")
            return True
        return False

    def battle_turn(self):
        self.player_attack()
        if self.check_victory():
            return True
        self.wizard_attack()
        if self.check_defeat():
            return True
        return False

    def start_battle(self):
        while True:
            if self.battle_turn():
                break
            self.wizard.regenerate_health()  # Assuming the wizard has a method to regenerate health.