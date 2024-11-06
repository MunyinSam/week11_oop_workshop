import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print all cities in Italy
cities_temp = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        cities_temp.append(city['city'])
print("All the cities in", my_country, ":")
print(cities_temp)
print()

# Print the average temperature for all the cities in Italy
temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temps.append(float(city['temperature']))
print("The average temperature of all the cities in", my_country, ":")
print(sum(temps)/len(temps))
print()

# Print the max temperature for all the cities in Italy
temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temps.append(float(city['temperature']))
print("The max temperature of all the cities in", my_country, ":")
print(max(temps))
print()

# Print the min temperature for all the cities in Italy
temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temps.append(float(city['temperature']))
print("The min temperature of all the cities in", my_country, ":")
print(min(temps))
print()

class CitiesDB:

    def __init__(self, cities):
        self.cities = cities

    def aggregate(self, aggregation_key, aggregation_function, dict_list):
        
        _list = []
        print(dict_list)
        
        for value in dict_list:
            _list.append(value[aggregation_key])
        print(_list)
        return aggregation_function(_list)
        

    def filter(self, condition):

        filtered_list = []
        for item in self.cities:
            if condition(item):
                filtered_list.append(item)
        return filtered_list
    
class CountryDB:

    def __init__(self, countries):
        self.countries = countries

    def aggregate(self, aggregation_key, aggregation_function, dict_list):

        _list = []
        for value in dict_list:
            _list.append(value[aggregation_key])
        
        print(aggregation_function(_list))
        return _list

    def filter(self, condition):

        filtered_list = []
        for item in self.countries:
            if condition(item):
                filtered_list.append(item)
        return filtered_list


cities_db = CitiesDB(cities)
countries_db = CountryDB(countries)


specific_country = countries_db.filter(lambda x: x['EU'] == "yes" and x['coastline'] == "no")

country_names = [country['country'] for country in specific_country]

wanted_country = cities_db.filter(lambda x: x['country'] in country_names)

cities_db = cities_db.aggregate(
    "temperature",
    lambda x: min(float(i) for i in x),
    wanted_country
)
# print(cities_db)


# print(cities_db.filter(lambda x: x['city'] in country_names))

# print(specific_country)


# cities_db.aggregate(
#     "temperature", 
#     lambda x: x,
#     cities_db.filter(lambda x: x['country'] == city)
#     )
# Let's write code to
# - print the average temperature for all the cities in Italy
# - print the average temperature for all the cities in Sweden
# - print the min temperature for all the cities in Italy
# - print the max temperature for all the cities in Sweden

class TableDB:
    def __init__(self):
        self.table_database = []

    def insert(self, table):
        self.table_database.append(table)
    def search(self, table_name):
        for table in self.table_database:
            if table.table_name == table_name:
                return table

class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def filter(self, condition):
        return [x for x in self.table if condition(x)]

    def aggregate(self, aggregation_function, aggregation_key):

        return [x for x in self.table if aggregation_function(x[aggregation_key])]

    
    def __str__(self):
        return f"Table: {self.table} / Table_name: {self.table_name}"



print()
cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))

db = TableDB()
db.insert(Table("test1", cities))
searched_db = db.search("test1")
filtered_db = searched_db.filter(lambda x: x['city'] == "Aalborg")
print(filtered_db)
print(searched_db.aggregate(lambda x: float(x) > 15, 'temperature'))