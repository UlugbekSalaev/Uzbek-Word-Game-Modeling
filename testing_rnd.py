# 1-chi execute fayl
# random tanlab olingan kubiklar yordamida qancha suzni (datasetdagi suzlardan) yasab bilishini hisoblash
# random kubiklar yordamisa yasaladigan suzlarni faylga yozib olish
from itertools import permutations
import operator

dataset = "en"

if dataset == "uz":
    soft = ['a', 'i', 'o', 'u', 'e', 'ō']    # uz
else:
    soft = ['e', 'a', 'o', 'i', 'u']      # en
cc = 8
cubics = []
words = []

def is_exist(word:str, n:int, cubic: tuple):
    for i in range(n):
        if word[i] not in cubic[i]:
            return False
    return True

for app in range(2):
    for iteration in range(1):
        print("App=", app, " iteration=", iteration)

        with open("words_"+dataset, encoding="utf8") as file:
            lines = file.readlines()
        words = [line.rstrip() for line in lines]

        with open("result/testrnd_"+dataset+"/train_res_app"+str(app), encoding="utf8") as file: # one row is cubic's letter
            lines = file.readlines()
            cubics = [line.rstrip().split() for line in lines]

        card_words_cnt = {}

        for word in words:
            #shu kubiklarga nicha suz yasash mumkinligni hisobla chiq,
            #keyin yana boshqa yul bn kubik yasa, hisobla
            n = len(word)  # word's length
            for i in permutations(cubics, n):
                if is_exist(word, n, i):
                    if word in card_words_cnt:
                        card_words_cnt[word] += 1
                    else:
                        card_words_cnt[word] = 1

        card_words_cnt = dict(sorted(card_words_cnt.items(), key=operator.itemgetter(1), reverse=True))
        with open("result/testrnd_"+dataset+"/test_res_app"+str(app), "w", encoding="utf8") as file:
            for i in card_words_cnt:
                file.writelines(i + "," + str(card_words_cnt[i]) + "\n")