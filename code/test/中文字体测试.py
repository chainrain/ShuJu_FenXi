from pylab import *
import random
import matplotlib.font_manager
myfont = matplotlib.font_manager.FontProperties(fname="/home/python/Desktop/NotoSansCJK-Black.ttc")
mpl.rcParams['axes.unicode_minus'] = False
t = arange(-5*pi, 5*pi, 0.001)
y = sin(t)/t
my_post = plt.plot(t, y)
plt.title(u'matplotlib中文显示测试——Tacey Wong',fontproperties=myfont)
plt.xlabel(u'这里是X坐标',fontproperties=myfont)
plt.ylabel(u'这里是Y坐标',fontproperties=myfont)

plt.show()