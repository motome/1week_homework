class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age
    
    def name_age(self):
        return f"{self.first_name} . age # {self.family_name}"

ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.name_age())  # "Ken's name and age"

tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.name_age())  # "Tom's name and age"

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.name_age())  # "Ieyasu's name and age"

#以上が課題C-2
#full_nameはここでは必要ないので削除しています
