import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
from transformers import pipeline


class TextAnalyzer:
    def word_count(self, text):
        return len(text.split())

    def char_count(self, text):
        return len(text)  # Liczy wszystkie znaki (w tym spacje)

    def unique_words(self, text):
        return len(set(text.split()))  # Usuwa duplikaty i liczy unikalne słowa

class AdvancedTextAnalyzer(TextAnalyzer):

    def sentiment_analysis(self, text):
        sentiment_pipeline = pipeline("sentiment-analysis")
        data = text
        return sentiment_pipeline(data)


with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()  # Odczytujemy cały tekst z pliku

a = TextAnalyzer()
b = AdvancedTextAnalyzer()

print("Liczba słów:", a.word_count(text))
print("Liczba znaków:", a.char_count(text))
print("Liczba unikalnych słów:", a.unique_words(text))
print("Sentiment: ", b.sentiment_analysis(text))
