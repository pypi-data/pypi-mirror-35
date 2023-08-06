# FIO

FIO is short for Feature I/O.

FIO is a concept stemming TensorFlow's low-level API. More specifically,
FIO is a concept of how to join the methods dealing with the protocol buffers
that write data to the TF.Record format and from the TF.Record format.


FIO works by defining your features __once__ in a "schema"


e.g. for "normal" features:
```
'my-features':     {'length': 'fixed', 'dtype': tf.string,  'shape': []}

```
and we are done. Make this a `tf.train.Example` or `tf.train.SequenceExample`,
write to a record, and read from it.

For rank 2 features:
```
'seq':         {
      'length': 'fixed',
      'dtype': tf.int64,
      'shape': [3, 3],
      'encode': 'channels',
      'channel_names': ['Channel 1', 'Channel 2', 'Channel 3'],
      'data_format': 'channels_last'
  }
```

and we are done again. I can now encode this as a `tf.train.Example` (with the
optional, but here provided channel names) or `tf.train.SequenceExample` without the names.

# Useful resources

## S.O.
[How to decompose tensors for TF.Record](https://stackoverflow.com/questions/52035692/tensorflow-v1-10-store-images-as-byte-strings-or-per-channel)
[How to recover TF Record data](https://stackoverflow.com/questions/52064866/tensorflow-1-10-tfrecorddataset-recovering-tfrecords)
## Colab
[Playing with Rank 2 Tensors and TF Records](https://colab.research.google.com/drive/1M10tbHih5eJ8LiApJSKKpNM79IconYJX)
[Recovering TF Records](https://colab.research.google.com/drive/1HUGoXfgxp0A_0eSdaCzutOkFvnYZ-egv)

# Motivation

Disclaimer: I am not familiar with the intricacies of TF, Protocol Buffers, and the like. So my motivation here may actually not make sense to the experts who actually designed this for TF. From my uninformed view, I find parts of this interface cumbersome and lacking documentation and FIO is as much as an over-engineered solution to my specific problem (getting some data in and out of TF Records) as it is an exploration of what works regarding TF Records.

## "Duplicate code"
Consider the exceptionally trivial data of writing and reading:
```
my_feature = 'hi'
```
from a TF.Record.


### Example
To get this feature into a record we must first wrap this data as follows:

```
example = tf.train.Example(
  features=tf.train.Features(
      feature={
      'my-feature': tf.train.Feature(
        bytes_list=tf.train.BytesList(
          value=[my_feature.encode()] # wrap as list
        ) # end byteslist
      ) # end feature
    }
  ) # end features
) # end example
```
which returns:


```
features {
  feature {
    key: "my-feature"
    value {
      bytes_list {
        value: "hi"
      }
    }
  }
}
```

and we can write this to a record with:

```
with tf.python_io.TFRecordWriter('my_record.tfrecord') as writer:
    writer.write(example.SerializeToString())
```

and we can retrieve it from this file with:

```
DATASET_FILENAMES = tf.placeholder(tf.string, shape=[None])
dataset = tf.data.TFRecordDataset(DATASET_FILENAMES).map(lambda r: parse_fn(r)).repeat().batch(1)
iterator = dataset.make_initializable_iterator()
next_element = iterator.get_next()

for _ in range(1): # epochs
    sess.run(iterator.initializer, feed_dict={DATASET_FILENAMES: ['my_record.tfrecord']})
    for _ in range(1): # batch
        recovered = sess.run(next_element)
```


Now it is very important to note that:
1. the above code is a bit more sophisticated than the base example needed (given the iterator), which I will not go into detail here about,

2. the above code will not run because `parse_fn` is not defined

Since we are using a TF Example, I will demonstrate how we can simply read the example to get the data back:


```
def parse_fn(record):
    features = {
        'my-feature': tf.FixedLenFeature([], dtype=tf.string)
    }
    parsed = tf.parse_single_example(record, features)
    # other things can be done if needed
    return parsed
```

now running the above code yields:


```
{'my-feature': array([b'hi'], dtype=object)}
```

So if we want to get back to `{'my-feature': 'hi'}` we still need to unwrap the list and decode the string:

```
recovered['my-feature'] = recovered['my-feature'][0].decode()
```

Note: this can not be done in the parsing function (at least as I have done here).  

### What I would like to solve
The point of showing all of this, is that if so much care goes into converting our data for TF.Records, why must I then also write similar code to extract it out?

A goal of FIO is to define a singular schema which gets data both into a TF Record and can recover it (as we put it in).

## De/re-composing tensors:
I will touch on the difference between `tf.train.Example` and `tf.train.SequenceExample` in the next section. Regardless of which you choose to use, any tensor of rank 2 or greater must be decomposed.

For simplicity consider the sequence:

```
seq = [
    # el1, el2, el3
    [   1,   1,  1], # channel 1
    [   2,   2,  2], # channel 2
    [   3,   3,  3], # channel 3
]
```

Both `tf.train.Example` and `tf.train.SequenceExample` require `seq` to be decomposed by channel:

either as:

```
# for tf.train.Example
tf.train.Features(
    feature={
    'channel 1': tf.train.Feature(int64_list=tf.train.Int64List(value=seq[0])),
    'channel 2': tf.train.Feature(int64_list=tf.train.Int64List(value=seq[1])),
    'channel 3': tf.train.Feature(int64_list=tf.train.Int64List(value=seq[2]))
  }
)
```

or as:

```
tf.train.FeatureLists(feature_list=
  tf.train.FeatureList(
    feature=[
      tf.train.Feature(int64_list=tf.train.Int64List(value=seq[i]))
      for i in range(number_of_channels(seq))
    ]
  )
)
```

The difference here being that for `SequenceExample`, the channels are unnamed features. For many channels, this is advantageous as one needs not worry about reassembling the sequence from all the channels. However, if one has only a few channels (e.g. rgb), then one could - prior to feeding into the model - rearrange the channels, or if there are multiple-inputs, this may be of use.

Either-way, FIO aims to handle this part, both for decomposing tensors and recomposing them (in the case of the `Example`).

## Singular interface
As mentioned above, a core distinction between `Example` and `SequenceExample` is whether or not each feature is named. However, there is one other core distinction: `SequenceExample` is a tuple. Rather, I should say, `SequenceExample` allows one to store "context" (metadata), where the context are features that adhere to all the restrictions of those for an `Example`.

The example given in the docs is that the context might be the same across sequences, but the large sequences may vary. Thus it saves space.

I admit, while that sound like a structure, I do not understand how to utilize that in practice. A `SequenceExample` _requires_ a context (although it can be just an empty `dict`). Thus if one is storing examples individually, they would most likely store the context in each record. Furthermore, given my current understanding, only sequence features can be stored in the `feature_lists` part of `SequenceExample`.

From my uninformed perspective, it might have been nicer to just maintain a single `Example` interface, and then using something like (the imaginary) `tf.train.SequenceFeature` allow everything to be stored together. Better yet, `tf.train.TensorFeature` might solve a lot of issues.


Anyway, FIO aims to be a singular interface for handling `Example` and `SequenceExample`, making it easy to decompose tensors to (un)named features and export / import correspondingly.

## Decomposing techniques

There are many ways to decompose a Tensor into its channels. I will only consider some of the possibilities for the aforementioned `seq`:

- separate each channel of `seq` and store as corresponding numeric type, name and store in `Example`
- separate each channel of `seq`, and store as bytes after converting via  `numpy.ndarray.tostring()`, name and store in `Example`
- separate each channel of `seq`, and convert each element to bytes, and then store as a `BytesList`, name and store in `Example`
- store altogether by dumping `seq` to bytes via `numpy.ndarray.tostring()`, name and store in `Example`
- separate each channel of `seq` and store as corresponding numeric type, leave unnamed and store in `SequenceExample`
- separate each channel of `seq`, and store as bytes after converting via  `numpy.ndarray.tostring()`, leave unnamed and store in `SequenceExample`
- separate each channel of `seq`, and convert each element to bytes, and then store as a `BytesList`, leave unnamed and store in `SequenceExample`
- store altogether by dumping `seq` to bytes via `numpy.ndarray.tostring()` and wrap as a single element bytes list.

Which one of these is best? No idea.
Maybe TF encoded `Float` and `Int64` `Features` to bytes behind the scene.

I will note that sometimes when trying to recover the data, if encoded as bytes, then the tensor is flattened. e.g. `[[1,2],[3,4]]` is restored as `[1,2,3,4]`.

Anyway, FIO aims to allow for tensors to be encoded and decoded via some of these methods, as I honestly do not know which is best (in terms of file size, read efficiency, etc).

Again, I think TF could do this better via a `tf.train.TensorFeature`

p.s. if anyone knows why how to encoded features are under `tf.train` (e.g. `tf.train.Feature(int64_list=tf.train.Int64List(value=value))`) and how to decoded features are just under `tf` (e.g. `tf.FixedLenFeature`) I would like to know. This seems odd to me...


