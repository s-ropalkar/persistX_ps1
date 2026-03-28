
# # // python -m tests.test_model
# from services.auditor import SustainabilityAuditor
# from utils.scraper import extract_text_from_url
# auditor = SustainabilityAuditor()


# test_cases = [
#     "This product is 100% eco-friendly and natural",
#     "Certified organic by USDA and uses 30% less water",
#     "Green and sustainable choice for your lifestyle",
#     "Approved by global environmental standards",
    
# ]

# for text in test_cases:
#     print("\nINPUT:", text)

#     result = auditor.audit(text)

#     print("OUTPUT:", result["final_category"])
#     print("LABEL:", result["predicted_label"])
#     print("CONFIDENCE:", result["confidence"])
#     print("BUZZWORDS:", result["buzzwords_detected"])
#     print("EXPLANATION:", result["explanation"])
# tests/test_model.py

from services.auditor import SustainabilityAuditor

auditor = SustainabilityAuditor()

test_cases = [
    "This product is 100% eco-friendly and natural",
    "Certified organic by USDA and uses 30% less water",
    "Green and sustainable choice for your lifestyle",
    "Patagonia jacket made with recycled materials"
]

for text in test_cases:
    print("\n========================")
    print("INPUT:", text)

    result = auditor.audit(text)

    print("FINAL:", result["final_category"])
    print("LABEL:", result["predicted_label"])
    print("CONFIDENCE:", result["confidence"])
    print("BUZZWORDS:", result["buzzwords_detected"])
    print("CERTIFICATIONS:", result["certifications_found"])
    print("EXPLANATION:", result["explanation"])