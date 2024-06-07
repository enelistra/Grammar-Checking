import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

paragraph = input(" enter the paragraph here: ")

matches = tool.check(paragraph)

for match in matches:
    print(f"Message: {match.message}")
    print(f"Incorrect Text: {match.context}")
    print(f"Suggested Correction: {match.replacements}")
    print()

corrected_paragraph = language_tool_python.utils.correct(paragraph, matches)

print("Original Paragraph:")
print(paragraph)
print("\nCorrected Paragraph:")
print(corrected_paragraph)
