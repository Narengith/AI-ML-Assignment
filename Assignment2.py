# Assignment 2:-

# # Area of a circle
class Circle:

    def __init__(self,radius):
        self.radius=radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius
    
radius=Circle(2)
AreaOfCircle=radius.calculate_area()
print("Area Of Cirlce:",AreaOfCircle)

# # Calculate discount
class Item:

    def __init__(self,original_price):
        self.original_price=original_price

    def calculate_discount(self,discount_percentage):
        discount_amount = self.original_price * (discount_percentage / 100)
        final_price = self.original_price - discount_amount
        return final_price

item=Item(100) # Original price is $100
discounted_price=item.calculate_discount(20) # Applying a 20% discount
print("Discounted Price:",discounted_price)

# Count vowels in a string
class count:

    def count_vowels(self,string):
        vowels="aeiouAEIOU"
        count=0
        for char in string:
            if char in vowels:
                count += 1
        return count

str=count()
vowel_count=str.count_vowels("Hello, World")
print("Number of vowels:",vowel_count)





