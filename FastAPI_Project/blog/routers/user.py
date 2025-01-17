from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, models, database, hashing
from ..repository import user

router= APIRouter(
    prefix="/user",
    tags=["users"]
)
get_db=database.get_db
Hash=hashing.Hash


@router.post('/')
def create_user( request:schemas.User, db:Session= Depends(get_db)):
    # hashedPassword=pwd_cxt.hash(request.password)
    # new_user=models.User(name=request.name, email=request.email, password=hashedPassword)
    # new_user=models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))

    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)

    # return new_user
    return user.create(request, db)



@router.get('/{id}', response_model=schemas.ShowUserBlogs)
def get_user(id:int, db:Session= Depends(get_db)):
    # user=db.query(models.User).filter(models.User.id==id).first()
    # if not user:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not found")
    # return user
    return user.get_user(id,db)
