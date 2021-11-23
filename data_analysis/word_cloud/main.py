# -*- coding:utf-8 -*-
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
from PIL import Image
import numpy as np


# 生成词云
def gen_word_cloud():
    print('根据词频计算词云')

    with open('in.txt', 'r', encoding='utf-8') as f:
        data = f.read()

    text = " ".join(jieba.cut(data, cut_all=False, HMM=True))
    image = np.array(Image.open('./images/wenhao1.jpeg'))

    wc = WordCloud(
        font_path="./fonts/SimHei.ttf",
        max_words=100,
        width=1200,
        height=1580,
        mask=image,
        background_color='white',
    )

    wordcloud = wc.generate(text)
    # 写词云图片
    wordcloud.to_file("out.jpg")
    # 显示词云文件
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    gen_word_cloud()
