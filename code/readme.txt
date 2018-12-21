下载Anaconda: https://www.anaconda.com/download/
安装Anaconda文档: http://docs.anaconda.com/anaconda/install/verify-install/
项目使用这个环境: Python 3.7.1 (~/anaconda3/envs/python3/bin/python): Python 3.7.1 (/home/python/anaconda3/envs/python3/bin/python)
安装额外包: conda install xxxxx,然后在文件内部alt+enter,安装



以上方法如果比较麻烦,不过可以一站式解决所有包
比较简单的方法是用虚拟环境:
mkvirtualenv + 虚拟环境名 -p python3 (使用py3的库)
然后:
pip install matplotlib
sudo apt-get install python3-tk


matplotlib 绘图工具更多的样式:http://matplotlib.org/gallery/index.html



不过以后更多的是用数据,然后用网页版的绘图框架,展示在前段,例如:http://www.echartsjs.com/examples/