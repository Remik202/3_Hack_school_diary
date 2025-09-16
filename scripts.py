from datacenter.models import Schoolkid, Lesson, Commendation, Subject, Mark, Chastisement
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
import random


COMMENDATIONS = [
    "Молодец!",
    "Отлично!",
    "Прекрасная работа!",
    "Гораздо лучше, чем вчера!",
    "Ты растёшь над собой!",
    "Так держать!",
]


def find_schoolkid(schoolkid_name: str) -> Schoolkid | None:
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
        return schoolkid
    except ObjectDoesNotExist:
        print("Ученик не найден. Проверь имя.")
        return None
    except MultipleObjectsReturned:
        print("Найдено несколько учеников. Уточни имя.")
        return None


def create_commendation(schoolkid_name: str, subject_title: str):
    schoolkid = find_schoolkid(schoolkid_name)

    if schoolkid:
        lessons = Lesson.objects.filter(
            year_of_study=schoolkid.year_of_study,
            group_letter=schoolkid.group_letter,
            subject__title=subject_title
        ).order_by('-date')

        if not lessons:
            print("Уроки по такому предмету не найдены.")
            return

        lesson = lessons.first()

        Commendation.objects.create(
            text=random.choice(COMMENDATIONS),
            created=lesson.date,
            schoolkid=schoolkid,
            subject=lesson.subject,
            teacher=lesson.teacher
        )
        print(f"Похвала для {schoolkid.full_name} по предмету {subject_title} добавлена.")
    else:
        print("Ученик не найден.")


def fix_marks(schoolkid):
    if schoolkid: 
        bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
        bad_marks.update(points=5)
        print(f"Заменено {bad_marks.count()} плохих оценок на пятёрки.")
    else:
        print("Ученик не найден. Невозможно заменить оценки.")


def remove_chastisements(schoolkid):
    if schoolkid:
        chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
        deleted, _ = chastisements.delete()
        print(f"Удалено замечаний: {deleted}")
    else:
        print("Ученик не найден. Невозможно удалить замечания.")