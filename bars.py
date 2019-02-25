import data_loaders
import math
from collections import namedtuple

barsjson = data_loaders.load_from_json("bars.json")

latig = float(input('lati = '))

longig = float(input('longi = '))

dist_min = 10e5

# функция вычисления расстояния от пользователя до текущего бара
def calcDistance(coord, lati, longi):
    return math.pow((coord[0] - lati)**2.0 + (coord[1] - longi)**2.0, 0.5)

#
lbars = barsjson.get('features')

# Объявление именованных кортежей
BarDist = namedtuple('BarDist', ['dist', 'Name'])
BarCount = namedtuple('BarDist', ['sCount', 'Name'])

# Заполнение именованных кортежей
lBarDist = list(map(lambda bar: BarDist(dist = calcDistance(bar.get('geometry').get('coordinates'), latig, longig),
Name = bar.get('properties').get('Attributes').get('Name')), lbars))

lBarCount = list(map(lambda bar: BarCount(sCount = bar.get('properties').get('Attributes').get('SeatsCount'),
Name = bar.get('properties').get('Attributes').get('Name')), lbars))

# Вывод результата
print ('Бар с наименьшим количеством мест: ', min(lBarCount).Name)
print ('Бар с наибольшим количеством мест: ', max(lBarCount).Name)
print ('Ближайший бар: ', min(lBarDist).Name)
