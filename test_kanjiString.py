import test
import kanjiString

def test_jaccardSimilarity():
    toolBox = kanjiString.kanjiTools()

    a = "名古屋大学"
    b = "名大"
    c = "名古屋市立大学"
    d = "名市大"
    e = "北里大学"

    c1 = toolBox.jaccardSimilarity(a,b)
    c2 = toolBox.jaccardSimilarity(c,d)
    c3 = toolBox.jaccardSimilarity(c,e)

    c4 = toolBox.jaccardSimilarity(b,c)
    c5 = toolBox.jaccardSimilarity(d,a)

    assert [c1,c2,c3,c4,c5] != [0,0,0,0,0]


def test_jaccardSimilarity_toRoman():
    toolBox = kanjiString.kanjiTools()

    a = "名古屋大学"
    b = "名大"
    c = "名古屋市立大学"
    d = "名市大"
    e = "北里大学"

    c1 = toolBox.jaccardSimilarity(a,b, to_roman = True)
    c2 = toolBox.jaccardSimilarity(c,d, to_roman = True)
    c3 = toolBox.jaccardSimilarity(c,e, to_roman = True)

    c4 = toolBox.jaccardSimilarity(b,c, to_roman = True)
    c5 = toolBox.jaccardSimilarity(d,a, to_roman = True)

    assert [c1,c2,c3,c4,c5] != [0,0,0,0,0]

def test_jaccardSimilarity_toHira():
    toolBox = kanjiString.kanjiTools()

    a = "名古屋大学"
    b = "名大"
    c = "名古屋市立大学"
    d = "名市大"
    e = "北里大学"

    c1 = toolBox.jaccardSimilarity(a,b, to_hira = True)
    c2 = toolBox.jaccardSimilarity(c,d, to_hira = True)
    c3 = toolBox.jaccardSimilarity(c,e, to_hira = True)

    c4 = toolBox.jaccardSimilarity(b,c, to_hira = True)
    c5 = toolBox.jaccardSimilarity(d,a, to_hira = True)

    assert [c1,c2,c3,c4,c5] != [0,0,0,0,0]

def test_jaccardSimilarity_toHira_gram3():
    toolBox = kanjiString.kanjiTools()

    a = "名古屋大学"
    b = "名大"
    c = "名古屋市立大学"
    d = "名市大"
    e = "北里大学"

    c1 = toolBox.jaccardSimilarity(a,b, grams = [1,2,3], to_hira = True)
    c2 = toolBox.jaccardSimilarity(c,d, grams = [1,2,3], to_hira = True)
    c3 = toolBox.jaccardSimilarity(c,e, grams = [1,2,3], to_hira = True)

    c4 = toolBox.jaccardSimilarity(b,c, grams = [1,2,3], to_hira = True)
    c5 = toolBox.jaccardSimilarity(d,a, grams = [1,2,3], to_hira = True)


    assert [c1,c2,c3,c4,c5] != [0,0,0,0,0]

def test_gram():
    toolBox = kanjiString.kanjiTools()

    a = "東京大学"
    uni = toolBox.gram(a, 1)
    bi = toolBox.gram(a, 2)
    tri = toolBox.gram(a, 3)

    assert uni == ["東", "京", "大" , "学"]
    assert bi == ["東京", "京大", "大学"]
    assert tri == ["東京大", "京大学"]