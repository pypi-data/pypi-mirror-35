"""
This module contains algotrading classes which the client need not access.
"""
from algo_trading.backtests.info import dev, figsize
from algo_trading.backtests.functions import (_cum_returns, 
                                             _daily_returns, 
                                             _alpha_beta, 
                                             _sharpe, 
                                             _portfolio_value, 
                                             _record_portfolio, 
                                             _record_long_short,
                                             _format_ts_ax)
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from datetime import timedelta

# change styling of matplotlib graphs
plt.rc('font', size=14)   
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10) 

class Asset:
    """
    Used to create new assets at the beginning of the simulation.
    """
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        
class Storage:
    """
    Holds simulation data which the algorithm must not have access to.
    """
    def __init__(self, start_date, end_date, data):
        self.start_date = start_date
        self.end_date = end_date
        self.data = data
               
class Context:
    """
    Is passed to the algorithm at the start of each day during the simulation.
    """
    def __init__(self, assets, start_date, capital_base, benchmark, 
                 num_periods):
        self.benchmark = benchmark
        self.num_periods = num_periods
        self.capital_base = capital_base
        self.start_date = start_date
        self.date = start_date
        self.positions = {'cash': Asset('cash', capital_base)}
        self.portfolio = {}
        self.transactions = {'date' : [], 'asset' : [], 'quantity' : [], 
                             'price' : [], 'value' : []} 
        self.long_short = {'date' : [], 'long' : [], 'short': []} 
        self.assets = assets
        self.recorded_vars = {}
    def order(self, order_type, name, amount=None):
        """
        Allows you to order a quantity of an item.
        
        Parameters
        ----------
        order_type : str{'value', 'quantity', 'zero'}
            If 'value', amount refers to value; else it refers to quantity.
        name : str
            The name of the asset you want to order.
        quantity : float
            The quantity of the asset you want to order.        
        """
        price = self.history.loc[(self.date, name)]['Close']
        if order_type == 'value':
            quantity = amount / float(price)
        elif order_type == 'quantity':
            quantity = amount
        elif order_type == 'zero':
            if name in self.positions:
                quantity = -self.positions[name].quantity
            else:
                quantity = 0
        self.positions['cash'].quantity -= (quantity * price)
        if name not in self.positions:
            self.positions[name] = (self.assets[name])
            self.positions[name].quantity = quantity
        else:
            self.positions[name].quantity += quantity
        for label, var in zip(['date', 'asset', 'quantity', 'price', 'value'], 
                             [self.date, name, quantity, price, 
                              price*quantity]):
            self.transactions[label].append(var)
        if self.positions[name].quantity == 0:
            self.positions.pop(name)
        if dev:
            print (str(round(quantity, 2)) + ' ' + name + ' @ ' + 
                   str(round(price, 2)))        
    def record_vars(self, to_record):
        """
        Allows you to record variables during the simulation.
        
        Parameters
        ----------
        to_record : dict
            to_record should have the form {'var1' : value1, 'var2' : value2 ...}
        """
        for var in to_record:
            if var not in self.recorded_vars:
                self.recorded_vars[var] = {}
            self.recorded_vars[var][self.date] = to_record[var]
    def portfolio_value(self):
        """
        Returns current portfolio value.
        """
        return _portfolio_value(self)
                      
class Simulation:
    """
    Simulation stores information relating to the simulation.
    """
    def __init__(self, capital_base, start_date, end_date, data, benchmark, 
                 num_periods):
        self.storage = Storage(start_date, end_date, data)
        self.context = (Context({name : Asset(name, 0) for name in 
                                 self.storage.data.index.levels[1].unique()}, 
        start_date, capital_base, benchmark, num_periods))
        self.get_history()
    def get_history(self):
        """
        Passes currently available data to the algorithm.
        """
        self.context.history = (self.storage.data.loc[:self.context.date])
    def record_default_vars(self):
        """
        Records default simulation values.
        
        NOTES
        -----
        At the moment, we simply record the value of the portfolio each day.
        """
        _record_portfolio(self.context)
        _record_long_short(self)
    def freeze_vars(self):
        """
        Generates statistics from recorded variables to pass to Backtest and
        freezes recorded variables into DataFrames.
        """
        # TODO do we need first two lines here? 
        for var, records in self.context.recorded_vars.items():
            self.context.recorded_vars[var] = (pd.Series(records))
        if len(self.context.recorded_vars) != 0:
            self.context.recorded_vars = pd.concat(self.context.recorded_vars, 
                                                  axis=1)
        self.context.transactions = (pd.DataFrame(self.context.transactions).
                                     set_index(['date', 'asset']))
        self.context.long_short = (pd.DataFrame(self.context.long_short).
                                   set_index('date'))
        self.context.portfolio = pd.Series(self.context.portfolio)
        self.context.end_date = self.storage.end_date
        if self.context.benchmark is not None:
            self.context.benchmark = (self.storage.data.
                                      xs(self.context.benchmark, level=1).
                                      loc[self.storage.start_date : 
                                          self.storage.end_date]['Close'])      
    def next_day(self):
        """
        Moves the simulation onto the next day and updates the data available
        to the algorithm.
        """
        self.context.date += timedelta(days=1)
        self.get_history()
                          
class Analysis:
    """
    Here we store the key performance metrics of the backtest.
    """
    def __init__(self, recorded_vars, transactions, long_short, portfolio, 
                 num_periods):
        self.recorded_vars = recorded_vars
        self.transactions = transactions
        self.portfolio = portfolio
        self.portfolio_cum_returns = _cum_returns(portfolio)
        self.portfolio_daily_returns = _daily_returns(portfolio)
        self.sharpe = _sharpe(self.portfolio_daily_returns, num_periods)
        self.daily_long_short = (self.transactions.groupby(level=0)['value'].
                                 agg({'long' : lambda x : x[x > 0].sum(),
                                      'short' : lambda x : x[x < 0].sum()}))
        self.cum_long_short = long_short
        self.leverage = ((self.cum_long_short['long'] + 
                         abs(self.cum_long_short['short']))/
    self.portfolio)
        self.data = pd.concat({'portfolio' : 
                                   self.portfolio, 
                               'portfolio_cum_returns' : 
                                   self.portfolio_cum_returns, 
                               'portfolio_daily_returns' : 
                                   self.portfolio_daily_returns, 
                               'daily_long' : self.daily_long_short['long'],
                               'daily_short' : self.daily_long_short['short'],
                               'cum_long' : self.cum_long_short['long'], 
                               'cum_short' : self.cum_long_short['short'], 
                               'leverage' : self.leverage}, 
    axis=1)
        if type(recorded_vars) != dict:
            self.data = self.data.join(self.recorded_vars)
        self.data.fillna(0)
            

class BenchmarkAnalysis(Analysis):
    """
    Extra analysis available if there is a benchmark.
    """
    def __init__(self, recorded_vars, transactions, long_short, 
                 portfolio, benchmark, num_periods):
        (super().__init__(recorded_vars, transactions, 
         long_short, portfolio, num_periods))
        self.benchmark = benchmark
        self.benchmark_cum_returns = _cum_returns(benchmark)
        self.benchmark_daily_returns = _daily_returns(benchmark)
        self.alpha, self.beta = _alpha_beta(self.portfolio_daily_returns, 
                                            self.benchmark_daily_returns)
        
        self.data = (self.data.join(pd.DataFrame({'benchmark' : 
            self.benchmark, 'benchmark_cum_returns' : 
                self.benchmark_cum_returns, 'benchmark_daily_returns' : 
                    self.benchmark_daily_returns})).fillna(0))
            
class Plot:
    def __init__(self, data, start_date, end_date):
        # TODO is there a better way to hide these attributes?
        self._data = data
        self._start_date = start_date
        self._end_date = end_date
    def portfolio_cum_returns(self):
        """
        Plots the portfolio cumulative returns from the backtest.
        """
        fig, ax = plt.subplots(figsize=figsize)
        ax.plot(self._data['portfolio_cum_returns']*100, label='Portfolio')
        ax.set_title('Returns')
        _format_ts_ax(ax, self._start_date, self._end_date)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: 
            '{:.1f}%'.format(y)))
        return ax
    def recorded_vars(self, var):
        """
        Plots the recorded vars from the backtest.
        """
        if var not in self._data.columns:
            raise ValueError(var + ' not recorded')
        fig, ax = plt.subplots(figsize=figsize)
        ax.plot(self._data[var], label=var)
        ax.set_title(var)
        _format_ts_ax(ax, self._start_date, self._end_date)
        return ax
    def daily_long_short(self):
        """
        Plots daily long and short positions from the backtest.
        """
        fig, ax = plt.subplots(figsize=figsize)
        ax.plot(self._data['daily_long'])
        ax.plot(self._data['daily_short'])
        ax.set_title('Daily Long Short')
        _format_ts_ax(ax, self._start_date, self._end_date)
        return ax
    def cum_long_short(self):
        """
        Plots cumulative long and short positions from the backtest.
        """
        fig, ax = plt.subplots(figsize=figsize)
        ax.plot(self._data['cum_long'])
        ax.plot(self._data['cum_short'])
        ax.set_title('Cumulative Long Short')
        _format_ts_ax(ax, self._start_date, self._end_date)
        return ax
    def leverage(self):
        """
        Plots the leverage accrued during the backtest.
        """
        fig, ax = plt.subplots(figsize=figsize)
        ax.plot(self._data['leverage'])
        ax.set_title('Leverage')
        _format_ts_ax(ax, self._start_date, self._end_date)
        return ax
        
class BenchmarkPlot(Plot):
    def __init__(self, data, alpha, beta, start_date, end_date):
        super().__init__(data, start_date, end_date)
        self._alpha = alpha
        self._beta = beta
    def portfolio_cum_returns(self):
        fig = super().portfolio_cum_returns()
        fig.axes.plot(self._data['benchmark_cum_returns'] * 100, 
                      label='Benchmark')
        fig.axes.legend()
        return fig.axes
    def CAPM_scatter(self):
        fig, ax = plt.subplots(figsize=figsize)
        x_min = self._data['benchmark_daily_returns'].min()
        x_max = self._data['benchmark_daily_returns'].max()
        ax.scatter(self._data['benchmark_daily_returns'], 
                   self._data['portfolio_daily_returns'])
        ax.plot([x_min, x_max], [self._alpha + self._beta*x_min, 
                self._alpha + self._beta*x_max])
        ax.set_title('CAPM Scatter')
        ax.set_xlabel('Benchmark Returns')
        ax.set_ylabel('Portfolio Returns')
        ax.grid(True)
        return ax
    
class Backtest:
    """
    A backtest object is returned by run_algorithm. It stores key performance
    metrics of the backtest and may be used to quickly plot graphs.
    """
    def __init__(self, context):
        if context.benchmark is not None:
            self.analysis = BenchmarkAnalysis(context.recorded_vars, 
                                     context.transactions,
                                     context.long_short,
                                     context.portfolio, 
                                     context.benchmark, 
                                     context.num_periods)
            self.plot = BenchmarkPlot(self.analysis.data, 
                                      self.analysis.alpha,
                                      self.analysis.beta,
                                      context.start_date, 
                                      context.end_date)
        else:
            self.analysis = Analysis(context.recorded_vars, 
                                     context.transactions,
                                     context.long_short,
                                     context.portfolio, 
                                     context.num_periods)
            self.plot = Plot(self.analysis.data,
                             context.start_date, 
                             context.end_date)