import enum


class Department(str, enum.Enum):
    GOUVERNANCE = "Gouvernance"
    FINANCE = "Finance"
    TECHNIQUE = "Technique"
    RH = "Ressources humaines"


class Role(str, enum.Enum):
    DG = "DG"
    ACTIONNAIRE = "Actionnaire"
    INVESTISSEUR = "Investisseur"
    CHARGE_FINANCE = "Chargé de finance"
    CONTROLEUR = "Contrôleur"
    INGENIEUR_IT = "Ingénieur IT"
    MEDIA_MARKETING = "Chargé de média & marketing"
    SECRETAIRE = "Secrétaire"
    AGENT_TERRAIN = "Agent terrain"


class VehicleType(str, enum.Enum):
    TAXI = "Taxi"
    TAXI_BUS = "Taxi-bus"


class ReportType(str, enum.Enum):
    JOURNALIER = "Journalier"
    HEBDOMADAIRE = "Hebdomadaire"
    MENSUEL = "Mensuel"
