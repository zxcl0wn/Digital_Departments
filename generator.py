import random


class GameEvent:
    players  = ["Анна", "Мария", "Екатерина", "Алина", "София", "Александр", "Дмитрий", "Максим", "Артём", "Илья"]
    actions = ["Убийство", "Смерть", "Ассист", "Повышение уровня"]
    def __init__(self):
        self.player = random.choice(self.players)
        self.action = random.choice(self.actions)
        self.score = random.randrange(100, 5000, 100)
        self.level = random.randint(1, 100)
