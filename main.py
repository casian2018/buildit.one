import firebase_admin
from firebase_admin import credentials, auth, firestore
import time

# Initialize Firebase Admin SDK
cred = credentials.Certificate('./cred.json')
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

def get_all_users():
    """Fetch all users from Firebase Authentication"""
    all_users = []
    page = auth.list_users()
    while page:
        for user in page.users:
            all_users.append(user)
        page = page.get_next_page()
    return all_users

def update_user_docs(users):
    """Update Firestore documents with user information"""
    for user in users:
        user_uid = user.uid
        user_email = user.email
        # Create or update document in Firestore
        doc_ref = db.collection('users').document(user_uid)
        # Check if the document already exists
        if not doc_ref.get().exists:
            doc_ref.set({
                'uid': user_uid,
                'email': user_email,
                'first_name': '',
                'last_name': '',
                'phone_no': ''
            })
        else:
            print(f"Document for user {user_uid} already exists. Skipping update.")

def main():
    while True:
        try:
            users = get_all_users()
            update_user_docs(users)
        except Exception as e:
            print(f"An error occurred: {e}")
        # Wait for 1 second
        time.sleep(1)

if __name__ == "__main__":
    main()
