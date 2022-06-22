class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimensional shape with strainght lines")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter


class Quadrilateral(Polygon):
    def display_info(self):
        print("A quadrilateral is a polygon with 4 edges.")


q1 = Quadrilateral([2, 3, 4, 5])
q1.display_info()
