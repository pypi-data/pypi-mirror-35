These tools are to provide effort by researchers in creating their own working environment
This is about dealing with {ICDAR} data
It provides you with initial processing tools for training and testing data.
It provides tools for calculating the text area using polygon of shapely.
Save results from images and text locations as a prelude to calculating precision.
And some other tools we will try to "more examples to explain the use later."

These tools have been quoted and written by the {EAST}.
Where you can see the original files here.
https://github.com/argman/EAST/

These tools depend on several libraries you must provide before use.
Like:
```
-opencv-3.x.x
-numpy
-scipy
-matplotlib
-shapely
```

use Modules!

```python
import icdar_tools
```
or 
```python
from icdar_tools import icdar
from icdar_tools import icd_util
from icdar_tools import locality_aware_nms
from icdar_tools import data_util
```

 - icdar.py

This module is very important as it is found to serve your time instead of betting a lot of effort and time in order to produce already existing tools, in order to handle the data.
Here you will find everything you need, from the future ICDAR Data Processing

From loading the data and locating the texts inside the images and some other things.
The following are examples of usage.

1:get_batch()
```python
get_batch(num_workers, **kwargs)
```
The function works to get the coordinates of the text in the images
Through text files with them in the same path
It then returns those geometrical coordinates,
image names, and images derived from the training images specified by the place of the text only.

use:

```python
data_generator = icdar.get_batch(num_workers=num_readers,
                                         training_data_path='path/to_data/icdar15/train/'
                                         input_size=input_size,
                                         batch_size=batch_size_per_gpu * len(gpus))
```

reutrn
```python
yield images, image_fns, score_maps, geo_maps, training_masks
```

2:load_annoataion()

```python
text_polys, text_tags = icdar.load_annoataion(txt_file-name)
```

   
3:restore_rectangle_rbox()
```python
text_box_restored = icdar.restore_rectangle_rbox(origin, geometry)
```
   
   
**:**
 - icd_util.py
 
 
1 - get_images()
The input path should be images
```python
images_list_fullName = icd_util.get_images(path/data/images/)
```
Repetition is a list of all images in the input path

   
   
2 -resize_image()

```python
im_resized, (ratio_h, ratio_w) = icd_util.resize_image(image)
```
    '''
    resize image to a size multiple of 32 which is required by the network
    :param im: the resized image
    :param max_side_len: limit of max image size to avoid out of memory in gpu
    :return: the resized image and the resize ratio
    '''
 - The default setting of the function
   ```python
   icd_util.resize_image(image, max_side_len=2400)
   ```

3 - detect() \
Here is the conclusion of the model represented in the geometrical map of coordinates and score

Use the threshold to filter the results that look false
The borders of the text boxes are then redrawn

return of these boxes and the time of implementation of this processe.

```python
boxes, timer = icd_util.detect(score_map=score, geo_map=geometry, timer=timer)
```

    '''
    restore text boxes from score map and geo map
    :param score_map:
    :param geo_map:
    :param timer:
    :param score_map_thresh: threshhold for score map
    :param box_thresh: threshhold for boxes
    :param nms_thres: threshold for nms
    :return: boxes and time out
    '''
    
    - The default setting of the function
    
   ```python
   icd_util.detect(score_map, geo_map, timer, score_map_thresh=0.8, box_thresh=0.1, nms_thres=0.2):
   ```
   
- write_result() \
This function gets the image and its name \
The file name is written as the text location in the image 

You get the text boxes that are expected for that image \
writeing text locations in text files \
drawing squares around those texts in the picture \
See the font size of the box and font color through passes 
```
color, thickness
```
Finally a place will be written  those 'output_path/'

Images and text files are written into a single folder.

```python
   icd_util.write_result(img ,boxes ,output_dir ,res_file ,img_fn)
```
   
 - The default setting of the function
 ```python
   icd_util.write_result(img ,boxes ,output_dir ,res_file ,img_fn ,color=(255, 255, 0),thickness=1, skip = True)
 ```
 
...
