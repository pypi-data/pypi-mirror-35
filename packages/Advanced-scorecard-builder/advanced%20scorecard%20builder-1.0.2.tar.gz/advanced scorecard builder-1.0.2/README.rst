Advanced Scorecard Builder
==========================

This package contains a ``AMA Intitute ASB Free Version`` 1.0 module.


Installation
--------------------------------

You can simply use pip to install, as the following:

.. code-block:: bash

   $ pip install Advanced-scorecard-builder

Examples
========
.. code:: python

    from sklearn import datasets
    X,y = datasets.make_classification(n_samples=10**5, n_features=25, random_state=123)
    print(X.shape)
    # Data Frame
    names = []
    for el in range(25):
        names.append("zm"+str(el+1))
    df = pd.DataFrame(X, columns=names)
    df['target'] = y
    # take asb object
    ama = asb(df,'target')
    # fit your model
    ama.fit()
    # get scorecard
    ama.get_scorecard()
    # get model informations
    ama.model_info_
    # and produce report file
    ama.html_report('raport.html')



How to Contribute
--------------------------------

Email me s.zajac@amainstitute.pl

