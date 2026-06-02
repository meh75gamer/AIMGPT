"""
Module principal de l'assistant IA AIMGPT
"""

import openai
from config import Config

class AIMGPT:
    """Classe principale de l'assistant IA"""
    
    def __init__(self):
        """Initialiser l'assistant IA"""
        Config.validate()
        
        # Configurer OpenAI
        openai.api_key = Config.OPENAI_API_KEY
        
        # Historique des messages pour le contexte
        self.conversation_history = []
        self.model = Config.MODEL
        self.temperature = Config.TEMPERATURE
        self.max_tokens = Config.MAX_TOKENS
        
        print(f"✅ Modèle configuré: {self.model}")
    
    def chat(self, user_message: str) -> str:
        """
        Envoyer un message et obtenir une réponse
        
        Args:
            user_message: Le message de l'utilisateur
            
        Returns:
            La réponse de l'assistant IA
        """
        try:
            # Ajouter le message de l'utilisateur à l'historique
            self.conversation_history.append({
                "role": "user",
                "content": user_message
            })
            
            # Appeler l'API OpenAI
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=self.conversation_history,
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            
            # Extraire la réponse
            assistant_message = response.choices[0].message.content
            
            # Ajouter la réponse à l'historique
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
        
        except openai.error.AuthenticationError:
            return "❌ Erreur d'authentification. Vérifiez votre clé API OpenAI."
        except openai.error.RateLimitError:
            return "⚠️  Limite de requêtes atteinte. Attendez un moment avant de réessayer."
        except Exception as e:
            return f"❌ Erreur: {str(e)}"
    
    def clear_history(self):
        """Effacer l'historique des conversations"""
        self.conversation_history = []
        print("🗑️  Historique effacé")
    
    def get_history(self) -> list:
        """Obtenir l'historique des conversations"""
        return self.conversation_history
    
    def search_web(self, query: str) -> str:
        """
        Effectuer une recherche web
        
        Args:
            query: Terme de recherche
            
        Returns:
            Les résultats de la recherche
        """
        # À implémenter avec une API de recherche
        # Exemple : Google Search API, Bing Search API, etc.
        print(f"🔍 Recherche web pour: {query}")
        return "Fonctionnalité de recherche web en développement..."
    
    def generate_content(self, prompt: str) -> str:
        """
        Générer du contenu
        
        Args:
            prompt: Le prompt pour la génération
            
        Returns:
            Le contenu généré
        """
        return self.chat(prompt)
def search_web(self, query):
    return "Fonctionnalité de recherche web en développement..."
