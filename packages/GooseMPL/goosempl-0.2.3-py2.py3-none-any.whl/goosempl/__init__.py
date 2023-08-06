'''
This module provides some extensions to matplotlib.

:dependencies:

  * numpy
  * matplotlib

:copyright:

  | Tom de Geus
  | tom@geus.me
  | http://www.geus.me
'''

# ==================================================================================================

import matplotlib.pyplot as plt
import matplotlib        as mpl
import numpy             as np
import os,re,sys

# ==================================================================================================

def find_latex_font_serif():
  r'''
Find an available font to mimic LaTeX.
  '''

  import os, re
  import matplotlib.font_manager

  name = lambda font: os.path.splitext(os.path.split(font)[-1])[0].split(' - ')[0]

  fonts = matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf')

  matches = [
    r'.*Computer\ Modern\ Roman.*',
    r'.*CMU\ Serif.*',
    r'.*CMU.*',
    r'.*Times.*',
    r'.*DejaVu.*',
    r'.*Serif.*',
  ]

  for match in matches:
    for font in fonts:
      if re.match(match,font):
        return name(font)

# --------------------------------------------------------------------------------------------------

def copy_style():
  r'''
Write all goose-styles to the relevant matplotlib configuration directory.
  '''

  import os
  import matplotlib

  # style definitions
  # -----------------

  styles = {}

  styles['goose.mplstyle'] = '''
figure.figsize       : 8,6
font.weight          : normal
font.size            : 16
axes.labelsize       : medium
axes.titlesize       : medium
xtick.labelsize      : small
ytick.labelsize      : small
xtick.top            : True
ytick.right          : True
axes.facecolor       : none
axes.prop_cycle      : cycler('color',['k', 'r', 'g', 'b', 'y', 'c', 'm'])
legend.fontsize      : medium
legend.fancybox      : true
legend.columnspacing : 1.0
legend.handletextpad : 0.2
lines.linewidth      : 2
image.cmap           : afmhot
image.interpolation  : nearest
image.origin         : lower
savefig.facecolor    : none
figure.autolayout    : True
errorbar.capsize     : 2
  '''

  styles['goose-tick-in.mplstyle'] = '''
xtick.direction      : in
ytick.direction      : in
  '''

  styles['goose-tick-lower.mplstyle'] = '''
xtick.top            : False
ytick.right          : False
axes.spines.top      : False
axes.spines.right    : False
  '''

  styles['goose-latex.mplstyle'] = r'''
font.family          : serif
font.serif           : {serif:s}
font.weight          : bold
font.size            : 18
text.usetex          : true
text.latex.preamble  : \usepackage{{amsmath}},\usepackage{{amsfonts}},\usepackage{{amssymb}},\usepackage{{bm}}
'''.format(serif=find_latex_font_serif())

  # write style definitions
  # -----------------------

  # directory name where the styles are stored
  dirname = os.path.abspath(os.path.join(matplotlib.get_configdir(), 'stylelib'))

  # make directory if it does not yet exist
  if not os.path.isdir(dirname): os.makedirs(dirname)

  # write all styles
  for fname, style in styles.items():
    open(os.path.join(dirname, fname),'w').write(style)

# ==================================================================================================

def set_decade_lims(axis=None,direction=None):
  r'''
Set limits the the floor/ceil values in terms of decades.

:options:

  **axis** ([``plt.gca()``] | ...)
    Specify the axis to which to apply the limits.

  **direction** ([``None``] | ``'x'`` | ``'y'``)
    Limit the application to a certain direction (default: both).
  '''

  # get current axis
  if axis is None:
    axis = plt.gca()

  # x-axis
  if direction is None or direction == 'x':
    # - get current limits
    MIN,MAX = axis.get_xlim()
    # - floor/ceil to full decades
    MIN = 10 ** ( np.floor(np.log10(MIN)) )
    MAX = 10 ** ( np.ceil (np.log10(MAX)) )
    # - apply
    axis.set_xlim([MIN,MAX])

  # y-axis
  if direction is None or direction == 'y':
    # - get current limits
    MIN,MAX = axis.get_ylim()
    # - floor/ceil to full decades
    MIN = 10 ** ( np.floor(np.log10(MIN)) )
    MAX = 10 ** ( np.ceil (np.log10(MAX)) )
    # - apply
    axis.set_ylim([MIN,MAX])

# ==================================================================================================

def scale_lim(lim,factor=1.05):
  r'''
Scale limits to be 5% wider, to have a nice plot.

:arguments:

  **lim** (``<list>`` | ``<str>``)
    The limits. May be a string "[...,...]", which is converted to a list.

:options:

  **factor** ([``1.05``] | ``<float>``)
    Scale factor.
  '''

  # convert string "[...,...]"
  if type(lim) == str: lim = eval(lim)

  # scale limits
  D       = lim[1] - lim[0]
  lim[0] -= (factor-1.)/2. * D
  lim[1] += (factor-1.)/2. * D

  return lim

# ==================================================================================================

def rel2abs_x(x, axis=None):
  r'''
Transform relative x-coordinates to absolute x-coordinates. Relative coordinates correspond to a
fraction of the relevant axis.

:arguments:

  **x** (``float``, ``list``)
    Relative coordinates.

:options:

  **axis** ([``plt.gca()``] | ...)
    Specify the axis to which to apply the limits.

:returns:

  **x** (``float``, ``list``)
    Absolute coordinates.
  '''

  # get current axis
  if axis is None:
    axis = plt.gca()

  # get current limits
  xmin, xmax = axis.get_xlim()

  # transform
  # - log scale
  if axis.get_xscale() == 'log':
    try   : return [10.**(np.log10(xmin)+i*(np.log10(xmax)-np.log10(xmin))) if i is not None else i for i in x]
    except: return  10.**(np.log10(xmin)+x*(np.log10(xmax)-np.log10(xmin)))
  # - normal scale
  else:
    try   : return [xmin+i*(xmax-xmin) if i is not None else i for i in x]
    except: return  xmin+x*(xmax-xmin)

# --------------------------------------------------------------------------------------------------

def rel2abs_y(y, axis=None):
  r'''
Transform relative y-coordinates to absolute y-coordinates. Relative coordinates correspond to a
fraction of the relevant axis.

:arguments:

  **y** (``float``, ``list``)
    Relative coordinates.

:options:

  **axis** ([``plt.gca()``] | ...)
    Specify the axis to which to apply the limits.

:returns:

  **y** (``float``, ``list``)
    Absolute coordinates.
  '''

  # get current axis
  if axis is None:
    axis = plt.gca()

  # get current limits
  ymin, ymax = axis.get_ylim()

  # transform
  # - log scale
  if axis.get_xscale() == 'log':
    try   : return [10.**(np.log10(ymin)+i*(np.log10(ymax)-np.log10(ymin))) if i is not None else i for i in y]
    except: return  10.**(np.log10(ymin)+y*(np.log10(ymax)-np.log10(ymin)))
  # - normal scale
  else:
    try   : return [ymin+i*(ymax-ymin) if i is not None else i for i in y]
    except: return  ymin+y*(ymax-ymin)

# ==================================================================================================

def plot_powerlaw(exp, startx, starty, width=None, **kwargs):
  r'''
Plot a power-law.

:arguments:

  **exp** (``float``)
    The power-law exponent.

  **startx, starty** (``float``)
    Start coordinates.

:options:

  **width, height, endx, endy** (``float``)
    Definition of the end coordinate (only on of these options is needed).

  **units** ([``'relative'``] | ``'absolute'``)
    The type of units in which the coordinates are specified. Relative coordinates correspond to a
    fraction of the relevant axis.

  **axis** ([``plt.gca()``] | ...)
    Specify the axis to which to apply the limits.

  ...
    Any ``plt.plot(...)`` option.

:returns:

  The handle of the ``plt.plot(...)`` command.
  '''

  # get options/defaults
  endx   = kwargs.pop('endx'  , None      )
  endy   = kwargs.pop('endy'  , None      )
  height = kwargs.pop('height', None      )
  units  = kwargs.pop('units' , 'relative')
  axis   = kwargs.pop('axis'  , plt.gca() )

  # apply width/height
  if width  is not None: endx = startx + width
  if height is not None: endy = starty + height

  # transform
  if units.lower() == 'relative':
    [startx, endx] = rel2abs_x([startx, endx], axis)
    [starty, endy] = rel2abs_y([starty, endy], axis)

  # determine multiplication constant
  const = starty / ( startx**exp )

  # get end x/y-coordinate
  if   endx is not None: endy = const * endx**exp
  elif endy is not None: endx = ( endy / const )**( -exp )

  # plot
  return axis.plot([startx, endx], [starty, endy], **kwargs)

# ==================================================================================================

def text(x, y, text, units='absolute', axis=None, **kwargs):
  r'''
Plot a text.

:arguments:

  **x, y** (``float``)
    Coordinates.

  **text** (``str``)
    Text to plot.

:options:

  **units** ([``'absolute'``] | ``'relative'``)
    The type of units in which the coordinates are specified. Relative coordinates correspond to a
    fraction of the relevant axis.

  ...
    Any ``plt.text(...)`` option.

:returns:

  The handle of the ``plt.text(...)`` command.
  '''

  # get current axis
  if axis is None:
    axis = plt.gca()

  # transform
  if units.lower() == 'relative':
    x = rel2abs_x(x, axis)
    y = rel2abs_y(y, axis)

  # plot
  return axis.text(x, y, text, **kwargs)

# ==================================================================================================

def histogram(data,**kwargs):
  r'''
Compute histogram.
See `numpy.histrogram <https://docs.scipy.org/doc/numpy/reference/generated/numpy.histogram.html>`_

:extra options:

  **return_edges** ([``True``] | [``False``])
    Return the bin edges if set to ``True``, return their midpoints otherwise.
  '''

  return_edges = kwargs.pop('return_edges', True)

  P, edges = np.histogram(data, **kwargs)

  if not return_edges: edges = np.diff(edges) / 2. + edges[:-1]

  return P, edges

# ==================================================================================================

def histogram_log(data,**kwargs):
  r'''
Compute histogram using log-binning.
See `numpy.histrogram <https://docs.scipy.org/doc/numpy/reference/generated/numpy.histogram.html>`_

:extra options:

  **return_edges** ([``True``] | [``False``])
    Return the bin edges if set to ``True``, return their midpoints otherwise.
  '''

  return_edges = kwargs.pop('return_edges', True)

  bins = kwargs.pop('bins', 10)

  if type(bins) == int: bins = np.logspace(np.log10(np.min(data)),np.log10(np.max(data)),bins)

  P, edges = np.histogram(data, bins=bins, **kwargs)

  if not return_edges: edges = np.diff(edges) / 2. + edges[:-1]

  return P, edges

# ==================================================================================================

def histogram_uniform(data,**kwargs):
  r'''
Compute histogram using bins that contain a uniform number of items.
See `numpy.histrogram <https://docs.scipy.org/doc/numpy/reference/generated/numpy.histogram.html>`_

:extra options:

  **bins** (``<int>``)
    Number of entries in each bin (the last bin is extended to fit the data).

  **return_edges** ([``True``] | [``False``])
    Return the bin edges if set to ``True``, return their midpoints otherwise.
  '''

  return_edges = kwargs.pop('return_edges', True)

  bins = kwargs.pop('bins', 10)

  count = int(np.floor(float(len(data))/float(bins))) * np.ones(bins, dtype='int')

  count[np.linspace(0, bins-1, len(data)-np.sum(count)).astype(np.int)] += 1

  idx = np.empty((bins+1), dtype='int')
  idx[0 ] = 0
  idx[1:] = np.cumsum(count)
  idx[-1] = len(data) - 1

  edges = np.unique(np.sort(data)[idx])

  P, edges = np.histogram(data, bins=edges, **kwargs)

  if not return_edges: edges = np.diff(edges) / 2. + edges[:-1]

  return P, edges

# ==================================================================================================

def histogram_cumulative(data,**kwargs):
  r'''
Compute cumulative histogram.
See `numpy.histrogram <https://docs.scipy.org/doc/numpy/reference/generated/numpy.histogram.html>`_

:extra options:

  **return_edges** ([``True``] | [``False``])
    Return the bin edges if set to ``True``, return their midpoints otherwise.

  **normalize** ([``False``] | ``True``)
    Normalize such that the final probability is one. In this case the function returns the (binned)
    cumulative probability density.
  '''

  return_edges = kwargs.pop('return_edges', True)

  norm = kwargs.pop('normalize', False)

  P, edges = np.histogram(data, **kwargs)

  P = np.cumsum(P)

  if norm: P = P/P[-1]

  if not return_edges: edges = np.diff(edges) / 2. + edges[:-1]

  return P, edges

# ==================================================================================================

def hist(P, edges, **kwargs):
  r'''
Plot histogram.
  '''

  from matplotlib.collections import PatchCollection
  from matplotlib.patches     import Polygon

  # extract local options
  axis      = kwargs.pop( 'axis'      , plt.gca() )
  cindex    = kwargs.pop( 'cindex'    , None      )
  autoscale = kwargs.pop( 'autoscale' , True      )

  # set defaults
  kwargs.setdefault('edgecolor','k')

  # no color-index -> set transparent
  if cindex is None:
    kwargs.setdefault('facecolor',(0.,0.,0.,0.))

  # convert -> list of Polygons
  poly = []
  for p, xl, xu in zip(P, edges[:-1], edges[1:]):
    coor = np.array([
      [xl, 0.],
      [xu, 0.],
      [xu, p ],
      [xl, p ],
    ])
    poly.append(Polygon(coor))
  args = (poly)

  # convert patches -> matplotlib-objects
  p = PatchCollection(args,**kwargs)
  # add colors to patches
  if cindex is not None:
    p.set_array(cindex)
  # add patches to axis
  axis.add_collection(p)

  # rescale the axes manually
  if autoscale:
    # - get limits
    xlim = [ edges[0], edges[-1] ]
    ylim = [ 0       , np.max(P) ]
    # - set limits +/- 10% extra margin
    axis.set_xlim([xlim[0]-.1*(xlim[1]-xlim[0]),xlim[1]+.1*(xlim[1]-xlim[0])])
    axis.set_ylim([ylim[0]-.1*(ylim[1]-ylim[0]),ylim[1]+.1*(ylim[1]-ylim[0])])

  return p

# ==================================================================================================

def cdf(data,mode='continuous',**kwargs):
  '''
Return cumulative density.

:arguments:

  **data** (``<numpy.ndarray>``)
    Input data, to plot the distribution for.

:returns:

  **P** (``<numpy.ndarray>``)
    Cumulative probability.

  **x** (``<numpy.ndarray>``)
    Data points.
  '''

  return ( np.linspace(0.0,1.0,len(data)), np.sort(data) )

# ==================================================================================================

def patch(*args,**kwargs):
  '''
Add patches to plot. The color of the patches is indexed according to a specified color-index.

:example:

  Plot a finite element mesh: the outline of the undeformed configuration, and the deformed
  configuration for which the elements get a color e.g. based on stress::

    import matplotlib.pyplot as plt
    import goosempl          as gplt

    fig,ax = plt.subplots()

    p = gplt.patch(coor=coor+disp,conn=conn,axis=ax,cindex=stress,cmap='YlOrRd',edgecolor=None)
    _ = gplt.patch(coor=coor     ,conn=conn,axis=ax)

    cbar = fig.colorbar(p,axis=ax,aspect=10)

    plt.show()

:arguments - option 1/2:

  **patches** (``<list>``)
    List with patch objects. Can be replaced by specifying ``coor`` and ``conn``.

:arguments - option 2/2:

  **coor** (``<numpy.ndarray>`` | ``<list>`` (nested))
    Matrix with on each row the coordinates (positions) of each node.

  **conn** (``<numpy.ndarray>`` | ``<list>`` (nested))
    Matrix with on each row the number numbers (rows in ``coor``) which form an element (patch).

:options:

  **cindex** (``<numpy.ndarray>``)
    Array with, for each patch, the value that should be indexed to a color.

  **axis** (``<matplotlib>``)
    Specify an axis to include to plot in. By default the current axis is used.

  **autoscale** ([``True``] | ``False``)
    Automatically update the limits of the plot (currently automatic limits of Collections are not
    supported by matplotlib).

:recommended options:

  **cmap** (``<str>`` | ...)
    Specify a colormap.

  **linewidth** (``<float>``)
    Width of the edges.

  **edgecolor** (``<str>`` | ...)
    Color of the edges.

  **clim** (``(<float>,<float>)``)
    Lower and upper limit of the color-axis.

:returns:

  **handle** (``<matplotlib>``)
    Handle of the patch objects.

.. seealso::

  * `matplotlib example
    <http://matplotlib.org/examples/api/patch_collection.html>`_.
  '''

  from matplotlib.collections import PatchCollection
  from matplotlib.patches     import Polygon

  # check dependent options
  if ( 'coor' not in kwargs or 'conn' not in kwargs ):
    raise IOError('Specify both "coor" and "conn"')

  # extract local options
  axis      = kwargs.pop( 'axis'      , plt.gca() )
  cindex    = kwargs.pop( 'cindex'    , None      )
  coor      = kwargs.pop( 'coor'      , None      )
  conn      = kwargs.pop( 'conn'      , None      )
  autoscale = kwargs.pop( 'autoscale' , True      )

  # set defaults
  kwargs.setdefault('edgecolor','k')

  # no color-index -> set transparent
  if cindex is None:
    kwargs.setdefault('facecolor',(0.,0.,0.,0.))

  # convert mesh -> list of Polygons
  if coor is not None and conn is not None:
    poly = []
    for iconn in conn:
      poly.append(Polygon(coor[iconn,:]))
    args = tuple(poly, *args)

  # convert patches -> matplotlib-objects
  p = PatchCollection(args,**kwargs)
  # add colors to patches
  if cindex is not None:
    p.set_array(cindex)
  # add patches to axis
  axis.add_collection(p)

  # rescale the axes manually
  if autoscale:
    # - get limits
    xlim = [ np.min(coor[:,0]) , np.max(coor[:,0]) ]
    ylim = [ np.min(coor[:,1]) , np.max(coor[:,1]) ]
    # - set limits +/- 10% extra margin
    axis.set_xlim([xlim[0]-.1*(xlim[1]-xlim[0]),xlim[1]+.1*(xlim[1]-xlim[0])])
    axis.set_ylim([ylim[0]-.1*(ylim[1]-ylim[0]),ylim[1]+.1*(ylim[1]-ylim[0])])

  return p

# ==================================================================================================


