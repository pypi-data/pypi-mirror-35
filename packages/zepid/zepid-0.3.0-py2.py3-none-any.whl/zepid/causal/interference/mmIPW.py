#########################################
# Mixed Effect Model IPW
#########################################

import numpy as np
import pandas as pd
import statsmodels.api as sm

# TODO have it work
# TODO have different estimators (important for households of various sizes Basse & Feller 2018)
# TODO validate with R data
# TODO variance estimation
# TODO diagnostics


class InterferenceIPW:
    """IPW for interference settings. Described in Tchetgen Tchetgen and VanderWeele 2012, and Perez-Heydrich et al.
    2014.
    """
    print('InterferenceIPW is not supported yet')

    def __init__(self, df, idvar, group, treatment, outcome, allocations, stabilized=True, coverage_comparison=None):
        """stuff"""
        self.df = df.copy()
        self.ex = treatment
        self.ou = outcome
        self.id = idvar
        self.group = group
        self.stabilized = stabilized
        if coverage_comparison is None:
            self.alpha = np.mean(self.df[treatment])
        else:
            self.alpha = coverage_comparison
        self.alpha_star = allocations

    def fit(self):
        # Setting up allocations as needed
        comparison_allocation_j = self._pi_calc(alpha=self.alpha, exclude_j=False)
        comparison_allocation_n = self._pi_calc(alpha=self.alpha, exclude_j=True)

        # Getting predicted probabilities as needed
        mm = sm.BinomialBayesMixedGLM.from_formula('dead ~ art + male',
                                                   vc_formulas={'label': 'age0'}, data=self.df).fit_map()

        # estimating each of the corresponding functions
        for a in self.alpha_star:
            print(a)

    def _pi_calc(self, alpha, exclude_j=False):
        """
        Calculates the part of the numerator for Y^ipw_i as designated by pi(A; alpha) in Perez-Heydrich et al. 2014

        For estimating Y(alpha)

            pi(A_i ; alpha) = cumprod_j=1(alpha^A * (1-alpha)^(1-A))

        For estimating Y(a;alpha) need to exclude j from the calculation such that;

            pi(A_i,-j ; alpha) = cumprod_k=1,k!=j(alpha^A * (1-alpha)^(1-A))

        This is done by using that same process as before, but now we divide by the individual level (to cancel out that
        cumulative product including individual j
        """
        pf = self.df.copy()
        pf['i_alpha'] = alpha ** (pf['treatment']) * (1 - alpha) ** (1 - pf['treatment'])
        pf.groupby(self.group)['i_alpha'].prod().reset_index()
        pf = pd.merge(pf, pf.groupby(self.group)['i_alpha'].prod().rename('g_alpha').reset_index(),
                      left_on=self.group, right_on=self.group)

        if exclude_j:
            pi = pf['g_alpha'] / pf['i_alpha']
        else:
            pi = pf['g_alpha']
        return pi

    def _yipw_calc(self, denom, a=None):
        """
        This calculates the corresponding Y^ipw for each potential combination. The version used depends on if 'a' is
        specified

        Y^ipw_i(a; alpha) = (sum(pi(A_i,-j; alpha) * I(A=a) * Y^ij) / Pr(A_i|X_i; phi) * n_i

        Y^ipw_i(alpha) = (sum(pi(A_i; alpha) * Y^ij) / Pr(A_i|X_i; phi) * n_i
        """
        ni = self.df.groupby(self.group)[self.id].count()
        if a is None:
            self.df['raw_numerator'] = self.df['pi2'] * self.df[self.ou]
            numer = self.df.groupby(self.group)['raw_numerator'].sum()
            yipw = numer / (denom * ni)
        else:
            self.df['raw_numerator'] = self.df['pi1'] * np.where(self.df[self.ex]==treat, 1, 0) * self.df[self.ou]
            numer = self.df.groupby(self.group)['raw_numerator'].sum()
            yipw = numer / (denom * ni)
        return yipw

