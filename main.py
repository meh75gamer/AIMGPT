"""
Point d'entrée principal de l'application AIMGPT
"""

import os
from dotenv import load_dotenv
from src.aimgpt import AIMGPT

# Charger les variables d'environnement
load_dotenv()

def main():
    """Fonction principale"""
    print("=" * 50)
    print("🤖 Bienvenue dans AIMGPT")
    print("=" * 50)
    print()
    
    # Initialiser l'assistant IA
    try:
        assistant = AIMGPT()
        print("✅ Assistant IA initialisé avec succès!")
        print()
        
        # Boucle interactive
        while True:
            print("-" * 50)
            user_input = input("📝 Entrez votre question (ou 'quit' pour quitter): ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Au revoir!")
                break
            
            if not user_input:
                print("⚠️  Veuillez entrer une question valide.")
                continue
            
            # Générer une réponse
            response = assistant.chat(user_input)
            print(f"\n🤖 Assistant: {response}\n")
    
    except Exception as e:
        print(f"❌ Erreur : {e}")
        print("Assurez-vous que votre clé API OpenAI est correctement configurée dans le fichier .env")

if __name__ == "__main__":
    main()
