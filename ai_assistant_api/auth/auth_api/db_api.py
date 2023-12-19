from logging import getLogger
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from auth.auth_api.auth_api import get_current_active_user
from auth.auth_api.dps import get_db
from auth.auth_common import schemas, crud
from auth.auth_common.models import User

logger = getLogger(__name__)

router = APIRouter()


@router.get("/users/me", response_model=schemas.User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    logger.info('create_user called')
    db_user = crud.get_user_by_username(db, username=user.username)  # ユーザー作成
    if db_user:
        raise HTTPException(status_code=400, detail="username already registered")  # noqa: E501
    return crud.create_user(db=db, user=user)
