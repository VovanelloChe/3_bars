import data_loaders
import math
from collections import namedtuple

bars_json = data_loaders.load_from_json("bars.json")
latig = float(input('lati = '))
longig = float(input('longi = '))


# функция вычисления расстояния от пользователя до текущего бара
def calc_distance(coord, lati, longi):
    return math.pow((coord[0] - lati)**2.0 + (coord[1] - longi)**2.0, 0.5)


l_bars = bars_json.get('features')

# Объявление именованных кортежей
bar_dist = namedtuple('BarDist', ['dist', 'Name'])
bar_count = namedtuple('BarDist', ['sCount', 'Name'])

# Заполнение именованных кортежей
l_bar_dist = list(map(lambda bar: bar_dist(dist=calc_distance(bar.get('geometry')
                    .get('coordinates'), latig, longig),
                    Name=bar.get('properties').get('Attributes').
                    get('Name')), l_bars))
l_bar_count = list(map(lambda bar: bar_count(sCount=bar.get('properties')
                     .get('Attributes').get('SeatsCount'),
                     Name=bar.get('properties').get('Attributes')
                     .get('Name')), l_bars))

# Вывод результата
print('Бар с наименьшим количеством мест: ', min(l_bar_count).Name)
print('Бар с наибольшим количеством мест: ', max(l_bar_count).Name)
print('Ближайший бар: ', min(l_bar_dist).Name)
