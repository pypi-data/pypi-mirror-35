import sqlite3
from collections import Counter
import codecs


    
def clean_stop_words (wordlist):
    with codecs.open('stop_words.txt', 'r', 'UTF-8') as myfile:
        stops = [x.replace("\r\n","") for x in myfile]
        return list(set(wordlist).difference(set(stops)))

class text ():
   
    def __init__(self, text): 
        self.text = text
        
    def sentiments( self) :
        emotions = []
        Words = clean_stop_words (self.text.split(" "))
        db = sqlite3.connect('emos.db')
        cursor = db.cursor()
        Words = list(filter(None, Words))
        for word in Words:
            if word.startswith("ي") or word.startswith("ت") or word.startswith("أ"):
                word=word[1:]
            if word.endswith("ة") or word.startswith("ي") or word.startswith(b'\xd8\xa9'.decode('utf-8')):
                word=word[:-1]
            
            cursor.execute(''' 

            SELECT priorpolarity FROM lexicon WHERE ar_word LIKE ?''', ('%{}%'.format(word),))



            emotion = cursor.fetchone()
            try:
                if emotion !=None or emotion[0] !='' :
                    emotions.append(emotion[0])
            except:
            # emotions.append('undefined')
                pass

        db.close()
        c = Counter(emotions)
        percents = [(i, c[i] / len(emotions) * 100.0) for i, count in c.most_common() if i!='None ']
        if percents !=[]:
            anal = dict(percents )
            anal['text'] = self.text
            
            return anal
        else:
            return "Insufficient text for analysis ! "




