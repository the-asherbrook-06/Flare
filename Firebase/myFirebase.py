import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime
from typing import Optional, Dict

def init(path: str) -> firestore.Client:
    cred = credentials.Certificate(path)
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db

def add_blog(db: firestore.Client, title: str, creator_name: str, description: str, content: str, creation_date: datetime, topics: list):
    blog_data = {
        'title': title,
        'creator_name': creator_name,
        'description': description,
        'content': content,
        'creation_date': creation_date,
        'topics': topics
    }
    try:
        db.collection('blogs').add(blog_data)
        print("Blog added successfully.")
    except Exception as e:
        print(f"Error adding blog: {e}")

def get_blog(db: firestore.Client, blog_id: str) -> Optional[Dict]:
    try:
        doc_ref = db.collection('blogs').document(blog_id)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            print("Blog not found.")
            return None
    except Exception as e:
        print(f"Error retrieving blog: {e}")
        return None

def update_blog(db: firestore.Client, blog_id: str, updates: Dict):
    try:
        db.collection('blogs').document(blog_id).update(updates)
        print("Blog updated successfully.")
    except Exception as e:
        print(f"Error updating blog: {e}")

def delete_blog(db: firestore.Client, blog_id: str):
    try:
        db.collection('blogs').document(blog_id).delete()
        print("Blog deleted successfully.")
    except Exception as e:
        print(f"Error deleting blog: {e}")
