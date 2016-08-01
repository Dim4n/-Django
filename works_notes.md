
Безопасный дамп данных Django-проекта
=====================================

python project/manage.py dumpdata --natural-foreign --exclude auth.permission --exclude contenttypes --indent 4 > dump.json

Исключение из индекса git файлов
================================

Нужно убрать его из индекса:
git rm --cached path/to/file

git rm --cached project/project/settings/local.py
