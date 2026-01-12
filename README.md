# Mini Matrix Clock 🕰️

![License](https://img.shields.io/github/license/CordaAvlao/MiniMatrixClock)
![Version](https://img.shields.io/github/v/release/CordaAvlao/MiniMatrixClock)
![Platform](https://img.shields.io/badge/platform-Windows-blue)

**English** | [Français](#version-française-)

A minimalist, always-on-top digital clock for Windows with a "Matrix" aesthetic.  
This V2.2/V6.1 edition is re-engineered for stability, smart transparency, and zero distraction.

---

## 🚀 Key Features

### 🎨 Visuals & Customization
*   **Always on Top**: Does what it says. Stays visible over all windows.
*   **Theming**: Colors present (Matrix Green, Cyber Blue, Red Alert, Amber, White) or **Pick Any Color**.
*   **Fonts**: Switch between Digital, Console, Modern, Bold, or Terminal styles.
*   **Zoom/Scale**: Resize the clock from Tiny (50%) to Huge (150%). The frame adjusts automatically.

### 🧠 Smart Logic (New!)
*   **Auto-Transparency**:
    *   **Solid Mode**: Blends with your taskbar.
    *   **Transparent Mode**: Fades to invisiblity when a FULLSCREEN app (Game, Movie) is active.
    *   **Smart Detection**: Determines if the active window is actually fullscreen logic or just the "Desktop". Clicking the wallpaper **will not** trigger transparency.
*   **Flicker-Free Background**: Continuously monitors the background color to match the taskbar seamlessly without flickering.
*   **Opaque Safety**: Detects dark taskbars and forces a solid black background to prevent accidental "ghosting".

### 🛠️ Robustness
*   **Run on Startup (Fixed)**: Uses a dedicated Registry Key (`MiniClock_Auto`) to bypass Task Manager "Disabled" states on stripped-down Windows versions (AtlasOS, ReviOS).
*   **Portable**: Single `.exe` file. No install. Settings saved in `config.json`.

---

## 📦 Installation
1.  Download the latest `MiniClock.exe` from [Releases](https://github.com/CordaAvlao/MiniMatrixClock/releases).
2.  Place it anywhere (e.g., specific folder or Desktop).
3.  Run it.

---

## 🖱️ Controls
| Action | Effect |
| :--- | :--- |
| **Drag** | Move the clock anywhere. Position is saved. |
| **Right-Click** | Open Context Menu (Options, Colors, Fonts, Exit). |
| **Snooze** | Hides the clock for 10 minutes. |

---

## 🔧 Technical Requirements
*   **OS**: Windows 10 / 11
*   **Runtime**: None (Portable EXE) or Python 3.x if running from source.
*   **Libraries**: `tkinter` (Standard), `Pillow` (Screenshot), `ctypes` (WinAPI).

---

## 🤝 Support
If you enjoy this small utility, you can support its maintenance:

👉 **[Support via PayPal](https://www.paypal.com/ncp/payment/NPGMPUL9N9TFQ)**

Contributions and Pull Requests are welcome!

---
---

# Version Française 🇫🇷

Une horloge numérique minimaliste "toujours visible" pour Windows avec une esthétique "Matrix".  
Cette version V2.2/V6.1 a été retravaillée pour la stabilité, la transparence intelligente et zéro distraction.

---

## 🚀 Fonctionnalités Clés

### 🎨 Visuel & Personnalisation
*   **Toujours Visible** : Reste au-dessus de toutes les fenêtres.
*   **Thèmes** : Couleurs prédéfinies (Vert Matrix, Bleu Cyber, Rouge Alerte, Ambre, Blanc) ou **Couleur Personnalisée**.
*   **Polices** : Choisissez entre Digital, Console, Moderne, Gras ou Terminal.
*   **Zoom/Échelle** : Redimensionnez l'horloge de Minuscule (50%) à Énorme (150%). Le cadre s'adapte automatiquement.

### 🧠 Logique Intelligente (Nouveau !)
*   **Transparence Auto** :
    *   **Mode Solide** : Se fond avec votre barre des tâches.
    *   **Mode Transparent** : Devient invisible si une application PLEIN ÉCRAN (Jeu, Film) est active.
    *   **Détection Intelligente** : Distingue un vrai plein écran du simple "Bureau". Cliquer sur le fond d'écran **ne déclenchera pas** la transparence.
*   **Fond Anti-Scintillement** : Surveille en continu la couleur d'arrière-plan pour s'adapter sans clignoter.
*   **Sécurité Opacité** : Détecte les barres des tâches sombres et force un fond noir opaque pour éviter l'effet "fantôme".

### 🛠️ Robustesse
*   **Démarrage Auto (Réparé)** : Utilise une clé de Registre dédiée (`MiniClock_Auto`) pour contourner les blocages du Gestionnaire des Tâches sur les Windows allégés (AtlasOS, ReviOS).
*   **Portable** : Fichier `.exe` unique. Pas d'installation. Paramètres sauvegardés dans `config.json`.

---

## 📦 Installation
1.  Téléchargez le dernier `MiniClock.exe` depuis les [Releases](https://github.com/CordaAvlao/MiniMatrixClock/releases).
2.  Placez-le où vous voulez.
3.  Lancez-le.

---

## 🖱️ Contrôles
| Action | Effet |
| :--- | :--- |
| **Glisser** | Déplace l'horloge. La position est sauvegardée. |
| **Clic-Droit** | Ouvre le Menu (Options, Couleurs, Polices, Quitter). |
| **Snooze** | Masque l'horloge pour 10 minutes. |

---

## 🔧 Détails Techniques
*   **OS** : Windows 10 / 11
*   **Exécution** : Aucune (EXE Portable) ou Python 3.x si lancé depuis les sources.
*   **Bibliothèques** : `tkinter`, `Pillow`, `ctypes`.

---

## 🤝 Soutien
Si cet outil vous est utile, vous pouvez soutenir sa maintenance :

👉 **[Soutenir via PayPal](https://www.paypal.com/ncp/payment/NPGMPUL9N9TFQ)**

Les contributions et Pull Requests sont les bienvenues !
