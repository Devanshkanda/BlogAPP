from fastapi.routing import APIRouter
from main import db
from models.user_model import Users
from fastapi import HTTPException

users_collection = db['users']

router = APIRouter(
    prefix="/users"
)

def give_user(users):
    return {
        "name": users["name"],
        "email": users["email"],
        "id": users["id"]
    }


@router.get("/")
async def get_users():
    all_users = users_collection.find()

    return {
        "status": 200,
        "message": "All users fetched successfully",
        "data": [give_user(user) for user in all_users]
    }


@router.post("/")
async def create_user(user: Users):

    if not user:
        raise HTTPException(
            401,
            detail={"error": "User data input incorrectly"}
        )
    
    user.id = str(users_collection.insert_one(dict(user)).inserted_id)

    return {
        "status": 201,
        "message": "User created successfully",
        "user id": user.id
    }
