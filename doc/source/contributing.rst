.. _contributing:

************
Contributing
************

BDD Scenarios
--------------

To aid in making correct design decisions and avoid unnecessary features implementation employ behaviour driven development (BDD) model.
The idea is to design usage scenarios together with the end users and developers using natural human language. The current implementation
is done using behave_, python package for BDD-style development.


Features
~~~~~~~~


Feature files are added in :file:`features` directory, and corresponded steps are in :file:`features/steps`.

The name of the feature file should be prepended with `behave_` and steps with `step_`. This is to avoid namespace conflicts between steps implementation and package modules.

::

  features/
  ├── behave_export_cf_netcdf.feature
  ├── environment.py
  └── steps
      └── steps_export_cf_netcdf.py



.. _behave: http://pythonhosted.org/behave
