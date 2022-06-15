item_1 = "Las Vegas"
item_2 = 73
item_3 = 3.14159
item_4 = (7 == 4)
item_5 = (4 >= 7)

# print(type(item_1))

top_travel_cities = ['Solta', 'Greenville', 'Buenos Aires', 'Los Cabos', 'Walla Walla Valley', 'Marakesh', 'Albuquerque', 'Archipelago Sea', 'Iguazu Falls', 'Salina Island', 'Toronto', 'Pyeongchang']
top_canadian_city = top_travel_cities[-2]
top_two = top_travel_cities[0:2]
# print(top_travel_cities[1])
# print(top_travel_cities[-1])
# print(top_canadian_city)
# print(top_travel_cities[4:6])
# print(top_two)
# print(top_travel_cities[:3])
# print(top_travel_cities[-4:-2])
# print(top_travel_cities[-3:])

continent_travel_cities = ['Buenos Aires, Argentina', 'Iguazu Falls, Argentina', 'Los Cabos, Mexico', 'Walla Walla Valley, Washington', 'Albuquerque, New Mexico', 'Greenville, South Carolina', 'Toronto, Canada', 'Archipelago Sea', 'Salina Island, Sicily', 'Solta, Croatia', 'Marakesh, Morocco', 'Pyeongchang, South Korea']
south_america = continent_travel_cities[0:3]
north_america = continent_travel_cities[3:7]
not_a_city = continent_travel_cities[7]
europe = continent_travel_cities[8:10]
asia = continent_travel_cities[-2:]
# print(south_america)
# print(north_america)
# print(not_a_city)
# print(europe)
# print(asia)

continent_travel_cities.append('Wuhan, China')
# print(continent_travel_cities)
print(len(continent_travel_cities))
continent_travel_cities.pop()
# print(continent_travel_cities)
print(len(continent_travel_cities))
continent_travel_cities.pop(continent_travel_cities.index('Archipelago Sea'))
# print(continent_travel_cities)
print(len(continent_travel_cities))

repeat_cities = ['Buenos Aires, Argentina', 'Iguazu Falls,Argentina', 'Los Cabos, Mexico', 'Walla Walla Valley, Washington', 'Albuquerque, New Mexico', 'Greenville, South Carolina', 'Toronto, Canada', 'Archipelago Sea', 'Salina Island, Sicily', 'Solta, Croatia', 'Marakesh, Morocco', 'Pyeongchang, South Korea', 'Wuhan, China', 'Wuhan, China', 'Toronto, Canada', 'Albuquerque, New Mexico', 'Salina Island, Sicily']
repeat_to_unique_cities_set = set(repeat_cities)
print(repeat_to_unique_cities_set)
print(len(repeat_cities))
print(len(repeat_to_unique_cities_set))

back_to_list_cities = list(repeat_to_unique_cities_set)
print(back_to_list_cities)
print(len(back_to_list_cities))

practice_cities = ['Buenos Aires, Argentina',
                     'Iguazu Falls,Argentina',
                     'Los Cabos, Mexico',
                     'Walla Walla Valley, Washington',
                     'Albuquerque, New Mexico',
                     'Greenville, South Carolina',
                     'Toronto, Canada',
                     'Archipelago Sea',
                     'Salina Island, Sicily',
                     'Solta, Croatia',
                     'Marakesh, Morocco',
                     'Pyeongchang, South Korea',
                     'Wuhan, China',
                     'Wuhan, China',
                     'Toronto, Canada',
                     'Albuquerque, New Mexico',
                     'Salina Island, Sicily'
                     ]
practice_cities_length = len(practice_cities)
practice_cities_set = set(practice_cities)
print(practice_cities_length)
print(len(practice_cities_set))