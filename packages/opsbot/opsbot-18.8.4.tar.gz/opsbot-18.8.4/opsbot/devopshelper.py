import os
import string
import random
from constant import CONSTANT
from random import randint



class OpsbotHelper:
    current_dir = None
    target_os = "ubuntu"
    target_os_version = "18.04"
    password_length = 32

    user_passwords = {}
    logs = []
    last_script = []

    hour = 0

    def __init__(self):
        self.current_dir =  os.path.dirname(os.path.realpath(__file__))

    def template(self, path):
        f = open("{}/template/{}".format(self.current_dir, path), "r")
        text = f.read()
        f.close()
        return text

    def opsbot_setting(self, params):
        scripts = []
        command = "".join(params)
        segs = command.split("=")
        field = segs[0]
        value = segs[1]
        
        if field == "password_length": 
            self.password_length = int(value)
            if self.password_length < 8 or self.password_length > 64 :
                print "Setting Password Fail!"
                print "Password length need >= 8 and <= 64"
                quit()
            scripts.append("echo 'password generated with length = {}'".format( self.password_length))            
        elif field == "target_os_version":
            self.target_os_version = value            
            if self.target_os_version not in ["16.10", "18.04"]:
                print "Build Fail!"
                print "{} version {} not support".format(self.target_os, self.target_os_version)
                quit()
            
            # scripts.append("#Check os version {}...OK".format(self.target_os_version))
            scripts.append("echo 'work on os version :{} {}'".format(self.target_os, self.target_os_version))

        elif field =="target_os":
            self.target_os = value
            if  self.target_os != "ubuntu":
                print "Build Fail!"
                print "OS {} not support".format(self.target_os)
                quit()
            # scripts.append("#Check os {}...OK".format(self.target_os))
            scripts.append("echo 'this script write for os {}'".format(self.target_os))
            
        return scripts

    def opsbot_env(self, params):
        env_name = params[0]
        scripts = []
        text = self.template("env/{}.sh".format(env_name))
        scripts.append(text)

        if(env_name == "lamp"):
            #TODO : gen password.
            #TODO: set password & auth-type
            self.user_passwords['root'] = {}
            self.user_passwords['root']['mysql'] = self.random_password()

            self.user_passwords['phpmyadmin'] = {}
            self.user_passwords['phpmyadmin']['mysql'] = self.random_password()


            if self.target_os_version == "18.04":
                text = self.template("fix/mysql-change-root-auth-type.sh")
                scripts.append(text)
            
            if self.target_os_version == "18.04":
                text = self.template("fix/phpmyadmin-upgrade-48.sh")
                scripts.append(text)
            self.last_script.append("echo \"restart apache2 after job done\"")
            self.last_script.append("systemctl restart apache2")
        elif(env_name == "mongodb"):
            self.user_passwords['root']['mongodb'] = self.random_password()
            self.last_script.append("echo \"restart mongo after job done\"")
            self.last_script.append("systemctl restart mongodb")
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
        text = self.template("user/unix.sh").format(username = username)
        scripts.append(text)
        return scripts

    def opsbot_user_mysql(self, username, prefix):
        scripts = []
        text = self.template("user/mysql.sh").format(username=username, prefix=prefix)
        scripts.append(text)
        return scripts


    def opsbot_user_mongodb(self, username, prefix):
        scripts = []
        text = self.template("user/mongodb.sh").format(username=username, prefix=prefix)
        scripts.append(text)
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
        valid_domains = ["www."+site, "dev."+site]

        scripts = []
        
        for param in params:
            if param == "--redirect-to-https":
                redirect_to_htmls = True
            elif str(param).startswith("--public_directory="):
                public_directory = str(param).split("=")[1]
            elif param.startswith("--include-domain="):
                include_domains = str(param).split("=")[1]
                include_domains_array = include_domains.split(",")
                valid_domains.extend(include_domains_array)

        access_log = "/var/www/{site}/access-{site}.log".format(site=site)
        error_log = "/var/www/{site}/error-{site}.log".format(site=site)

        self.logs.append(access_log)
        self.logs.append(error_log)

        text = self.template("site/vhost.sh").format(site=site, 
            domains=" ".join(valid_domains), 
            public_directory = public_directory, redirect_to_htmls = redirect_to_htmls,
            access_log = access_log, error_log = error_log)
        scripts.append(text)

        text = self.template("site/rule.sh").format(site = site, owner=owner,
            access_log = access_log, error_log = error_log)
        scripts.append(text)

        return scripts
        

    def opsbot_begin_block(self, params):
        scripts = []
        return scripts

    def human_readable_to_bytes(self, size):
        """Given a human-readable byte string (e.g. 2G, 10GB, 30MB, 20KB),
            return the number of bytes.  Will return 0 if the argument has
            unexpected form.
        """
        if (size[-1] == 'B' or size[-1] == 'b' ):
            size = size[:-1]
        if (size.isdigit()):
            bytes = int(size)
        else:
            bytes = size[:-1]
            unit = size[-1]
            if (bytes.isdigit()):
                bytes = int(bytes)
                if (unit == 'G'):
                    bytes *= 1073741824
                elif (unit == 'M'):
                    bytes *= 1048576
                elif (unit == 'K'):
                    bytes *= 1024
                else:
                    bytes = 0
            else:
                bytes = 0
        return bytes

    def opsbot_tool(self, params):
        cmd = params[0]
        scripts = []

        if cmd == "allow_normal_user_add_site":
            
            # BUILD ADD SITE TOOL.
            rule = self.template("site/rule.sh").format(site="$SITE", owner = "$OWNER", redirect_to_htmls="$REDIRECT_TO_HTMLS", 
                public_directory="$PUBLIC_DIRECTORY", access_log = "$ACCESS_LOG", error_log="$ERROR_LOG")
            vhost = self.template("site/vhost.sh").format(site="$SITE", owner = "$OWNER", redirect_to_htmls="$REDIRECT_TO_HTMLS", 
                public_directory="$PUBLIC_DIRECTORY", access_log = "$ACCESS_LOG", error_log="$ERROR_LOG", domains="$DOMAINS")
            vhost_ssl =  self.template("site/vhost-ssl.sh").format(site="$SITE", owner = "$OWNER", redirect_to_htmls="$REDIRECT_TO_HTMLS", 
                public_directory="$PUBLIC_DIRECTORY", access_log = "$ACCESS_LOG", error_log="$ERROR_LOG", domains="$DOMAINS")
            tool_add_site = self.template("tool/tool_add_site.sh").format(script_site_rule=rule, script_site_vhost = vhost, script_site_vhost_ssl = vhost_ssl)
            
            return self.make_tool_available_global(tool_add_site,CONSTANT.TOOL_ADD_SITE_NAME)

        elif cmd == "allow_normal_user_certbot":
            #make tool safe_certbot.
            safe_certbot = self.template("tool/tool_safe_certbot.sh")
            return self.make_tool_available_global(safe_certbot,CONSTANT.TOOL_SAFE_CERTBOT_NAME)            

        elif cmd == "auto_reset_log":
            #write tool
            reset_log_sh = self.template("tool/tool_reset_log.sh")
            scripts = self.make_tool_available_global(reset_log_sh, "reset_log")

            #make contab.
            maximum_bytes = 50 * 1024 * 1024 
            for param in params:
                if param.startswith("--max-size=") :
                    max_size = param.split("=")[1]
                    # print max_size
                    maximum_bytes = self.human_readable_to_bytes(max_size)

            for log in self.logs:
                script = "reset_log \"{log}\" {maximum_bytes}".format(log = log, maximum_bytes = maximum_bytes)
                scripts.extend(self.opsbot_make_contab_daily(script))
            return scripts

           
    def make_tool_available_global(self, tool_sh, tool_command):        
        scripts = []

        #create tool
        if not os.path.exists(CONSTANT.DEFAULT_OUTPUT_TOOL_DIR):
            os.makedirs(CONSTANT.DEFAULT_OUTPUT_TOOL_DIR)
        path = "{}/{}.sh".format(CONSTANT.DEFAULT_OUTPUT_TOOL_DIR, tool_command) 
        f = open(path, "wb")
        f.write(tool_sh)
        f.close()

        scripts.append("echo \"tool {} build in  {}\"\n".format(tool_command, path))


        #make tool avaiable global
        text = self.template("tool/allow_normal_user_use_tool.sh").format(path=path, tool_command = tool_command)
        scripts.append(text)
        return scripts

    
    def opsbot_make_contab_daily(self, command):
        scripts = []
        self.hour = (self.hour+1) % 24
        minute = randint(0,59)
        scripts.append(self.template("tool/make_crontab_daily.sh").format(hour=self.hour, minute=minute, command = command))
        return scripts