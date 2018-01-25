from textblob import TextBlob
#from textblob_fr import PatternTagger, PatternAnalyzer

def analize_sentiment(text):
    analysis = TextBlob(text)
    print("language : " + analysis.detect_language())
    trad = analysis.translate(from_lang="auto", to="en")
    print("en : " + str(trad))
    #French Version
    #analysis = TextBlob(text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    if trad.sentiment.polarity > 0:
        return 1
    elif trad.sentiment.polarity == 0:
        return 0
    else:
        return -1

ptext = input()
result = analize_sentiment(ptext)
print(result)
