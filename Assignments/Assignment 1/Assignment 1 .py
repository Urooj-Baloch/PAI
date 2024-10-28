#Name:Urooj Baloch
#ID:23k-0071
class Animal:
    def __init__(self, name, age, habitat):
        self.name = name
        self.age = age
        self.habitat = habitat
        self.available_for_viewing = True  

    def mark_availability(self, available):
        self.available_for_viewing = available

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Habitat: {self.habitat}, Available: {self.available_for_viewing}"


class Mammal(Animal):
    def __init__(self, name, age, habitat, fur_length, diet_type, feeding_time):
        super().__init__(name, age, habitat)
        self.fur_length = fur_length
        self.diet_type = diet_type
        self.feeding_time = feeding_time

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Fur Length: {self.fur_length}, Diet Type: {self.diet_type}, Feeding Time: {self.feeding_time}"


class Bird(Animal):
    def __init__(self, name, age, habitat, wingspan, flight_altitude, feeding_time):
        super().__init__(name, age, habitat)
        self.wingspan = wingspan
        self.flight_altitude = flight_altitude
        self.feeding_time = feeding_time

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Wingspan: {self.wingspan}, Flight Altitude: {self.flight_altitude}, Feeding Time: {self.feeding_time}"


class Reptile(Animal):
    def __init__(self, name, age, habitat, scale_pattern, venomous, feeding_time):
        super().__init__(name, age, habitat)
        self.scale_pattern = scale_pattern
        self.venomous = venomous  
        self.feeding_time = feeding_time

    def display_info(self):
        base_info = super().display_info()
        venom_status = "Venomous" if self.venomous else "Non-venomous"
        return f"{base_info}, Scale Pattern: {self.scale_pattern}, Venomous: {venom_status}, Feeding Time: {self.feeding_time}"



if __name__ == "__main__":

    lion = Mammal(name="Lion", age=5, habitat="Savannah", fur_length="Short", diet_type="Carnivore", feeding_time="2 PM")
    parrot = Bird(name="Parrot", age=2, habitat="Rainforest", wingspan="25 inches", flight_altitude="High", feeding_time="10 AM")
    snake = Reptile(name="Snake", age=3, habitat="Desert", scale_pattern="Striped", venomous=True, feeding_time="1 PM")

    print(lion.display_info())
    print(parrot.display_info())
    print(snake.display_info())

    lion.mark_availability(False)  
    parrot.mark_availability(True)  
    snake.mark_availability(False)  

    print("\nUpdated Information:")
    print(lion.display_info())
    print(parrot.display_info())
    print(snake.display_info())
