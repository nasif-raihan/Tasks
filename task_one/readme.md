# MNIST Digit Recognition using Convolutional Neural Network (CNN)

This Python script demonstrates building and training a Convolutional Neural Network (CNN) using TensorFlow and Keras to recognize handwritten digits from the MNIST dataset. The MNIST dataset is a collection of 28x28 pixel grayscale images of handwritten digits from 0 to 9.

## Model Architecture

The CNN model consists of the following layers:

1. **Input Layer:** Accepts images with the shape (28, 28, 1).
2. **Convolutional Layer (Conv2D):** Applies 32 filters with a kernel size of (3, 3) and ReLU activation.
3. **MaxPooling Layer:** Performs max pooling with a pool size of (2, 2).
4. **Convolutional Layer (Conv2D):** Applies 64 filters with a kernel size of (3, 3) and ReLU activation.
5. **MaxPooling Layer:** Performs max pooling with a pool size of (2, 2).
6. **Flatten Layer:** Converts the 2D matrix data to a vector for the fully connected layers.
7. **Dropout Layer:** Applies dropout regularization with a rate of 0.5 to reduce overfitting.
8. **Dense Layer (Fully Connected):** Produces output with the number of classes (num_classes=10) using softmax activation.

## Data Preprocessing

1. Load the MNIST dataset using `keras.datasets.mnist.load_data()`.
2. Scale the pixel values to the range [0, 1] by dividing by 255.
3. Expand the dimensions of the images to include the channel dimension (shape (28, 28, 1)).
4. Convert the class labels to binary class matrices using one-hot encoding.

## Training

1. Compile the model using categorical crossentropy loss, the Adam optimizer, and accuracy as the evaluation metric.
2. Train the model on the training data (`x_train`, `y_train`) with a batch size of 128 and 15 epochs, with 10% of the data used for validation.

## Evaluation

- Evaluate the trained model on the test data (`x_test`, `y_test`) to calculate the test loss and accuracy.

## How to Use

1. Run each block one after another maintaining serial wise.
2. Monitor the training progress, and view the final test accuracy and loss.

