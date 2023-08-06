######
PDXtra
######

PDXtra is a data analysis library built on top of Pandas and geared toward
time-series data analysis. The library offers subclasses of traditional
Pandas ``Series`` and ``DataFrame`` objects which provide additional
convenience methods for querying and manipulating data while retaining all
of the functionality of the original Pandas API. Additionally, the library also
provides ``TimeSeries`` and ``TimeSeriesDataFrame`` subclasses which are
specifically designed to be used for time-series and financial data analysis.

What can the package do?
------------------------
- Downcast entire dataframes. Choose whether to downcast integer columns, float
  columns, or both.
- Perform Excel-style x-lookup, and v-lookup.
- Qickly scan dataframes for column values based on index values, and
  optionally search using nearest-match.
- Compute the intersections of curves.
- Use inter-quartile range to eliminate outliers in data sets.
- Compute the linear regression of a series.
- Get true N-day moving averages.
- Temporarily set a dataframe index using a context manager.
- Compute common financial time-series metrics including: relative strength
  index, moving average convergence-divergence, and on-balance volume.

.. note::

   This distribution has been developed and tested on a standalone Python build
   and could--under rare circumstances--exibit unexpected behavior on standard
   CPython. Although no differences between the execution of code in the
   standalone build and normal CPython have been found during the process of
   development, I nevertheless wish to provide fair warning.

Installation
------------

.. code:: python

   python -m pip install pdxtra

Documentation
-------------
Up-to-date documentation can be found here: `<https://jammin93.github.io/pdxtra/>`_

Usage
-----
``TimeSeries`` and ``TimeSeriesDataFrame`` are both subclasses of the
``Series`` and ``DataFrame`` objects, respectively, and they themselves are
subclasses of the original Pandas ``DataFrame`` and ``Series`` objects. This
means that all of the functionality of the Pandas API is inhereted by these
subclasses.

Series Objects
^^^^^^^^^^^^^^
Creation of ``Series`` and ``DataFrame`` objects follows the same syntax as
traditional Pandas.

.. code:: python

   import pdxtra as pdx

   series = pdx.Series([1, 2, 3, 4, 5])
   time_series = pdx.TimeSeries([1, 2, 3, 4, 5])

DataFrame Objects
^^^^^^^^^^^^^^^^^
Creating ``TimeSeries`` and ``TimeSeriesDataFrame`` objects is no different
from creating their vanilla counterparts.

.. code:: python

   import pdxtra as pdx

   df = pdx.Dataframe({
       "a": ["a", "b", "c", "d", "e"],
       "b": [1, 2, 3, 4, 5],
   })
   ts_df = pdx.TimeSeriesDataFrame({
       "a": ["a", "b", "c", "d", "e"],
       "b": [1, 2, 3, 4, 5],
   })

License
-------
GNU General Public License
