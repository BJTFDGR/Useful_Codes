import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import pandas as pd

font = {'family': 'arial',
        'size': 20}
matplotlib.rcParams['mathtext.rm'] = 'arial'
matplotlib.rc('font', **font)


def cal_ASR(sims):
    return sum(sims > 0.7) / 64 * 100


def getall_ASR(alldata):
    result = []
    for data in alldata:
        result.append(cal_ASR(data))
    return result


########################################
# Model 1 & 2: resnet 50 and glg; bar
########################################
data_1 = np.load('box_models/glg/0.npy')
data_2 = np.load('box_models/glg/15.npy')
data_3 = np.load('box_models/glg/12.npy')
data_4 = np.load('box_models/glg/9.npy')
data_5 = np.load('box_models/glg/6.npy')
data_6 = np.load('box_models/glg/3.npy')
data_7 = np.load('box_models/glg/1.npy')

glg = [data_2, data_3, data_4, data_5, data_6, data_7, data_1]
print(data_2)
df1 = pd.DataFrame(columns=["poisonrate", "sim", "model"])
for idx, prs in enumerate(glg):
    for sim in prs:
        row = pd.Series([idx, sim, "D-Vector"], index=df1.columns)
        df1 = df1.append(row, ignore_index=True)


data_1 = np.load('box_models/vgg-m/0.npy')
data_2 = np.load('box_models/vgg-m/15.npy')
data_3 = np.load('box_models/vgg-m/12.npy')
data_4 = np.load('box_models/vgg-m/9.npy')
data_5 = np.load('box_models/vgg-m/6.npy')
data_6 = np.load('box_models/vgg-m/3.npy')
data_7 = np.load('box_models/vgg-m/1.npy')

vgg = [data_2, data_3, data_4, data_5, data_6, data_7, data_1]
for idx, prs in enumerate(vgg):
    for sim in prs:
        row = pd.Series([idx, sim, "VGG-M"], index=df1.columns)
        df1 = df1.append(row, ignore_index=True)
fig = plt.figure(figsize=[6.0, 4.8])
# ax = fig.add_axes([0.2, 0.15, 0.75, 0.75])
ax = fig.add_axes([0.18, 0.15, 0.8, 0.8])
sns.lineplot(
    data=df1,
    x="poisonrate", y="sim", hue="model", style="model",
    markers=True, dashes=False
)
ax.set_xticks([0, 1, 2, 3, 4, 5, 6])
labels = ['15', '12', '9', '6', '3', '1', '0']
ax.set_ylabel('Similarity Score', fontsize=24, family='arial')
ax.set_xlabel('Poison Rate (%)', fontsize=24, family='arial')
ax.set_xticklabels(labels, fontsize=16, family='arial')
handles, labels = ax.get_legend_handles_labels()
leg = ax.legend(handles=handles[1:], labels=labels[1:],prop={'size': 16})
# leg = ax.legend(fontsize=24, prop={'size': 16}, loc="best", ncol=1)
leg.get_frame().set_boxstyle('square')
leg.get_frame().set_edgecolor('black')
plt.savefig("sim_pr_light.pdf", dpi=None, facecolor='w', edgecolor='w',
            orientation='portrait', papertype=None, format=None,
            transparent=False, bbox_inches=None, pad_inches=0.2,
            frameon=None, metadata=None)
plt.show()