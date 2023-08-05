 #!/usr/bin/python
 # -*- coding: utf-8 -*-
  
import argparse
import os
import pprint
from constant import CONSTANT
from devopshelper import OpsbotHelper

def init():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    templateFile =  open(dir_path+"/template/"+".opsbot.template", "r")
    templateText = templateFile.read()
    templateFile.close()

    devopsFile = open(CONSTANT.DEFAULT_OPSBOT_PLAN,"w+")
    devopsFile.write(templateText.replace(r"\r\n", "\n").replace(r"\r", "\n"))
    devopsFile.close()

    print "File {} created".format(CONSTANT.DEFAULT_OPSBOT_PLAN)
    print "Please open this file to write out your devops plan.".format(CONSTANT.DEFAULT_OPSBOT_PLAN)
    return 0

def build():    
    dir_path = os.path.dirname(os.path.realpath(__file__))

    devopsFile = open(CONSTANT.DEFAULT_OPSBOT_PLAN,"r")
    lines = devopsFile.readlines()
    current_block = ""
    
    commands = []
    for line in lines:
        sline = line.strip()
        
        if (sline.startswith("[")):
            current_block = sline[1:len(sline)-1]
            # commands.append({"command": "begin_block", "params":[current_block]})
        elif sline != "" and not sline.startswith("#"):
            params = sline.split(" ")
            commands.append({"command": current_block, "params":params})

    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(commands)

    scriptblocks = []
    sh = ""
    opsbot = OpsbotHelper()
    for command in commands:
        functionName = "opsbot_" + command['command']
        method_to_call = getattr(opsbot, functionName)
        scripts = method_to_call(command['params'])
        if scripts != None and len(scripts) > 0 :
            heading = "\n# > {} > {}\n".format(command['command'], (" ").join(command['params'])).upper()

        scriptblocks.append(heading)  
        scriptblocks.extend(scripts)

    #passwords.
    account_block_sh = "\n".join(opsbot.opsbot_account())

    #scripts
    script_block_sh = "\n".join(scriptblocks)

    #last script
    final_block_sh  = "\n".join(opsbot.last_script)

    #
    f =  open(dir_path+"/template/"+"opsbot_generated.sh.template", "r")
    full_script = f.read().format(account_block=account_block_sh, 
        script_block=script_block_sh,
        final_block = final_block_sh )
    f.close()

    f = open(CONSTANT.DEFAULT_OUTPUT_BASH, "wb")
    f.write(full_script.replace(r"\r\n", "\n").replace(r"\r", "\n"))
    f.close()

    os.chmod(CONSTANT.DEFAULT_OUTPUT_BASH, 700)

    print "Build complete! "
    print "Type ./{} to run automatically devops ".format(CONSTANT.DEFAULT_OUTPUT_BASH)
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