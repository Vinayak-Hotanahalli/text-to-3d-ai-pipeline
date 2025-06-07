# Import the Ollama package
import ollama

# Function to interact with LLM in a loop
def chat_with_llm():
    while True:
        prompt = input("You: ")  # Get user input
        if prompt.lower() in ['exit', 'quit']:  # Exit condition
            break

        # Send user input to LLM and get response
        response = ollama.chat(
            model='llama3',
            messages=[{'role': 'user', 'content': prompt}]
        )

        # Display the LLM's response
        print("LLM:", response['message']['content'])

# Run the chat function if file is executed
if __name__ == "__main__":
    chat_with_llm()
