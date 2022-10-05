# image_filtering_without_module
### You are given a Portrait of a Young Woman which is a small oil-on-oak panel painting completed in 1470 (Portrait_of_a_Young_Woman.jpg). It marks a major stylistic advance in contemporary portraiture; the girl is set in an airy, three-dimensional, realistic setting, and stares out at the viewer with a complicated expression that is reserved, yet intelligent and alert.

![image](https://user-images.githubusercontent.com/54437726/194074017-0bc6d752-e383-4f06-8dcc-b0aa27c9bb1e.png)


### However, because this picture belongs to a 15th century painting, we clearly see the deformation and cracks within the picture.
### Find a way to digitally improve the quality of this picture with a Python code (30 points). (must be done without a python library)

In this application, after importing the necessary libraries, a function is created to filter the image. For this, a kernel is specified. After the dimensions of the image and offset are defined, the specified kernel is applied to the image by navigating with the for loops. The image is filtered by navigating the pixels.

![image](https://user-images.githubusercontent.com/54437726/194074348-1980fd6a-8377-4649-9420-aee949264f49.png)


This function applies the mean filter (Smoothing/Averaging/Box filtering). The mean filter is a simple and easy to apply method of softening images. In other words, to reduce the amount of change between one pixel and the others. Often used to reduce noise in images. The mean filter is a convolution filter. Convolution filters are based on kernel. In this filtering application In this filtering application, 7x7 kernel is used.

The difference between the original image and the filtered image is shown below :

![image](https://user-images.githubusercontent.com/54437726/194074551-a931cdd4-22cc-486e-853b-f9df01cdc355.png)
