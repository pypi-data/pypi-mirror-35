import sys
if 'np' not in sys.modules: import numpy as np
if 'tf' not in sys.modules: import tensorflow as tf

from .base import Base
from ..utils.decode import decode_bstring_array
from ..utils.utils import default_channel_names
from ..utils.types import tf_encoded_type, tf_type_string
from ..utils.features import unwrap_features

class Recon(Base):

    def reconstruct(self, features):
        features = features if type(features) is dict else {**features[0], **features[1]}
        features = {
            fname: self.reconstruct_feature(features, fname, fdata)
            for fname, fdata in self.schema.items()
        }
        if self.etype == 'sequence_example':
            return self.split_features(features)
        return features


    # TODO  cleanup logic


    def reconstruct_feature(self, features, fname, fdata):
        finfo = self.schema[fname]
        dtype = finfo['dtype']

        etype = self.etype
        if fname in self.context_features: etype = 'example'

        if 'string' in tf_type_string(dtype):
            features[fname] = decode_bstring_array(features[fname])

        if finfo['encode'] is None or etype == 'sequence_example':
            # sequence_examples encodes channels as unnamed features
            return features[fname]
        return self.reconstruct_channels(features, fname, finfo)

    def reconstruct_channels(self, features, fname, finfo):

        # shorter variable names
        data_format   = finfo['data_format']
        dtype         = finfo['dtype']
        encode        = finfo['encode']
        channel_names = finfo['channel_names']
        if channel_names is None: channel_names = default_channel_names(finfo['shape'], data_format)

        se_dtype = tf_type_string(tf_encoded_type(dtype, encode))
        s_dtype  = tf_type_string(dtype)
        # if encoded as string but specified as not a string, decode
        if ('string' in se_dtype and 'string' not in s_dtype) or 'string' in encode:
            for channel in channel_names:
                features[channel] = tf.decode_raw(features[channel], dtype)

        joined = np.array([features[channel] for channel in channel_names], dtype=s_dtype)
        return joined

    def reconstitute(self, features, reconstruct_q=True, unwrap_q=True):
        if reconstruct_q:
            features = self.reconstruct(features)
        if unwrap_q:
            if self.etype == 'example':
                features = unwrap_features(features)
            else:
                features = (unwrap_features(features[0]), unwrap_features(features[1]))
        return features
