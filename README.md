# CWHQ File Backup

The CWHQ File Backup script allows CWHQ users to create compressed archives of project folders and download them locally.

## Installation

Create a file called `main.py` in the root of your Editor's file system and copy the contents of [https://raw.githubusercontent.com/daniel-schroeder-dev/cwhq-file-backup/main/main.py](https://raw.githubusercontent.com/daniel-schroeder-dev/cwhq-file-backup/main/main.py) into the file.

## Usage

Run the `main.py` file to execute the app. 

You'll need to provide two pieces of configuration each time you run the app:
1. Your CWHQ username
2. Your preferred archive format
    - This is either ZIP (`zip`) or tar + gzip (`gztar`)

To compress all folders for a course, enter the course name without the lesson number. For example, if I had all of these folders in my file tree, I would use the pattern `i_h113_intro_python` as the folder pattern to compress: 

```text
➜  cwhq-file-backup git:(main) tree -L 1
.
├── i_h113_intro_python_01
├── i_h113_intro_python_02
├── i_h113_intro_python_03
├── i_h113_intro_python_04
├── i_h113_intro_python_05
├── i_h113_intro_python_06
├── i_h113_intro_python_07
├── i_h113_intro_python_08
├── i_h113_intro_python_09
├── i_h113_intro_python_10
├── i_h113_intro_python_11
├── i_h113_intro_python_12
├── main.py
└── README.md

13 directories, 3 files
```
That would create an archive called `i_h113_intro_python.tar.gz` (assuming I chose the `gztar` option as my archive format) in a directory called `archived-files`:

```bash
➜  cwhq-file-backup git:(main) tree archived-files 
archived-files
└── i_h113_intro_python.tar.gz

0 directories, 1 file
```

There's also an `archived-files.html` file created each time you add a new archive file:

```text
➜  cwhq-file-backup git:(main) cat archived-files.html
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
            <a href="https://danielj.codewizardshq.com/archived-files/i_h113_intro_python.tar.gz">https://danielj.codewizardshq.com/archived-files/i_h113_intro_python.tar.gz</a>
			
        </main>
    </body>
</html>
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

