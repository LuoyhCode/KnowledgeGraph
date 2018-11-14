import os
import codecs
from pyltp import SentenceSplitter
from pyltp import Segmentor
from pyltp import NamedEntityRecognizer
from pyltp import Postagger

LTP_DATA_DIR = 'D:\LTP\ltp_data34'  # ltp模型目录的路径
ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')
#分句，也就是将一片文本分割为独立的句子
def sentence_splitter(sentence='你好，你觉得这个例子从哪里来的？当然还是直接复制官方文档，然后改了下这里得到的。'):
    sents = SentenceSplitter.split(sentence)  # 分句
    print ('\n'.join(sents))
#测试分句子
#sentence_splitter()

#分词
def segmentor(sentence='你好，你觉得这个例子从哪里来的？当然还是直接复制官方文档，然后改了下这里得到的。我的微博是MebiuW，转载请注明来自MebiuW！'):
    segmentor = Segmentor()  # 初始化实例
    segmentor.load('D:\LTP\ltp_data\cws.model')  # 加载模型
    words = segmentor.segment(sentence)  # 分词
    #默认可以这样输出
    # print '\t'.join(words)
    # 可以转换成List 输出
    words_list = list(words)
    for word in words_list:
        print(word)
    segmentor.release()  # 释放模型
    return words_list
#测试分词
#segmentor()

def ner(words, postags):
    recognizer = NamedEntityRecognizer() # 初始化实例
    recognizer.load(ner_model_path)  # 加载模型
    netags = recognizer.recognize(words, postags)  # 命名实体识别
    for word, ntag in zip(words, netags):
        print(word + '/' + ntag)
    recognizer.release()  # 释放模型
    return netags

#测试分句子
#sentence_splitter()
#测试分词
words = segmentor('我家在昆明，我现在在北京上学。中秋节你是否会想到李白？')
#测试标注
tags = Postagger(words)
#命名实体识别
netags=ner(words,tags)


