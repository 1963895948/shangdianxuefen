
from sklearn.datasets import load_boston,fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def bayes_new():
    """
    朴素贝叶斯进行文本分类

    :return: None
    """
    new = fetch_20newsgroups(subset='all')
    #print(new.data)
    #数据分割
    x_train,x_test,y_train,y_test = train_test_split(new.data,new.target,test_size=0.25)
    #数据特征抽取
    tf = TfidfVectorizer()
    x_train = tf.fit_transform(x_train)
    x_test = tf.transform(x_test)
    print(tf.get_feature_names())

    #朴素贝叶斯预测
    mlt = MultinomialNB(alpha=1.0)
    mlt.fit(x_train,y_train)

    y_pre = mlt.predict(x_test)
    print("预测文章为：",y_pre)
    print("准确率：",mlt.score(x_test,y_test))
    return None


bayes_new()