
Безопасный дамп данных Django-проекта
=====================================

```bash
python project/manage.py dumpdata --natural-foreign --exclude auth.permission --exclude contenttypes --exclude admin.logentry --indent 4 > dump.json
```

Инициализция git репозитария
============================

```bash
git init
git remote add origin git-реп
```

поправить .gitignore

```bash
git add .
git commit -a -m "init"
git push origin master
git pull origin master
```

Исключение из индекса git файлов
================================

Нужно убрать его из индекса:
```bash
git rm --cached path/to/file
git rm --cached project/project/settings/local.py
```

Hg улаживание конфликтов
========================

Чтобы выйти из vimdiff - :cq
```bash
`hg resolve -t internal:other --all` to accept theirs and
`hg resolve -t internal:local --all` to accept yours
```
