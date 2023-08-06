#  wia_scan

![wia_scan](res/teaser.png)

A simple utility for using document scanners that support [Windows Image Acquisition (WIA)](https://learn.microsoft.com/en-us/windows/win32/wia/-wia-startpage) and is easy to install. If your scanner works using `Windows Fax and Scan`, there is a good chance it will work with this python script.

Use case:
*  You have a flatbed scanner and you need to scan a lot of documents, thus you don't want to use Windows Fax and Scan tool as it can introduce quite some overhead.

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
wia_scan many --callibration_file calib...
```


```
wia_scan list_devices
```

```
wia_scan single
```


```
wia_scan calibrate
```


### Library Usage - Custom Loop

```
from wia_scan import scan
```


## License
`wia_scan` is distributed under the terms of the MIT license.
