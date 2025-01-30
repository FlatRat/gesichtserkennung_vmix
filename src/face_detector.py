from deepface import DeepFace
import cv2
import os
import numpy as np

class FaceDetector:
    def __init__(self, known_faces_dir):
        self.known_faces_dir = known_faces_dir
        self.known_faces = {}
        self._load_known_faces()
        
    def _load_known_faces(self):
        print(f"Suche nach Referenzbildern in: {self.known_faces_dir}")
        
        for person_dir in os.listdir(self.known_faces_dir):
            person_path = os.path.join(self.known_faces_dir, person_dir)
            
            if not os.path.isdir(person_path):
                continue
                
            print(f"Lade Referenzbilder für Person: {person_dir}")
            self.known_faces[person_dir] = []
            
            for img_file in os.listdir(person_path):
                if img_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    img_path = os.path.join(person_path, img_file)
                    try:
                        embedding = DeepFace.represent(img_path, enforce_detection=False, 
                                                     detector_backend="retinaface")[0]["embedding"]
                        self.known_faces[person_dir].append(embedding)
                        print(f"  - Erfolgreich geladen: {img_file}")
                    except Exception as e:
                        print(f"  - Fehler beim Laden von {img_file}: {str(e)}")
            
            print(f"Geladene Bilder für {person_dir}: {len(self.known_faces[person_dir])}")
        
        print(f"Insgesamt geladene Personen: {len(self.known_faces)}")
    
    def identify_face(self, frame):
        if not self.known_faces:
            return None
            
        try:
            current_embedding = DeepFace.represent(frame, 
                                                 enforce_detection=False,
                                                 detector_backend="retinaface")[0]["embedding"]
            
            best_matches = []
            for person_name, embeddings in self.known_faces.items():
                person_distances = []
                for ref_embedding in embeddings:
                    distance = np.linalg.norm(np.array(current_embedding) - np.array(ref_embedding))
                    person_distances.append(distance)
                
                best_distance = min(person_distances)
                best_matches.append((person_name, best_distance))
            
            if best_matches:
                best_match = min(best_matches, key=lambda x: x[1])
                print(f"Beste Übereinstimmung: {best_match[0]} (Distanz: {best_match[1]:.3f})")
                
                if best_match[1] < 1.2:  # Erhöhter Schwellenwert für realistischere Erkennung
                    detected_name = best_match[0]
                    print(f"Person erkannt: {detected_name}")
                    return detected_name
                else:
                    print(f"Distanz zu hoch ({best_match[1]:.3f}), keine sichere Erkennung")
            return None
                
        except Exception as e:
            print(f"Fehler bei der Gesichtserkennung: {str(e)}")
            return None
