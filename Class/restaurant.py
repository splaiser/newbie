class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"Welcome to {self.name}")
        print(f"It's Restaurant {self.type} cuisine!")
    def open_restaurant(self):
        print(f"Restaurant {self.name} is open.Come in!")
    def show_number_served(self):
        print(f"We can served {self.number_served} seat per day")
    def set_number_served(self,seat):
        self.number_served = seat
    def increment_number_served(self,seat):
        self.number_served += seat

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['chery','banana','white']
    def show_flavor(self):
        print(f"list : {self.flavors}")

restaurant_0 = IceCreamStand('Sapore','Italian')
restaurant_0.show_flavor()