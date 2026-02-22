def unique_lines(text):
    # Split the text by newlines and strip whitespace
    lines = [line.strip() for line in text.strip().split('\n') if line.strip()]
    # Use a dict to preserve order and ensure uniqueness
    unique = list(dict.fromkeys(lines))
    return unique

# Example usage
multiline_text = """

"""

results = unique_lines(multiline_text)
print(results)
print(len(results))

results.sort()
for result in results:
    print(result+',')

