class parent():
    def __init__(self):
        print("parent class")

    def menu(dish):
        if dish == "burger":
            print("You can add following toppins")
            print("More Cheese | add Jalapenos")
        elif dish == "iced_americano":
            print("You can add following toppins")
            print("Add chocolate flavour | add caramel flavour")
        else:
            print("Please enter valid dish")

    def final_amount(dish, addons):
        if dish == "burger" and addons == "cheese":
            print("Your total amount is 250 USD")
        elif(dish == "burger" and addons == "jalepeeno"):
            print("You need to pay 350 USD")
        elif dish == "iced_americano" and addons == "chocolate":
            print("You need to pay 250 USD")
        elif dish == "iced_americano" and addons == "caramel":
            print("You need to pay 450 USD")

class child1(parent) :
    def __init__(self, dish):
        self.new_dish = dish
    def get_menu(self):
        parent.menu(self.new_dish)

class child2(parent):
    def __init__(self, dish, addons):
        self.new_dish = dish
        self.addons = addons
    def get_final_amount(self):
        parent.final_amount(self.new_dish, self.addons)

child1_object = child1("iced_americano")
child1_object.get_menu()

child2_object = child2("iced_americano", "chocolate")
child2_object.get_final_amount()