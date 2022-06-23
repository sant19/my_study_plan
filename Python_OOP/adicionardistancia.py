# Exemplo
class Distance:
    # initialize feet and inches attributes
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def add_distances(self, distance):
        result_inches = self.inches + distance.inches
        result_feet = self.feet + distance.feet

        # while inch is 12 or greater,
        # increase feet by 1 and decrease inches by 12
        while (result_inches >= 12):
            result_feet = result_feet + 1
            result_inches = result_inches - 12

        # create an object of Distance
        result_distance = Distance(result_feet, result_inches)
        return result_distance


# create distance1 object
distance1 = Distance(12, 8)
# create distance2 object
distance2 = Distance(10, 6)
# call add_distances using distance1 object
# distance2 is used as argument
result = distance1.add_distances(distance2)
print(f'Result distance: {result.feet} ft {result.inches} inches')
