import boto3
import uuid

def setup():
    secrets_manager_client = boto3.client("secretsmanager")
    secret_values = get_values()
    seed_secrets_manager(secrets_manager_client, secret_values)

def get_values(quantity: int = 45):
    values = []
    for v in range(quantity):

        item = {
            "description": f"item number {v}",
            "name": f"some_secret_{str(uuid.uuid4())}",
            "secret_string": str(uuid.uuid4()) if v != 32 else f"OS_YOU_FOUNDIT_{str(uuid.uuid4())}"
        }
        values.append(item)

    return values

def seed_secrets_manager(client, data: list):
    for d in data:
        try:
            response = client.create_secret(
                Description=d["description"],
                Name=d["name"],
                SecretString=d["secret_string"]
            )
        except:
            raise

if __name__ == "__main__":
    setup()