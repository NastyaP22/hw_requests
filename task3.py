import requests
from pprint import pprint

url = 'https://api.stackexchange.com/2.3/search?fromdate=1683849600&todate=1684022400&order=desc&sort=activity&tagged=python&site=stackoverflow'
response_data = requests.get(url).json()
count_questions = len(response_data['items'])
print(f'За период с 12 по 14 мая на сайте было {count_questions} вопросов с тэгом python')
pprint(response_data)