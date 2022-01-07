## THIS IS OUR RASPBERRY PI PROYECT WRITTEN IN PYTHON

## INSTALAR PYTHON IDE

    sudo apt update
    sudo apt install python3 idle3

## INSTALAR LIBRERÍA SEEED STUDIO
    curl -sL https://github.com/Seeed-Studio/grove.py/raw/master/install.sh | sudo bash -s -

## INSTALAR GUIZERO
    sudo pip3 install guizero
    
## INSTALAR LIBRERÍA REQUESTS
    pip install requests
    
## INICIALIZAR AL INICIO DE LA RPI
    sudo nano /home/pi/.bashrc

    insertar las siguiente linea con la ruta de tu proyecto

    sudo python /home/pi/IOT-Proyect/main.py

