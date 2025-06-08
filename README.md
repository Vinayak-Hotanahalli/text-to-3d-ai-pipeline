# AI Developer Challenge – Text-to-3D Model Generator
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/status-Completed-brightgreen)
![Framework](https://img.shields.io/badge/framework-Streamlit-red)
![SDK](https://img.shields.io/badge/Openfabric-SDK-purple)
![Model](https://img.shields.io/badge/model-LLM%20%7C%20Diffusion-blueviolet)
![UI](https://img.shields.io/badge/interface-Interactive%20Web-orange)
![Contributions](https://img.shields.io/badge/contributions-welcome-yellow)

Welcome to the AI Developer Challenge! This project implements a creative AI pipeline that transforms simple user prompts into immersive 3D models through a series of intelligent and modular steps. Built using Python, Openfabric SDK, and locally hosted LLMs, the goal is to provide a seamless, imaginative, and persistent user experience that brings ideas to life.

From understanding human prompts using an LLM to generating visuals with text-to-image models, and finally converting those into 3D models – this app does it all, locally, intelligently, and efficiently.

## 🎯 Vision & Mission

**Vision:**  
Build a creative AI partner that transforms simple prompts into stunning visual art and interactive 3D models, unlocking imagination at scale.

**Mission:**  
Leverage local LLMs and Openfabric apps to:  
- Understand and expand user ideas creatively  
- Generate images from text seamlessly  
- Convert images into 3D models dynamically  
- Remember user creations with persistent memory for remixing and evolution  

Empower users to bring their wildest concepts to life with privacy-first, fully local, and scalable AI pipelines.


## 📚 Table of Contents

- [Features](#features)  
- [How It Works](#how-it-works)  
- [Project Structure](#project-structure)  
- [Installation](#installation)  
- [How to Run / Deploy](#how-to-run--deploy)  
- [Openfabric Stub Usage & API Integration](#openfabric-stub-usage--api-integration)  
- [Memory & Data Management](#memory--data-management)  
- [Input / Output Samples](#input--output-samples)  
- [Technologies Used](#technologies-used)  
- [.gitignore – Recommended Exclusions](#gitignore--recommended-exclusions)  
- [References / Credits](#references--credits)  
- [Acknowledgment](#acknowledgment)  
- [Contact](#contact)  

## 🧩 Features

A robust, end-to-end AI pipeline transforming text prompts into detailed 3D models using fully local AI technologies—no external cloud dependencies.

#### 🔍 Intelligent Prompt Processing
- Leverages local LLMs (DeepSeek, LLaMA) for semantic understanding and creative prompt expansion.
- Enhances input quality for superior generation accuracy and relevance.

#### 🎨 Text-to-Image Synthesis
- Integrates Openfabric’s Text-to-Image app with dynamic schema-driven requests.
- Generates high-fidelity, context-aware visuals from enriched prompts.

#### 🌀 Image-to-3D Model Transformation
- Converts 2D images into interactive, depth-aware 3D models via Openfabric’s Image-to-3D service.
- Enables immersive visualization and spatial exploration.

#### 🧠 Contextual Memory Management
- Supports session-level context and persistent storage using SQLite or JSON.
- Enables recall, iterative refinement, and seamless user experience continuity.

#### 🛠 Modular & Scalable Architecture
- Decoupled components for easy maintenance, upgrades, and integration.
- Flexible to swap AI models or generation modules without disruption.

#### 📜 Developer-Friendly API
- Swagger UI for intuitive API testing and interaction.
- Simplifies pipeline control with clean, well-documented endpoints.

#### 💾 Secure Local Data Handling
- Local storage of all assets ensures privacy and data control.
- Efficient asset management for revisiting and evolving creations.


## 🚀 How It Works

This project implements a modular AI pipeline that transforms text prompts into 3D models using local LLMs and Openfabric apps:

1. **User Input:** Receive natural language prompts describing desired objects or scenes.
2. **Prompt Enhancement:** Utilize local LLMs (DeepSeek/LLaMA) to interpret and expand prompts for richer detail.
3. **Text-to-Image Generation:** Call Openfabric’s Text-to-Image app to create high-quality 2D visuals from enriched prompts.
4. **Image-to-3D Conversion:** Convert generated images into interactive 3D models via Openfabric’s Image-to-3D app.
5. **Memory Management:** Maintain session context and persist data locally (SQLite/JSON) for recall, iterative refinement, and seamless user experience.


### 🔄 Pipeline Flow

                       🧑‍💻 User Prompt (Text Input) 
                                     ⬇  
          🧠 Local LLM (DeepSeek / LLaMA) – Prompt Understanding & Expansion  
                                     ⬇  
                🖼️ Text-to-Image App (Openfabric) – Visual Generation  
                                     ⬇  
                 🧱 Image-to-3D App (Openfabric) – 3D Model Conversion  
                                     ⬇  
                 💾 Memory Storage – Session & Long-Term Persistence

This design ensures flexibility, scalability, and full local execution without external dependencies.

## 🏗️ Project Structure

```bash
AI-Developer-Challenge/
├── main.py                    # Entry point to the pipeline execution logic
├── test_main.py               # Test script to validate local runs
├── memory_manager.py          # Handles short-term and long-term memory storage
├── requirements.txt           # Python dependencies for the project
├── .gitignore                 # Git ignored files and folders
├── README.md                  # Project documentation (you’re reading it!)
├── memory.json                # Stores long-term memory data (prompts, outputs)
├── output/
│   ├── generated_image.png    # Example output from Text-to-Image
│   └── generated_model.obj    # Example 3D model output
├── venv/                      # Local Python virtual environment (excluded from Git)

```
Description
- **main.py:** Runs the AI pipeline from text prompt to 3D model.  
- **memory_manager.py:** Manages session and long-term data storage.  
- **output/:** Contains generated images and 3D models.  
- **requirements.txt:** Lists Python dependencies (`pip install -r requirements.txt`).  
- **.gitignore:** Prevents committing environment and temporary files.


## ⚙️ Installation Instructions
Clone the repository and set up your environment to run the project locally.

📁 1. Clone the Repository
```bash

git clone https://github.com/Vinayak-Hotanahalli/text-to-3d-ai-pipeline.git
cd text-to-3d-ai-pipeline
```

🛠️ 2. Set Up Python Environment
You have two options to manage dependencies and virtual environments:

Option A: Using pip + requirements.txt (Simple & universal)
Create and activate a Python virtual environment manually:

Windows:

```bash

python -m venv venv
venv\Scripts\activate
```
macOS/Linux:

```bash

python3 -m venv venv
source venv/bin/activate
```
Install dependencies:

```bash

pip install -r requirements.txt
```
Option B: Using Poetry (Recommended for advanced dependency & environment management)
Poetry handles virtual environments and dependencies automatically.

Install Poetry
macOS/Linux:

```bash

curl -sSL https://install.python-poetry.org | python3 -
```
Windows (PowerShell):

```bash

(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```
Or download the installer from python-poetry.org.

Install dependencies & start shell
```bash

poetry install
poetry shell
```
Note:
Poetry creates and activates its own virtual environment automatically; manual activation is not required outside poetry shell.

#### 🚀 3. Run the Application
```bash

python main.py
```
#### 🧪 4. (Optional) Run Tests
```bash

python test_main.py
```
#### 📤 Output Location
Generated files will be saved in the output/ folder:

```bash

output/
├── generated_image.png
└── generated_model.obj
```
- **Python 3.10+**  
- **Poetry (dependency management)**  
- **OpenFabric SDK**  
- **Local LLMs (DeepSeek / LLaMA)**  
- **NumPy, Pillow**

### 📜 Ground Rules

To align with the challenge requirements, this project follows strict constraints:

-  No external APIs or cloud-based AI services (e.g., no OpenAI ChatGPT, Google APIs, etc.)  
-  All AI processing runs locally using self-hosted LLMs like DeepSeek or LLaMA  
-  No plagiarism — all code, logic, and models are original or properly attributed  
-  The entire pipeline is designed for offline or self-hosted execution  
-  Persistence and memory are implemented locally without cloud storage  
-  The project must be fully functional and bug-free without external dependencies


## ▶️ How to Run / Deploy

#### 1. Local Execution

- **Streamlit UI (Recommended):**
```bash
streamlit run streamlit_app.py
```
Interactive prompt input, image + 3D preview, auto-save outputs (generated_image.png, generated_model.obj, memory.json).

CLI Pipeline:
```bash

python main.py
```
Runs full pipeline: local LLM prompt expansion → Openfabric Text-to-Image → Image-to-3D → saves outputs.

Unix Start Script:

```bash
./start.sh
```
(Linux/macOS only) Starts server locally.

2. Docker Container
```bash
docker build -t ai-dev-challenge .
docker run -p 8888:8888 ai-dev-challenge
```
 Containerized deployment, cross-platform.

3. API Access (Swagger UI)
Open browser:

```bash

http://localhost:8888/swagger-ui/#/App/post_execution
```
Send POST prompts, inspect JSON, test pipeline endpoints.

### 🚀 Pipeline Flow

Local LLM (DeepSeek/LLaMA) for prompt understanding & creative expansion

Openfabric Text-to-Image App (ID: f0997a01-d6d3-a5fe-53d8-561300318557)

Openfabric Image-to-3D App (ID: 69543f29-4d41-4afc-7f29-3d51591f11eb)

Persistent memory storage (memory.json) for context and recall

## 🔧 Openfabric Stub Usage & API Integration

Use the `Stub` from Openfabric SDK to interact with modular AI apps dynamically.

### 🧪 Example Pipeline: Prompt → Image → 3D → Save

```python
from openfabric_sdk.context import Stub
```
#### Initialize stub with App IDs for text-to-image and image-to-3D
```python
stub = Stub(app_ids=[
    "f0997a01-d6d3-a5fe-53d8-561300318557",  # Text-to-Image
    "69543f29-4d41-4afc-7f29-3d51591f11eb"   # Image-to-3D
])
```
#### Step 1: Expand Prompt (via local LLM like DeepSeek or LLaMA)
```python
expanded_prompt = expand_prompt_with_llm("A glowing dragon on a cliff at sunset")
```
#### Step 2: Generate Image from Expanded Prompt
```python
img_result = stub.call(
    "f0997a01-d6d3-a5fe-53d8-561300318557.node3.openfabric.network",
    {"prompt": expanded_prompt},
    "super-user"
)
with open("generated_image.png", "wb") as f:
    f.write(img_result["result"])
```
#### Step 3: Convert Image to 3D Model
```python
model_result = stub.call(
    "69543f29-4d41-4afc-7f29-3d51591f11eb.node3.openfabric.network",
    {"image": img_result["result"]},
    "super-user"
)
with open("generated_model.obj", "wb") as f:
    f.write(model_result["result"])
```

This snippet demonstrates how to:
- Expand a creative prompt using a local LLM
- Call Openfabric's **Text-to-Image** and **Image-to-3D** apps using `stub.call(...)`
- Save the generated outputs (`.png`, `.obj`) locally for persistent reuse

## 🧠 Memory & Data Management

The app supports **context-aware generation** with:

#### 🔄 Short-Term Memory (Runtime)
- Keeps data (prompt, image, model) during a session
- Enables contextual linking between steps

#### 💾 Long-Term Memory (Persistent)
- Stored in `memory.json` for reuse/remix
- Format includes:
  - Original + expanded prompt
  - Paths to `generated_image.png` and `generated_model.obj`
  - Timestamp for traceability

```json
{
  "prompt": "Futuristic samurai in the rain",
  "expanded_prompt": "A high-tech samurai standing under neon rain in Tokyo...",
  "image_file": "generated_image.png",
  "model_file": "generated_model.obj",
  "timestamp": "2025-06-07 12:30:45"
}
```

All files are saved in the project root for easy access.


## 📥 Input / Output Samples

#### 🔡 Sample Prompt
```json
{
  "prompt": "Create a glowing spaceship flying over a desert planet at night"
}
```

### 📤 Expanded Output
> "A sleek, glowing spacecraft with pulsating lights flying above a vast, sandy desert under a star-filled night sky — illuminated by twin moons."

#### ✅ Sample API Response
```json
{
  "message": "3D model and image generated successfully",
  "image_file": "generated_image.png",
  "model_file": "generated_model.obj"
}
```

>  Use this output for visualization, AR/VR integration, or asset pipelines.


## 🧰 Technologies Used

| **Category**           | **Technology / Tool**                                   | **Purpose / Description**                                                |
|------------------------|---------------------------------------------------------|---------------------------------------------------------------------------|
| Language               | Python 3.10+                                            | Core programming language                                                 |
| Frontend UI            | [Streamlit](https://streamlit.io/)                      | Web interface for prompt input and visualizing outputs                    |
| Local LLM              | [DeepSeek](https://github.com/deepseek-ai) / [LLaMA](https://ai.meta.com/llama/) | Expands and enhances user prompts locally                                 |
| Text-to-Image Engine   | Openfabric SDK App<br>App ID: `f0997a01-d6d3-a5fe-53d8-561300318557` | Generates images from enhanced prompts                                   |
| Image-to-3D Converter  | Openfabric SDK App<br>App ID: `69543f29-4d41-4afc-7f29-3d51591f11eb` | Converts image to 3D `.obj` model                                        |
| API Testing            | Swagger UI<br>`http://localhost:8888/swagger-ui`        | REST API testing and manual interaction                                   |
| Data Persistence       | `memory.json` (Flat file storage)                       | Stores prompt history, output file paths, and timestamps                  |
| Output Files           | `generated_image.png`, `generated_model.obj`            | AI-generated outputs from pipeline                                        |
| Containerization (Optional) | Docker                                           | For isolated deployment and running as an API service                    |
| Dependency Management  | `pip`, `requirements.txt`                               | Installing and managing Python packages                                  |

## 📂 .gitignore – Recommended Exclusions

Exclude auto-generated, environment, and output files to keep repo clean and secure:

| __pycache__/ | *.pyc | venv/ | memory.json | *.png | *.obj |
|--------------|--------|-------|--------------|--------|--------|

- `__pycache__/`, `*.pyc`: Python bytecode cache files  
- `venv/`: Local Python virtual environment  
- `memory.json`: Persistent local AI prompt & output storage  
- `*.png`, `*.obj`: AI-generated images & 3D model assets 

## 📌 Final Notes

-  Fully local pipeline — no cloud APIs used (meets AI Challenge constraints)
-  Uses Openfabric SDK with valid app IDs for Text-to-Image and Image-to-3D
-  Local LLMs (DeepSeek / LLaMA) used for prompt understanding and expansion
-  Persistent storage via `memory.json` for recall and remix
-  Clean project structure with `.gitignore`, `requirements.txt`, and `README.md`
-  Runs via CLI (`main.py`), Streamlit (`streamlit_app.py`), or Docker
-  Tested locally using `test_main.py`

 ## 📎 References / Credits

- [DeepSeek LLM](https://github.com/deepseek-ai)  
- [LLaMA](https://ai.meta.com/llama/)  
- [Openfabric SDK](https://docs.openfabric.ai/)  
- [Streamlit](https://streamlit.io/)

## 🙏 Acknowledgment

This project was developed as part of the **Openfabric AI Developer Challenge**.

I would like to thank **Openfabric** for the opportunity to contribute and showcase my skills through this challenge. Special thanks to the developers of [DeepSeek LLM](https://github.com/deepseek-ai), [LLaMA](https://ai.meta.com/llama/), and the creators of [Openfabric SDK](https://docs.openfabric.ai/) and [Streamlit](https://streamlit.io/) for enabling such powerful tools.


## 📞 Contact

- **Name:** Vinayak Girish Hotanahalli  
- **Email:** [vinayakhotanahalli72@gmail.com](mailto:vinayakhotanahalli72@gmail.com)  
- **LinkedIn:** [linkedin.com/in/vinayak-hotanahalli-2775b929b](https://www.linkedin.com/in/vinayak-hotanahalli-2775b929b)  
- **GitHub:** [github.com/Vinayak-Hotanahalli](https://github.com/Vinayak-Hotanahalli)

