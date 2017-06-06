from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_content':"HELLO I'M FROM MODELS_APP!"}
    return render(request,'models_app_templ/index.html', context=my_dict)
