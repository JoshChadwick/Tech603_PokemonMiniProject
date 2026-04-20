class PokemonObject:
    def __init__(self, name, ability, height, weight, attack, defense, speed, hp):
        self.name = name
        self.ability = ability
        self.height = height
        self.weight = weight
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.hp = hp

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)

    def calculate_damage(self, opponent_defense):
        return max(1, self.attack - (opponent_defense // 2))
    

#Testing

if __name__ == "__main__":
    pikachu = PokemonObject("pikachu", 55, 40, ["thunder-shock", "quick-attack"])

    print(pikachu.name)
    print(pikachu.hp)
    print(pikachu.speed)
    print(pikachu.calculate_damage(20))

    pikachu.take_damage(30)
    print(pikachu.hp)
    print(pikachu.is_alive())
