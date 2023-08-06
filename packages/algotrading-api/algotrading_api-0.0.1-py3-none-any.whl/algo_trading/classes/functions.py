"""
This module contains the functions used throughout the package.
"""
import matplotlib.dates as dates
import numpy as np
import statsmodels.api as sm

# ANALYSIS FUNCTIONS

def _cum_returns(asset):
    """
    Returns the cumulative returns of an asset.
    """
    return (asset - asset[0]) / asset[0]

def _daily_returns(asset):
    """
    Returns the daily returns of an asset.
    """
    return asset.pct_change().dropna()

def _sharpe(portfolio_daily_returns, num_periods):
    """
    Calculates annualised sharpe ratio assuming risk free rate of 0.
    
    Parameters
    ----------
    portfolio_daily_returns : pd.Series
    num_periods : int
        Number of periods in one trading year.
        
    """
    return (np.sqrt(num_periods) * portfolio_daily_returns.mean() 
            / portfolio_daily_returns.std())

def _alpha_beta(portfolio_daily_returns, benchmark_daily_returns):
    """
    Used to find the alpha and beta of the strategy.
    """
    model = sm.OLS(portfolio_daily_returns, 
                   sm.add_constant(benchmark_daily_returns)).fit()
    return (model.params[0], model.params[1])   

# RECORDING FUNCTIONS
    
def _portfolio_value(obj):
    """
    Used to calculate portfolio value at an instant in time.
    """
    portfolio = 0
    for name, asset in obj.positions.items():
        if name != 'cash':
            portfolio += (obj.history.
                                loc[(obj.date, name)]['Close'] 
                                * asset.quantity)
        else:
            portfolio += asset.quantity
    return portfolio

def _record_portfolio(obj):
    """
    Used to record portfolio value during the simulation.
    """
    obj.portfolio[obj.date] = _portfolio_value(obj)

def _record_long_short(obj):
    """
    Used to calculate the total value of long and short positions each day.
    """
    poss = {'long' : 0, 'short' : 0}
    for name, asset in obj.context.positions.items():
        if name != 'cash':
            pos = 'long' if asset.quantity > 0 else 'short'
            poss[pos] += (obj.context.history.loc[(obj.context.date, name)]
            ['Close']* asset.quantity)
    for label, var in zip(['date', 'long', 'short'], [obj.context.date, 
                          poss['long'], poss['short']]):
        obj.context.long_short[label].append(var)
        
# HELPER FUNCTIONS

def _format_ts_ax(ax, start_date, end_date):
    """
    Used to format time series axes produced from the backtest.
    """
    ax.grid(True)
    simulation_length = (end_date - start_date).days
    ax.set_xlim(left=start_date, right=end_date)
    if (simulation_length < 20):
        ax.xaxis.set_major_locator(dates.DayLocator())
        ax.xaxis.set_major_formatter(dates.DateFormatter('%d-%m'))
    elif (simulation_length < 100):
        ax.xaxis.set_major_locator(dates.WeekdayLocator())
        ax.xaxis.set_major_formatter(dates.DateFormatter('%d-%m'))
    else:
        ax.xaxis.set_minor_locator(dates.MonthLocator())
        ax.xaxis.set_major_locator(dates.YearLocator())
        ax.xaxis.set_major_formatter(dates.DateFormatter('%Y'))
        