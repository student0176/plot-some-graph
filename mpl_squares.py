import matplotlib.pyplot as plt

# input_value = [i for i in range(1,6)]
# squares = [i**2 for i in range(1,6)]
# plt.plot(input_value, squares, linewidth=5) # 這裏就是準備階段，初始化軸、右上角象限、文字等等，下面show顯示出來。正如a=3已經弄好了，print打印出來
# plt.title('Square Numbers', fontsize=24)
# plt.xlabel('Value', fontsize=14)
# plt.ylabel('Square of Value', fontsize=14)
#
# plt.tick_params(axis='both', labelsize=14)
#
#
# plt.savefig('./image_rw/aline_add_xaixs.jpg')
# plt.show()


plt.scatter(2,90, s = 200) # s為尺寸
x_values = [i for i in range(1,30)]
y_values = [1/i/i for i in range(1,30)]
plt.scatter(x_values,y_values,c = y_values,cmap=plt.cm.Blues,s = 100) # s為尺寸,c設定色(設為（0.1，0.7，0.8）也行),jet是彩色。如果是漸變，那麽c就是每個點分配的顔色權重

plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

plt.axis([0,30,0,1])
plt.tick_params(axis='both', which = 'major', labelsize=14)

# plt.savefig('./image_rw/scatter_colormap_bbox.jpg',bbox_inches='tight') #裁剪了邊緣
plt.show()