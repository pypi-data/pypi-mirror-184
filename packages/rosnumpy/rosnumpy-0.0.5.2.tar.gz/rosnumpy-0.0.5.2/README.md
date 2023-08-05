# <div align="center">ros_numpy</div>

Note: This is the same as the original ros_numpy package by  [eric-wieser](https://github.com/eric-wieser) just edited to be OS independent and installable using pip.

## <div align="left">Install using:</div>
```
pip install rosnumpy
```

## <div align="center">Quick Start</div>
### PointCloud2 msg to Numpy array:
```Python
import ros_numpy
import sensor_msgs

def get_pc_from_ros_pc2_msg(msg):
    """ Returns point-cloud as a structured numpy array. 
    Note: can be used with any topic of message type 'sensor_msgs/PointCloud2'
    """
    msg.__class__ = sensor_msgs.msg.PointCloud2
    return ros_numpy.numpify(msg)

pc_array =  get_pc_from_pc2_msg(msg)
```

### Image msg to Numpy array:
```Python
import ros_numpy
import sensor_msgs

def get_img_from_ros_image_msg(msg):
    """ Returns image as a numpy array. 
    Note: can be used with any topic of message type 'sensor_msgs/Image'
    """
    msg.__class__ = sensor_msgs.msg.Image
    return ros_numpy.numpify(msg)

img_array =  get_img_from_ros_image_msg(msg)
```


