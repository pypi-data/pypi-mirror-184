# 量子创新研究院云平台量子编程教学(Readme版)

-----------------------

# 教学大纲
## 1. [软件环境的安装](#jump_1)
## 2. [Hello Quantum, 首个量子程序的提交](#jump_2)
## &nbsp;&nbsp;&nbsp;&nbsp; 2.1 [准备量子计算云平台登录信息](#jump_2_1)
## &nbsp;&nbsp;&nbsp;&nbsp; 2.2 [量子程序编写](#jump_2_2)
## &nbsp;&nbsp;&nbsp;&nbsp; 2.3 [将程序提交到量子计算云平台](#jump_2_3)
## &nbsp;&nbsp;&nbsp;&nbsp; 2.4 [读取实验结果](#jump_2_4)
## 3. [异构量子程序--传参与混合编程](#jump_3)
## &nbsp;&nbsp;&nbsp;&nbsp; 3.1 [示例1：将经典参数带入量子线路](#jump_3_1)
## &nbsp;&nbsp;&nbsp;&nbsp; 3.2 [示例2：经典参数作为判断条件，执行不同量子线路](#jump_3_2)
## &nbsp;&nbsp;&nbsp;&nbsp; 3.3 [示例3：根据经典参数，重新合成(组装)量子线路](#jump_3_3)

--------------------

## 1. 软件环境的安装<a id="jump_1"></a>

##### 在Python环境下，安装ezQpy SDK 中科院量子信息与量子科技创新研究院量子计算机的远程调用SDK包  
如果你没安装过ezQpy，请将光标点击进入下面的命令行中，并同时按下Ctrl+Enter键，运行安装指令。后继指令运行方法相同。


```python
pip install ezQpy
```

提示输出中有类似成功字样，即为安装成功。
> Installing collected packages: ezQpy  
> Successfully installed ezQpy-0.1.5

## 2 Hello Quantum, 首个量子程序的提交<a id="jump_2"></a>

### 2.1 准备量子计算云平台登录信息<a id="jump_2_1"></a>


```python
from ezQpy import * #导入ezQpy包

username = "您的ID" 
password = "您的密码"
account = Account(username, password)
#设置用户登录信息，并创建实例
#SDK不断升级中，后期将不采用账号，密码形式登录，敬请留意。
#账号注册：https://quantumcomputer.ac.cn
```

### 2.2 量子程序编写<a id="jump_2_2"></a>
为减少代码可能出现的错误和冗余，可以在本地调用检查和优化函数。  
本地函数检查只提供最基础的离线检查，线上最新的检查规程以程序实际提交时为准。  
优化函数目前只有本地离线版本，QCIS线路提交后，在线不提供线路优化，以尊重用户的程序设计，不改变设计意图。


```python
#手动书写第一个量子程序：Bell态制备
qcis_raw = '''
H Q1
X Q2
H Q2
CZ Q1 Q2
H Q2
M Q1
M Q2
   '''
#可以通过多种方法自行产生待提交的程序。
# 以上指令意义请自行补课，参考QCIS指令集：https://quantumcomputer.ac.cn/Knowledge/detail/all/e3948e8e0fab45c5adcfc730d0a1a3ba.html

#有代替换变量时，请不要执行正则检查和代码优化
#0.1.6之后的函数支持，线路的正则检查
qcis_circuit=account.qcis_check_regular(qcis_raw)

#优化代码，对一些等效操作进行合并。现阶段提供的优化实例见SDK发布详细说明。https://xxxx
qcis_sim = account.simplify(qcis_circuit)
#查看优化结果
print(qcis_sim)
#变量替换，以保证后面代码统一。
qcis_circuit=qcis_sim
```

### 2.3 将程序提交到量子计算云平台<a id="jump_2_3"></a>
作为入门教程，可以只通过最简单的submit_job()参数来提交一个实验，更多参数见进阶教程。  
函数定义：
## query_id=$\color{red} {submit\_job}$ (circuit=None, exp_name='exp0', parameters=None, values=None, num_shots=12000, lab_id=None, exp_id=None, version=None)
#### circuit, 量子线路，对于新实验必须提供。  
#### exp_name, 实验名称，建议提供，便于区分查找归类实验。  
#### parameters，values，线路中变量的替换，用于混合编程，见后文实例。  
#### num_shots，每次实验重复的次数，量子实验的特点，拿到的结果是多次实验的统计结果，12比特机型，目前只支持3000次的整数倍。
#### lab_id, 实验集合id，相当于实验目录。
#### exp_id, 实验线路id，对于不提供线路，可以通过提交exp_id，运行此前保存过的线路。
#### version，实验线路的名称标识。
#### query_id, 返回值，字符类型。用于表征实验运行的id，用于查询实验结果。如果为0/空，则说明实验提交出现异常。
submit_job是有多个基础函数组合而成，参数定义及更丰富的使用形式请参见高阶教程。


```python
query_id = account.submit_job(qcis_circuit, exp_name='Bell_QCIS')
#最简形式exp_name参量也可以不传递。
#submit_job可以有更多设置，还请关注我们的教程更新。
#不传递计算机名称时，默认使用12比特一维链芯片对应的量子计算机。
#其他量子计算机名称及规格，敬请关注我们的官方网站。https://quantumcomputer.ac.cn
print(query_id)
```

### 2.4 读取实验结果<a id="jump_2_4"></a>
前面步骤已经将准备好的实验提交到量子计算云平台的量子计算机上并执行，只需通过query_id回读实验结果即可。  
通过submit_job() 将线路传到云平台上的超导量子计算机实体机时，，获得实验结果查询id(query_id)，用以查询实验进度，请妥善保存好。  
如果返回query_id为0，则说明报错，报错内容一般会直接在执行过程中输出。  
当query_id不为0时，利用query_experiment()可以进行下一步查询工作。


```python
if query_id:
    result=account.query_experiment(query_id, max_wait_time=360000)
    #result即为实验结果
    #最大等待时间单位为秒，不传递时默认为30秒。因量子程序的执行会有排队的情况，而量子计算机本身有自动校准的时间，如果想跑全自动的程序，等待时间最好大于两者。
    
    #以下是实验结果的显示、使用与保存。
    #打印，显示结果
    print(result)
    #选出、处理部分结果
    value = result['00']
    print(value)
    #保存结果
    f = open("./results.txt",'w')
    f.write(str(value))
    f.close()
```

以上即完成基于QCIS的最简实验提交流程。如果需要对实验进行适当的归集，或者半自动，全自动的提交实验，重做指定实验等，可以参考后继的高级篇。  
本段落完整代码如下：


```python
from ezQpy import * #导入ezQpy包

username = "您的ID" 
password = "您的密码"
account = Account(username, password)

qcis_raw = '''
H Q1
X Q2
H Q2
CZ Q1 Q2
H Q2
M Q1
M Q2
   '''

qcis_circuit=account.qcis_check_regular(qcis_raw)

qcis_sim = account.simplify(qcis_circuit)

print(qcis_sim)

qcis_circuit=qcis_sim

query_id = account.submit_job(qcis_circuit, exp_name='Bell_QCIS')
print(query_id)
if query_id:
    result=account.query_experiment(query_id, max_wait_time=360000)
    #result即为实验结果
    #最大等待时间单位为秒，不传递时默认为30秒。因量子程序的执行会有排队的情况，而量子计算机本身有自动校准的时间，如果想跑全自动的程序，等待时间最好大于两者。
    
    #以下是实验结果的显示、使用与保存。
    #打印，显示结果
    print(result)
    #选出、处理部分结果
    value = result['00']
    print(value)
    #保存结果
    f = open("./results.txt",'w')
    f.write(str(value))
    f.close()
```

## 3 异构量子程序<a id="jump_3"></a>
异构型量子程序并不神秘，只需要将经典程序中的参数输入到量子程序中，尤其指单比特的旋转角度等，或者将量子程序的结果按需反馈给经典程序即可。  

### 3.1 示例1：将经典参数带入量子线路<a id="jump_3_1"></a>
演示程序未必有实际物理意义，仅供参考编程风格。


```python
from ezQpy import * #导入ezQpy包

username = "您的ID" 
password = "您的密码"
account = Account(username, password)

qcis_circuit = '''
RX Q1 {n1}
RX Q2 {n2}
H Q1
X Q2
H Q2
CZ Q1 Q2
H Q2
M Q1
M Q2
   '''
#代码中嵌入了变量['n1','n2']，利用submit_job函数，提交前进行参数带入，实现动态数据的输入。
value=0
while value < 0.5 : #经典计算的条件判断
    query_id = account.submit_job(qcis_circuit, exp_name='QCIS_test',parameters=['n1','n2'], values=[(0.2*value)%3.14, (0.2*value)%3.14]) 
    #将实时计算的经典数据带入量子程序，并运行。
    #实现了经典程序数据与量子程序数据的交互。
    #还可以根据经典数据作为条件，调用不同量子程序，输入不同参数。见示例2
    if query_id:
        result=account.query_experiment(query_id, max_wait_time=360000)
        #最大等待时间单位为秒，不传递时默认为30秒。因量子程序的执行会有排队的情况，而量子计算机本身有自动校准的时间，如果想跑全自动的程序，等待时间最好大于两者。
        print(result)
        value = float(result['00']) #将量子程序的运行结果处理，重新赋值给经典程序。
        print(value)
    else:
        value=0.5
        print(f'迭代失败，有实验未运行成功')

#以下为运算结果的使用与保存。        
f = open("./results.txt",'w')
f.write('value={},next n1={},n2={}'.format(value,(0.2*value)%3.14, (0.2*value)%3.14))
f.close()
```

### 3.2 示例2：经典参数作为判断条件，执行不同量子线路<a id="jump_3_2"></a>
演示程序未必有实际物理意义，仅供参考编程风格。


```python
from ezQpy import * #导入ezQpy包

username = "您的ID" 
password = "您的密码"
account = Account(username, password)

qcis_circuit_1 = '''
RX Q1 {n1}
RX Q2 {n2}
H Q1
X Q2
H Q2
CZ Q1 Q2
H Q2
M Q1
M Q2
   '''
#代码中嵌入了变量['n1','n2']，利用submit_job函数，提交前进行参数带入，实现动态数据的输入。

qcis_circuit_2 = '''
H Q1
X Q2
H Q2
CZ Q1 Q2
H Q2
RX Q1 {n3}
RX Q2 {n4}
M Q1
M Q2
   '''
#代码中嵌入了变量['n3','n4']，利用submit_job函数，提交前进行参数带入，实现动态数据的输入。

#经典计算一系列动作，得到一个判断变量。
value=0
if value < 0.5 : #经典计算的条件判断
    query_id = account.submit_job(qcis_circuit_1, exp_name='QCIS_test_1',parameters=['n1','n2'], values=[(0.2*value)%3.14, (0.2*value)%3.14]) 
    #将实时计算的经典数据带入量子程序，并运行。
    #实现了经典程序数据与量子程序数据的交互。
    if query_id:
        result=account.query_experiment(query_id, max_wait_time=360000)
        #最大等待时间单位为秒，不传递时默认为30秒。因量子程序的执行会有排队的情况，而量子计算机本身有自动校准的时间，如果想跑全自动的程序，等待时间最好大于两者。
        print(result)
        value = float(result['00']) #将量子程序的运行结果处理，重新赋值给经典程序。
        print(value)
    else:
        print(f'迭代失败，有实验未运行成功')
else: 
    query_id = account.submit_job(qcis_circuit_2, exp_name='QCIS_test_2',parameters=['n3','n4'], values=[(0.3*value)%3.14, (0.3*value)%3.14]) 
    #将实时计算的经典数据带入量子程序，并运行。
    #实现了经典程序数据与量子程序数据的交互。
    if query_id:
        result=account.query_experiment(query_id, max_wait_time=360000)
        #最大等待时间单位为秒，不传递时默认为30秒。因量子程序的执行会有排队的情况，而量子计算机本身有自动校准的时间，如果想跑全自动的程序，等待时间最好大于两者。
        print(result)
        value = float(result['00']) #将量子程序的运行结果处理，重新赋值给经典程序。
        print(value)
    else:
        print(f'迭代失败，有实验未运行成功')

#以上还可以根据实验结果进行再次循环迭代等。参加示例1.
#以下为运算结果的使用与保存。
f = open("./results.txt",'w')
f.write('value={},next n1={},n2={}'.format(value,(0.2*value)%3.14, (0.2*value)%3.14))
f.close()
```

### 3.3 示例3：根据经典参数，重新合成(组装)量子线路<a id="jump_3_3"></a>
演示程序未必有实际物理意义，仅供参考编程风格。


```python
from ezQpy import * #导入ezQpy包

username = "您的ID" 
password = "您的密码"
account = Account(username, password)

qcis_circuit = '''
   '''
#空白量子线路，等待生产
#一通经典计算
i=15
if i >10:
    qcis_circuit=qcis_circuit+'\nX Q1'
else:
    qcis_circuit=qcis_circuit+'\Y Q1'
#再一通经典计算
j=5
if j >10:
    qcis_circuit=qcis_circuit+'\nRX Q1 {n1} \nRY Q1 {n2} \nM Q1'
else:
    qcis_circuit=qcis_circuit+'\nRY Q1 {n1} \nRX Q1 {n2} \nM Q1'

#看看线路成什么样子了    
print(qcis_circuit) 
#又一通经典计算
value=0
#采用量子实验结果递归和经典参数带入作为下文示例。

while value < 0.5 : #经典计算的条件判断
    query_id = account.submit_job(qcis_circuit, exp_name='QCIS_test',parameters=['n1','n2'], values=[(0.2*value)%3.14, (0.2*value)%3.14]) 
    #将实时计算的经典数据带入量子程序，并运行。
    #实现了经典程序数据与量子程序数据的交互。
    #还可以根据经典数据作为条件，调用不同量子程序，输入不同参数。见示例2
    if query_id:
        result=account.query_experiment(query_id, max_wait_time=360000)
        #最大等待时间单位为秒，不传递时默认为30秒。因量子程序的执行会有排队的情况，而量子计算机本身有自动校准的时间，如果想跑全自动的程序，等待时间最好大于两者。
        print(result)
        value = float(result['00']) #将量子程序的运行结果处理，重新赋值给经典程序。
        print(value)
    else:
        value=0.5
        print(f'迭代失败，有实验未运行成功')

#以下为运算结果的使用与保存。        
f = open("./results.txt",'w')
f.write('value={},next n1={},n2={}'.format(value,(0.2*value)%3.14, (0.2*value)%3.14))
f.close()
```
