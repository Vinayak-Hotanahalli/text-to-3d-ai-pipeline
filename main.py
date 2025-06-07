import base64
import logging
import ollama
from memory import save_memory  # Your function to save memory data

# Setup logging format and level
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

# Input class to hold user input
class Input:
    def __init__(self, text):
        self.text = text

# Output class to hold output text
class Output:
    def __init__(self):
        self.text = []

# Dummy context to simulate API calls and configurations
class DummyContext:
    def __init__(self):
        self.configurations = {
            'super-user': DummyConfig()
        }

    # Simulate API call to different apps
    def call(self, app_id, payload):
        if app_id == 't2i-app':  # Text-to-Image app
            logging.info("Simulating Text-to-Image response...")
            with open('placeholder.png', 'rb') as f:
                return {'result': base64.b64encode(f.read()).decode()}
        elif app_id == 'i2d-app':  # Image-to-3D app
            logging.info("Simulating Image-to-3D response...")
            with open('placeholder.obj', 'rb') as f:
                return {'result': base64.b64encode(f.read()).decode()}
        else:
            raise ValueError("Unknown app_id: " + app_id)

# Dummy configuration with app IDs
class DummyConfig:
    def __init__(self):
        self.app_ids = ['t2i-app', 'i2d-app']

# Called when the app is created
def on_create(ctx):
    logging.info("App initialized successfully.")

# Main function to process message
def on_message(ctx, input: Input) -> Output:
    output = Output()

    try:
        if not input.text or len(input.text) == 0:
            raise ValueError("No prompt text provided")

        prompt = input.text[0]
        user_config = ctx.configurations.get('super-user', None)
        app_ids = user_config.app_ids if user_config else []

        if len(app_ids) < 2:
            raise ValueError("Insufficient app IDs in configuration")

        t2i_app_id = app_ids[0]
        i2d_app_id = app_ids[1]

        # Expand prompt using Ollama's Llama3 model
        logging.info("Expanding prompt using Llama3...")
        response = ollama.chat(
            model='llama3',
            messages=[{
                'role': 'user',
                'content': f"Expand this into a vivid visual scene: {prompt}"
            }]
        )
        expanded_prompt = response['message']['content']
        logging.info(f"Expanded prompt: {expanded_prompt}")

        # Call Text-to-Image app simulation
        logging.info("Calling Text-to-Image application...")
        t2i_response = ctx.call(t2i_app_id, {'prompt': expanded_prompt})
        image_data = t2i_response.get('result')
        if not image_data:
            raise ValueError("No image data returned from Text-to-Image")

        image_bytes = base64.b64decode(image_data)
        with open('generated_image.png', 'wb') as img_file:
            img_file.write(image_bytes)
        logging.info("Image saved as 'generated_image.png'")

        # Call Image-to-3D app simulation
        logging.info("Calling Image-to-3D application...")
        i2d_response = ctx.call(i2d_app_id, {'image': image_bytes})
        model_3d = i2d_response.get('result')
        if not model_3d:
            raise ValueError("No 3D model data returned from Image-to-3D")

        model_bytes = base64.b64decode(model_3d)
        with open('generated_model.obj', 'wb') as model_file:
            model_file.write(model_bytes)
        logging.info("3D model saved as 'generated_model.obj'")

        # Save prompt details to memory (your implementation)
        save_memory(
            prompt=prompt,
            expanded_prompt=expanded_prompt,
            image_file="generated_image.png",
            model_file="generated_model.obj"
        )
        logging.info("Memory saved to memory.json")

        output.text.append(f"3D model generated successfully for: '{prompt}'")

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        output.text.append(f"Failed: {str(e)}")

    return output
