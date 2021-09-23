# Пакет ROS для робота TurtleBro

Текущая (master) ветка для ROS Noetic и python3

Версия для ROS melodic в ветке [Melodic](https://github.com/voltbro/turtlebro/tree/melodic)


### Установка пакета

Для установки пакета, необходимо склонировать репозиторий в вашу папку `catkin_ws/src`

```bash
cd ~/catkin_ws/src
git clone https://github.com/voltbro/turtlebro
```

Далее необходимо запустить процесс сборки пакета

```bash
cd ~/catkin_ws
catkin_make --pkg=turtlebro
```

Для работы, может понадобиться пакет `rosserial`. Если пакет не установлен, то его можно установить командой

```bash
sudo apt install ros-melodic-rosserial-arduino && sudo apt install ros-melodic-rosserial
```
