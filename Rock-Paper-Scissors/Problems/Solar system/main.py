# create the planets.txt
f = open('planets.txt', 'w', encoding='utf-8')
planets = ['Mercury\n', 'Venus\n', 'Earth\n', 'Mars\n', 'Jupiter\n', 'Saturn\n', 'Uranus\n', 'Neptune']
f.writelines(planets)
f.close()