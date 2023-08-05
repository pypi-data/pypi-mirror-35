import micral_name_core

def namePrint(dict_input, plot):
    output_coarse = dict()
    if dict_input != None:
        for nameImg, dictImg in dict_input.items():
            if 'name' in dictImg:
                output_coarse[nameImg] = dictImg['name']
            
    return output_coarse

def nameImage(images, plot):
    out = micral_name_core.analyse(images, plot)
    return namePrint(out, plot)