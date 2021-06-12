class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        #self.number_served = int(self.number_served)
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


first_restaurant = Restaurant('Sapore','Italian')
first_restaurant.show_number_served()
first_restaurant.set_number_served(65)
first_restaurant.show_number_served()
first_restaurant.increment_number_served(6)
first_restaurant.show_number_served()
#first_restaurant.number_served()
#first_restaurant.describe_restaurant()
#first_restaurant.open_restaurant()
second_restaurant = Restaurant('Y Ashota','Armenian')
#second_restaurant.describe_restaurant()
third_restaurant = Restaurant('Dobrinya','Russian')
#third_restaurant.describe_restaurant()
