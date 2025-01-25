import click


@click.command()
@click.option('--name', '-n', default='Elham', help='Firstname description')
# @click.option('--name', '-n', nargs=2)
@click.option('--location', '-l', multiple=True)
@click.argument('age', default=23, type=int)
def main(name, location, age):
    click.echo(f'Hello, {name}!')
    click.echo(f'\n{location}')


if __name__ == '__main__':
    main()
