import os
import yaml
import functools
from .debug import simple
from jinja2 import Template

def all(parent_folder, role_names = []):
    def get_role_names(roles_path):
        def get_roles():
            return [y for x in [dirs for root, dirs, _ in os.walk(roles_path, followlinks = True) if root == roles_path] for y in x]

        return get_roles() if os.path.exists(roles_path) else []
    
    def get_defaults_by_name(rolename):
        def get_defaults(path):
            return yaml.load(open(path, 'r')) if os.path.exists(path) else {}
            
        return simple(get_defaults(os.path.join(parent_folder, "roles", rolename, "defaults", "main.yml")), "get_defaults_by_name") \
            if len(role_names) == 0 or rolename in role_names \
               else {}
    def combine(names):
        def combine_dict(a, b):
            # if len(list(filter(lambda n: n in b, a))) > 0:
            #     raise Error("have duplicated keys")
            return {**a, **b}
        return functools.reduce(combine_dict, names)
    return combine([get_defaults_by_name(rolename) for rolename in get_role_names(os.path.join(parent_folder, "roles"))])

def write(file_path, keyvals):
    from .tools.data_convert import dict2assignments

    file = open(file_path, 'w')
    try:
        file.write(Template('''[all:vars]
{% for assignment in assignments %}{{assignment}}
{% endfor %}
''').render(assignments = dict2assignments(keyvals)))
        
    finally:
        file.close()

def override_values(cfg_json, host_values):
    def override(new_values):
        simple(host_values, "override_values_host_values").update(new_values)
        return host_values

    return override(cfg_json["predefined_variables"]) \
        if "predefined_variables" in cfg_json \
           else simple(host_values, "override_values_host_values")
        
