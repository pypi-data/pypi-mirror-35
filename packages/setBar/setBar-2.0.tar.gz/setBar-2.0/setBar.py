# -*- coding: utf-8 -*-

from __future__ import print_function
import os
from PIL import Image
# im = Image.open('a.jpg')
# print '图像格式 ， 图像大小 ， 图像模式\n'
# print im.format , im.size , im.mode
# weight=im.size[0]
# height=im.size[1]

# box=(0,0,weight,40)
# region=im.crop(box)
# print region.format , region.size
# region.save('./bar.jpg')
# ===========================================
# 处理文件夹里面的截图base就是别人的截图 
# bar就是已经准备好的状态栏图片
# 找到base的宽高，然后把bar缩放处理成同等宽度，然后直接黏贴上去，保存为out.jpg

# 720屏幕状态栏设置50px，1080屏幕状态栏70px

# base=Image.open('b.jpg')
# bar=Image.open('bar.jpg')
# weight=base.size[0]
# height=base.size[1]

# box=(0,80,weight,height)
# base_noBar=base.crop(box)
# print 'base      :' , base.size
# print 'base_noBar:' , base_noBar.size
# bar=bar.resize((weight,80),Image.ANTIALIAS)
# bar=bar.rotate(180)
# print 'bar       :' , bar.size
# bar = bar.transpose(Image.ROTATE_180)

# bar_box=(0,0,weight,80)
# base.paste(bar,bar_box)
# base.save('out.jpg')
# ================================================
# 下面是我的尝试
def change_statusBar(base , yourself , out):
	base=Image.open(base)
	yourself=Image.open(yourself)
	base_weight , base_height = base.size
	yourself_weight , yourself_height = yourself.size
	yourself_bar=None

	if yourself_weight == 720:
		box=(0,0,yourself_weight,50)
		yourself_bar=yourself.crop(box)
	elif yourself_weight == 1080:
		box=(0,0,yourself_weight,70)
		yourself_bar = yourself.crop(box)
	else:
		print('your mobliephone is not 720p or 1080p')
		i=50.0/720.0
		bar_weight=yourself_weight*i
		bar_height=int(bar_height)
		box=(0,0,yourself_weight,bar_height)
		yourself_bar = yourself.crop(box)

	if base_weight == 720:
		yourself_bar = yourself_bar.resize((720,50))
		yourself_bar = yourself_bar.transpose(Image.ROTATE_180)
		yourself_bar = yourself_bar.rotate(180)
		base.paste(yourself_bar,(0,0,720,50))
	if base_weight == 1080:
		yourself_bar = yourself_bar.resize((1080,70))
		yourself_bar = yourself_bar.transpose(Image.ROTATE_180)
		print(yourself_bar.size)
		yourself_bar = yourself_bar.rotate(180)
		base.paste(yourself_bar,(0,0,1080,70))
	else:
		print('the base picture is not 720p or 1080p')
		bar_weight = base_weight
		bar_height = base_weight*i
		yourself_bar = yourself_bar.resize(bar_weight,bar_height)
		yourself_bar = yourself_bar.transpose(Image.ROTATE_180)
		yourself_bar = yourself_bar.rotate(180)
		base.paste(yourself_bar,(0,0,bar_weight,bar_height))
	print('OK!')
	base.save(out)
	