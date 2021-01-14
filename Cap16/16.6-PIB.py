import pygal
from datapackage import Package

from COUNTRIES.country_codes import get_country_code


package = Package('https://datahub.io/core/gdp/datapackage.json')

pib_dict = {}
for resource in package.resources:
    if resource.descriptor['datahub']['type'] == 'derived/csv':
        read = resource.read()
        for data in read:
            if data[2] == 2016:
                country_name = data[0]
                pib = int(float(data[3]))
                code = get_country_code(country_name)
                if code:
                    pib_dict[code] = pib

# Agrupa os países em três níveis populacionais.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in pib_dict.items():
    if pop < 1000000000000:
        cc_pops_1[cc] = pop
    elif pop < 10000000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# Vê quantos países estão em cada nível
print()

wm = pygal.maps.world.World()
wm.force_uri_protocol = 'http'

wm.title = 'World PIB in 2016, by Country'
wm.add('PIB, <  1tri', cc_pops_1)
wm.add('PIB, < 10tri', cc_pops_2)
wm.add('PIB, > 10tri', cc_pops_3)

wm.render_to_file('16.6-PIB.svg')
