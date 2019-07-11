class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):

    if user in group.get_users():
        return True

    for sub_group in group.get_groups():
        return is_user_in_group(user, sub_group)

    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Test case 1
child1 = Group("child1")
child2 = Group("child2")
parent.add_user("Person1")
result = is_user_in_group("Person1", parent)  #Result:  True
print ("Result: ", result)
result = is_user_in_group("Person1", child)  #Result:  False
print ("Result: ", result)
result = is_user_in_group("sub_child_user", parent) #Result:  True
print ("Result: ", result)

#Test case 2
parent1 = Group("parent1")
parent2 = Group("parent2")
parent3 = Group("parent3")

parent3.add_user("User1")
parent1.add_group(parent3)
parent2.add_group(parent1)
parent2.add_user("User2")

result = is_user_in_group("Person1", parent3)  # Result:  False
print ("Result: ", result)
result = is_user_in_group("User1", parent3)   #Result:  True
print ("Result: ", result)
result = is_user_in_group("User2", parent3)   #Result:  False
print ("Result: ", result)

#Test case 3
parent = Group("parent")
child = Group("child")
sub_child = Group("subchildren")

child.add_user("User1")
sub_child.add_group(parent)
sub_child.add_group(child)
parent.add_user("User2")

result = is_user_in_group("Person1", child) #Result:  False
print ("Result: ", result)
result = is_user_in_group("User2", sub_child)  #Result:  True
print ("Result: ", result)
result = is_user_in_group("User1", child)  #Result:  True
print ("Result: ", result)

#Test case 4
parent = Group("parent")
parent.add_user("D")

result = is_user_in_group("", parent)  # testing empty string Result:  False
print ("Result: ", result)
result = is_user_in_group("D", parent)  #testing edge case Result:  True
print ("Result: ", result)

