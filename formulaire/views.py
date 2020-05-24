from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import Utilisateur
from django.contrib import messages
import datetime
from operator import itemgetter
import pytz

tz = pytz.timezone('Europe/Berlin')

from .forms import SymptomesForm
# Create your views here.

def checkAnswer(iterable):
    for element in iterable:
        if element == 'False':
            return False
    return True


def ContactView(request):
    form = SymptomesForm()

    if request.method == "POST":
        form = SymptomesForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            covid = form.cleaned_data["covid"]
            fievre = form.cleaned_data["fievre"]
            courbature = form.cleaned_data["courbature"]
            toux = form.cleaned_data["toux"]
            orl = form.cleaned_data["orl"]
            odorat_sans_nez_bouche = form.cleaned_data["odorat_sans_nez_bouche"]
            tete = form.cleaned_data["tete"]
            digestion = form.cleaned_data["digestion"]
            fatigue = form.cleaned_data["fatigue"]
            autre = form.cleaned_data["autre"]
            odorat_gout = form.cleaned_data["odorat_gout"]
            bouton = form.cleaned_data["bouton"]
            contact1 = form.cleaned_data["contact1"]
            contact2 = form.cleaned_data["contact2"]
            date = datetime.datetime.now(tz)
            utilisateur = Utilisateur.objects.get(email=email)
            prenom = utilisateur.prenom
            nom = utilisateur.nom
            reponses = {'covid19': covid,
                        'fièvre': fievre,
                        'courbature': courbature,
                        'toux': toux,
                        'orl': orl,
                        'odorat sans nez bouché': odorat_sans_nez_bouche,
                        'maux de tête': tete,
                        'digestion': digestion,
                        'fatigue': fatigue,
                        'autres signes': autre,
                        'odorat et goût': odorat_gout,
                        'Éruption de boutons': bouton,
                        'Contact avec une personne atteinte du covid': contact1,
                        'Contact avec une personne ayant un symptôme décrit dans le questionnaire': contact2,
                        }
            val = {
                'prenom': prenom,
                'nom': nom,
                'date': date.strftime("%d-%m-%Y"),
                'heure' : date.strftime("%Hh%M"),
            }
            if checkAnswer(list(reponses.values())):
                val['verdict'] = 'ACCÈS AUTORISÉ'
                autorisation = True
            else:
                val['verdict'] = 'ACCÈS REFUSÉ'
                autorisation = False
                oui = list(itemgetter(*[idx for idx,e in enumerate(list(reponses.values())) if e == 'False'])(list(reponses.keys())))
                val['symptomes'] = oui
                val['email'] = email
                html_message = render_to_string('formulaire/alertEmail.html', val)
                plain_message = strip_tags(html_message)
                send_mail("Symptomes covid", plain_message, settings.EMAIL_HOST_USER, ['testserge@yopmail.com'],
                          fail_silently=False, html_message=html_message)

            html_message = render_to_string('formulaire/email.html', val)
            plain_message = strip_tags(html_message)
            send_mail("Récapitulatif de formulaire", plain_message, settings.EMAIL_HOST_USER, [email],
                      fail_silently=False, html_message=html_message)
            messages.success(request, "Votre formulaire a bien été enregistré, vous avez reçu un mail de confirmation")

            return redirect('formulaire')

    else:
        form = SymptomesForm()

    return render(request, 'formulaire/contact.html', locals())


