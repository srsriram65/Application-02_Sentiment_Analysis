
text = input("Enter a sentence: ")

positive_words = [
    "good", "great", "excellent", "happy",
    "love", "amazing", "wonderful", "best"
]

negative_words = [
    "bad", "terrible", "sad", "hate",
    "worst", "poor", "awful"
]

words = text.lower().split()

positive = 0
negative = 0

for word in words:
    if word in positive_words:
        positive += 1

    if word in negative_words:
        negative += 1

if positive > negative:
    print("Sentiment: Positive")
elif negative > positive:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")
