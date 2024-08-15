# forms.py
from django import forms
from folio import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.ContactMessage
        fields = ["name", "email", "subject", "message"]
        labels = {
            "name": "Prénom et nom",
            "email": "Courriel",
            "subject": "Sujet",
            "message": "Message",
        }
