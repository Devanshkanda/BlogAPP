from fastapi.routing import APIRouter
from fastapi import HTTPException
from main import db
from models.user_model import Comments
# Comment routes

comment_collection = db['comments']

router = APIRouter()


def get_comments(comment):
    return {
        "comment id": str(comment["_id"]),
        "post id": comment["post_id"],
        "user id": comment["user_id"],
        "content": comment["content"]
    }


@router.post("/{blog_id}/comment")
async def comment_on_post(comment: Comments, blog_id: str):
    comment_id = str(comment_collection.insert_one(dict(comment)).inserted_id)

    return {
        "status": 201,
        "message": "comment added on post",
        "post id": blog_id,
        "comment id": comment_id
    }


@router.get("/{blog_id}/all_comments")
async def show_all_comments(blog_id: str):

    all_comments = comment_collection.find({"post_id": blog_id})
    
    if not all_comments:
        raise HTTPException(404, {"message": "No comments found on this post"})
    
    return {
        "status": 200,
        "message": "all comments fetched successfully",
        "data": [get_comments(comm) for comm in all_comments]
    }
