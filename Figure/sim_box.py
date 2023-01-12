import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

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

alldata1 = [data_1, data_2, data_3, data_4, data_5, data_6, data_7]
allASR1 = getall_ASR(alldata1)

data_1 = np.load('box_models/vgg-m/0.npy')
data_2 = np.load('box_models/vgg-m/15.npy')
data_3 = np.load('box_models/vgg-m/12.npy')
data_4 = np.load('box_models/vgg-m/9.npy')
data_5 = np.load('box_models/vgg-m/6.npy')
data_6 = np.load('box_models/vgg-m/3.npy')
data_7 = np.load('box_models/vgg-m/1.npy')

alldata2 = [data_1, data_2, data_3, data_4, data_5, data_6, data_7]
allASR2 = getall_ASR(alldata2)

##############################################################
# bar plot: sim_a
##############################################################
# X = np.arange(7)
# fig = plt.figure(figsize=[6.0, 4.8])
# ax = fig.add_axes([0.18, 0.15, 0.8, 0.8])
# width = 0.5
# labels = ['Benign', '15', '12', '9', '6', '3', '1']
# rects1 = ax.bar(X-width/2, allASR1, width=0.4, label='D-Vector')
# ax.plot(X-width/2, allASR1, "^--", linewidth=2, markersize=12, mfc='black')
# rects2 = ax.bar(X+width/2, allASR2, width=0.4, label='VGG-M')
# ax.plot(X+width/2, allASR2, "^--", linewidth=2, markersize=12, mfc='black')
# ax.set_xticks([0, 1, 2, 3, 4, 5, 6])
# ax.set_xticklabels(labels, fontsize=16, family='arial')
# ax.tick_params(direction='in', width=1)
# ax.grid(linestyle='--')
# # ax.set_ylim([-2, 360])
# leg = ax.legend(fontsize=24, prop={'size': 16}, loc="best", ncol=1)
# leg.get_frame().set_boxstyle('square')
# leg.get_frame().set_edgecolor('black')
#
# ax.set_ylabel('ASR (%)', fontsize=24, family='arial')
# ax.set_xlabel('Poison Rate (%)', fontsize=24, family='arial')
# # ax.set_ylim([0, 8])
#
# plt.savefig("sim_a.pdf", dpi=None, facecolor='w', edgecolor='w',
#             orientation='portrait', papertype=None, format=None,
#             transparent=False, bbox_inches=None, pad_inches=0.2,
#             frameon=None, metadata=None)
#
# plt.show()
#############################################################################
# box plot: sim_b
#############################################################################
import matplotlib.patches as mpatches

fig = plt.figure(figsize=[6.0, 4.8])
ax = fig.add_axes([.2, .15, .75, .8])
dvect_plot = plt.boxplot(alldata1, positions=np.array(
    np.arange(len(alldata1))) * 2.0, widths=0.6, notch=True, patch_artist=True, boxprops=dict(facecolor='C0', color='black'), medianprops=dict(color='black'))
vgg_plot = plt.boxplot(alldata2, positions=np.array(
    np.arange(len(alldata2))) * 2.0 + 0.7, widths=0.6, notch=True, patch_artist=True, boxprops=dict(facecolor='C1', color='black'), medianprops=dict(color='black'))
patch1 = mpatches.Patch(color='C0', label='D-Vector')
patch2 = mpatches.Patch(color='C1', label='VGG-M')
leg = ax.legend(handles=[patch1, patch2], fontsize=20, prop={'size': 16}, loc="bottom center", ncol=3)
labels = ['Benign', '15', '12', '9', '6', '3', '1']
ax.set_xticks([0, 2, 4, 6, 8, 10, 12])
ax.set_xticklabels(labels, fontsize=16, family='arial')
leg.get_frame().set_boxstyle('square')
leg.get_frame().set_edgecolor('black')
#ax.set_ylim([-1, 1.6])
ax.set_ylabel('Similarity Score', fontsize=24, family='arial')
ax.set_xlabel('Poison Rate (%)', fontsize=24, family='arial')
plt.savefig("sim_b.pdf", dpi=None, facecolor='w', edgecolor='w',
            orientation='portrait', papertype=None, format=None,
            transparent=False, bbox_inches=None, pad_inches=.2,
            frameon=None, metadata=None)
plt.show()
#
# ####################################################################
# # sim_c: bar deeper model: resnet50, aert
# ####################################################################
data_1 = np.load('box_models/resnet50/0.npy')
data_2 = np.load('box_models/resnet50/15.npy')
data_3 = np.load('box_models/resnet50/12.npy')
data_4 = np.load('box_models/resnet50/9.npy')
data_5 = np.load('box_models/resnet50/6.npy')
data_6 = np.load('box_models/resnet50/3.npy')
data_7 = np.load('box_models/resnet50/1.npy')
alldata3 = [data_1, data_2, data_3, data_4, data_5, data_6, data_7]
allASR3 = getall_ASR(alldata3)

data_1 = np.load('box_models/AERT/0.npy')
data_2 = np.load('box_models/AERT/15.npy')
data_3 = np.load('box_models/AERT/12.npy')
data_4 = np.load('box_models/AERT/9.npy')
data_5 = np.load('box_models/AERT/6.npy')
data_6 = np.load('box_models/AERT/3.npy')
data_7 = np.load('box_models/AERT/1.npy')
alldata4 = [data_1, data_2, data_3, data_4, data_5, data_6, data_7]
allASR4 = getall_ASR(alldata4)
#########################################################################

# X = np.arange(7)
# fig = plt.figure(figsize=[6.0, 4.8])
# ax = fig.add_axes([0.18, 0.15, 0.8, 0.8])
# width = 0.5
# labels = ['Benign', '15', '12', '9', '6', '3', '1']
# rects1 = ax.bar(X-width/2, allASR3, width=0.4, label='ResNet-50')
# ax.plot(X-width/2, allASR3, "^--", linewidth=2, markersize=12, mfc='black')
# rects2 = ax.bar(X+width/2, allASR4, width=0.4, label='AERT')
# ax.plot(X+width/2, allASR4, "^--", linewidth=2, markersize=12, mfc='black')
# ax.set_xticks([0, 1, 2, 3, 4, 5, 6])
# ax.set_xticklabels(labels, fontsize=16, family='arial')
# ax.tick_params(direction='in', width=1)
# ax.grid(linestyle='--')
# # ax.set_ylim([-2, 360])
# leg = ax.legend(fontsize=24, prop={'size': 16}, loc="best", ncol=1)
# leg.get_frame().set_boxstyle('square')
# leg.get_frame().set_edgecolor('black')
#
# ax.set_ylabel('ASR (%)', fontsize=24, family='arial')
# ax.set_xlabel('Poison Rate (%)', fontsize=24, family='arial')
# # ax.set_ylim([0, 8])
#
# # plt.savefig("sim_c.pdf", dpi=None, facecolor='w', edgecolor='w',
# #             orientation='portrait', papertype=None, format=None,
# #             transparent=False, bbox_inches=None, pad_inches=0.2,
# #             frameon=None, metadata=None)
#
# plt.show()
#
# ####################################################################
# # sim_d: box deeper model: resnet50, aert
# ####################################################################
import matplotlib.patches as mpatches
#
fig = plt.figure(figsize=[6.0, 4.8])
ax = fig.add_axes([.2, .15, .75, .8])
res_plot = plt.boxplot(alldata3, positions=np.array(
    np.arange(len(alldata3))) * 2.0, widths=0.6, notch=True, patch_artist=True, boxprops=dict(facecolor='C0', color='black'), medianprops=dict(color='black'))
aert_plot = plt.boxplot(alldata4, positions=np.array(
    np.arange(len(alldata4))) * 2.0 + 0.7, widths=0.6, notch=True, patch_artist=True, boxprops=dict(facecolor='C1', color='black'), medianprops=dict(color='black'))
patch1 = mpatches.Patch(color='C0', label='ResNet-50')
patch2 = mpatches.Patch(color='C1', label='AERT')
leg = ax.legend(handles=[patch1, patch2], fontsize=20, prop={'size': 12}, loc="upper center", ncol=3)
labels = ['Benign', '15', '12', '9', '6', '3', '1']
ax.set_xticks([0, 2, 4, 6, 8, 10, 12])
ax.set_xticklabels(labels, fontsize=16, family='arial')
leg.get_frame().set_boxstyle('square')
leg.get_frame().set_edgecolor('black')
#ax.set_ylim([-1, 1.6])
ax.set_ylabel('Similarity Score', fontsize=24, family='arial')
ax.set_xlabel('Poison Rate (%)', fontsize=24, family='arial')
plt.savefig("sim_d.pdf", dpi=None, facecolor='w', edgecolor='w',
            orientation='portrait', papertype=None, format=None,
            transparent=False, bbox_inches=None, pad_inches=.2,
            frameon=None, metadata=None)
plt.show()