#Django 
from django.http import HttpResponse

#utilities
from datetime import datetime
import json



def hello_world(request):

    return HttpResponse('Oh, hi! Current server time in {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y -%H:%M hrs')
        ))

def sort_integrest(request):
    numbers = [int(i)for i in request.GET['numbers'].split(',')]
    sorted_inst = sorted(numbers)
    #import pdb;pdb.set_trace()
    data = {
        'status': 'ok',
        'numbers': sorted_inst,
        'message': 'Integers sorted succeddfully.' 
    }
    return HttpResponse(
        json.dumps(data, indent=4),
          content_type='application/json')

def say_hi(request,name,age):
    if age < 12:
        message = f'Sorry {name},you are not allowed here'
    else:
        message = f'Hi, {name}! Welcome to plazigram'
    return HttpResponse(message)
