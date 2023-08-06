import click

from ..._util.format import pretty_info


@click.command()
@click.argument('bucket-name', type=click.STRING)
@click.option('-n', '--namespace', type=click.STRING, show_default=True)
@click.pass_obj
def cli(obj: dict, bucket_name: str, namespace: str):
    """Get bucket acl
    """
    client = obj['client']

    res = client.bucket.get_acl(bucket_name=bucket_name, namespace=namespace)

    click.secho(f'Bucket "{bucket_name}" acl:', bold=True)
    click.echo(pretty_info(res))
