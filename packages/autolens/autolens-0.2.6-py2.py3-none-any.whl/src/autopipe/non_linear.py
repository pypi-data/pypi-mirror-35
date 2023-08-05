import getdist

from autolens import exc
import math
import os
import pymultinest
import scipy.optimize
from autolens.imaging import hyper_image
import conf
from autolens.autopipe import model_mapper as mm
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)

default_path = '{}/../../output'.format(os.path.dirname(os.path.realpath(__file__)))
dir_path = os.path.dirname(os.path.realpath(__file__))

SIMPLEX_TUPLE_WIDTH = 0.1

def generate_parameter_latex(parameters, subscript=''):
    """Generate a latex label for a non-linear search parameter.

    This is used for the param names file and outputting the nlo of a run to a latex table.

    Parameters
    ----------
    parameters : [str]
        The parameter names to be converted to latex.
    subscript : str
        The subscript of the latex entry, often giving the parameter type (e.g. light or dark matter) or numerical \
        number of the component of the model_mapper.

    """

    latex = []

    if subscript == '':
        for param in parameters:
            latex.append('$' + param + '$')
    else:
        for param in parameters:
            latex.append('$' + param + r'_{\mathrm{' + subscript + '}}$')

    return latex


class Result(object):

    def __init__(self, constant, likelihood, variable=None):
        """
        The result of an optimization.

        Parameters
        ----------
        constant: mm.ModelInstance
            An instance object comprising the class instances that gave the optimal fit
        likelihood: float
            A value indicating the likelihood given by the optimal fit
        variable: mm.ModelMapper
            An object comprising priors determined by this stage of the analysis
        """
        self.constant = constant
        self.likelihood = likelihood
        self.variable = variable

    def __str__(self):
        return "Analysis Result:\n{}".format(
            "\n".join(["{}: {}".format(key, value) for key, value in self.__dict__.items()]))


class NonLinearOptimizer(object):

    def __init__(self, include_hyper_image=False, model_mapper=None,
                 config_path=None, path=default_path, name=None, **classes):
        """Abstract base class for non-linear optimizers.

        This class sets up the file structure for the non-linear optimizer nlo, which are standardized across all \
        non-linear optimizers.

        Parameters
        ------------
        path : str
            The path where the non-linear analysis nlo are stored.
        obj_name : str
            Unique identifier of the weighted_data being analysed (e.g. the name of the weighted_data set)
        """
        self.nlo_config = conf.NamedConfig(
            "{}/../../config/non_linear.ini".format(dir_path) if config_path is None else config_path,
            self.__class__.__name__)

        self.path = "{}/{}".format(path, name) if name is not None else path
        self.variable = mm.ModelMapper() if model_mapper is None else model_mapper
        self.constant = mm.ModelInstance()

        self.file_param_names = "{}/{}".format(self.path, '/multinest.paramnames')
        self.file_model_info = "{}/{}".format(self.path, '/model.info')

        # If the include_hyper_image flag is set to True make this an additional prior model
        if include_hyper_image:
            self.hyper_image = mm.PriorModel(hyper_image.HyperImage, config=self.variable.config)

    def save_model_info(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)  # Create results folder if doesnt exist

    #    self.create_param_names()
        self.variable.output_model_info(self.file_model_info)
        self.variable.check_model_info(self.file_model_info)

    def fit(self, analysis):
        raise NotImplementedError("Fitness function must be overridden by non linear optimizers")

    # def create_param_names(self):
    #     """The param_names file lists every parameter's name and Latex tag, and is used for *GetDist* visualization.
    #
    #     The parameter names are determined from the class instance names of the model_mapper. Latex tags are \
    #     properties of each model class."""
    #     param_names = open(self.file_param_names, 'w')
    #
    #     for prior_name, prior_model in self.variable.flat_prior_models:
    #
    #         param_labels = prior_model.cls.parameter_labels.__get__(prior_model.cls)
    #         component_number = prior_model.cls().component_number
    #         subscript = prior_model.cls.subscript.__get__(prior_model.cls) + str(component_number + 1)
    #
    #         param_labels = generate_parameter_latex(param_labels, subscript)
    #
    #         for param_no, param in enumerate(self.variable.class_priors_dict[prior_name]):
    #             line = prior_name + '_' + param[0]
    #             line += ' ' * (40 - len(line)) + param_labels[param_no]
    #
    #             param_names.write(line + '\n')
    #
    #     param_names.close()


class DownhillSimplex(NonLinearOptimizer):

    def __init__(self, include_hyper_image=False, model_mapper=None, path=default_path,
                 fmin=scipy.optimize.fmin, name=None):
        super(DownhillSimplex, self).__init__(include_hyper_image=include_hyper_image,
                                              model_mapper=model_mapper, path=path, name=name)

        self.xtol = self.nlo_config.get("xtol", float)
        self.ftol = self.nlo_config.get("ftol", float)
        self.maxiter = self.nlo_config.get("maxiter", int)
        self.maxfun = self.nlo_config.get("maxfun", int)

        self.full_output = self.nlo_config.get("full_output", int)
        self.disp = self.nlo_config.get("disp", int)
        self.retall = self.nlo_config.get("retall", int)

        self.fmin = fmin

        logger.debug("Creating DownhillSimplex NLO")

    def fit(self, analysis):
        initial_vector = self.variable.physical_vector_from_prior_medians

        class Fitness(object):
            def __init__(self, instance_from_physical_vector, constant):
                self.result = None
                self.instance_from_physical_vector = instance_from_physical_vector
                self.constant = constant

            def __call__(self, vector):
                instance = self.instance_from_physical_vector(vector)
                for key, value in self.constant.__dict__.items():
                    setattr(instance, key, value)

                likelihood = analysis.fit(**instance.__dict__)
                self.result = Result(instance, likelihood)

                # Return Chi squared
                return -2 * likelihood

        fitness_function = Fitness(self.variable.instance_from_physical_vector, self.constant)

        logger.info("Running DownhillSimplex...")
        output = self.fmin(fitness_function, x0=initial_vector)
        logger.info("DownhillSimplex complete")
        res = fitness_function.result

        # Create a set of Gaussian priors from this result and associate them with the result object.
        res.variable = self.variable.mapper_from_gaussian_means(output)

        return res


class MultiNest(NonLinearOptimizer):

    def __init__(self, include_hyper_image=False, model_mapper=None, path=default_path,
                 sigma_limit=3, run=pymultinest.run, name=None):
        """Class to setup and run a MultiNest analysis and output the MultiNest nlo.

        This interfaces with an input model_mapper, which is used for setting up the individual model instances that \
        are passed to each iteration of MultiNest.

        Parameters
        ------------
        path : str
            The path where the non_linear nlo are stored.
        """

        super(MultiNest, self).__init__(include_hyper_image=include_hyper_image, model_mapper=model_mapper,
                                        path=path, name=name)

        self.file_summary = "{}/{}".format(self.path, 'summary.txt')
        self.file_weighted_samples = "{}/{}".format(self.path, 'multinest.txt')
        self._weighted_sample_model = None
        self.sigma_limit = sigma_limit

        self.importance_nested_sampling = self.nlo_config.get('importance_nested_sampling', bool)
        self.multimodal = self.nlo_config.get('multimodal', bool)
        self.const_efficiency_mode = self.nlo_config.get('const_efficiency_mode', bool)
        self.n_live_points = self.nlo_config.get('n_live_points', int)
        self.evidence_tolerance = self.nlo_config.get('evidence_tolerance', float)
        self.sampling_efficiency = self.nlo_config.get('sampling_efficiency', float)
        self.n_iter_before_update = self.nlo_config.get('n_iter_before_update', int)
        self.null_log_evidence = self.nlo_config.get('null_log_evidence', float)
        self.max_modes = self.nlo_config.get('max_modes', int)
        self.mode_tolerance = self.nlo_config.get('mode_tolerance', float)
        self.outputfiles_basename = self.nlo_config.get('outputfiles_basename', str)
        self.seed = self.nlo_config.get('seed', int)
        self.verbose = self.nlo_config.get('verbose', bool)
        self.resume = self.nlo_config.get('resume', bool)
        self.context = self.nlo_config.get('context', int)
        self.write_output = self.nlo_config.get('write_output', bool)
        self.log_zero = self.nlo_config.get('log_zero', float)
        self.max_iter = self.nlo_config.get('max_iter', int)
        self.init_MPI = self.nlo_config.get('init_MPI', bool)
        self.run = run

        logger.debug("Creating MultiNest NLO")

    @property
    def pdf(self):
        return getdist.mcsamples.loadMCSamples(self.file_weighted_samples)

    def fit(self, analysis, manual_bypass=False):
        self.save_model_info()

        class Fitness(object):
            def __init__(self, instance_from_physical_vector, constant):
                self.result = None
                self.instance_from_physical_vector = instance_from_physical_vector
                self.constant = constant
                self.max_likelihood = 0.

            def __call__(self, cube, ndim, nparams, lnew):
                instance = self.instance_from_physical_vector(cube)
                for key, value in self.constant.__dict__.items():
                    setattr(instance, key, value)

                likelihood = analysis.fit(**instance.__dict__)

                # TODO: Use multinest to provide best model

                if likelihood > self.max_likelihood:
                    self.max_likelihood = likelihood
                    self.result = Result(instance, likelihood)

                return likelihood

        # noinspection PyUnusedLocal
        def prior(cube, ndim, nparams):

            phys_cube = self.variable.physical_vector_from_hypercube_vector(hypercube_vector=cube)

            for i in range(self.variable.total_parameters):
                cube[i] = phys_cube[i]

            return cube

        fitness_function = Fitness(self.variable.instance_from_physical_vector, self.constant)

        if manual_bypass is False:

            logger.info("Running MultiNest...")
            self.run(fitness_function.__call__, prior, self.variable.total_parameters,
                     outputfiles_basename="{}/".format(self.path), n_live_points=self.n_live_points,
                     const_efficiency_mode=self.const_efficiency_mode,
                     importance_nested_sampling=self.importance_nested_sampling,
                     evidence_tolerance=self.evidence_tolerance, sampling_efficiency=self.sampling_efficiency,
                     null_log_evidence=self.null_log_evidence, n_iter_before_update=self.n_iter_before_update,
                     multimodal=self.multimodal, max_modes=self.max_modes, mode_tolerance=self.mode_tolerance,
                     seed=self.seed,
                     verbose=self.verbose, resume=self.resume, context=self.context, write_output=self.write_output,
                     log_zero=self.log_zero, max_iter=self.max_iter, init_MPI=self.init_MPI)
            logger.info("MultiNest complete")

        result = fitness_function.result

        result.variable = self.variable.mapper_from_gaussian_tuples(self.gaussian_priors_at_sigma_limit(self.sigma_limit))

        return result

    def open_summary_file(self):

        summary = open(self.file_summary)

        expected_parameters = (len(summary.readline()) - 113) / 112

        if expected_parameters != self.variable.total_parameters:
            raise exc.MultiNestException(
                'The file_summary file has a different number of parameters than the input model')

        return summary

    def read_vector_from_summary(self, number_entries, offset):

        summary = self.open_summary_file()

        summary.seek(0)
        summary.read(2 + offset * self.variable.total_parameters)
        vector = []
        for param in range(number_entries):
            vector.append(float(summary.read(28)))

        summary.close()

        return vector

    def most_probable_from_summary(self):
        """
        Read the most probable or most likely model values from the 'obj_summary.txt' file which nlo from a \
        multinest analysis.

        This file stores the parameters of the most probable model in the first half of entries and the most likely
        model in the second half of entries. The offset parameter is used to start at the desired model.

        """
        return self.read_vector_from_summary(number_entries=self.variable.total_parameters, offset=0)

    def most_likely_from_summary(self):
        """
        Read the most probable or most likely model values from the 'obj_summary.txt' file which nlo from a \
        multinest analysis.

        This file stores the parameters of the most probable model in the first half of entries and the most likely
        model in the second half of entries. The offset parameter is used to start at the desired model.
        """
        return self.read_vector_from_summary(number_entries=self.variable.total_parameters, offset=56)

    def max_likelihood_from_summary(self):
        return self.read_vector_from_summary(number_entries=2, offset=112)[0]

    def max_log_likelihood_from_summary(self):
        return self.read_vector_from_summary(number_entries=2, offset=112)[1]

    def most_probable_instance_from_summary(self):
        most_probable = self.most_probable_from_summary()
        return self.variable.instance_from_physical_vector(most_probable)

    def most_likely_instance_from_summary(self):
        most_likely = self.most_likely_from_summary()
        return self.variable.instance_from_physical_vector(most_likely)

    def gaussian_priors_at_sigma_limit(self, sigma_limit):
        """Compute the Gaussian Priors these results should be initialzed with in the next phase, by taking their \
        most probable values (e.g the means of their PDF) and computing the error at an input sigma_limit.

        Parameters
        -----------
        sigma_limit : float
            The sigma limit within which the PDF is used to estimate errors (e.g. sigma_limit = 1.0 uses 0.6826 of the \
            PDF).
        """

        means = self.most_probable_from_summary()
        uppers = self.model_at_upper_sigma_limit(sigma_limit)
        lowers = self.model_at_lower_sigma_limit(sigma_limit)

        # noinspection PyArgumentList
        sigmas = list(map(lambda mean, upper, lower: max([upper - mean, mean - lower]), means, uppers, lowers))

        return list(map(lambda mean, sigma: (mean, sigma), means, sigmas))

    def model_at_sigma_limit(self, sigma_limit):
        limit = math.erf(0.5 * sigma_limit * math.sqrt(2))
        densities_1d = list(map(lambda p: self.pdf.get1DDensity(p), self.pdf.getParamNames().names))
        return list(map(lambda p: p.getLimits(limit), densities_1d))

    def model_at_upper_sigma_limit(self, sigma_limit):
        """Setup 1D vectors of the upper and lower limits of the multinest nlo.

        These are generated at an input limfrac, which gives the percentage of 1d posterior weighted samples within \
        each parameter estimate

        Parameters
        -----------
        sigma_limit : float
            The sigma limit within which the PDF is used to estimate errors (e.g. sigma_limit = 1.0 uses 0.6826 of the \
            PDF).
        """
        return list(map(lambda param: param[1], self.model_at_sigma_limit(sigma_limit)))

    def model_at_lower_sigma_limit(self, sigma_limit):
        """Setup 1D vectors of the upper and lower limits of the multinest nlo.

        These are generated at an input limfrac, which gives the percentage of 1d posterior weighted samples within \
        each parameter estimate

        Parameters
        -----------
        sigma_limit : float
            The sigma limit within which the PDF is used to estimate errors (e.g. sigma_limit = 1.0 uses 0.6826 of the \
            PDF).
        """
        return list(map(lambda param: param[0], self.model_at_sigma_limit(sigma_limit)))

    def weighted_sample_instance_from_weighted_samples(self, index):
        """Setup a model instance of a weighted sample, including its weight and likelihood.

        Parameters
        -----------
        index : int
            The index of the weighted sample to return.
        """
        model, weight, likelihood = self.weighted_sample_model_from_weighted_samples(index)

        self._weighted_sample_model = model

        return self.variable.instance_from_physical_vector(model), weight, likelihood

    def weighted_sample_model_from_weighted_samples(self, index):
        """From a weighted sample return the model, weight and likelihood hood.

        NOTE: GetDist reads the log likelihood from the weighted_sample.txt file (column 2), which are defined as \
        -2.0*likelihood. This routine converts these back to likelihood.

        Parameters
        -----------
        index : int
            The index of the weighted sample to return.
        """
        return list(self.pdf.samples[index]), self.pdf.weights[index], -0.5 * self.pdf.loglikes[index]
