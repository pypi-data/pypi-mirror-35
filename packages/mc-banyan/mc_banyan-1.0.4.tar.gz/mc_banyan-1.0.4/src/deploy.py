import os


def init_deploy(root_folder, project_name, config_name, build_handler, run_handler, error_handler):
    '''
build_handler: (configuration_folder, banayan_configuration_name)，if the configuration_folder has not already created, build_handler will be called.
run_handler: (configuration_folder), if the configuration_folder has already been created, it will call this handler
error_handler: (msg), raise error message friendly.
'''
    def banyan_config_path():
        return os.path.join(root_folder, project_name, "deploy", "banyan.cfg" if config_name == None else config_name + ".cfg")

    def config_path():
        return os.path.join(root_folder, project_name, "deploy", ".banyan" if config_name == None else "." + config_name)
    
    def check_structure():
        def check(path):
            return "%s is not existing" % path if not os.path.exists(path) else None
        return check(banyan_config_path())









    if check_structure():
        error_handler(check_structure())

    if os.path.exists(config_path()):
        run_handler(config_path())

    if not os.path.exists(config_path()):
        build_handler(config_path(), banyan_config_path())


def run_deploy(configuration_path):
    '''configuration_path: it is the folder path which contains the main.sh to launch the deploy script'''
    import subprocess
    
    def run(current_path):
        try:
            os.chdir(configuration_path)
            p = subprocess.Popen("bash main.sh", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

            while p.poll() is None:
                line = p.stdout.readline()
                if line:
                    print(line.strip())
        finally:
            os.chdir(current_path)

    run(os.getcwd())
