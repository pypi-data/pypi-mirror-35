import h5py
from math import ceil
import numpy as np
from matplotlib import pyplot as plt

from ..interfaces import stan_utility
from ..interfaces.stan import Direction
from ..interfaces.integration import ExposureIntegralTable
from ..propagation.energy_loss import get_Eth_src, get_Eex, get_kappa_ex
from ..utils import PlotStyle
from ..plotting import AllSkyMap

__all__ = ['Results', 'PPC']


class Results():
    """
    Manage the output of Analysis object.
    """

    def __init__(self, filename):
        """
        Manage the output of Analysis object.
        Reads in a HDF5 file containting fit/simulation
        results for further plotting, analysis and PPC.
        """

        self.filename = filename


    def get_chain(self, list_of_keys):
        """
        Returns chain of desired parameters specified by list_of_keys.
        """

        chain = {}
        with h5py.File(self.filename, 'r') as f:
            fit_output = f['output/fit/samples']
            for key in list_of_keys:
                chain[key] = fit_output[key].value

        return chain

    def get_truths(self, list_of_keys):
        """
        For the case where the analysis was based on simulated 
        data, return input values or 'truths' for desired 
        parameters specified by list_of_keys.
        """

        truths = {}
        with h5py.File(self.filename, 'r') as f:

            try:
                sim_input = f['input/simulation']
                for key in list_of_keys:
                    truths[key] = sim_input[key].value

            except:
                print('Error: file does not contain simulation inputs.')
        return truths
    

    def traceplot(self, list_of_keys):
        """
        Plot the traceplot for parameters specified by list_of_keys.
        """
        return 0
    

    def summary(self):
        """
        Print a summary of the results.
        """
        return 0

    def get_fit_parameters(self):
        """
        Return mean values of all main fit parameters.
        """

        list_of_keys = ['B', 'alpha', 'L', 'F0']
        chain = self.get_chain(list_of_keys)

        fit_parameters = {}
        fit_parameters['B'] = np.mean(chain['B'])
        fit_parameters['alpha'] = np.mean(chain['alpha'])
        fit_parameters['F0'] = np.mean(chain['F0'])
        fit_parameters['L'] = np.mean(np.transpose(chain['L']), axis = 1)
        
        return fit_parameters
        
    def get_input_data(self):
        """
        Return fit input data.
        """

        fit_input = {}
        with h5py.File(self.filename, 'r') as f:
            fit_input_from_file = f['input/fit']
            for key in fit_input_from_file:
                fit_input[key] = fit_input_from_file[key].value
                
        return fit_input
    
    def run_ppc(self, stan_sim_file, N = 3):
        """
        Run N posterior predictive simulations.
        """

        fit_parameters = self.get_fit_parameters()
        input_data = self.get_input_data()
    
        self.ppc = PPC(stan_sim_file)
        
        self.ppc.simulate(fit_parameters, input_data, N = N)

    
    

class PPC():
    """
    Handles posterior predictive checks.
    """

    def __init__(self, stan_sim_file):
        """
        Handles posterior predictive checks.
        :param stan_sim_file: the stan file to use to run the simulation
        """
    
        # compile the stan model
        self.simulation = stan_utility.compile_model(stan_sim_file)

        self.arrival_direction_preds = []
        self.Edet_preds = []
                
        
    def simulate(self, fit_parameters, input_data, seed = None, N = 3):
        """
        Simulate from the posterior predictive distribution. 
        """

        self.alpha = fit_parameters['alpha']
        self.B = fit_parameters['B']
        self.F0 = fit_parameters['F0']
        self.L = fit_parameters['L']

        self.arrival_direction = Direction(input_data['arrival_direction'])
        self.Edet = input_data['Edet']
        self.Eth = input_data['Eth']
        
        # calculate eps integral
        print('precomputing exposure integrals...')
        # rescale to [Mpc]
        D = [(d / 3.086) * 100 for d in input_data['D']]
        self.Eth_src = get_Eth_src(input_data['Eth'], D)
        self.Eex = get_Eex(self.Eth_src, self.alpha)
        self.kappa_ex = get_kappa_ex(self.Eex, self.B, D)        
        
        varpi = input_data['varpi']
        params = input_data['params']
        self.ppc_table = ExposureIntegralTable(varpi = varpi, params = params)
        self.ppc_table.build_for_sim(self.kappa_ex, self.alpha, self.B, input_data['D'])
            
        eps = self.ppc_table.sim_table
        # convert scale for sampling
        eps = [e / 1000 for e in eps]
        
        # compile inputs 
        self.ppc_input = {
            'kappa_c' : input_data['kappa_c'],
            'Ns' : input_data['Ns'],
            'varpi' : input_data['varpi'],
            'D' : input_data['D'],
            'A' : input_data['A'][0],
            'a0' : input_data['a0'],
            'theta_m' : input_data['theta_m'],
            'alpha_T' : input_data['alpha_T'],
            'eps' : eps}
        
        self.ppc_input['B'] = self.B
        self.ppc_input['L'] = self.L
        self.ppc_input['F0'] = self.F0
        self.ppc_input['alpha'] = self.alpha
        
        self.ppc_input['Eth'] = input_data['Eth']
        self.ppc_input['Eerr'] = input_data['Eerr']
        self.ppc_input['Dbg'] = input_data['Dbg']

        for i in range(N):
            # run simulation
            print('running posterior predictive simulation(s)...')
            self.posterior_predictive = self.simulation.sampling(data = self.ppc_input, iter = 1,
                                                                 chains = 1, algorithm = "Fixed_param", seed = seed)
            # extract output
            arrival_direction = self.posterior_predictive.extract(['arrival_direction'])['arrival_direction'][0]
            arr_dir_pred = Direction(arrival_direction)
            self.arrival_direction_preds.append(arr_dir_pred)
            Edet_pred = self.posterior_predictive.extract(['Edet'])['Edet'][0]
            self.Edet_preds.append(Edet_pred)
            print(i, 'completed')


    def plot(self, ppc_type = None, cmap = None):
        """
        Plot the posterior predictive check against the data 
        (or original simulation) for ppc_type == 'arrival direction' 
        or ppc_type == 'energy'.
        """

        if ppc_type == None:
            ppc_type = 'arrival direction'

        # how many simulaitons
        N_sim = len(self.arrival_direction_preds)
        N_grid = N_sim + 1
        N_rows = ceil(np.sqrt(N_grid))
        N_cols = ceil(N_grid / N_rows)
            
        if ppc_type == 'arrival direction':

            # plot style
            if cmap == None:
                style = PlotStyle()
            else:
                style = PlotStyle(cmap_name = cmap)
            
            # figure
            fig, ax = plt.subplots(N_rows, N_cols, figsize = (5 * N_rows, 4 * N_cols))
            flat_ax = ax.reshape(-1)
                                   
            # skymap
            skymap = AllSkyMap(projection = 'hammer', lon_0 = 0, lat_0 = 0);
                                   
            for i, ax in enumerate(flat_ax):

                if i < N_grid:
                    # data
                    if i == 0:
                        skymap.ax = ax
                        label = True
                        for lon, lat in np.nditer([self.arrival_direction.lons, self.arrival_direction.lats]):
                            if label:
                                skymap.tissot(lon, lat, 4.0, npts = 30, alpha = 0.5, label = 'data')
                                label = False
                            else:
                                skymap.tissot(lon, lat, 4.0, npts = 30, alpha = 0.5)
                  
                    # predicted
                    else:
                        skymap.ax = ax
                        label = True
                        for lon, lat in np.nditer([self.arrival_direction_preds[i - 1].lons, self.arrival_direction_preds[i - 1].lats]):
                            if label: 
                                skymap.tissot(lon, lat, 4.0, npts = 30, alpha = 0.5,
                                              color = 'g', label = 'predicted')
                                label = False
                            else:
                                skymap.tissot(lon, lat, 4.0, npts = 30, alpha = 0.5, color = 'g')
                else:
                    ax.axis('off')
                            
        if ppc_type == 'energy':

            bins = np.logspace(np.log(self.Eth), np.log(1e4), base = np.e)

            # figure
            fig, ax = plt.subplots(N_rows, N_cols, figsize = (5 * N_rows, 4 * N_cols))
            flat_ax = ax.reshape(-1)

            for i, ax in enumerate(flat_ax):

                if i < N_grid:

                    if i == 0:
                        ax.hist(self.Edet, bins = bins, alpha = 0.7, label = 'data', color = 'k')
                        ax.set_xscale('log')
                        ax.set_yscale('log')
                        ax.get_yaxis().set_visible(False)
                    else:
                        ax.hist(self.Edet_preds[i - 1], bins = bins, alpha = 0.7, label = 'predicted', color = 'g')
                        ax.set_xscale('log')
                        ax.set_yscale('log')
                        ax.get_yaxis().set_visible(False)
                        
                else:
                    ax.axis('off')
