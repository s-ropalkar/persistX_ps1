
# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# import torch
# import torch.nn.functional as F


# class GreenwashingClassifier:
#     def __init__(self):
#         print("🔄 Loading NLP model safely...")

#         self.tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-mnli")

#         # 🔥 IMPORTANT: no .to(), no device forcing
#         self.model = AutoModelForSequenceClassification.from_pretrained(
#             "facebook/bart-large-mnli",
#             low_cpu_mem_usage=True
#         )

#         self.model.eval()

#         print("✅ Model loaded (safe mode)!")

#     def classify(self, text, use_advanced=True):

#         labels = [
#             "vague marketing claim",
#             "greenwashing or misleading claim",
#             "fact-based sustainability claim with certification",
#             "scientific environmental statement with data"
#         ]

#         # NLI input formatting
#         inputs = [f"{text} </s></s> This statement is {label}." for label in labels]

#         encoded = self.tokenizer(
#             inputs,
#             return_tensors="pt",
#             padding=True,
#             truncation=True,
#             max_length=512
#         )

#         # 🔥 DO NOT MOVE TO DEVICE
#         with torch.no_grad():
#             outputs = self.model(**encoded)

#         logits = outputs.logits

#         # entailment score (index 2)
#         probs = F.softmax(logits, dim=1)[:, 2]

#         scores = probs.tolist()

#         sorted_pairs = sorted(
#             zip(labels, scores),
#             key=lambda x: x[1],
#             reverse=True
#         )

#         best_label, best_score = sorted_pairs[0]

#         return {
#             "label": best_label,
#             "confidence": float(best_score),
#             "all_scores": dict(sorted_pairs)
#         }
# models/nlp_model.py

from transformers import pipeline


class GreenwashingClassifier:
    def __init__(self):
        print("🔄 Loading NLP model...")

        self.classifier = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli",
            device=-1  # 🔥 force CPU (safe for your system)
        )

        print("✅ Model ready!")

    def classify(self, text, use_advanced=True):

        labels = [
            "vague marketing claim",
            "greenwashing or misleading claim",
            "fact-based sustainability claim with certification",
            "scientific environmental statement with data"
        ]

        result = self.classifier(
            str(text),            # 🔥 ensure string
            labels,
            truncation=True       # 🔥 prevents crash on long text
        )

        return {
            "label": result["labels"][0],
            "confidence": float(result["scores"][0]),
            "all_scores": dict(zip(result["labels"], result["scores"]))
        }