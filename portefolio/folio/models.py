from django.db import models

class Contact(models.Model):
    text = models.CharField(max_length=255)
    link = models.URLField(null=True, blank=True)
    icon = models.ImageField()

    def __str__(self):
        return self.text

class Skill(models.Model):
    skill = models.CharField(max_length=255)
    level = models.IntegerField()
    experience = models.IntegerField()
    logo_skill = models.ImageField()

    def __str__(self):
        return self.skill
    
class Project(models.Model):
    project = models.CharField(max_length=255)
    link = models.URLField(null=True, blank=True)
    logo = models.ImageField()
    language = models.CharField(max_length=255)
    framework = models.CharField(max_length=255)

    def __str__(self):
        return self.project()
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
