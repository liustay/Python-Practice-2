from os import path

import jieba
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import WordCloud

#读取脚本所在目录
mulu = path.dirname(__file__)

#从文本中生成关键词
csv = open(path.join(mulu, 'douban.csv')).read()
seg_list = jieba.cut(csv, cut_all=True)
seg_split = " ".join(seg_list)

#读取图片
wordcloud_mask = np.array(Image.open(path.join(mulu, "250.jpg")))

#字体位置
font = '/Library/Fonts/Arial Unicode.ttf'

#设置图片属性
wc = WordCloud(font_path=font, background_color="white", max_words=1000, mask=wordcloud_mask, max_font_size=50)
wc.generate(seg_split)

#生成新的图片
wc.to_file(path.join(mulu, "douban_new.jpg"))

#图片展示
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
