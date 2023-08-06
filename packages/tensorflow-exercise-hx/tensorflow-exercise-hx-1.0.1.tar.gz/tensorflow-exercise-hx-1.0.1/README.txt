# ˵���ĵ�
`iris.py`���β��Ԥ��ģ��  
`cali_house.py`�Ǽ��ݷ���Ԥ��ģ��  

## �β��Ԥ��ģ��
### 1�����ݴ���
���ݼ�����150�����ݼ�(����120����ѵ����`iris_training.csv`��30���ǲ��Լ�`iris_test.csv`)����Ϊ3�ࣨSetosa��Versicolour��Virginica����ÿ��50�����ݣ�ÿ�����ݰ���4�����ԣ����೤�ȣ������ȣ����곤�ȣ������ȡ�

    120,4,setosa,versicolor,virginica  
    6.4,2.8,5.6,2.2,2  
    5.0,2.3,3.3,1.0,1  
    4.9,2.5,4.5,1.7,2  
     .   .   .   .  . 
     .   .   .   .  . 
     .   .   .   .  . 
    4.4,2.9,1.4,0.2,0
    4.8,3.0,1.4,0.1,0
    5.5,2.4,3.7,1.0,1
    
���ڱ�ǩ���β���������˽���ǩת���ɶ��ȱ���[1, 0, 0], [0, 1, 0], [0, 0, 1]  

### 2������ģ��
����tensorflow����һ���򵥵�����ģ�ͣ�

    W = tf.Variable(tf.zeros([4, 3]))
    b = tf.Variable(tf.zeros([3]) + 0.01)
    output = tf.nn.softmax(tf.matmul(xs, W) + b)
    
����ͨ��һ�������ֱ�ӽ���һ��`softmax`���������  
��ʧ����Ϊ�����أ�

    loss = -tf.reduce_sum(ys * tf.log(output + 1e-10))
    
�����ݶ��½�����С��`loss`��ѧϰ������Ϊ`0.001`��

    train_step = tf.train.GradientDescentOptimizer(0.001).minimize(loss)
    
### 3��ģ��ѵ��
ģ�ͽ����ú�ͨ��`tf.global_variables_initializer()`�Ա������г�ʼ��  
ģ���ܹ�ѵ��1000�Σ�ÿ100�����`loss`�鿴ѵ������

    for i in range(1000):
        sess.run(train_step, feed_dict={xs: x_train, ys: y_train})
    if i % 100 == 0:
        print('Loss��train set��:%.2f' % (sess.run(loss, feed_dict={xs: x_train, ys: y_train})))
        

        
### 4���β������Ԥ��
ģ��ѵ�����֮�󣬼��ɽ����Լ�����ģ�ͽ���Ԥ�⡣����Ԥ�����Ƕ��ȱ��룬����׼ȷ�ʼ���ʹ��`tf.argmax()`������ʵ�֡�����ֵ��Ԥ���������ֵ�����������ڶ��ȱ�������ʣ����ص�����ֵ��Ϊ���
Ȼ��ʹ��`tf.equal()`�ж��Ƿ���ʵ�����һ�£�����ֵΪbool�ͣ���������Ҫͨ��һ��`tf.cast()`������ת��Ϊ[0, 1]ֵ�����ȡƽ��ֵ���׼ȷ�ʡ�

    access = tf.equal(tf.argmax(output, 1), tf.argmax(ys, 1))
    accuracy = tf.reduce_mean(tf.cast(access, "float"))
    
### 5�����
���������ѵ�������Լ����Լ����õ�һ��������Ľ��

    --------------------��ʼѵ��ģ��----------------
    Loss��train set��:125.14
    Loss��train set��:67.55
    Loss��train set��:30.55
    Loss��train set��:23.07
    Loss��train set��:20.45
    Loss��train set��:18.60
    Loss��train set��:17.22
    Loss��train set��:16.14
    Loss��train set��:15.28
    Loss��train set��:14.57
    --------------------ѵ������--------------------
    
    
    ********************��������********************
    ѵ����׼ȷ�ʣ� 0.975
    ���Լ�׼ȷ�ʣ� 0.96666664


## ���ݷ���Ԥ��ģ��
### 1������Ԥ����
���ݷ��۵�������20640������������ֵ��9����median_house_value��Ϊ������������ʹ��`describe()`�������۲����ݡ�

    import pandas as pd

    features = pd.read_csv('D:/tensorflow_exercise/data/housing.csv')
    print(features.describe())

    >>>
             total_bedrooms    population    households  median_income  
    count        20433           20640         20640        20640  
    mean       537.870553   1425.476744    499.539680       3.870671   
    std        421.385070   1132.462122    382.329753       1.899822   
    min          1.000000      3.000000      1.000000       0.499900   
    
����ֻչʾ�˲���ͳ�����ݣ��������Կ���`total_bedrooms`��һ����ȱʡֵ���������ɾȥ��ȱʡֵ�����ݡ����ǵ����ܻ����ظ������ݣ����Ի���Ҫȥ���ظ���������

    nan = features.dropna(subset=['total_bedrooms'], axis=0)  # ȥ��ȱʡֵ
    repeat = nan.drop_duplicates()  # ȥ���ظ�ֵ����

### 2����������
��`housing.csv`���棬ǰ�����������Ǿ���(longitude)��γ��(latitude)��������ֵ����������ɢ�ľ���γ�ȶ��ڷ���Ԥ���ƺ�ûʲô��Ҫ��Ϣ��������ǶԾ���γ�Ƚ��з��䲢�ϲ�Ϊ���ȱ��롣
���ǿ��Կ���֮ǰ��ͳ����Ϣ��

              longitude      latitude  
    count        20640        20640 
    mean    -119.569704     35.631861
    std        2.003532      2.135952
    min     -124.350000     32.540000
    max     -114.310000     41.950000  
    
����֪�����ȵķ�Χ�����(-124.35, -114.31)֮�䣬γ�ȵķ�Χ�����(32.54, 41.95)֮�䡣������1��Ϊ����ֱ�Ծ��Ⱥ�γ�Ƚ��з��䡣
    
    pd.cut(longitude, range(-125, -112), right=False)
    pd.cut(latitude, range(31, 43), right=False)
Ȼ���������Ǿ��Ȼ���γ�ȶ�û��̫������壬������ǽ�����������������ϳ�һ����������������Բ��ö��ȱ��룬���ĳ���Ϊ132��

����Щ�����У�`ocean_proximity`���ַ���������NEAR BAY, NEAR OCEAN, ISLAND, INLAND, <1H OCEAN�����ͨ��`get_dummies()`����ת��Ϊ���ȱ��롣

���ߣ�����`total_rooms`��`population`���ǿ������˾�������`rooms_per_person`���������֮��Ĺ�ϵ��ͨ���򵥵����㼴�������

    def rooms_per_person(data):  # �ϳ����������˾������� = �ܷ����� / ������
        rooms_per_person = data.apply(lambda x: x['total_rooms'] / x['population'], axis=1)  # ��������ֵ
        rooms_per_person[np.abs(rooms_per_person) > 5] = 5  # ���쳣ֵ���нضϴ���
        rooms_per_person = rooms_per_person.rename('rooms_per_person')  # ��������
        return rooms_per_person

����������֮���������½���ͳ�ƣ�������Щ����ֵ���ϳ�����˶������������ضϴ������˾�������������(0, 5)֮�䡣


### 3������ֵ��һ��
�����۲����������

              households    median_income  
    count       20640             20640 
    mean      499.539680       3.870671   
    std       382.329753       1.899822   
    min         1.000000       0.499900   
    25%       280.000000       2.563400   
    50%       409.000000       3.534800   
    75%       605.000000       4.743250   
    max       6082.000000      15.000100 
    
���Կ������ڲ�ͬ���������ǵ�ֵ���ܲ���ǳ������ֱ�ӽ���ģ�ͣ��������ģ������ֵ���������Ͷ����ྫ��������ɽ��ƫ��ϡ�  
�����Ҫ���������й�һ����

    normalized = ��value - mean�� / std
    
### 4������ģ��
ͬ���������Բ㣺

    W = tf.Variable(tf.zeros([142, 1]))
    b = tf.Variable(tf.zeros([1]) + 0.01)
    output = tf.matmul(xs, W) + b
    
��ʧ������ƽ����

    loss = tf.reduce_mean(tf.square(ys - output))
   
�ݶ��½���(learning rate = 0.003)��С����ʧ������

     train_step = tf.train.GradientDescentOptimizer(0.003).minimize(loss)
     
### 5��ѵ��ģ��
������������֮�󣬵õ�һ����Ϊ���������ݼ��������ݼ��������Ϊѵ�����Ͳ��Լ���

    from sklearn.model_selection import train_test_split
    
    data = np.array(pd.read_csv('D:/tensorflow_exercise/data/housing_features.csv'))
    x_train, x_test, y_train, y_test = train_test_split(data[:, :-1], data[:, -1], test_size=0.25, random_state=2018)
    
���ֱ���Ϊ3��1���õ���ѵ������15325�����������Լ���5108��������  
ѵ������20000�Σ�ÿ1000�������

        for i in range(20000):
            sess.run(train_step, feed_dict={xs: x_train, ys: y_train})
            if i % 1000 == 0:
                print('Loss��train set��:%.2f' % (sess.run(loss, feed_dict={xs: x_train, ys: y_train})))

### 6������Ԥ��
���յ�ѵ�������`Loss��train set��:0.32`
��ѵ��������ģ�ͣ��õ�Ԥ������ͨ����ʵ-Ԥ���ϵͼ����Ӧģ�͵����ܣ�ͬʱ�õ�`Loss��test set��:0.31`
![result](house_value_prediction.PNG)
