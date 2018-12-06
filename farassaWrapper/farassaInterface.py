import jpype
from jpype import *
import subprocess


class Farasa:
    def __init__(self,path_to_jars):
        jvmPath = jpype.getDefaultJVMPath()
        jpype.startJVM(jvmPath,
                       "-Djava.class.path="+path_to_jars)


    def segment(self,text):
        Far = JPackage("com").qcri.farasa.segmenter.Farasa
        far = Far()
        return far.segmentLine(text)

    def lemmetize(self,text):
        Far = JPackage("com").qcri.farasa.segmenter.Farasa
        far = Far()
        return far.lemmatizeLine(text)
    #
    # def TAG(self,text):
    #     Farasa = JPackage("com").qcri.farasa.segmenter.Farasa
    #     FarPosTagger = JPackage("com").qcri.farasa.pos.FarasaPOSTagger
    #     Sentence = JPackage("com").qcri.farasa.pos.Sentence;
    #
    #
    #     far = Farasa()
    #     tagger = FarPosTagger(far)
    #     lines = Sentence()
    #     lines = self.segment(text)
    #     sents = tagger.tagLine(lines)
    #
    #     for sent in sents:
    #         print (sent)
    #     # print(sents)

    def tag_file(self, file_path,path_to_postagger):
        subprocess.call(['java', '-jar', path_to_postagger, '-i', file_path, '-o', 'tmp.out'])

        try:
            tmp_out = open("tmp.out", 'r')
        except IOError:
            tmp_out = open("tmp.out", 'w')
        tagged = tmp_out.read()
        res_split = tagged.split()
        res = []
        for r in res_split:
            t = r.split("/")
            res.append((t[0], t[1]))
        return res

    def tag(self, text,path_to_postagger):
        tmp_in = open('tmp.in', 'w')
        tmp_in.write(text)
        tmp_in.close()
        subprocess.call(['java', '-jar', path_to_postagger, '-i', 'tmp.in', '-o', 'tmp.out'])

        try:
            tmp_out = open("tmp.out", 'r')
        except IOError:
            tmp_out = open("tmp.out", 'w')

        tagged = tmp_out.read()
        res_split = tagged.split()
        res = []
        for r in res_split:
            t = r.split("/")
            res.append((t[0], t[1]))
        return res

