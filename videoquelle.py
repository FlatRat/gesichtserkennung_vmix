import cv2

def play_video_loop():
    # Öffne das Video (0 für Webcam oder Dateipfad für Video)
    cap = cv2.VideoCapture(1)
    
    # Prüfe ob Video/Kamera erfolgreich geöffnet wurde
    if not cap.isOpened():
        print("Fehler beim Öffnen des Videos")
        return

    while True:
        # Frame für Frame lesen
        ret, frame = cap.read()
        
        # Wenn Frame erfolgreich gelesen wurde
        if ret:
            # Frame anzeigen
            cv2.imshow('Video', frame)
            
            # Bei Video-Datei: Zurück zum Start springen wenn Ende erreicht
            if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            
            # Warte 25ms zwischen den Frames
            # Beende wenn 'q' gedrückt wird
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    # Aufräumen
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    play_video_loop()
