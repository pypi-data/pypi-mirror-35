from autolens.pipeline import pipeline as pl
from autolens.imaging import image as im
from autolens.imaging import scaled_array
from autolens.autopipe import non_linear as nl
import shutil

import os

dirpath = os.path.dirname(os.path.realpath(__file__))


def load_image(name):

    data_dir = "{}/../../data/{}".format(dirpath, name)

    data = scaled_array.ScaledArray.from_fits(file_path=data_dir + '/masked_image', hdu=0, pixel_scale=0.05)
    noise = scaled_array.ScaledArray.from_fits(file_path=data_dir + '/noise', hdu=0, pixel_scale=0.05)
    psf = im.PSF.from_fits(file_path=data_dir + '/psf', hdu=0)

    return im.Image(array=data, pixel_scale=0.05, psf=psf, noise=noise)


def test_profile_pipeline():
    name = "test_pipeline"
    try:
        shutil.rmtree("{}/../../output/{}".format(dirpath, name))
    except FileNotFoundError:
        pass
    pipeline = make_profile_pipeline(name, optimizer_class=nl.DownhillSimplex)
    results = pipeline.run(load_image("integration/hst_0"))
    for result in results:
        print(result)


def make_profile_pipeline(name="profile", optimizer_class=None):
    from autolens.pipeline import phase as ph
    from autolens.autopipe import non_linear as nl
    from autolens.analysis import galaxy_prior as gp
    from autolens.imaging import mask as msk
    from autolens.profiles import light_profiles, mass_profiles

    if optimizer_class is None:
        optimizer_class = nl.MultiNest

    # 1) Lens Light : EllipticalSersic
    #    Mass: None
    #    Source: None
    #    NLO: MultiNest
    #    Image : Observed Image
    #    Mask : Circle - 3.0"

    phase1 = ph.LensOnlyPhase(lens_galaxy=gp.GalaxyPrior(elliptical_sersic=light_profiles.EllipticalSersic),
                              optimizer_class=optimizer_class, phase_name="{}/phase1".format(name))

    class LensSubtractedPhase(ph.ProfileSourceLensPhase):
        def modify_image(self, masked_image, previous_results):
            return masked_image - previous_results.last.lens_galaxy_image

        def pass_priors(self, previous_results):
            self.lens_galaxy.sie.centre = previous_results.last.variable.lens_galaxy.elliptical_sersic.centre

    # 2) Lens Light : None
    #    Mass: SIE (use lens light profile centre from previous phase as prior on mass profile centre)
    #    Source: EllipticalSersic
    #    NLO: MultiNest
    #    Image : Lens Subtracted Image (previous phase)
    #    Mask : Annulus (0.4" - 3.0")

    def annular_mask_function(img):
        return msk.Mask.annular(img.shape_arc_seconds, pixel_scale=img.pixel_scale, inner_radius=0.4,
                                outer_radius=3.)

    phase2 = LensSubtractedPhase(lens_galaxy=gp.GalaxyPrior(sie=mass_profiles.SphericalIsothermal),
                                 source_galaxy=gp.GalaxyPrior(elliptical_sersic=light_profiles.EllipticalSersic),
                                 optimizer_class=optimizer_class,
                                 mask_function=annular_mask_function,
                                 name="{}/phase2".format(name))

    # 3) Lens Light : Elliptical Sersic (Priors phase 1)
    #    Mass: SIE (Priors phase 2)
    #    Source : Elliptical Sersic (Priors phase 2)
    #    NLO : MultiNest
    #    Image : Observed Image
    #    Mask : Circle - 3.0"

    class CombinedPhase(ph.ProfileSourceLensPhase):
        def pass_priors(self, previous_results):
            self.lens_galaxy = gp.GalaxyPrior(
                elliptical_sersic=previous_results.first.variable.lens_galaxy.elliptical_sersic,
                sie=previous_results.last.variable.lens_galaxy.sie)
            self.source_galaxy = previous_results.last.variable.source_galaxy

    phase3 = CombinedPhase(optimizer_class=optimizer_class,
                           name="{}/phase3".format(name))

    # 3H) Hyper-Parameters: Make Lens Galaxy and Source Galaxy Hyper-Galaxies.
    #     Lens Light / Mass / Source - Fix parameters to phase 3 most likely result
    #     NLO : DownhillSimplex
    #     Image : Observed Image
    #     Mask : Circle - 3.0"

    phase3h = ph.SourceLensHyperGalaxyPhase(name="{}/phase3h".format(name))

    # 4) Repeat phase 3, using its priors and the hyper-galaxies fixed to their optimized values.
    #    Lens Light : Elliptical Sersic (Priors phase 3)
    #    Mass: SIE (Priors phase 3)
    #    Source : Elliptical Sersic (Priors phase 3)
    #    NLO : MultiNest
    #    Image : Observed Image
    #    Mask : Circle - 3.0"

    class CombinedPhase2(ph.ProfileSourceLensPhase):
        def pass_priors(self, previous_results):
            phase_3_results = previous_results[2]
            self.lens_galaxy = phase_3_results.variable.lens_galaxy
            self.source_galaxy = phase_3_results.variable.source_galaxy
            self.lens_galaxy.hyper_galaxy = previous_results.last.constant.lens_galaxy.hyper_galaxy
            self.source_galaxy.hyper_galaxy = previous_results.last.constant.source_galaxy.hyper_galaxy

    phase4 = CombinedPhase2(optimizer_class=optimizer_class, name="{}/phase4".format(name))

    return pl.Pipeline(name, phase1, phase2, phase3, phase3h, phase4)


if __name__ == "__main__":
    test_profile_pipeline()
