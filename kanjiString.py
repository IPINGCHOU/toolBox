
import pykakasi


class kanjiTools:
    
    def __init__(self):
        self.kks = pykakasi.kakasi()

    def gram(self, text, unit):
        if len(text) < unit:
            text = text.rjust(unit, "O")
        res = [text[i:i+unit] for i in range(len(text) - unit + 1)]
        return res

    def jaccardSimilarity(self, s1, s2, grams = [1], to_hira = False, to_roman = False):
        
        if to_roman:
            s1 = self.kks.convert(s1)
            s1 = "".join([i['hepburn'] for i in s1])
            s2 = self.kks.convert(s2)
            s2 = "".join([i['hepburn'] for i in s2])
        elif to_hira:
            s1 = self.kks.convert(s1)
            s1 = "".join([i['hira'] for i in s1])
            s2 = self.kks.convert(s2)
            s2 = "".join([i['hira'] for i in s2])

        g1, g2 = [], []
        for g in grams:
            g1.extend(self.gram(s1, g))
            g2.extend(self.gram(s2, g))
        res =  len(set(g1).intersection(set(g2)))/len(set(g1).union(set(g2)))
        
        return res
        
