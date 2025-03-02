import requests # type: ignore
import json

class RequestFailed(Exception):
    pass


try:
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code != 200:
        raise RequestFailed(f'Request Failed with {r.status_code}')
except RequestFailed as error:
    print(error)
else:
    # Convert text data into python dict
    response_data = json.loads(r.text)
    print(f'The length of response data has a total of {len(response_data)} items')
    # Extract id and userids only
    extract = list(map(lambda x: {"id": x['id'], "user_id": x['userId']}, response_data))
    # Filter id and titles by userid 10
    get_titles_by_user_id_10 = list(map(lambda y: {"id": y['id'], "title": y['title']}, filter(lambda x: x['userId'] == 10, response_data)))
    print(*get_titles_by_user_id_10, sep='\n')
    # Number of posts by each user
    posts_per_user = {}
    for post in response_data:
        posts_per_user[post['userId']] = 1 + posts_per_user.get(post['userId'], 0)
    print("UserID\tNumber of Posts" )
    for user_id, num_posts in posts_per_user.items():
        print(f'{user_id}\t{num_posts}')
    
    # Post Titles Grouped by UserId
    titles_by_user = {}
    for post in response_data:
        if post['userId'] not in titles_by_user:
            titles_by_user[post['userId']] = []
        titles_by_user[post['userId']].append(post['title'])
    print("UserID\tTitles")
    for user, titles in titles_by_user.items():
        titles_string = "\n\t".join(titles)
        print(f'{user}\t{titles_string}')

