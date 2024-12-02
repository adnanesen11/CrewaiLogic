import panel as pn
from crew import JobChatbotCrew

# Load the CrewAI configuration
crew = JobChatbotCrew().crew()

# Initialize the Panel extension
pn.extension()

# Define the chatbot interface
chat_history = pn.widgets.TextAreaInput(name="Chat History", value="", height=300, disabled=True)
user_input = pn.widgets.TextInput(name="User Input")
submit_button = pn.widgets.Button(name="Send", button_type="primary")

# Define the callback for the chatbot interaction
def process_input(event):
    user_message = user_input.value
    if user_message.strip():
        # Simulate running the CrewAI chatbot
        inputs = {"user_message": user_message}
        try:
            response = crew.kickoff(inputs=inputs)
            chat_history.value += f"User: {user_message}\nBot: {response}\n"
        except Exception as e:
            chat_history.value += f"Error: {str(e)}\n"
    user_input.value = ""

submit_button.on_click(process_input)

# Layout the application
app = pn.Column(
    pn.pane.Markdown("# CrewAI Chatbot"),
    chat_history,
    user_input,
    submit_button,
)

# Serve the application
app.servable()
