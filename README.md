# scripts.py — управление дневником через shell

Модуль `scripts.py` содержит 3 функции для работы с электронным дневником:

---

## Функции

### `fix_marks(schoolkid)`
Заменяет все оценки 2 и 3 у переданного ученика на 5.

### `remove_chastisements(schoolkid)`
Удаляет все замечания у переданного ученика.

### `create_commendation(schoolkid_name, subject)`
Добавляет случайную похвалу для указанного ученика по предмету.

---

## Как использовать

1. Откройте Django shell.

2. Импортируйте функции:
```
	from scripts import fix_marks, remove_chastisements, create_commendation
	from datacenter.models import Schoolkid
```


3 Найдите ученика.
Например Фралов Иван:
```
	kid = Schoolkid.objects.get(full_name__contains='Фролов Иван')
```

4. Используйте функции:
```
	fix_marks(kid)
	remove_chastisements(kid)
	create_commendation('Фролов Иван', 'Музыка')
```

Список комплиментов для похвалы хранится в COMMENDATIONS внутри scripts.py.