import connect

class Project:
    def __init__(self, json_data, user):
        self.user_id = json_data['user_id']
        self.name = json_data['name']
        self.color = json_data['color']
        self.collapsed = json_data['collapsed']
        self.item_order = json_data['item_order']
        self.indent = json_data['indent']
        self.cache_count = json_data['cache_count']
        self.id = json_data['id']

        self.user = user

    def delete(self):
        connect.connect(method="DELETE", url="deleteProject", params={'token': self.user.api_token, 'project_id': self.id})

    def update(self, name=None, color=None, indent=None):
        params = {'token': self.user.api_token, 'project_id': self.id}

        if(name):
            params['name'] = name
            self.name = name
        if(color):
            params['color'] = color
            self.color = color
        if(indent):
            params['indent'] = indent
            self.indent = indent

        connect.connect(method="PUT", url="updateProject", params=params)

class ProjectList(list):
    def add(self, name, color=None, indent=None, order=None):
        params = {'token': self[0].user.api_token, 'name': name}

        if(color):
            params['color'] = color
        if(indent):
            params['indent'] = indent
        if(order):
            params['order'] = order

        json_data = connect.connect(method="POST", url="addProject", params=params)
        return Project(json_data, self[0].user.api_token)

    def find(**kwargs):
        matches = ProjectList()
        if kwargs.pop('id', None):
            for project in self:
                if project.id == kwargs['id']:
                    matches.append(project)
        elif kwargs.pop('name', None):
            for project in self:
                if project.name == kwargs['name']:
                    matches.append(project)
        else:
            matches = self

        if len(matches) == 0:
            return None
        elif len(matches) == 1:
            return matches[0]
        else:
            return matches

    def delete(self):
        for project in self:
            project.delete()

        self = ProjectList()

    def update(self, name=None, color=None, indent=None):
        for project in self:
            project.update(name, color, indent)

