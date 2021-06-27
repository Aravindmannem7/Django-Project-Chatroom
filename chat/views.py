from django.shortcuts import render
from .models import Message

def index(request):
    authenticated = {
            "bool" : "False"
        }
    # print("calling")
    return render(request, 'index.html', authenticated)


def room(request, room_name):
    return render(request, 'test2.html', {
        'room_name': room_name
        
    })

def history(request):
    user = request.user
    msgs = user.message_set.all()
    print(msgs[0].content)
    return render(request , 'history.html',{
        'msgs' : msgs[::-1]
    }
    )

def test(request):
    return render(request , "test3.html",{"test3":15})


