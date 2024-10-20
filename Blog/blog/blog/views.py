from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from  .forms import ContactForm
from django.urls import reverse
from django.core.mail import send_mail



def home_view(request):
    # return HttpResponse('Hello World!')
    return render(request, 'home.html')

def contact_view(request):
    # return HttpResponse('Contactez nous')
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)                                      # la on recupere les imformation qui sont envoyer avec le parametre qui recupere toutes les informations en question
        if form.is_valid():    # la on recupere le nom
            nom =form.cleaned_data['nom']
            prenom =form.cleaned_data['prenom'] 
            email =form.cleaned_data['email']
            message =form.cleaned_data['message']
           
            titre = f'blog |  {nom} {prenom} {email}'
            send_mail(titre, message, 'blog.maxadj@gmail.com', ['blog.maxadj@gmail.com',])


        return HttpResponseRedirect(reverse('remerciements'))                  # ici une fois les information entrer on doit avoir une page de remerciement 
    return render(request, 'contact.html', {"form":form})


def remerciements_view(request):
    return HttpResponse("merci de nous avoir contacter")

