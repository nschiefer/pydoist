import connect
import project

class User:
    # declares a new user
    # essentially a data structure with added classes
    def __init__(self, json_data):
        self.start_page = json_data['start_page']
        self.notifo = json_data['notifo']
        self.api_token = json_data['api_token']
        self.time_format = json_data['time_format']
        self.sort_order = json_data['sort_order']
        self.full_name = json_data['full_name']
        self.mobile_number = json_data['mobile_number']
        self.mobile_host = json_data['mobile_host']
        self.timezone = json_data['timezone']
        self.jabber = json_data['jabber']
        self.id = json_data['id']
        self.date_format = json_data['date_format']
        self.premium_until = json_data['premium_until']
        self.tz_offset = json_data['tz_offset']
        self.msn = json_data['msn']
        self.default_reminder = json_data['default_reminder']
        self.email = json_data['email']

    def update(self, email=None, full_name=None, password=None, timezone=None):
        if(email):
            self.email = email
        if(full_name):
            self.full_name = full_name
        if(password):
            self.password = password
        if(timezone):
            self.timezone = timezone
        connect.connects(url="updateUser", params={'token': self.api_token, 'email': self.email, 'password': self.password, 'full_name': self.full_name, 'timezone': self.timezon})

    def projects(self):
        projects_json_data = connect.connect(url="getProjects", params={'token': self.api_token})

        projects = project.ProjectList(self)
        for project_json_data in projects_json_data:
            projects.append(project.Project(project_json_data, self))

        return projects

def login(email, password):
    json_data = connect.connects(url="login", params={'email': email, 'password': password})
    return User(json_data)

def register(email, full_name, password, timezone):
    json_data = connect.connects(method="POST", url="register", params={'email': email, 'password': password, 'full_name': full_name, 'timezone': timezone})
    return User(json_data)

