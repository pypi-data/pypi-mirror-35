"""Structuring of BLP problem results and computation of post-estimation outputs."""

import time
from typing import Any, Callable, Dict, Hashable, List, Optional, Sequence, TYPE_CHECKING, Tuple

import numpy as np
import scipy.linalg

from . import exceptions, options
from .configurations.iteration import Iteration
from .primitives import LinearParameters, Market, NonlinearParameters
from .utilities.basics import Array, Error, TableFormatter, format_number, format_seconds, generate_items, output
from .utilities.statistics import compute_gmm_se, compute_gmm_weights


# import additional classes that create import cycles only when checking types
if TYPE_CHECKING:
    from .problem import Problem, Progress  # noqa


class Results(object):
    r"""Results of a solved BLP problem.

    Many results are class attributes. Other post-estimation outputs be computed by calling class methods.

    .. note::

       All methods in this class support :func:`parallel` processing. If multiprocessing is used, market-by-market
       computation of each post-estimation output will be distributed among the processes.

    Attributes
    ----------
    problem : `Problem`
        :class:`Problem` that created these results.
    last_results : `Results`
        :class:`Results` from the last GMM step.
    step : `int`
        GMM step that created these results.
    optimization_time : `float`
        Number of seconds it took the optimization routine to finish.
    cumulative_optimization_time : `float`
        Sum of :attr:`Results.optimization_time` for this step and all prior steps.
    total_time : `float`
        Sum of :attr:`Results.optimization_time` and the number of seconds it took to set up the GMM step and compute
        results after optimization had finished.
    cumulative_total_time : `float`
        Sum of :attr:`Results.total_time` for this step and all prior steps.
    optimization_iterations : `int`
        Number of major iterations completed by the optimization routine.
    cumulative_optimization_iterations : `int`
        Sum of :attr:`Results.optimization_iterations` for this step and all prior steps.
    objective_evaluations : `int`
        Number of GMM objective evaluations.
    cumulative_objective_evaluations : `int`
        Sum of :attr:`Results.objective_evaluations` for this step and all prior steps.
    fp_iterations : `ndarray`
        Number of major iterations completed by the iteration routine used to compute :math:`\delta(\hat{\theta})` in
        each market during each objective evaluation. Rows are in the same order as :attr:`Results.unique_market_ids`
        and column indices correspond to objective evaluations.
    cumulative_fp_iterations : `ndarray`
        Concatenation of :attr:`Results.fp_iterations` for this step and all prior steps.
    contraction_evaluations : `ndarray`
        Number of times the contraction used to compute :math:`\delta(\hat{\theta})` was evaluated in each market during
        each objective evaluation. Rows are in the same order as :attr:`Results.unique_market_ids` and column indices
        correspond to objective evaluations.
    cumulative_contraction_evaluations : `ndarray`
        Concatenation of :attr:`Results.contraction_evaluations` for this step and all prior steps.
    theta : `ndarray`
        Estimated unfixed nonlinear parameters, :math:`\hat{\theta}`.
    sigma : `ndarray`
        Estimated Cholesky decomposition of the covariance matrix that measures agents' random taste distribution,
        :math:`\hat{\Sigma}`.
    pi : `ndarray`
        Estimated parameters that measures how agent tastes vary with demographics, :math:`\hat{\Pi}`.
    rho : `ndarray`
        Estimated parameters that measure within nesting group correlations, :math:`\hat{\rho}`.
    beta : `ndarray`
        Estimated demand-side linear parameters, :math:`\hat{\beta}`.
    gamma : `ndarray`
        Estimated supply-side linear parameters, :math:`\hat{\gamma}`.
    sigma_se : `ndarray`
        Estimated standard errors for unknown :math:`\hat{\Sigma}` elements in :math:`\hat{\theta}`.
    pi_se : `ndarray`
        Estimated standard errors for unknown :math:`\hat{\Pi}` elements in :math:`\hat{\theta}`.
    rho_se : `ndarray`
        Estimated standard errors for unknown :math:`\hat{\rho}` elements in :math:`\hat{\theta}`.
    beta_se : `ndarray`
        Estimated standard errors for :math:`\hat{\beta}`.
    gamma_se : `ndarray`
        Estimated standard errors for :math:`\hat{\gamma}`.
    sigma_bounds : `tuple`
        Bounds for :math:`\Sigma` that were used during optimization, which are of the form ``(lb, ub)``.
    pi_bounds : `tuple`
        Bounds for :math:`\Pi` that were used during optimization, which are of the form ``(lb, ub)``.
    rho_bounds : `tuple`
        Bounds for :math:`\rho` that were used during optimization, which are of the form ``(lb, ub)``.
    delta : `ndarray`
        Estimated mean utility, :math:`\delta(\hat{\theta})`, which may have been residualized to absorb any demand-side
        fixed effects.
    true_delta : `ndarray`
        Estimated mean utility, :math:`\delta(\hat{\theta})`.
    tilde_costs : `ndarray`
        Estimated transformed marginal costs, :math:`\tilde{c}(\hat{\theta})`, which may have been residualized to
        absorb any demand-side fixed effects. Transformed marginal costs are simply :math:`\tilde{c} = c`, marginal
        costs, under a linear cost specification, and are :math:`\tilde{c} = \log c` under a log-linear specification.
        If `costs_bounds` were specified in :meth:`Problem.solve`, :math:`c` may have been clipped.
    true_tilde_costs : `ndarray`
        Estimated transformed marginal costs, :math:`\tilde{c}(\hat{\theta})`. Transformed marginal costs are simply
        :math:`\tilde{c} = c`, marginal costs, under a linear cost specification, and are :math:`\tilde{c} = \log c`
        under a log-linear specification. If `costs_bounds` were specified in :meth:`Problem.solve`, :math:`c` may have
        been clipped.
    xi : `ndarray`
        Estimated unobserved demand-side product characteristics, :math:`\xi(\hat{\theta})`, or equivalently, the
        demand-side structural error term, which includes the contribution of any absorbed demand-side fixed effects.
    true_xi : `ndarray
        Estimated unobserved demand-side product characteristics, :math:`\xi(\hat{\theta})`.
    omega : `ndarray`
        Estimated unobserved supply-side product characteristics, :math:`\omega(\hat{\theta})`, or equivalently, the
        supply-side structural error term, which includes the contribution of any absorbed supply-side fixed effects.
    true_omega : `ndarray`
        Estimated unobserved supply-side product characteristics, :math:`\omega(\hat{\theta})`, or equivalently, the
        supply-side structural error term.
    objective : `float`
        GMM objective value.
    xi_jacobian : `ndarray`
        Estimated :math:`\partial\xi / \partial\theta = \partial\delta / \partial\theta`.
    omega_jacobian : `ndarray`
        Estimated :math:`\partial\omega / \partial\theta = \partial\tilde{c} / \partial\theta`.
    gradient : `ndarray`
        Estimated gradient of the GMM objective with respect to :math:`\theta`. This is still computed once at the end
        of an optimization routine that was configured to not use analytic gradients.
    gradient_norm : `ndarray`
        Infinity norm of :attr:`Results.gradient`.
    sigma_gradient : `ndarray`
        Estimated gradient of the GMM objective with respect to unknown :math:`\Sigma` elements in :math:`\theta`.
    pi_gradient : `ndarray`
        Estimated gradient of the GMM objective with respect to unknown :math:`\Pi` elements in :math:`\theta`.
    rho_gradient : `ndarray`
        Estimated gradient of the GMM objective with respect to unknown :math:`\rho` elements in :math:`\theta`.
    WD : `ndarray`
        Demand-side weighting matrix, :math:`W_D`, used to compute these results.
    WS : `ndarray`
        Supply-side weighting matrix, :math:`W_S`, used to compute these results.
    updated_WD : `ndarray`
        Updated demand-side weighting matrix.
    updated_WS : `ndarray`
        Updated supply-side weighting matrix.
    unique_market_ids : `ndarray`
        Unique market IDs, which are in the same order as post-estimation outputs returned by methods that compute a
        single value for each market.

    Examples
    --------
    For examples of how to use class methods, refer to the :doc:`Examples </examples>` section.

    """

    problem: 'Problem'
    last_results: Optional['Results']
    step: int
    optimization_time: float
    cumulative_optimization_time: float
    total_time: float
    cumulative_total_time: float
    optimization_iterations: int
    cumulative_optimization_iterations: int
    objective_evaluations: int
    cumulative_objective_evaluations: int
    fp_iterations: Array
    cumulative_fp_iterations: Array
    contraction_evaluations: Array
    cumulative_contraction_evaluations: Array
    theta: Array
    sigma: Array
    pi: Array
    rho: Array
    beta: Array
    gamma: Array
    sigma_se: Array
    pi_se: Array
    rho_se: Array
    beta_se: Array
    gamma_se: Array
    sigma_bounds: tuple
    pi_bounds: tuple
    rho_bounds: tuple
    delta: Array
    true_delta: Array
    tilde_costs: Array
    true_tilde_costs: Array
    xi: Array
    true_xi: Array
    omega: Array
    true_omega: Array
    objective: Array
    xi_jacobian: Array
    omega_jacobian: Array
    gradient: Array
    gradient_norm: Array
    sigma_gradient: Array
    pi_gradient: Array
    rho_gradient: Array
    WD: Array
    WS: Array
    updated_WD: Array
    updated_WS: Array
    unique_market_ids: Array

    _se_type: str
    _errors: List[Error]
    _linear_parameters: LinearParameters
    _nonlinear_parameters: NonlinearParameters

    def __init__(
            self, progress: 'Progress', last_results: Optional['Results'], step_start_time: float,
            optimization_start_time: float, optimization_end_time: float, iterations: int, evaluations: int,
            iteration_mappings: Sequence[Dict[Hashable, int]], evaluation_mappings: Sequence[Dict[Hashable, int]],
            center_moments: bool, W_type: str, se_type: str) -> None:
        """Update weighting matrices, estimate standard errors, and compute cumulative progress statistics."""

        # initialize values from the progress structure
        self._errors = progress.errors
        self.problem = progress.problem
        self.WD = progress.WD
        self.WS = progress.WS
        self.theta = progress.theta
        self.true_delta = progress.true_delta
        self.true_tilde_costs = progress.true_tilde_costs
        self.xi_jacobian = progress.xi_jacobian
        self.omega_jacobian = progress.omega_jacobian
        self.delta = progress.delta
        self.tilde_costs = progress.tilde_costs
        self.true_xi = progress.true_xi
        self.true_omega = progress.true_omega
        self.beta = progress.beta
        self.gamma = progress.gamma
        self.objective = progress.objective
        self.gradient = progress.gradient
        self.gradient_norm = progress.gradient_norm

        # initialize counts and times
        self.step = 1
        self.total_time = self.cumulative_total_time = time.time() - step_start_time
        self.optimization_time = self.cumulative_optimization_time = optimization_end_time - optimization_start_time
        self.optimization_iterations = self.cumulative_optimization_iterations = iterations
        self.objective_evaluations = self.cumulative_objective_evaluations = evaluations

        # store unique market IDs
        self.unique_market_ids = self.problem.unique_market_ids

        # convert contraction mappings to matrices with rows ordered by market
        iteration_lists = [[m[t] if m else 0 for m in iteration_mappings] for t in self.unique_market_ids]
        evaluation_lists = [[m[t] if m else 0 for m in evaluation_mappings] for t in self.unique_market_ids]
        self.fp_iterations = self.cumulative_fp_iterations = np.array(iteration_lists, np.int)
        self.contraction_evaluations = self.cumulative_contraction_evaluations = np.array(evaluation_lists, np.int)

        # initialize last results and add to cumulative values
        self.last_results = last_results
        if last_results is not None:
            self.step += last_results.step
            self.cumulative_total_time += last_results.cumulative_total_time
            self.cumulative_optimization_time += last_results.cumulative_optimization_time
            self.cumulative_optimization_iterations += last_results.cumulative_optimization_iterations
            self.cumulative_objective_evaluations += last_results.cumulative_objective_evaluations
            self.cumulative_fp_iterations = np.c_[
                last_results.cumulative_fp_iterations, self.cumulative_fp_iterations
            ]
            self.cumulative_contraction_evaluations = np.c_[
                last_results.cumulative_contraction_evaluations, self.cumulative_contraction_evaluations
            ]

        # store parameter information
        self._linear_parameters = LinearParameters(self.problem, self.beta, self.gamma)
        self._nonlinear_parameters = progress.nonlinear_parameters
        self.sigma_bounds = self._nonlinear_parameters.sigma_bounds
        self.pi_bounds = self._nonlinear_parameters.pi_bounds
        self.rho_bounds = self._nonlinear_parameters.rho_bounds

        # expand the nonlinear parameters and their gradient
        self.sigma, self.pi, self.rho = self._nonlinear_parameters.expand(self.theta)
        self.sigma_gradient, self.pi_gradient, self.rho_gradient = self._nonlinear_parameters.expand(
            self.gradient, nullify=True
        )

        # compute a version of xi that includes the contribution of any demand-side fixed effects
        self.xi = self.true_xi
        if self.problem.ED > 0:
            ones = np.ones_like(self.xi)
            true_X1 = np.column_stack((ones * f.evaluate(self.problem.products) for f in self.problem._X1_formulations))
            self.xi = self.true_delta - true_X1 @ self.beta

        # compute a version of omega that includes the contribution of any supply-side fixed effects
        self.omega = self.true_omega
        if self.problem.ES > 0:
            ones = np.ones_like(self.xi)
            true_X3 = np.column_stack((ones * f.evaluate(self.problem.products) for f in self.problem._X3_formulations))
            self.omega = self.true_tilde_costs - true_X3 @ self.gamma

        # update the weighting matrices
        self.updated_WD, WD_errors = compute_gmm_weights(
            self.true_xi, self.problem.products.ZD, W_type, center_moments, self.problem.products.clustering_ids
        )
        self.updated_WS, WS_errors = compute_gmm_weights(
            self.true_omega, self.problem.products.ZS, W_type, center_moments, self.problem.products.clustering_ids
        )
        self._errors.extend(WD_errors + WS_errors)

        # stack errors, weights, instruments, Jacobian of the errors with respect to parameters, and clustering IDs
        if self.problem.K3 == 0:
            u = self.true_xi
            Z = self.problem.products.ZD
            W = self.WD
            jacobian = np.c_[self.xi_jacobian, self.problem.products.X1]
            stacked_clustering_ids = self.problem.products.clustering_ids
        else:
            u = np.r_[self.true_xi, self.true_omega]
            Z = scipy.linalg.block_diag(self.problem.products.ZD, self.problem.products.ZS)
            W = scipy.linalg.block_diag(self.WD, self.WS)
            jacobian = np.c_[
                np.r_[self.xi_jacobian, self.omega_jacobian],
                scipy.linalg.block_diag(self.problem.products.X1, self.problem.products.X3)
            ]
            stacked_clustering_ids = np.r_[self.problem.products.clustering_ids, self.problem.products.clustering_ids]

        # compute standard errors
        se, se_errors = compute_gmm_se(u, Z, W, jacobian, se_type, self.step, stacked_clustering_ids)
        self.sigma_se, self.pi_se, self.rho_se = self._nonlinear_parameters.expand(
            se[:self._nonlinear_parameters.P], nullify=True
        )
        self.beta_se = se[self._nonlinear_parameters.P:self._nonlinear_parameters.P + self.problem.K1]
        self.gamma_se = se[self._nonlinear_parameters.P + self.problem.K1:]
        self._errors.extend(se_errors)
        self._se_type = se_type

    def __str__(self) -> str:
        """Format full results as a string."""

        # construct section containing summary information
        header = [
            ("Cumulative", "Total Time"), ("GMM", "Step"), ("Optimization", "Iterations"),
            ("Objective", "Evaluations"), ("Total Fixed Point", "Iterations"), ("Total Contraction", "Evaluations"),
            ("Objective", "Value"), ("Gradient", "Infinity Norm"),
        ]
        widths = [max(len(k1), len(k2), options.digits + 6 if i > 5 else 0) for i, (k1, k2) in enumerate(header)]
        formatter = TableFormatter(widths)
        sections = [[
            "Results Summary:",
            formatter.line(),
            formatter([k[0] for k in header]),
            formatter([k[1] for k in header], underline=True),
            formatter([
                format_seconds(self.cumulative_total_time),
                self.step,
                self.optimization_iterations,
                self.objective_evaluations,
                self.fp_iterations.sum(),
                self.contraction_evaluations.sum(),
                format_number(float(self.objective)),
                format_number(float(self.gradient_norm))
            ]),
            formatter.line()
        ]]

        # construct a standard error description
        if self._se_type == 'unadjusted':
            se_description = "Unadjusted SEs"
        elif self._se_type == 'robust':
            se_description = "Robust SEs"
        else:
            assert self._se_type == 'clustered'
            se_description = f'Robust SEs Adjusted for {np.unique(self.problem.products.clustering_ids).size} Clusters'

        # construct a section containing linear estimates
        sections.append([
            f"Linear Estimates ({se_description} in Parentheses):",
            self._linear_parameters.format_estimates(self.beta, self.gamma, self.beta_se, self.gamma_se)
        ])

        # construct a section containing nonlinear estimates
        if self.problem.K2 > 0 or self.problem.H > 0:
            sections.append([
                f"Nonlinear Estimates ({se_description} in Parentheses):",
                self._nonlinear_parameters.format_estimates(
                    self.sigma, self.pi, self.rho, self.sigma_se, self.pi_se, self.rho_se
                )
            ])

        # combine the sections into one string
        return "\n\n".join("\n".join(s) for s in sections)

    def __repr__(self) -> str:
        """Defer to the string representation."""
        return str(self)

    def _validate_name(self, name: str) -> None:
        """Validate that a name corresponds to a variable in X1, X2, or X3."""
        formulations = self.problem._X1_formulations + self.problem._X2_formulations + self.problem._X3_formulations
        names = {n for f in formulations for n in f.names}
        if name not in names:
            raise NameError(f"The name '{name}' is not one of the underlying variables, {list(sorted(names))}.")

    def _combine_results(self, compute_market_results: Callable, fixed_args: Sequence, market_args: Sequence) -> Array:
        """Compute post-estimation outputs for each market and stack them into a single matrix

        An output for a single market is computed by passing fixed_args (identical for all markets) and market_args
        (matrices with as many rows as there are products that are restricted to the market) to compute_market_results,
        a ResultsMarket method that returns the output for the market and a set of any errors encountered during
        computation.
        """
        errors: List[Error] = []

        # keep track of how long it takes to compute results
        start_time = time.time()

        # define a factory for markets
        def market_factory(s: Hashable) -> tuple:
            """Build a market along with arguments used to compute results."""
            market_s = ResultsMarket(self.problem, s, self.sigma, self.pi, self.rho, self.beta, self.true_delta)
            args_s = [None if a is None else a[self.problem._product_market_indices[s]] for a in market_args]
            return (market_s, *fixed_args, *args_s)

        # construct a mapping from market IDs to market-specific results and compute the full results matrix size
        rows = columns = 0
        matrix_mapping: Dict[Hashable, Array] = {}
        for t, (array_t, errors_t) in generate_items(self.unique_market_ids, market_factory, compute_market_results):
            errors.extend(errors_t)
            matrix_mapping[t] = np.c_[array_t]
            rows += matrix_mapping[t].shape[0]
            columns = max(columns, matrix_mapping[t].shape[1])

        # output a warning about any errors
        if errors:
            output("")
            output(exceptions.MultipleErrors(errors))
            output("")

        # preserve the original product order or the sorted market order when stacking the matrices
        combined = np.full((rows, columns), np.nan, options.dtype)
        for t, matrix_t in matrix_mapping.items():
            if rows == self.problem.N:
                combined[self.problem._product_market_indices[t], :matrix_t.shape[1]] = matrix_t
            else:
                combined[self.unique_market_ids == t, :matrix_t.shape[1]] = matrix_t

        # output how long it took to compute results
        end_time = time.time()
        output(f"Finished after {format_seconds(end_time - start_time)}.")
        output("")
        return combined

    def compute_aggregate_elasticities(self, factor: float = 0.1, name: str = 'prices') -> Array:
        r"""Estimate aggregate elasticities of demand, :math:`E`, with respect to a variable, :math:`x`.

        In market :math:`t`, the aggregate elasticity of demand is

        .. math:: E = \sum_{j=1}^{J_t} \frac{s_{jt}(x + \Delta x) - s_{jt}}{\Delta},

        in which :math:`\Delta` is a scalar factor and :math:`s_{jt}(x + \Delta x)` is the share of product :math:`j` in
        market :math:`t`, evaluated at the scaled values of the variable.

        Parameters
        ----------
        factor : `float, optional`
            The scalar factor, :math:`\Delta`.
        name : `str, optional`
            Name of the variable, :math:`x`. By default, :math:`x = p`, prices.

        Returns
        -------
        `ndarray`
            Estimates of aggregate elasticities of demand, :math:`E`, for all markets. Rows are in the same order as
            :attr:`Results.unique_market_ids`.

        """
        output(f"Computing aggregate elasticities with respect to {name} ...")
        self._validate_name(name)
        return self._combine_results(ResultsMarket.compute_aggregate_elasticity, [factor, name], [])

    def compute_elasticities(self, name: str = 'prices') -> Array:
        r"""Estimate matrices of elasticities of demand, :math:`\varepsilon`, with respect to a variable, :math:`x`.

        For each market, the value in row :math:`j` and column :math:`k` of :math:`\varepsilon` is

        .. math:: \varepsilon_{jk} = \frac{x_k}{s_j}\frac{\partial s_j}{\partial x_k}.

        Parameters
        ----------
        name : `str, optional`
            Name of the variable, :math:`x`. By default, :math:`x = p`, prices.

        Returns
        -------
        `ndarray`
            Stacked :math:`J_t \times J_t` estimated matrices of elasticities of demand, :math:`\varepsilon`, for each
            market :math:`t`. Columns for a market are in the same order as products for the market. If a market has
            fewer products than others, extra columns will contain ``numpy.nan``.

        """
        output(f"Computing elasticities with respect to {name} ...")
        self._validate_name(name)
        return self._combine_results(ResultsMarket.compute_elasticities, [name], [])

    def compute_diversion_ratios(self, name: str = 'prices') -> Array:
        r"""Estimate matrices of diversion ratios, :math:`\mathscr{D}`, with respect to a variable, :math:`x`.

        Diversion ratios to the outside good are reported on diagonals. For each market, the value in row :math:`j` and
        column :math:`k` is

        .. math:: \mathscr{D}_{jk} = -\frac{\partial s_{k(j)} / \partial x_j}{\partial s_j / \partial x_j},

        in which :math:`s_{k(j)}` is :math:`s_0 = 1 - \sum_j s_j` if :math:`j = k`, and is :math:`s_k` otherwise.

        Parameters
        ----------
        name : `str, optional`
            Name of the variable, :math:`x`. By default, :math:`x = p`, prices.

        Returns
        -------
        `ndarray`
            Stacked :math:`J_t \times J_t` estimated matrices of diversion ratios, :math:`\mathscr{D}`, for all markets.
            Columns for a market are in the same order as products for the market. If a market has fewer products than
            others, extra columns will contain ``numpy.nan``.

        """
        output(f"Computing diversion ratios with respect to {name} ...")
        self._validate_name(name)
        return self._combine_results(ResultsMarket.compute_diversion_ratios, [name], [])

    def compute_long_run_diversion_ratios(self) -> Array:
        r"""Estimate matrices of long-run diversion ratios, :math:`\bar{\mathscr{D}}`.

        Long-run diversion ratios to the outside good are reported on diagonals. For each market, the value in row
        :math:`j` and column :math:`k` is

        .. math:: \bar{\mathscr{D}}_{jk} = \frac{s_{k(-j)} - s_k}{s_j},

        in which :math:`s_{k(-j)}` is the share of product :math:`k` computed with the outside option removed from the
        choice set if :math:`j = k`, and with product :math:`j` removed otherwise.

        Parameters
        ----------

        Returns
        -------
        `ndarray`
            Stacked :math:`J_t \times J_t` estimated matrices of long-run diversion ratios, :math:`\bar{\mathscr{D}}`,
            for all markets. Columns for a market are in the same order as products for the market. If a market has
            fewer products than others, extra columns will contain ``numpy.nan``.

        """
        output("Computing long run mean diversion ratios ...")
        return self._combine_results(ResultsMarket.compute_long_run_diversion_ratios, [], [])

    def extract_diagonals(self, matrices: Any) -> Array:
        r"""Extract diagonals from stacked :math:`J_t \times J_t` matrices for each market :math:`t`.

        Parameters
        ----------
        matrices : `array-like`
            Stacked matrices, such as estimates of :math:`\varepsilon`, computed by
            :meth:`Results.compute_elasticities`; :math:`\mathscr{D}`, computed by
            :meth:`Results.compute_diversion_ratios`; or :math:`\bar{\mathscr{D}}`, computed by
            :meth:`Results.compute_long_run_diversion_ratios`.

        Returns
        -------
        `ndarray`
            Stacked diagonals for all markets. If the matrices are estimates of :math:`\varepsilon`, a diagonal is a
            market's own elasticities of demand; if they are estimates of :math:`\mathscr{D}` or
            :math:`\bar{\mathscr{D}}`, a diagonal is a market's diversion ratios to the outside good.

        """
        output("Computing own elasticities ...")
        return self._combine_results(ResultsMarket.extract_diagonal, [], [matrices])

    def extract_diagonal_means(self, matrices: Any) -> Array:
        r"""Extract means of diagonals from stacked :math:`J_t \times J_t` matrices for each market :math:`t`.

        Parameters
        ----------
        matrices : `array-like`
            Stacked matrices, such as estimates of :math:`\varepsilon`, computed by
            :meth:`Results.compute_elasticities`; :math:`\mathscr{D}`, computed by
            :meth:`Results.compute_diversion_ratios`; or :math:`\bar{\mathscr{D}}`, computed by
            :meth:`Results.compute_long_run_diversion_ratios`.

        Returns
        -------
        `ndarray`
            Stacked means of diagonals for all markets. If the matrices are estimates of :math:`\varepsilon`, the mean
            of a diagonal is a market's mean own elasticity of demand; if they are estimates of :math:`\mathscr{D}` or
            :math:`\bar{\mathscr{D}}`, the mean of a diagonal is a market's mean diversion ratio to the outside good.
            Rows are in the same order as :attr:`Results.unique_market_ids`.

        """
        output("Computing mean own elasticities ...")
        return self._combine_results(ResultsMarket.extract_diagonal_mean, [], [matrices])

    def compute_costs(self) -> Array:
        r"""Estimate marginal costs, :math:`c`.

        Marginal costs are computed with the BLP-markup equation,

        .. math:: c = p - \eta.

        Parameters
        ----------

        Returns
        -------
        `ndarray`
            Marginal costs, :math:`c`.

        """
        output("Computing marginal costs ...")
        return self._combine_results(ResultsMarket.compute_costs, [], [])

    def compute_approximate_prices(self, firms_index: int = 1, costs: Optional[Any] = None) -> Array:
        r"""Estimate approximate Bertrand-Nash prices after firm ID changes, :math:`p^a`, under the assumption that
        shares and their price derivatives are unaffected by such changes.

        This approximation is discussed in, for example, :ref:`Nevo (1997) <n97>`. Prices in each market are computed
        according to the BLP-markup equation,

        .. math:: p^a = c + \eta^a,

        in which the approximate markup term is

        .. math:: \eta^a = -\left(O^* \circ \frac{\partial s}{\partial p}\right)^{-1}s

        where :math:`O^*` is the ownership matrix associated with specified firm IDs.

        Parameters
        ----------
        firms_index : `int, optional`
            Column index of the firm IDs in the `firm_ids` field of `product_data` in :class:`Problem`. If an
            `ownership` field was specified, the corresponding stack of ownership matrices will be used.
        costs : `array-like, optional`
            Marginal costs, :math:`c`, computed by :meth:`Results.compute_costs`. By default, marginal costs are
            computed.

        Returns
        -------
        `ndarray`
            Estimates of approximate Bertrand-Nash prices after any firm ID changes, :math:`p^a`.

        """
        output("Solving for approximate Bertrand-Nash prices ...")
        return self._combine_results(ResultsMarket.compute_approximate_prices, [firms_index], [costs])

    def compute_prices(
            self, iteration: Optional[Iteration] = None, firms_index: int = 1, prices: Optional[Any] = None,
            costs: Optional[Any] = None) -> Array:
        r"""Estimate Bertrand-Nash prices after firm ID changes, :math:`p^*`.

        Prices are computed in each market by iterating over the :math:`\zeta`-markup equation from
        :ref:`Morrow and Skerlos (2011) <ms11>`,

        .. math:: p^* \leftarrow c + \zeta^*(p^*),

        in which the markup term is

        .. math:: \zeta^*(p^*) = \Lambda^{-1}(p^*)[O^* \circ \Gamma(p^*)]'(p^* - c) - \Lambda^{-1}(p^*)

        where :math:`O^*` is the ownership matrix associated with specified firm IDs.

        Parameters
        ----------
        iteration : `Iteration, optional`
            :class:`Iteration` configuration for how to solve the fixed point problem in each market. By default,
            ``Iteration('simple', {'tol': 1e-12})`` is used.
        firms_index : `int, optional`
            Column index of the firm IDs in the `firm_ids` field of `product_data` in :class:`Problem`. If an
            `ownership` field was specified, the corresponding stack of ownership matrices will be used.
        prices : `array-like, optional`
            Prices at which the fixed point iteration routine will start. By default, unchanged prices, :math:`p`, are
            used as starting values. Other reasonable starting prices include :math:`p^a`, computed by
            :meth:`Results.compute_approximate_prices`.
        costs : `array-like`
            Marginal costs, :math:`c`, computed by :meth:`Results.compute_costs`. By default, marginal costs are
            computed.

        Returns
        -------
        `ndarray`
            Estimates of Bertrand-Nash prices after any firm ID changes, :math:`p^*`.

        """
        output("Solving for Bertrand-Nash prices ...")
        if iteration is None:
            iteration = Iteration('simple', {'tol': 1e-12})
        elif not isinstance(iteration, Iteration):
            raise ValueError("iteration must an Iteration instance.")
        return self._combine_results(ResultsMarket.compute_prices, [iteration, firms_index], [prices, costs])

    def compute_shares(self, prices: Optional[Any] = None) -> Array:
        r"""Estimate shares evaluated at specified prices.

        Parameters
        ----------
        prices : `array-like`
            Prices at which to evaluate shares, such as Bertrand-Nash prices, :math:`p^*`, computed by
            :meth:`Results.compute_prices`, or approximate Bertrand-Nash prices, :math:`p^a`, computed by
            :meth:`Results.compute_approximate_prices`. By default, unchanged prices are used.

        Returns
        -------
        `ndarray`
            Estimates of shares evaluated at the specified prices.

        """
        output("Computing shares ...")
        return self._combine_results(ResultsMarket.compute_shares, [], [prices])

    def compute_hhi(self, firms_index: int = 0, shares: Optional[Any] = None) -> Array:
        r"""Estimate Herfindahl-Hirschman Indices, :math:`\text{HHI}`.

        The index in market :math:`t` is

        .. math:: \text{HHI} = 10,000 \times \sum_{f=1}^{F_t} \left(\sum_{j \in \mathscr{J}_{ft}} s_j\right)^2,

        in which :math:`\mathscr{J}_{ft}` is the set of products produced by firm :math:`f` in market :math:`t`.

        Parameters
        ----------
        firms_index : `int, optional`
            Column index of the firm IDs in the `firm_ids` field of `product_data` in :class:`Problem`. By default,
            unchanged firm IDs are used.
        shares : `array-like, optional`
            Shares, :math:`s`, such as those computed by :meth:`Results.compute_shares`. By default, unchanged shares
            are used.

        Returns
        -------
        `ndarray`
            Estimated Herfindahl-Hirschman Indices, :math:`\text{HHI}`, for all markets. Rows are in the same order as
            :attr:`Results.unique_market_ids`.

        """
        output("Computing HHI ...")
        return self._combine_results(ResultsMarket.compute_hhi, [firms_index], [shares])

    def compute_markups(self, prices: Optional[Any] = None, costs: Optional[Any] = None) -> Array:
        r"""Estimate markups, :math:`\mathscr{M}`.

        The markup of product :math:`j` in market :math:`t` is

        .. math:: \mathscr{M}_{jt} = \frac{p_{jt} - c_{jt}}{p_{jt}}.

        Parameters
        ----------
        prices : `array-like, optional`
            Prices, :math:`p`, such as Bertrand-Nash prices, :math:`p^*`, computed by :meth:`Results.compute_prices`, or
            approximate Bertrand-Nash prices, :math:`p^a`, computed by :meth:`Results.compute_approximate_prices`. By
            default, unchanged prices are used.
        costs : `array-like`
            Marginal costs, :math:`c`, computed by :meth:`Results.compute_costs`. By default, marginal costs are
            computed.

        Returns
        -------
        `ndarray`
            Estimated markups, :math:`\mathscr{M}`.

        """
        output("Computing markups ...")
        return self._combine_results(ResultsMarket.compute_markups, [], [prices, costs])

    def compute_profits(
            self, prices: Optional[Any] = None, shares: Optional[Any] = None, costs: Optional[Any] = None) -> Array:
        r"""Estimate population-normalized gross expected profits, :math:`\pi`.

        The profit of product :math:`j` in market :math:`t` is

        .. math:: \pi_{jt} = p_{jt} - c_{jt}s_{jt}.

        Parameters
        ----------
        prices : `array-like, optional`
            Prices, :math:`p`, such as Bertrand-Nash prices, :math:`p^*`, computed by :meth:`Results.compute_prices`, or
            approximate Bertrand-Nash prices, :math:`p^a`, computed by :meth:`Results.compute_approximate_prices`. By
            default, unchanged prices are used.
        shares : `array-like, optional`
            Shares, :math:`s`, such as those computed by :meth:`Results.compute_shares`. By default, unchanged shares
            are used.
        costs : `array-like`
            Marginal costs, :math:`c`, computed by :meth:`Results.compute_costs`. By default, marginal costs are
            computed.

        Returns
        -------
        `ndarray`
            Estimated population-normalized gross expected profits, :math:`\pi`.

        """
        output("Computing profits ...")
        return self._combine_results(ResultsMarket.compute_profits, [], [prices, shares, costs])

    def compute_consumer_surpluses(self, prices: Optional[Any] = None) -> Array:
        r"""Estimate population-normalized consumer surpluses, :math:`\text{CS}`.

        Assuming away nonlinear income effects, the surplus in market :math:`t` is

        .. math:: \text{CS} = \sum_{i=1}^{I_t} w_i\text{CS}_i,

        in which, if there is no nesting, the consumer surplus for individual :math:`i` is

        .. math:: \text{CS}_i = \frac{\log\left(1 + \sum_{j=1}^{J_t} \exp V_{jti}\right)}{\alpha + \alpha_i}

        where

        .. math:: V_{jti} = \delta_{jt} + \mu_{jti}.

        If there is nesting,

        .. math:: \text{CS}_i = \frac{\log\left(1 + \sum_{h=1}^H \exp V_{hti}\right)}{\alpha + \alpha_i}

        where

        .. math:: V_{hti} = (1 - \rho_h)\log\sum_{j\in\mathscr{J}_{ht}} \exp[V_{jti} / (1 - \rho_h)].

        .. warning::

           The consumer surpluses computed by this method are only correct when there are not nonlinear income effects.
           For example, computed consumer surpluses will be incorrect if a formulation contains ``log(prices)``.

        Parameters
        ----------
        prices : `array-like, optional`
            Prices at which utilities, :math:`u`, and price derivatives, :math:`\alpha` and :math:`\alpha_i`, will be
            evaluated, such as Bertrand-Nash prices, :math:`p^*`, computed by :meth:`Results.compute_prices`, or
            approximate Bertrand-Nash prices, :math:`p^a`, computed by :meth:`Results.compute_approximate_prices`. By
            default, unchanged prices are used.

        Returns
        -------
        `ndarray`
            Estimated population-normalized consumer surpluses, :math:`\text{CS}`, for all markets. Rows are in the same
            order as :attr:`Results.unique_market_ids`.

        """
        output("Computing consumer surpluses with the equation that assumes away nonlinear income effects ...")
        return self._combine_results(ResultsMarket.compute_consumer_surplus, [], [prices])


class ResultsMarket(Market):
    """Results for a single market of a solved BLP problem, which can be used to compute post-estimation outputs. Each
    method returns a matrix and a list of any errors that were encountered.
    """

    def compute_aggregate_elasticity(self, factor: float, name: str) -> Tuple[Array, List[Error]]:
        """Estimate the aggregate elasticity of demand with respect to a variable."""
        scaled_variable = (1 + factor) * self.products[name]
        delta = self.update_delta_with_variable(name, scaled_variable)
        mu = self.update_mu_with_variable(name, scaled_variable)
        shares = self.compute_probabilities(delta, mu) @ self.agents.weights
        aggregate_elasticities = (shares - self.products.shares).sum() / factor
        return aggregate_elasticities, []

    def compute_elasticities(self, name: str) -> Tuple[Array, List[Error]]:
        """Estimate a matrix of elasticities of demand with respect to a variable."""
        derivatives = self.compute_utility_derivatives(name)
        jacobian = self.compute_shares_by_variable_jacobian(derivatives)
        elasticities = jacobian * self.products[name].T / self.products.shares
        return elasticities, []

    def compute_diversion_ratios(self, name: str) -> Tuple[Array, List[Error]]:
        """Estimate a matrix of diversion ratios with respect to a variable."""
        derivatives = self.compute_utility_derivatives(name)
        jacobian = self.compute_shares_by_variable_jacobian(derivatives)

        # replace the diagonal with derivatives with respect to the outside option
        jacobian_diagonal = np.c_[jacobian.diagonal()]
        jacobian[np.diag_indices_from(jacobian)] = -jacobian.sum(axis=1)

        # compute the ratios
        ratios = -jacobian / np.tile(jacobian_diagonal, self.J)
        return ratios, []

    def compute_long_run_diversion_ratios(self) -> Tuple[Array, List[Error]]:
        """Estimate a matrix of long-run diversion ratios."""

        # compute share differences when products are excluded and store outside share differences on the diagonal
        changes = np.zeros((self.J, self.J), options.dtype)
        for j in range(self.J):
            shares_without_j = self.compute_probabilities(eliminate_product=j) @ self.agents.weights
            changes[j] = (shares_without_j - self.products.shares).flat
            changes[j, j] = -changes[j].sum()

        # compute the ratios
        ratios = changes / np.tile(self.products.shares, self.J)
        return ratios, []

    def extract_diagonal(self, matrix: Array) -> Tuple[Array, List[Error]]:
        """Extract the diagonal from a matrix."""
        diagonal = matrix[:, :self.J].diagonal()
        return diagonal, []

    def extract_diagonal_mean(self, matrix: Array) -> Tuple[Array, List[Error]]:
        """Extract the mean of the diagonal from a matrix."""
        diagonal_mean = matrix[:, :self.J].diagonal().mean()
        return diagonal_mean, []

    def compute_costs(self) -> Tuple[Array, List[Error]]:
        """Estimate marginal costs."""
        eta, errors = self.compute_eta()
        costs = self.products.prices - eta
        return costs, errors

    def compute_approximate_prices(
            self, firms_index: int = 0, costs: Optional[Array] = None) -> Tuple[Array, List[Error]]:
        """Estimate approximate Bertrand-Nash prices under the assumption that shares and their price derivatives are
        unaffected by firm ID changes. By default, use unchanged firm IDs and compute marginal costs.
        """
        errors: List[Error] = []
        if costs is None:
            costs, errors = self.compute_costs()
        ownership_matrix = self.get_ownership_matrix(firms_index)
        eta, eta_errors = self.compute_eta(ownership_matrix)
        errors.extend(eta_errors)
        prices = costs + eta
        return prices, errors

    def compute_prices(
            self, iteration: Iteration, firms_index: int = 0, prices: Optional[Array] = None,
            costs: Optional[Array] = None) -> Tuple[Array, List[Error]]:
        """Estimate Bertrand-Nash prices. By default, use unchanged firm IDs, use unchanged prices as starting values,
        and compute marginal costs.
        """
        errors: List[Error] = []
        if costs is None:
            costs, errors = self.compute_costs()

        # configure NumPy to identify floating point errors
        with np.errstate(divide='call', over='call', under='ignore', invalid='call'):
            np.seterrcall(lambda *_: errors.append(exceptions.BertrandNashPricesFloatingPointError()))
            prices, converged = self.compute_bertrand_nash_prices(costs, iteration, firms_index, prices)[:2]

        # determine whether the fixed point converged
        if not converged:
            errors.append(exceptions.BertrandNashPricesConvergenceError())
        return prices, errors

    def compute_shares(self, prices: Optional[Array] = None) -> Tuple[Array, List[Error]]:
        """Estimate shares evaluated at specified prices. By default, use unchanged prices."""
        if prices is None:
            prices = self.products.prices
        delta = self.update_delta_with_variable('prices', prices)
        mu = self.update_mu_with_variable('prices', prices)
        shares = self.compute_probabilities(delta, mu) @ self.agents.weights
        return shares, []

    def compute_hhi(self, firms_index: int = 0, shares: Optional[Array] = None) -> Tuple[Array, List[Error]]:
        """Estimate HHI. By default, use unchanged firm IDs and shares."""
        if shares is None:
            shares = self.products.shares
        firm_ids = self.products.firm_ids[:, [firms_index]]
        hhi = 1e4 * sum((shares[firm_ids == f].sum() / shares.sum())**2 for f in np.unique(firm_ids))
        return hhi, []

    def compute_markups(
            self, prices: Optional[Array] = None, costs: Optional[Array] = None) -> Tuple[Array, List[Error]]:
        """Estimate markups. By default, use unchanged prices and compute marginal costs."""
        errors: List[Error] = []
        if prices is None:
            prices = self.products.prices
        if costs is None:
            costs, errors = self.compute_costs()
        markups = (prices - costs) / prices
        return markups, errors

    def compute_profits(
            self, prices: Optional[Array] = None, shares: Optional[Array] = None, costs: Optional[Array] = None) -> (
            Tuple[Array, List[Error]]):
        """Estimate population-normalized gross expected profits. By default, use unchanged prices, use unchanged
        shares, and compute marginal costs.
        """
        errors: List[Error] = []
        if prices is None:
            prices = self.products.prices
        if shares is None:
            shares = self.products.shares
        if costs is None:
            costs, errors = self.compute_costs()
        profits = (prices - costs) * shares
        return profits, errors

    def compute_consumer_surplus(self, prices: Optional[Array] = None) -> Tuple[Array, List[Error]]:
        """Estimate population-normalized consumer surplus. By default, use unchanged prices."""
        if prices is None:
            delta = self.delta
            mu = self.mu
        else:
            delta = self.update_delta_with_variable('prices', prices)
            mu = self.update_mu_with_variable('prices', prices)
        if self.K2 == 0:
            mu = 0

        # compute the exponentiated utilities that will be summed in the expression for consume surplus
        exp_utilities = np.exp(delta + mu)
        if self.H > 0:
            exp_utilities = self.groups.sum(exp_utilities**(1 / (1 - self.rho)))**(1 - self.group_rho)

        # compute the derivatives of utility with respect to prices, which are assumed to be constant across products
        alpha = -self.compute_utility_derivatives('prices')[0]

        # compute consumer surplus
        consumer_surplus = (np.log1p(exp_utilities.sum(axis=0)) / alpha) @ self.agents.weights
        return consumer_surplus, []
