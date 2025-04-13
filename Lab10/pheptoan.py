lunch = {'tra sua', 'com van phong', 'banh mi'}
dinner = {'banh trang tron', 'tra sua', 'khong'}

# Phép hợp
# union()
meals  = lunch.union(dinner)
# | (or)
meals = lunch | dinner
print(meals)
# Phép giao
# intersection()
meals = lunch.intersection(dinner)
# & (and)
meals = lunch & dinner
print(meals)
# Phép tru/ phep hieu
# difference()
meals =lunch.difference(dinner)
# - (not)
meals = lunch - dinner
print(meals)