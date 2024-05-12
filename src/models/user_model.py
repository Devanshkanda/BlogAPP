from pydantic import BaseModel


class Users(BaseModel):
    name: str | None
    email: str | None


class BlogPost(BaseModel):
    title: str | None
    content: str | None
    user_id: str | None


class Comments(BaseModel):
    content: str | None
    user_id: str | None
    post_id: str | None


class Likes(BaseModel):
    no_of_likes: int = 0
    user_id: str | None
    poet_id: str | None