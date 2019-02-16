class Admin():
    def __init__(self):
        self.privileges = Privileges()

"""A class used to represent privileges"""
class Privileges():
    def __init__(self, privileges = ['can add posts', 'can delete posts', 'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        print("The privileges defines for admin are:")
        for privilege in self.privileges:
            print("\"" + privilege + "\"")

admin = Admin()
admin.privileges.show_privileges()
