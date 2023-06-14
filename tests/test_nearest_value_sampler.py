from autora.experimentalist.sampler.nearest_value import nearest_values_sample
import numpy as np

def test_output_dimensions():
    #Meta-Setup
    X_allowed = np.linspace(-3, 6, 10)
    X = np.random.choice(X_allowed,10).reshape(-1, 1)
    n = 5
    
    #Sampler
    X_new = nearest_values_sample(X, X_allowed, n)

    # Check that the sampler returns n experiment conditions
    assert X_new.shape == (n, X.shape[1])