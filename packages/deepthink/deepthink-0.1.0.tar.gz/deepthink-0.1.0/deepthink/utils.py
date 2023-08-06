import os

import numpy as np
from sklearn.datasets import fetch_openml


def initialize_weights(shape, init_type, dtype=np.float32):
    """
    Return initialized weights for a trainable layer.

    Weights can either be implemented using Glorot or He initialization
    and can be either uniform or normal distribution.

    Parameters
    ----------
    shape : tuple
        The dimensions of the weights.
    init_type : str
        The initialization type to use.
    dtype : type
        The data-type to use, float32 by default.

    Returns
    -------
    np.array
        A Numpy array of weights

    References
    ----------
    - https://arxiv.org/pdf/1502.01852.pdf (He/Kaiming)
    - http://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf (Glorot/Xavier)
    - https://keras.io/api/layers/initializers/
    """
    # Ensure fan_in and fan_out are scalar values
    if len(shape) == 2:
        # Dense layer
        fan_in, fan_out = shape
    else:
        # Convolutional kernels, shape:
        # (depth-out, depth-in, kernel, kernel)
        receptive_field = np.prod(shape[2:])
        fan_in = shape[1] * receptive_field
        fan_out = shape[0] * receptive_field

    if init_type == 'glorot_normal':
        stddev = np.sqrt(2.0 / (fan_in + fan_out))
        return np.random.randn(*shape).astype(np.float32) * stddev
    elif init_type == 'glorot_uniform':
        limit = np.sqrt(6.0 / (fan_in + fan_out))
        return np.random.uniform(limit, -limit, size=shape).astype(dtype)
    elif init_type == 'he_normal':
        stddev = np.sqrt(2.0 / fan_in)
        return np.random.randn(*shape).astype(np.float32) * stddev
    elif init_type == 'he_uniform':
        limit = np.sqrt(6.0 / fan_in)
        return np.random.uniform(limit, -limit, size=shape).astype(dtype)
    else:
        raise Exception(f'Weight init type "{init_type}" not recognized')


def one_hot_encode(arr,  k, dtype=np.float32):
    """
    Takes 1D array of target integer values and return a
    one-hot-encoded 2D array.

    Parameters
    ----------
    arr : np.array
        The 1D array to encode
    k : int
        The number of target classes
    dtype : type,default=np.float32
        The data-type to use

    Returns
    -------
    np.array
        The one-hot-encoded array
    """
    return np.eye(k, dtype=dtype)[arr]


def load_mnist_data(test_split=60000, filepath='Data/mist784.npy',
                    shuffle=True, flat_data=False):
    """
    A function to load and prepare the MNIST dataset.

    The data is split into 60k training & 10k testing samples by
    default. Data values are normalized to range 0 to 1. Labels are
    one-hot-encoded.

    If the dataset has not been downloaded already it will use
    sklearn's fetch_openml to save it. Subsequent calls will then load
    the local version.

    Parameters
    ----------
    test_split : int
        The number of training samples, everything after this
        returned as test samples.
    filepath : str,default='../Data/mist784.npy'
        The file-path of the MNIST dataset. If this does not exist
        it will download and save it.
    shuffle : bool,default=True
        Used to shuffle training data, True by default.
    flat_data : bool,default=False
        When set to True images are represented by 1D arrays of length
        784, when set to False images are reshaped to image dimensions:
        (1, 28, 28).

    Returns
    -------
    training_data : tuple
        A tuple of (X_train, y_train), both numpy arrays, for training
        X-data and labels.
    test_data : tuple
        A tuple of (X_test, y_test), both numpy arrays, for test X-data
        and labels.
    """
    if not os.path.exists(filepath):
        print('Downloading dataset...')
        dataset = fetch_openml('mnist_784')
        np.save(filepath, dataset)

    with open(filepath, 'rb') as f:
        X, y = np.load(f)

    X = X.astype(np.float32)
    # Preprocess data, normalize images 0-1
    X /= 255.0
    # One-hot encode labels
    y_new = one_hot_encode(y.astype(np.int8), k=10)
    # Split data into training and testing
    X_train, y_train = X[:test_split], y_new[:test_split]
    X_test, y_test = X[test_split:], y_new[test_split:]
    if shuffle:
        # Shuffle training data
        shuffle_index = np.random.permutation(test_split)
        X_train, y_train = X_train[shuffle_index], y_train[shuffle_index]
    if not flat_data:
        # Reshape from 1D to image dimensions
        X_train = X_train.reshape(-1, 1, 28, 28)
        X_test = X_test.reshape(-1, 1, 28, 28)

    training_data = (X_train, y_train)
    test_data = (X_test, y_test)
    return training_data, test_data
