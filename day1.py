class Dog:
    def __init__(self,name):
        self.name=name

    def bark(self):
        print(f"{self.name}왈")

dog1 = Dog("김채은")
dog2 = Dog("깽이")

dog1.bark()
dog2.bark()
