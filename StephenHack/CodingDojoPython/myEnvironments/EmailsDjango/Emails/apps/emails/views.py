from django.shortcuts import render, redirect, HttpResponse
from .models import Email
# Create your views here.
def index(request):
    if not 'errors' in request.session: 
        request.session['errors'] = []
    return render (request, 'emails/index.html')

def create(request):
    if request.method == "POST": #Returns the method/HTTP verb associated with the request
        result = Email.emailMgr.register(request.POST['email']) #Email Manager of the Email class, register method, 
        if result[0]: #if (True, e) 
            request.session['email'] = result[1].email #sets the new session value to the new email 
            request.session.pop('errors') #pop the one error in session
            return redirect('/success')
        else:
            request.session['errors'] = result[1] #populate the session error variable
            return redirect('/')
    else:
        return redirect ('/')

def success(request):
    emails = Email.emailMgr.all() #Get all the values in Email
    return render (request, 'emails/success.html', {'emails': emails, 'your_email': request.session.get('email')})

def destroy(request, id):
    result = Email.emailMgr.destroy(id)
    if result[0]:
        return redirect('/success')
    else:
        print result[1]
