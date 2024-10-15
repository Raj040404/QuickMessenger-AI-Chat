# QuickMessenger-AI-Chat

QuickMessenger-AI-Chat is an innovative messaging platform that combines the ease of direct messaging with the power of AI chat responses. It enables users to send messages to specified recipients and get instant AI-powered replies through a local LLaMA 3.2 model hosted on LM Studio. 

## Features

- **Direct Messaging**: Send messages to specific users by using the `send to [name]` command.
- **AI-Powered Chat**: Ask questions and receive intelligent responses from the LLaMA 3.2 model.
- **Message History**: View past AI responses and sent messages in an organized format.
- **Easy Integration**: Easily integrates with a locally hosted LLaMA 3.2 model using LM Studio.
- **Customizable**: Can be configured to meet various use cases and requirements.

## Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher
- LM Studio (installed locally) with LLaMA 3.2 model
- Virtual environment setup (recommended)
- Git (for cloning the repository)

## Getting Started

### Step 1: Clone the Repository


git clone https://github.com/raj040404/QuickMessenger-AI-Chat.git
cd QuickMessenger-AI-Chat

Step 2: Set Up a Virtual Environment
It's recommended to use a virtual environment to manage dependencies. You can set one up using the following commands:
For Windows:
python -m venv venv
venv\Scripts\activate
For macOS/Linux:
python3 -m venv venv
source venv/bin/activate

Step 3: Install Dependencies
Make sure your virtual environment is activated, then install the required dependencies:

pip install -r requirements.txt
Step 4: Set Up LM Studio with LLaMA 3.2
Download and Install LM Studio: Follow the installation instructions for LM Studio from LM Studio's official website.
Download LLaMA 3.2 Model: Open LM Studio and download the LLaMA 3.2 model.
Run LLaMA 3.2 on Local Server:
Configure the model to run on a local server.
Ensure the server is listening on localhost with port 1235. You can change the port in the code if needed.
Specify the Port in Code: Update the port in your Django views if it's different from 1235.


Step 5: Configure Django
Apply Database Migrations:


python manage.py migrate
Run the Development Server:


python manage.py runserver
Access the App: Open your web browser and navigate to http://127.0.0.1:8000/chatbot/.

Step 6: Adding Users and Viewing Sent Messages
Add users to users.json in the following format:
json
{
    "alice": "Alice Doe",
    "bob": "Bob Smith"
}
View sent messages by clicking on the "View Sent Messages" button. The app will fetch messages stored in messages.json.


Project Structure
csharp
Copy code
QuickMessenger-AI-Chat/
│
├── chatbot_project/           # Django project folder
│   ├── chatbot/               # Core app files
│   │   ├── templates/         # HTML files
│   │   ├── static/            # CSS, JS, images
│   │   ├── views.py           # Core logic
│   │   └── ...                
│   └── ...
│
├── venv/                      # Virtual environment (excluded from Git)
├── requirements.txt           # List of dependencies
├── users.json                 # Sample user data
├── messages.json              # Sent messages storage
└── README.md                  # Project documentation


Usage Example

Send a Message:
Type "send to bob. Hello, how are you?" in the chat input field and click Send.

Ask a Question:
Type "What is the capital of France?" and click Send to get an AI response.


License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Fork the repository.
Create a new branch: git checkout -b feature/your-feature-name.
Make your changes and commit: git commit -m 'Add new feature'.
Push the branch: git push origin feature/your-feature-name.
Open a Pull Request.
For any issues, please contact the project maintainer.

This README provides a comprehensive guide to setting up and running your QuickMessenger-AI-Chat project.
