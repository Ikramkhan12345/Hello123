from django.shortcuts import render
import socket


REMOTE_SERVER = "www.google.com"


def index(request):
    if is_connected(REMOTE_SERVER):
        if request.method == "POST":
            email = request.POST.get("email", "")
            password = request.POST.get("password", "") 
        return render(request, 'index.html')
    else:
        return render(request, 'internet.html')

def signup(request):
    if request.method == "POST":
        import pdb; pdb.set_trace()
    return render(request, 'signup.html')

def is_connected(hostname):
  try:
    host = socket.gethostbyname(hostname)
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False