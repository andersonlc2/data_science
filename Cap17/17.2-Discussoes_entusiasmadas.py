import requests
import pygal
from operator import itemgetter

# Faz uma chamada de API e armazena a resposta.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Processa informações sobre cada artigo submetido.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    url = (
        f"https://hacker-news.firebaseio.com/v0/item/{str(submission_id)}.json")
    submission_r = requests.get(url)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': f'http://news.ycombinator.com/item?id={str(submission_id)}',
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(
    submission_dicts, key=itemgetter('comments'), reverse=True)

names, dics = [], []
for submission_dict in submission_dicts:
    names.append(submission_dict['title'])
    dic = {
        'xlink': submission_dict['link'],
        'value': submission_dict['comments']
    }

    dics.append(dic)

# Cria a visualização dos dados.
chart = pygal.Bar(x_label_rotation=45, show_legend=False)
chart.title = 'Trendy Hackers News'
chart.x_labels = names
chart.add('', dics)

chart.render_to_file('17.2-Discussoes_entusiasmadas.svg')
