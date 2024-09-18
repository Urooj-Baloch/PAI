
class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity
    def calculate_fare(self):
        return self.seating_capacity * 100
class Bus(Vehicle):
    def calculate_fare(self):
        base_fare = super().calculate_fare()
        maintenance_charge = 0.10 * base_fare
        return base_fare + maintenance_charge
if __name__ == "__main__":
    bus = Bus(seating_capacity=60)
    print("The total fare for the bus is:",bus.calculate_fare())
