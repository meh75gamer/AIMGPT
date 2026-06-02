# 🤖 AIMGPT

**Assistant IA autonome avec recherche web et génération de contenu**

Un assistant intelligent alimenté par l'IA qui peut effectuer des recherches sur le web et générer du contenu de qualité.

---

## ✨ Fonctionnalités

- 🔍 **Recherche Web** - Accès aux informations actualisées du web
- 📝 **Génération de Contenu** - Création de contenu intelligent et pertinent
- 🤖 **IA Autonome** - Fonctionnement autonome sans intervention constante
- ⚡ **Rapide et Efficace** - Réponses instantanées et précises

---

## 📋 Prérequis

Avant de commencer, assurez-vous d'avoir :

- Python 3.8+ installé
- pip (gestionnaire de paquets Python)
- Une clé API OpenAI (ou autre fournisseur IA)
- Une clé API pour la recherche web (ex: Google Search API)

---

## 🔧 Installation

### 1. Cloner le repository

```bash
git clone https://github.com/meh75gamer/AIMGPT.git
cd AIMGPT
```

### 2. Créer un environnement virtuel

```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer les variables d'environnement

Créez un fichier `.env` à la racine du projet :

```env
OPENAI_API_KEY=votre_clé_openai
SEARCH_API_KEY=votre_clé_recherche
```

---

## 💻 Utilisation

### Démarrage rapide

```bash
python main.py
```

### Exemples

```python
from aimgpt import AIMGPT

# Initialiser l'assistant
assistant = AIMGPT()

# Effectuer une recherche web
results = assistant.search("dernières nouvelles IA")

# Générer du contenu
content = assistant.generate_content("Rédige un article sur l'IA")
```

---

## 📁 Structure du Projet

```
AIMGPT/
├── main.py              # Point d'entrée principal
├── requirements.txt     # Dépendances du projet
├── .env.example         # Exemple de configuration
├── README.md            # Cette documentation
├── LICENSE              # Licence MIT
└── src/
    ├── aimgpt.py        # Code principal
    ├── search.py        # Module de recherche web
    ├── generator.py     # Module de génération de contenu
    └── config.py        # Configuration
```

---

## 🛠️ Technologies Utilisées

- **Python** - Langage de programmation
- **OpenAI API** - Modèles d'IA
- **Requests** - Requêtes HTTP
- **python-dotenv** - Gestion des variables d'environnement

---

## 📝 Licence

Ce projet est sous licence **MIT**. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## 👤 Auteur

Créé par [meh75gamer](https://github.com/meh75gamer)

---

## 📧 Support

Pour des questions ou des problèmes, veuillez [ouvrir une issue](https://github.com/meh75gamer/AIMGPT/issues).

---

## 🚦 État du Projet

🟡 **En Développement** - Le projet est actuellement en phase de développement actif.

