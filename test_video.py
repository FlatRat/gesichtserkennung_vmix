import cv2

def list_video_devices():
    available_devices = []
    for i in range(10):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                print(f"Gerät {i}: Erfolgreich geöffnet")
                # Zeige das Bild für 3 Sekunden
                cv2.imshow(f'Test Device {i}', frame)
                cv2.waitKey(3000)
                cv2.destroyWindow(f'Test Device {i}')
            cap.release()
            available_devices.append(i)
    return available_devices

if __name__ == "__main__":
    print("Suche nach verfügbaren Videoeingängen...")
    devices = list_video_devices()
    print(f"Gefundene Videoeingänge: {devices}")
