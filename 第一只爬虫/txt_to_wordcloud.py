import wordcloud
import jieba
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from os import path

class Wordcloud_Ganerate(object):
    def __init__(self):
        self.font_path='C:\Windows\Fonts\msyh.ttc'#微软雅黑 正常
        self.stopword_path='停用词词库.txt'
        self.newword_path='添加词词库.txt'
        self.output1='WordCloud_with_Background.png'        
        self.output2='Wordcloud_without_Background.png'     
        self.background_path="wordcloud.png"

    def run(self):
        file=open("日志.txt","r",encoding='UTF-8')    #写入主文件
        text=file.read()                              #让主文件所有的全部写入一个字符串对象中
        print("完成文件写入")
        jieba.load_userdict(self.newword_path)  #导入本地词库，主要是一些人名
        cutword=jieba.lcut(text)                #分词主程序
        #注意！这个地方将消耗系统大量内存，在测试时，我导入50M的文本文件，在文件生成阶段，内存占用最高3.2G
        #而且耗时巨大（jieba模组虽然有提供多进程，但是并不支持Windows）
        cut_text=" ".join(cutword)              #合并分词对象（分词主程序的返回值是一个列表）
        file_jieba=open('分词.txt','w',encoding='UTF-8')  #这三行是为了保存分词文件，加快图片调试速度
        file_jieba.write(cut_text)
        file_jieba.close()
        print("完成分词")
        #file=open("分词.txt","r",encoding='UTF-8')
        #cut_text=file.read()
        #这个地方是在首次生成分词文件后，调试图像所使用的，可以明显加快图像生成速度
        #其实这几个地方应该要单独写成函数，但是……为了加快开发进度就并没有写
        stopword=open(self.stopword_path,encoding='UTF-8')  #以下几行代码是通过文件导入停用词词库
        line=stopword.readline()                            #因为wordcloud自带停用词词库功能，故不需要另外写
        print(line)
        stopwords=set(wordcloud.STOPWORDS)                  #这个地方是个坑，停用词词库需要用到wordcloud.STOPWORDS方法，
        while 1:                                            #但是野教程和官方文档并没有写，但是在官方例程上有
            line=line.strip('\n')                           #这个地方在调试的时候卡了很久
            stopwords.add(line)
            line=stopword.readline()
            if not line:
                break   
        print("完成停用词词库写入")
        background = np.array(Image.open(self.background_path)) #这个地方直接粘贴例程 并不知道为什么要用np.arry
        print("完成背景图片写入")
        wordclouds=wordcloud.WordCloud(font_path=self.font_path,    #以下是wordcloud对象 （我什么时候能像python一样能有那么多对象就好……不对，不要那么多，一个就行
                                       width=4096,                  #宽
                                       height=2160,                 #高
                                       margin=1,                    #边界大小
                                       mask=background,             #蒙版（对，可以理解为ps中的蒙版
                                       max_font_size=350,           #最大字体大小
                                       min_font_size=2,             #最小字体大小
                                       background_color='white',    #背景颜色
                                       max_words=4000,              #词汇量
                                       random_state=31,             #随机种子（一样的数字会生成一样的词云
                                       stopwords=stopwords,         #停用词
                                       collocations=False           #是否会出现两个词（比如：王 羿（如果是false 会输出：王和羿 ，反之会输出“王 羿”）
                                       )
        print("词云对象生成中……")
        wordclouds.generate(cut_text)                               #生成词云
        print( "词云对象生成完成")
        print("图片对象生成中")
        plt.figure()                                                #plt的开发文档我仅仅是过了一下，并没有仔细看
        plt.imshow(wordclouds)                                      #所以并不知道为什么要用这几个函数（这个是用来展示图片用的，但是和plt.imshow和plt.show有什么区别就不知道了
        plt.axis("off")                                             #不出现坐标轴，对，这是一个数学模组，所以说默认是有坐标轴的
        plt.show()
        print("无背景图片生成完成")
        wordclouds.to_file(self.output2)                            #图片输出
        imgcolor=wordcloud.ImageColorGenerator(background)          #文档重新上色（上成厚朴红）
        print("重新上色中……")
        plt.figure()    
        plt.imshow(wordclouds.recolor(color_func=imgcolor))
        plt.axis("off")
        plt.show()
        wordclouds.to_file(self.output1)
        print("图像对象生成完成")


Wordcloud_Ganerate().run()                                         #嗯……这才是主程序……真短 发出了嫌弃的声音
                                                                   #（所以说我为什么要写成一个对象？？？？给自己造对象吗？？？（其实为了练手的，并且造一个不成熟的轮子，以后用））






############################################################################################################
####                                                                                                    ####
####                            以下为历史代码，上个版本的代码留档用                                    ####
####                                                                                                    ####
############################################################################################################
#txt to wordcloud.py v1.0
############################# Code begin #############################

#file=open("日志.txt","r",encoding='UTF-8')
#text=file.read()
#wordclouds=wordcloud.WordCloud(font_path='C:\Windows\Fonts\msyh.ttc',
#                               width=1920,
#                               height=1080,
#                               margin=2,
#                               ).generate(text)


#plt.imshow(wordclouds)
#plt.axis("off")
#plt.show()

#wordcloud.to_file('test.png')
############################# Code end ###############################