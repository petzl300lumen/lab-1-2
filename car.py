class Car:
    def __init__(self,Color,Type,Year):
        self.Color = Color
        self.Type = Type
        self.Year = Year
    def turn_on_car(self):
        print("Автомобиль заведен")
    def turn_off_car(self):
        print("Автомобиль заглушен")
        
    def car_set_year(self, year):
        self.Year = year
    def car_set_type(self, type):
        self.Type = type
    def car_set_color(self, color):
        self.Color = color
car1 = Car("xxxx", "xxxx", "2000")
car1.turn_on_car()
car1.turn_off_car()
car1.car_set_year("1995")
car1.car_set_type("bmw3")
car1.car_set_color("black")
