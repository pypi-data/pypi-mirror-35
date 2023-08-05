import os
import string
import random
from constant import CONSTANT

class OpsbotHelper:
    current_dir = None
    target_os = "ubuntu"
    target_os_version = "18.04"
    password_length = 32

    user_passwords = {}

    def __init__(self):
        self.current_dir =  os.path.dirname(os.path.realpath(__file__))

    def opsbot_setting(self, params):
        scripts = []
        field = params[0]
        value = params[1]
        
        if field == "password_length": 
            self.password_length = int(value)
            if self.password_length >= 8 and self.password_length <= 512 :
                scripts.append("#Set password_length = {}...OK".format( self.password_length))            
        elif field == "target_os_version":
            self.target_os_version = value            
            if self.target_os_version not in ["16.10", "18.04"]:
                print "Build Fail!"
                print "{} version {} not support".format(self.target_os, self.target_os_version)
                quit()
            scripts.append("#Check os version {}...OK".format(self.target_os_version))
        elif field =="target_os":
            self.target_os = value
            if  self.target_os != "ubuntu":
                print "Build Fail!"
                print "OS {} not support".format(self.target_os)
                quit()
            scripts.append("#Check os {}...OK".format(self.target_os_version))
        return scripts

    def opsbot_env(self, params):
        env_name = params[0]
        scripts = []
        envshFile = open("{}/template/env/{}.sh".format(self.current_dir, env_name))
        scripts.append(envshFile.read())

        if(env_name == "lamp"):
            #TODO : gen password.
            #TODO: set password & auth-type
            self.user_passwords['root'] = {}
            self.user_passwords['root']['mysql'] = self.random_password()

            self.user_passwords['phpmyadmin'] = {}
            self.user_passwords['phpmyadmin']['mysql'] = self.random_password()


            if self.target_os_version == "18.04":
                fixFile = open("{}/template/fix/mysql-change-root-auth-type.sh".format(self.current_dir))
                scripts.append(fixFile.read())
            
            if self.target_os_version == "18.04":
                fixFile = open("{}/template/fix/phpmyadmin-upgrade-48.sh".format(self.current_dir))
                scripts.append(fixFile.read())
        
        return scripts
    

    def random_password(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(self.password_length))

    def opsbot_account(self):
        scripts = []

        for user in self.user_passwords:
            for service in self.user_passwords[user]:
                varname = "{}_{}_password".format(user, service)
                scripts.append("{}=\"{}\"".format(varname, self.user_passwords[user][service]))
        return scripts
    
    def opsbot_user_unix(self, username):
        scripts = []
        f = open("{}/template/user/{}.sh".format(self.current_dir, "unix"))
        sh = f.read()
        scripts.append(sh.format(username = username))
        return scripts

    def opsbot_user_mysql(self, username, prefix):
        scripts = []
        f = open("{}/template/user/{}.sh".format(self.current_dir, "mysql"))
        sh = f.read()
        scripts.append(sh.format(username=username, prefix=prefix) )
        return scripts

    def opsbot_user_mongodb(self, username, prefix):
        scripts = []
        f = open("{}/template/user/{}.sh".format(self.current_dir, "mongodb"))
        sh = f.read()
        scripts.append(sh.format(username=username, prefix=prefix))
        return scripts
    
    def opsbot_user(self, params):
        scripts = []
        username = params[0]
        self.user_passwords[username] = {}
        self.user_passwords[username]['unix'] = self.random_password()
        scripts.extend(self.opsbot_user_unix(username))

        #TODO: parse param here
        mongo_enabled = False
        mysql_enabled = False
        database_prefix = username
        #print params
        for param in params:
            if param == "--mongodb" or param == "--mongo":
                mongo_enabled = True
            elif param == "--mysql":
                mysql_enabled = True
            elif str(param).startswith("--database-prefix="):
                database_prefix = str(param).split("=")[1]
        #print "mongo_enable {} mysql_enable {} database_prefix {}".format(mongo_enabled, mysql_enable, database_prefix)       

        if mysql_enabled:
            self.user_passwords[username]['mysql'] = self.random_password()
            scripts.extend(self.opsbot_user_mysql(username, database_prefix))

        if mongo_enabled:
            self.user_passwords[username]['mongodb'] = self.random_password()
            scripts.extend(self.opsbot_user_mongodb(username, database_prefix))

        return scripts

    def opsbot_site(self, params):
        site = params[0]
        owner = params[1]
        public_directory = "html"
        redirect_to_htmls = 0

        scripts = []
        
        for param in params:
            if param == "--redirect-to-https":
                redirect_to_htmls = True
            elif str(param).startswith("--public_directory="):
                public_directory = str(param).split("=")[1]


        f = open("{}/template/site/vhost.sh".format(self.current_dir))
        sh = f.read()
        f.close()
        scripts.append(sh.format(site=site, public_directory = public_directory, redirect_to_htmls=redirect_to_htmls ))

        f = open("{}/template/site/rule.sh".format(self.current_dir))
        sh = f.read()
        f.close()
        scripts.append(sh.format(site=site, owner=owner))       

        return scripts
        

    def opsbot_begin_block(self, params):
        scripts = []
        return scripts
    
    def opsbot_tool(self, params):
        cmd = params[0]
        scripts = []

        if cmd == "allow_normal_user_add_site":
            
            # BUILD ADD SITE TOOL.
            f0 = open ("{}/template/tool/tool_add_site.sh".format(self.current_dir))
            f1 = open ("{}/template/site/rule.sh".format(self.current_dir))
            f2 = open ("{}/template/site/vhost.sh".format(self.current_dir))
            f3 = open ("{}/template/site/vhost-ssl.sh".format(self.current_dir))
            script_site_rule = f1.read().format(site="$SITE", owner = "$OWNER") + "\n" 
            script_site_vhost = f2.read().format(site="$SITE", owner = "$OWNER", redirect_to_htmls="$REDIRECT_TO_HTMLS", public_directory="$PUBLIC_DIRECTORY") + "\n" 
            script_site_vhost_ssl =  f3.read().format(site="$SITE", owner = "$OWNER", redirect_to_htmls="$REDIRECT_TO_HTMLS", public_directory="$PUBLIC_DIRECTORY")  + "\n"
            tool_add_site = f0.read().format(script_site_rule=script_site_rule, script_site_vhost = script_site_vhost, script_site_vhost_ssl = script_site_vhost_ssl)
            
            if not os.path.exists(CONSTANT.DEFAULT_OUTPUT_TOOL_DIR):
                os.makedirs(CONSTANT.DEFAULT_OUTPUT_TOOL_DIR)
            toolFilePath = "{}/{}".format(CONSTANT.DEFAULT_OUTPUT_TOOL_DIR, CONSTANT.TOOL_ADD_SITE_NAME)

            toolFile = open(toolFilePath, "wb")
            toolFile.write(tool_add_site)

            f0.close(); f1.close(); f2.close();  f3.close()


            f = open ("{}/template/tool/allow_normal_user_add_site.sh".format(self.current_dir))
            scripts.append(f.read().format(tool_add_site_path=toolFilePath))
            f.close()

            return scripts

        elif cmd == "allow_normal_user_certbot":
            #make tool safe_certbot.
            f0 = open ("{}/template/tool/tool_safe_certbot.sh".format(self.current_dir))

            if not os.path.exists(CONSTANT.DEFAULT_OUTPUT_TOOL_DIR):
                            os.makedirs(CONSTANT.DEFAULT_OUTPUT_TOOL_DIR)
            toolFilePath = "{}/{}".format(CONSTANT.DEFAULT_OUTPUT_TOOL_DIR, CONSTANT.TOOL_SAFE_CERTBOT_NAME)   
            fwrite = open(toolFilePath, "wb")
            fwrite.write(f0.read())
            fwrite.close(); fwrite.close()

            #wri
            f = open ("{}/template/tool/allow_normal_user_certbot.sh".format(self.current_dir), "r")
            scripts.append(f.read().format(tool_safe_certbot_path=toolFilePath))
            f.close()
            
            return scripts