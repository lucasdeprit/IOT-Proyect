## TECHNOLOGY HEALTH COMPUTING

Aplicación que monitoriza la distancia de la persona frente al monitor y la analiza para una mejora ergonomica del usuario.


## INSTALACIÓN 

   Clonamos el repositorio
    
    git clone https://github.com/lucasdeprit/IOT-Proyect.git
    
   para ejecutarlo manualmente realizaremos los siguientes pasos:
    
    cd IOT-Proyect/
    
    python main.py #para ejecutar los sensores y guardar los datos en corlysis
    
    cd Data/
    
    ./curl.sh #para generar los documentos de recolecta de datos y mandar un mail
    

## DEPENDENCIAS

### INSTALAR PYTHON IDE

    sudo apt update
    sudo apt install python3 idle3

### INSTALAR LIBRERÍA SEEED STUDIO

    curl -sL https://github.com/Seeed-Studio/grove.py/raw/master/install.sh | sudo bash -s -

### INSTALAR SEEED_DHT

    sudo pip install seeed-python-dht ##para sensor de humedad y temperatura
    
### INSTALAR SERVICIO SMTP

    sudo pip install smtplib #para mandar los mails
    
### INSTALAR LIBRERÍA REQUESTS

    pip install requests #para realizar las requests

### CREAR DATAFILES Y MANDAR MAIL CADA CIERTO TIEMPO

    crontab -e

    insertamos la siguiente linea con la ruta del proyecto

    */5 * * * * /home/pi/IOT-Proyect/Data/curl.sh #cada 5 mins

    reiniciamos el servicio de crontab

    /sbin/service cron start

### INICIALIZAR AL INICIO DE LA RPI

    sudo nano /home/pi/.bashrc

    insertar las siguiente linea con la ruta de tu proyecto

    sudo python /home/pi/IOT-Proyect/main.py
    
