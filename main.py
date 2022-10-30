from pathlib import Path
from shutil import make_archive, rmtree, copytree
from string import Template


def build_html_file():
    """Builds an HTML file which you can view to download the compressed archives."""

    with open(archive_html_filename, mode="wt", encoding="utf-8") as archived_files:
        links = ""
        for child_path in sorted(root_archive_path.iterdir()):
            download_path = username_root_url + str(child_path)
            links += f'<a href="{download_path}">{download_path}</a>\n\t\t\t'
        template = Template(html_container).safe_substitute(links=links)
        archived_files.writelines(template)


def create_archive(folder_starts_with: str, archive_format: str) -> None:
    """Creates a compressed archive based on `archive_format` with all directories that begin
    with `folder_starts_with`."""

    folder_archive_path = root_archive_path / Path(folder_starts_with)
    temp_folder_archive_path = Path(f"temp-{folder_starts_with}")

    if not root_archive_path.exists():
        root_archive_path.mkdir()

    if folder_archive_path.exists():
        rmtree(folder_archive_path)

    create_temp_files(folder_starts_with, temp_folder_archive_path)
    make_archive(str(folder_archive_path), archive_format, temp_folder_archive_path)
    build_html_file()
    rmtree(temp_folder_archive_path)


def create_temp_files(folder_starts_with: str, temp_folder_archive_path: Path) -> None:
    """
    Creates a temporary folder to hold all files with `folder_starts_with` as the start of the path.

    We need this because it is easy to zip all of the folders at once if they are in a central location
    like this temporary folder. The `temp_folder_archive_path` will be removed after we create the
    compressed archive files.
    """

    if temp_folder_archive_path.exists():
        rmtree(temp_folder_archive_path)

    temp_folder_archive_path.mkdir()

    root_path = Path("./")
    for child_path in sorted(root_path.iterdir()):
        if str(child_path).startswith(folder_starts_with):
            copytree(child_path, temp_folder_archive_path / child_path)


def view_archives():
    """Lets a user view all of the compressed archive files in the `root_archive_path`."""

    if not root_archive_path.exists():
        print("You don't have any compressed archive files yet!")
        return

    print("\nCurrent archives\n")
    print("#" * 60)
    print()
    print(*[path.name for path in sorted(root_archive_path.iterdir())], sep="\n")
    print()
    print("#" * 60)
    print()


def view_archive_html_path():
    """"""
    archive_html_path = username_root_url + archive_html_filename
    print(f"Go to {archive_html_path} to download all compressed archive files")


options = """
    Welcome to the CWHQ Compressed Archive creator!

Available Options:

    1. Create Compressed Archive
    2. View Compressed Archives
    3. Download All Compressed Archives
    4. Exit
"""

html_container = """\
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta http-equiv="X-UA-Compatible" content="ie=edge" />
        <title>Compressed CWHQ Files</title>
        <style>
            body {
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            
            a {
                display: block;
                padding: 6px;
                margin: 4px;
                border-radius: 4px;
                width: fit-content;
            }

            a:hover {
                background-color: gainsboro;
            }
        </style>
    </head>
    <body>
        <h1>Compressed Project Files</h1>
        <main>
            $links
        </main>
    </body>
</html>
"""

CREATE_ARCHIVE = 1
VIEW_ARCHIVES = 2
DOWNLOAD_ARCHIVES = 3
EXIT = 4

root_archive_path = Path("archived-files")
archive_html_filename = "archived-files.html"

username = input("Please enter your CWHQ username: ")
username_root_url = f"https://{username}.codewizardshq.com/"

archive_format = input("Enter your desired compression archive format (zip or gztar): ")

while True:
    user_choice = int(input(options))

    if user_choice == CREATE_ARCHIVE:
        folder_starts_with = input("Enter the pattern the folder starts with: ")
        create_archive(folder_starts_with, archive_format)
    elif user_choice == VIEW_ARCHIVES:
        view_archives()
    elif user_choice == DOWNLOAD_ARCHIVES:
        view_archive_html_path()
    elif user_choice == EXIT:
        print("Goodbye!")
        break
