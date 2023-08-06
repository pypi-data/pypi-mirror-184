from aws import get_client
from botocore.exceptions import ClientError


def get_secret(secret_name='dev-k8s'):
    client = get_client(service='secretsmanager')

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        raise e
    secret = get_secret_value_response['SecretString']
    return secret
