from django.shortcuts import render
from django.core.mail import send_mail
from folio import models
from folio import forms


def index(request):
    contacts = models.Contact.objects.all()
    skills = models.Skill.objects.all()
    projet = models.Project.objects.all()
    form = forms.ContactForm()
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            # Enregistrement en base de données (optionnel)
            form.save()
            # Envoi d'un email
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["email"]
            recipient = "fredericsejournant7@gmail.com"
            send_mail(
                subject,
                message,
                sender,
                [recipient],
                fail_silently=False,
            )
            return render(
                request,
                "folio/index.html",
                context={
                    "form": form,
                    "success_message": "Votre message a bien été envoyé.",
                },
            )
    else:
        form = forms.ContactForm()

    return render(
        request,
        "folio/index.html",
        context={
            "skills": skills,
            "contacts": contacts,
            "projets": projet,
            "form": form,
        },
    )


# def contact(request):
#     return render(request, "folio/index.html", context={"form": form})
