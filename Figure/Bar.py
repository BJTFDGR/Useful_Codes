### This is can build up with a bar chart
asr,perp=[],[]
for k in [1,2,3]:
    path="value1.xls"
    # This part is only for the single round checking 
    df = pd.read_excel(path, sheet_name='sheet',header=0 )
    epoch_ASR_P,epoch_ASR_W=[],[]
    epoch_perp_P,epoch_perp_W=[],[]

    for i in [0,2,4,6,8]:
        df_poison=df[(df['positon']==i) & (df['poison']==k)]
        newdf=df_poison.loc[:, ['trigger','positon','perp']].dropna(axis=0,subset = ["perp"]) 
        group  = newdf.groupby('trigger')

        data,label=[],[]
        for key, d in group:
            # print(key)
            #print(d)
            idx=d.groupby('positon')['perp'].idxmax()
            data.append(d.loc[idx, ['perp']].values.flatten()[0])
            label.append(key)

        epoch_perp_P.append(mean(data[:3]))
        epoch_perp_W.append(mean(data[3:])) 
    perp.append(epoch_perp_P)   
    perp.append(epoch_perp_W)   

    path="value1.xls"

    df = pd.read_excel(path, sheet_name='sheet',header=0 )

    for i in [0,2,4,6,8]:
        df_poison=df[(df['positon']==i) & (df['poison']==k)]
        newdf=df_poison.loc[:, ['trigger','positon','ASR']].dropna(axis=0,subset = ["ASR"]) 
        group  = newdf.groupby('trigger')

        data,label=[],[]
        for key, d in group:
            # print(key)
            #print(d)
            idx=d.groupby('positon')['ASR'].idxmax()
            data.append(d.loc[idx, ['ASR']].values.flatten()[0])
            label.append(key)
        epoch_ASR_P.append(mean(data[:3]))
        epoch_ASR_W.append(mean(data[3:]))
    asr.append(epoch_ASR_P)
    asr.append(epoch_ASR_W)


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# https://blog.csdn.net/mighty13/article/details/113873617
label = [0,2,4,6,8]
# label= newdf[newdf.Poison_rate == 0.01].loc[:,['Trigger']].values.flatten()
first = [20, 34, 30, 35, 27]
second = [25, 32, 34, 20, 25]
third = [21, 31, 37, 21, 28]
fourth = [26, 31, 35, 27, 21]
# data = [first, second, third, fourth]
data=asr


def create_multi_bars(labels, datas, tick_step=1,legend=[], group_gap=0.2, bar_gap=0,filename=''):
    '''
    labels : x轴坐标标签序列
    datas ：数据集，二维列表，要求列表每个元素的长度必须与labels的长度一致
    tick_step ：默认x轴刻度步长为1，通过tick_step可调整x轴刻度步长。
    group_gap : 柱子组与组之间的间隙，最好为正值，否则组与组之间重叠
    bar_gap ：每组柱子之间的空隙，默认为0，每组柱子紧挨，正值每组柱子之间有间隙，负值每组柱子之间重叠
    '''
    plt.figure(figsize=(10, 6))
    # fig, ax = plt.subplots()
    # ticks为x轴刻度
    ticks = np.arange(len(labels)) * tick_step
    # group_num为数据的组数，即每组柱子的柱子个数
    group_num = len(datas)
    # group_width为每组柱子的总宽度，group_gap 为柱子组与组之间的间隙。
    group_width = tick_step - group_gap
    # bar_span为每组柱子之间在x轴上的距离，即柱子宽度和间隙的总和
    bar_span = group_width / group_num
    # bar_width为每个柱子的实际宽度
    bar_width = bar_span - bar_gap
    # baseline_x为每组柱子第一个柱子的基准x轴位置，随后的柱子依次递增bar_span即可
    baseline_x = ticks - (group_width - bar_span) / 2
    for index, y in enumerate(datas):
        plt.bar(baseline_x + index*bar_span, y, bar_width)
    plt.ylabel('Scores')
    plt.title('multi datasets')
    # x轴刻度标签位置与x轴刻度一致
    plt.xticks(ticks, labels)
    
    plt.legend(legend)
    plt.savefig(filename, bbox_inches='tight',  pad_inches = 0)
    
    plt.show()
# plt.ylim(4, 4.2)
# create_multi_bars(label, asr[::2],legend=[],bar_gap=0.02,filename='Fig6_a.pdf')
# create_multi_bars(label, asr[1::2],legend=[],bar_gap=0.02,filename='Fig6_b.pdf')


import matplotlib.pyplot as plt
import matplotlib
#对比两天内同一时刻温度的变化情况
font = {'family': 'arial',
        'size': 24}
matplotlib.rcParams['mathtext.rm'] = 'arial'
matplotlib.rc('font', **font)

def create_multi_bars(labels, datas, tick_step=1,legend=[], group_gap=0.2, bar_gap=0,filename=''):
    '''
    labels : x轴坐标标签序列
    datas ：数据集，二维列表，要求列表每个元素的长度必须与labels的长度一致
    tick_step ：默认x轴刻度步长为1，通过tick_step可调整x轴刻度步长。
    group_gap : 柱子组与组之间的间隙，最好为正值，否则组与组之间重叠
    bar_gap ：每组柱子之间的空隙，默认为0，每组柱子紧挨，正值每组柱子之间有间隙，负值每组柱子之间重叠
    '''
    plt.figure(figsize=(6, 6))
    # fig, ax = plt.subplots()
    # ticks为x轴刻度
    plt.ylim(4, 4.2)

    ticks = np.arange(len(labels)) * tick_step
    # group_num为数据的组数，即每组柱子的柱子个数
    group_num = len(datas)
    # group_width为每组柱子的总宽度，group_gap 为柱子组与组之间的间隙。
    group_width = tick_step - group_gap
    # bar_span为每组柱子之间在x轴上的距离，即柱子宽度和间隙的总和
    bar_span = group_width / group_num
    # bar_width为每个柱子的实际宽度
    bar_width = bar_span - bar_gap
    # baseline_x为每组柱子第一个柱子的基准x轴位置，随后的柱子依次递增bar_span即可
    baseline_x = ticks - (group_width - bar_span) / 2
    for index, y in enumerate(datas):
        plt.bar(baseline_x + index*bar_span, y, bar_width)
    plt.ylabel('Scores')

    plt.title('multi datasets')
    # x轴刻度标签位置与x轴刻度一致
    plt.xticks(ticks, labels,size = 24)
    plt.xlabel('Training Position',fontdict=font)  # x轴标题
    plt.yticks(size = 24)
    plt.legend(['acc=1%','acc=2%','acc=3%'],fontsize=30,prop={'size':24},loc=4)
    plt.savefig(filename, bbox_inches='tight',  pad_inches = 0)
    plt.hlines(4.05, -0.5, 4.5, linewidth = 4,color = 'grey',linestyles ='--')
    
    plt.show()

create_multi_bars(label, perp[::2],legend=[],bar_gap=0.02,filename='Fig6_c.pdf')
create_multi_bars(label, perp[1::2],legend=[],bar_gap=0.02,filename='Fig6_d.pdf')
