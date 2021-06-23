# CHANGELOG

## 22/06/2021 Feature inclusion de protocolos

Debido a la incorporacion de una camara Dahua nueva, es necesario incluir otros tipos de protocolos que permitan capturar las imagenes

Se modifica capture para construir una url en función de los valores del definidas en las varaibles de entorno.
La url final se construye a partir de una plantilla de url que se reemplazara integrando los datos de usuario y contraseña.

las url tienen una apariencia similar a:

protocolo://usuario:passwor@ip/carpetas?otrainfo

los datos de usuario y passoword deben ser ingresados como tags (frases encerradas entre {}) para que sean insertados en la ruta

## 13/06/2021 docker deploy

Preparo los archivos para que se pueda implementar como un servicio de docker.
Se puede ejecutar con docker compose usando docker-compose.yml que acompaña al proyecto, cambiando el puerto segun se requiera.
Tambien se puede ejecutar un contenedor con 

```bash
docker run --publish 6001:5000 -e CAM_USERNAME=admin -e CAM_PASSWORD=123456 -e CAM_URL=192.168.0.240/media?action=stream vyra-camera
```

Indicando los puertos a exponer y los valores de las varaibles de entorno.

## 12/06/2021 Testing OpenCV Solution

Implemente un servidor con Flask con dos rutas. El index incorpora un img que visualiza un stream de una imagen jpg multiparte provista por la ruta /video.
La ruta /video entrega un flujo continuo de captura de imagenes por medio de opencv

Para esto tuve que instalar Flask

```bash
conda install -c anaconda flask
```

El servidor se activa en modo debug
Los nombres de usuario, password y url se harcodean en app.py

## 12/06/2021 Pruebas

Trate de utilizar el html y javascript que resulta del acceso al servidor de video de la camara IP. Pero tiene CORS activado, por lo que no se puede obtener acceso a nada mas que la imagen en forma de lectura.

La lectura de la imagen se realiza utilizando la propiedad src del elemento img, pero este elemento no tiene un metodo para detectar el error de la carga de stream.

Procedo a preparar un entorno conda para utilizar opencv con python. El objetivo es crear un simple servidor web con python que permita refrescar la imagen cada vez que el stream se corte. La implementación se realizara con docker.

La instalación utilizada por el momento consiste en:

```bash
# instalar conda
# configurar conda
# actualizar conda
conda update conda
conda update conda-build

# crear un entorno
conda create --name camera python=3.9.5

# activar entorno
conda activate camera

# actualizar pip
python -m pip install -U pip 

# instalar opencv
conda install -c conda-forge opencv
```

