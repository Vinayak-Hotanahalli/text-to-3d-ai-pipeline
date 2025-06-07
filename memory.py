import json
from datetime import datetime

def save_memory(prompt, expanded_prompt, image_file, model_file):
    memory_data = {
        "prompt": prompt,
        "expanded_prompt": expanded_prompt,
        "image_file": image_file,
        "model_file": model_file,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        with open("memory.json", "r") as f:
            memories = json.load(f)
    except FileNotFoundError:
        memories = []

    memories.append(memory_data)

    with open("memory.json", "w") as f:
        json.dump(memories, f, indent=4)
