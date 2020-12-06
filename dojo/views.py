from django.shortcuts import render,HttpResponse ,HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from dojo.models import Contact
# Create your views here.

def home(request):
     if request.method == 'POST':
        name = request.POST.get('name' , '')
        phone = request.POST.get('Phone' , '')
        email = request.POST.get('email' , '')
        about = request.POST.get('about' , '')
        massage = 'Nmae :'+name + '\nPhone :'+ phone +'\nEmail :'+email + '\nabout :'+about
        # #recipient_list = ['suvo2510@outlook.com']
        # print(massage)
        detail = Contact(name=name,phone=phone,email=email,about=about)
        detail.save()


        if name and about and email:
            try:
                send_mail('NEW STUDENT WANT TO JOIN', massage, settings.EMAIL_HOST_USER , ['suvo2510@outlook.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('contact')
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')
       # a = send_mail( name, about, settings.EMAIL_HOST_USER, recipient_list ,fail_silently=False,)  
    
     return render(request,'web.html')




def contact(request):
    return render(request,'contact.html')








