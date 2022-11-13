import statistics

first_name = "Jhea Angel"
last_name = "Delgado"
full_name = first_name + " " + last_name

id_no = 212053

ArtAp10 = 98 #int1
Phys10 = 91 #int2
Polsc21 = 89 #int3
grades = ArtAp10, Phys10, Polsc21
average = statistics.mean(grades)

print(full_name)
print(id_no)
print(grades)
print("My average in three subjects is" +" " +str(round(average,2)))



