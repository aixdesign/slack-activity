class Member:
    # id, name, real_name, profile.display_name_normalized, profile.display_name, profile.real_name, profile.real_name_normalized, profile.email
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.real_name = ''
        self.display_name = ''
        self.email = ''