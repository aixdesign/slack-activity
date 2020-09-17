## script to analyze activity of members within time range
## activity is considered to be messages sent and thread responses
## if a user only reacts with emojis, that is not taken into account
## Note for later automation development: add rule to not delete member if is_admin or is_owner
import os
from slack import WebClient
from member import Member
from datetime import datetime, timedelta
import csv

SLACK_TOKEN = os.environ["SLACK_TOKEN"]
client = WebClient(token=SLACK_TOKEN)

# get list of members that have not been deactivated and are not bots
users = client.users_list()
members = users["members"]

# Get list of channels
response = client.conversations_list()
conversations = response["channels"]

# look through all public channels that has not been archived (is_channel = True, is_archived = False)
# time range to look for messages
range_in_days = 30
oldest_date = datetime.today() - timedelta(days=range_in_days)
oldest = (oldest_date - datetime(1970, 1, 1)).total_seconds()

# store id of active members in list
active_members = []
# log info of channel that was unable to be accessed
unread_channel = []

for channel in conversations:
    if channel["is_channel"] and not channel["is_archived"]:
        try:
            # get messages in channel
            response = client.conversations_history(
                channel=channel["id"],
                oldest=oldest
            )
            messages = response["messages"]

            # for each message, get id of user who posted it
            for message in messages:
                # print(message)
                user = message["user"]
                if user not in active_members:
                    active_members.append(user)

                # if message has thread (has reply_count), get reply_users (list with user id of those who replied)
                if 'reply_count' in message:
                    for user in message['reply_users']:
                        if user not in active_members:
                            active_members.append(user)
        except Exception as e:
            print(channel["id"], channel["name"], e)
            unread_channel.append(channel)


# # get rid of inactive users by comparing active_members with whole member list
# inactive_members = [x for x in members_id if x not in active_members]
count = 0

# lookup info of inactive users and write to file
# relevant info (id, name, real_name, profile.display_name_normalized, profile.display_name, profile.real_name, profile.real_name_normalized, profile.email

# set up file name based on today's date & date_range

with open('inactive_members.csv', mode='w+') as file:
    fieldnames = ['id', 'name', 'real_name', 'display_name', 'email']
    writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(fieldnames)

    # look through members, check if they are in active list
    for member in members:
        if not member['deleted'] and not member['is_bot'] and member['id'] not in active_members:
            # print(member)
            # write member object and collect all information possible
            m = Member(member['id'], member['name'])
            try:
                setattr(m, 'real_name', member['profile']['real_name_normalized'])
                setattr(m, 'display_name', member['profile']['display_name_normalized'])
                setattr(m, 'email', member['profile']['email'])

            except Exception as e:
                print(e)

            # get relevant info and write to csv
            # writer.writerow([member['id'], member['name'], member['real_name', member['profile']['display_name'], member['profile']['display_name_normalized'], member['profile']['real_name'], member['profile']['real_name_normalized'], member['profile']['email']]])
            writer.writerow([m.id, m.name, m.real_name, m.display_name, m.email])
            count += 1


print(count)
