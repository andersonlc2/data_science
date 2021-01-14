import csv
import pygal
from pygal.style import RotateStyle as RC
from COUNTRIES.country_codes import get_country_code

filename = "API_EN.POP.SLUM.UR.ZS_DS2_en_csv_v2_1927862.csv"

with open(filename) as f:
    reader = csv.reader(f)
    reader_row = next(reader)
    reader_row = next(reader)
    reader_row = next(reader)
    reader_row = next(reader)

    pop_slums = {}
    for row in reader:
        country_name = row[0]
        if row[62]:
            porc_pop_slums = float(row[62])
            code = get_country_code(country_name)
            if porc_pop_slums:
                pop_slums[code] = porc_pop_slums

cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for index, value in pop_slums.items():
    if value < 30:
        cc_pops_1[index] = value
    elif value < 60:
        cc_pops_2[index] = value
    else:
        cc_pops_3[index] = value

wm_style = RC('#ff3333')

wm = pygal.maps.world.World(style=wm_style)
wm.force_uri_protocol = 'http'
wm.title = "Population living in slums (percent of urban population)"
wm.add("< 30%", cc_pops_1)
wm.add("< 60%", cc_pops_2)
wm.add("> 60%", cc_pops_3)

wm.render_to_file("16.7-Escolha_seus_dados.svg")
