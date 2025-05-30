import random, os

class Pokemon:
    def __init__(self, name):
        self.name = name
        self.health = random.randint(20, 30)  # Health remains an integer
        self.attack = random.uniform(1.5, 5)  # Attack is now a float
        self.defense = random.uniform(0.75, 1)  # Defense is now a float

    def check_stats(self):
        print(f"Name: {self.name}\nHP: {self.health}\nATK: {self.attack:.2f}\nDEF: {self.defense:.2f}")
    
    def is_alive(self):
        if self.health <= 0:
            return f"Pokemon {self.name} has fainted!"
        else:
            return f"{self.name} is still fighting with {self.health} HP remaining."

class Magic(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.special = random.uniform(1, 1.5)

    def attack_target(self, target):
        damage = self.attack * self.special - target.defense
        damage = max(damage, 0)  # Ensure damage is not negative
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage:.2f} damage!")
        if target.health < 0:
            target.health = 0

class Fighter(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.special = random.uniform(1, 1.5)

    def attack_target(self, target):
        damage = self.attack * self.special - target.defense
        damage = max(damage, 0)  # Ensure damage is not negative
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage:.2f} damage!")
        if target.health < 0:
            target.health = 0

name1 = input("Enter the name for the magic Pokemon: ")
name2 = input("Enter the name for the fighter Pokemon: ")

poke1 = Magic(name1)
poke2 = Fighter(name2)

os.system('cls' if os.name == 'nt' else 'clear')

print("Initial Stats:")
poke1.check_stats()
poke2.check_stats()

print("\nBoth Pokemon are ready for battle!\n")
input("Press Enter to start the battle...")
os.system('cls' if os.name == 'nt' else 'clear')

print("\nBattle Begins!\n")
poke1.attack_target(poke2)
poke2.attack_target(poke1)

print("\nStats after first round of attacks:")
poke1.check_stats()
poke2.check_stats()

input("Press Enter to continue to the next round...")
os.system('cls' if os.name == 'nt' else 'clear')

print("\nContinuing the battle...\n")
poke1.attack_target(poke2)
poke2.attack_target(poke1)

print("\nStats after second round of attacks:")
poke1.check_stats()
poke2.check_stats()

input("Press Enter to continue to the final round...")
os.system('cls' if os.name == 'nt' else 'clear')

print("\nFinal Round of Attacks:\n")
poke1.attack_target(poke2)
poke2.attack_target(poke1)

print("\nFinal Stats:")
poke1.check_stats()
poke2.check_stats()

input("Press Enter to see the battle results...")
os.system('cls' if os.name == 'nt' else 'clear')

print("\nBattle Results:")
if poke1.health > poke2.health:
    print(f"{poke1.name} wins!")
elif poke2.health > poke1.health:
    print(f"{poke2.name} wins!")
else:
    print("It's a tie!")