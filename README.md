# click_tutorial
A simple tutorial about how to use click

## Basic configurations
1. install library using this command:
`pip install click`

2. write some function
```python
def main():
    click.echo('welcome to click')
```
click.echo prints the data as usual.
3. convert function into command
Using a `@click.command()` decorator, converts the function into a cli-command.

4. run command by `python <filename.py> <command-name>`.

By providing docstrings for commands, it displays on --help command.

## Adding options
You can add some options to command. 
```python
@click.option(long_parameter_name, short_parameter_name, default=DEFAULT_VALUE, help=HELP_TEXT, nargs=NUMBER, type=INT)
```
The decorator `@click.option()` is the primary code to add options.

The first and second arguments are long and short parameter forms. The long form is also used as the parameter name of function. Long parameter comes with 2 dash and short one comes with 1.

The default, is the value if nothing is entered for parameter.

Help is the text that appears in help command.

Type defines the type of parameters and it typecast them itself.

Nargs is the count of acceptable values for that option and its default value is 1.

As you may guess, we can have multiple options too. As we can pass it with multiple duplicate options. 
## Adding arquments
You can add some options to command. 
```python
@click.argument(ARGUMENT_NAME, default=DEFAULT_VALUE, type=TYPE)
```

The difference between options and arguments, is arguments are nessecory. 

If not enough arguments are provided, you got `Error: Missing Argument`.

Type defines the type of parameters and it typecasts them itself.


## Tips
if nargs is negative, it means you can have as many as you want.

