import connect

class Project:
    def __init__(self, json_data):
        self.user_id = json_data['user_id']
        self.name = json_data['name']
        self.color = json_data['color']
        self.collapsed = json_data['collapsed']
        self.item_order = json_data['item_order']
        self.indent = json_data['indent']
        self.cache_count = json_data['cache_count']
        self.id = json_data['id']

