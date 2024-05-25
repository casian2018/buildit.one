import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials, firestore
import json

# Initialize Firestore
cred = credentials.Certificate("cred.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Define URLs and categories
urls = {
    "tailwindflex": "https://tailwindflex.com/search?q=",
    "tailwindcomponents": "https://tailwindcomponents.com/search?query=",
}
categories = ["Navbar", "Hero", "Contact", "Form", "Table", "Footer", "About"]

# Function to scrape data from a URL
def scrape_data(url, category):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    components = []

    for option in soup.find_all("option", value=category):
        component = {
            "title": option.text,
            "imageURL": "",  # Placeholder, replace with actual image URL if available
            "url": url + option.get('value'),
            "category": category
        }
        components.append(component)
    return components

# Function to create and save a Vue component file
def create_vue_file(components, category):
    vue_template = """
<template>
{}
</template>
"""
    vue_content = "\n".join([
        f'<option value="{component["title"]}">{component["title"]}</option>'
        for component in components
    ])
    vue_file_content = vue_template.format(vue_content)
    vue_file_path = f"{category}.vue"
    with open(vue_file_path, "w") as file:
        file.write(vue_file_content)
    return vue_file_path

# Function to upload a file to the server
def upload_file(file_path):
    upload_url = "https://data.codeko.ro/upload"
    files = {'file': open(file_path, 'rb')}
    response = requests.post(upload_url, files=files)
    if response.status_code == 200:
        print("File uploaded successfully.")
        return response.json().get('url')
    else:
        print(f"Failed to upload file. Status code: {response.status_code}")
        print(f"Response: {response.text}")
        return None

# Function to store data in Firestore and post to buildit.ctp.one/add
def store_and_post_data(components, upload_link):
    post_url = "https://buildit.ctp.one/add"
    user_id = "hrMqtsafFsP48sMfx50ISYSWu4r1"
    headers = {'Content-Type': 'application/json'}

    for component in components:
        component['url'] = upload_link
        db.collection('components').add(component)
        
        payload = {
            "userID": user_id,
            "title": component['title'],
            "imageURL": component['imageURL'],
            "url": component['url'],
            "category": component['category']
        }
        response = requests.post(post_url, json=payload, headers=headers)
        if response.status_code == 200:
            print(f"Component {component['title']} posted successfully.")
        else:
            print(f"Failed to post component {component['title']}. Status code: {response.status_code}")
            print(f"Response: {response.text}")

# Main script
for category in categories:
    all_components = []
    for site_name, site_url in urls.items():
        components = scrape_data(site_url, category)
        all_components.extend(components)
    
    if all_components:
        vue_file_path = create_vue_file(all_components, category)
        upload_link = upload_file(vue_file_path)
        
        if upload_link:
            store_and_post_data(all_components, upload_link)
        else:
            print(f"Failed to upload and process the {category} components.")
    else:
        print(f"No components found for the {category} category.")

print("Script completed.")
