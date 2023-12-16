# coding: utf-8
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String, TIMESTAMP, Table, Text, text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Date(Base):
    __tablename__ = 'dates'

    id = Column(Integer, primary_key=True)
    lesson_date = Column(Date)


class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    image_url = Column(String(255), nullable=False)
    content = Column(Text)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))


t_sqlite_sequence = Table(
    'sqlite_sequence', metadata,
    Column('name', NullType),
    Column('seq', NullType)
)


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    subject_id = Column(ForeignKey('subjects.id'))

    subject = relationship('Subject')


class Lesson(Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True)
    subject_id = Column(ForeignKey('subjects.id'))
    date_id = Column(ForeignKey('dates.id'))
    group = Column(String(50))
    lesson_number = Column(Integer)
    time = Column(String(20))

    date = relationship('Date')
    subject = relationship('Subject')
    users = relationship('User', secondary='user_lessons')


class TeacherSubject(Base):
    __tablename__ = 'teacher_subjects'

    id = Column(Integer, primary_key=True)
    teacher_id = Column(ForeignKey('users.id'))
    subject_id = Column(ForeignKey('subjects.id'))

    subject = relationship('Subject')
    teacher = relationship('User')


class Attendance(Base):
    __tablename__ = 'attendance'

    id = Column(Integer, primary_key=True)
    lesson_id = Column(ForeignKey('lessons.id'))
    student_id = Column(ForeignKey('users.id'))
    status = Column(Boolean, nullable=False)

    lesson = relationship('Lesson')
    student = relationship('User')


class StudentGroup(Base):
    __tablename__ = 'student_groups'

    id = Column(Integer, primary_key=True)
    student_id = Column(ForeignKey('users.id'))
    group_id = Column(ForeignKey('groups.id'))

    group = relationship('Group')
    student = relationship('User')


t_user_lessons = Table(
    'user_lessons', metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('lesson_id', ForeignKey('lessons.id'), primary_key=True)
)
