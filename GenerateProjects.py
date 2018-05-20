import sublime, sublime_plugin
import os, json

class GenerateProjectsCommand(sublime_plugin.WindowCommand):

    def run(self):
        path = settings.get('project_files_directory')
        for name in os.listdir(path):
            if os.path.isdir(os.path.join(path, name)) and not self.is_blacklisted(name):
                self.generateProject(name)

    def is_blacklisted(self, name):
        """Check if directory is blacklisted"""
        blacklist = settings.get('blacklist')
        return name in blacklist

    def generateProject(self, name):
        """Generate a Sublime Text project file"""
        project_path = settings.get('project_files_directory') + '/' + name
        project_settings_path = settings.get('sublime_project_settings_directory')
        project_file = project_settings_path + '/' + name + '.sublime-project'
        if not os.path.isfile(project_file):
            project = {'name': name, 'folders': [{'path': project_path}]}
            with open(project_file, 'w') as f:
                f.write(json.dumps(project, indent = 4))
                f.close()