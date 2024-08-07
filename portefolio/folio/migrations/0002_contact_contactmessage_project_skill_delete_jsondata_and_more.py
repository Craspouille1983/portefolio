# Generated by Django 5.0.7 on 2024-08-06 16:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("folio", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.CharField(max_length=255)),
                ("link", models.URLField(blank=True, null=True)),
                ("icon", models.ImageField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="ContactMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=255)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("project", models.CharField(max_length=255)),
                ("link", models.URLField(blank=True, null=True)),
                ("logo", models.ImageField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="Skill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "skill",
                    models.CharField(
                        choices=[
                            (1, "HTML5"),
                            (2, "CSS"),
                            (3, "Sass"),
                            (4, "JavaScript"),
                            (5, "Bootstrap"),
                            (6, "TailwindCSS"),
                            (7, "jQuery"),
                            (8, "Python"),
                            (9, "Django"),
                            (10, "VueJS"),
                            (11, "ReactJS"),
                            (12, "Wordpress"),
                            (13, "GitLab"),
                            (14, "GitHub"),
                            (15, "Photoshop"),
                            (16, "Affinity Design"),
                            (17, "Affinity Photo"),
                            (18, "Gimp"),
                            (19, "Figma"),
                            (20, "Adobe XD"),
                        ],
                        default="HTML5",
                        max_length=100,
                    ),
                ),
                ("type", models.CharField(max_length=100)),
                ("level", models.IntegerField()),
                ("experience", models.IntegerField()),
                ("logo_skill", models.ImageField(upload_to="")),
            ],
        ),
        migrations.DeleteModel(
            name="JSONData",
        ),
        migrations.AddField(
            model_name="project",
            name="language",
            field=models.ManyToManyField(to="folio.skill"),
        ),
    ]
