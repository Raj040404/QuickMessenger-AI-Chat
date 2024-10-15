from openai import OpenAI

class ChatbotAI:
    def __init__(self):
        # Connect to the locally hosted LLaMA 3.2 model server via LM Studio
        self.client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

    def generate_response(self, user_message):
        try:
            # Use the client to send a chat completion request to the local server
            response = self.client.chat.completions.create(
                model="local_model",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.5,
            )

            # Extract and return the response content
            return response.choices[0].message.content

        except Exception as e:
            print(f"Error generating response: {e}")
            return "I'm sorry, I am currently unable to process your request."
