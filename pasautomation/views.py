from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'log-in.html', {})


def logMeIn(request):
    # username = request.GET.get("username", None)
    # password = request.GET.get("password", None)
    username = request.POST.get("lemail", None)
    password = request.POST.get("lpassword", None)

    # RESTApi 
    # url = 
    print("-"*50,username, password)
    if username == "a@abc.com" and password == "12345":
        print("Inside logmein")
        return render(request, 'index.html', {})
    else:
        return render(request, 'log-in.html', {})