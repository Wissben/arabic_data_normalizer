# -*- coding: utf-8 -*-
import farassaWrapper.farassaInterface
import os

root= "/home/weiss/CODES/NLP/Mini-project/farasa/jars/"
f = str.join(":", [root+name for name in os.listdir(root)])

#
# '''
# First you need to define where are the jar(s)
# '''
segm = "/home/weiss/CODES/NLP/Mini-project/farasa/jars/FarasaSegmenterJar.jar"
postagger = "/home/weiss/CODES/NLP/Mini-project/farasa/jars/FarasaPOSJar.jar"
# #test = open("/home/weiss/CODES/NLP/Mini-project/farasa/posTagger/tests/test.in",'r').read()
test = "يُشار إلى أن اللغة العربية يتحدثها أكثر من 422 مليون نسمة ويتوزع متحدثوها في المنطقة المعروفة باسم الوطن العربي بالإضافة إلى العديد من المناطق الأخرى المجاورة مثل الأهواز وتركيا وتشاد والسنغال وإريتريا وغيرها. وهي اللغة الرابعة من لغات منظمة الأمم المتحدة الرسمية الست."

far = farassaWrapper.farassaInterface.Farasa(f)
res = far.tag(test,postagger)
print(res)

