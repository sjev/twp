"""
Common code for reuse in notebooks
"""


def systemInfo():
    """ print versions of most important modules """
    import imp

    modules = ['tradingWithPython','pandas','ibapi','ib']
    
    
    for name in modules:
        print(5*'-',name,5*'-')
        try:
            result = imp.find_module(name)
        except ImportError as e:
            print(e)
            continue
            
        pkg = imp.load_module(name,*result)
        print('Version: ',pkg.__version__)
        print('Location:', pkg.__file__)

def prettifyNotebook(figsize=[8,6], max_rows=10, precision=2):
    """
    cosmetic tweaks to make notebook look pretty
    """
    import matplotlib.pyplot as plt
    plt.style.use('ggplot')

    # bigger fitures
    import matplotlib
    matplotlib.rcParams['figure.figsize'] = figsize

    # limint number of rows shown by pandas
    import pandas as pd
    pd.options.display.max_rows = max_rows

    # set two-digit precision, we usually don't need more for financial data
    pd.options.display.precision = precision


if __name__=="__main__":
    #systemInfo()
    prettifyNotebook()
