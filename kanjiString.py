
import pykakasi
import kanjiStringUtils


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
    

    def toRomaji_MOFA(self, kana):
        out = []
        pt = 0
        doubleConsonant = False # 促音 check
        while pt < len(kana):
            print(pt, kana[pt])
            # 2 kanas
            if pt + 2 <= len(kana) and kana[pt:pt+2] in kanjiStringUtils.hebon:
                match = kanjiStringUtils.hebon[kana[pt:pt+2]]
                if doubleConsonant == True and kana[pt] == "チ":
                    doubleConsonant = False
                    match = "t" + match
                out.append(match)
                pt += 2
            # found "ッ"
            elif kana[pt] == "ッ":
                doubleConsonant = True
                pt += 1
            # found "ー", skip
            elif kana[pt] == "ー":
                pt += 1
            # 1 kana
            elif kana[pt] in kanjiStringUtils.hebon:
                match = kanjiStringUtils.hebon[kana[pt]]
                if doubleConsonant == True:
                    doubleConsonant = False
                    if kana[pt] == "チ":
                        match = "t" + match
                    else:
                        match = match[0] + match
                # 撥音 check
                if match[0] in {"B", "M", "P"} and len(out) > 0 and out[-1] == "N":
                    out[-1] = "M"
                # 長音 check OやUは記入しません。
                if match == "U" and ((out[-1][-1] == "U") or out[-1][-1] == "O") :
                    # OU, UU skip
                    match = ""
                elif match == "O" and len(out) > 0 and out[-1] == "O":
                    # OO skip
                    match = ""

                out.append(match)
                pt += 1
            else:
                out.append("X")
                pt += 1

        out = "".join(out)
        out = out.lower()
        return out

                
