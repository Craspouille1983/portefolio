from django.shortcuts import render
from django.core.mail import send_mail
from folio import models
from folio import forms
from portefolio.settings import EMAIL_HOST


def index(request):
    contacts = models.Contact.objects.all()
    skills = models.Skill.objects.all()
    projects = models.Project.objects.all()
    SKILL_CHOICES = dict(models.SKILL_CHOICES)
    for skill in skills:
        skill.skill_id = SKILL_CHOICES[int(skill.skill)]
    for project in projects:
        project.skills_list = [
            SKILL_CHOICES.get(skill.id) for skill in project.language.all()
        ]
    skill_counts = {}
    for project in projects:
        for skill in project.language.all():
            skill_id =  SKILL_CHOICES.get(skill.id)
            skill_counts[skill_id] = skill_counts.get(skill_id, 0) + 1

    # Filtrer les skills en fonction des occurrences
    filtered_skills = [skill for skill, count in skill_counts.items()]


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
            recipient = EMAIL_HOST
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
            "filtered_skills": filtered_skills,
            "contacts": contacts,
            "projets": projects,
            "SKILL_CHOICES": SKILL_CHOICES,
            "form": form,
        },
    )
