# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 18:34:07 2018

@author: wuhongrui
"""

import sys
import MySQLdb
import os
from PIL import Image

def image2db():
    
    #本地图片所在路径
    localpath = "D:/file/try/try_png"
    projectName = 'name'
    #建立一个MySQL连接
    db = MySQLdb.connect(host="localhost", user="root", passwd="123456", charset='utf8')

    # 创建游标
    cursor = db.cursor()
    #创建项目数据库
    cursor.execute("CREATE DATABASE if not exists %s DEFAULT CHARACTER SET utf8" % projectName)
    cursor.execute("USE %s" % projectName)
    
    #创建保存图片数据的表格
    imgTbName = projectName+'img'
    sql = "Create table if not exists %s (id int(10) unsigned primary key auto_increment, image_name varchar(200), raw_data longblob, is_marking char(20) default 'no', if_verify char(20) default 'no') default character set utf8"% imgTbName
    cursor.execute(sql)

    #从本地读取图片文件存入数据库
    for imagefile in os.listdir(localpath):
        with open(os.path.join(localpath, imagefile), "rb") as f:
            img_data = f.read()
            f.close()
        
        image_name = str(imagefile)[:-4]
    
        sql = "INSERT INTO %s (image_name, raw_data) VALUES ('%s', '%s')" % (imgTbName, image_name, MySQLdb.escape_string(img_data))
        cursor.execute(sql)
        db.commit()

    #创建储存标注数据的表格
    xmlTbName = projectName+'xml'
    sql = "Create table if not exists %s (id int(10) unsigned primary key auto_increment, image_name varchar(200), xml_content varchar(2000), marker_id char(20)) default character set utf8"%  xmlTbName
    cursor.execute(sql)
    
    db.commit()
    cursor.close()
    db.close()       

def jpg2png():
    
    #本地图片所在路径和png图片保存路径
    jpgpath = "D:/file/try/try_jpg"
    pngpath = "D:/file/try/try_png"
    for imagefile in os.listdir(jpgpath):
        f = Image.open(os.path.join(jpgpath, imagefile))
        imagefile = str(imagefile)[:-4]+'.png'
        f.save(os.path.join(pngpath, imagefile))

if __name__=="__main__":
    #jpg2png()
    image2db()
