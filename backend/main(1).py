from datetime import timedelta
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from function import auth

app = FastAPI()


@app.post("/token", response_model=auth.Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = auth.authenticate_user(auth.fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/user/test", response_model=auth.User)
async def read_users_me(
    current_user: Annotated[auth.User, Depends(auth.get_current_active_user)]
):
    return current_user


@app.get("/news")
async def func():
    return None


@app.get("/lessons/lessons")
async def func():
    return None


@app.get("/lessons/end/lessons")
async def func():
    return None


@app.get("/lessons/lesson")
async def func():
    return None

@app.get("/lessons/group")
async def func():
    return None


@app.post("/lessons/attend")
async def func():
    return None
