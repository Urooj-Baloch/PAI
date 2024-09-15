class Vehicle:
    def __init__(self, name, cap):
        self.name = name
        self.cap = cap
    def fare(self):
        return self.cap * 100
class Bus(Vehicle):
    def __init__(self, name, cap):
        super().__init__(name, cap)
    def maintenance_charge(self):
        return self.fare() * 0.10
    def total_fare(self):
        return self.fare() + self.maintenance_charge()
bus = Bus("FAST NUCES TRANSPORT", 50)
print("Name:", bus.name)
print("Capacity:",bus.cap)
print("Base Fare:",bus.fare())
print("Maintenance Charge:",bus.maintenance_charge())
print("Total Fare:", bus.total_fare())
