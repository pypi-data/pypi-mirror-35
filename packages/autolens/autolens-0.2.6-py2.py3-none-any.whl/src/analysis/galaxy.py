import numpy as np
from autolens.profiles import light_profiles as lps, mass_profiles as mps
from itertools import count


def is_light_profile(obj):
    return isinstance(obj, lps.LightProfile) and not isinstance(obj, mps.MassProfile)


def is_mass_profile(obj):
    return isinstance(obj, mps.MassProfile)


class Galaxy(object):
    """
    @DynamicAttrs
    """

    def __init__(self, redshift=None, pixelization=None, hyper_galaxy=None, **kwargs):
        """
        Represents a real galaxy. This could be a lens galaxy or source galaxy. Note that a lens galaxy must have mass
        profiles

        Parameters
        ----------
        redshift: float
            The redshift of this galaxy
        light_profiles: [LightProfile]
            A list of light profiles describing the light profiles of this galaxy
        mass_profiles: [MassProfile]
            A list of mass profiles describing the mass profiles of this galaxy
        """
        self.redshift = redshift

        for name, val in kwargs.items():
            setattr(self, name, val)

        self.pixelization = pixelization
        self.hyper_galaxy = hyper_galaxy

    @property
    def light_profiles(self):
        return [value for value in self.__dict__.values() if is_light_profile(value)]

    @property
    def mass_profiles(self):
        return [value for value in self.__dict__.values() if is_mass_profile(value)]

    @property
    def has_pixelization(self):
        """
        Returns
        -------
        True iff this galaxy has an associated pixelization
        """
        return self.pixelization is not None

    @property
    def has_hyper_galaxy(self):
        """
        Returns
        -------
        True iff this galaxy has an associated hyper galaxy
        """
        return self.hyper_galaxy is not None

    @property
    def has_profile(self):
        """
        Returns
        -------
        True iff there is one or more mass or light profiles associated with this galaxy
        """
        return len(self.mass_profiles) + len(self.light_profiles) > 0

    def __repr__(self):
        string = "Redshift: {}".format(self.redshift)
        if self.pixelization:
            string += str(self.pixelization)
        if self.hyper_galaxy:
            string += str(self.hyper_galaxy)
        if self.light_profiles:
            string += "\nLight Profiles:\n{}".format("\n".join(map(str, self.light_profiles)))
        if self.mass_profiles:
            string += "\nMass Profiles:\n{}".format("\n".join(map(str, self.mass_profiles)))
        return string

    def intensity_from_grid(self, grid):
        if self.light_profiles is not None and len(self.light_profiles) > 0:
            return sum(map(lambda p: p.intensity_from_grid(grid), self.light_profiles))
        else:
            return np.zeros((grid.shape[0],))

    def intensity_from_grid_individual(self, grid):
        """
        Compute the individual intensities of the galaxy's light profiles at a given set of image_grid.

        See *light_profiles* module for details of how this is performed.

        Parameters
        ----------
        grid : ndarray
            The image_grid in image_grid space
        Returns
        -------
        intensity : [float]
            The summed values of intensity at the given image_grid
        """
        return list(map(lambda p: p.intensity_from_grid(grid), self.light_profiles))

    def luminosity_within_circle(self, radius):
        """
        Compute the total luminosity of the galaxy's light profiles within a circle of specified radius.

        See *light_profiles.luminosity_within_circle* for details of how this is performed.

        Parameters
        ----------
        radius : float
            The radius of the circle to compute the luminosity within.

        Returns
        -------
        luminosity : float
            The total combined luminosity within the specified circle.
        """
        return sum(map(lambda p: p.luminosity_within_circle(radius), self.light_profiles))

    def luminosity_within_circle_individual(self, radius):
        """
        Compute the individual total luminosity of each light profile in the galaxy, within a circle of
        specified radius.

        See *light_profiles.luminosity_within_circle* for details of how this is performed.

        Parameters
        ----------
        radius : float
            The radius of the circle to compute the luminosity within.

        Returns
        -------
        luminosity : [float]
            The total combined luminosity within the specified circle.
        """
        return list(map(lambda p: p.luminosity_within_circle(radius), self.light_profiles))

    def luminosity_within_ellipse(self, major_axis):
        """
        Compute the total luminosity of the galaxy's light profiles, within an ellipse of specified major axis. This 
        is performed via integration of each light profile and is centred, oriented and  aligned with each light 
        model_mapper's individual geometry.

        See *light_profiles.luminosity_within_ellipse* for details of how this is performed.

        Parameters
        ----------
        major_axis: float
            The major-axis of the ellipse to compute the luminosity within.
        Returns
        -------
        intensity : float
            The total luminosity within the specified ellipse.
        """
        return sum(map(lambda p: p.luminosity_within_ellipse(major_axis), self.light_profiles))

    def luminosity_within_ellipse_individual(self, major_axis):
        """
        Compute the individual total luminosity of each light profile in the galaxy, within an ellipse of 
        specified major axis.

        See *light_profiles.luminosity_within_ellipse* for details of how this is performed.

        Parameters
        ----------
        major_axis: float
            The major-axis of the ellipse to compute the luminosity within.
        Returns
        -------
        intensity : [float]
            The total luminosity within the specified ellipse.
        """
        return list(map(lambda p: p.luminosity_within_ellipse(major_axis), self.light_profiles))

    def surface_density_from_grid(self, grid):
        """

        Compute the summed surface density of the galaxy's mass profiles at a given set of image_grid.

        See *mass_profiles* module for details of how this is performed.

        Parameters
        ----------
        grid : ndarray
            The x and y image_grid of the image_grid

        Returns
        ----------
        The summed values of surface density at the given image_grid.
        """
        return sum(map(lambda p: p.surface_density_from_grid(grid), self.mass_profiles))

    def surface_density_from_grid_individual(self, grid):
        """

        Compute the individual surface densities of the galaxy's mass profiles at a given set of image_grid.

        See *mass_profiles* module for details of how this is performed.

        Parameters
        ----------
        grid : (float, float)
            The x and y image_grid of the image_grid

        Returns
        ----------
        The summed values of surface density at the given image_grid.
        """
        return list(map(lambda p: p.surface_density_from_grid(grid), self.mass_profiles))

    def potential_from_grid(self, grid):
        """
        Compute the summed gravitational potential of the galaxy's mass profiles at a given set of image_grid.

        See *mass_profiles* module for details of how this is performed.

        Parameters
        ----------
        grid : ndarray
            The x and y image_grid of the image_grid

        Returns
        ----------
        The summed values of gravitational potential at the given image_grid.
        """
        return sum(map(lambda p: p.potential_from_grid(grid), self.mass_profiles))

    def potential_from_grid_individual(self, grid):
        """
        Compute the individual gravitational potentials of the galaxy's mass profiles at a given set of image_grid.

        See *mass_profiles* module for details of how this is performed.

        Parameters
        ----------
        grid : Union(ndarray, (float, float))
            The x and y image_grid of the image_grid

        Returns
        ----------
        The summed values of gravitational potential at the given image_grid.
        """
        return list(map(lambda p: p.potential_from_grid(grid), self.mass_profiles))

    def deflections_from_grid(self, grid):
        if self.mass_profiles is not None and len(self.mass_profiles) > 0:

            deflections = sum(map(lambda p: p.deflections_from_grid(grid), self.mass_profiles))

            # return sum(map(lambda p: p.deflections_from_coordinate_grid(grid), self.mass_profiles))
            return deflections
        else:
            return np.full((grid.shape[0], 2), 0.0)

    def deflections_from_grid_individual(self, grid):
        """
        Compute the individual deflection angles of the galaxy's mass profiles at a given set of image_grid.

        See *mass_profiles* module for details of how this is performed.

        Parameters
        ----------
        grid : Union(np.ndarray, (float, float))
            The x and y image_grid of the image_grid

        Returns
        ----------
        The summed values of deflection angles at the given image_grid.
        """
        return np.asarray(list(map(lambda p: p.deflections_from_grid(grid), self.mass_profiles)))

    def dimensionless_mass_within_circles(self, radius):
        """
        Compute the total dimensionless mass of the galaxy's mass profiles within a circle of specified radius.

        See *mass_profiles.dimensionless_mass_within_circles* for details of how this is performed.


        Parameters
        ----------
        radius : float
            The radius of the circle to compute the dimensionless mass within.

        Returns
        -------
        dimensionless_mass : float
            The total dimensionless mass within the specified circle.
        """
        return sum(map(lambda p: p.dimensionless_mass_within_circle(radius), self.mass_profiles))

    def dimensionless_mass_within_circles_individual(self, radius):
        """
        Compute the individual dimensionless mass of the galaxy's mass profiles within a circle of specified radius.

        See *mass_profiles.dimensionless_mass_within_circles* for details of how this is performed.

        Parameters
        ----------
        radius : float
            The radius of the circle to compute the dimensionless mass within.

        Returns
        -------
        dimensionless_mass : ndarray
            The total dimensionless mass within the specified circle.
        """
        return np.asarray(list(map(lambda p: p.dimensionless_mass_within_circle(radius), self.mass_profiles)))

    def dimensionless_mass_within_ellipses(self, major_axis):
        """
        Compute the total dimensionless mass of the galaxy's mass profiles within an ellipse of specified major_axis.

        See *mass_profiles.dimensionless_mass_within_ellipses* for details of how this is performed.


        Parameters
        ----------
        major_axis : float
            The major axis of the ellipse

        Returns
        -------
        dimensionless_mass : float
            The total dimensionless mass within the specified circle.
        """
        return sum(map(lambda p: p.dimensionless_mass_within_ellipse(major_axis), self.mass_profiles))

    def dimensionless_mass_within_ellipses_individual(self, major_axis):
        """
        Compute the individual dimensionless mass of the galaxy's mass profiles within an ellipse of specified 
        major-axis.

        See *mass_profiles.dimensionless_mass_within_circles* for details of how this is performed.

        Parameters
        ----------
        major_axis : float
            The major axis of the ellipse

        Returns
        -------
        dimensionless_mass : ndarray
            The total dimensionless mass within the specified circle.
        """
        return list(map(lambda p: p.dimensionless_mass_within_ellipse(major_axis), self.mass_profiles))


# TODO : Should galaxy image and minimum value be in the constructor (they aren't free parameters)?

class HyperGalaxy(object):
    _ids = count()

    def __init__(self, contribution_factor=0.0, noise_factor=0.0, noise_power=1.0):
        """Class for scaling the noise in the different galaxies of an image (e.g. the lens, source).

        Parameters
        -----------
        contribution_factor : float
            Factor that adjusts how much of the galaxy's light is attributed to the contribution map.
        noise_factor : float
            Factor by which the noise is increased in the regions of the galaxy's contribution map.
        noise_power : float
            The power to which the contribution map is raised when scaling the noise.
        """
        self.contribution_factor = contribution_factor
        self.noise_factor = noise_factor
        self.noise_power = noise_power

        self.component_number = next(self._ids)

    @property
    def subscript(self):
        return 'hg'

    @property
    def parameter_labels(self):
        return [r'\Omega', r'\omega1', r'\omega2']

    def contributions_from_model_images(self, model_image, galaxy_image, minimum_value):
        """Compute the contribution map of a galaxy, which represents the fraction of flux in each pixel that \
        galaxy can be attributed to contain.

        This is computed by dividing that galaxy's flux by the total flux in that pixel, and then scaling by the \
        maximum flux such that the contribution map ranges between 0 and 1.

        Parameters
        -----------
        model_image : ndarray
            The model image of the observed weighted_data (from a previous analysis phase). This tells us the total light \
            attributed to each image pixel by the model.
        galaxy_image : ndarray
            A model image of the galaxy (e.g the lens light profile or source reconstruction) computed from a
            previous analysis.
        minimum_value : float
            The minimum fractional flux a pixel must contain to not be rounded to 0.
        """
        contributions = galaxy_image / (model_image + self.contribution_factor)
        contributions = contributions / np.max(contributions)
        contributions[contributions < minimum_value] = 0.0
        return contributions

    def scaled_noise_for_contributions(self, noise, contributions):
        """Compute a scaled galaxy noise map from a baseline nosie map.

        This uses the galaxy contribution map with their noise scaling hyper-parameters.

        Parameters
        -----------
        noise : ndarray
            The noise before scaling (this may already have the background scaled in HyperImage)
        contributions : ndarray
            The galaxy contribution map.
        """
        return self.noise_factor * (noise * contributions) ** self.noise_power

    def __eq__(self, other):
        if isinstance(other, HyperGalaxy):
            return self.contribution_factor == other.contribution_factor and \
                   self.noise_factor == other.noise_factor and \
                   self.noise_power == other.noise_power
        return False

    def __str__(self):
        return "\n".join(["{}: {}".format(k, v) for k, v in self.__dict__.items()])


class Redshift(object):
    def __init__(self, redshift):
        self.redshift = redshift

    def __str__(self):
        return str(self.redshift)

    @property
    def parameter_labels(self):
        return 'z'

    @property
    def subscript(self):
        return 'g'
