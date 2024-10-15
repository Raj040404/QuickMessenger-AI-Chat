import json
import os

# Paths for the JSON files
USERS_FILE = os.path.join(os.path.dirname(__file__), 'users.json')
MESSAGES_FILE = os.path.join(os.path.dirname(__file__), 'messages.json')

def user_exists(username):
    with open(USERS_FILE, 'r') as file:
        users = json.load(file)
        return any(user['name'].lower() == username.lower() for user in users)

def save_message(message, sender, recipient):
    new_message = {
        "message": message,
        "sender": sender,
        "recipient": recipient
    }
    with open(MESSAGES_FILE, 'r+') as file:
        messages = json.load(file)
        messages.append(new_message)
        file.seek(0)
        json.dump(messages, file, indent=4)

def parse_message(input_text):
    parts = input_text.strip().split("\n\n")
    if len(parts) == 2:
        message = parts[0].strip()
        recipient = parts[1].strip()
        return message, recipient
    else:
        return input_text, None
