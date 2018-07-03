GenerateProjects
================

A simple Sublime Text plugin for generating Sublime Project files for all folders within a specified repository folder.

If you save all your projects/repositories in a single folder and want to be able to quickly scan this folder for new folders and generate Project files automatically for these then this is the plugin for you.

Set Up
------

Before using this plugin you will need to set the paths in the plugin settings file.

* `local_repositories_directory` - this is the absolute path to the folder containing your project code
* `sublime_project_directory` - this is the absolute path you want Sublime to save Project setting files to for each of the projects in `local_repositories_directory`

The plugin will not work until these have been set.

There is also an optional `blacklist` setting which takes an array of folders within `local_repositories_directory` that you want to exclude when generating project files.

An example settings file for the plugin:-

    {
        "local_repositories_directory": "/Users/andy/Sites",
        "sublime_project_directory": "/Users/andy/projects",
        "blacklist": [
            "tools"
        ]
    }

This will generate project files in `/Users/andy/projects` for all folders in `/Users/andy/Sites` except the @tools@ folder.

Usage
-----

Once the plugin is set up you can select 'Generate Projects' from the 'Projects' menu and Sublime will create all the relevant project files for you. You can then just 'Open Project...' as normal and select one of the newly created projects.

License
-------

GenerateProjects is released under an MIT License.
