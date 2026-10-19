class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

rec = Rectangle(10, 20)

print(f"eni : {rec.width} ,uzunlugu : {rec.height}")
print(f"Sahesi : {rec.calculate_area()}")
print(f"Perimetri : {rec.calculate_perimeter()}")