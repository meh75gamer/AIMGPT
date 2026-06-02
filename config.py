"""
Module de configuration pour AIMGPT
"""

import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

class Config:
    """Classe de configuration principale"""
    
    # ===== API KEYS =====
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    SEARCH_API_KEY = os.getenv('SEARCH_API_KEY', '')
    
    # ===== MODELE IA =====
    MODEL = os.getenv('MODEL', 'gpt-3.5-turbo')
    TEMPERATURE = float(os.getenv('TEMPERATURE', 0.7))
    MAX_TOKENS = int(os.getenv('MAX_TOKENS', 2000))
    
    # ===== CONFIGURATION GENERALE =====
    DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
    LANGUAGE = os.getenv('LANGUAGE', 'fr')
    REQUEST_TIMEOUT = int(os.getenv('REQUEST_TIMEOUT', 30))
    
    @classmethod
    def validate(cls):
        """Valider la configuration"""
        if not cls.OPENAI_API_KEY:
            raise ValueError("⚠️  OPENAI_API_KEY n'est pas configurée. Vérifiez votre fichier .env")
        return True
