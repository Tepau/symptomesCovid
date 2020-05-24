from django import forms
from .models import Utilisateur


choices = [(False, 'OUI'), (True, 'NON')]


class SymptomesForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'size': '40'}))
    covid = forms.ChoiceField(widget=forms.RadioSelect,
                              label='Avez-vous été atteint du Covid 19 dans les 15 derniers jours ?', choices=choices)
    fievre = forms.ChoiceField(widget=forms.RadioSelect,
                              label='De la fièvre (température égale ou supérieur à 37,8 ) ?', choices=choices)
    courbature = forms.ChoiceField(widget=forms.RadioSelect,
                              label='Des courbatures ?', choices=choices)
    toux = forms.ChoiceField(widget=forms.RadioSelect,
                              label='De la toux ?', choices=choices)
    orl = forms.ChoiceField(widget=forms.RadioSelect,
                            label="Des signes ORL : rhume, angine, pharyngite (en dehors de la rhinite ou d'une conjonctivite allergique diagnostiquée) ?",
                            choices=choices)
    odorat_sans_nez_bouche = forms.ChoiceField(widget=forms.RadioSelect,
                                               label="Une perte de l'odorat sans nez bouché ou une perte du goût des aliments (distincte de la perte d'appétit) ?",
                                               choices=choices)
    tete = forms.ChoiceField(widget=forms.RadioSelect,
                              label='Des maux de tête inhabituels ?', choices=choices)
    digestion = forms.ChoiceField(widget=forms.RadioSelect,
                              label='Des troubles digestifs (nausée, vomissement, diarrhée) ?', choices=choices)
    fatigue = forms.ChoiceField(widget=forms.RadioSelect,
                              label='Une fatigue inhabituelle ?', choices=choices)
    autre = forms.ChoiceField(widget=forms.RadioSelect,
                              label="D'autres signes comme des moments de désorientation ou des chutes inexpliquées ?",
                              choices=choices)
    odorat_gout = forms.ChoiceField(widget=forms.RadioSelect,
                              label='Une perte ou une modification de l’odorat ou du goût ?', choices=choices)
    bouton = forms.ChoiceField(widget=forms.RadioSelect,
                              label='Une éruption de boutons ou bien de tâches rouge sur le corps ?', choices=choices)
    contact1 = forms.ChoiceField(widget=forms.RadioSelect,
                              label='Avez-vous été en contact avec une personne atteinte du COVID 19 ?', choices=choices)
    contact2 = forms.ChoiceField(widget=forms.RadioSelect,
                                label="Avez-vous été en contact avec une personne qui présentait l'un des signes mentionnés dans les questions 1 à 10 ?",
                                choices=choices)

    def clean(self):
        cleaned_data = super(SymptomesForm, self).clean()
        email = cleaned_data.get("email")
        all_email = []
        all_people = Utilisateur.objects.all()
        for people in all_people:
            all_email.append(people.email)
        if email not in all_email:
            raise forms.ValidationError("Le mail n'est pas valide")

        return cleaned_data





