import configparser
import click
import sys

@click.command()
@click.argument('configfile', type=click.File('rb'))
@click.argument('section')
@click.argument('option')
@click.option('-e', '--encoding', default='utf-8')
def extract_from_inifile(configfile, section, option, encoding):
    # click opens a file ready to be read so 
    # read the configfile into a config parser
    # with the specified encoding
    try:
        config = configparser.ConfigParser()
        config.read_string(configfile.read().decode(encoding))
        result = config.get(section, option)
        click.echo(result)
    except configparser.Error as e:
        # If we get an error opening the file then
        # print it to stderr
        click.echo('Error: {}'.format(e), err=True)
        sys.exit()
