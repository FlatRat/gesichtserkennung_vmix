import requests

def test_connection():
    url = "http://192.168.178.23:8088/api/"
    params = {
        "Function": "SetText",
        "Input": "1",
        "SelectedName": "Name.Text",
        "Value": "Test"
    }
    print(f"Versuche Verbindung zu: {url}")
    print(f"Parameter: {params}")
    
    try:
        response = requests.get(url, params=params)
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        print("Verbindungsfehler: vMix nicht erreichbar")
    except Exception as e:
        print(f"Fehler: {str(e)}")
    return False

# Test ausführen
result = test_connection()
print(f"Test erfolgreich: {result}")
