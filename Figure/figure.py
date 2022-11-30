
#绘制折线图，添加数据点，设置点的大小
# * 表示绘制五角星；此处也可以不设置线条颜色，matplotlib会自动为线条添加不同的颜色
x=range(len(list(key)))

plt.figure(figsize=(6, 6))
plt.figure().set_size_inches(6,6)
plt.xlabel('Training Dataset Org Type',fontdict=font)  # x轴标题
plt.ylabel('Toxic Generation Rate',fontdict=font)  # y轴标题
plt.plot(x, all_data_list[0], 
         linestyle = 'solid',
         linewidth = 4,
         marker = 's',
         markersize = 15,
        #  color = 'darkorange',
) 
plt.plot(x, all_data_list[1], 
         linestyle = '--',
         linewidth = 4,
         marker = 's',
         markersize = 15,
        #  color = 'darkorange',
) 
plt.plot(x, all_data_list[2], 
         linestyle = 'solid',
         linewidth = 4,
         marker = 's',
         markersize = 15,
        #  color = 'darkorange',
) 

plt.plot(x, all_data_list[3], 
         linestyle = 'solid',
         linewidth = 4,
         marker = 's',
         markersize = 15,
        #  color = 'darkorange',
) 
plt.plot(x, all_data_list[4], 
         linestyle = 'solid',
         linewidth = 4,
         marker = 's',
         markersize = 15,
        #  color = 'darkorange',
) 

plt.xticks(x,size = 24)
plt.yticks(size = 24)
plt.grid(linestyle="-")
     
#给图像添加注释，并设置样式
# for a, b in zip(x, y1):
#     plt.text(a, b, b, ha='center', va='bottom')
# for a, b in zip(x, y2):
#     plt.text(a, b, b, ha='center', va='bottom')

plt.legend(['Prompt 1','Prompt 2','Prompt 3','Prompt 4'],fontsize=30,prop={'size':24},loc=4)
#绘制图例
# plt.legend(['Single-Turn','Multi-Turn'],fontsize=30,prop={'size':24},loc=4)
# plt.savefig('Fig1_a.png', dpi=300,bbox_inches='tight',  pad_inches = 0)


plt.savefig(os.path.join(figure_path,'Fig4_c.pdf'), dpi=300,bbox_inches='tight',  pad_inches = 0)
plt.show()
#显示图像

'''
================================
@2
================================
'''
plt.figure(figsize=(6, 6))
plt.figure().set_size_inches(6,6)
plt.xlabel('Training Dataset Org Type',fontdict=font)  # x轴标题
plt.ylabel('NT2T Rate',fontdict=font)  # y轴标题
plt.plot(x, all_data_list_e[0], 
         linestyle = 'solid',
         linewidth = 4,
         marker = 's',
         markersize = 15,
        #  color = 'darkorange',
) 
plt.plot(x, all_data_list_e[1], 
         linestyle = '--',
         linewidth = 4,
         marker = 's',
         markersize = 15,
        #  color = 'darkorange',
) 
plt.plot(x, all_data_list_e[2], 
         linestyle = 'solid',
         linewidth = 4,
         marker = 's',
         markersize = 15,
        #  color = 'darkorange',
) 

plt.plot(x, all_data_list_e[3], 
         linestyle = 'solid',
         linewidth = 4,
         marker = 's',
         markersize = 15,
        #  color = 'darkorange',
) 
plt.plot(x, all_data_list_e[4], 
         linestyle = 'solid',
         linewidth = 4,
         marker = 's',
         markersize = 15,
        #  color = 'darkorange',
) 

plt.xticks(x,size = 24)
plt.yticks(size = 24)
plt.grid(linestyle="-")
     
#给图像添加注释，并设置样式
# for a, b in zip(x, y1):
#     plt.text(a, b, b, ha='center', va='bottom')
# for a, b in zip(x, y2):
#     plt.text(a, b, b, ha='center', va='bottom')

plt.legend(['Prompt 1','Prompt 2','Prompt 3','Prompt 4'],fontsize=30,prop={'size':24},loc=4)
#绘制图例
# plt.legend(['Single-Turn','Multi-Turn'],fontsize=30,prop={'size':24},loc=4)
# plt.savefig('Fig1_a.png', dpi=300,bbox_inches='tight',  pad_inches = 0)


plt.savefig(os.path.join(figure_path,'Fig4_d.pdf'), dpi=300,bbox_inches='tight',  pad_inches = 0)
plt.show()
