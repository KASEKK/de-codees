
from app import db, app
from app.models.db.db_model import User, Profil, Competence, CompetenceSuggestion, Formation, Ressource, Temoignage, Tag, UserTag

with app.app_context():
    print("\n------------------------")
    print("Connexion db établie ✅")
    print("------------------------")

    db.session.query(UserTag).delete()
    db.session.query(Tag).delete()
    db.session.query(Temoignage).delete()
    db.session.query(Ressource).delete()
    db.session.query(Formation).delete()
    db.session.query(Competence).delete()
    db.session.query(CompetenceSuggestion).delete()
    db.session.query(Profil).delete()
    db.session.query(User).delete()
    db.session.commit()

    # Création de données réalistes
    lucie = User(
        email="lucie.reconversion@example.com",
        password="hashed_pwd123",  # mot de passe hashé à faire côté form normalement
        nom="Dupont",
        prenom="Lucie",
        role="contributrice"
    )

    profil = Profil(
        user=lucie,
        biographie="Ancienne assistante sociale en reconversion vers le numérique.",
        motivations="Mieux concilier impact social et équilibre personnel.",
        annee_reconversion=2024,
        region="Bruxelles"
    )

    suggestion1 = CompetenceSuggestion(nom="Python", type="hard")
    suggestion2 = CompetenceSuggestion(nom="Communication", type="soft")

    competences = [
        Competence(profil=profil, nom="Python", type="hard", niveau="intermédiaire"),
        Competence(profil=profil, nom="Communication", type="soft", niveau="avancée")
    ]

    formation = Formation(
        profil=profil,
        nom="Formation Fullstack Python",
        organisme="Technofutur TIC",
        date_debut="2025-04",
        date_fin="2025-09",
        format="présentiel",
        type="certif"
    )

    ressource = Ressource(
        profil=profil,
        titre="Podcast : 'Women in Tech'",
        type="podcast",
        impact="motivation",
        url="https://example.com/women-in-tech",
        commentaire="M'a beaucoup encouragée à persévérer dans ma reconversion."
    )

    temoignage = Temoignage(
        profil=profil,
        contenu="C'est un chemin exigeant, mais chaque pas me rapproche de ma liberté.",
        publier=True
    )

    tag = Tag(nom="reconversion")

    # Étape 1 : insérer user, tag et commit pour générer leurs ID
    db.session.add(lucie)
    db.session.add(tag)
    db.session.commit()

    # Étape 2 : créer le lien UserTag
    user_tag = UserTag(user_id=lucie.id, tag_id=tag.id)
    db.session.add(user_tag)

    # Étape 3 : insérer tout le reste
    db.session.add_all([profil, suggestion1, suggestion2] + competences + [formation, ressource, temoignage])
    db.session.commit()

    print("Données de test insérées avec succès ✅")
