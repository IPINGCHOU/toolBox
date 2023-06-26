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

def test_toRomaji_MOFA():
    toolBox = kanjiString.kanjiTools()
    # normal
    s1 = "カタカナ"
    s1t = toolBox.toRomaji_MOFA(s1)
    assert s1t == "katakana"

    s2 = "シュヒュルロニョ"
    s2t = toolBox.toRomaji_MOFA(s2)
    assert s2t == "shuhyururonyo"

    # 撥音
    s3, s4, s5 = "ナンバ", "ホンマ", "サンペイ"
    s3t = toolBox.toRomaji_MOFA(s3)
    s4t = toolBox.toRomaji_MOFA(s4)
    s5t = toolBox.toRomaji_MOFA(s5)

    assert s3t == "namba"
    assert s4t == "homma"
    assert s5t == "sampei"

    # 促音
    s6, s7, s8, s9 = "ハットリ", "キッカワ", "ホッチ", "ハッチョウ"
    s6t = toolBox.toRomaji_MOFA(s6)
    s7t = toolBox.toRomaji_MOFA(s7)
    s8t = toolBox.toRomaji_MOFA(s8)
    s9t = toolBox.toRomaji_MOFA(s9)

    assert s6t == "hattori"
    assert s7t == "kikkawa"
    assert s8t == "hotchi"
    assert s9t == "hatcho"
    
    # 「―」を省略する場合
    s10, s11, s12 = "ニーナ", "シーナ", "サリー"
    s10t = toolBox.toRomaji_MOFA(s10)
    s11t = toolBox.toRomaji_MOFA(s11)
    s12t = toolBox.toRomaji_MOFA(s12)

    assert s10t == "nina"
    assert s11t == "shina"
    assert s12t == "sari"

    # 「イ」を省略しない場合
    s13, s14, s15 = "ニイナ", "シイナ", "サリイ"
    s13t = toolBox.toRomaji_MOFA(s13)
    s14t = toolBox.toRomaji_MOFA(s14)
    s15t = toolBox.toRomaji_MOFA(s15)

    assert s13t == "niina"
    assert s14t == "shiina"
    assert s15t == "sarii"

    # 「ウ」を含む長音「ウウ」の場合（「UU」は表記しません。）
    s16, s17, s18 = "ヒュウガ", "ユウキ", "ユウコ"
    s16t = toolBox.toRomaji_MOFA(s16)
    s17t = toolBox.toRomaji_MOFA(s17)
    s18t = toolBox.toRomaji_MOFA(s18)

    assert s16t == "hyuga"
    assert s17t == "yuki"
    assert s18t == "yuko"

    # 「オ」を含む長音「オウ」の場合（「OU」は表記しません。）
    s19, s20, s21 = "コウタ", "ヨウコ", "リョウコ"
    s19t = toolBox.toRomaji_MOFA(s19)
    s20t = toolBox.toRomaji_MOFA(s20)
    s21t = toolBox.toRomaji_MOFA(s21)

    assert s19t == "kota"
    assert s20t == "yoko"
    assert s21t == "ryoko"

    # 「オ」を含む長音「オオ」の場合（「OO」は表記しません。）
    s22, s23, s24 = "オオノ", "オオコウチ", "オオニシ"
    s22t = toolBox.toRomaji_MOFA(s22)
    s23t = toolBox.toRomaji_MOFA(s23)
    s24t = toolBox.toRomaji_MOFA(s24)

    assert s22t == "ono"
    assert s23t == "okochi"
    assert s24t == "onishi"

    # 末尾が「オオ」音で、ヨミカタが「オ」の場合（「OO」と表記します。）
    s25, s26, s27 = "セノオ", "タカトオ", "ヨコオ"
    s25t = toolBox.toRomaji_MOFA(s25)
    s26t = toolBox.toRomaji_MOFA(s26)
    s27t = toolBox.toRomaji_MOFA(s27)

    assert s25t == "senoo"
    assert s26t == "takatoo"
    assert s27t == "yokoo"

    # 末尾が「オウ」音で、ヨミカタが「ウ」の場合（「OU」とは表記しません。）
    s28, s29, s30 = "イトウ", "タカトウ", "ミソノウ"
    s28t = toolBox.toRomaji_MOFA(s28)
    s29t = toolBox.toRomaji_MOFA(s29)
    s30t = toolBox.toRomaji_MOFA(s30)

    assert s28t == "ito"
    assert s29t == "takato"
    assert s30t == "misono"

    # 「ヴ」のつく氏名例
    s31, s32 = "ヴィヴィアン", "ヴォードレール"
    s31t = toolBox.toRomaji_MOFA(s31)
    s32t = toolBox.toRomaji_MOFA(s32)

    assert s31t == "buibuian"
    assert s32t == "buodoreru"
    