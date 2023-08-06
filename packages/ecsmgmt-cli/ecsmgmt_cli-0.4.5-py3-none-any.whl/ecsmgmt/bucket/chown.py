import click
from ecsclient.common.exceptions import ECSClientException

from .._util.echo import success
from .._util.exceptions import EcsmgmtClickException


@click.command()
@click.argument('bucket-name', type=click.STRING)
@click.argument('user-id', type=click.STRING)
@click.option('-n', '--namespace', type=click.STRING, show_default=True)
@click.pass_obj
def cli(obj: dict, bucket_name: str, user_id: str, namespace: str):
    """Change owner of bucket
    """
    client = obj['client']

    try:
        client.bucket.set_owner(bucket_name=bucket_name, new_owner=user_id, namespace=namespace)
        success(f'changed owner of bucket "{bucket_name}" to "{user_id}"')
    except ECSClientException as e:
        raise EcsmgmtClickException(e.message)
