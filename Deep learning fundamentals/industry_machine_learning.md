
## Industry machine learning project

* Process and analyze datasets
* Create an efficient data pipeline for feeding input data into machine learning models
* Develop robust machine learning models for both classification and regression task
* Interpret model results with respect to the project domain


### Input pipeline

* The process in which data is loaded from files and fed into a machine learning model is known as the input pipeline.

* We recommend a flexible and efficient format for storing large amounts of data is Google's `protocol buffer`, and make the input pipeline for large datasets much more streamlined

### Loading data

* `tf.data` API provides us with all the tools necessary to create an efficient input pipeline, can process protocol buffers and numpy data


* `tf.train.Example` class represents the protocol buffer used to store data for the input pipeline.It convert raw data to a protocol buffer by initializing a `tf.train.Example` 

```
import tensorflow as tf

features = tf.train.Features(feature=f_dict)
ex = tf.train.Example(features=features)
```

* Feature is represented by `tf.train.Feature`

```
import tensorflow as tf
int_f = tf.train.Feature(
    int64_list=tf.train.Int64List(value=[1,2]))

float_f = tf.train.Feature(
    float_list=tf.train.FloatList(value=[-8.2, 5]))

bytes_f = tf.train.BytesList(value=[b'\xff\xcc', b'\xac'])

str_f = tf.train.Feature(
    bytes_list=tf.train.BytesList(value=['joe'.encode()]))

```


### TFRecords

* How to write serialized protocol buffers to TFRecords files
```
import tensorflow as tf
# protocol buffer
ex = tf.train.Example(features=tf.train.Features(feature=f_dict))

# then serialize the object
ser_ex = ex.SerializeToString()
```

* Implement a function that writes a list of feature data to a TFRecords file
```
import tensorflow as tf
writer = tf.python_io.TFRecordWriter('out.tfrecords')
writer.write(ser_ex)
write.close()

```

### Features

* Example spec

* VarLenFeature class

* FixedLenFeature class

```
import tensorflow as tf

name = tf.FixedLenFeature((), tf.string)
jobs = tf.VarLenFeature(tf.string)
salary = tf.FixedLenFeature(2, tf.int64, default_value=0)
example_spec = {
    'name': name,
    'jobs': jobs,
    'salary': salary
}

def make_feature_config(shape, tf_type, feature_config):
    if not shape:
        feature = tf.VarLenFeature(tf_type)
    else:
        default_value = tf.feature_config.get('default_value', None)
        feature = tf.FixedLenFeature(shape, tf_type, default_value)
    return feature

```

### Parsing



### Dataset

* `tf.data.Dataset.from_tensor_slices` to create a dataset from numpy to  `protocol buffers`.
* `tf.data.Dataset.from_tensor_slices` is not limited to just taking Numpy arrays as input, we can use it to create a dataset of file names.

```
import numpy as np
import tensorflow as tf

data = np.array([[1., 2.1],
    [2.,    3.],
    [8.1, -10.]
    ])

d1 = tf.data.Dataset.from_tensor_slices(data)

```

* Example 2

```
import numpy as np
import tensorflow as tf

filename = ['img1.jpg', 'img2.jpg']  # filename
img_d1 = tf.data.Dataset.from_tensor_slices(filenames)

labels = np.array([1, 0])
img_d2 = tf.data.Dataset.from_tensor_slices((filenames, labels))
print(img_d2)

```

* Specialized datasets by using `tf.data.TFRecordDataset` and `tf.data.TextLineDataset`
```
import numpy as np
import tensorflow as tf

records_file = ['one.tfrecords', 'two.tfrecords']
d1 = tf.data.TFRecordDataset(records_files)

txt_files = ['lines.txt']
d2 = tf.data.TextLineDataset(txt_files)
```

### Mapping 

* map a function onto each observation of a dataset

* Implement a function that create a dataset of serialized protocol buffers and parses each observation

```
import numpy as np
import tensorflow as tf

data1 = np.array([1.2, 2.2],
        [7.3, 0.])

data2 = np.array([0.1, 1.1])

d1 = tf.data.Dataset.from_tensor_slices((data1, data2))
d2 = d1.map(lambda x, y: x+y)  # take the tuple as argument

```

`epochs` means single training run over the entire dataset.

```
import numpy as np
import tensorflow as tf

data = np.random.uniform(-100, 100, (1000, 5))
original = tf.data.Dataset.from_tensor_slices(data)

batch1 = original.batch(1)
print(batch1)

batch2 = original.batch(2)
print(batch2)
```

### Dataset Iteration

* Learn how to iterate through a dataset and extract values from data observations

```
import numpy as np
import tensorflow as tf

data = np.array([[1., 2.],
        [3., 4.]])
dataset = tf.data.Dataset.from_tensor_slices(data)
dataset = dataset.batch(1)

it = dataset.make_one_shot_iterator()
next_elem = it.get_next()

added = next_elem + 1
```

### Feature columns

* a feature column is how we specify what kind of data contains. `numeric or categorical data`