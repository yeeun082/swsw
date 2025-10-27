class Dog:
    count=0

    def __init__(self,name):
        self.name=name
        Dog.count +=1

    def bark(self):
        print(f"{self.name}왈")

    @classmethod
    def show_count(cls):
        print(f"현재 강아지 수: {cls.count}")
    @staticmethod
    def sound():
        print("개는 멍멍")

dog1 = Dog("김채은")
dog2 = Dog("깽이")

dog1.bark()
dog2.bark()
 
Dog.show_count()
Dog.sound()