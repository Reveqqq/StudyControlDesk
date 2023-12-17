import datetime

from sqlalchemy.orm import Session, Query
from sqlalchemy import func

from . import models, schemas
from backend.function.auth import verify_password


def prepare_lessons(query: Query):
    lessons = [row._asdict() for row in query.all()]
    for lesson in lessons:
        lesson["groups"] = lesson["groups"].split(",")
    return lessons


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_name(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def creat_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password
    db_user = models.User(username=user.username, email=user.email, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, username: str, password: str):
    user = get_user_name(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

# SELECT
#     lessons.id AS id,
#     lessons.lesson_number as num,
#     GROUP_CONCAT("group") as groups,
#     lessons.time,
#     subjects.name AS title,
#     dates.lesson_date as date
# FROM lessons
# JOIN subjects ON lessons.subject_id = subjects.id
# JOIN dates ON lessons.date_id = dates.id
# JOIN teacher_subjects ON lessons.subject_id = teacher_subjects.subject_id
# WHERE teacher_subjects.teacher_id = 1
# GROUP BY lessons.lesson_number, lessons.time, subjects.name, dates.lesson_date;
def get_all_lessons(db: Session, teacher_id: int, passed: bool = False):
    lesson = models.Lesson
    subject = models.Subject
    date = models.Date
    teacher_subject = models.TeacherSubject
    query = db\
        .query(
            lesson.id,
            lesson.lesson_number.label("num"),
            func.group_concat(lesson.group, ",").label("groups"),
            lesson.time,
            subject.name.label("title"),
            date.lesson_date.label("date")
        )\
        .join(subject)\
        .join(date)\
        .join(teacher_subject)\
        .where(teacher_subject.teacher_id == teacher_id)\
        .group_by(lesson.lesson_number,
                  lesson.time,
                  subject.name,
                  date.lesson_date)
    if passed:
        query = query.where(date.lesson_date < func.current_date())
    lessons = prepare_lessons(query)
    return lessons
#
# SELECT
#     lessons.id AS id,
#     lessons.lesson_number as num,
#     GROUP_CONCAT(group_number) as groups,
#     lessons.time,
#     subjects.name AS title,
#     dates.lesson_date as date
# FROM lessons
# JOIN subjects ON lessons.subject_id = subjects.id
# JOIN dates ON lessons.date_id = dates.id
# JOIN teacher_subjects ON lessons.subject_id = teacher_subjects.subject_id
# WHERE teacher_subjects.teacher_id = 1;


def get_lesson(db: Session, lesson_id: int):
    lesson = models.Lesson
    subject = models.Subject
    date = models.Date
    query = db \
        .query(
            lesson.id,
            lesson.lesson_number.label("num"),
            func.group_concat(lesson.group, ",").label("groups"),
            lesson.time,
            subject.name.label("title"),
            date.lesson_date.label("date")
        ) \
        .join(subject) \
        .join(date) \
        .where(lesson.id == lesson_id)
    lessons = prepare_lessons(query)
    return lessons[0]

# SELECT attendance.id        AS №,
#        users.username       AS ФИО,
#        lessons.group_number as 'Номер группы',
#        attendance.status    as Статус
# FROM attendance
#          JOIN
#      users ON attendance.student_id = users.id
#          JOIN
#      lessons ON attendance.lesson_id = lessons.id
# WHERE attendance.lesson_id = 1;


def get_attendance_students(db: Session, lesson_id: int):
    lesson = models.Lesson
    user = models.User
    attendance = models.Attendance
    return db\
        .query(
            user.id,
            user.username.label("fio"),
            lesson.group,
            attendance.status
        )\
        .join(user)\
        .join(lesson)\
        .where(lesson.id == lesson_id)\
        .all()

# fake_hashed_password = user.password
#     db_user = models.User(username=user.username, email=user.email, password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

def set_attendance(db: Session, lesson_id: int, attendances: [schemas.student_status]):
    for attendance in attendances:
        db.add(models.Attendance(
            lesson_id=lesson_id,
            student_id=attendance.student_id,
            status=attendance.status
        ))
    db.commit()