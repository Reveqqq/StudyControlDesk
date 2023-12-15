from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from function.auth import oauth2_scheme, SECRET_KEY, ALGORITHM
from sql_app import crud, models, schemas
from sql_app.crud import get_user_name
from sql_app.database import SessionLocal, engine

from datetime import timedelta
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from function import auth
from jose import JWTError, jwt
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="kyrsa4")

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



def db_get():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(db_get),):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user_name(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[schemas.UserCreate, Depends(get_current_user)]
):
    # if current_user.disabled:
    #     raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(db_get)
):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
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


@app.get("/user/me", response_model=schemas.User)
async def read_users_me(
    current_user: Annotated[schemas.User, Depends(get_current_active_user)]
):
    return current_user


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(db_get)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.creat_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_user(current_user: Annotated[schemas.User, Depends(get_current_active_user)], skip: int = 0, limit: int = 100, db: Session = Depends(db_get)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/user/{user_id}", response_model=schemas.User)
def read_user(user_id: int, current_user: Annotated[schemas.User, Depends(get_current_active_user)], db: Session = Depends(db_get)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User  not found")
    return db_user


@app.get("/lessons/my/", response_model=list[schemas.lesson])
def read_lessons(current_user: Annotated[schemas.User, Depends(get_current_active_user)], db: Session = Depends(db_get)):
    lessons = crud.get_all_lessons(db=db, teacher_id=current_user.id)
    return lessons


@app.get("/lessons/passed/", response_model=list[schemas.lesson])
def read_lessons(current_user: Annotated[schemas.User, Depends(get_current_active_user)], db: Session = Depends(db_get)):
    lessons = crud.get_all_lessons(db=db, teacher_id=current_user.id, passed=True)
    return lessons


@app.get("/lesson/{lesson_id}", response_model=schemas.lesson)
def read_lesson(current_user: Annotated[schemas.User, Depends(get_current_active_user)], lesson_id: int, db: Session = Depends(db_get)):
    return crud.get_lesson(db=db, lesson_id=lesson_id)


@app.get("/attendance/{lesson_id}", response_model=schemas.attendance)
def read_attendance(current_user: Annotated[schemas.User, Depends(get_current_active_user)], lesson_id: int, db: Session = Depends(db_get)):
    return {
        "lesson": crud.get_lesson(db=db, lesson_id=lesson_id),
        "students": crud.get_attendance_students(db=db, lesson_id=lesson_id)
    }


@app.post("/attendance", response_model=schemas.attendance)
def create_attendance(current_user: Annotated[schemas.User, Depends(get_current_active_user)], data: schemas.attendance_data, db: Session = Depends(db_get)):
    crud.set_attendance(db=db, lesson_id=data.lesson_id, attendances=data.attendances)
    return read_attendance(current_user=current_user, lesson_id=data.lesson_id, db=db)

