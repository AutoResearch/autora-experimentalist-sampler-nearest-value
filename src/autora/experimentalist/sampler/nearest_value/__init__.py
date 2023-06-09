from typing import Iterable, Sequence, Union
import numpy as np

from autora.utils.deprecation import deprecated_alias


def nearest_values_sample(
    samples: Union[Iterable, Sequence],
    allowed_values: np.ndarray,
    num_samples: int,
):
    """
    A sampler which returns the nearest values between the input samples and the allowed values,
    without replacement.

    Args:
        samples: input conditions
        allowed_values: allowed conditions to sample from
        num_samples: number of samples

    Returns:
        the nearest values from `allowed_samples` to the `samples`

    """

    if isinstance(allowed_values, Iterable):
        allowed_values = np.array(list(allowed_values))

    if len(allowed_values.shape) == 1:
        allowed_values = allowed_values.reshape(-1, 1)

    if isinstance(samples, Iterable):
        samples = np.array(list(samples))

    if allowed_values.shape[0] < num_samples:
        raise Exception(
            "More samples requested than samples available in the set allowed of values."
        )

    if isinstance(samples, Iterable) or isinstance(samples, Sequence):
        samples = np.array(list(samples))

    if hasattr(samples, "shape"):
        if samples.shape[0] < num_samples:
            raise Exception(
                "More samples requested than samples available in the pool."
            )

    x_new = np.empty((num_samples, allowed_values.shape[1]))

    # get index of row in x that is closest to each sample
    for row, sample in enumerate(samples):

        if row >= num_samples:
            break

        dist = np.linalg.norm(allowed_values - sample, axis=1)
        idx = np.argmin(dist)
        x_new[row, :] = allowed_values[idx, :]
        allowed_values = np.delete(allowed_values, idx, axis=0)

    return x_new

nearest_values_sampler = deprecated_alias(nearest_values_sample, "nearest_values_sampler")
