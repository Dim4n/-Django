# Полезные ссылки:

Как спроектировать схему базы данных http://eax.me/database-design/
Обратная совместимость и изменение схемы базы данных http://eax.me/backward-compatibility/
Почему эти ваши модные NoSQL решения не так уж хороши http://eax.me/avoid-nosql/
Простой пример работы с PostgreSQL на Python http://eax.me/python-postgresql/
Мemcached — это просто! http://eax.me/memcached/
Redis и области его применения http://eax.me/redis/
Мой первый опыт использования MongoDB http://eax.me/mongodb/
Начало работы с PostgreSQL http://eax.me/postgresql-install/
Некоторые интересные отличия PostgreSQL от MySQL http://eax.me/postgresql-vs-mysql/

# Общая информация

Импорт/экспорт дампа БД PostgreSQL через SSH
Linux хостинг 
Если вам не удается загрузить данные в базу данных стандартными средствами, вы можете воспользоваться альтернативным способом, описанным в данной статье.

Перед выполнением дальнейших действий необходимо выполнить следующее:
Создайте сайт и настройте подключение по FTP.
Настройте подключение по SSH.
Добавьте базу данных.

Затем подключитесь к вашему сайту по FTP, используя данные из п.1, и загрузите дамп в корневую папку сайта. Если он заархивирован, разархивируйте его перед загрузкой (после разархивирования у него должно быть расширение .sql).

Подключитесь к вашему сайту по SSH, используя инструкцию "Настройка SSH-клиента".

Импорт
Перед тем как выполнить импорт, перейдите в соответствующую директорию. Сделать это вы можете при помощи команд pwd (показ текущего каталога), ls (отображение списка файлов в текущем каталоге) и cd (перемещение по каталогам). Полный список команд и их значение перечислены в статье "Основные команды консоли".

Выполнить импорт дампа БД можно строкой:
pg_restore -h hostname -U username -F format -d dbname dumpfile

В строку нужно внести следующие изменения:
Вместо hostname – IP для внутреннего доступа localhost.
Вместо username – имя пользователя.
Вместо format – формат дампа (может быть одной из трех букв: 'с' (custom — архив .tar.gz), 't' (tar — tar-файл), 'p' (plain — текстовый файл). В команде букву надо указывать без кавычек.
Вместо dbname – имя вашей БД.
Вместо dumpfile– название файла дампа.

если sql дамп.
psql -U {user_name} -d {database_name} -f {file_path} -h {host_name}
database_name: Which database should you insert your file data in.
file_path: Absolute path to the file through which you want to perform the importing.
host_name: The name of the host. For development purposes, it is mostly localhost.


Импорт может продолжаться длительное время. Дождитесь сигнала о завершении (переход на следующую строку в SSH клиенте).

Экспорт
Чтобы осуществить экспорт дампа, воспользуйтесь командой:
pg_dump -h hostname -U username -F format -f dumpfile dbname


# Работа с Postgres

sudo apt-add-repository ppa:pitti/postgresql
sudo apt-get update
sudo apt-get install postgresql-9.2


sudo -u postgres psql

CREATE DATABASE test_database;
CREATE USER test_user WITH password 'qwerty';
GRANT ALL ON DATABASE test_database TO test_user;

psql -h localhost test_database test_user



CREATE SEQUENCE user_ids;
CREATE TABLE users (
  id INTEGER PRIMARY KEY DEFAULT NEXTVAL('user_ids'),
  login CHAR(64),
  password CHAR(64));
