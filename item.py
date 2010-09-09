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

        self.project = user.projects().find(id=self.project_id)
        self.user = user

class ItemList(list):
    def __init__(self, user):
        self.user = user

    def add(self, content, project=None, date_string=None, priority=None, js_date=None):
        params = {'token': self.user.api_token, 'content': content}

        if not(project):
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
        new_item = Item(json_data)
        self.append(new_item)
        return new_item

