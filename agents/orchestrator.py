from agents.agent import generate_art_idea
from agents.image_agent import generate_image
import streamlit as st

class MultiAgentOrchestrator:
    def __init__(self):
        self.history = []

    def generate_art(self, mood, style, num_variations, creativity_level=None, additional_info=None):
        # Step 1: Create the base art prompt
        prompt = generate_art_idea(mood, style)

        # Optional: Add extra detail (only if it's needed later)
        if additional_info:
            prompt += f"\n\nAdd this: {additional_info}"

        # Step 2: Generate multiple image variations
        images = []
        for i in range(num_variations):
            result = generate_image(prompt)
            if isinstance(result, list):
                images.extend(result)
            else:
                st.error(f"Image generation failed: {result}")

        # Step 3: Save to history if images generated
        if images:
            self.history.append({
                'prompt': prompt,
                'image': images,  # always store as list
                'mood': mood,
                'style': style,
                'timestamp': st.session_state.get('timestamp', 'now')
            })

        return prompt, images
