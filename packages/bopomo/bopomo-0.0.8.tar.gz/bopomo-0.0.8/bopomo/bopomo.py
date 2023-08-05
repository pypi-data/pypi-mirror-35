# -*- coding: utf-8 -*-
import jieba
import re
import pycrfsuite
import csv
import pkg_resources

filename = pkg_resources.resource_filename('bopomo', 'data/bopomo_word.csv')
with open(filename, 'rt', encoding='utf8') as fin:
    reader= csv.reader(fin)
    bopomo_word = {x[0]:x[1:] for x in reader}
filename = pkg_resources.resource_filename('bopomo', 'data/bopomo_words.csv')
with open(filename, 'rt', encoding='utf8') as fin:
    reader= csv.reader(fin)
    bopomo_words = {x[0]:x[1:] for x in reader}
filename = pkg_resources.resource_filename('bopomo', 'data/bopomo_seg_words.csv')
with open(filename, 'rt', encoding='utf8') as fin:
    reader = csv.reader(fin)
    bopomo_seg_words = {x[0]:x[1:] for x in reader}

filename = pkg_resources.resource_filename('bopomo', 'data/words_list.txt')
fout = open(filename, 'wt', encoding='utf8')
for i in [x[0] for x in list(bopomo_words.items()) + list(bopomo_seg_words.items())]:
    fout.write(i + ' ' + '1\n')
fout.close()

jieba.set_dictionary(filename)
bopomo_word.update(bopomo_words)
bopomo_word.update(bopomo_seg_words)
del bopomo_words,bopomo_seg_words,i,fout
class bopomo_sent():
    def __init__(self, s):
        self.split = re.split('\W',s)
        self.cut = [list(jieba.cut(x, HMM=False)) for x in self.split]
        self.cut = [x for x in self.cut if len(x) > 0]
    def bopomo_tag(self):
        tagger = pycrfsuite.Tagger()
        filename = pkg_resources.resource_filename('bopomo', 'model/bopomo.crfsuite')
        tagger.open(filename)
        def word2features(sent, i):
            word = sent[i]
            features = [
                'bias',
                'word=' + word
            ]
            if i > 0:
                word1 = sent[i - 1]
                features.extend([
                    '-1:word=' + word1
                ])

            if i < len(sent) - 1:
                word1 = sent[i + 1]
                features.extend([
                    '+1:word=' + word1
                ])
            return features

        def sent2features(sent):
            return [word2features(sent, i) for i in range(len(sent))]
        y_predict = [tagger.tag(sent2features(s)) for s in self.cut]
        def bopomo_choose(w, p):
            if len(w)== len(p):
                w0 = []
                p0 = []
                for i in range(len(w)):
                    if w[i] in set(bopomo_word):
                        w0.append(w[i])
                        if len(bopomo_word[w[i]]) < int(p[i]):
                            p[i] = len(bopomo_word[w[i]])
                        p0.append(bopomo_word[w[i]][int(p[i])-1])
                    else:
                        w0.append(w[i])
                        p0.append(w[i])
            else:
                print('len(w) != len(p)')
            return [''.join(w0),' '.join(p0)]
        result = [bopomo_choose(x,y) for x,y in zip(self.cut, y_predict)]

        return result


if __name__ == "__main__":
    txt = input('輸入一段中文')
    print(bopomo_sent(txt).bopomo_tag())
