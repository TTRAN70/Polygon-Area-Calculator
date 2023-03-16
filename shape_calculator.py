class Rectangle:
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)

    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

    def set_width(self, num):
        self.width = num

    def set_height(self, num):
        self.height = num

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.height <= 50 and self.width <= 50:
            picture = ""
            for i in range(self.height):
                picture += "*"*self.width
                picture += "\n"
            return picture
        else:
            big = "Too big for picture."
            return big

    def get_amount_inside(self, shape):
        inside = self.get_area() // shape.get_area()
        return inside

class Square(Rectangle):
    def __init__(self, length):
        self.width = int(length)
        self.height = int(length)

    def __str__(self):
        return "Square(side=" + str(self.height) + ")"

    def set_side(self, length):
        self.width = int(length)
        self.height = int(length)

    def set_width(self, num):
        self.width = int(num)
        self.height = int(num)

    def set_height(self, num):
        self.width = int(num)
        self.height = int(num)




