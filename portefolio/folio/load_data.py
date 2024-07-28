import json
from .models import Skill
from .serializers import SkillSerializer

# Charger les données JSON
with open('skills.json') as f:
    data = json.load(f)

# Créer des instances de modèle et les enregistrer
for item in data:
    serializer = SkillSerializer(data=item)
    if serializer.is_valid():
        serializer.save()