from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel
from random import randrange

#youtube video- https://www.youtube.com/watch?v=0sOvCWFmrtA&t=34415s
app=FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published : bool = True
    rating :  Optional[int] = None

my_posts=[{"title":"titleValue1","content":"contentValue1","id":1 },
          {"title":"titleValue2","content":"contentValue2","id":2 }]

def find_post(id):
    for post in my_posts:
        if post["id"]==id:
            return post

@app.get("/")
def read_root():
    return {"message": "Hello Hellloo"}


# @app.post("/createpost")
# def create_user(payLoad: dict=Body(...)):
#     print(payLoad)
#     return {"new+-ost": f"title {payLoad['title']} content :{payLoad['content']}"}


#GetAll
@app.get("/posts")
def get_posts():
    return {"data": my_posts}

#Get
@app.post("/posts")
def create_user(post: Post):
    post_dict=post.dict()
    post_dict['id']=randrange(0,1000000)
    my_posts.append(post_dict)
    return {"response": post_dict}

#post 
@app.post("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    return {"data": post}