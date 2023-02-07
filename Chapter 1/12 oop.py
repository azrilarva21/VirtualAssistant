class Car:
    def get_owner(self):
        print("Owner is ",self._Name)
    def set_owner(self,Name):
        self._Name=Name


def main():
    my_car=Car()
    my_car.set_owner("Fahri")
    my_car.get_owner()

    rmd_car=Car()
    rmd_car.set_owner("Ramadhan")
    rmd_car.get_owner()


if __name__ == '__main__':main()