from util.permissions_reader import read_permissions_csv_file

class permissions:

    def __init__(self):
        self.permissions = []

    def get_permissions(self):
        return self.permissions

    def read_permissions(self, num_permissions):
        self.permissions = read_permissions_csv_file(num_permissions)

