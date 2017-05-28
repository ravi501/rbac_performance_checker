from data_elements.permissions import read_permissions_csv_file

from data_elements import roles
from data_elements import users_permission_requirements

from process import constants

import random


class Checker:

    def __init__(self):
        self.permissions = []
        self.roles = []
        self.total_permissions = constants.TOTAL_SYSTEM_PERMISSIONS
        self.total_roles = constants.TOTAL_SYSTEM_ROLES
        self.total_users = constants.TOTAL_SYSTEM_USERS
        self.role_size = []
        self.users_requirements = []

    def initialize_system_permissions(self):
        self.permissions = read_permissions_csv_file(self.total_permissions)

    def print_system_permissions(self):
        print("The system permissions are: " + str(self.permissions))

    def allot_permissions_to_roles(self):
        permission_per_role = int(self.total_permissions/self.total_roles)
        self.role_size = [0] * self.total_roles
        role = [0] * self.total_roles

        local_permissions = []

        for perm in self.permissions:
            local_permissions.append(perm)

        used_permissions_count = 0

        while used_permissions_count < self.total_permissions:
            perm = 0
            while True:
                perm = random.randint(0, self.total_permissions - 1)

                if local_permissions[perm] != '1':
                    permission = local_permissions[perm]
                    break

            while True:
                role_number = random.randint(0, self.total_roles - 1)

                if self.role_size[role_number] < permission_per_role:
                    break

            if role[role_number] == 0:
                new_role = roles.Roles()
                new_role.permissions_in_role.append(permission)
                role[role_number] = new_role
            else:
                existing_role = role[role_number]
                existing_role.permissions_in_role.append(permission)

            local_permissions[perm] = '1'
            self.role_size[role_number] += 1;
            used_permissions_count = used_permissions_count + 1

        return role

    def print_permission_to_roles_assignment(self, role):
        for i in range(0, len(role)):
            print("Role " + str(i) + " size = " + str(self.role_size[i]) + " permissions:", end="")
            for j in range(self.role_size[i]):
                print(str(role[i].permissions_in_role[j]), end = " ")
            print()

    def generate_users_requirements(self):
        self.users_requirements = [0] * self.total_users
        for i in range(0, self.total_users):
            j = 0
            while j < constants.PERMISSION_PER_USER:
                user_req = random.randint(0, self.total_permissions - 1)
                translated_reqs = self.permissions[user_req]
                k = 0
                while k < j:
                    if translated_reqs == self.users_requirements[i].user_permissions[k]:
                        user_req = random.randint(0, self.total_permissions - 1)
                        translated_reqs = self.permissions[user_req]
                        k = 0;
                    else:
                        k += 1
                if self.users_requirements[i] == 0:
                    user_req = users_permission_requirements.UserRequirements()
                    user_req.user_permissions.append(translated_reqs)
                    self.users_requirements[i] = user_req
                else:
                    self.users_requirements[i].user_permissions.append(translated_reqs)
                j += 1

    def print_user_requirements(self):
        for i in range(0, self.total_users):
            print("User " + str(i) + " requirements: ", end="")
            for j in range(0, len(self.users_requirements[i].user_permissions)):
                print(self.users_requirements[i].user_permissions[j] + " ", end="")
            print()

checker = Checker()
checker.initialize_system_permissions()
checker.print_system_permissions()
role = checker.allot_permissions_to_roles()
checker.print_permission_to_roles_assignment(role)

print("===============================================")
checker.generate_users_requirements()
checker.print_user_requirements()
