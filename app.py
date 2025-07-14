import streamlit as st
from io import BytesIO
from agents.orchestrator import MultiAgentOrchestrator

st.set_page_config(
    page_title="EmotoArt - Multi-Agent Assistant",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize orchestrator
if 'orchestrator' not in st.session_state:
    st.session_state.orchestrator = MultiAgentOrchestrator()

# Sidebar - Settings
with st.sidebar:
    st.header(" Settings")

    mood = st.selectbox("How are you feeling today?", [
        "Calm", "Excited", "Anxious", "Happy", "Melancholic",
        "Joyful", "Nostalgic", "Inspired", "Frustrated", "Relaxed", "Curious", "Hopeful"
    ], help="Select your current emotional state to inspire the art")

    style = st.selectbox("Preferred Art Style", [
        "Watercolor", "Anime", "Surrealism", "Digital Painting", "Abstract",
        "Impressionism", "Cubism", "Pop Art", "Expressionism", "Minimalism", "Fantasy Art", "Concept Art"
    ], help="Choose your favorite visual expression style")

    color_palette = st.selectbox("Choose a Color Palette", ["Warm", "Cool", "Monochrome", "Pastel", "Vibrant"], help="Defines the overall color tone")

    theme = st.multiselect("Select Theme or Subject Matter", ["Nature", "Urban", "Fantasy", "Portraits", "Abstract Forms", "Animals"], help="Select one or more subjects for your art")

    keywords = st.text_input("Enter keywords (optional)", placeholder="e.g., sunset, cityscape", help="Add any specific concepts you want to include")

    art_size = st.selectbox("Select Art Size", ["Portrait", "Landscape", "Square"], help="Choose your canvas orientation")

    num_variations = st.slider("Number of variations", 1, 4, 1, help="How many image versions should be generated")
    creativity_level = st.slider("Creativity level", 1, 10, 7, help="How imaginative the generation should be")
    generate = st.button("🎨 Generate Art", use_container_width=True)

# Title & Introduction
st.markdown("<h1 style='text-align: center;'>🎨 EmoToArt - Multi Agent Assistant </h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Where Emotions Become Masterpieces</h3>", unsafe_allow_html=True)

# Tabs layout
selected_tab = st.tabs(["🏠 Home", "🖼️ Gallery", "🗣️ Feedback"])

# --------------------
# Home Tab
# --------------------
with selected_tab[0]:
    # Update generation flag BEFORE any rendering
    if generate:
        st.session_state.generating = True

    # Show description only if generation hasn't started yet
    if not st.session_state.get('generating', False):
        st.markdown("""
        <div style='text-align: center; font-size:17px; padding: 1rem 3rem;'>
        Don't just imagine art—create it with your feelings!!!<br>
        Turn your mood into stunning AI-generated artwork with just a few clicks! Whether you're feeling joyful, melancholic, or inspired,My EmoToArt Multi Agent transforms your emotions.
        </div>
        """, unsafe_allow_html=True)

    # If generation is triggered
    if st.session_state.get('generating', False):
        with st.spinner("✨ Crafting your artwork..."):
            try:
                prompt, images = st.session_state.orchestrator.generate_art(
                    mood, style, num_variations, creativity_level
                )

                st.subheader("📝 Generated Prompt")
                st.markdown(f'<div class="generated-content">{prompt}</div>', unsafe_allow_html=True)

                st.markdown("---")
                st.markdown("Want to make it better?")
                if st.button("🔄 Refine this Prompt", use_container_width=True):
                    if st.session_state.orchestrator.history:
                        st.session_state.orchestrator.history.pop()
                    st.rerun()

            except Exception as e:
                st.error(f"Image generation failed: {e}")

# --------------------
# Gallery Tab
# --------------------
with selected_tab[1]:
    if st.session_state.orchestrator.history:
        cols = st.columns(4)
        for i, item in enumerate(reversed(st.session_state.orchestrator.history[-8:])):
            with cols[i % 4]:
                for idx, img in enumerate(item['image']):
                    st.image(img, use_container_width=True)
                    st.caption(item['prompt'].splitlines()[0])
                    buf = BytesIO()
                    img.save(buf, format="PNG")
                    st.download_button(
                        f"📥 Download {i+1}.{idx+1}",
                        buf.getvalue(),
                        file_name=f"artistryai_art_{i+1}_{idx+1}.png",
                        mime="image/png"
                    )
    else:
        st.info("No art generated yet. Go to the Home tab and generate your first masterpiece!")

# --------------------
# Feedback Tab
# --------------------
with selected_tab[2]:
    with st.form("feedback_form"):
        name = st.text_input("Your Name")
        feedback_text = st.text_area("Your Feedback")
        submit = st.form_submit_button("Submit")

        if submit:
            st.success("Thank you! Here's a happy quote for you: ✨ 'Creativity takes courage!' – Henri Matisse")

# --------------------
# Footer
# --------------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>© 2025 <b>Amna Sabahat</b>. All rights reserved.</p>",
    unsafe_allow_html=True
)
