class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type


    def describe_restaurant(self):
        print(f"Welcome to {self.name}")
        print(f"It's Restaurant {self.type} cuisine!")
    def open_restaurant(self):
        print(f"Restaurant {self.name} is open.Come in!")

first_restaurant = Restaurant('Sapore','Italian')
first_restaurant.describe_restaurant()
first_restaurant.open_restaurant()
second_restaurant = Restaurant('Y Ashota','Armenian')
second_restaurant.describe_restaurant()
third_restaurant = Restaurant('Dobrinya','Russian')
third_restaurant.describe_restaurant()
