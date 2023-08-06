# DeepThink

DeepThink is a deep learning library for Python, designed as a learning project and as a resource for others looking to learn about deep learning. It provides a high-level interface for building, training, and evaluating deep learning models, as well as a range of utilities for working with data and optimizing models.

## Features

- A high-level API for defining, training, and evaluating models with minimal code
- Utilities for data loading, preprocessing, and model evaluation
- Tools for debugging, profiling, and optimizing models
- Extensive documentation and examples

Please note that DeepThink is a basic deep learning library and may not have the same level of performance or support for advanced features as other more established deep learning libraries.

## Installation

```
pip install deepthink
```

## Quickstart

Here is a simple example of how to use DeepThink to train a deep learning model:

```
from optimizers import Adam
from layers import Dense, Conv2D, MaxPooling, Flatten
from model import Model
from activations import ReLU,  Softmax
from utils import load_mnist_data
from loss import cce_cost_function

# Load dataset
training_data, test_data = load_mnist_data()

# Creating a model
optimizer = Adam(0.001)
model = Model(optimizer, cost=cce_cost_function, batch_size=64)

model.add_layer(Conv2D(kernel_size=5, n_filters=8,
                       input_shape=(64, 1, 28, 28)))
model.add_layer(ReLU())
model.add_layer(MaxPooling())
model.add_layer(Flatten())
model.add_layer(Dense(16))
model.add_layer(ReLU())
model.add_layer(Dense(10)
model.add_layer(Softmax())

model.initialize()

# Train the model
history = model.train(training_data, test_data, epochs=5)
```

For more information and examples, see the documentation.

## Contributing

We welcome contributions to DeepThink! If you would like to report a bug, request a feature, or contribute code, please see our contributing guidelines.

## License

DeepThink is released under the MIT License.