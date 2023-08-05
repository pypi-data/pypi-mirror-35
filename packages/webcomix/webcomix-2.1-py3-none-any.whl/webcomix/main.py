#! python3

import click

from webcomix.comic import Comic
from webcomix.search import discovery
from webcomix.supported_comics import supported_comics


@click.group()
@click.version_option()
def cli():
    pass


@cli.command()
def comics():
    """
    Shows all predefined webcomics
    """
    comics_content = [
        "{}: {}".format(key, value[0])
        for key, value in sorted(supported_comics.items())
    ]

    click.echo("\n".join(comics_content))


@cli.command()
@click.argument("name", type=click.STRING)
@click.option(
    "--cbz",
    is_flag=True,
    default=False,
    help="Outputs the comic as a cbz file")
def download(name, cbz):
    """
    Downloads a predefined webcomic by name
    """
    if name in list(supported_comics.keys()):
        comic = Comic(*supported_comics[name])
        comic.download(name)
        if cbz:
            comic.make_cbz(name, name)


@cli.command()
@click.argument("name", type=click.STRING)
@click.option(
    "--start_url",
    prompt=True,
    type=click.STRING,
    help="URL of the comic's first page")
@click.option(
    "--cbz",
    default=False,
    is_flag=True,
    help="Outputs the comic as a cbz file")
@click.option(
    "--yes",
    "-y",
    default=False,
    is_flag=True,
    help="Skips the verification prompt")
def search(name, start_url, cbz, yes):
    """
    Downloads a webcomic using a general XPath
    """
    comic = discovery(start_url)
    if comic is not None:
        validation = Comic.verify_xpath(comic.start_url,
                                        comic.next_page_selector,
                                        comic.comic_image_selector)
        print_verification(validation)
        click.echo(
            "Verify that the links above are correct.")
        if yes or click.confirm("Are you sure you want to proceed?"):
            comic.download(name)
            if cbz:
                comic.make_cbz(name, name)


@cli.command()
@click.option(
    "--comic_name",
    prompt=True,
    type=click.STRING,
    help="Name of the user-defined comic")
@click.option(
    "--start_url",
    prompt=True,
    type=click.STRING,
    help="URL of the comic's first page")
@click.option(
    "--next_page_xpath",
    prompt=True,
    type=click.STRING,
    help="XPath expression giving the url to the next page")
@click.option(
    "--image_xpath",
    prompt=True,
    type=click.STRING,
    help="XPath expression giving the url to the image")
@click.option(
    "--cbz",
    default=False,
    is_flag=True,
    help="Outputs the comic as a cbz file")
@click.option(
    "--yes",
    "-y",
    default=False,
    is_flag=True,
    help="Skips the verification prompt")
def custom(comic_name, start_url, next_page_xpath, image_xpath, cbz, yes):
    """
    Downloads a user-defined webcomic
    """
    comic = Comic(start_url, next_page_xpath, image_xpath)
    validation = Comic.verify_xpath(comic.start_url,
                                    comic.next_page_selector,
                                    comic.comic_image_selector)
    print_verification(validation)
    click.echo("Verify that the links above are correct.")
    if yes or click.confirm("Are you sure you want to proceed?"):
        comic.download(comic_name)
        if cbz:
            comic.make_cbz(comic_name, comic_name)


def print_verification(validation):
    """
    Prints the verification given by the verify_xpath function
    """
    for i in range(3):
        click.echo("Page {}:\nPage URL: {}\nImage URLs:\n{}\n".format(
            i + 1, validation[i][0], "\n".join(validation[i][1])))
