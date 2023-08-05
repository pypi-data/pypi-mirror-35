
import micral_core
import micral_summary
import micral_utils

def extractDict(dict_input):
    dict_output = dict()
    for name,val in dict_input.items():
        if name not in dict_output:
            dict_output[name] = dict()
        if "grain" in val and isinstance(val["grain"],dict) and "coarse" in val["grain"]:
            dict_output[name]["coarse_grain"] = "%.2f%%" % val["grain"]["coarse"]
        if "harmonicity" in val and isinstance(val["harmonicity"],dict) and "harmonicity" in val["harmonicity"]:
            dict_output[name]["harmonicity"] = "%.2f%%" % val["harmonicity"]["harmonicity"]
        if "classify" in val and isinstance(val["classify"],dict) and "category" in val["classify"]:
            dict_output[name]["category"] = val["classify"]["category"]
        if "name" in val and isinstance(val["name"],dict) and "name" in val["name"]:
            dict_output[name]["name"] = val["name"]["name"]
            
    return dict_output

def globalAnalyse(images):
    raw_output = micral_core.analyse(images)
    micral_summary.summary(raw_output)
    output_dict = extractDict(raw_output)
    micral_utils.printDict(output_dict)
    return output_dict