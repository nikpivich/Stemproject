import random

class Dragon:
    def __init__(self, name, color, wingspan, breath_type):
        self.name = name
        self.color = color
        self.wingspan = wingspan
        self.breath_type = breath_type

    def display_info(self):
        print(f"Dragon {self.name}:")
        print(f"Color: {self.color}")
        print(f"Wingspan: {self.wingspan} meters")
        print(f"Breath Type: {self.breath_type}")
        print()

class DragonGenetics:
    COLORS = ["Red", "Blue", "Green", "Black", "White"]
    BREATH_TYPES = ["Fire", "Ice", "Acid", "Electric"]

    def create_random_dragon(self, name):
        color = random.choice(self.COLORS)
        wingspan = random.uniform(5.0, 25.0)  # Random wingspan between 5.0 and 25.0 meters
        breath_type = random.choice(self.BREATH_TYPES)

        return Dragon(name, color, wingspan, breath_type)

# Пример использования
genetics_engine = DragonGenetics()

# Создаем драконов с случайными характеристиками
dragon1 = genetics_engine.create_random_dragon("Drako")
dragon2 = genetics_engine.create_random_dragon("Flare")

# Выводим информацию о драконах
dragon1.display_info()
dragon2.display_info()
