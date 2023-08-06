import os, click
from .snippets.css import (
    meta_data,
    default_style,
)
from .snippets.html import (
    default_footer_content,
    default_header_content,
    default_home_content,
    default_page_content,
)
from .snippets.php import (
    default_functions,
    default_theme_options,
    functions_no_bs,
    golden_content,
)
from .snippets.sass import (
    default_sass,
)
from .vars import file_names


@click.command()
@click.option(
    "--theme_name",
    default="custom_theme",
    help="Change the theme name.  Default: 'custom_theme'",
)
@click.option(
    "--classic",
    default=True,
    help='Determines whether template files should be classic "php" (True) or block style "html" (False).  Default: True',
)
@click.option(
    "--bootstrap",
    default=True,
    help="Determines whether or not to use bootstrap.  Default: True",
)
@click.option(
    "--sass", default=True, help="Determines whether or not to use Sass.  Default: True"
)
def cli(theme_name, classic, bootstrap, sass):
    """Create the default files for the custom theme"""
    base_url = os.getcwd()
    base_url += f"\\{theme_name}"

    os.mkdir(base_url)
    os.mkdir(f"{base_url}\\css\\")
    os.mkdir(f"{base_url}\\assets\\")
    os.mkdir(f"{base_url}\\includes\\")

    if sass:
        with open(f"{base_url}\\main.scss", "w") as f:
            f.write(default_sass())

    for filename in file_names:
        base_filename = f"{base_url}\\{filename}"
        if filename == "style":
            file_name = f"{base_filename}.css"
            data = meta_data
        elif filename == "functions":
            file_name = f"{base_filename}.php"
            if bootstrap:
                data = default_functions()
            else:
                data = functions_no_bs()

            data += default_theme_options()
        elif filename == "main":
            file_name = f"{base_url}\\css\\{filename}.css"
            data = default_style()
        else:
            file_name = f"{base_filename}.php" if classic else f"{base_filename}.html"
            if filename == "header":
                data = default_header_content()
            elif filename == "page":
                data = default_page_content()
            elif filename == "home":
                data = default_home_content()
            elif filename == "footer":
                data = default_footer_content()
            else:
                data = golden_content() if classic else f"<h1>{filename}</h1>"

        with open(file_name, "w") as f:
            f.write(str(data))


if __name__ == "__main__":
    cli()
