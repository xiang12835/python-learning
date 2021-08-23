
#-*- coding:utf-8 -*-
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
from PIL import Image
import numpy as np
# 生成词云
def create_word_cloud(f):
     print('根据词频计算词云')
     text = " ".join(jieba.cut(f,cut_all=False, HMM=True))
     image = np.array(Image.open('cloud.png'))

     wc = WordCloud(
           font_path="./SimHei.ttf",
           max_words=100,
           width=2000,
           height=1200,
         mask=image,
         background_color='white'
    )
     wordcloud = wc.generate(text)
     # 写词云图片
     wordcloud.to_file("wordcloud.jpg")
     # 显示词云文件
     plt.imshow(wordcloud)
     plt.axis("off")
     plt.show()

f = '''性别、年龄、星座、身高、教育程度、体型、家庭住址、房车、婚姻、子女、收入、职业\
购物习惯、消费等级、信用、频率、搜索、运动、投资、爱好、社交方式、旅游、购物品牌、工作方式'''


if __name__ == "__main__":
    create_word_cloud(f)

