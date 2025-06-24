from app.models.dto.competence.competence_suggestion_schema import CompetenceSuggestionSchema

print("\n\n✅ Test Suggestion de compétence :")
suggestion_ok = {
    "nom": "Docker",
    "type": "hard"
}

schema_sugg = CompetenceSuggestionSchema()
print(schema_sugg.load(suggestion_ok))
