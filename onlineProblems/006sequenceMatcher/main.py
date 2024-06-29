from difflib import SequenceMatcher

textOne= "My Name is Sharathchandra"
textTwo = "Hi, My Name is Sharathchandra"

sequenceScore = SequenceMatcher(None, textOne, textTwo).ratio()
print(f"Both are {sequenceScore * 100} % similar")

