from sqlite3 import Time
from datetime import date, time
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class UserBase(BaseModel):
    email: str | None = None
    username: str | None = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class lesson(BaseModel):
    id: int
    title: str
    groups: list[str]
    num: int
    time: str
    date: date


class student(BaseModel):
    fio: str
    group: str
    status: str


class attendance(BaseModel):
    lesson: lesson
    students: list[student]


class student_status(BaseModel):
    student_id: int
    status: str


class attendance_data(BaseModel):
    lesson_id: int
    attendances: list[student_status]
