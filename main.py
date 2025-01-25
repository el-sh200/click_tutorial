import click


@click.command()
@click.option('--name', '-n', default='Elham', help='Firstname description')
# @click.option('--name', '-n', nargs=2)
@click.option('--location', '-l', multiple=True)
def main(name, location):
    click.echo(f'Hello, {name}!')
    click.echo(f'\n{location}')


if __name__ == '__main__':
    main()
