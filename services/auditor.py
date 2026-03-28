
# from models.nlp_model import GreenwashingClassifier

# class SustainabilityAuditor:
#     def __init__(self):
#         self.model = GreenwashingClassifier()

#     # 🔍 Detect vague/buzzwords
#     def contains_vague_terms(self, text):
#         vague_words = [
#             "eco-friendly",
#             "natural",
#             "green",
#             "sustainable",
#             "environmentally safe",
#             "planet friendly"
#         ]
#         return [word for word in vague_words if word in text.lower()]

#     # 🧠 Explanation generator
#     def generate_explanation(self, label, confidence, buzzwords):
#         if buzzwords:
#             return f"The claim uses vague terms like {buzzwords}, which are not easily verifiable."

#         if confidence < 0.6:
#             return f"The model is uncertain about this claim (low confidence: {confidence:.2f}), indicating possible vagueness."

#         if "vague" in label or "misleading" in label:
#             return "The claim appears vague or potentially misleading without strong supporting evidence."

#         return "The claim includes specific, measurable, or certifiable sustainability information."

#     # 🚀 MAIN AUDIT FUNCTION
#     def audit(self, text):

#         result = self.model.classify(text, use_advanced=True)

#         label = result["label"]
#         confidence = result["confidence"]

#         buzzwords = self.contains_vague_terms(text)

#         # 🔥 FINAL DECISION LOGIC (IMPROVED)
#         if buzzwords and confidence < 0.75:
#             final_category = "❌ Marketing Fluff (Buzzword + Weak Evidence)"

#         elif confidence < 0.6:
#             final_category = "❌ Marketing Fluff (Low Confidence)"

#         elif "vague" in label or "misleading" in label:
#             final_category = "❌ Marketing Fluff"

#         else:
#             final_category = "✅ Evidence-Based"

#         explanation = self.generate_explanation(label, confidence, buzzwords)

#         return {
#             "final_category": final_category,
#             "predicted_label": label,
#             "confidence": round(confidence, 3),
#             "buzzwords_detected": buzzwords,
#             "explanation": explanation,
#             "detailed_scores": result["all_scores"]
#         }
# services/auditor.py

from models.nlp_model import GreenwashingClassifier
from services.rag_engine import RAGEngine


class SustainabilityAuditor:
    def __init__(self):
        self.model = GreenwashingClassifier()
        self.rag = RAGEngine()

    def contains_vague_terms(self, text):
        vague_words = [
            "eco-friendly",
            "natural",
            "green",
            "sustainable",
            "environmentally safe",
            "planet friendly",
            "eco-conscious"
        ]

        text_lower = text.lower()
        return [word for word in vague_words if word in text_lower]

    def generate_explanation(self, label, confidence, buzzwords, rag_results):

        if rag_results:
            return f"Certified brand detected: {rag_results}. This increases credibility."

        if buzzwords:
            return f"The claim uses vague terms like {buzzwords}, which are not verifiable."

        if confidence < 0.6:
            return f"Low confidence ({confidence:.2f}) suggests unclear claims."

        if "vague" in label or "misleading" in label:
            return "The claim appears vague or misleading without strong evidence."

        return "The claim includes measurable or certified sustainability proof."

    def audit(self, text):

        result = self.model.classify(text)

        label = result["label"]
        confidence = result["confidence"]

        buzzwords = self.contains_vague_terms(text)
        rag_results = self.rag.find_certification(text)

        # Final decision logic
                # 🔥 FINAL DECISION (IMPROVED)

        # 1. Certified brand = always trusted
        if rag_results:
            final_category = "✅ Evidence-Based (Certified Brand)"

        # 2. Buzzwords without proof = fluff (STRONG RULE)
        elif buzzwords:
            final_category = "❌ Marketing Fluff (Buzzwords)"

        # 3. Low confidence = suspicious
        elif confidence < 0.6:
            final_category = "❌ Marketing Fluff (Low Confidence)"

        # 4. Model says vague/misleading
        elif "vague" in label or "misleading" in label:
            final_category = "❌ Marketing Fluff"

        # 5. Otherwise = valid claim
        else:
            final_category = "✅ Evidence-Based"

        explanation = self.generate_explanation(
            label, confidence, buzzwords, rag_results
        )

        return {
            "final_category": final_category,
            "predicted_label": label,
            "confidence": round(confidence, 3),
            "buzzwords_detected": buzzwords,
            "certifications_found": rag_results,
            "explanation": explanation,
            "detailed_scores": result["all_scores"]
        }