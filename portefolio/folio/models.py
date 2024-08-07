from django.db.utils import IntegrityError
from django.db import models

SKILL_CHOICES = {
    1: "HTML5",
    2: "CSS",
    3: "Sass",
    4: "JavaScript",
    5: "Bootstrap",
    6: "TailwindCSS",
    7: "jQuery",
    8: "Python",
    9: "Django",
    10: "VueJS",
    11: "ReactJS",
    12: "Wordpress",
    13: "GitLab",
    14: "GitHub",
    15: "Photoshop",
    16: "Affinity Design",
    17: "Affinity Photo",
    18: "Gimp",
    19: "Figma",
    20: "Adobe XD",
}

# class SkillName(models.Model):
#     name = models.CharField(max_length=100, choices=tuple(SKILL_CHOICES.items()))
    
#     def __str__(self):
        # return self.name
        


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    text = models.CharField(max_length=255)
    link = models.URLField(null=True, blank=True)
    icon = models.ImageField()

    def __str__(self):
        return self.text


class Skill(models.Model):
    skill = models.CharField(
        max_length=100,
        choices=SKILL_CHOICES,
        default=SKILL_CHOICES[1]  # Définissez une valeur par défaut
    )
    type = models.CharField(max_length=100)
    level = models.IntegerField()
    experience = models.IntegerField()
    logo_skill = models.ImageField()

    def __str__(self):
        return str(self.skill)
    

class Project(models.Model):
    project = models.CharField(max_length=255)
    link = models.URLField(null=True, blank=True)
    logo = models.ImageField()
    language = models.ManyToManyField(Skill)

    def __str__(self):
        return self.project()
