import torch
import torch.nn as nn


class Model(nn.Module):
    """Model class for linear regression using PyTorch.

    Args:
        nn: PyTorch module
    """

    def __init__(self, input_size, output_size):
        """Init the model with input and output size.
        Args:
            input_size (str): input features
            output_size (str): output features

        Example:
            model = Model(2, 3)
        """
        super().__init__()
        self.linear = nn.Linear(input_size, output_size)

    def forward(self, x):
        """Apply a linear transformation to the input data (x) and
        apply a sigmoid activation function. The sigmoid activation function
        maps any real value to a value between 0 and 1 (neccessary for calculating probabilities).
        Thereafter, the predicted probabilities are returned.

        sigmoid(x) = 1 / (1 + exp(-x))


        Args:
            x (PyTorch tensor): input data

        Returns:
            pred (PyTorch tensor): predicted probabilities for each data point in x
        """

        # pred: tensor with predicted probabilities for each data point in x.
        # pred = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1]
        pred = torch.sigmoid(self.linear(x))

        return pred

    def predict(self, x):
        """Predict the class label for the input data x using the forward method.
        If the predicted probability > 0.5, the class label is 1, otherwise 0.

        Args:
            x (PyTroch tensor): input data

        Returns:
            1, 0 (int): Returns the predicted class label (0 or 1)
        """

        pred = self.forward(x)

        if pred >= 0.5:
            return 1
        else:
            return 0
