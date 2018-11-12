import requests, json
import jdatetime

'''
In this code we use jdatetime to get jalali date and requests to get that page we need 
dict_result : return a dictionary that include weather our city and jalali date
'''
api_address = 'http://api.openweathermap.org/data/2.5/weather?q=%s,%s&APPID=84495e742bed7b6a65cb86fde09af7af'
dict_result = {}
date = jdatetime.date.today()
dict_result['date'] = date
city = [['toronto', 'ca'], ['tehran', 'ir'], ['mashhad', 'ir'], ['shiraz', 'ir'], ['isfahan', 'ir'], ['tabriz', 'ir']]
for ci in city:
    url = api_address % (ci[0], ci[1])
    json_data = requests.get(url)

    if json_data.status_code == 200:
        dict_data = json.loads(json_data.text)
        dict_result[ci[0]] = dict_data
    else:
        print json_data.status_code
print (str(dict_result['tabriz']))