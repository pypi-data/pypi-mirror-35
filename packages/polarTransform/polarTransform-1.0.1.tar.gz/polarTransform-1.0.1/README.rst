Introduction
=================
polarTransform is a Python package for converting images between the polar and Cartesian domain. It contains many
features such as specifying the start/stop radius and angle, interpolation order (bicubic, linear, nearest, etc), and
much more.

Installing
=================
Prerequisites
-------------
* Python 3
* Dependencies:
   * numpy
   * scipy
   * scikit-image

Installing polarTransform
-------------------------
polarTransform is currently available on `PyPi <https://pypi.python.org/pypi/polarTransform/>`_. The simplest way to
install alone is using ``pip`` at a command line::

  pip install polarTransform

which installs the latest release.  To install the latest code from the repository (usually stable, but may have
undocumented changes or bugs)::

  pip install git+https://github.com/addisonElliott/polarTransform.git


For developers, you can clone the polarTransform repository and run the ``setup.py`` file. Use the following commands to get
a copy from GitHub and install all dependencies::

  git clone pip install git+https://github.com/addisonElliott/polarTransform.git
  cd polarTransform
  pip install .

or, for the last line, instead use::

  pip install -e .

to install in 'develop' or 'editable' mode, where changes can be made to the local working code and Python will use
the updated polarTransform code.

Test and coverage
=================
To test the code on any platform, make sure to clone the GitHub repository to get the tests and::

  python tests/test_polarTransform.py

Example
=================
Input image:

.. image:: http://polartransform.readthedocs.io/en/latest/_images/verticalLines.png
    :alt: Cartesian image

.. code-block:: python

    import polarTransform
    import matplotlib.pyplot as plt
    import imageio

    verticalLinesImage = imageio.imread('IMAGE_PATH_HERE')

    polarImage, ptSettings = polarTransform.convertToPolarImage(verticalLinesImage, initialRadius=30,
                                                                finalRadius=100, initialAngle=2 / 4 * np.pi,
                                                                finalAngle=5 / 4 * np.pi)

    cartesianImage = ptSettings.convertToCartesianImage(polarImage)

    plt.figure()
    plt.imshow(polarImage, origin='lower')

    plt.figure()
    plt.imshow(cartesianImage, origin='lower')

Resulting polar domain image:

.. image:: http://polartransform.readthedocs.io/en/latest/_images/verticalLinesPolarImage_scaled3.png
    :alt: Polar image

Converting back to the cartesian image results in:

.. image:: http://polartransform.readthedocs.io/en/latest/_images/verticalLinesCartesianImage_scaled.png
    :alt: Cartesian image

Next Steps
=================
To learn more about polarTransform, see the `documentation <http://polartransform.readthedocs.io/>`_.

License
=================
polarTransform has an MIT-based `license <https://github.com/addisonElliott/polarTransform/blob/master/LICENSE>`_.
