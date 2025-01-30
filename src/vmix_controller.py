import requests
from config import *

class VMixController:
    def __init__(self):
        self.base_url = f"http://{VMIX_IP}:{VMIX_PORT}/api/"
        print(f"vMix Controller initialisiert mit URL: {self.base_url}")
    
    def update_title(self, text):
        try:
            params = {
                "Function": "SetText",
                "Input": VMIX_INPUT,
                "SelectedName": f"{VMIX_FIELD}.Text",
                "Value": text
            }
            print(f"Sende an vMix - URL: {self.base_url}")
            print(f"Parameter: {params}")
            
            response = requests.get(self.base_url, params=params)
            
            if response.status_code == 200:
                print(f"Erfolgreich an vMix gesendet: {text}")
                return True
            else:
                print(f"Fehler beim Senden an vMix: Status Code {response.status_code}")
                return False
                
        except Exception as e:
            print(f"Fehler bei der vMix-Verbindung: {str(e)}")
            return False
