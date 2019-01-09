#encoding:utf-8
import os

def file_path():

	#os.path.dirname(__file__)返回的是.py所在的目录

	'''打开当前运行脚本的绝对路径'''
	paths = os.path.dirname(__file__)

	print(paths)

	'''切割路径，以split后面传的字符串切割'''

	newpaths = paths.split('unitest_example')[0]

	print(newpaths)

    #os.path.abspath(__file__)返回的是.py文件的绝对路径（完整路径）

	new = os.path.abspath(__file__)

	print(new)


if __name__ == '__main__':
	file = file_path()
	print(file)