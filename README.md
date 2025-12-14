# Mini Matrix Clock

![License](https://img.shields.io/github/license/CordaAvlao/MiniMatrixClock)
![Version](https://img.shields.io/github/v/release/CordaAvlao/MiniMatrixClock)

A minimalist, always-on-top digital clock for Windows with a "Matrix" aesthetic. Designed to be unobtrusive, smart, and fully customizable.

## 🚀 What's New (v6.1)
*   **Startup Fix**: New robust startup logic (Registry Force) to ensure it runs even on simplified OS (Atlas/Revi).
*   **Smart Background**: 
    *   **Flicker-Free**: Continuous monitoring of the background color.
    *   **Opaque Safety**: Prevents accidental transparency on dark taskbars.
    *   **Desktop Exclusion**: Clicking the Desktop wallpaper no longer triggers transparency!
*   **Zoom & Scale**: Resize the clock 50% to 150% (Controls UI, Font, and Frame).
*   **Fonts**: Choose between Digital, Console, Modern, Bold, or Terminal fonts.
*   **Performance**: Optimized 50ms refresh rate for "Always on Top" enforcement.

## ⚙️ How it works
1.  **Launch**: Run `MiniClock.exe`. It positions itself automatically above the taskbar.
2.  **Move**: Drag and drop anywhere. It remembers its position.
3.  **Options**: Right-click the text to change colors, toggle startup, or exit.
4.  **Zero Distraction**: It detects background colors to blend in and fades out when needed.

## 📥 Downloads
Download the latest portable executable here:  
👉 **[Releases](https://github.com/CordaAvlao/MiniMatrixClock/releases)**

## 🔧 Technical Details
*   **Language**: Python 3.x
*   **GUI**: Tkinter (No heavy frameworks)
*   **API**: Windows API (ctypes) for Taskbar detection, transparency, and registry access.
*   **Portable**: Single EXE file, no installation required.

## 🤝 Contributing
Contributions are welcome!

1.  Fork the repository
2.  Create a feature branch (`feature/my-feature`)
3.  Submit a Pull Request

Suggestions, improvements, and bug reports are greatly appreciated.

## ❤️ Support the Project
Hi! I’m **CordaAvlao** 👋

I develop small, simple utilities for Windows, like **MiniClock** and **Beepschéduler**.  
My work is free, but it takes time to build and improve these tools.  
If you’d like to support my work, you can make a small contribution here:

👉 **[Support via PayPal](https://www.paypal.com/ncp/payment/NPGMPUL9N9TFQ)**

Thank you very much for your support!

## 📜 License
MIT License. See [LICENSE](LICENSE) file for details.

---

# Version Française 🇫🇷

Une horloge numérique minimaliste "toujours visible" pour Windows avec une esthétique "Matrix". Conçue pour être discrète, intelligente et entièrement personnalisable.

## 🚀 Nouveautés (v6.1)
*   **Démarrage Réparé** : Nouvelle logique robuste (Force Registry) pour garantir le lancement même sur les OS allégés (Atlas/Revi).
*   **Fond Intelligent** :
    *   **Anti-Scintillement** : Surveillance continue de la couleur d'arrière-plan.
    *   **Sécurité Opacité** : Empêche la transparence accidentelle sur les barres des tâches sombres.
    *   **Exclusion Bureau** : Le clic sur le fond d'écran ne déclenche plus la transparence !
*   **Zoom & Échelle** : Redimensionnez l'horloge de 50% à 150% (Ajuste l'interface, la police et le cadre).
*   **Polices** : Choix entre Digital, Console, Moderne, Gras ou Terminal.
*   **Performance** : Rafraîchissement optimisé à 50ms pour le "Toujours Visible".

## ⚙️ Fonctionnement
1.  **Lancement** : Lancez `MiniClock.exe`. Elle se positionne automatiquement au-dessus de la barre des tâches.
2.  **Déplacement** : Glissez-déposez n'importe où. Elle mémorise sa position.
3.  **Options** : Clic droit sur le texte pour changer les couleurs, activer le démarrage ou quitter.
4.  **Zéro Distraction** : Elle détecte la couleur de fond pour s'intégrer et s'efface si besoin.

## 📥 Téléchargements
Téléchargez le dernier exécutable portable ici :  
👉 **[Releases](https://github.com/CordaAvlao/MiniMatrixClock/releases)**

## 🔧 Détails Techniques
*   **Langage** : Python 3.x
*   **Interface** : Tkinter (Pas de framework lourd)
*   **API** : Windows API (ctypes) pour la détection de la barre des tâches, la transparence et l'accès au registre.
*   **Portable** : Fichier EXE unique, aucune installation requise.

## 🤝 Contribuer
Les contributions sont les bienvenues !

1.  Forkez le dépôt
2.  Créez une branche de fonctionnalité (`feature/ma-fonctionnalite`)
3.  Soumettez une Pull Request

Les suggestions, améliorations et rapports de bugs sont très appréciés.

## ❤️ Soutenir le Projet
Salut ! Je suis **CordaAvlao** 👋

Je développe de petits utilitaires simples pour Windows, comme **MiniClock** et **Beepschéduler**.  
Mon travail est gratuit, mais il faut du temps pour construire et améliorer ces outils.  
Si vous souhaitez soutenir mon travail, vous pouvez faire une petite contribution ici :

👉 **[Soutenir via PayPal](https://www.paypal.com/ncp/payment/NPGMPUL9N9TFQ)**

Merci beaucoup pour votre soutien !

## 📜 Licence
Licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
