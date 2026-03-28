
import os

# 🔥 fixes for Python 3.13
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"
os.environ["TRANSFORMERS_NO_TORCHVISION"] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = ""

import streamlit as st
from services.auditor import SustainabilityAuditor

# ---------------- INIT ----------------
auditor = SustainabilityAuditor()

st.set_page_config(page_title="GT Auditor Pro", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
html, body {
    background-color: #050608;
    color: #ffffff;
}

.score-bar {
    height: 12px;
    border-radius: 10px;
    background: linear-gradient(90deg, red, yellow, green);
}

.highlight {
    background-color: rgba(255,0,0,0.3);
    padding: 2px 6px;
    border-radius: 5px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<h1 style='color:#00ff88;text-align:center'>Green Truth Auditor</h1>", unsafe_allow_html=True)

# ---------------- INPUT ----------------
text = st.text_area(
    "Product Description",
    placeholder="Paste product description...",
    height=150,
    label_visibility="collapsed"
)

run = st.button("RUN NEURAL AUDIT")

# ---------------- HIGHLIGHT FUNCTION ----------------
def highlight_text(text, buzzwords):
    for word in buzzwords:
        text = text.replace(word, f"<span class='highlight'>{word}</span>")
    return text

# ---------------- RUN ----------------
if run:

    if not text:
        st.error("⚠️ Please enter product description")

    else:
        with st.spinner("🔍 Running AI Audit..."):
            result = auditor.audit(text)

        st.success("✅ Audit Complete")

        confidence = result["confidence"]
        buzzwords = result["buzzwords_detected"]
        certifications = result["certifications_found"]

        trust_score = int(confidence * 100)

        # color logic
        if "❌" in result["final_category"]:
            color = "#ff4b4b"
            fraud = "HIGH"
        else:
            color = "#00ff88"
            fraud = "LOW"

        evidence = "FOUND" if certifications else "NONE"

        # ---------------- SCORE ----------------
        st.markdown("### 🔥 Sustainability Score")

        st.progress(trust_score)

        st.markdown(f"""
        <div class="score-bar" style="width:{trust_score}%"></div>
        """, unsafe_allow_html=True)

        # ---------------- METRICS ----------------
        st.markdown("### CRITICAL INDICES")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Trust Score", f"{trust_score}%")
        c2.metric("Fraud Risk", fraud)
        c3.metric("Evidence", evidence)
        c4.metric("AI Confidence", f"{confidence*100:.1f}%")

        # ---------------- VERDICT ----------------
        st.markdown("### AUDIT VERDICT")

        st.markdown(f"""
        <div style="padding:20px;border:2px solid {color};border-radius:10px">
            <h2 style="color:{color}">{result['final_category']}</h2>
            <p>{result['explanation']}</p>
        </div>
        """, unsafe_allow_html=True)

        # ---------------- HIGHLIGHT ----------------
        st.markdown("### 🔍 Highlighted Text")

        highlighted = highlight_text(text.lower(), buzzwords)
        st.markdown(highlighted, unsafe_allow_html=True)

        # ---------------- BUZZWORDS ----------------
        st.markdown("### BUZZWORDS DETECTED")

        if buzzwords:
            for b in buzzwords:
                st.success(b.upper())
        else:
            st.info("No buzzwords found")