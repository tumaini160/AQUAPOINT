import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('aquapoint-425407-firebase-adminsdk-cn1zh-50c9a9fdec.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://aquapoint-425407-default-rtdb.firebaseio.com'
})