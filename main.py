import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

data = response.json()

print("Data fectched!")

print(type(data))

processed_posts = []

for post in data:
    processed_post = {
        "post_id": post["id"],
        "title": post["title"],
        "title_length": len(post["title"])
    }
    processed_posts.append(processed_post)

##print("Processed first 3 posts:")
##print(processed_posts[:3])


with open("processed_posts.json", "w") as file:
    json.dump(processed_posts, file, indent=4)

print("Processed data saved to processed_posts.json")

