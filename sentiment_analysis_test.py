import unittest
from sentiment_analysis import analyze_sentiment

class TestSentimentAnalysis(unittest.TestCase):
    def test_positive_sentiment(self):
        positive_text = "I absolutely love this wonderful, fantastic product!"
        self.assertEqual(analyze_sentiment(positive_text), "Positive")

    def test_negative_sentiment(self):
        negative_text = "This is the worst experience ever, I hate it so much."
        self.assertEqual(analyze_sentiment(negative_text), "Negative")

    def test_neutral_sentiment(self):
        neutral_text = "It was unusuable."
        self.assertEqual(analyze_sentiment(neutral_text), "Neutral")

    def test_empty_string(self):
        # Testing an edge-case where the string is empty.
        self.assertEqual(analyze_sentiment(""), "Neutral")

if __name__ == "__main__":
    unittest.main()
