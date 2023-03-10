from django.shortcuts import render
from .models import Contact
from json import dumps
# Create your views here.

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        mode_of_contact = request.POST.get('contact')
        question_categories = request.POST.get('queries')
        message = request.POST.get('message')
        contact_data = Contact(name=name, email=email, phone=phone, mode_of_contact=mode_of_contact, question_categories=question_categories, message=message)
        contact_data.save()
        # create data dictionary
        dataDictionary = {
            'hello': name
        }
        dataJSON = dumps(dataDictionary)
        return render(request, 'success.html', {'data': dataJSON})


        #return render(request, 'success.html')
    

    return render(request, 'contact.html')
#def send_dictionary(request):
    