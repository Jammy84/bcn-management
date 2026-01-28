# Bombacar Nayo – Application de gestion

Application web FastAPI pour la gestion des véhicules, paiements, utilisateurs et rapports PDF.

## Démarrage rapide (développement)

1. Créer un fichier `.env` à la racine (voir `.env.example`):

```
DATABASE_URL=postgresql+asyncpg://USER:PASSWORD@HOST:PORT/DBNAME
SECRET_KEY=change-me
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
SUPABASE_STORAGE_BUCKET=reports
```

2. Installer les dépendances:

```
pip install -r requirements.txt
```

3. Lancer l’application:

```
uvicorn app.main:app --reload
```

## Supabase
Pour Supabase, utilise les informations du projet (Connection string) et adapte au format suivant:

```
DATABASE_URL=postgresql+asyncpg://USER:PASSWORD@HOST:PORT/DBNAME
```

## Déploiement Render (Docker)
1. Pousser le code sur GitHub.
2. Créer un nouveau service Render en choisissant le dépôt.
3. Plan: **Starter**.
4. Variables d’environnement:
	- DATABASE_URL (Supabase)
	- SECRET_KEY
	- SUPABASE_URL
	- SUPABASE_SERVICE_ROLE_KEY
	- SUPABASE_STORAGE_BUCKET (ex: reports)

Les PDF seront envoyés dans Supabase Storage si ces variables sont définies.
Le bucket doit être **public** pour que le lien de téléchargement fonctionne.

## Taux de paiement (Taxi / Taxi-bus)
Après démarrage, crée les taux via l’API:

```
POST /payment-rates
{
	"vehicle_type": "Taxi",
	"amount": 55000
}
```

```
POST /payment-rates
{
	"vehicle_type": "Taxi-bus",
	"amount": 110000
}
```

## Notes
- Le logo doit être placé dans `static/images/logo.png`.
- Les rapports PDF sont générés dans `reports/`.
