class Player:
    def __init__(self, health= 100, energy= 100):
        self.name = input("Enter your name: ")
        self.health = health
        self.energy = energy
        print(f"Name: {self.name}, Health: {health}, Energy: {energy}")

    def attack(self, damage= 10):
        if damage < self.energy:
            self.energy -= damage
            print(f"[ATTACK] Damage taken: {damage} | 🛡️ Energy reduced to {self.energy} | ❤️ Health remains at {self.health}")
        else:
            self.health -= damage - self.energy
            self.energy = 0
            print(f"Damage taken: {damage} | 🛡️ Energy left: {self.energy} | ❤️ Health left: {self.health}")
    pass

player = Player()
player.attack()
