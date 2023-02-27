from typing import Optional
from fastapi import Body, FastAPI,Response,status,HTTPException
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
        if post['id']==id:
            return post
        
def find_index_post(id):
    for i,post in enumerate(my_posts):
        if post['id']==id:
            return i
        

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

#Create
@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_user(post: Post):
    post_dict=post.dict()
    post_dict['id']=randrange(0,1000000)
    my_posts.append(post_dict)
    return {"response": post_dict}

#Get single post
@app.post("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} was not found")
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {"message":f"post with id {id} was not found"}
    return {"data": post}


#Delete single post
@app.delete("/posts/{id}")
def delete_post(id: int):

    index=find_index_post(id)
    my_posts.pop(index)
    
    return {"message": f"post was successfully deleted"}