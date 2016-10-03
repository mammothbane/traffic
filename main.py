import argparse

import json

from traffic.car import Car
from traffic.traffic import Traffic


parser = argparse.ArgumentParser(description='Solve the traffic problem.')
parser.add_argument('file', metavar='FILE', help='json problem definition file')
parser.add_argument('--strategy', help='what search strategy do we use?')
args = parser.parse_args()

with open(args.file) as f:
    content = json.load(f)

cars = []
for elem in content['cars']:
    car = Car(elem, None, elem['dir'], (elem['x'], elem['y']), elem.get('len', 2), elem.get('player', False))
    cars.append(car)

traffic = Traffic(content['exit'], cars, (content['dimens']['x'], content['dimens']['y']))
