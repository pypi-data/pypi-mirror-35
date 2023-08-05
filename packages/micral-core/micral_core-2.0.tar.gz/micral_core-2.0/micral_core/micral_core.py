import micral_grain_core
import micral_harmonic_core
import micral_classify_core
import micral_name_core
import micral_utils

def extractAllDict(dict_input, input_dict_name, dict_output):
    if isinstance(dict_input, dict):
        for name,val in dict_input.items():
            if name not in dict_output:
                dict_output[name] = dict()
            dict_output[name][input_dict_name] = val
    return dict_output

def globalAnalyseCore(images, grainParameters=None, harmonicParameters=None):
    dict_output = dict()
    extractAllDict(micral_grain_core.analyse(images, parameters=grainParameters), "grain", dict_output)
    extractAllDict(micral_harmonic_core.analyse(images, parameters=harmonicParameters, plot=True), "harmonicity", dict_output)
    extractAllDict(micral_classify_core.analyse(images), "classify", dict_output)
    extractAllDict(micral_name_core.analyse(images), "name", dict_output)
    return micral_utils.removeEmptyDict(dict_output)