
"""Data Science from Scratch, Chapter 1. DataScienster."""

users =[
        {"id": 0, "name": "Hero"},
        {"id": 1, "name": "Dunn"},
        {"id": 2, "name": "Sue"},
        {"id": 3, "name": "Chi"},
        {"id": 4, "name": "Thor"},
        {"id": 5, "name": "Clive"},
        {"id": 6, "name": "Hicks"},
        {"id": 7, "name": "Devin"},
        {"id": 8, "name": "Kate"},
        {"id": 9, "name": "Klein"}
        ]


friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


print(users)
print(friendships)

for user in users:
    user["friends"] = []

for i, j in friendships:
    # this works because user[i] is the user whose id id i
    users[i]["friends"].append(users[j]["id"]) # add i as friend of j
    users[j]["friends"].append(users[i]["id"]) # add j as friend of i

# print(users)
# pretty print
import pprint
pprint.pprint(users)


# function for calculating number of friends
def number_of_friends(user):
    """how many friends does _user_ have?"""
    return (len(user["friends"]))


# friends for each user
for user in users:
    print(user["name"]," has ", number_of_friends(user), " friends.")


# friends of all users (connections)
total_connections = sum(number_of_friends(user)
                        for user in users)
print("\ntotal connections: ", total_connections)


# I am using python3: from __future__ import division # integer division in python2 is lame
num_users = len(users) # length of the users list
avg_connections = total_connections / num_users
print("average number of connections: ", avg_connections)

# create a list (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user))
                    for user in users]

# sort it
print("Sorted by number of friends")
pprint.pprint(
sorted(num_friends_by_id,                                # get it sorted
        key=lambda user: user[1],  # by num_friends
        reverse=True)                                    # largest to smallest
)


# Data Scientists you might know

"""
def friends_of_friend_ids_bad(user):
    # "foaf" is short for "friend of a friend"
    return [foaf["id"]
            for friend in user["friends"] # for each of user's friends
            for foaf in friend["friends"]] # get each of _their_friends
"""
