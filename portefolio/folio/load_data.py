import argparse
import json
from .models import Skill, Project, Contact
from .serializers import SkillSerializer

# Dictionnaire pour mapper les IDs des compétences aux objets Skill
skill_cache = {}

def load_data(filename):
    with open(filename) as f:
        data = json.load(f)

        # Créer des instances de modèle et les enregistrer
        for item in data:
            # Créer ou récupérer l'objet Project
            project, created = Project.objects.get_or_create(
                project=item['project'],
                link=item['link'],
                logo=item['logo']
            )

            # Associer les compétences au projet
            for skill_id in item['language']:
                # Vérifier si la compétence est déjà en cache
                if skill_id not in skill_cache:
                    try:
                        skill = Skill.objects.get(id=skill_id)
                        skill_cache[skill_id] = skill
                    except Skill.DoesNotExist:
                        print(f"Skill with ID {skill_id} not found.")
                        continue  # Passer à la compétence suivante si elle n'existe pas

                project.language.add(skill_cache[skill_id])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Nom du fichier JSON à charger")
    args = parser.parse_args()

    load_data(args.filename)