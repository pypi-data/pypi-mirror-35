import click
import dnz
import json
import sys


@click.group(context_settings=dict(
    ignore_unknown_options=True,
    allow_extra_args=True,
))
@click.pass_context
def cli(ctx, **kwargs):
    pass


@cli.command(context_settings=dict(
    ignore_unknown_options=True,
    allow_extra_args=True,
))
@click.option('--host', '-h', default='www.espn.com', multiple=True, help='Host')
@click.option('--out', '-o', help='Help file to write out to')
@click.option('--format', '-f', default='json', type=click.Choice(['json', 'csv', 'txt']), help='Format of writing to file')
@click.argument('engine')
@click.pass_context
def targets(ctx, **kwargs):
    extra_args = {}
    if ctx.args:
        for item in ctx.args:
            extra_args.update({item.split('=')[0].replace('--', '').replace('-', ''): item.split('=')[1]})

    engine_cls = dnz.get_engine(kwargs.get('engine'))

    if not engine_cls:
        click.echo(click.style(f'{kwargs.get("engine")} is not a valid engine', 'red'))
        sys.exit(1)

    try:
        engine = engine_cls(**extra_args)
    except TypeError:
        click.echo(click.style('An option was entered that is not allowed', 'red'))
        sys.exit(1)

    total_output = {}

    for host in kwargs.get('host'):
        try:
            output = engine.run(host)
            total_output.update({host: output})
        except Exception:
            raise

    if kwargs.get('format') == 'json':
        click.echo(json.dumps(total_output))
    elif kwargs.get('format') == 'csv':
        pass
    else:
        for k, v in total_output.items():
            click.echo('\n'.join(v))


if __name__ == '__main__':
    cli()
