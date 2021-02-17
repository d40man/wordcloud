#-*- coding: utf-8 -*-

from os import path
from wordcloud import WordCloud
import jieba
import collections
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

d = path.dirname(__file__)

text = open(u'琅琊榜.txt', encoding='gbk').read()

cut_text = jieba.cut(text, cut_all=False)
#result = " ".join(cut_text)

result = ''
remove_words = [u'的', u'，',u'和', u'是', u'么', u'在', u'对',u'等',
                u'能',u'都',u'。',u' ',u'、',u'中',u'在',u'了',
                u'通常',u'他',u'我',u'你',u'人', u'也', u'她', u'吗', 
                u'还', u'不', u'去', u'来', u'这', u'要', u'却', u'我们', u'这个', u'那', 
                u'好', u'没有', u'说', u'被', u'他们', u'呢', u'吧', u'还是', u'什么', u'就是', 
                u'不是', u'这样', u'已经', u'将', u'一个', u'好', u'所以', u'怎么', u'大家', u'啊', 
                u'但', u'上', u'有', u'自己', u'现在', u'到', u'不过', u'只是',
                u'便', u'有些', u'没', u'得', u'给', u'过', u'看', u'可是',
                u'可是', u'因为', u'时', u'想', u'个', u'已', u'可以', u'把',
                u'很', u'那个', u'会', u'只有', u'跟', u'可', u'虽然', u'着',
                u'才', u'知道', u'不会', u'不能', u'再', u'有', u'过来', u'与',
                u'多', u'看着', u'让', u'那个', u'后', u'今天', u'而', u'为',
                u'你们', u'走', u'出来', u'突然', u'如果', u'一起', u'时候', u'只',
                u'谁', u'起来', u'过去', u'这里', u'并', u'几个', u'一定', u'之',
                u'听', u'不要', u'一', u'见', u'做', u'向', u'道', u'应该',
                u'实在', u'一直', u'一下', u'其实', u'为了', u'先生', u'不知', u'一点',
                u'觉得', u'从', u'立即', u'以', u'心中', u'叫', u'还有', u'既然',
                u'进来', u'事', u'明白', u'更', u'这些', u'真的', u'想要', u'就算',
                u'请', u'连', u'这位', u'之后', u'笑', u'仍', u'此时', u'问',
                u'两人', u'太', u'事情', u'开始', u'当然', u'最后', u'对于', u'里',
                u'样子', u'那么', u'一样', u'若', u'为什么', u'只怕', u'根本', u'自然',
                u'心里', u'最', u'所', u'这么', u'您', u'如此', u'不敢', u'似乎',
                u'先', u'反而', u'站', u'表情', u'可能', u'到底', u'些', u'出',
                u'些', u'只要', u'两个', u'慢慢', u'一声', u'意思', u'有人', u'的话',
                u'地方', u'下来', u'打', u'忙', u'十分', u'刚才', u'快', u'大',
                u'它', u'一向', u'一般', u'回来', u'如何', u'这种', u'脸上', u'倒',
                u'清楚', u'比', u'住', u'以前', u'一些', u'虽', u'无', u'难道',
                u'看看', u'一句', u'一些', u'当年', u'其他', u'带', u'坐', u'确实',
                u'这是', u'发现', u'不想', u'们', u'话', u'任何', u'当', u'除了',
                u'而已', u'没什么', u'目光', u'用', u'拿', u'时间', u'声音', u'毕竟',
                u'眼前', u'之间', u'起', u'以为', u'看到', u'手', u'小', u'身上',
                u'也许', u'是不是', u'所以', u'该', u'前', u'真是', u'所有', u'一面',
                u'竟', u'地道', u'问道', u'准备', u'一时', u'出去', u'不由', u'眼睛',
                u'一次', u'由', u'不必', u'一眼', u'吃', u'感觉', u'哪里', u'象',
                u'只能', u'起身', u'外面', u'大概', u'果然', u'几乎', u'身边', u'想到',
                u'如今', u'一片', u'想到', u'当时', u'早就', u'于', u'这时', u'这次',
                u'面前', u'算', u'罢了', u'陪', u'说话', u'低声', u'问题', u'仿佛',
                u'片刻', u'依然', u'身份', u'回去', u'下', u'无论', u'甚', u'不好',
                u'同时', u'转身', u'看见', u'找', u'回', u'最终', u'好像', u'一切',
                u'正在', u'忍不住', u'由于', u'下去', u'结果', u'原本', u'可惜', u'好好',
                u'又', u'地', u'就'] # 自定义去除词库

for word in cut_text: # 循环读出每个分词
    if word not in remove_words: # 如果不在去除词库中
        #object_list.append(word) # 分词追加到列表
        result = result + ' ' + word

# 词频统计
#word_counts = collections.Counter(object_list) # 对分词做词频统计
#mask = np.array(Image.open('background.png')) # 定义词频背景
wc = WordCloud(
    font_path='锐字云字库准圆体_GBK.ttf',
 #   mask=mask,
    max_font_size=100,
    max_words=200)
#wc.generate_from_frequencies(word_counts)
wc.generate(result)
wc.to_file(r"wordcloud.png")
plt.figure()
plt.imshow(wc)
plt.axis("off")
plt.show()