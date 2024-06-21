from difflib import SequenceMatcher
text1 = "My Name is Ainy Gupta"
text2 = "Hi, My Name is AinyGupta"
sequenceScore = SequenceMatcher(None, text1, text2).ratio()
print(f"Both are {sequenceScore * 100} % similar")

text1 = "My Name is Ainy gupta"
text2 = "I am python developer"
sequenceScore = SequenceMatcher(None, text1, text2).ratio()
print(f"Both are {sequenceScore * 100} % similar")