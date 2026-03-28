# 🌱 Green-Truth Auditor  
### 🚀 Team: PersistX  

---

## 🌍 Why We Built This  

Today, almost every product claims to be *eco-friendly*, *natural*, or *green*.  
But how many of these claims are actually true?  

This practice, known as **greenwashing**, creates confusion and breaks consumer trust.  
People who genuinely want to make sustainable choices often don’t have the tools to verify these claims.  

That’s the problem we wanted to solve.  

---

## 💡 Our Idea  

We built the **Green-Truth Auditor** — a simple yet powerful tool that helps users check whether a sustainability claim is genuine or just marketing fluff.  

Instead of blindly trusting labels, users can now get:  
- A clear verdict  
- A confidence score  
- And most importantly, a reason behind the decision  

---

## 🧠 How It Works  

Our system combines AI and logic to make decisions more reliable.

### Step 1: Input  
Users can either paste a product description or provide a URL.

### Step 2: Understanding the Claim  
We use a **zero-shot NLP model (BART MNLI)** to understand the intent of the text — whether it sounds vague or evidence-based.

### Step 3: Detecting Buzzwords  
We check for commonly misused terms like:  
*eco-friendly, natural, green, sustainable*  

These are strong indicators of potential greenwashing.

### Step 4: Decision Making  
We don’t rely only on AI.  
We combine:
- Model prediction  
- Buzzword detection  
- Confidence score  

This hybrid approach makes our system more robust.

### Step 5: Explanation  
Instead of just saying “this is wrong”, we explain *why*.  
This makes the system transparent and user-friendly.

---

## ✨ What Makes Our Project Special  

- We don’t just classify — **we explain**  
- We combine **AI + rule-based logic**  
- No training data required (zero-shot learning)  
- Designed for real-world use  

---

## 🛠️ Tech Stack  

- Python  
- Hugging Face Transformers (BART MNLI)  
- FastAPI (Backend)  
- Streamlit (Frontend)  
- BeautifulSoup (Web Scraping)  

---

## 📊 Current Status  

- The system is fully functional for text-based analysis  
- URL scraping is implemented  
- Accuracy evaluation is still in progress  

---

## ⚠️ Limitations  

- We have not yet integrated a certification database (RAG)  
- The system depends on how clearly the claim is written  
- Model predictions may vary in edge cases  

---

## 🔮 What’s Next  

We see a lot of potential for this project.  

In the future, we plan to:  
- Add a certification database (RAG) to verify claims  
- Introduce a sustainability score (0–100)  
- Build a browser extension for real-time analysis  
- Improve accuracy through fine-tuning  

---

## 🌍 Impact  

Our goal is simple:  

👉 Help people make better, informed choices  
👉 Reduce misleading sustainability claims  
👉 Promote honest and transparent branding  

---

## 👥 Team  

**PersistX**  

---

## 🚀 How to Run  

Install dependencies:

```bash
pip install -r requirements.txt
