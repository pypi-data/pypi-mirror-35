 #!/usr/bin/python
 # -*- coding: utf-8 -*-
  
import argparse
import os
import pprint
from constant import CONSTANT
from devopshelper import OpsbotHelper
import time


def init():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    templateFile =  open(dir_path+"/template/"+".opsbot.template", "r")
    templateText = templateFile.read()
    templateFile.close()

    devopsFile = open(CONSTANT.DEFAULT_OPSBOT_PLAN,"w+")
    devopsFile.write(templateText.replace(r"\r\n", "\n").replace(r"\r", "\n"))
    devopsFile.close()

    print("File {} created".format(CONSTANT.DEFAULT_OPSBOT_PLAN))
    print("Please open this file to write out your devops plan.")
    return 0

def build():    
    dir_path = os.path.dirname(os.path.realpath(__file__))

    devopsFile = open(CONSTANT.DEFAULT_OPSBOT_PLAN,"r")
    lines = devopsFile.readlines()
    current_block = ""
    
    commands = []

    previousline=""

    for line in lines:
        currentline = line.strip()
        currentline = previousline + currentline

        if currentline.endswith("\\"):
            previousline = currentline[0:len(currentline)-1]
            continue        
        if currentline.startswith("#"):
            continue
        if currentline == "":
            continue
        
        if currentline.startswith("["):
            current_block = currentline[1:len(currentline)-1]
            previousline = ""
        else:
            params = currentline.split(" ")
            commands.append({"command": current_block, "params":params})
            previousline = ""
       


    #TODO : Check valid commands.

    opsbot = OpsbotHelper()

    if opsbot.compile(commands) == 0:
        exit

    pp = pprint.PrettyPrinter(indent=2, width=120)
    #pp.pprint(commands)
    
    scriptblocks = []
    for command in commands:
        functionName = "opsbot_" + command['command']
        method_to_call = getattr(opsbot, functionName)
        scripts = method_to_call(command['params'])
        if scripts != None and len(scripts) > 0 :
            heading = "# > {} > {}".format(command['command'], (" ").join(command['params'])).upper()
            print(heading)
            heading = "\n" + heading +"\n"
            time.sleep(.100)
        scriptblocks.append(heading)  
        scriptblocks.extend(scripts)

    #passwords.
    account_block_sh = "\n".join(opsbot.opsbot_account())

    # print scriptblocks[29]
    #scripts
    script_block_sh = "\n".join(scriptblocks)

    #last script
    final_block_sh  = "\n".join(opsbot.last_script)

    #
    f =  open(dir_path+"/template/"+"opsbot_generated.sh.template", "r")
    full_script = f.read().format(account_block=account_block_sh, 
        script_block=script_block_sh,
        final_block = final_block_sh,
        admin = opsbot.admin )
    f.close()

    f = open(CONSTANT.DEFAULT_OUTPUT_BASH, "wb")
    f.write(full_script.replace(r"\r\n", "\n").replace(r"\r", "\n"))
    f.close()

    os.chmod(CONSTANT.DEFAULT_OUTPUT_BASH, 0o777)

    print("Build complete! ")
    print( "Type ./{} to run automatically devops ".format(CONSTANT.DEFAULT_OUTPUT_BASH))
    #begin run
    
    return 0

def main():
    parser = argparse.ArgumentParser(description=u'I\'m Opsbot. I can help you build the best devops scripts.')
    subparsers = parser.add_subparsers(help='Avaiable commands',  dest='command')

    subparsers.add_parser('init', help='Create .opsbot file, where you will write devops plan')

    build_parser = subparsers.add_parser('build', help='Build .opsbot file. export devops scripts')
    build_parser.add_argument('--output', '-o', help='The output bash script file path')    

    PARSER = parser.parse_args()
    if PARSER.command == "init" :
        init()
    elif PARSER.command == "build":
        build()

if __name__ == "__main__":
    main()