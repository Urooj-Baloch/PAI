class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.booked_tables = {}
        self.customer_orders = {}

    def add_item_to_menu(self, item_name, price):
        self.menu_items[item_name] = price

    def book_table(self, table_number, customer_name):
        if table_number in self.booked_tables:
            return f"Table ",table_number,"is already booked."
        self.booked_tables[table_number] = customer_name
        return "Table ",table_number," has been booked for",customer_name

    def customer_order(self, customer_name, order_items):
        if customer_name not in self.customer_orders:
            self.customer_orders[customer_name] = []
        self.customer_orders[customer_name].extend(order_items)

    def print_menu(self):
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: ${price:.2f}")

    def print_booked_tables(self):
        print("Booked Tables:")
        for table_number, customer_name in self.booked_tables.items():
            print(f"Table {table_number}: Reserved by {customer_name}")

    def print_customer_orders(self):
        print("Customer Orders:")
        for customer_name, orders in self.customer_orders.items():
            print(f"{customer_name} has ordered: {', '.join(orders)}")
restaurant = Restaurant()
restaurant.add_item_to_menu("Burger", 250.0)
restaurant.add_item_to_menu("Pizza", 1200.0)
restaurant.add_item_to_menu("Pasta", 700.0)
restaurant.print_menu()
print(restaurant.book_table(1, "Urooj Baloch"))
print(restaurant.book_table(2, "Mahnoor Hussain"))
restaurant.print_booked_tables()
restaurant.customer_order("Urooj Baloch", ["Burger", "Pizza"])
restaurant.customer_order("Mahnoor Hussain", ["Pasta"])
restaurant.print_customer_orders()
