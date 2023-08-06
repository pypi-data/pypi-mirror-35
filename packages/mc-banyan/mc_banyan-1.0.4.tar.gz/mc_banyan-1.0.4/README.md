# banyan #
Banyan is a microservice deployment management tool. It assumes that your microservice projects deployment are driven by ansible. If you are interesting in it, please make sure your project development is compliant to the [specifications](SPEC.md) and [banyan configuration](BANYAN_CFG.md).

# Background  
The banyan program assumes that the project subjects to [specifications](SPEC.md). Based on [specifications](SPEC.md), the depended project should be in the same folder.   

# How to use it
## Installation
```
/usr/bin/python3 -m pip install banyan
```
`banyan` is developed in python 3.x. Please make sure python 3.x has been installed in your system.   

---
There are two ways to work with `banyan`.   
## Start from git repository
```
mkdir working_space
cd working_space
banyan init -g <git-url> -c <configuration-name> -k <key-file-of-git-repository>
```
Please refer to [banyan commands:init](BANYAN_COMMANDS.md#init) for more details.   


## Start from existing code

To start from existing code, please make sure your folder structure follows [specifications](SPEC.md). The `git-url` should be configured in the *.cfg file.

## Work with banyan
banyan can work for you in following aspects:   
* commit changes across microservice projects
* manage tags across microservice projects
* deploy the microservice project for specified configuration

run the following command:
```
cd working_space
banyan deploy -p <project-folder-name> -c <configuration-name>
```
The command above will deploy the microservice based on the configuration.   
* project-folder-name: the name of the project folder. It subjects to [banyan configuration](BANYAN_CFG.md).   
* configuration-name: the name of the configuration for deployment. Please refer to [banyan configuration](BANYAN_CFG.md) for more details.   

After the command executing, the folder `.<project-folder-name>-<configuration-name>` is added to `working_space`. The generated folder structure would be like following. 
```
working_space
|-.<project-folder-name>-<configuration-name>
  |-main.host
  |-main.yml
  |-main.sh
  |-roles
    |-role-folders 
    |- ...
```

