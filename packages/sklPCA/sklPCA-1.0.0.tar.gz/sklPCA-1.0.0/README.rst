=======
skl-PCA
=======

This package implements Supervised Kernel-based Longitudinal Principal Components Analysis (skl-PCA) for predictor dimension reduction in longitudinal models. The software was written by members of the Mindstrong Health Data Science team:

    * Patrick Staples, PhD
    * Min Ouyang, PhD
    * Bob Dougherty, PhD
    * Greg Ryslik, PhD, FCAS, MAAA
    * Paul Dagum, MD, PhD


Please contact us at `datascience@mindstronghealth.com <datascience@mindstronghealth.com>`_.

NOTE: If you use this software in your work, please cite the following `paper <http://arxiv.org/abs/1808.06638>`_:

    Patrick Staples, Min Ouyang, Robert F. Dougherty, Gregory A. Ryslik, and Paul Dagum (2018). Supervised Kernel PCA For Longitudinal Data. http://arxiv.org/abs/1808.06638.

Installation
------------

The easiest way to install the package is via ``easy_install`` or ``pip``::

    $ pip install sklPCA

This should also take care of the dependencies (numpy, scipy, pandas, and sklearn).

Usage
-----

See examples.py for examples of simulated data, predictor reduction, fitting, and cross-validated model performance.


Copyright & License
-------------------

Copyright (c) 2018, `Mindstrong Health <http://mindstronghealth.com>`_. GNU Affero General Public License.

