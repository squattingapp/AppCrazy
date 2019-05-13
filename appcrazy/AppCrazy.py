import deformation_method
from optparse import  OptionParser

if __name__ == "__main__":
    # str='''Supports the following Squatting Generation Models:
    #         vowel_character_insertion,vowel_character_deletion,vowel_character_substitution,double_character_insertion,double_character_deletion,
    #         puncatuation_substitution,puncatuation_deletion,misspelling_mistakes_substition,string_rearrangement'''
    usage = "usage:%prog [options] arg"
    parser = OptionParser()
    parser.add_option("-a","--appname",action="store",type = "string",dest="appname",default=False,help="appname deformation")
    parser.add_option("-p", "--packagename", action="store",type = "string",dest="packagename", default=False, help="packagename deformation")
    parser.add_option("-f","--file",action="store",type="string",dest="filename",default=False,help="write results to filename.txt")
    options,args = parser.parse_args()

    p_result_dic = {}
    A_result_dic = {}
    if options.packagename is not False:
        p_variants = deformation_method.DeformationMethod(options.packagename.lower())
        p_variants.packagename_deformation()
        p_result_dic = p_variants.variant_dic

    if options.appname is not False:
        A_variants = deformation_method.DeformationMethod(options.appname.lower())
        A_variants.appname_deformation()
        A_result_dic = A_variants.variant_dic

    if options.filename is False:
        print("AppCrazy Deformation Result")
        print("ori_appname:%20s"%options.appname)
        print("ori_packagename:%10s"%options.packagename)
        print("")
        print("Squatting Generation Models %20s"%("Squatting Name"))
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")
        for key,value in A_result_dic.items():
            print("%s %s"%(value.ljust(40),key))
        for key,value in p_result_dic.items():
            print("%s %s"%(value.ljust(40),key))
    else:
        with open(options.filename,"w") as f:
            f.write("AppCrazy Deformation Result"+"\n")
            f.write("ori_appname:%20s" % options.appname+"\n")
            f.write("ori_packagename:%10s" % options.packagename+"\n")
            f.write(""+"\n")
            f.write("Squatting Generation Models %20s" % ("Squatting Name")+"\n")
            f.write("- - - - - - - - - - - - - - - - - - - - - - - - - - -"+"\n")
            for key, value in A_result_dic.items():
                f.write("%s %s" % (value.ljust(40), key)+"\n")
            for key, value in p_result_dic.items():
                f.write("%s %s" % (value.ljust(40), key)+"\n")
            f.close()