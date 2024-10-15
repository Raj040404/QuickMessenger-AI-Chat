import json
import os
import re
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserMessage
from .chatbot_ai import ChatbotAI

# Initialize the chatbot instance
chatbot = ChatbotAI()

def index(request):
    """Render the chatbot index page."""
    return render(request, 'chatbot/index.html')

@csrf_exempt
def send_message(request):
    """Handle sending messages to users or the chatbot."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message_content = data.get('message', '')

            print(f"Received message: {message_content}")

            users = load_users()

            # Check for the 'send to' command in the message
            if 'send to ' in message_content:
                match = re.match(r'send to ([^.]+)\.?(.*)', message_content)
                if match:
                    recipient_name = match.group(1).strip()
                    message_text = match.group(2).strip() if match.group(2) else ""

                    # Validate the recipient name
                    if recipient_name in users:
                        save_message(message_text, recipient_name)
                        return JsonResponse({"status": "Message sent", "recipient": recipient_name, "message": message_text})
                    else:
                        return JsonResponse({"status": "Error", "message": f"'{recipient_name}' is not a valid user."})

            # Generate a response from the chatbot if it's not a 'send to' command
            response = chatbot.generate_response(message_content)
            save_ai_response(message_content, response)
            return JsonResponse({"status": "Message sent", "response": response})

        except json.JSONDecodeError:
            return JsonResponse({"status": "Error", "message": "Invalid JSON data."})

    return JsonResponse({"status": "Error", "message": "Only POST requests are allowed."})

def load_users():
    """Load the list of users from the users.json file."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, 'users.json')
    with open(json_path, 'r') as f:
        return json.load(f)

def save_message(text, recipient_name):
    """Save a message sent to a specific recipient."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, 'messages.json')

    # Load existing messages or initialize a new structure
    if os.path.exists(json_path):
        with open(json_path, 'r') as f:
            messages = json.load(f)
    else:
        messages = {}

    if recipient_name not in messages:
        messages[recipient_name] = []
    messages[recipient_name].append(text)

    # Save the updated messages to the JSON file
    with open(json_path, 'w') as f:
        json.dump(messages, f, indent=4)

def save_ai_response(question, response):
    """Save the AI's response to a question."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, 'response.json')

    # Load existing responses or initialize a new structure
    if os.path.exists(json_path):
        with open(json_path, 'r') as f:
            responses = json.load(f)
    else:
        responses = {}

    if "AI" not in responses:
        responses["AI"] = []
    responses["AI"].append({"question": question, "response": response})

    # Save the updated responses to the JSON file
    with open(json_path, 'w') as f:
        json.dump(responses, f, indent=4)

def get_sent_messages(request):
    """Retrieve and return all sent messages with recipient names."""
    if request.method == 'GET':
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        json_path = os.path.join(base_dir, 'messages.json')

        if os.path.exists(json_path):
            with open(json_path, 'r') as f:
                messages = json.load(f)
            return JsonResponse(messages, safe=False)

        return JsonResponse({"status": "Error", "message": "No sent messages found."})
    
    return JsonResponse({"status": "Error", "message": "Only GET requests are allowed."})


        
