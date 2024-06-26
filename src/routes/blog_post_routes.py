from main import db
from fastapi.routing import APIRouter
from fastapi import HTTPException, Request
from bson import ObjectId
from models.user_model import BlogPost, Comments

blogs_collection = db["blogs"]

router = APIRouter(
    prefix="/blogs"
)

def get_blogs(blogs):
    return {
        "id": str(blogs["_id"]),
        "name": blogs["name"],
        "content": blogs["content"],
    }

@router.get("/")
async def get_all_blogs():
    all_blogs = blogs_collection.find()

    if not all_blogs:
        raise HTTPException(404, detail={"error": "no blog posts found"})
    
    return {
        "status": 200,
        "message": "All Blog posts fetched successfully",
        "data": [get_blogs(blog) for blog in all_blogs]
    }


@router.get("/{blog_id}")
async def get_blog_by_id(blog_id: str):

    if not blog_id:
        raise HTTPException(400, detail={"error": "Blog id is required"})
    
    blog = blogs_collection.find_one(filter={"_id": ObjectId(blog_id)})

    if not blog:
        raise HTTPException(401, detail={"error": "No Blog Found"})
    
    return {
        "status": 200,
        "message": "Blog details Successfully found",
        "data": get_blogs(blog)
    }


@router.post("/")
async def create_blog(blog: BlogPost):

    # new_blog = dict(blog)
    # new_blog['user_id'] = ObjectId(oid=blog.user_id)
    
    new_blog_id = str(blogs_collection.insert_one(dict(blog)).inserted_id)

    if not new_blog_id:
        raise HTTPException(401, detail={"error": "Failed to create new blog"})

    return {
        "status": 201,
        "message": "Successfully created blog post",
        "post id": new_blog_id
    }


@router.delete("/{blog_id}")
async def delete_blog(blog_id: str):

    if not blog_id:
        raise HTTPException(401, {"error": "no blog id passed"})
    
    blogs_collection.delete_one({"_id": ObjectId(oid=blog_id)})

    return {
        "status": 200,
        "message": "Blog post deleted"
    }


from routes import comment_routes
router.include_router(comment_routes.router)