import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        damage = max(1, damage)
        opponent.health -= damage
        opponent.health = max(0, opponent.health)
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")

        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def heal(self):
        heal_amount = 25
        before = self.health
        self.health = min(self.max_health, self.health + heal_amount)
        print(f"{self.name} heals for {self.health - before} health "
              f"({self.health}/{self.max_health})")

    def display_stats(self):
        print(f"{self.name} — Health: {self.health}/{self.max_health}, "
              f"Attack Power: {self.attack_power}")


# Warrior class
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def power_strike(self, opponent):
        bonus = random.randint(10, 20)
        damage = self.attack_power + bonus
        opponent.health -= damage
        opponent.health = max(0, opponent.health)
        print(f"{self.name} uses Power Strike for {damage} damage!")

    def battle_cry(self):
        self.attack_power += 5
        print(f"{self.name} uses Battle Cry! Attack increased to {self.attack_power}.")


# Mage class
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.arcane_shield = False

    def fireball(self, opponent):
        bonus = random.randint(12, 25)
        damage = self.attack_power + bonus
        opponent.health -= damage
        opponent.health = max(0, opponent.health)
        print(f"{self.name} casts Fireball for {damage} damage!")

    def arcane_shield_spell(self):
        self.arcane_shield = True
        print(f"{self.name} casts Arcane Shield! Next hit will be reduced.")


# Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=28)
        self.evade_next = False

    def quick_shot(self, opponent):
        print(f"{self.name} uses Quick Shot!")
        self.attack(opponent)
        if opponent.health > 0:
            self.attack(opponent)

    def evade(self):
        self.evade_next = True
        print(f"{self.name} prepares to Evade the next attack!")


# Paladin class
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=20)
        self.shield_next = False

    def holy_strike(self, opponent):
        bonus = random.randint(8, 15)
        damage = self.attack_power + bonus
        opponent.health -= damage
        opponent.health = max(0, opponent.health)
        print(f"{self.name} uses Holy Strike for {damage} damage!")

    def divine_shield(self):
        self.shield_next = True
        print(f"{self.name} raises a Divine Shield!")


# Evil Wizard class
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health = min(self.max_health, self.health + 5)
        print(f"{self.name} regenerates 5 health "
              f"({self.health}/{self.max_health})")


def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    choice = input("Enter choice: ")
    name = input("Enter your character's name: ")

    if choice == '1':
        return Warrior(name)
    elif choice == '2':
        return Mage(name)
    elif choice == '3':
        return Archer(name)
    elif choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)


def battle(player, wizard):
    while player.health > 0 and wizard.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)

        elif choice == '2':
            if isinstance(player, Warrior):
                print("1. Power Strike")
                print("2. Battle Cry")
                ability = input("Choose ability: ")
                if ability == '1':
                    player.power_strike(wizard)
                elif ability == '2':
                    player.battle_cry()

            elif isinstance(player, Mage):
                print("1. Fireball")
                print("2. Arcane Shield")
                ability = input("Choose ability: ")
                if ability == '1':
                    player.fireball(wizard)
                elif ability == '2':
                    player.arcane_shield_spell()

            elif isinstance(player, Archer):
                print("1. Quick Shot")
                print("2. Evade")
                ability = input("Choose ability: ")
                if ability == '1':
                    player.quick_shot(wizard)
                elif ability == '2':
                    player.evade()

            elif isinstance(player, Paladin):
                print("1. Holy Strike")
                print("2. Divine Shield")
                ability = input("Choose ability: ")
                if ability == '1':
                    player.holy_strike(wizard)
                elif ability == '2':
                    player.divine_shield()

        elif choice == '3':
            player.heal()

        elif choice == '4':
            player.display_stats()
            wizard.display_stats()

        else:
            print("Invalid choice.")

        if wizard.health > 0:
            print("\n--- Wizard's Turn ---")
            wizard.regenerate()

            if hasattr(player, 'evade_next') and player.evade_next:
                print(f"{player.name} dodges the attack!")
                player.evade_next = False

            elif hasattr(player, 'shield_next') and player.shield_next:
                print(f"{player.name}'s shield blocks the attack!")
                player.shield_next = False

            elif hasattr(player, 'arcane_shield') and player.arcane_shield:
                damage = random.randint(5, 10)
                player.health -= damage
                player.health = max(0, player.health)
                print(f"Arcane Shield reduces damage to {damage}!")
                player.arcane_shield = False

            else:
                wizard.attack(player)

        if player.health <= 0:
            print("\nYou have been defeated!")
            return

    print("\nVictory! You defeated the Evil Wizard!")


def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)


if __name__ == "__main__":
    main()
