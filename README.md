# Пакет ROS для робота TurtleBro


### Установка пакета на компьютер

Для установки пакета, необходимо склонировать репозиторий в вашу папку `catkin_ws/src`

```bash
cd ~/catkin_ws/src
git clone https://github.com/voltbro/turtlebro
```

Далее необходимо запустить процесс сборки пакета

```bash
cd ~/catkin_ws
sudo ./src/catkin/bin/catkin_make --install -DCMAKE_BUILD_TYPE=Release --install-space /opt/ros/melodic --pkg=turtlebro
```

Для работы, может понадобиться пакет `rosserial`. Если пакет не установлен, то его можно установить командой

```bash
sudo apt install ros-melodic-rosserial-arduino && sudo apt install ros-melodic-rosserial
```
### Установка пакета на робота

Для установки пакета, необходимо склонировать репозиторий в вашу папку `ros_catkin_ws/src`

```bash
cd ~/ros_catkin_ws/src
git clone https://github.com/voltbro/turtlebro
```

Далее необходимо запустить процесс сборки пакета

```bash
cd ~/catkin_ws
sudo ./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release --install-space /opt/ros/kinetic --pkg=turtlebro
```

Для работы, может понадобиться пакет `rosserial`. Если пакет не установлен, то его можно установить командой

```bash
sudo apt install ros-melodic-rosserial-arduino && sudo apt install ros-melodic-rosserial
```

