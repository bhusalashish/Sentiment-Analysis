from textblob import TextBlob

def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment polarity
    polarity = blob.sentiment.polarity
    
    # Determine sentiment based on polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    # Prompt the user for input
    text = input("Enter a text string: ")
    
    # Analyze the sentiment
    sentiment = analyze_sentiment(text)
    
    # Output the result
    print(f"The sentiment of the text is: {sentiment}")
