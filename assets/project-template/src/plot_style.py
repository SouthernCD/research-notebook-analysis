"""Shared Matplotlib defaults for project figures; apply explicitly at initialization."""

import matplotlib.pyplot as plt


def set_plot_style():
    """
    Apply the user's shared base style to subsequent Matplotlib figures.

    Uses Arial text and custom math fonts, editable PDF/PS font type 42,
    a 6-by-6-inch default canvas, and consistent font sizes and line widths.
    Updates global rcParams; does not create, display, or save a figure.
    Importing this module alone does not apply the style.

    Individual figures may override size and layout while retaining the base
    typography and line styling. Arial must be available to the rendering kernel;
    otherwise Matplotlib may substitute another font.
    """
    # Figure size
    plt.rcParams['figure.figsize'] = (6, 6)

    # Text and mathematical typography
    plt.rcParams['pdf.fonttype'] = 42
    plt.rcParams['ps.fonttype'] = 42
    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.titlesize'] = 10
    plt.rcParams['axes.labelsize'] = 10
    plt.rcParams['xtick.labelsize'] = 9
    plt.rcParams['ytick.labelsize'] = 9
    plt.rcParams['mathtext.it'] = 'Arial:italic'
    plt.rcParams['mathtext.rm'] = 'Arial'
    plt.rcParams['mathtext.tt'] = 'Arial'
    plt.rcParams['mathtext.bf'] = 'Arial:bold'
    plt.rcParams['mathtext.cal'] = 'Arial'
    plt.rcParams['mathtext.sf'] = 'Arial'
    plt.rcParams['mathtext.fontset'] = 'custom'

    # Axis, tick, and line styling
    plt.rcParams['axes.linewidth'] = 1
    plt.rcParams['xtick.major.width'] = 1
    plt.rcParams['ytick.major.width'] = 1
    plt.rcParams['lines.linewidth'] = 1
    plt.rcParams['lines.color'] = '#000000'
