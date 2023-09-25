class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age
      
    def entry_fee(self):
        if self.age < 20:
            return 1000
        elif self.age >= 65:
            return 1200
        else:
            return 1500

ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(f"ken.entry_fee()  # {ken.entry_fee()}")

tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(f"tom.entry_fee()  # {tom.entry_fee()}")

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(f"ieyasu.entry_fee()  # {ieyasu.entry_fee()}")

#これがc-3のコードです

