import string

text = "Hello! How are you doing today? Let's analyze this sentence."

# Remove punctuation
text_without_punctuation = ''.join([char for char in text if char not in string.punctuation])
print(f"Text Without Punctuation: {text_without_punctuation}")
