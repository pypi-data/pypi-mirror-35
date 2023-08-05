# bopomo

This is a package to translate a chinese sentence into bopomofo letters baesed on revised dictionary of Ministry of Education, segment corpus, artificial label data, and python package jieba and python-crfsuite.

```python
>>> import bopomo
>>> sent = '妹妹背著洋娃娃，走到花園來看花。'
>>> bopomo_sent = bopomo.bopomo_sent(sent)
>>> print(bopomo_sent.bopomo_tag())
[['妹妹背著洋娃娃', 'ㄇㄟˋ ˙ㄇㄟ ㄅㄟ ˙ㄓㄜ ㄧㄤˊ ㄨㄚˊ ˙ㄨㄚ'], ['走到花園來看花', 'ㄗㄡˇ ㄉㄠˋ ㄏㄨㄚ ㄩㄢˊ ㄌㄞˊ ㄎㄢˋ ㄏㄨㄚ']]

>>> sent = '如果薪水不到4萬8，可向老闆說你給的薪水太低了。'
>>> bopomo_sent = bopomo.bopomo_sent(sent)
>>> print(bopomo_sent.bopomo_tag())
[['如果薪水不到4萬8', 'ㄖㄨˊ ㄍㄨㄛˇ ㄒㄧㄣ ㄕㄨㄟˇ ㄅㄨˋ ㄉㄠˋ 4 ㄨㄢˋ 8'], ['可向老闆說你給的薪水太低了', 'ㄎㄜˇ ㄒㄧㄤˋ ㄌㄠˇ ㄅㄢˇ ㄕㄨㄛ ㄋㄧˇ ㄍㄟˇ ˙ㄉㄜ ㄒㄧㄣ ㄕㄨㄟˇ ㄊㄞˋ ㄉㄧ ˙ㄌㄜ']]


```