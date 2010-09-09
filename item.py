import connect

class Item:
    def __init__(json_data, user):
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

        self.user = user

