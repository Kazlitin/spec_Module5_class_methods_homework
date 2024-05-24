class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors  # Изменение атрибута этажности
        print(f"Новое количество этажей: {self.numberOfFloors}")  # Вывод нового значения

house = House()
house.setNewNumberOfFloors(2)  # Устанавливаем 2 этажа для дома