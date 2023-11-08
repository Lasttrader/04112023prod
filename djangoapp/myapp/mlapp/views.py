from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.


def get_predict(request):
    X_scaled = [0.82737724, -0.53037664,  0.43279337, -0.47367361, -
                0.50143844,  0.73769513, -1.44232155, -2.1037683,   0.58111394]
    api_message = requests.post('http://0.0.0.0:5000/api/v1/add_message/',
                                json={'X_scaled': X_scaled})
    print(api_message)
    if api_message.ok:
        print(api_message.json())
    return HttpResponse(f'Your pessenger predict {api_message.json()}')
