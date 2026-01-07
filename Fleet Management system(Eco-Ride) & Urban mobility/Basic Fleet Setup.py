class Vehicle:

    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.__maintenance_status = "Good"  # private attribute
        self.__rental_price = 1500          # private attribute
        self.set_battery_percentage(battery_percentage)

    def get_maintenance_status(self):
        return self.__maintenance_status
    def set_maintenance_status(self,status):
        self.__maintenance_status = status

    def get_rental_price(self):
        return self.__rental_price
    def set_rental_price(self,price):
        if price > 0:
          self.__rental_price = price
        else:
            print("Rental price must be positive")

    def set_battery_percentage(self, battery_percentage):
        if 0 <= battery_percentage <= 100:
            self.battery_percentage = battery_percentage
        else:
            print("Battery percentage must be between 0 and 100")
    def get_battery_percentage(self):
        return self.battery_percentage

class ElectricCar(Vehicle):
    def __init__(self, vehicle_id,model,battery_percentage,seating_capacity):
        Vehicle.__init__(self, vehicle_id, model, battery_percentage)
        self.__seating_capacity = seating_capacity
class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id,model,battery_percentage,max_speed_limit):
        Vehicle.__init__(self, vehicle_id,model,battery_percentage)
        self.__max_speed_limit = max_speed_limit

v1 = Vehicle("V102","Mercedes-C89",72)
print("Vehicle_ID: ",v1.vehicle_id)
print("Model: ",v1.model)
print("Battery Level: ",v1.get_battery_percentage,"%")
print("Maintenance Status: ",v1.get_maintenance_status())
print("rental price: ",v1.get_rental_price())

v1.set_battery_percentage(120)
v1.set_battery_percentage(80)

v1.set_rental_price(-500)
v1.set_rental_price(1500)
