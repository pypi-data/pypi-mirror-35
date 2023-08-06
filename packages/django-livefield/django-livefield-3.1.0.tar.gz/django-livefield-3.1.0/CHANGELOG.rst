Changelog
=========

3.1.0
------------------
    - Fix [deprecation of context param for Field.from_db_value](https://code.djangoproject.com/ticket/28370)
    - Support for Django 2.1 (Thanks [@lukeburden](https://github.com/lukeburden)
    - Switch tests suite to use pytest
    - Remove pylint-django plugin, no longer needed


3.0.0
------------------
    - Add support for Python 3.6
    - Add support for Django 2.0
    - Remove support for Python 3.4
    - Remove support for old Django versions
    - Remove GIS


2.5.0 (Not released)
------------------
    - Added official Python 3 support.
    - Re-added support for Django 1.8. Now supports Django 1.8 and 1.9.

2.4.0 (2016-02-11)
------------------
    - Drop support for Django 1.8
    - Add number of affected rows for delete methods (hard_delete, soft_delete, delete). Note: Django 1.9+ only.

2.1.0 (2014-09-04)
------------------
    - Add support for Django 1.7.

2.0.0 (2014-07-13)
------------------
    - Renamed top-level namespace to ``livefield``.
    - Restructured internally to match Django convention.
    - Added GIS support.
    - Added South support.

1.0.0 (2014-02-14)
------------------
    - Initial release.
    - Separated existing code from main application repository.
