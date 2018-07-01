
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

Доступ к разным репозиториям на разных gitlab аккаунтам
=======================================================

Чтобы работать с разными проектами, находящимися в разных gitlab-аккаунтах,
необходимо создать ключи:

```bash
ssh-keygen -f id_rsa_account1
ssh-keygen -f id_rsa_account2
```

перенесем ключи в ~/.ssh директорию, выполним и добавим строки:

```bash
vi ~/.ssh/config

Host gitlab.com-account1
    HostName gitlab.com
    User git
    IdentityFile ~/.ssh/id_rsa_account1

Host gitlab.com-account2
    HostName gitlab.com
    User git
    IdentityFile ~/.ssh/id_rsa_account2
    
:wq
```

проверить, как подключается к аккаунту:

```bash
ssh -T gitlab.com-account1
ssh -T gitlab.com-account2
```

отредактируем git-конфиг (для другого проекта - аналогично):

```bash
[remote "origin"]
	url = git@gitlab.com-account1:account1/name_project.git
```
