## TECHNOLOGY HEALTH COMPUTING

Aplicación que monitoriza la distancia de la persona frente al monitor y la analiza para una mejora ergonomica del usuario.

## INSTALAR PYTHON IDE

    sudo apt update
    sudo apt install python3 idle3

## INSTALAR LIBRERÍA SEEED STUDIO

    curl -sL https://github.com/Seeed-Studio/grove.py/raw/master/install.sh | sudo bash -s -

## INSTALAR GUIZERO

    sudo pip3 install guizero

## INSTALAR LIBRERÍA REQUESTS

    pip install requests

## CREAR DATAFILES Y MANDAR MAIL CADA CIERTO TIEMPO

    crontab -e

    insertamos la siguiente linea con la ruta del proyecto

    */5 * * * * /home/pi/IOT-Proyect/Data/curl.sh #cada 5 mins

    reiniciamos el servicio de crontab

    /sbin/service cron start

## INICIALIZAR AL INICIO DE LA RPI

    sudo nano /home/pi/.bashrc

    insertar las siguiente linea con la ruta de tu proyecto

    sudo python /home/pi/IOT-Proyect/main.py
