# main.py
from pynput import keyboard
import cv2
from face_detector import FaceDetector
from vmix_controller import VMixController
from config import *
import time

class GesichtserkennungController:
    def __init__(self):
        self.trigger_active = False
        self.current_name = None
        self.last_detected_name = None
        self.vmix = VMixController()
        
    def set_detected_name(self, name):
        if name:  # Nur speichern wenn ein Name erkannt wurde
            self.last_detected_name = name
            self.current_name = name
            print(f"Aktuell erkannte Person: {self.current_name}")
        
    def on_press(self, key):
        try:
            if key == keyboard.Key.space:
                if self.last_detected_name:
                    print(f"\nLEERTASTE GEDRÜCKT - Name '{self.last_detected_name}' wird gesendet")
                    success = self.vmix.update_title(self.last_detected_name)
                    if success:
                        print(f"Name erfolgreich an vMix gesendet: {self.last_detected_name}")
                    else:
                        print("Fehler beim Senden an vMix")
                else:
                    print("\nLEERTASTE GEDRÜCKT - Keine Person erkannt")
        except AttributeError:
            pass

    def on_release(self, key):
        if key == keyboard.Key.space:
            self.trigger_active = False
            print("Leertaste losgelassen - Warte auf nächsten Trigger")

def main():
    print("\n=== Gesichtserkennung mit Trigger ===")
    print("STEUERUNG:")
    print("- LEERTASTE: Person in Bauchbinde übernehmen")
    print("- Q: Programm beenden")
    
    controller = GesichtserkennungController()
    listener = keyboard.Listener(
        on_press=controller.on_press,
        on_release=controller.on_release)
    listener.start()
    
    # Verbesserte Kamera-Initialisierung
    cap = None
    for camera_id in range(3):  # Test Kamera 0-2
        print(f"Versuche Kamera {camera_id} zu öffnen...")
        cap = cv2.VideoCapture(camera_id, cv2.CAP_DSHOW)  # DirectShow Backend
        if cap.isOpened():
            # Setze Kamera-Properties
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
            cap.set(cv2.CAP_PROP_FPS, 30)
            print(f"Kamera {camera_id} erfolgreich geöffnet!")
            break
        cap.release()
    
    if not cap or not cap.isOpened():
        print("FEHLER: Keine Kamera gefunden!")
        return
    
    detector = FaceDetector(KNOWN_FACES_DIR)
    last_detection_time = 0
    frame_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Fehler beim Lesen des Kamerabildes")
            time.sleep(0.1)  # Kurze Pause bei Fehler
            continue
        
        frame_count += 1
        frame = cv2.flip(frame, 1)  # Horizontale Spiegelung
        
        # Verarbeite nur jeden 3. Frame für bessere Performance
        if frame_count % 3 == 0:
            current_time = time.time()
            if current_time - last_detection_time > 0.5:
                name = detector.identify_face(frame)
                if name:
                    controller.set_detected_name(name)
                last_detection_time = current_time
        
        # Status im Bild anzeigen
        if controller.last_detected_name:
            status = "BEREIT - LEERTASTE drücken" if not controller.trigger_active else "AKTIV"
            cv2.putText(frame, f"Erkannt: {controller.last_detected_name}", (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, status, (10, 70), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, 
                       (0, 255, 0) if controller.trigger_active else (0, 255, 255), 2)
        else:
            cv2.putText(frame, "Keine Person erkannt", (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        # FPS-Anzeige
        cv2.putText(frame, f"Frame: {frame_count}", (10, frame.shape[0] - 10),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        cv2.namedWindow('Gesichtserkennung', cv2.WINDOW_NORMAL)
        cv2.imshow('Gesichtserkennung', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("\nProgramm wird beendet...")
            break
    
    cap.release()
    cv2.destroyAllWindows()
    listener.stop()

if __name__ == "__main__":
    main()
