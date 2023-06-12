class FoodItem:
    def __init__(self, food_id, name, quantity, price, discount, stock):
        self.food_id = food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

    def __str__(self):
        return f"FoodID: {self.food_id}, Name: {self.name}, Quantity: {self.quantity}, Price: {self.price}, " \
               f"Discount: {self.discount}, Stock: {self.stock}"
class Menu:
    def __init__(self):
        self.food_items = []

    def add_food_item(self, name, quantity, price, discount, stock):
        food_id = len(self.food_items) + 1  # Generate FoodID automatically
        food_item = FoodItem(food_id, name, quantity, price, discount, stock)
        self.food_items.append(food_item)
        return food_item

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                return True
        return False

    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                return True
        return False

    def view_all_food_items(self):
        for food_item in self.food_items:
            print(food_item)
menu = Menu()

food_item1 = menu.add_food_item("Pizza", "Large", 15.99, 0.2, 10)
food_item2 = menu.add_food_item("Burger", "Single", 7.99, 0.1, 20)
food_item3 = menu.add_food_item("Salad", "Regular", 6.99, 0, 15)

menu.edit_food_item(food_item2.food_id, "Cheeseburger", "Single", 8.99, 0.15, 15)

menu.view_all_food_items()
menu.remove_food_item(food_item3.food_id)



class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password


class Application:
    def __init__(self):
        self.menu = Menu()
        self.users = []
        self.current_user = None
        self.order_history = []

    def register(self, full_name, phone_number, email, address, password):
        user = User(full_name, phone_number, email, address, password)
        self.users.append(user)
        return user

    def login(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                self.current_user = user
                return True
        return False

    def place_new_order(self):
        if not self.current_user:
            print("Please log in to place an order.")
            return

        print("Select the food items you want to order by entering the item numbers:")
        self.menu.view_all_food_items()

        selected_items = input("Enter the item numbers (separated by commas): ")
        selected_items = [int(item) for item in selected_items.split(',')]

        order_items = []
        total_price = 0

        for item_number in selected_items:
            if 0 < item_number <= len(self.menu.food_items):
                food_item = self.menu.food_items[item_number - 1]
                order_items.append(food_item)
                total_price += food_item.price

        if order_items:
            print("Selected Items:")
            for item in order_items:
                print(f"{item.name} ({item.quantity}) [INR {item.price}]")

            place_order = input("Do you want to place the order? (yes/no): ")
            if place_order.lower() == "yes":
                order = {
                    "user": self.current_user,
                    "items": order_items,
                    "total_price": total_price
                }
                self.order_history.append(order)
                print("Order placed successfully!")
            else:
                print("Order cancelled.")
        else:
            print("No valid food items selected.")

    def view_order_history(self):
        if not self.current_user:
            print("Please log in to view the order history.")
            return

        if self.order_history:
            print("Order History:")
            for order in self.order_history:
                user = order["user"]
                items = order["items"]
                total_price = order["total_price"]

                print(f"User: {user.full_name}")
                print("Items:")
                for item in items:
                    print(f"- {item.name} ({item.quantity}) [INR {item.price}]")
                print(f"Total Price: INR {total_price}")
                print("------------")
        else:
            print("No order history found.")

    def update_profile(self, full_name, phone_number, email, address, password):
        if not self.current_user:
            print("Please log in to update your profile.")
            return

        self.current_user.full_name = full_name
        self.current_user.phone_number = phone_number
        self.current_user.email = email
        self.current_user.address = address
        self.current_user.password = password
        print("Profile updated successfully!")
app = Application()
user1 = app.register("John Doe", "1234567890", "john@example.com", "123 Main St
