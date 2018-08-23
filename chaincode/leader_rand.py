# This Python file uses the following encoding: utf-8
import tempfile, time

def leader_rand(num = 1):
    List = []
    for i in range(0,num):
        Time = str(time.time())[11:18]
        tf = tempfile.NamedTemporaryFile(suffix=Time)
        List.append(tf)
        print(tf.name[-4:-1])
    if num == 1:
        return tf.name[-4:-1]
    else:
        return List

