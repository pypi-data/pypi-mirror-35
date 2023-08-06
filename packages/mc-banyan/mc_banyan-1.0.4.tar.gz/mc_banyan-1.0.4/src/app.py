from .defaults import write as write_defaults, override_values, all as all_defaults
from .roles import build as roles_build, link as roles_link, load as roles_load
from .debug import simple as debug_simple
from .banyan_opt import get_options
import sys
import os
import yaml
from .tools.file import get_file_name, get_file_only_name, put_file
from .tools.folder import put_folder
import demjson
from .deploy import init_deploy, run_deploy
import logging
logging.basicConfig(stream = sys.stdout, level = 'DEBUG')

def run(options):
    
    def build_deploy_script(target_folder, cfg_file_path): #yml_file_path#
        yml_file_folder = lambda: put_folder(os.path.abspath(target_folder))
        yml_file_path = lambda: os.path.join(yml_file_folder(), "main.yml")
        host_file = lambda: os.path.join( \
            yml_file_folder(), \
            debug_simple(get_file_only_name(yml_file_path()), "host file name") + ".host")
        bash_file = lambda: os.path.join( \
                                          yml_file_folder(),
                                          get_file_only_name(yml_file_path()) + ".sh")

                                           
        def build(file, roles_data):
            # write data to file
            file.write(roles_build(roles_data))
            # build link for role folders
            roles_link(roles_data, \
                       debug_simple(yml_file_folder(), "link_root") \
            )
            # build inventory files on roles
            write_defaults(host_file(), \
                           override_values( \
                                                     demjson.decode_file(cfg_file_path), \
                                                     all_defaults(yml_file_folder(), \
                                                                  [role["name"] for role in roles_data] \
                                                                  ) \
                                                     ) \
                           )
            # build the bash file
            open(bash_file(), "w") \
                .write("sudo ansible-playbook ./{yml_file} -i ./{host_file}" \
                       .format(yml_file = get_file_name(put_file(yml_file_path())), \
                               host_file = get_file_name(host_file()) \
                       ) \
                )

            
        build(open(put_file(yml_file_path()), 'w'), \
              roles_load(cfg_file_path) \
        )

        run_deploy(target_folder)
        
    def error_handler(msg):
        print(msg)

    def run_deploy_script(configuration_path):
        run_deploy(configuration_path)
        
    if options.command == "deploy":
        init_deploy(os.getcwd(), options.projectname, options.cfg, \
                build_deploy_script, \
                run_deploy_script, \
                error_handler)
    elif options.command == "init":
        from .init_code_with_tag import init_tag_for_project
        init_tag_for_project(options.giturl, options.tag, options.cfg, os.getcwd())
    else:
        print('please set the valid command: deploy, init')
        
def main():
    run(get_options())
