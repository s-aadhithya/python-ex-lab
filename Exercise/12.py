class Vehicle:
    def __init__(self, make, model, year, fuel_type):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type

    def display_info(self):
        pass 


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type, num_doors, num_passengers, car_type):
        super().__init__(make, model, year, fuel_type)
        self.num_doors = num_doors
        self.num_passengers = num_passengers
        self.car_type = car_type

    def display_info(self):
        return f"Car: {self.make} {self.model} ({self.year}), Fuel: {self.fuel_type}, Doors: {self.num_doors}, Passengers: {self.num_passengers}, Type: {self.car_type}"


class Truck(Vehicle):
    def __init__(self, make, model, year, fuel_type, payload_capacity, four_wheel_drive):
        super().__init__(make, model, year, fuel_type)
        self.payload_capacity = payload_capacity
        self.four_wheel_drive = four_wheel_drive

    def display_info(self):
        return f"Truck: {self.make} {self.model} ({self.year}), Fuel: {self.fuel_type}, Payload Capacity: {self.payload_capacity}, 4WD: {self.four_wheel_drive}"


class ElectricCar(Car):
    def __init__(self, make, model, year, num_doors, num_passengers, car_type, battery_capacity, charging_time):
        super().__init__(make, model, year, "Electric", num_doors, num_passengers, car_type)
        self.battery_capacity = battery_capacity
        self.charging_time = charging_time

    def display_info(self):
        return f"Electric Car: {self.make} {self.model} ({self.year}), Battery Capacity: {self.battery_capacity}, Charging Time: {self.charging_time}, {super().display_info()}"


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, fuel_type, num_wheels, has_sidecar, motorcycle_type):
        super().__init__(make, model, year, fuel_type)
        self.num_wheels = num_wheels
        self.has_sidecar = has_sidecar
        self.motorcycle_type = motorcycle_type

    def display_info(self):
        return f"Motorcycle: {self.make} {self.model} ({self.year}), Fuel: {self.fuel_type}, Wheels: {self.num_wheels}, Sidecar: {self.has_sidecar}, Type: {self.motorcycle_type}"


def display_vehicle_info(vehicles):
    for vehicle in vehicles:
        print(vehicle.display_info())


car1 = Car("Toyota", "Camry", 2022, "Gasoline", 4, 5, "Sedan")
truck1 = Truck("Ford", "F-150", 2022, "Gasoline", 1500, True)
electric_car1 = ElectricCar("Tesla", "Model S", 2022, 4, 5, "Sedan", 100, 8)
motorcycle1 = Motorcycle("Harley-Davidson", "Sportster", 2022, "Gasoline", 2, False, "Cruiser")

vehicles_list = [car1, truck1, electric_car1, motorcycle1]

display_vehicle_info(vehicles_list)
