import boto3
from botocore.exceptions import NoCredentialsError

def upload_file_to_s3(file_name, bucket_name, object_name=None):

    if object_name is None:
        object_name = file_name

    s3 = boto3.client('s3')

    try:
        s3.upload_file(file_name, bucket_name, object_name)
        print(f'El archivo {file_name} se ha subido exitosamente a S3 en el bucket {bucket_name} como {object_name}')
        return True
    except FileNotFoundError:
        print(f"El archivo {file_name} no se encontró.")
    except NoCredentialsError:
        print("No se encontraron credenciales de AWS. Asegúrate de configurar tus credenciales.")
    except Exception as e:
        print(f"Ocurrió un error al subir el archivo a S3: {str(e)}")  # Aquí estaba incompleto

        return False

# Definir los nombres de archivo local, nombre de bucket y nombre en S3
local_file = 'ml_creditCard.py'
bucket_name = 'ml-practica-serviciosnube'
s3_file_name = 'ml_creditCard.py'

# Llamar a la función para cargar el archivo
upload_file_to_s3(local_file, bucket_name, s3_file_name)

