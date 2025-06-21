import firebase_admin
from firebase_admin import credentials, db

# Load Firebase key
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://wildlife-poaching-default-rtdb.firebaseio.com'})

ref = db.reference('/test')
ref.set({'status': 'Poaching det6ected!'})

print("Firebase connected successfully!")
