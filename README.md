# Face Capure

Simple tool which locates and labels faces in photographs. This tool uses [NumPy](http://www.numpy.org/) and [OpenCV](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html) libraries.

## Requirements

* Python `3.x`

## Instructions

1. Clone `face-capture` repository in a local directory.

```sh
git clone https://github.com/kghamilton89/face-capture.git
```

2. Install OpenCV:

```sh
sudo apt-get install build-essential
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
```

3. Install NumPy:

```sh
sudo apt-get install python-numpy
```

2. Store the photo to be analyzed in the same directory as the repository.
3. Navigate to the new directory.

```sh
cd ./path/to/new-directory
```

4. Enable execute permissions and run `capture.py`.

```sh
chmod +x capture.py
python capture.py
```

### Results
