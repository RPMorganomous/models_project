from django.shortcuts import render
from django.http import HttpResponse
from models_app.models import Topic,Webpage,AccessRecord

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}

    # my_dict = {'insert_content':"HELLO I'M FROM MODELS_APP!"}
    return render(request,'models_app_templ/index.html', context=date_dict)
