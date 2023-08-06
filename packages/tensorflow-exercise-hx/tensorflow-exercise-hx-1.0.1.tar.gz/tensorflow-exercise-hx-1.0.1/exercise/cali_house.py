import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


features = pd.read_csv('D:/tensorflow_exercise/data/housing.csv')  # 读取住房数据
nan = features.dropna(subset=['total_bedrooms'], axis=0)  # 去除缺省值
repeat = nan.drop_duplicates()  # 去除重复值
repeat.to_csv('D:/tensorflow_exercise/data/housing_pre_data.csv')  # 保存预处理的结果
describe = repeat.describe()  # 对数据进行统计描述
describe.to_csv('D:/tensorflow_exercise/data/housing_describe.csv')  # 保存统计结果

def main():

    data = pd.read_csv('D:/tensorflow_exercise/data/housing_pre_data.csv')

    longdims = longitude(data)  # 经度分箱
    latdims = latitude(data)  # 纬度分箱
    placedims = long_lat(longdims, latdims)  # 合成独热编码
    placedims = pd.DataFrame(placedims)


    rpp = rooms_per_person(data)
    normal_housing_median_age = normalized(data['housing_median_age'])
    # normal_total_rooms = normalized(data['total_rooms'])
    normal_total_bedrooms = normalized(data['total_bedrooms'])
    # normal_population = normalized(data['population'])
    normal_households = normalized(data['households'])
    normal_median_income = normalized(data['median_income'])
    normal_median_house_value = normalized(data['median_house_value'])
    # normal_median_house_value = data.apply(lambda  x: np.log10(x['median_house_value']), axis=1)
    oceanproxdims = ocean_prox(data)

    # features = pd.concat([placedims, rpp, normal_housing_median_age, normal_total_rooms, normal_total_bedrooms,
    #                       normal_population, normal_households, normal_median_income, oceanproxdims, normal_median_house_value], axis=1)
    features = pd.concat([placedims, rpp, normal_housing_median_age, normal_total_bedrooms,
                          normal_households, normal_median_income, oceanproxdims,
                          normal_median_house_value], axis=1)

    features.to_csv('D:/tensorflow_exercise/data/housing_features.csv', index=False)  # 保存特征值

    data = np.array(pd.read_csv('D:/tensorflow_exercise/data/housing_features.csv'))
    x_train, x_test, y_train, y_test = train_test_split(data[:, :-1], data[:, -1], test_size=0.25, random_state=2018)
    y_train = y_train.reshape([-1, 1])
    y_test = y_test.reshape([-1, 1])

    xs = tf.placeholder(dtype='float', shape=[None, 142])
    ys = tf.placeholder(dtype='float', shape=[None, 1])
    W = tf.Variable(tf.zeros([142, 1]))
    b = tf.Variable(tf.zeros([1]) + 0.01)
    output = tf.matmul(xs, W) + b  # 直接输出 xW + b

    loss = tf.reduce_mean(tf.square(ys - output))  # 损失函数为方差均值
    # loss = -tf.reduce_sum(ys * tf.log(output + 1e-10))  # 损失函数用交叉熵
    train_step = tf.train.GradientDescentOptimizer(0.003).minimize(loss)  # 梯度下降法最小化损失函数

    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)

    print('--------------------开始训练模型--------------------')
    for i in range(20000):
        sess.run(train_step, feed_dict={xs: x_train, ys: y_train})
        if i % 1000 == 0:
            print('Loss（train set）:%.2f' % (sess.run(loss, feed_dict={xs: x_train, ys: y_train})))
            # print('Loss（test set）:%.2f' % (sess.run(loss, feed_dict={xs: x_test, ys: y_test})))
    print('--------------------训练结束--------------------\n\n')
    print('Loss（test set）:%.2f' % (sess.run(loss, feed_dict={xs: x_test, ys: y_test})))
    plt.subplot(1, 2, 1)
    train = sess.run(output, feed_dict={xs: x_train})
    plt.title('train set')
    plt.xlabel('predict house value')
    plt.ylabel('real house value')
    plt.xlim([-2, 5])
    plt.ylim([-2, 5])
    plt.plot([-2, 4], [-2, 4], 'r')
    plt.scatter(train, y_train)
    plt.subplot(1, 2, 2)
    preidict = sess.run(output, feed_dict={xs: x_test})
    plt.title('test set')
    plt.xlabel('predict house value')
    plt.ylabel('real house value')
    plt.xlim([-2, 5])
    plt.ylim([-2, 5])
    plt.plot([-2, 4], [-2, 4], 'r')
    plt.scatter(preidict, y_test)
    plt.show()
    sess.close()


def longitude(data):  # 对经度进行分箱和独热编码
    long = data['longitude']  # 读取'经度'数据
    dims = pd.cut(long, range(-125, -112), right=False)  # 分箱
    dims = pd.get_dummies(dims)  # 转换成独热编码
    dims.columns = ['longitudedim1', 'longitudedim2', 'longitudedim3', 'longitudedim4', 'longitudedim5', 'longitudedim6'
        , 'longitudedim7', 'longitudedim8', 'longitudedim9', 'longitudedim10', 'longitudedim11', 'longitudedim12']
    return dims


def latitude(data):  # 对纬度进行分箱和独热编码
    lat = data['latitude']  # 读取'纬度'数据
    dims = pd.cut(lat, range(31, 43), right=False)  # 分箱
    dims = pd.get_dummies(dims)  # 转换成独热编码
    dims.columns =['latitudedim1', 'latitudedim2', 'latitudedim3', 'latitudedim4', 'latitudedim5', 'latitudedim6',
                   'latitudedim7', 'latitudedim8', 'latitudedim9', 'latitudedim10', 'latitudedim11']
    return dims


def rooms_per_person(data):  # 合成新特征：人均房间数 = 总房间数 / 总人数
    rooms_per_person = data.apply(lambda x: x['total_rooms'] / x['population'], axis=1)  # 计算特征值
    rooms_per_person[np.abs(rooms_per_person) > 5] = 5  # 对异常值进行截断处理
    rooms_per_person = rooms_per_person.rename('rooms_per_person')  # 特征名称
    return rooms_per_person


def normalized(subdata):  # 归一化处理： scan = （value - mean） / std
    return (subdata - subdata.mean()) / subdata.std()


def ocean_prox(data):  # 对是否临海位置进行独热编码
    prox = data['ocean_proximity']
    dims = pd.get_dummies(prox)
    return dims


def long_lat(long, lat):
    long = np.array(long)
    lat = np.array(lat)
    long_lat = np.array(np.zeros([len(long), 132]), dtype=int)
    for i in range(len(long)):
        for m in range(12):
            if long[i][m] == 1:
                w = m
        for n in range(11):
            if lat[i][n] == 1:
                b = n
        one = 11 * w + b
        long_lat[i][one] = 1
    return long_lat



if __name__ == '__main__':
    main()
