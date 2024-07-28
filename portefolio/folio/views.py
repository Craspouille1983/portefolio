from django.shortcuts import render
import folio.models 

def index(request):
    contacts = folio.models.Contact.objects.all()
    skills = folio.models.Skill.objects.all()
    projet = folio.models.Project.objects.all()
    return render(request, 'folio/index.html', context={'skills': skills, 'contacts': contacts, 'projets': projet})