from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 40
NUMBER_SUBJECTS = 5
NUMBER_TEACHERS = 4
NUMBER_RATING = 20


def generate_fake_data(number_groups, number_students, number_subjects, number_teachers, number_rating) -> tuple():

    fake_groups = []
    fake_students = []
    fake_subjects = []
    fake_teachers = []
    fake_rating = []

    fake_data = faker.Faker()

    for _ in range(number_groups):
        fake_groups.append(fake_data.company())

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    for _ in range(number_subjects):
        fake_subjects.append(fake_data.job())
    
    for _ in  range(number_teachers):
        fake_teachers.append(fake_data.name())

    for _ in range(number_rating):
        fake_rating.append(randint(1,5))

    return fake_groups, fake_students, fake_subjects, fake_teachers, fake_rating


def prepare_data(groups, students, subjects, teachers, rating):

    for_groups = []

    for group in groups :
        for_groups.append((group,))

    for_students =[]

    for student in students :
        for_students.append((student, randint(1,NUMBER_GROUPS)))

    for_subjects = []
    for subject in subjects:
        for_subjects.append((subject, randint(1,NUMBER_TEACHERS)))

    for_teachers = []
    for teacher in teachers:
        for_teachers.append((teacher,))

    for_rating = []
    for _ in range(NUMBER_RATING):

        for student_id in range(1, NUMBER_STUDENTS + 1):

            for subject_id in range(1, NUMBER_SUBJECTS + 1):

                rating_list = [randint(1, 5) for _ in range(20)]
                for_rating.append((subject_id, student_id, rating_list))

    return for_groups, for_students, for_subjects, for_teachers, for_rating


def insert_data_to_db(groups, students, subjects, teachers, ratings):
    
     with sqlite3.connect('salary.db') as con:

        cur = con.cursor()

        sql_to_group = '''INSERT INTO groups (group_name) VALUES (?)'''
        cur.executemany(sql_to_group, groups)

        sql_to_students ='''INSERT INTO students (student_name, group_id) VALUES (?,?)'''
        cur.executemany(sql_to_students, students)

        sql_to_subjects = '''INSERT INTO subjects (subject_name, teacher_id) VALUES (?,?)'''
        cur.executemany(sql_to_subjects, subjects)

        sql_to_teachers = '''INSERT INTO teachers (teacher_name) VALUES (?)'''
        cur.executemany(sql_to_teachers,teachers)
        
        for rating in ratings:
            subject_id, student_id, scores = rating
            for score in scores:
                sql_to_rating = '''INSERT INTO magazine (subject_id, student_id, rating) VALUES (?, ?, ?)'''
                cur.execute(sql_to_rating, (subject_id, student_id, score))


if __name__ == "__main__":
    groups, students, subjects, teachers, rating = prepare_data(*generate_fake_data(NUMBER_GROUPS, NUMBER_STUDENTS, NUMBER_SUBJECTS, NUMBER_TEACHERS,NUMBER_RATING))
    insert_data_to_db(groups, students, subjects, teachers, rating)









