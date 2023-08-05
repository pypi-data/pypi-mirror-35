[![Build Status](https://travis-ci.org/iranianpep/iautomate.svg?branch=master)](https://travis-ci.org/iranianpep/iautomate)
[![codecov](https://codecov.io/gh/iranianpep/iautomate/branch/master/graph/badge.svg)](https://codecov.io/gh/iranianpep/iautomate)

### Requirements
- Python 2.7+
- `pip`

### Installation
1. Make sure the user is `root`:
    ```
    sudo su
    ```
2. Run `bootstrap.sh`:
    ```
    sh bootstrap.sh
    ```
    This will install `pip` and `iautomate`. If `pip` is already installed you can run the following command straightaway:
    ```
    pip install --ignore-installed --no-cache-dir iautomate
    ```
3. Upload the configuration file for example `sample-configuration.json`.
4. Upload the files which are going to be used as a source for new files (this is explained in configuration section).
5. Finally run:
    ```
    iautomate sample-config.json
    ```

### Configurations
IAutomate automates all the server configurations mainly based on a JSON config file. An example of the file named `sample-config.json` is provided in the repo.

The config file consists of:
- `vars`: which are the global variables including:

|   Name    | Type | Required | Description |
|:----------|:-----|:---------|:------------|
| sudo | boolean | no | Whether actions are run as `root` or not. It is recommended to be `true` |
| debug | boolean | no | Whether shell commands output should be printed or not. This is used for troubleshooting |
| doc_root | string | yes | Server document root e.g. `/var/www/html` |

- `tasks`: Includes a list of tasks that will be run in order. Each `task` may have the following resources:
    - `files`: Responsible for managing files. Each file may have the following properties:
    
    |   Name    | Type | Required | Description |
    |:----------|:-----|:---------|:------------|
    | name | string | yes | Path to the file. Name can have a dynamic variable e.g. `{$doc_root}` referring to a global variable in this case `doc_root` |
    | action | string | no | Action to be run: `create`, `remove`. If `create` is specified the `source` file must be specified too |
    | ensure | string | no | Run a check on a file. At the moment only `present` supported |
    | source | string | no | Path to the source file if a new file is going to be created based on it |
    | owner | string | no | Owner of the file. Must be specified for a new file |
    | group | string | no | Group of the file. Must be specified for a new file |
    | mode | integer | no | Mode (permission) of the file. Must be specified for a new file |
    
    - `execs`: Responsible for running shell commands. Each exec may have the following properties:
    
    |   Name    | Type | Required | Description |
    |:----------|:-----|:---------|:------------|
    | name | string | yes | Description of a command to be run |
    | action | string | yes | Shell command to be run
    
    - `packages`: Responsible for managing Debian packages. Each package may have the following properties:
    
    |   Name    | Type | Required | Description |
    |:----------|:-----|:---------|:------------|
    | name | string | yes | Exact name of a package |
    | action | string | yes | Action to be run: `install`, `remove` |
    | version | string | no | Version of a new package. If is not specified the latest version is installed |
    
    - `services`: Responsible for managing services. Each service may have the following properties:
    
    |   Name    | Type | Required | Description |
    |:----------|:-----|:---------|:------------|
    | name | string | yes | Exact name of a service |
    | ensure | string | yes | Run a check on a service. At the moment only: `running`, `dead`, `restarted`. If the current status of the service does not match with ensure value IAutomate tries to change the service status. For example if the service is dead, the service will be started |
    
    - `directories`: Responsible for managing directories. Each directory may have the following properties:
    
    |   Name    | Type | Required | Description |
    |:----------|:-----|:---------|:------------|
    | name | string | yes | Path to a directory. Name can have a dynamic variable e.g. `{$doc_root}` referring to a global variable in this case `doc_root` |
    | action | string | no | Action to be run: `create`, `remove`. |
    | ensure | string | no | Run a check on a directory. At the moment only: `present`. If the directory does not exist an exception will be thrown |
    | owner | string | no | Owner of the directory. Must be specified for a new directory |
    | group | string | no | Group of the directory. Must be specified for a new directory |
    | mode | integer | no | Mode (permission) of the directory. Must be specified for a new directory |
    
    Also each resource can have another property called `after_tasks` which has got the exact structure of a parent `tasks`. This is useful to run some additional tasks immediately after running a resource.

### The Engine Architecture
If you look at the `iautomate/iautomate` directory you will see two packages:
- `helpers`: includes a few standalone functions
- `resources`: which basically includes a model for each of the above resources

In addition to the parent package which includes:
- `global_variables.py`: A class to make accessing the `vars` easier
- `iautomate.py`: The engine for the application and all it does is:
    1. Iterating through all the resources specified in the config file in the same order:
    
    ```
    def __handle_task(self, task):
    # for each task handle the sub items based on the type
    for config_type, properties in task.items():
        if config_type == 'execs':
            print('| Handling execs ...')
            self.__handle_execs(properties)
        elif config_type == 'packages':
            print('| Handling packages ...')
            self.__handle_packages(properties)
        elif config_type == 'services':
            print('| Handling services ...')
            self.__handle_services(properties)
        elif config_type == 'files':
            print('| Handling files ...')
            self.__handle_files(properties)
        elif config_type == 'directories':
            print('| Handling directories ...')
            self.__handle_directories(properties)
        else:
            # unsupported resource
            print('Unsupported resource: ' + config_type)
    ```
    
    2. Instantiating an object for each resource
    3. And finally calling the `run` function on each resource object for example for `execution` resource:
    ```
    # handle execution resource
    def __handle_execs(self, execs):
        for execution in execs:
            self.__handle_exec(execution)

    # handle execution resource
    def __handle_exec(self, execution_properties):
        # instantiate execution model and run it
        execution = execution_resource.ExecutionResource(execution_properties, self.global_variables)
        execution.run()

        if execution_properties.get(abstract_resource.AbstractResource.AFTER_TASKS_KEY, None):
            self.__handle_tasks(execution_properties.get(abstract_resource.AbstractResource.AFTER_TASKS_KEY))
    ```
    
    Also since the resource objects share some common properties and functions, an abstract parent class named `AbstractResource` is created to make the next developer's life easier!
    
 You may ask why this kind of design? Well, I checked the config files for the existing tools such as `Chef`, `Puppet`, `Ansible` and chose the user-friendly pieces and came up with the current config file. Then based on the config file the app structure was implemented.