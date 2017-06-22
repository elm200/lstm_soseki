# preprocess

whitelist = "\n「」。、あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゐゆゑよらりるれろわをんがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽぁぃぅぇぉゃゅょっゎ"
whitelist = set(whitelist)
with open("souseki_all_hiragana.txt", "r") as f:
    for l in f:
        for c in l:
            if c in whitelist:
                print(c, end="")
