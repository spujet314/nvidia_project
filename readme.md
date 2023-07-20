# Project Name

Digit Analyzer

## The Algorithm

This project utilizes a 5 layer Convolutional Neural Network (CNN) to recognize handwritten digits from a USB camera stream. When first run, the model is trained 3 epochs on the full MNIST dataset, a widely used collection of images of handwritten digits. The model is saved in a file which is used in subsequent executions. A sequence of torchvision transforms is used to change the live USB stream into images that can be input into the model, which then makes predictions every 0.25 seconds. The model is decently accurate after this training, but this project also allows the user to create their own, smaller dataset of handwriting samples that the model can train on - a concept called transfer learning. This allows the user to tailor the model to their own style of handrwritten digits.

## Running this project

1. Download dataset.py, net.ipynb, and readme.md.
2. The project relies on the following libraries: torch, torchvision, os, IPython, time, threading, PIL, traitlets, ipywidgets, numpy, and jetcam.
3. To avoid having to install these libraries, run the project in the DLI docker on the jetson nano. Add "--volume ~/<download_dir>:/nvdli-nano/project" to the docker setup file to mount the download directory to the docker image.
4. Execute the code cells in net.ipynb sequentially. Comments will outline two cells that should only be run for the first execution of the program.
5. The second to last cell will launch the GUI for the program.
6. Do not run the last cell until you wish to terminate execution. It will deallocate the memory required for the camera and restart the kernel.

Video explaining functionality: https://www.youtube.com/watch?v=4jEktt6P-AQ
