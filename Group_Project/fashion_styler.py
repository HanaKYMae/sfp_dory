import streamlit as st
import random
import os

# --- Configuration ---
st.set_page_config(page_title="Fashion Styler", layout="centered")

st.title("👗 LookLoop")
st.markdown("Pick your preferences and let the app generate a stylish outfit for you!")

# --- Sidebar Filters ---
st.sidebar.header("✨ Filters")

gender = st.sidebar.selectbox("Gender", ["Men", "Women"])
occasion = st.sidebar.selectbox("Occasion", ["Casual", "Formal", "Party"])
season = st.sidebar.selectbox("Season", ["Summer", "Winter", "All Season"])

# --- Dummy Outfit Database ---
# Images should be placed in the `images/` folder
outfit_db = {
    "Men": {
        "Casual": {
            "top": ["casual_men_top.png"],
            "bottom": ["casual_men_bottom.png"],
            "shoes": ["casual_men_shoes.png"]
        },
        "Formal": {
            "top": ["formal_men_top.png"],
            "bottom": ["formal_men_bottom.png"],
            "shoes": ["formal_men_shoes.png"]
        },
        "Party": {
            "top": ["party_men_top.png"],
            "bottom": ["party_men_bottom.png"],
            "shoes": ["party_men_shoes.png"]
        }
    },
    "Women": {
        "Casual": {
            "top": ["casual_women_top.png"],
            "bottom": ["casual_women_bottom.png"],
            "shoes": ["casual_women_shoes.png"]
        },
        "Formal": {
            "top": ["formal_women_top.png"],
            "bottom": ["formal_women_bottom.png"],
            "shoes": ["formal_women_shoes.png"]
        },
        "Party": {
            "top": ["party_women_top.png"],
            "bottom": ["party_women_bottom.png"],
            "shoes": ["party_women_shoes.png"]
        }
    }
}

# --- Style Tips ---
style_tips = {
    "Casual": "🧢 Try pairing comfy sneakers with loose-fit jeans for a casual vibe.",
    "Formal": "🧥 Blazers and leather shoes always elevate a formal look.",
    "Party": "🎉 Go bold with colors or textures like sequins or velvet!"
}

# --- Outfit Generator ---
if st.button("👚 Generate Outfit"):
    top = random.choice(outfit_db[gender][occasion]["top"])
    bottom = random.choice(outfit_db[gender][occasion]["bottom"])
    shoes = random.choice(outfit_db[gender][occasion]["shoes"])

    st.subheader("Your Styled Look")
    cols = st.columns(3)
    cols[0].image(f"images/{top}", caption="Top", use_column_width=True)
    cols[1].image(f"images/{bottom}", caption="Bottom", use_column_width=True)
    cols[2].image(f"images/{shoes}", caption="Shoes", use_column_width=True)

    st.success(style_tips[occasion])

# --- Footer ---
st.markdown("---")
st.markdown("💡 Pro tip: Try different occasions or switch genders for variety!")
