import cv2
import numpy as np

img = cv2.imread("Portrait_of_a_Young_Woman.jpg")

def filter(image, kernel):
    #Get a image ndarray and a kernel 
    size_y = image.shape[0]   #width
    size_x = image.shape[1]   #height
    ofs = len(kernel)//2    # Middle of the kernel, offset=kernel size/2
    #Compute convolution between intensity and kernels
    for i in range(ofs, size_y-ofs):    
        for j in range(ofs, size_x -ofs):  
            val = 0
            for k in range(len(kernel)**2):
                im_val = image[i + k//len(kernel) - ofs][j+ k%len(kernel)-ofs]
                val += kernel[k//len(kernel)][k%len(kernel)] * im_val
            image[i][j] = val
    return image 
kernel_s = 7  # the dimension of the x and y axis of the kernel (7x7)
kernel = np.ones([kernel_s ** 2])
kernel = kernel / np.sum(kernel)
kernel = np.reshape(kernel,[kernel_s,kernel_s])

img_filtered = filter(img,kernel) #filter function calling
cv2.imshow("filtered",img_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("improved_Portrait_of_a_Young_Woman.tif",img_filtered)






