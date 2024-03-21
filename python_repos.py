import pygal
import pygal_maps_world.maps
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url) # r為響應對象，是返回一個字符串。如果這個字符串以JSON格式編碼，可用json轉為dict
print('Status code:',r.status_code) # Status code: 200，狀態碼200表示請求成功

response_dict = r.json()
# print(response_dict.keys()) # 不出意外，得到dict_keys(['total_count', 'incomplete_results', 'items'])
print('Total repositories:',response_dict['total_count'])


repo_dicts = response_dict['items']
# print('Repositories returned:',len(repo_dicts))

# repo_dict = repo_dicts[0] # 用來查蘭第一個倉庫信息
# print('\nKeys:',len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

# print('\nSelected information about each repository:')
# for repo_dict in repo_dicts:
    # print('Name:',repo_dict['name'])
    # print('Owner:',repo_dict['owner']['login'])
    # print('Stars:',repo_dict['stargazers_count'])
    # print('Repository:',repo_dict['html_url'])
    # print('Created:',repo_dict['created_at'])
    # print('Updated:',repo_dict['updated_at'])
    # print('Description:',repo_dict['description'])
    # print()

names, stars = [], []
dict_list = []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # stars.append(repo_dict['stargazers_count'])
    plot_dict = {
        'value' : repo_dict['stargazers_count'],
        'label' : repo_dict['description'],
        'xlink' : repo_dict['html_url']
    }
    dict_list.append((plot_dict))

my_style = RS('#333366',base_style=LCS)
# my_config = pygal.Config()
# my_config.x_label_rotation = 45
# my_config.show_legend=False
# my_config.title_font_size = 24
# my_config.label_font_size = 14
# my_config.major_label_label_font_size = 18
# my_config.truncate_label = 15
# my_config.show_y_guides = False
# my_config.width = 1000

# chart = pygal.Bar(my_config,style = my_style,)
# chart.title = 'Most-Starred python projects on Github'

chart = pygal.Bar(style = my_style,x_label_rotation=45,show_legend=False)
chart.title = 'Most-Starred python projects on Github'

chart.x_labels = names
chart.add('',dict_list) # 如果傳入list裏面是字典，將value畫高度，將label設置鼠標懸停。xlink就是跳轉網址（如果有的話，變爲交互性的）

chart.render_to_file('./image_map/python_repos_finetune3.svg')









