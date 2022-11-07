import os
from fnmatch import fnmatch


debug = False
debug_pause = False

print("")
print("Eagle's Handy OTG scripts")
print("")
print("")
print("Thanks for using Eagle's Handy OTG scripts, Here's a list of current functions:")
print("")
print("1. Eagle's simple search and write script")
print("This script searches folders & subfolders for .bc files & writes the following data to a seperate file:")
print("<biomename>.bc  BiomeColor: <value>  ReplaceToBiomeName: <name or empty if not used>")
print("BiomeTemperature: <value>  BiomeWetness: <value>  WaterColor: <value>  GrassColor: <value>  FoliageColor: <value>  BiomeDictId: <value>  InheritMobsBiomeName: <value>")
print("FogColor: <value>  FogDensity: <value>  FogTimeWeight: <value>  FogRainWeight: <value>  FogThunderWeight: <value>")
print("")
print("")
print("2. Eagle's inheritance script")
print("This script checks the ReplaceToBiomeName value of a biome and makes sure it's contents reflect the values of the ReplaceToBiomeName biome. If the ReplaceToBiomeName value is empty it will skip the file.")
print("")
print("")
print("3. Eagle's Duplicate Biomecolor Finder")
print("This script checks all biomes for their biomecolors and outputs a list of duplicate ones making it easier to make each biome have it's own unique biomecolor. This is handy for FromImage or Hybrid worlds.")
print("")
print("")

loop = True
count = 0

while loop == True:
    script = input("Enter the number of script you want to run:")

    if ((script == "1") or (script == "2") or (script == "3")):
        if (count >= 10):
            count = 0
        
    elif count >= 100:
        print("")
        print("I'm sure you have better things to do...")
        print("")
        count += 1
        
    elif count >= 10:
        print("")
        print("Yeah, this isn't getting anywhere")
        print("")
        count += 1
        
    elif ((script != "1") or (script != "2") or (script != "3")):
        print("")
        print("Invalid script, please try again.")
        print("")
        count += 1
        
    else:
        loop=False
        print("")
        
    #------------------------------------------- SCRIPT 1 --------------------------------------------------
    if script == "1":
            
        print("---------------------------------------------------------------------")
        print("Eagle's simple search and write script")
        print("---------------------------------------------------------------------")
        print("")

        dir_path = input("Enter directory root path or press enter to use current directory:")
        print("")

        if dir_path == "":
            dir_path = os.getcwd()



        current_path = os.getcwd()
        output_name = input("Enter name of output file (E.G. temp.txt) Or press enter to create a temp.txt file:")
        if output_name == "":
            output_name = "temp.txt"
        print("")
        output_current_path = ('Save '+output_name+' in '+current_path+'? Y/N'+'\nPressing enter defaults to Y')
        save_current = input(output_current_path)


            
        if (("y" in save_current) or ("Y" in save_current)):
            print("")
            print(output_name," will be saved in ",current_path)
            print("")
            output_path = current_path
            
        if (("n" in save_current) or ("N" in save_current)):
            current_path = input("Enter directory path:")
            print("")
            print(output_name," will be saved in ",current_path)
            print("")
            output_path = os.path.join(current_path, output_name)
            
        if "" in save_current:
            print("")
            print(output_name," will be saved in ",current_path)
            print("")
            output_path = current_path

        completeName = os.path.join(output_path, output_name)
        dir_list = os.listdir(dir_path)


        print(dir_path, "Contains the following files: ")
        print("")

        root = dir_path
        pattern = "*.bc"

        for path, subdirs, files in os.walk(root):
            for name in files:
                if fnmatch(name, pattern):
                    print("")
                    
                    
                    
                    file_source = os.path.join(path, name)
                    file_read = open(file_source, "r")
                    
                    text1 = "BiomeColor:"
                    lines = file_read.readlines()
                    for line in lines:
                        if text1 in line:
                            file_list1 = line.strip('\n')
                    file_read.close()
                    
                    file_read = open(file_source, "r")
                    text2 = "ReplaceToBiomeName:"
                    lines = file_read.readlines()
                    for line in lines:
                        if text2 in line:
                            file_list2 = line.strip('\n')
                    file_read.close()

                    file_read = open(file_source, "r")
                    text3 = "BiomeTemperature:"
                    lines = file_read.readlines()
                    for line in lines:
                        if text3 in line:
                            file_list3 = line.strip('\n')
                    file_read.close()
                    
                    file_read = open(file_source, "r")
                    text4 = "BiomeWetness:"
                    lines = file_read.readlines()
                    for line in lines:
                        if text4 in line:
                            file_list4 = line.strip('\n')
                    file_read.close()
                    
                    file_read = open(file_source, "r")
                    text5 = "WaterColor:"
                    lines = file_read.readlines()
                    for line in lines:
                        if text5 in line:
                            file_list5 = line.strip('\n')
                    file_read.close()

                    file_read = open(file_source, "r")
                    text6 = "GrassColor:"
                    lines = file_read.readlines()
                    for line in lines:
                        if text6 in line:
                            file_list6 = line.strip('\n')
                    file_read.close()
                    
                    file_read = open(file_source, "r")
                    text7 = "FoliageColor:"
                    lines = file_read.readlines()
                    for line in lines:
                        if text7 in line:
                            file_list7 = line.strip('\n')
                    file_read.close()
                    
                    file_read = open(file_source, "r")
                    text8 = "BiomeDictId:"
                    lines = file_read.readlines()
                    for line in lines:
                        if text8 in line:
                            file_list8 = line.strip('\n')
                    file_read.close()
                    
                    file_read = open(file_source, "r")
                    text9 = "InheritMobsBiomeName:"
                    lines = file_read.readlines()
                    for line in lines:
                        if text9 in line:
                            file_list9 = line.strip('\n')
                    file_read.close()
                    
                    file_read = open(file_source, "r")
                    text10 = "FogColor:"
                    lines = file_read.readlines()
                    for line in lines:
                        if text10 in line:
                            file_list10 = line.strip('\n')
                    file_read.close()
                    
                    file_read = open(file_source, "r")
                    text11 = "FogDensity:"
                    lines = file_read.readlines()
                    for line in lines:
                        if text11 in line:
                            file_list11 = line.strip('\n')
                    file_read.close()
                    
                    file_read = open(file_source, "r")
                    text12 = "FogTimeWeight:"
                    lines = file_read.readlines()
                    for line in lines:
                        if text12 in line:
                            file_list12 = line.strip('\n')
                    file_read.close()
                    
                    file_read = open(file_source, "r")
                    text13 = "FogRainWeight:"
                    lines = file_read.readlines()
                    for line in lines:
                        if text13 in line:
                            file_list13 = line.strip('\n')
                    file_read.close()
                    
                    file_read = open(file_source, "r")
                    text14 = "FogThunderWeight:"
                    lines = file_read.readlines()
                    for line in lines:
                        if text14 in line:
                            file_list14 = line.strip('\n')
                    file_read.close()

                    #Write lines in file:
                    print("    ",name,file_list1,file_list2)
                    print("    ",file_list3,"  ",file_list4,"  ",file_list5,"  ",file_list6,"  ",file_list7,"  ",file_list8,"  ",file_list9)
                    print("    ",file_list10,"  ",file_list11,"  ",file_list12,"  ",file_list13,"  ",file_list14)
                    first_line = ("    ",name,"  ",file_list1,"  ",file_list2,"\n")
                    second_line = ("    ",file_list3,"  ",file_list4,"  ",file_list5,"  ",file_list6,"  ",file_list7,"  ",file_list8,"  ",file_list9,"\n")
                    third_line = ("    ",file_list10,"  ",file_list11,"  ",file_list12,"  ",file_list13,"  ",file_list14,"\n\n")
                    f = open(completeName, "a")
                    f.writelines(first_line)
                    f.writelines(second_line)
                    f.writelines(third_line)
                    f.close()
        
        print("")
        end = input("press enter to return to menu")
        
        print("")
        print("Eagle's Handy OTG scripts")
        print("")
        print("")
        print("Thanks for using Eagle's Handy OTG scripts, Here's a list of current functions:")
        print("")
        print("1. Eagle's simple search and write script")
        print("This script searches folders & subfolders for .bc files & writes the following data to a file:")
        print("<biomename>.bc  BiomeColor: <value>  ReplaceToBiomeName: <name or empty if not used>")
        print("BiomeTemperature: <value>  BiomeWetness: <value>  WaterColor: <value>  GrassColor: <value>  FoliageColor: <value>  BiomeDictId: <value>  InheritMobsBiomeName: <value>")
        print("")
        print("")
        print("2. Eagle's inheritance script")
        print("This script checks the ReplaceToBiomeName value of a biome and makes sure it's contents reflect the values of the ReplaceToBiomeName biome. If the ReplaceToBiomeName value is empty it will skip the file.")
        print("")
        print("")
        print("3. Eagle's Duplicate Biomecolor Finder")
        print("This script checks all biomes for their biomecolors and outputs a list of duplicate ones making it easier to make each biome have it's own unique biomecolor. This is handy for FromImage or Hybrid worlds.")
        print("")
        print("")
        
        loop = True
        
    #------------------------------------------- SCRIPT 2 --------------------------------------------------
    if script == "2":
    
        import shutil, os.path
        
        print("---------------------------------------------------------------------")
        print("Eagle's inheritance script")
        print("---------------------------------------------------------------------")
        print("")
        print("Before you proceed it is adviced to make a work folder with a copy of your worldbiomes folder and use this as your directory root.")
        print("Doing this makes sure that even if things go wrong it only applies to the work folder and not to your actual preset folders.")
        print("It is important that your worldbiomes folder also contains a separate folder with the vanilla biomes because this script uses those files for reference whenever they are used as ReplaceToBiomeName value and builds on them being in a separated folder. E.G. vanillabiomes\Beach.bc")
        print("")
        print("The values that this script will replace are: BiomeTemperature, BiomeWetness, WaterColor, GrassColor, FoliageColor, BiomeDictId, InheritMobsBiomeName, FogColor, FogDensity, FogTimeWeight, ForRainWeight and FogThunderWeight")
        dir_path = input("Enter directory root path:")
        if dir_path == "":
            dir_path = os.getcwd()
        print("")


        import os
        import os.path
        import fileinput
        
        vanilla = 0 #Number of virtual biomes that inherit from vanilla biomes.
        parent = 0 #Number of custom parent biomes.
        custom = 0 #Number of virtual biomes that inherit from custom biomes.
        allbiomes = 0 #Number of all the biomes passed, both custom as vanilla.
        name_array = []
        non_virtual_biome_array = []
        skip_file = False
        
        
        #------------------------------------------- SEARCH FOR THE VANILLA PATH -------------------------------------------------#
        continue_script = False
        
        while continue_script == False:

            for dirpath, dirnames, filenames in os.walk(dir_path):
                for filename in [f for f in filenames if (f.endswith(".bc") and ("Birch Forest Hills M" in f))]:
                    print("detected folder with vanilla biomes: ",os.path.join(dirpath)," and will use this folder as reference.")
                    
                    print("")
                    print("Make sure to update the vanilla biome folder to at least the latest 1.12.2 default vanilla folders. Versions older then 1.12.2 do not have BiomeDictId's and this will result in empty BiomeDictId's causing issues with mod compatibility! The best way to prevent this is to delete the vanilla biome folder and letting OTG re-generate them.")
                    print("")
                    
                    
                    confirm = input("Confirm: Y/N:")
                    
                    vanilla_full_path = (os.path.join(dirpath))
                    vanilla_path = (vanilla_full_path.rsplit('\\',1)[1])
                    
                    if (("y" in confirm) or ("Y" in confirm)):
                        continue_script = True

                        
                    if (("n" in confirm) or ("N" in confirm)):
                        continue_script = False
                        print("")
                        print("Re-attempting search for vanilla biome folder.")
                        print("")
        #------------------------------------------- SEARCH FOR THE VANILLA PATH END -------------------------------------------------#
             

        #------------------------------------------- LIST ALL NON-VIRTUAL BIOMES -------------------------------------------------#
        
        root = dir_path
        pattern = "*.bc"
        
        for path, subdirs, files in os.walk(root):
            for name in files:
                if (fnmatch(name, pattern) and (name not in name_array)):
                    file_source = os.path.join(path, name)
                    passed_already = False
                    
                    file_read = open(file_source, "r")
                    lines = file_read.readlines()

                    if vanilla_path not in path:
                    
                        if debug: print ("Checking if ",name," is a non-virtual biome")
                        if debug_pause: deb = input()
                                
                        #checking line by line for replacetobiomename - start -
                        for line in lines:
                            
                            # Confirmation that the source_file is a virtual biome.
                            if (("ReplaceToBiomeName:" in line) and (("ReplaceToBiomeName:\n" in line) or ("ReplaceToBiomeName: \n" in line)) and ("#" not in line)):
                                if debug:
                                    print(file_source," Is a non virtual biome")
                                    if debug_pause:
                                        deb = input()
                                        
                                non_virtual_biome_array.append(file_source)
        
        
        
        #------------------------------------------- LIST ALL NON-VIRTUAL BIOMES END-------------------------------------------------#


        #------------------------------------------- SEARCH FOR REPLACETOBIOMENAME IN FILES  -------------------------------------------------#

        
        #for each source_file in file structure search for replacedbiomenames
        for path, subdirs, files in os.walk(root):
            for name in files:
                if (fnmatch(name, pattern)):
                    file_source = os.path.join(path, name)
                    passed_already = False
                    
                    file_read = open(file_source, "r")
                    lines = file_read.readlines()
                    
                    
                    if debug:
                        print("Searching for ReplaceToBiomeName in: ",name)
                        if debug_pause:
                            deb = input()
                    #Making sure the source_file is not a vanilla file by referencing vanilla path.
                    if debug:
                        print("Checking if",vanilla_path,"is in",path)
                        if debug_pause:
                            deb = input()
                    
                    if vanilla_path not in path:
                    
                        allbiomes += 1
                    
                        if debug:
                            print("Confirmed",vanilla_path,"is not in",path)
                            if debug_pause:
                                deb = input()
                        

                        
                        #checking line by line for replacetobiomename - start -
                        for line in lines:

                            if (("ReplaceToBiomeName:" in line) and ("#" not in line) and ("minecraft:" in line)):
                                vanilla += 1
                            # Confirmation that the source_file is a virtual biome.
                            if (("ReplaceToBiomeName:" in line) and ("ReplaceToBiomeName:\n" not in line) and ("ReplaceToBiomeName: \n" not in line) and ("#" not in line)):
                                custom += 1
                            
                                if debug:
                                    print(name,"is a virtual biome because",line,"is empty")
                                    if debug_pause:
                                        deb = input()
                                
                                #transform 'ReplaceToBiomename: Dregora_Cave' into 'Dregora_Cave.bc'
                                line = line.strip("ReplaceToBiomeName: ")
                                line = line.strip("\n")
                                lineprint = line.strip("\n")
                                line = (line+".bc")
                                vanilla_path_line = line
                                #end transform
                                
                                #searching for the replacedbiomename target_file in file structure
                                file_source = os.path.join(path, name)
                                for find_path, find_subdirs, find_files in os.walk(root):
                                    for find_file in find_files:
                                        if debug:
                                            print("Checking if ",vanilla_path_line,"is same as",find_file)
                                            if debug_pause:
                                                deb = input()
                                        if ((find_file == vanilla_path_line) and (passed_already != True)):
                                           
                                            vanilla_full_path_complete = os.path.join(find_path, vanilla_path_line)
                                            
                                            if debug: print(vanilla_path_line,"Is the same as",find_file)
                                            if debug: print("vanilla_full_path_complete is now set to",vanilla_full_path_complete)
                                            
                                            #once target_file has been found copy it's settings to variables
                                            
                                            file_read_vanilla = open(vanilla_full_path_complete, "r")
                                            vanilla_lines = file_read_vanilla.readlines()
                                            for line in vanilla_lines:
                                                if 'BiomeTemperature:' in line:
                                                    BiomeTemperature = line
                                                if 'BiomeWetness:' in line:
                                                    BiomeWetness = line
                                                if 'SkyColor:' in line:
                                                    SkyColor = line
                                                if 'WaterColor:' in line:
                                                    WaterColor = line
                                                if 'GrassColor:' in line:
                                                    GrassColor = line
                                                if 'GrassColor2:' in line:
                                                    GrassColor2 = line
                                                if 'FoliageColor:' in line:
                                                    FoliageColor = line
                                                if 'FoliageColor2:' in line:
                                                    FoliageColor2 = line
                                                if 'BiomeDictId:' in line:
                                                    BiomeDictId = line
                                                if 'FogColor:' in line:
                                                    FogColor = line
                                                if 'FogDensity:' in line:
                                                    FogDensity = line
                                                if 'FogTimeWeight:' in line:
                                                    FogTimeWeight = line
                                                if 'FogRainWeight:' in line:
                                                    FogRainWeight = line
                                                if 'FogThunderWeight:' in line:
                                                    FogThunderWeight = line
                                            file_read_vanilla.close()
                                            
                        #Check if file_source is a non virtual bionme:
                        if file_source in non_virtual_biome_array:
                            print("")
                            print(file_source,"is a non-virtual biome, skipping write actions.")
                            print("")
                            parent += 1
                        else:
                            #Write the variables from target_file to source_file
                            print("writing information from",vanilla_full_path_complete," to ",file_source)
                            
                            replaced_content = ""

                            for line in lines:

                                if (('BiomeTemperature:' in line) and ((line.startswith("#")) is not True)):
                                    new_line = line.replace(line, BiomeTemperature)
                                    line = line.strip()
                                else:
                                    new_line = line.replace(line, line)
                                replaced_content = (replaced_content + new_line)
                                
                            file_read.close()
                            write_file = open(file_source, "w")
                            write_file.write(replaced_content)
                            write_file.close()

                            file_read = open(file_source, "r")
                            replaced_content = ""
                            for line in file_read:
                                if (('BiomeWetness:' in line) and ((line.startswith("#")) is not True)):
                                    new_line = line.replace(line, BiomeWetness)
                                    line = line.strip()
                                else:
                                    new_line = line.replace(line, line)
                                replaced_content = (replaced_content + new_line)
                                
                            file_read.close()
                            write_file = open(file_source, "w")
                            write_file.write(replaced_content)
                            write_file.close()
                            
                            file_read = open(file_source, "r")
                            replaced_content = ""
                            for line in file_read:
                                if (('SkyColor:' in line) and ((line.startswith("#")) is not True)):
                                    new_line = line.replace(line, SkyColor)
                                    line = line.strip()
                                else:
                                    new_line = line.replace(line, line)
                                replaced_content = (replaced_content + new_line)
                                
                            file_read.close()
                            write_file = open(file_source, "w")
                            write_file.write(replaced_content)
                            write_file.close()
                            
                            file_read = open(file_source, "r")
                            replaced_content = ""
                            for line in file_read:
                                if (('WaterColor:' in line) and ((line.startswith("#")) is not True)):
                                    new_line = line.replace(line, WaterColor)
                                    line = line.strip()
                                else:
                                    new_line = line.replace(line, line)
                                replaced_content = (replaced_content + new_line)
                                
                            file_read.close()
                            write_file = open(file_source, "w")
                            write_file.write(replaced_content)
                            write_file.close()
                            
                            file_read = open(file_source, "r")
                            replaced_content = ""
                            for line in file_read:
                                if (('GrassColor:' in line) and ((line.startswith("#")) is not True)):
                                    new_line = line.replace(line, GrassColor)
                                    line = line.strip()
                                else:
                                    new_line = line.replace(line, line)
                                replaced_content = (replaced_content + new_line)
                                
                            file_read.close()
                            write_file = open(file_source, "w")
                            write_file.write(replaced_content)
                            write_file.close()
                            
                            file_read = open(file_source, "r")
                            replaced_content = ""
                            for line in file_read:
                                if (('GrassColor2:' in line) and ((line.startswith("#")) is not True)):
                                    new_line = line.replace(line, GrassColor2)
                                    line = line.strip()
                                else:
                                    new_line = line.replace(line, line)
                                replaced_content = (replaced_content + new_line)
                                
                            file_read.close()
                            write_file = open(file_source, "w")
                            write_file.write(replaced_content)
                            write_file.close()
                            
                            file_read = open(file_source, "r")
                            replaced_content = ""
                            for line in file_read:
                                if (('FoliageColor:' in line) and ((line.startswith("#")) is not True)):
                                    new_line = line.replace(line, FoliageColor)
                                    line = line.strip()
                                else:
                                    new_line = line.replace(line, line)
                                replaced_content = (replaced_content + new_line)
                                
                            file_read.close()
                            write_file = open(file_source, "w")
                            write_file.write(replaced_content)
                            write_file.close()
                            
                            file_read = open(file_source, "r")
                            replaced_content = ""
                            for line in file_read:
                                if (('FoliageColor2:' in line) and ((line.startswith("#")) is not True)):
                                    new_line = line.replace(line, FoliageColor2)
                                    line = line.strip()
                                else:
                                    new_line = line.replace(line, line)
                                replaced_content = (replaced_content + new_line)
                                
                            file_read.close()
                            write_file = open(file_source, "w")
                            write_file.write(replaced_content)
                            write_file.close()
                           
                            
                            file_read = open(file_source, "r")
                            replaced_content = ""
                            for line in file_read:
                                if (('FogColor:' in line) and ((line.startswith("#")) is not True)):
                                    new_line = line.replace(line, FogColor)
                                    line = line.strip()
                                else:
                                    new_line = line.replace(line, line)
                                replaced_content = (replaced_content + new_line)
                                
                            file_read.close()
                            write_file = open(file_source, "w")
                            write_file.write(replaced_content)
                            write_file.close()
                            
                            file_read = open(file_source, "r")
                            replaced_content = ""
                            for line in file_read:
                                if (('FogDensity:' in line) and ((line.startswith("#")) is not True)):
                                    new_line = line.replace(line, FogDensity)
                                    line = line.strip()
                                else:
                                    new_line = line.replace(line, line)
                                replaced_content = (replaced_content + new_line)
                                
                            file_read.close()
                            write_file = open(file_source, "w")
                            write_file.write(replaced_content)
                            write_file.close()
                            
                            file_read = open(file_source, "r")
                            replaced_content = ""
                            for line in file_read:
                                if (('FogTimeWeight:' in line) and ((line.startswith("#")) is not True)):
                                    new_line = line.replace(line, FogTimeWeight)
                                    line = line.strip()
                                else:
                                    new_line = line.replace(line, line)
                                replaced_content = (replaced_content + new_line)
                                
                            file_read.close()
                            write_file = open(file_source, "w")
                            write_file.write(replaced_content)
                            write_file.close()
                            
                            file_read = open(file_source, "r")
                            replaced_content = ""
                            for line in file_read:
                                if (('FogRainWeight:' in line) and ((line.startswith("#")) is not True)):
                                    new_line = line.replace(line, FogRainWeight)
                                    line = line.strip()
                                else:
                                    new_line = line.replace(line, line)
                                replaced_content = (replaced_content + new_line)
                                
                            file_read.close()
                            write_file = open(file_source, "w")
                            write_file.write(replaced_content)
                            write_file.close()
                            
                            file_read = open(file_source, "r")
                            replaced_content = ""
                            for line in file_read:
                                if (('FogThunderWeight:' in line) and ((line.startswith("#")) is not True)):
                                    new_line = line.replace(line, FogThunderWeight)
                                    line = line.strip()
                                else:
                                    new_line = line.replace(line, line)
                                replaced_content = (replaced_content + new_line)
                                
                            file_read.close()
                            write_file = open(file_source, "w")
                            write_file.write(replaced_content)
                            write_file.close()
                            
                            file_read = open(file_source, "r")
                            replaced_content = ""
                            for line in file_read:
                                if (('BiomeDictId:' in line) and ((line.startswith("#")) is not True)):
                                    new_line = line.replace(line, BiomeDictId)
                                    line = line.strip()
                                else:
                                    new_line = line.replace(line, line)
                                replaced_content = (replaced_content + new_line)
                                
                            file_read.close()
                            write_file = open(file_source, "w")
                            write_file.write(replaced_content)
                            write_file.close()

 

        #vanilla = 0 #Number of virtual biomes that inherit from vanilla biomes.
        #parent = 0 #Number of custom parent biomes.
        #custom = 0 #Number of virtual biomes that inherit from custom biomes.
        #allbiomes = 0 #Number of all the biomes passed, both custom as vanilla.
        
        sum = float(vanilla) + float(custom)

        print("")
        print("The script has updated ",vanilla," virtual biomes inherited from vanilla biomes and ",custom," virtual biomes inherited from custom biomes for a total of ",sum," Virtual Biomes")
        print("In total, without counting vanilla biomes this preset contains ",allbiomes," biomes from which ",parent," are non-virtual biomes.")
        print("")
        

        end = input("press enter to return to menu")
        
        print("")
        print("Eagle's Handy OTG scripts")
        print("")
        print("")
        print("Thanks for using Eagle's Handy OTG scripts, Here's a list of current functions:")
        print("")
        print("1. Eagle's simple search and write script")
        print("This script searches folders & subfolders for .bc files & writes the following data to a file:")
        print("<biomename>.bc  BiomeColor: <value> SkyColor: <value>  ReplaceToBiomeName: <name or empty if not used>")
        print("BiomeTemperature: <value>  BiomeWetness: <value>  WaterColor: <value>  GrassColor: <value>  FoliageColor: <value>  BiomeDictId: <value>  InheritMobsBiomeName: <value>")
        print("FogColor: <value>  FogDensity: <value>  FogTimeWeight: <value>  FogRainWeight: <value>  FogThunderWeight: <value>")
        print("")
        print("")
        print("2. Eagle's inheritance script")
        print("This script checks the ReplaceToBiomeName value of a biome and makes sure it's contents reflect the values of the ReplaceToBiomeName biome. If the ReplaceToBiomeName value is empty it will skip the file.")
        print("")
        print("")
        print("3. Eagle's Duplicate Biomecolor Finder")
        print("This script checks all biomes for their biomecolors and outputs a list of duplicate ones making it easier to make each biome have it's own unique biomecolor. This is handy for FromImage or Hybrid worlds.")
        print("")
        print("")
        
        loop = True
        
    #------------------------------------------- SCRIPT 3 --------------------------------------------------
    
    if script == "3":
    
    #------------------------------------------- Check if biomes have duplicate biomecolors -------------------------------------------------#
        import os
        import os.path
        import fileinput
        
        print("")
        dir_path = input("Enter directory root path:")
        print("")
        
        root = dir_path
        pattern = "*.bc"
        savecolor = []
        savedupes = []
        singledupes = []
        
        for path, subdirs, files in os.walk(root):
            for name in files:
                if (fnmatch(name, pattern)):
                    file_source = os.path.join(path, name)
                    
                    file_read = open(file_source, "r")
                    lines = file_read.readlines()
                                
                    #checking line by line for biomecolor - start -
                    for line in lines:
                        # Confirmation that the source_file is a virtual biome.
                        if (("BiomeColor:" in line) and ((line.startswith("#")) is not True)):
                            
                            if (line in savecolor):
                                save_dupe = savedupes.append(line)
                            if (line not in savecolor):
                                save_fresh = savecolor.append(line)
                    
        count_dupes = len(savedupes)
        count_fresh = len(savecolor)
        
        if (count_dupes >= 1):
            print("")
            print("The script has finished searching for duplicates and has found ",count_dupes," duplications in ",count_fresh," scanned files.")
            print("")
            print("The following biomecolors are duplicated across multiple biomes:")
            print("")
            for item in savedupes:
                if (item not in singledupes):
                    print(item)
                    single_dupes = singledupes.append(item)
        if (count_dupes == 0):
            print("")
            print("Congratulations! The script has finished searching for duplicates and has found ",count_dupes," duplications in ",count_fresh," scanned files.")
            print("")
        print("")
        end = input("press enter to return to menu")
        
        print("")
        print("Eagle's Handy OTG scripts")
        print("")
        print("")
        print("Thanks for using Eagle's Handy OTG scripts, Here's a list of current functions:")
        print("")
        print("1. Eagle's simple search and write script")
        print("This script searches folders & subfolders for .bc files & writes the following data to a file:")
        print("<biomename>.bc  BiomeColor: <value>  ReplaceToBiomeName: <name or empty if not used>")
        print("BiomeTemperature: <value>  BiomeWetness: <value>  WaterColor: <value>  GrassColor: <value>  FoliageColor: <value>  BiomeDictId: <value>  InheritMobsBiomeName: <value>")
        print("")
        print("")
        print("2. Eagle's inheritance script")
        print("This script checks the ReplaceToBiomeName value of a biome and makes sure it's contents reflect the values of the ReplaceToBiomeName biome. If the ReplaceToBiomeName value is empty it will skip the file.")
        print("")
        print("")
        print("3. Eagle's Duplicate Biomecolor Finder")
        print("This script checks all biomes for their biomecolors and outputs a list of duplicate ones making it easier to make each biome have it's own unique biomecolor. This is handy for FromImage or Hybrid worlds.")
        print("")
        print("")
        
        loop = True
        