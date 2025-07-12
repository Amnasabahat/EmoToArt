#  EmotoArt🎨 - Multi-Agent Creative Assistant

> Where Emotions Become Masterpieces  
> Powered by multi-agent AI, EmotoArt transforms your *feelings* into *stunning, AI-generated artwork*.

---

## Features

- 🎭 **Emotion-Driven Art** — Generate prompts based on your current mood  
- 🌟 **Style-Adaptive Artwork** — Choose from Anime, Watercolor, Cyberpunk, and more  
- 🎨 **Personalized Color Palettes** — Warm, Cool, Vibrant, and others  
- ✨ **Real-Time Refinement** — Instantly refine the AI's creations  
- 📥 **Gallery & Download** — View and save your favorite artworks  

---

## Powered by Multi-Agent Architecture

EmotoArt uses a modular **Multi-Agent System**, designed with the GenAI AgentOS protocol in mind:

- 🧭 **Planner Agent** — Understands user emotion, style, theme, and intent  
- 🎨 **Artist Agent** — Converts structured context into prompt-ready creative instructions  
- 🔍 **Critic Agent** *(optional)* — Allows refinement loop if user wants to regenerate  
- 🧠 **Orchestrator** — Coordinates agents and ensures cohesive generation

> Built to be extendable: agents can be swapped, retrained, or improved independently.

---

## 🧰 Tech Stack

| Layer           | Tools Used                                                                 |
|----------------|------------------------------------------------------------------------------|
| Frontend        | [Streamlit](https://streamlit.io)                                          |
| Backend Logic   | Python 3.10, Modular Agent Classes (`PlannerAgent`, `ArtistAgent`, etc.)   |
| Model API       | Hugging Face Image Models (GROQ or Stable Diffusion)                       |
| UI Styling      | Custom CSS + Streamlit widgets                                             |
| Deployment      | Localhost / Streamlit deployment                                |
| Version Control | Git + GitHub                                                               |

---


## 🛠️ Installation & Setup

1. **Clone the repository**  
```bash
   git clone https://github.com/your-username/emotoart.git
   cd emotoart
```
2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```
3. **Install dependencies**  
```bash
   pip install -r requirements.txt
```
4. **Run the App**
```bash
streamlit run app.py
```
