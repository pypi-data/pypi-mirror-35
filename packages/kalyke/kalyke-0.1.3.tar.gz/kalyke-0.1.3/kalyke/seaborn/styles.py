# -*- coding: utf-8 -*-

"""Some default styling for seaborn."""

class Line:
    """Some seaborn line styles."""

    red = {
        'scatter_kws': {'color':'coral', 's':200, 'alpha': 0.5},
        'line_kws': {'color': 'coral', 'lw': 2}
    }

    blue = {
        'scatter_kws': {'color':'cornflowerblue', 's':200, 'alpha': 0.5},
        'line_kws': {'color': 'cornflowerblue', 'lw': 2}
    }

    green = {
        'scatter_kws': {'color':'green', 's':200, 'alpha': 0.5},
        'line_kws': {'color': 'green', 'lw': 2}
    }

    black = {
        'scatter_kws': {'color':'k', 's':120000, 'alpha': 0.5},
        'line_kws': {'color': 'k', 'lw': 2, 'ls': '--'}
    } 
