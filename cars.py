cars = 100
space_in_car = 4
drivers = 30 
passengers = 90 

cars_driven = drivers 
cars_not_driven = cars - drivers 

carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers/cars_driven 

print "there are",cars,"cars in total"
print "there are only",passengers,"passengers in total"
print average_passengers_per_car

