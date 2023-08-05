import micral_classify_core

def classifyPrint(dict_input, plot):
    output_coarse = dict()
    if dict_input != None:
        for nameImg, dictImg in dict_input.items():
            if 'category' in dictImg:
                output_coarse[nameImg] = dictImg['category']
            
    return output_coarse

def classifyImage(images, plot):
    out = micral_classify_core.analyse(images, plot)
    return classifyPrint(out, plot)