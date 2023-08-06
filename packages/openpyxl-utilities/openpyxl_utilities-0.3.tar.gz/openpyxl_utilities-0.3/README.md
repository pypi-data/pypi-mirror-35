# Openpyxl_utilities

This project consists of a library with functionalities to work with the popular module openpyxl (mainly used to read and write xlsx and xls files from Python) more efficiently. It was kickstarted when I found out openpyxl package does not includes sorting fucntionalities to create xlsx files already sorted (the only option available was to set a sorting button to sort the rows inside Microsoft Excel, not creating the file already sorted).

### Prerequisites

This script is written in Python 3.6 using the following non-standard modules:
* [openpyxl 2.5 or higher](https://github.com/chronossc/openpyxl)

### Installing

First, make sure you have the prerequisites installed using the following command:

```
$pip freeze
```

If the list of installed modules does not includes openpyxl==2.5 or higher, run the following command:

```
$pip install openpyxl==2.5
```

Once the prerequisites are fullfiled, install the module with the following command:

```
$pip install openpyxl_utilities
```

If no errors are given, you can already import the module as usual 

```
import 

