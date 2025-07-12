# prompts/art_prompt_template.py

def art_prompt(mood: str, style: str = ""):
    return f"""
You are a helpful creative assistant for artists.

🎨 The artist is feeling: {mood}
🖌️ Preferred art style: {style if style else "No specific style"}

Suggest a unique art idea that matches their mood and style. 
Also include:
1. 3 visual elements (e.g., fog, mountains, feathers,trees,sand,seaview,lights,sandy-nights,snowfalling)
2. A suggested color palette
3. A short motivational caption to inspire the artist
"""
