import json
import pygal

from pygal.style import RotateStyle as RC, LightColorizedStyle as LCS

from COUNTRIES.country_codes import get_country_code


# Carrega os dados em uma lista.
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Constrói um dicionário com dados das populações.
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name.split(', ')[0])
        if code:
            cc_populations[code] = population
        else:
            print(country_name)

# Agrupa os países em três níveis populacionais.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# Vê quantos países estão em cada nível
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RC('#336699', base_style=LCS)

wm = pygal.maps.world.World(style=wm_style)
wm.force_uri_protocol = 'http'

wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('16.5-Todos_paises.svg')
