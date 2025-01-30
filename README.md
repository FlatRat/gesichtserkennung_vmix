# Gesichtserkennung mit vMix-Integration

Dieses Projekt ermöglicht die automatische Erkennung von Personen via Webcam und die Steuerung von Bauchbinden (Lower Thirds) in vMix. Erkannte Personen können per Tastendruck in die vMix-Bauchbinde übernommen werden.

## Funktionen

- Echtzeit-Gesichtserkennung über Webcam
- Automatische Personenerkennung basierend auf Referenzbildern
- Integration mit vMix über Web API
- Steuerung der Bauchbinden-Übernahme per Leertaste
- Visuelles Feedback über erkannte Personen
- Unterstützung mehrerer Referenzbilder pro Person

## Voraussetzungen

### Software
- Python 3.10 oder höher
- vMix (getestet mit Version 25)
- Visual Studio Code (empfohlen) oder ein anderer Code-Editor

### Python-Pakete

pip install deepface
pip install opencv-python
pip install tensorflow
pip install numpy
pip install requests
pip install pynput
pip install tf-keras


## Installation

1. Repository klonen:

git clone [repository-url]
cd Gesichtserkennung_vMix

2. Virtuelle Umgebung erstellen und aktivieren:

Windows

python -m venv venv
venv\Scripts\activate

macOS/Linux

python3 -m venv venv
source venv/bin/activate

3. Abhängigkeiten installieren:

pip install -r requirements.txt

## Projektstruktur

Gesichtserkennung_vMix/
├── src/
│ ├── main.py
│ ├── face_detector.py
│ ├── vmix_controller.py
│ └── config.py
├── data/
│ └── known_faces/
│ ├── Person1/
│ │ ├── bild1.jpg
│ │ └── bild2.jpg
│ └── Person2/
│ └── bild1.jpg
└── requirements.txt


## Konfiguration

1. **Referenzbilder hinzufügen**
   - Erstelle für jede Person einen Ordner unter `data/known_faces/`
   - Der Ordnername wird als Personenname verwendet
   - Füge mehrere Bilder der Person in ihren Ordner ein

2. **vMix einrichten**
   - Erstelle eine Bauchbinde in vMix
   - Benenne das Textfeld als "Name"
   - Notiere die Input-Nummer der Bauchbinde

3. **Config anpassen**
   - Öffne `src/config.py`
   - Passe die vMix IP-Adresse an
   - Setze die korrekte Input-Nummer
   - Passe ggf. weitere Parameter an

## Verwendung

1. Starte vMix und richte eine Bauchbinde ein

2. Starte das Programm:

python src/main.py


3. Bedienung:
   - LEERTASTE: Erkannte Person in Bauchbinde übernehmen
   - Q: Programm beenden

## Fehlerbehebung

- **Kamera wird nicht erkannt**: Überprüfe die Kamera-ID in config.py
- **vMix-Verbindung fehlgeschlagen**: Überprüfe IP-Adresse und Port
- **Keine Erkennung**: Stelle sicher, dass die Referenzbilder gut ausgeleuchtet sind

## Technische Details

- Verwendet DeepFace für die Gesichtserkennung
- Kommuniziert mit vMix über die Web API
- Unterstützt verschiedene Kamera-Backends (DirectShow, MSMF)
- Optimiert für Performance durch Frame-Skipping

## Lizenz

[Ihre gewählte Lizenz]

## Autor

Lucas Alias FlatRat
