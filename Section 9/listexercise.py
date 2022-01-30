#Dictionary in list excercise
#Nesting Dictoionary in a list
travel_log = [{"country":"France","cities_visited":["Paris","Lille","Leon"],"total_visits":12},
 {"country":"Korea","cities_visited":["Seoul","Busan","Jejudo"],"total_visits":3}]

def add_new_country(country_visited,times_visited,cities_visited):
  new_countries = {}
  new_countries["country"] = country_visited
  new_countries["visited"] = times_visited 
  new_countries["cities"] = cities_visited
  #print("here is",new_countries,"\n")
  travel_log.append(new_countries)

add_new_country("Russia",2,["Moscow","Saint Petersburg"])
print(travel_log)










