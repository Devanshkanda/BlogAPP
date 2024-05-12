from fastapi.routing import APIRouter
from models.user_model import Likes
from main import db

likes_router = APIRouter(
    prefix="/likes"
)

likes_collection = db["likes"]

@likes_router.get("/{blog_id}/likes")
async def get_likes_on_post(blog_id: str):
    likes = likes_collection.find({"post_id": blog_id})

    return {
        "status": 200,
        "message": "likes fetched successfully",
        "post id": blog_id,
        "likes": len(likes)
    }

@likes_router.post("/{blog_id}")
async def like_a_post(like: Likes, blog_id: str):
    like_id = str(likes_collection.insert_one(dict(like)))

    return {
        "status": 201,
        "message": "post liked successfully",
        "post id": blog_id,
        "like id": like_id
    }