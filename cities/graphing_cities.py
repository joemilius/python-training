# -*- coding: utf-8 -*-
cities = ['Oaxaca', 'Mexico', '17.021886', '-96.784615', 'San Miguel de Allende', 'Mexico', '20.910399', '-100.737493', 'Hoi An', 'Vietnam', '15.883323', '108.340323', 'Chiang Mai', 'Thailand', '18.754378', '98.973933', 'Florence', 'Italy', '43.773492', '11.247146', 'Kyoto', 'Japan', '35.131373', '135.526008', 'Udaipur', 'India', '24.3566124', '73.706713', 'Luang Prabang', 'Laos', '19.863075', '102.215407', 'Ubud', 'Indonesia', '-8.502221', '115.265032', 'Istanbul', 'Turkey', '41.162210', '28.765515', 'Mexico City', 'Mexico', '19.407963', '-99.147823', 'Bangkok', 'China', '13.741712', '100.568078', 'Rome', 'Italy', '41.899323', '12.494508', 'Jaipur', 'India', '26.910191', '75.786958', 'Tokyo', 'Japan', '35.668356', '139.736732', 'Siem Reap', 'Cambodia', '13.382729', '103.890376', 'Lisbon', 'Portugal', '38.762778', '-9.182357', 'Charleston, SC', 'USA', '32.788745', '-80.003739', 'Cuzco', 'Peru', '-13.535684', '-71.964657', 'Porto', 'Portugal', '41.159228', '-8.625023', 'Singapore', 'Singapore', '1.352427', '103.866592', 'New Orleans, LA', 'USA', '29.942969', '-90.085780', 'Seville', 'Spain', '37.387139', '-5.986822', 'Mérida', 'Mexico', '20.963875', '-89.596392', 'Kraków', 'Poland', '50.027269', '19.979097']
oaxaca = cities[0:4]
print(oaxaca)

list_of_cities = ['Austin', 'Chicago', 'Denver', 'Houston', 'New York', 'San Francisco', 'Seattle', 'Washington D.C.']

for city in list_of_cities:
    print(city)


city_names = []

for element in cities[::4]:
    city_names.append(element)

print(city_names)

cities_list = []

ind = 0

for group in range(len(cities[::4])):
    cities_list.append(cities[ind:ind+4])
    ind += 4

print(cities_list)
print(cities.index('Tokyo'))

for i in cities_list:
    if i[0] == 'Tokyo':
        print(i)

lat = []
longi = []

for i in cities_list:
    lat.append(float(i[3]))
    longi.append(float(i[2]))

print((float(cities_list[3][3]), float(cities_list[3][2])) == (lat[3], longi[3]))