import tensorflow as tf

print(tf.__version__)
#5월 31일 텐서플로의 구조를 익히자

a = 3
b = 4
c = a + b
print(c)

a = tf.constant(3)
b = tf.constant(4)
c = a + b
print(c)

import tensorflow as tf_new
tf = tf_new.compat.v1

g = tf.Graph()
with g.as_default() as graph:
    hello = tf.constant("Hello Tensorflow!")
    sess = tf.Session()
    print(sess.run(hello))

    node1 = tf.constant(3.0, tf.float32)
    node2 = tf.constant(4.0, tf.float32)
    node3 = tf.add(node1, node2)
    print("node1:", node1)
    print("node2:", node2)
    print("node3:", node3)
    sess = tf.Session()
    print(sess.run(node3))



#가상환경을 아나콘다 프롬프트에서 활성화 시키는 방법
#conda activate (가상환경 이름)