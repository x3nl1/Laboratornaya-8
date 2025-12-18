import click

@click.command()
@click.argument('name')
def hello(name):
    """Приветствует пользователя"""
    print(f"Привет, {name}!")

if __name__ == '__main__':
    hello()