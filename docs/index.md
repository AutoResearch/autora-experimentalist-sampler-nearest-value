# Nearest Value Sampler

A sampler which returns the nearest values between the input samples and the allowed values, without replacement.

# Example Code

```
from autora.experimentalist.sampler.nearest_value import nearest_values_sample
import numpy as np

#Meta-Setup
X_allowed = np.linspace(-3, 6, 10)
X = np.random.choice(X_allowed,10)
n = 5

#Sampler
X_new = nearest_values_sample(X, X_allowed, n)
```
