# class Student:
#     def __init__(self,name,pohlavi):
#         self.name = name
#         self.pohlavi = pohlavi
#
#     def pozdrav(self):
#         print(f"ahoj jsem {self.name}")
#
# student = Student("Jan", "muž")
# student.pozdrav()
class Auto:
    def __init__(self, rychlost, váha):
        self.rychlost = rychlost
        self.váha = váha
    def check_limit_speed_obec(self):
        if self.rychlost <=50:
            print("Jedeš ok")
        else:
            print("nejedeš ok")

    def check_limit_speed_dalnice(self):
        if self.rychlost <80:
            print("Jedeš ok")
        else:
            print("nejedeš ok")
auto1=Auto(30,40)
auto1.check_limit_speed_dalnice()
auto1.check_limit_speed_obec()
class Kamion(Auto):
    def __init__(self, rychlost, váha, zatizeni):
        super().__init__(rychlost,váha)
        self.zatizeni=zatizeni
kamion1=Kamion(50,60,50)
kamion1.check_limit_speed_obec()
kamion1.check_limit_speed_dalnice()



