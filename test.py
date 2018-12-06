# -*- coding: utf-8 -*-
import farassaWrapper.farassaInterface
import os





'''
First you need to define where are the jar(s)
'''
root= "/home/weiss/CODES/NLP/Mini-project/farasa/jars/"
jars = str.join(":", [root+name for name in os.listdir(root)])
# segm = "/home/weiss/CODES/NLP/Mini-project/farasa/jars/FarasaSegmenterJar.jar"
# postagger = "/home/weiss/CODES/NLP/Mini-project/farasa/jars/FarasaPOSJar.jar"
# test = open("/home/weiss/CODES/NLP/Mini-project/farasa/posTagger/tests/test.in",'r').read()
test = "يُشار إلى أن اللغة العربية يتحدثها أكثر من 422 مليون نسمة ويتوزع متحدثوها في المنطقة المعروفة باسم الوطن العربي بالإضافة إلى العديد من المناطق الأخرى المجاورة مثل الأهواز وتركيا وتشاد والسنغال وإريتريا وغيرها. وهي اللغة الرابعة من لغات منظمة الأمم المتحدة الرسمية الست."


'''
Instantiate a Farasa object with the path to the jars as parameter
'''
far = farassaWrapper.farassaInterface.Farasa(jars)



'''
Use different methods
'''
res = far.lemmetize(test)
print(res)

