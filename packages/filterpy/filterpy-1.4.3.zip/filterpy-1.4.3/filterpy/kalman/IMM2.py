# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 07:53:34 2018

@author: rlabbe
"""
from __future__ import (absolute_import, division)
import numpy as np
from filterpy.common import pretty_str

class IMMEstimator2(object):
    """ Implements an Interacting Multiple-Model (IMM) estimator.

    Parameters
    ----------

    filters : (N,) array_like of KalmanFilter objects
        List of N filters. filters[i] is the ith Kalman filter in the
        IMM estimator.

        Each filter must have the same dimension for the state `x` and `P`.


    mu : (N,) ndarray of float
        mode probability: mu[i] is the probability that
        filter i is the correct one.

    M : (N,N) ndarray of float
        Markov chain transition matrix. M[i,j] is the probability of
        switching from filter j to filter i.

    Attributes
    ----------
    x : numpy.array(dim_x, 1)
        Current state estimate. Any call to update() or predict() updates
        this variable.

    P : numpy.array(dim_x, dim_x)
        Current state covariance matrix. Any call to update() or predict()
        updates this variable.

    N : int
        number of filters in the filter bank

    mu : (N,) ndarray of float
        mode probability: mu[i] is the probability that
        filter i is the correct one.

    M : (N,N) ndarray of float
        Markov chain transition matrix. M[i,j] is the probability of
        switching from filter j to filter i.


    cbar   - total probaiblity?

    likelihood
    omega


    Examples
    --------

    See my book Kalman and Bayesian Filters in Python
    https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python


    References
    ----------

    Bar-Shalom, Y., Li, X-R., and Kirubarajan, T. "Estimation with
    Application to Tracking and Navigation". Wiley-Interscience, 2001.

    Crassidis, J and Junkins, J. "Optimal Estimation of
    Dynamic Systems". CRC Press, second edition. 2012.

    Labbe, R. "Kalman and Bayesian Filters in Python".
    https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python
    """

    def __init__(self, filters, mu, M, x0, P0):
        """"
        Create an IMM estimator from a list of filters.

        """

        if len(filters) < 1:
            raise ValueError('filters must contain at least one filter')

        self.filters = filters
        self.mu = np.asarray(mu) / np.sum(mu)
        self.trans = M

        x_shape = filters[0].x.shape
        for f in filters:
            if x_shape != f.x.shape:
                raise ValueError(
                        'All filters must have the same state dimension')

        self.x = x0.copy()
        self.P = P0.copy()
        self.N = len(filters)  # number of filters

        # cbar is the total probability, after interaction,
        # that the target is in state j. We use it as the
        # normalization constant.
        self.cbar = np.dot(self.mu, self.trans)
        self.likelihood = np.zeros(self.N)
        self.omega = np.zeros((self.N, self.N))
        self._compute_mixing_probabilities()

    def update(self, z, u=None):
        """
        Add a new measurement (z) to the Kalman filter. If z is None, nothing
        is changed.

        Parameters
        ----------

        z : np.array
            measurement for this update.

        u : np.array, optional
            u[i] contains the control input for the ith filter
        """
        # pylint: disable=too-many-locals

        # each element j = sum M_ij * mu_i

        # run update on each filter, and save the likelihood
        for i, f in enumerate(self.filters):
            f.update(z)
            self.likelihood[i] = f.likelihood

        # update mode probabilities from total probability * likelihood
        self.mu = self.cbar * self.likelihood
        self.mu /= np.sum(self.mu)  # normalize

        self._compute_mixing_probabilities()

        # compute mixed IMM state and covariance
        self.x.fill(0.)
        self.P.fill(0.)

        for f, mu in zip(self.filters, self.mu):
            self.x += f.x * mu

        for f, mu in zip(self.filters, self.mu):
            y = f.x - self.x
            self.P += mu * (np.outer(y, y) + f.P)

    def predict(self, us=None):
        x_js = []
        P_js = []

        # compute mixed initial conditions
        for j, f_j in enumerate(self.filters):
            x_j = np.zeros(self.x.shape)
            P_j = np.zeros(self.P.shape)

            for i, f_i in enumerate(self.filters):
                w = self.omega[i, j]
                x_j += w * f_i.x

            for i, f_i in enumerate(self.filters):
                w = self.omega[i, j]
                y = f_i.x - x_j
                # use outer in case y is 1D array
                P_j += w * (f_i.P + np.outer(y, y))
            x_js.append(x_j)
            P_js.append(P_j)

        # propagate using the mixed initial conditions
        for j, f_j in enumerate(self.filters):
            f_j.x = x_js[j].copy()
            f_j.P = P_j[j].copy()
            if us is not None:
                f_j.predict(us[i])
            else:
                f_j.predict()

    def _compute_mixing_probabilities(self):
        self.cbar = np.dot(self.mu, self.trans)

        for i in range(self.N):
            for j in range(self.N):
                self.omega[i, j] = (self.trans[i, j]*self.mu[i]) / self.cbar[j]

    def __repr__(self):
        return '\n'.join([
            'IMMEstimator object',
            pretty_str('N', self.N),
            pretty_str('x', self.x),
            pretty_str('P', self.P),
            pretty_str('mu', self.mu),
            pretty_str('M', self.trans),
            pretty_str('cbar', self.cbar),
            pretty_str('likelihood', self.likelihood),
            ])


if __name__ == '__main__':
    r = 100.
    dt = 1.
    phi_sim = np.array(
        [[1, dt, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 1, dt],
         [0, 0, 0, 1]])

    gam = np.array([[dt**2/2, 0],
                    [dt, 0],
                    [0, dt**2/2],
                    [0, dt]])

    x = np.array([[2000, 0, 10000, -15.]]).T

    simxs = []
    N = 600
    for i in range(N):
        x = np.dot(phi_sim, x)
        if i >= 400:
            x += np.dot(gam, np.array([[.075, .075]]).T)
        simxs.append(x)
    simxs = np.array(simxs)

    zs = np.zeros((N, 2))
    zs[0, 0] = 2000
    zs[0, 1] = 10000
    for i in range(1, len(zs)):
        zs[i, 0] = simxs[i-1, 0] # + randn()*r
        zs[i, 1] = simxs[i-1, 2] # + randn()*r

    try:
        #data to test against crassidis' IMM matlab code
        zs_tmp = np.genfromtxt('c:/users/rlabbe/dropbox/Crassidis/mycode/xx.csv', delimiter=',')[:-1]
        zs = zs_tmp
    except:
        pass

    from filterpy.kalman import KalmanFilter

    ca = KalmanFilter(6, 2)
    cano = KalmanFilter(6, 2)
    dt2 = (dt**2)/2
    ca.F = np.array(
        [[1, dt, dt2, 0, 0,  0],
         [0, 1,  dt,  0, 0,  0],
         [0, 0,   1,  0, 0,  0],
         [0, 0,   0,  1, dt, dt2],
         [0, 0,   0,  0,  1, dt],
         [0, 0,   0,  0,  0,  1]])
    cano.F = ca.F.copy()

    ca.x = np.array([[2000., 0, 0, 10000, -15, 0]]).T
    cano.x = ca.x.copy()

    ca.P *= 1.e-12
    cano.P *= 1.e-12
    ca.R *= r**2
    cano.R *= r**2
    cano.Q *= 0
    q = np.array([[.05, .125, 1/6],
                 [.125, 1/3, .5],
                 [1/6, .5, 1]])*1.e-3

    ca.Q[0:3, 0:3] = q
    ca.Q[3:6, 3:6] = q

    ca.H = np.array([[1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0]])
    cano.H = ca.H.copy()

    filters = [ca, cano]
    trans = np.array([[0.97, 0.03],
                      [0.03, 0.97]])

    imm = IMMEstimator2(filters, (0.5, 0.5), trans, ca.x, ca.P)

    xs, probs = [], []
    cvxs, caxs = [], []
    from filterpy.common import Saver
    s = Saver(imm)
    for i, z in enumerate(zs):
        z = np.array([z]).T
        if i > 0:
            imm.predict()

        imm.update(z)
        imm.predict()

        xs.append(imm.x.copy())
        s.save()
    s.to_array()

    xs = np.array(xs)
    cvxs = np.array(cvxs)
    caxs = np.array(caxs)
    probs = np.array(probs)
    import matplotlib.pyplot as plt

    #plt.subplot(121)
    plt.plot(xs[:, 0], xs[:, 3], 'k')
    plt.scatter(zs[:, 0], zs[:, 1], marker='+', alpha=0.6)

    '''plt.subplot(122)
    plt.plot(probs[:, 0])
    plt.plot(probs[:, 1])
    plt.ylim(-1.5, 1.5)
    plt.title('probability ratio p(cv)/p(ca)')'''


