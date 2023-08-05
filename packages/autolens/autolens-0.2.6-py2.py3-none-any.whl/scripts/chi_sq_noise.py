import sys
sys.path.append("../")

from autolens.analysis import fitting

import numpy as np

# Image 1 - lets pretend units are electrons per second

image = np.array([1.0])
noise = np.array([0.1])
model = np.array([0.5])

chi_sq_0 = fitting.chi_squared_term_from_chi_squareds(image=image, noise=noise, model=model)
noise_term_0 = fitting.noise_term_from_noise(noise)
likelihood_0 = fitting.likelihood_from_chi_squared_and_noise_terms(image=image, noise=noise, model=model)

# Image 2 - Same image_coords but electron counts (x 10000)

image = np.array([10000.0])
noise = np.array([1000.0])
model = np.array([5000.0])

chi_sq_1 = fitting.chi_squared_term_from_chi_squareds(image=image, noise=noise, model=model)
noise_term_1 = fitting.noise_term_from_noise(noise)
likelihood_1 = fitting.likelihood_from_chi_squared_and_noise_terms(image=image, noise=noise, model=model)

print('The likelihoods are different, due to the normalization terms')
print('(However, we only care about potential changes in likelihood)')
print()

print(chi_sq_0, chi_sq_1)
print(noise_term_0, noise_term_1)
print(likelihood_0, likelihood_1)


# Lets scale the noise in both images by x3, does the change in likelihood care about the image_coords units?

image = np.array([1.0])
noise = np.array([0.3])
model = np.array([0.5])

chi_sq_2 = fitting.chi_squared_term_from_chi_squareds(image=image, noise=noise, model=model)
noise_term_2 = fitting.noise_term_from_noise(noise)
likelihood_2 = fitting.likelihood_from_chi_squared_and_noise_terms(image=image, noise=noise, model=model)

image = np.array([10000.0])
noise = np.array([3000.0])
model = np.array([5000.0])

chi_sq_3 = fitting.chi_squared_term_from_chi_squareds(image=image, noise=noise, model=model)
noise_term_3 = fitting.noise_term_from_noise(noise)
likelihood_3 = fitting.likelihood_from_chi_squared_and_noise_terms(image=image, noise=noise, model=model)

print()
print('Likelihood normalizations different again')
print()
print(chi_sq_2)
print(noise_term_2)
print(chi_sq_2 + noise_term_2)

print(chi_sq_3)
print(noise_term_3)
print(chi_sq_3 + noise_term_3)

print()

print('Noise terms are on different scales...')
print(noise_term_1 - noise_term_0)
print(noise_term_3 - noise_term_2)
print(noise_term_0 - noise_term_2)
print(noise_term_1 - noise_term_3)
print()
print('But, magically, the change in likelihoods are identical (i.e. noise units dont impact likelihood scale)')
print((likelihood_0) - (likelihood_1))
print((likelihood_2) - (likelihood_3))
print((likelihood_0) - (likelihood_2))
print((likelihood_1) - (likelihood_3))