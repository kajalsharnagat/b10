from appp.models import *

# exec(open(r'D:\Python-B10\Django_Projects\first_project\appp\db_shell.py').read())

# CRUD operations 

# emp = Employee(first_name = "emp3", last_name = "tgf", email = "emp3@gmail.com", mobile_num = 176544)
# emp.save()

# emp = Employee(first_name = "emp4", last_name = "des", email = "emp4@gmail.com", mobile_num = 544)
# emp = Employee(first_name = "emp5", last_name = "fgtf", email = "emp5@gmail.com", mobile_num = 54334)
# emp.save()

# emp4 = Employee.objects.get(id = 5)
# emp4.delete()

# Employee.objects.get(id = 6).delete()

# Employee.objects.filter().delete()  --- will delete all record - don't use 

# emp_obj = Employee.objects.get(id = 3)
# emp_obj.first_name = "mac"
# emp_obj.last_name = "ron"
# emp_obj.save()

# all_emps = Employee.objects.all()
# print(all_emps)

# for emp in all_emps:
#     print(emp)
#     print(emp.id)


# emp = Employee.objects.get(id = 2)
# print(emp)

# try:
#     emp = Employee.objects.get(id = 10)
#     print(emp)
# except Employee.DoesNotExist as msg:
#     print(msg)

# try:
#     emp = Employee.objects.get(first_name = "emp2")
#     print(emp)
# except Employee.DoesNotExist as msg:
#     print(msg)    

# try:
#     emp = Employee.objects.get(mobile_num = 3455)
#     print(emp)
# except Employee.DoesNotExist as msg:
#     print(msg)    

# emps = Employee.objects.filter(first_name__startswith = "e")
# print(emps)  

# emps = Employee.objects.filter(last_name__startswith = "p")
# print(emps)

# emps = Employee.objects.filter(first_name__in = ["emp1", "emp2"])
# print(emps)

# emps = Employee.objects.filter(first_name__in = ["emp1", "emp3"])
# print(emps)

# emps = Employee.objects.filter(first_name__contains = "1")
# print(emps)

# emps = Employee.objects.filter(first_name__contains = "e").first()
# print(emps)

# emps = Employee.objects.filter(first_name__contains = "e")[1]
# print(emps)

# from django.db.models import Sum, Avg

# total_count = Employee.objects.count()
# print(total_count)
# total_sum = Employee.objects.aggregate(total=Sum('salary'))
# print(total_sum)
# average_value = Employee.objects.aggregate(average=Avg('salary'))
# print(average_value)

# data = Employee.objects.order_by('salary')
# print(data)

# data = Employee.objects.order_by('-salary')
# print(data)

# filtered_and_ordered = Employee.objects.filter(mobile_num__startswith = 1).order_by('id')
# print(filtered_and_ordered)

from datetime import datetime

# p1 = Person.objects.create(first_name="p1", last_name="pln1")
# p2 = Person.objects.create(first_name="p2", last_name="pln2")
# p3 = Person.objects.create(first_name="p3", last_name="pln3")
# p4 = Person.objects.create(first_name="p4", last_name="pln4")

# print(p3.__dict__)

# Profile.objects.create(bio="student1", birthdate=datetime(1990, 1, 15), user=p1)
# Profile.objects.create(bio="student2", birthdate=datetime(1992, 2, 25), user=p2)
# Profile.objects.create(bio="student3", birthdate=datetime(1994, 4, 5), user_id=10)
# Profile.objects.create(bio="student3", birthdate=datetime(1990, 1, 15), person=p3)

# p4 = Person.objects.get(id = 11 )
# Profile.objects.create(bio = "Student4", birthdate = datetime(1996, 4, 2), user = p4)

# p1 = Person.objects.get(id=7)
# p1.delete()

# Address.objects.create(street="DP road", city="Pune", state="MH",postal_code=412451, person=p1)
# Address.objects.create(street="wakad road", city="Pune", state="MH",postal_code=411057, person_id=p1.id)

# p1 = Person.objects.get(id = 8)
# Address.objects.create(street="DP road", city="Pune", state="MH",postal_code=412451, person=p1)
# Address.objects.create(street="wakad road", city="Pune", state="MH",postal_code=411057, person_id=p1.id)

# p2 = Person.objects.create(first_name = "pawan", last_name = "chandel")
# Address.objects.filter(id__in = [1,2]).update(person = p2)

# p1 = Person.objects.get(id=12)
# # print(dir(p1))
# print(p1.address_set.all())

# adr1 = Address.objects.get(id=1)
# print(adr1.person)


# pr1 = Profile.objects.get(id=1)
# print(pr1.person)


# p1 = Person.objects.get(id=4)
# print(dir(p1))
# print(p1.address_set.all())



# many to many

# c180 = CarModel.objects.create(name="C180")
# c200 = CarModel.objects.create(name="C200")

# print(CarModel.objects.all())


# gas = FuelType.objects.create(name="Gas")
# diesel = FuelType.objects.create(name="Diesel")
# hybrid = FuelType.objects.create(name="Hybrid")

# print(FuelType.objects.all())

# exec(open(r'D:\Python-B10\Django_Projects\first_project\appp\db_shell.py').read())


c180 = CarModel.objects.get(name="C180") #  1
gas = FuelType.objects.get(name = "Gas")
# c180.fueltype.add(gas)
# print(c180.fueltype.all())
# d = FuelType.objects.get(name = "Diesel")
# c180.fueltype.add(d)
# print(c180.fueltype.all())

# c200 = CarModel.objects.get(name = "C200")

# f1 = FuelType.objects.get(name="Gas") # 2
# f2 = FuelType.objects.get(name="Diesel") # 2
# f3 = FuelType.objects.get(name="Hybrid") # 2


# c200.fueltype.add(f1, f2, f3) # CarModelObject.fueltype.add(FuelTypeObject)
# print(c200.fueltype.all())

# c200.fueltype.create(name="Bio Diesel")

# print(f1.models.all())
# print(gas.models.all())
# print(FuelType.objects.get(name="Gas").models.all())
# print(FuelType.objects.get(name = "Bio Diesel").models.all())

# print(CarModel.objects.filter(fueltype__name__startswith="G"))
# print(CarModel.objects.filter(fueltype__name__startswith="B"))
# print(CarModel.objects.filter(fueltype__name__startswith = "H"))

# c1 = FuelType.objects.filter(models__name__startswith="C")
# print(c1)
# c1 = FuelType.objects.filter(models__name__startswith="D")


# print(c180.fueltype.all())
# c180.fueltype.remove(gas)
# c180.fueltype.all()

# cars = CarModel.objects.filter(fueltype__name__startswith="B")
# cars.delete()

# c180.fueltype.clear()

# f4 = FuelType.objects.get(name="lithium battery")              ##for testing 
# f5 = FuelType.objects.get(name="water")   