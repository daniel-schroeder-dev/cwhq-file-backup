#!/usr/local/bin/python3.11


from pathlib import Path
from shutil import make_archive, rmtree, copytree
from string import Template


def create_zip(folder_starts_with: str, zip_format: str) -> None:
    root_path = Path("./")

    folder_zip_path = root_zip_path / Path(folder_starts_with)
    temp_folder_zip_path = Path(f"temp-{folder_starts_with}")

    if not root_zip_path.exists():
        root_zip_path.mkdir()

    if folder_zip_path.exists():
        rmtree(folder_zip_path)

    if temp_folder_zip_path.exists():
        rmtree(temp_folder_zip_path)

    temp_folder_zip_path.mkdir()

    for child_path in sorted(root_path.iterdir()):
        if str(child_path).startswith(folder_starts_with):
            copytree(child_path, temp_folder_zip_path / child_path)

    make_archive(str(folder_zip_path), zip_format, temp_folder_zip_path)
    build_html_file()

    rmtree(temp_folder_zip_path)


def view_zip_files():
    if not root_zip_path.exists():
        print("You don't have any zipped files yet!")
        return

    print(*[path.name for path in sorted(root_zip_path.iterdir())], sep="\n")


def build_html_file():
    with open("zipped-files.html", mode="wt", encoding="utf-8") as zipped_files:
        links = ""
        for child_path in sorted(root_zip_path.iterdir()):
            download_path = username_root_url + str(child_path)
            links += f'<a href="{download_path}">{download_path}</a>'
        template = Template(html_container).safe_substitute(links=links)
        zipped_files.writelines(template)


def download_all_zips():
    zipped_html_path = username_root_url + "zipped-files.html"
    print(f"Go to {zipped_html_path} to download all zipped files")


options = """

    Welcome to the ZIP Archive creator!

Available Options:

    1. Create ZIP Archive
    2. View ZIP Archives
    3. Download All ZIP Archives
    4. Exit
"""

CREATE_ZIP = 1
VIEW_ZIP = 2
DOWNLOAD_ALL_ZIPS = 3
EXIT = 4


root_zip_path = Path("zipped-files")

username = input("Please enter your CWHQ username: ")
username_root_url = f"https://{username}.codewizardshq.com/"


zip_format_options = """
    Here are the possible ZIP format options:
    
        - zip
        - tar
        - gztar
"""

print(zip_format_options)
zip_format = input("Enter desired ZIP format: ")

html_container = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta http-equiv="X-UA-Compatible" content="ie=edge" />
        <title>Zipped CWHQ Files</title>
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
        <h1>Zipped Project Files</h1>
        <main>
            $links
        </main>
    </body>
</html>
"""


while True:
    user_choice = int(input(options))

    if user_choice == CREATE_ZIP:
        folder_starts_with = input("Enter the pattern the folder starts with: ")
        create_zip(folder_starts_with, zip_format)
    elif user_choice == VIEW_ZIP:
        view_zip_files()
    elif user_choice == DOWNLOAD_ALL_ZIPS:
        download_all_zips()
    elif user_choice == EXIT:
        print("Goodbye!")
        break
