# class CarDriver:
#
#     def __init__(self, skill_level):
#         self.skill_level = float(skill_level)
#
#     def get_skill(self):
#         return self.skill_level
#
#
# class Car:
#     def __init__(self, speed):
#         self.speed = float(speed)
#         self.driver = None
#
#     def get_driving_speed(self):
#         if self.driver:
#             return self.speed * self.driver.get_skill()
#         else:
#             return 1.0
#
#     def set_driver(self, driver):
#         self.driver = driver
#
#
# class RaceTrack:
#     car_lst = []
#     def __init__(self, length):
#         self.length = length
#
#     def add_car(self, car):
#         self.car_lst.append(car)
#
#     def race(self):
#         fast_lst = [car.get_driving_speed() for car in self.car_lst]
#         fastest = max(fast_lst)
#         return self.length / fastest
#
#
#
#
# some_driver = CarDriver(1)
# some_car = Car(50)
# some_car.set_driver(some_driver)
# my_race_track = RaceTrack(200)
# my_race_track.add_car(some_car)
# print(my_race_track.race())

# class Student:
#     def __init__(self, name, grades):
#         self.grades = grades
#         self.name = name
#
#     def get_grade_avg(self):
#         return sum(self.grades) / len(self.grades)


class Student:
    def _init_(self, name, grades):
        self.name = name
        self.avg = sum(grades) / len(grades)

    def get_grade_avg(self):
        return self.avg

    def get_name(self):
        return self.name


class ClassRoom:
    def _init_(self, students):
        self.classroom = []
        for stu in students:
            self.classroom.append((stu.get_name(), stu.get_grade_avg()))

    def _str_(self):
        return str(self.classroom)





yossi = Student("Yossi", [100, 90, 95])

class_room = ClassRoom(yossi)

print(class_room)