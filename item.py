import connect

class Item:
    def __init__(self, json_data, user):
        self.due_date = json_data['due_date']
        self.user_id = json_data['user_id']
        self.in_history = json_data['in_history']
        self.priority = json_data['priority']
        self.item_order = json_data['item_order']
        self.content = json_data['content']
        self.indent = json_data['indent']
        self.project_id = json_data['project_id']
        self.checked = json_data['checked']
        self.date_string = json_data['date_string']
        self.id = json_data['id']

        self.project = user.projects().find(id=self.project_id)
        self.user = user

    def delete(self):
        connect.connect(method="DELETE", url="deleteItems", params={'token': self.user.api_token, 'ids': "[" + str(self.id) + "]"})

    def update(self, content=None, date_string=None, priority=None, indent=None, item_order=None, js_date=None):
        params={'token': self.user.api_token, 'id': self.id}

        if content:
            params['content'] = content
            self.content = content
        if date_string:
            params['date_string'] = date_string
            self.date_string = date_string
        if priority:
            params['priority'] = priority
            self.priority = priority
        if indent:
            params['indent'] = indent
            self.indent = indent
        if item_order:
            params['item_order'] = item_order
            self.item_order = item_order
        if js_date:
            params['js_date'] = js_date
            self.js_date = js_date

        connect.connect(method="PUT", url="updateItem", params=params)

class ItemList(list):
    def __init__(self, user):
        self.user = user

    def add(self, content, project=None, date_string=None, priority=None, js_date=None):
        params = {'token': self.user.api_token, 'content': content}

        if not(project):
            if self.project():
                project = self.project()
            else
                raise Exception
        else:
            params['project_id'] = project.id

            if date_string:
                params['date_string'] = date_string
            if priority:
                params['priority'] = priority
            if js_date:
                params['js_date'] = js_date

        json_data = connect.connect(method="POST", url="addItem", params=params)
        new_item = Item(json_data, self.user)
        self.append(new_item)
        return new_item

    def update(self, content=None, date_string=None, priority=None, indent=None, item_order=None, js_date=None):
        for item in self:
            item.update(content, date_string, priority, indent, item_order, js_date)

    def delete(self):
        for item in self:
            item.delete()

        self = ItemList(self.user)

    def project(self):
        if len(self) > 0:
            project = self[0].project

            for item in self:
                if item.project != project:
                    return None

            return project
        return None

    def find(self, **kwargs):
        matches = ItemList(self.user)

        if kwargs.get('content', None):
            for item in self:
                if item.content == kwargs['content']:
                    matches.append(item)
        elif kwargs.get('id', None):
            for item in self:
                if item.id == kwargs['id']:
                    matches.append(item)
        elif kwargs.get('checked', None):
            for item in self:
                if item.checked == kwargs['checked']:
                    matches.append(item)

        if len(matches) == 0:
            return None
        elif len(matches) == 1:
            return matches[0]
        else:
            return matches

