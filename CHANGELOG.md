# CHANGELOG

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

