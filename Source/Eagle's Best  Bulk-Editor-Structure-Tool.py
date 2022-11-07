import os
import os.path
from os import path
from fnmatch import fnmatch
from pathlib import Path
import shutil
import re
import sys

first = True

print("")


print("███████╗░█████╗░░██████╗░██╗░░░░░███████╗██╗░██████╗  ██████╗░███████╗░██████╗████████╗  ".center(100))
print("██╔════╝██╔══██╗██╔════╝░██║░░░░░██╔════╝╚█║██╔════╝  ██╔══██╗██╔════╝██╔════╝╚══██╔══╝  ".center(100))
print("█████╗░░███████║██║░░██╗░██║░░░░░█████╗░░░╚╝╚█████╗░  ██████╦╝█████╗░░╚█████╗░░░░██║░░░  ".center(100))
print("██╔══╝░░██╔══██║██║░░╚██╗██║░░░░░██╔══╝░░░░░░╚═══██╗  ██╔══██╗██╔══╝░░░╚═══██╗░░░██║░░░  ".center(100))
print("███████╗██║░░██║╚██████╔╝███████╗███████╗░░░██████╔╝  ██████╦╝███████╗██████╔╝░░░██║░░░  ".center(100))
print("╚══════╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚══════╝░░░╚═════╝░  ╚═════╝░╚══════╝╚═════╝░░░░╚═╝░░░  ".center(100))
print("")
print("Eagle's Best | Bulk-Editor-Structure-Tool".center(100))
print("")
print("")
print("Thanks for using Eagle's Best, a bulk editor structure tool that finds and replaces blocks for".center(100))
print("e.g. entities and/or blocks without messing with the coordinates".center(100))
print("")


while True:

    missing = []

    #Check if Config Exists
    current_path = os.getcwd()
    config = current_path+"\Eagle's Best Config.txt"
    isConfig = os.path.isfile(config)

    #Check if SourceFolder Exists
    sourcefolder = current_path+"\Eagle's Best SourceFolder"
    isSourcefolder = os.path.isdir(sourcefolder)

    #Check if OutputFolder Exists
    outputfolder = current_path+"\Eagle's Best OutputFolder"
    isOutputefolder = os.path.isdir(outputfolder)

    if isConfig != True:
        missing.append("Eagle's Best Config")
    if isSourcefolder != True:
        missing.append("Eagle's Best SourceFolder")
    if isOutputefolder != True:
        missing.append("Eagle's Best OutputFolder")
        

        
        
    if missing != []:

        print("The following files seem to be missing;".center(100))
        print(f" {missing} ".center(100))
        bad = input("press any key to generate them".center(100))
        print("")
        #Generate Config
        if isConfig != True:
        
            default = ["#Eagle's Best (Bulk-Editor-Structure-Tool) Config\n\n",

            "Remove Comments (true/false): false\n",
            "#removes all comments from the bo3/bo4 file.\n\n",

            "Extrude Blocks: None\n",
            "#Changing None into BEDROCK:0, IRON_BLOCK:0 would remove all BEDROCK:0 and IRON_BLOCK:0 blocks from bo3/bo4 file.\n\n",
            
            "Replace NBT data (true/false): false\n",
            "#Chest:1* will replace all NBT data.\n\n",

            "Remove # to enable: (Sponge:* will replace all datavalues of Sponge)\n",
            "#Block -> Block | SPONGE:*               -> EMERALD_BLOCK:0\n",
            "#Block -> RandomBlock | STONE:0          -> SMOOTH_BRICK,40,SMOOTH_BRICK:1,50,SMOOTH_BRICK:2,40,COBBLESTONE,100\n",
            "#Block -> Entity | OBSIDIAN:0            -> villager,1,nbtdata.nbt\n"
            "#Block -> Block | CHEST:1,*               -> CHEST:1,chest.nbt\n"
            ]
            
            with open("Eagle's Best Config.txt", 'w') as f:
                f.writelines(default)
                
                
        #Generate Source Folder
        if isSourcefolder != True:
            os.makedirs(sourcefolder)
            
        #Generate Output Folder
        if isOutputefolder != True:
            os.makedirs(outputfolder)
            
            
    #Check if config is default or not
    
    
    loop = True
    while loop == True:
                      
        config_read = open(config, "r")
        lines = config_read.readlines()
        
        default = ["#Eagle's Best (Bulk-Editor-Structure-Tool) Config\n\n", 'Remove Comments (true/false): false\n', '#removes all comments from the bo3/bo4 file.\n\n', 'Extrude Blocks: None\n', '#Changing None into BEDROCK:0, IRON_BLOCK:0 would remove all BEDROCK:0 and IRON_BLOCK:0 blocks from bo3/bo4 file.\n\n', 'Replace NBT data (true/false): false\n', '#Chest:1* will replace all NBT data.\n\n', 'Remove # to enable: (Sponge:* will replace all datavalues of Sponge)\n', '#Block -> Block | SPONGE:*               -> EMERALD_BLOCK:0\n', '#Block -> RandomBlock | STONE:0          -> SMOOTH_BRICK,40,SMOOTH_BRICK:1,50,SMOOTH_BRICK:2,40,COBBLESTONE,100\n', '#Block -> Entity | OBSIDIAN:0            -> villager,1,nbtdata.nbt\n#Block -> Block | CHEST:1,*               -> CHEST:1,chest.nbt\n']

        if (lines == default):
            print("No changes have been made to the config, please adjust accordingly".center(100))
            bad = input("Press any key to refresh and continue".center(100))
            print("")
        else:
            if (first == True):
                good = input("Press any key to execute the script.".center(100))
                print("")
                loop = False
                first = False
            else:
                good = input("Press any key to re-execute the script.".center(100))
                print("")
                loop = False
            
            
    #list all objects that should be changed:
    modified_blocks = []
    extrude_blocks = []
    totalcount = 0
    count = 0

    config_read = open(config, "r")
    lines = config_read.readlines()

    for line in lines:
        if (line.startswith("Remove Comments (true/false):")):
            if not ((line.endswith("false")) or (line.endswith("False"))):
                uncomment = True
        if (line.startswith("Replace NBT data (true/false):")):
            if not ((line.endswith("false")) or (line.endswith("False"))):
                replacenbt = True
        if (line.startswith("Block ->")):
            modified_blocks.append(line)
        if ("Extrude Blocks:" in line):
            k = (line.split(":", 1)[1].strip())
            if ("None" not in k):
                k = k.lower()
                h = k.replace(" ", "")
                extrude_blocks = (h.split(","))

            
    #Copy files to output folder if these are .bo3 or .bo4
    patterns = ["*.bo3","*.bo4"]

    for path, subdirs, files in os.walk(current_path):
        for name in files:
            for p in patterns:
                if (fnmatch(name, p)):
                    if ("Eagle's Best SourceFolder" in path):
                        totalcount+=1
                        
    count = 0
    SourceFolder = []

    for path, subdirs, files in os.walk(current_path):
        for name in files:
            for p in patterns:
                if (fnmatch(name, p)):
                    if ("Eagle's Best SourceFolder" in path):

                        file_source = os.path.join(path, name)
                        file_target = os.path.join(outputfolder, name)
                        
                        file_read = open(file_source, "r")
                        lines = file_read.readlines()
                        file_read.close()
                        
                        file_create = open(file_target, "w")
                        file_create.writelines(lines)
                        file_create.close()
                        
                        SourceFolder.append(name)
                        
                        count+=1
                        print("{} out of {} files have been scanned".format(count,totalcount).center(100), end='\r')
                        
                        

        #lines corrospond in following:
        #OriginalBlock = Block it is
        #BlockTypeToConvertTo = Block, RandomBlock or Entity.
        #endstring = pasted after coordinates
        
        #Dissect lines

        #OBSIDIAN:0 -> EXTRUDE
        #OBSIDIAN:0 -> Block|SPONGE:0
        #OBSIDIAN:0 -> RandomBlock|OBSIDIAN:0,20,SPONGE:0,20,AIR:0,20,STONE:0,20
        #OBSIDIAN:0 -> Entity|Villager,1,nbtfile.nbt       
             
    count = 0

             
    for path, subdirs, files in os.walk(current_path):
        for name in files:
            
            for p in patterns:
                if (fnmatch(name, p)):
                    if (("Eagle's Best OutputFolder" in path) and (name in SourceFolder)):
                    
                        ############################################# Comments Replacer ##############################################################
                        file_target = os.path.join(outputfolder, name)
                        file_source = open(file_target, "r")
                        lines = file_source.readlines()
                        file_read = open(file_target, "r")
                        searchblocks = []
                        convertblocks = []
                        wildcardblocks = []
                        convertwildblocks = []
                        convertnbtblocks = []
                        
                        for entries in modified_blocks:
                            x = entries.split("|")[-1]
                            y = x.split("->")[0].strip()
                            # y is block to search for
                            a = x.split("->")[-1].strip()
                            # a = block to replace y with.
                            z = entries.split("|")[0]
                            m = z.split("->")[1]
                            i = (y+"|"+a+"|"+m)
                            y = y.lower()

                            if (":*" in y):
                                g = y.replace(":*", "")
                                wildcardblocks.append(g)
                                convertwildblocks.append(i)
                            else:
                                searchblocks.append(y)
                                convertblocks.append(i)
                                
                            if (",*" in y):
                                g = y.replace(",*", ",")
                                i = (y+"|"+a+"|"+m)
                                convertnbtblocks.append(i.lower())
                        
                        replaced_content = ""
                        
                        for line in lines:
                            new_line = line.replace(line, line)
                            if ((uncomment == True) and (line[0] == "#")):
                                if ((line.startswith("##")) or (line.startswith("# +")) or (line.startswith("# |")) or (line.startswith("# Height Limits for the"))):
                                    new_line = line.replace(line, line)
                                else:
                                    new_line = line.replace(line, "")
                            replaced_content = (replaced_content + new_line)
                            
                        write_file = open(file_target, "w")
                        write_file.write(replaced_content)
                        write_file.close()
                        file_read.close()
                        file_source.close()
                        
                        ############################################ NBT Data Replacer ##############################################################
                        
                        if ((convertnbtblocks != []) and (replacenbt == True)):
                            
                            file_target = os.path.join(outputfolder, name)
                            file_source = open(file_target, "r")
                            lines = file_source.readlines()
                            file_read = open(file_target, "r")
                            replaced_content = ""
                            

                            for line in lines:
                                new_line = line.replace(line, line)
                                low_line = line.lower()
                                if ((low_line.startswith("b(")) or (low_line.startswith("block("))):
                                    if (",minecraft:" in line):
                                        line = line.replace("minecraft:", "")
                            
                                    splitline = line.split(",")
                                    lowline = (splitline[3].lower())
                                    

                                    
                                    if any(lowline in s for s in convertnbtblocks):

                                        for block in convertnbtblocks:
                                            convertfrom = (block.split("|")[0])
                                            convertto = (block.split("|")[1]+")")
                                            if (lowline in convertfrom):
                                                
                                                replacecontent = (splitline[3]+","+splitline[4])
                                                new_line = line.replace(replacecontent, convertto+"\n")
                                                

                                        
                                replaced_content = (replaced_content + new_line)
                                       
                            write_file = open(file_target, "w")
                            write_file.write(replaced_content)
                            write_file.close()
                            file_read.close()
                            file_source.close()

                                    
                        ############################################ Wildcard Block Replacer ##############################################################
                        
                        
                        if (wildcardblocks != []):
                            
                            file_target = os.path.join(outputfolder, name)
                            file_source = open(file_target, "r")
                            lines = file_source.readlines()
                            file_read = open(file_target, "r")
                            replaced_content = ""
                            

                            for line in lines:
                                new_line = line.replace(line, line)
                                low_line = line.lower()
                                if ((low_line.startswith("b(")) or (low_line.startswith("block("))):
                                    if (",minecraft:" in line):
                                        line = line.replace("minecraft:", "")
                                    
                                    u = line.split(",")[-1].split(')')[0].lower()
                                    
                                    if ("minecraft:" in line):
                                        h = u.split(":", 1)[-1]
                                        j = h.split(":", 1)[0]
                                    else:
                                        j = u.split(":", 1)[0]
                                        

                                    if (j in wildcardblocks):

                                        for item in convertwildblocks:
                                            itemlow = item.lower()
                                            if j in itemlow:

                                                convertfrom = item.split('|')[0].lower()
                                                convertto = item.split('|')[1]
                                                converttype = item.split('|')[2].strip()
                                                
                                                low_line = line.lower()
                                                
                                                new_line = low_line.replace(u, convertto)
                                                
                                                blocktype = line.split("(", 1)[0].lower()
                                                blocktype = (blocktype+"(")
                                                converttype = (converttype+"(")
                                                new_line = new_line.replace(blocktype, converttype)
                                                
                                                if ("Entity(" in converttype):
                                                    air_line = new_line.replace(convertto, "AIR:0")
                                                    air_line = air_line.replace("Entity(", "Block(")
                                                    new_line = (new_line+air_line)
                                                if ("E(" in converttype):
                                                    air_line = new_line.replace(convertto, "AIR:0")
                                                    air_line = air_line.replace("E(", "B(")
                                                    new_line = (new_line+air_line)
                                                

                                                
                                replaced_content = (replaced_content + new_line)
                                       
                            write_file = open(file_target, "w")
                            write_file.write(replaced_content)
                            write_file.close()
                            file_read.close()
                            file_source.close()
                            
                        ############################################ BLOCK -> BLOCK replacer ##############################################################
                        
                        file_target = os.path.join(outputfolder, name)
                        file_source = open(file_target, "r")
                        lines = file_source.readlines()
                        file_read = open(file_target, "r")
                        replaced_content = ""

                        for line in lines:
                            new_line = line.replace(line, line)
                            low_line = line.lower()
                            if ((low_line.startswith("b(")) or (low_line.startswith("block("))):
                                if (",minecraft:" in line):
                                    line = line.replace("minecraft:", "")
                                
                                u = line.split(",")[-1].split(')')[0].lower()
                                
                                
                                
                                if (u in searchblocks):
                                    u = (u+"|")
                                    for item in convertblocks:
                                    
                                        itemlow = item.lower()
                                        if u in itemlow:

                                            convertfrom = item.split('|')[0].lower()
                                            convertto = item.split('|')[1].strip()
                                            converttype = item.split('|')[2].strip()
                                            convertfrom = convertfrom.strip()
                                            
                                            low_line = line.lower()
                                            new_line = low_line.replace(convertfrom, convertto)
                                            

                                            
                                            
                                            blocktype = line.split("(", 1)[0].lower()
                                            blocktype = (blocktype+"(")
                                            converttype = (converttype+"(")
                                            new_line = new_line.replace(blocktype, converttype)


                                            if ("Entity(" in converttype):
                                                air_line = new_line.replace(convertto, "AIR:0")
                                                air_line = air_line.replace("Entity(", "Block(")
                                                new_line = (new_line+air_line)
                                            if ("E(" in converttype):
                                                air_line = new_line.replace(convertto, "AIR:0")
                                                air_line = air_line.replace("E(", "B(")
                                                new_line = (new_line+air_line)

                            
                            replaced_content = (replaced_content + new_line)
                                   
                        write_file = open(file_target, "w")
                        write_file.write(replaced_content)
                        write_file.close()
                        file_read.close()
                        file_source.close()
                        
                        ############################################ Blocks Extruder ##############################################################
                        
                        if (extrude_blocks != []):

                            
                            file_target = os.path.join(outputfolder, name)
                            file_source = open(file_target, "r")
                            lines = file_source.readlines()
                            file_read = open(file_target, "r")
                            replaced_content = ""

                            for line in lines:
                                new_line = line.replace(line, line)
                                low_line = line.lower()
                                if ((low_line.startswith("b(")) or (low_line.startswith("block("))):
                                    if (",minecraft:" in line):
                                        line = line.replace("minecraft:", "")
                                    u = line.split(",")[-1].split(')')[0].lower()
                                    if (u in extrude_blocks):
                                        new_line = line.replace(line, "")
                                    else:
                                        new_line = line.replace(line, line)
                                                
                                replaced_content = (replaced_content + new_line)
                                       
                            write_file = open(file_target, "w")
                            write_file.write(replaced_content)
                            write_file.close()
                            file_read.close()
                            file_source.close()
                            
                        count+=1
                        print("{} out of {} files have been processed".format(count,totalcount).center(100), end='\r')
                           

    config_read.close()                       
    print("{} out of {} files have been processed".format(count,totalcount).center(100))

    print("")
    print(" ///,        ////".center(100))
    print(" \  /,      /  >.".center(100))
    print("  \  /,   _/  /. ".center(100))
    print("   \_  /_/   /.  ".center(100))
    print("    \__/_   <    ".center(100))
    print("    /<<< \_\_    ".center(100))
    print("   /,)^>>_._ \   ".center(100))
    print("   (/   \\\\ /\\\\\\  ".center(100))
    print("        // ````  ".center(100))
    print("       ((`       ".center(100))
    print("")

    #print("                 ".center(100))
    #print("                 ".center(100))
    #print("                 ".center(100))
    #print("                 ".center(100))
    #print("     __ ___      ".center(100))
    #print("    /<<\   \_    ".center(100))
    #print("   /,)^>>\\  \_  ".center(100))
    #print("   (/ / \\\\_  \ ".center(100))
    #print("   //// //   \\\\".center(100))
    #print("       ((`=      ".center(100))

    print("Thank you for using Eagle's Best!".center(100))
    print("")









