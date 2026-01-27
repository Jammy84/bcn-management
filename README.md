# Bombacar Nayo – Application de gestion

Application web FastAPI pour la gestion des véhicules, paiements, utilisateurs et rapports PDF.

## Démarrage rapide (développement)

1. Créer un fichier `.env` à la racine (voir `.env.example`):

```
DATABASE_URL=postgresql+asyncpg://USER:PASSWORD@HOST:PORT/DBNAME
SECRET_KEY=change-me
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
