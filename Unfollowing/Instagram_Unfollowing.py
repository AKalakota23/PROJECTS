import json #in order to import the .json files

#opens and reads the files
following = open("Unfollowing/following.json", "r")
followers = open("Unfollowing/followers_1.json", "r")

#loads and stores the files
following_json= json.load(following)
followers_json = json.load(followers)

#converts the contents into sets
following_set = set()
followers_set = set()

#stores the usernames from each file into the set
def gather_data(followers_json, following_json):

    for i in followers_json:
        followers_set.add((i)['string_list_data'][0]['value'])
        
    for j in following_json['relationships_following']:
        following_set.add((j)['string_list_data'][0]['value'])

    unfollow = (following_set - followers_set)

    display_data(following_set, unfollow)

#displays the data
def display_data(following_set, unfollow):

    print('\n# of people you are following:', len(following_set))
    print('# of people who are not following you:', len(unfollow), '\n')

    #prints the usernames 
    for unfollow in unfollow:
        print(unfollow)

gather_data(followers_json, following_json) #calls function

