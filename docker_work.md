Что такое Докер: https://guides.hexlet.io/docker/

## Настройка на Ubuntu

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```
если ошибка: error add-apt-repository command not found
```
sudo apt install software-properties-common
```

```
sudo apt-get update
apt-cache policy docker-ce
sudo apt-get install -y docker-ce
sudo systemctl status docker
```

Для того чтобы добавить можно было запускать докер-команды от обычного пользователя:

```
sudo usermod -aG docker ${USER}
su - ${USER}
id -nG
```

Подробнее: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04

## Установка docker-compose

```
sudo curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```

Подробнее: https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-16-04



