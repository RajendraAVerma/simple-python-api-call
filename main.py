import requests


class ApiModel:
    def __init__(self, id, title, excerpt):
        self.id = id
        self.title = title
        self.excerpt = excerpt


url = "https://dnnews.in/wp-json/wp/v2/posts?_fields=author,id,excerpt,title,link,jetpack_featured_media_url"

r = requests.get(url)

if r.status_code == 200:
    print(r.status_code)
    json = r.json()

    model_list = []
    for item in json:
        id = item['id']
        title = item['title']['rendered']
        excerpt = item['excerpt']['rendered']
        model_list.append(ApiModel(id, title, excerpt))

    for model in model_list:
        print(model.id)
        print(model.title)
        print("\n")

else:
    print("Error Occurred!!")

# post method for posting post on wordpress site fastguide
# post_url = "https://fastguide.in/wp-json/wp/v2/posts/"
# header = {
#     "Authorization": "Bearer <---- api token key ----->"}
# data = {
#     "title": "this title of post",
#     "status": "publish",
#     "content": "this is content",
#     "slug": "post-slug-means-link-name"
# }
#
# post = requests.post(headers=header, url=post_url, data=data)
