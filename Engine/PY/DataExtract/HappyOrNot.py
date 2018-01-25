from textblob import TextBlob
#from textblob_fr import PatternTagger, PatternAnalyzer

def analize_sentiment(text):
    analysis = TextBlob(text)
    print("language : " + analysis.detect_language())
    #French Version
    #analysis = TextBlob(text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1

ptext = input()
result = analize_sentiment(ptext)
print(result)
