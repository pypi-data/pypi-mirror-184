#  wia_scan

![wia_scan](res/teaser.png)

A simple utility for using document scanners that support [Windows Image Acquisition (WIA)](https://learn.microsoft.com/en-us/windows/win32/wia/-wia-startpage) and is easy to install. If your scanner works using `Windows Fax and Scan`, there is a good chance it will work with this python script.

Use cases:
* You have a flatbed scanner and you need to scan a lot of documents, thus you don't want to use Windows Fax and Scan tool as it can introduce quite some overhead.
* Support scanners on Windows using a simple python dependency

Alternatives: Existing WIA libraries, but to my surprise the ones I found required quite old versions of python, which I didn't want since I wanted to combine the scanning process with some modern python packages.

## Installation
```
pip install wia_scan
```

### Alternative: From Source
Download this source and install flit uisng `pip install flit` and run the following command from the source folder
```
flit install
```

## Usage

### Command Line Interface

```
wia_scan <version>

Usage:
  wia_scan list_devices [-v]
  wia_scan single_side [-v]
  wia_scan many_flatbed [-v]
  wia_scan --help

Options:
  -h --help            Show this screen.
  --version            Show version.
  -v --verbose         Verbose output
```


### Library Usage - Custom Loop
Example: Scan 10 single sided documents from the same scanner:
```
import os
from wia_scan import *

print_function = print
device_manager = get_device_manager()
device_identifier = prompt_choose_device(device_manager=device_manager, print_function=print_function)
device = connect_device(device_manager=device_manager,
                        device_identifier=device_identifier, print_function=print_function)
for i in range(10):
    os.system("pause")
    wia_image = scan_side(device=device, settings=DEFAULT_SCAN_SETTINGS,
                        print_function=print_function)
    wia_image.SaveFile(f'{i}.jpeg')
```


## License
`wia_scan` is distributed under the terms of the MIT license.
