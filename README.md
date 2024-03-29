# Cookiecutter for CloudBlue Connect Reports  
  
Powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter), Cookiecutter for CloudBlue Connect Reports provides a framework for boostraping your custom reports for Connect.

With this project you can write your own reports to execute either locally or using the reports module of Connect.

In order to create your own custom report you will need to get familiar with the [Connect Rest API](https://connect.cloudblue.com/community/api/) and it's OpenAPI implementation using the [connect-openapi-client](https://github.com/cloudblue/connect-python-openapi-client).

## Dependencies

We recommend to use instead of directly `cookiecutter` our <a href="https://github.com/cloudblue/connect-cli">**connect-cli**</a> project. This utility provides all what you need to handle the lifecycle of your project including the bootstraping, validation and adding new reports.

In the case you want to bootstrap your project directly, you will require following packages:

* cookiecutter
* openpyxl

## Features

* Works fit python 3.8 and 3.9
* Bootstraps a custom report project within seconds
* Provides all needed dependencies
* Provides basic testing functionality including right mockers
* Compatible with github Actions
* Configures project licensing

## Usage

Creating a project that provides a report package that could be run either using the [Connect CLI](https://github.com/cloudblue/connect-cli) or directly in [Connect](https://connect.cloudblue.com) is simple.

After installing [Connect CLI](https://github.com/cloudblue/connect-cli), you could run the following command on your terminal for having a fresh new reports project:

	$ cd $HOME/connect_projects
	$ ccli project report bootstrap
 
You'll be prompted for some values. Provide them and a Connect project will be created for you.

**Warning**: Please change sample data with your own desired information

	Bootstraping report project...

	project_name [My Awesome Project]: My Awesome Project
	project_slug [my_awesome_project]:
	description [My reports are really usefull!]:
	package_name [reports]: My Super Reports Package
	package_slug [my_super_reports_package]:
	initial_report_name [My Awesome Report]: My Awesome Report
	initial_report_slug [my_awesome_report]:
	initial_report_description [This report provides all data i need]:
	Select initial_report_renderer:
	1 - xlsx
	2 - csv
	3 - pdf
	4 - json
	5 - jinja2
	Choose from 1, 2, 3, 4, 5 [1]: 1
	author [Globex Corporation]: ISV Inc
	version [0.1.0]: 1.0.0
	Select license:
	1 - Apache Software License 2.0
	2 - MIT
	3 - BSD
	Choose from 1, 2, 3 [1]: 1
	use_github_actions [y]: y
	Done! Your report project is ready to go!

	Report Project location: $HOME/connect_projects/my_awesome_project

Now you can access your recently created project folder and take a look arround it:

	$ cd my_awesome_project
	$ ls

Starting here, if you want you can put your project on a git repository, for example at github:

	$ git init
	$ git add .
	$ git commit -m "first commit"
	$ git remote add origin https://github.com/cloudblue/my_custom_reports_project.git
	$ git push -u origin master

In the use case that you decided to use github actions, you will notice that a first CI task will run, this one will run the sample test

## Creating your own report

The creation of a new report requires some knowledge of [Connect Rest API](https://connect.cloudblue.com/community/api/) and the [connect-openapi-client](https://github.com/cloudblue/connect-python-openapi-client). 

First, edit the reports.json file, this file is a descriptor that can be read by Connect as well as Connect CLI to understand your package. Please ensure that all properties are defined. On the parameters list, you can define the parameters that will be asked to be populated by who runs the report, just select the ones you need as described in our community portal.

The code of your report must be defined at your entrypoint, here is where system will find your function that will receive an instantiated client, this client is the openapi one and can work with our API, additionally you will get a function that you must invoke in order to update the progress

Job done? Try to run it locally!

	$ ccli report list -d ./my_awesome_project

	************************************************************

	My Awesome Project version 1.0.0

	************************************************************

	Welcome to My Awesome Project !

	My reports are really usefull!

	License

	My Awesome Project is licensed under the Apache Software License 2.0 license.


	************************************************************

	List of available reports:

	Report ID: my_awesome_report - Report name: My Awesome Project

Now if you want you can execute it also using ccli

	$ ccli report execute my_awesome_report_1 -d ./my_awesome_report

## Examples

All our reports that you can run from Connect platform are available to you, if you want to take a look at them and it's code visit our github repository available [here](https://github.com/cloudblue/connect-reports)

Please take a look to our oficial [documentation site](https://connect.cloudblue.com) for more information on how to work with reports
