"""
This module contains functions which are used throughout the package.
"""
from algo_trading.backtests.info import dev
from algo_trading.backtests.classes import Simulation, Backtest
import pandas as pd
from datetime import datetime
from termcolor import colored

def run_algorithm(start_date, end_date, algorithm, data, capital_base, 
                  setup=None, benchmark=None, num_periods=252):
    """
    Initiates backtest of a trading algorithm.
    
    PARAMETERS
    ----------
    start_date : str
        Must have format '%Y-%m-%d'.
    end_date : str
        Must have format '%Y-%m-%d'.
    algorithm : function
        The algorithm to backtest. Must accept context object as parameter.
    setup : function
        Runs before the simulation starts. Used to initially bind attributes to
        context.
    data : pd.DataFrame
        All available data to be used for the simulation. Use ingest_data
        function to create this from many DataFrames containg time series 
        information.
    capital_base : float
        The capital base to use for the simulation.
    benchmark : str
        The benchmark to use during the simulation. It must be the name of
        the benchmark as used in `data`.
    num_periods : int
        If there is data for every day in the year, num_periods = 365; if 
        there is data for all trading days, num_periods = 252.
    
    RETURNS
    -------
    Backtest        
    """
    if dev:
        print ('\n\nSTARTING BACKTEST')
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    simulation = Simulation(capital_base, start_date, end_date, data, 
                            benchmark, num_periods)
    if setup is not None:
        setup(simulation.context)
    while simulation.context.date <= end_date:
        if dev:
            print (colored('\n\nDATE:', 'cyan'))
            print (datetime.strftime(simulation.context.date, '%Y-%m-%d'))
            print (colored('ORDERS:', 'cyan'))
        # only run algorithm if trading day  
        if simulation.context.date in simulation.storage.data.index.levels[0]:
            algorithm(simulation.context)        
            simulation.record_default_vars()
        if dev:
            print (colored('POSITIONS:', 'cyan'))
            for asset in simulation.context.positions.values():
                print (asset.name + ': ' + str(round(asset.quantity, 2)))
            print (colored('PORTFOLIO VALUE:', 'cyan'))
            print (round(simulation.context.portfolio[simulation.context.date], 
                         2))
        simulation.next_day()
    if dev:
        print ('\n\nBACKTEST COMPLETE')
    simulation.freeze_vars()
    return(Backtest(simulation.context))
    
def ingest_data(data):
    """
    This function takes in many OHLC DataFrames and returns a comprehensive 
    MultiIndex DataFrame.
    
    PARAMETERS
    ----------
    data : dict
        A dictionary of the form {'asset1' : asset1_df, 
                                  'asset2' : asset2_df ...}
    
    RETURNS
    -------
    pandas DataFrame
    """
    num_assets = len(data)
    data = pd.concat(data).swaplevel().sort_index()
    data.index.names = ['Date', 'Asset']
    data = data.groupby(level=0).filter(lambda x: len(x) == num_assets)
    data.index = data.index.remove_unused_levels()
    return data