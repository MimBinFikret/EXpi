**Title: Enhanced Recursive File Content Extractor (EXpi)**

## Description

EXpi (Enhanced Recursive File Content Extractor) is a Python script that allows you to easily aggregate the content of all files within a specified directory and its subdirectories into a single text file. This feature is particularly useful for transferring the data of a local project to an AI chatbot or any other application.

**Note:** Please be cautious when using this script with projects containing binary files or extremely large files, as it may lead to undesirable results.

## How to Use

1. Copy the "expi.py" script into the root folder of the project from which you want to extract the content.

2. Navigate to the root folder of your project using the command line or terminal.

3. Run the script by executing the following command:

```bash
python expi.py
```

4. The script will recursively read the content of all files within the project's directory and its subdirectories.

5. Once the process is complete, it will generate an "output.txt" file in the root folder containing the aggregated content of all the files.

6. You can now use the "output.txt" file as needed, such as inputting it into an AI chatbot or any other application.

## Example Output

```
<file name: ./a.c>
<content>
--content of a.c file here--
<content/>
<file/>

<file name: ./src/x.cpp>
<content>
--content of x.cpp file here--
<content/>
<file/>
```

## Requirements

- Python 3.x

## License

This project is licensed under the [MIT License](LICENSE).

## Contribution

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## Disclaimer

This script deals with file I/O operations, so use it with caution. Always make sure to back up your important data before running any code that might modify or delete files. The author of this script is not responsible for any loss of data.

Feel free to use, modify, and distribute this script following the terms of the MIT License. Happy coding!
