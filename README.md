# Chrome Dragon Game With IMU
---
## What is IMU?
IMU(Inertial measurement unit)包含加速度計、陀螺儀的晶片單元，用以算出物體的姿態。

---

## Google Dragon Game

Google 離線狀態的情況下會出現一個可愛的恐龍遊戲，本專案利用嵌入式系統開發版來操控這隻可愛的小恐龍
![Dino Game](https://programcodelib.com/wp-content/uploads/2015/01/google-chrome-offline-game11.jpg)

---
## Pre-requirement
* BeagleBone Black 開發版 x 1
* LSM9DS0晶片(陀螺儀、加速度計、磁力計) x 1
* Linux based os

---
## Installation

* **Beaglebone Black**
    Compile LSM9DS0
    ```
    g++ -shared -fPIC -o 1sm9ds0.so 1sm9ds0.cpp
    ```


    Python dependency

    ```
    pip install numpy
    pip install websockets
    ```

* **LocalMachine**
    Python dependency
    ```
    pip install websockets
    pip install
    ```