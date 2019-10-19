import requests
import pprint
URL = "https://api.telegram.org/bot962102849:AAHmDtPsD8xJrf_6lC0HmfUTpzmz4i9hLuY"
r = requests.get(f'{URL}/getUpdates')
#print(r.json())
#print(r)
#get updates = мы сами делаем запрос к телеграму и получаем обновления
#веб хуки - требует своего сервера+ доменного имени и телеграм сам отправляет изменения.
pprint.pprint((r.json()))
# payload = {}
# payload['chat_id'] =431073306
# payload['text'] = 'I`d like this fight'
# print(payload)
# r = requests.post(f'{URL}/sendMessage', data =payload)


