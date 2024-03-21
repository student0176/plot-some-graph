import json

import pygal
import pygal_maps_world.maps
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
# from pygal.i18n import COUNTRIES # 這裏標紅是因爲此插件已經棄用，可用pygal_maps_world來代替
from pygal_maps_world.i18n import COUNTRIES


### 看下COUNTRIES裏面的成分
# for country_code in sorted(COUNTRIES.keys()): # 按照字母排序
    # print(country_code, COUNTRIES[country_code])

### 本來字典裏有3字簡稱，但pygal需要2字簡稱，所以借用COUNTRIES
def get_country_code(country_name):
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
    return None # 這裏一開始寫到if那裏的else去了，當然只檢查第一個，emmm
# print(get_country_code('Somalia'))
# print(get_country_code('Adorra'))

filename = './csv_and_json/pupulation_data.json'
with open(filename) as f:
    pop_data = json.load(f) #reader是一個iterator，將一行按逗號弄成list后讀進來

di = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        population = int(float(pop_dict['Value']))
        country_full_name = pop_dict['Country Name']
        country_name = get_country_code(country_full_name)
        if country_name:
            di[country_name] = population
            # print(country_name + ": " + str(population))
        else:
            continue
            # print('ERROE - ' + ": " + country_full_name)
# print(dict)
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in di.items(): # 要是不用item,就會把key的前兩個字母分別給cc,pop
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3), )

wm_style = RS('#336699',base_style=LCS)

wm = pygal_maps_world.maps.World(style=wm_style) # 改了style后沒有施加到wm上,當然不會變化
wm.title = 'Populations in 2010'
wm.add('0-10m',cc_pops_1)
wm.add('10m-1bn',cc_pops_2)
wm.add('>1bn',cc_pops_3)


wm.render_to_file('./image_map/population_change_style.svg')


