class Vehicle:
    def get_vehicle_features(self):
        print("Initializing vehicle features")


class Car(Vehicle):
    def get_car_features(self):
        print("Initializing car features")


car1 = Car()
car1.get_vehicle_features()
car1.get_car_features()
