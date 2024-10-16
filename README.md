# Django : Домашнее задание 1

## Описание проекта

Это первое домашнее задание по дисциплине Веб-программирование. Основная цель — создать базовое Django приложение с пользовательскими URL, которые отображают информацию, такую как имя, группа и возраст, а также создать суперпользователя с доступом к панели администратора.

## Структура проекта

- Название проекта: Kan
- Название приложения: Erik
- Страницы и URL:
    - /name: Отображает ваше полное имя (“Erik Kan”)
	- /groupe: Отображает номер вашей группы (“БИН-22-2”)
	- /age: Отображает ваш возраст (“21 y.o.”)
	- /common: Отображает всю информацию вместе (“Erik Kan, БИН-22-2, 21 y.o.”).

## Использование
1. Клонируйте проект с GitHub:

```bash
git clone https://github.com/your_username/your_project_name.git
cd your_project_name
```
2. Примените миграции:
```bash
python manage.py migrate
```
3. Создайте суперпользователя (он уже создан в проекте, но если потребуется пересоздать):
```bash
python manage.py createsuperuser
```

4. Запустите сервер разработки:
```bash
python manage.py runserver
```
5. Откройте браузер и перейдите на следующие страницы:
- 127.0.0.1:8000/name для отображения моего полного имени
- 127.0.0.1:8000/group для отображения группы
- 127.0.0.1:8000/age для отображения возраста
- 127.0.0.1:8000/common для отображения всей информации на одной странице

6. Панель администратора:

Доступ к панели администратора по адресу 127.0.0.1:8000/admin
Данные для входа:
- Логин: root
- Пароль: root

## Сведения об авторе
Проект выполнил студент гр. БИН-22-2 Кан Эрик Валерьевич
