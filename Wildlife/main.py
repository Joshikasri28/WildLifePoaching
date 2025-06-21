import cv2
from ultralytics import YOLO
import firebase_admin
from firebase_admin import credentials, db
from twilio.rest import Client
from gtts import gTTS
import os
import pygame

# Load Firebase key
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://wildlife-poaching-default-rtdb.firebaseio.com'})

# Twilio credentials
account_sid = 'ACf57012fefcc2d9d8e24db3e45aab0efe'
auth_token = '7a828db808b7fbec4d7318a6e93be363'
client = Client(account_sid, auth_token)

# Load YOLO model
model = YOLO('yolov8n.pt')

# Open camera
cap = cv2.VideoCapture(0)

# ✅ Function to play voice alert through a walkie-talkie (or speaker)
def play_voice_alert(detected_object):
    try:
        # Convert text to speech
        text = f"{detected_object} detected in the wildlife area. Immediate action required."
        tts = gTTS(text=text, lang='en')
        tts.save("alert.mp3")

        # Initialize pygame mixer
        pygame.mixer.init()
        pygame.mixer.music.load("alert.mp3")
        pygame.mixer.music.play()

        # Wait until the audio finishes playing
        while pygame.mixer.music.get_busy():
            continue

        print(f"🔊 Voice alert sent for: {detected_object}")

        # Remove the audio file after playing
        os.remove("alert.mp3")

    except Exception as e:
        print(f"❌ Error sending voice alert: {e}")

# ✅ Function to send alert
def send_alert(detected_object):
    try:
        # Firebxrase update
        ref = db.reference('/alerts')
        ref.push({'status': f'{detected_object} detected!'})

        # Send SMS via Twilio (Optional, if needed)
        message = client.messages.create(
            body=f"{detected_object} detected in the wildlife area!",
            from_='+17756406408',
            to='+918778244247'
        )
        print(f"✅ ALERT: {detected_object} detected! SMS sent with SID: {message.sid}")

        # Trigger voice alert
        play_voice_alert(detected_object)

    except Exception as e:
        print(f"❌ Error sending alert: {e}")

# Debug Twilio number status
try:
    from_number_info = client.lookups.v2.phone_numbers('+17756406408').fetch()
    print(f"From Number Status: {from_number_info}")
    to_number_info = client.lookups.v2.phone_numbers('+918778244247').fetch()
    print(f"To Number Status: {to_number_info}")
except Exception as e:
    print(f"❌ Error fetching phone number details: {e}")

# ✅ Start Detection Loop
while True:
    ret, frame = cap.read()
    if ret:
        # Object detection
        results = model(frame)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                class_id = int(box.cls[0])
                confidence = float(box.conf[0])
                if confidence > 0.5:
                    label = model.names[class_id]
                    print(f"Detected: {label} with confidence: {confidence}")
                    if label in ['person', 'gun', 'fire', 'knife']:
                        print(f"🚨 Sending alert for: {label}")
                        send_alert(label)
                        
        cv2.imshow('Wildlife Poaching Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
