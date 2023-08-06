#  wia_scan

![wia_scan](res/teaser.png)

A simple utility for using document scanners that support
[Windows Image Acquisition (WIA)](https://learn.microsoft.com/en-us/windows/win32/wia/-wia-startpage)
and is easy to install. If your scanner works using `Windows Fax and Scan`, there is a good chance it will work with this python script.
This package allows you to create your own efficient scanning loop or use the one the one already provided.

Use cases:
* You have a flatbed scanner, and you need to scan a lot of documents, thus you don't want to
  use Windows Fax and Scan tool as it can introduce quite some overhead. This utility allows
  you to only press a few keystrokes in between scans, while you may need to turn the page or
  change the paper since you don't have an automatic feeding scanner like I don't.
* Support scanners in your own application on Windows using a simple Python dependency

Alternatives: Existing WIA libraries, but to my surprise the ones I found required quite old
versions of Python, which I didn't want since I wanted to combine the scanning process with some modern Python packages.

## Installation
```
pip install wia_scan
```

### Alternative: From Source
Download this source and install flit using `pip install flit` and run the following command from the source folder
```
flit install
```

## Usage

### Command Line Interface

```
  wia_scan list_devices [-v]
  wia_scan single [--file=<output_file>] [--dpi=<dpi>] [--brightness=<brightness>] [--contrast=<contrast>] [--mode=<mode>] [-v] [--uid=<uid>] [-q]
  wia_scan many [--out=<output_folder>] [-v]
  wia_scan --help

Options:
  -h --help                    Show this screen.
  --version                    Show version.
  -v --verbose                 Verbose output
  -q --quiet                   Quiet=no output
  --dpi=<dpi>                  Dots per inch; the higher this setting the higher the output resolution
  --brightness=<brightness>    Brightness setting for the scanner, goes from -1000 to 1000
  --contrast=<contrast>        Contrast setting for the scanner, goes from -1000 to 1000
  --mode=<mode>                RGB for colored, L for grayscale
  --file=<output_file>         Image output file
  --out=<output_folder>        Scanned images output folder
```


### Library Usage - Custom Loop
Example: Scan many single sided documents from the same scanner while waiting for a single key press between scans:
```
from wia_scan import *

device = prompt_choose_device_and_connect()
for i in range(1000000):
    press_any_key_to_continue()
    pillow_image = scan_side(device=device, scan_profile=DEFAULT_SCAN_PROFILE)
    filename = f'{i}.jpeg'
    pillow_image.save(filename, subsampling=0, optimize=True,
             progressive=True, quality=80)
```


## License
`wia_scan` is distributed under the terms of the MIT license.
