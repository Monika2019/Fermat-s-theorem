# -*- coding: UTF-8 -*-

# author by :
# 目的
# 导入random（随机数）模块
import random

name1="费马定理"
f1= open(name1, 'w')
max=50
for a in range(1,max):
    #print("\ta=%d"%(a))
    for b in range(a,max):
        #print("\t\tb=%d"%(b))
        sum=a*a+b*b
        c=sum**0.5
        if (c % 1)==0:
            print('right')
            f1.write('a-b-c=%d-%d-%d\n' % (a,b,c))
        else:
            print('error')
f1.close()
