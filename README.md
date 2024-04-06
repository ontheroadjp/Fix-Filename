# Python Script: File Renamer

## Overview

This Python script is designed to rename filenames within a specified directory. It replaces spaces in filenames with underscores and normalizes the filenames using Unicode normalization form KC (NFKC). This can be particularly useful for ensuring consistency and compatibility across different systems and platforms.

## Getting Started

To use this script, follow these steps:

1. Ensure you have Python installed on your system.
2. Download the script from the repository.
3. Rename the script to `fix_filename.py`.
4. Open a terminal or command prompt.
5. Navigate to the directory containing the script.
6. Run the script using the following command:
   
   ```
   python fix_filename.py <dir> <extension> [-r] [-v]
   ```
   
   Replace `<dir>` with the target directory where you want to rename files, and `<extension>` with the target file extension. Optionally, use the flags `-r` or `--recursive` to enable recursive mode and `-v` or `--verbose` to display detailed operating steps.

## Environment

This script is written in Python and should be compatible with both Python 2 and Python 3.

## Usage

```
python fix_filename.py <dir> <extension> [-r] [-v]
```

- `<dir>`: Target directory where filenames will be renamed. If not specified, the current directory will be used.
- `<extension>`: Target file extension to specify the type of files to rename.
- `-r`, `--recursive`: Optional flag to enable recursive mode, which searches for files in subdirectories as well.
- `-v`, `--verbose`: Optional flag to display detailed operating steps.

## Example

Suppose you have a directory structure like this:

```
parent_directory/
    ├── subdirectory1/
    │   ├── file with spaces.md
    │   ├── another_file.md
    │   └── ...
    ├── subdirectory2/
    │   ├── some file.md
    │   ├── example file.md
    │   └── ...
    └── ...
```

To rename all files with the extension `.md` within the `parent_directory` and its subdirectories, you can run the following command:

```bash
python fix_filename.py parent_directory md -r -v
```

This command will perform the following actions:

- Traverse through the `parent_directory` and its subdirectories.
- Find all files with the `.md` extension.
- Rename each file, replacing spaces with underscores and normalizing the filenames.
- Display detailed operating steps due to the `-v` or `--verbose` flag.

After the execution of the script, your directory structure will be updated as follows:

```
parent_directory/
    ├── subdirectory1/
    │   ├── file_with_spaces.md
    │   ├── another_file.md
    │   └── ...
    ├── subdirectory2/
    │   ├── some_file.md
    │   ├── example_file.md
    │   └── ...
    └── ...
```

All filenames will now be normalized, with spaces replaced by underscores.
