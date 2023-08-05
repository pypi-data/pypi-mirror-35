
Django Password-Protect
=======================

Easy password-protected URLs for your Django website.

Install
-------

1. Install via pip: ``pip install django-pwdprotect``.
2. Add ``pwdprotect`` your ``INSTALLED_APPS``.
3. Add ``pwdprotect.middleware.PasswordProtectMiddleware`` to your ``MIDDLEWARE`` settings.
4. Run migrations ``python manage.py migrate pwdprotect``.

Usage
-----

After installation you can add protected URLs via the Django admin. Only local URLs starting with a ``/`` are allowed (do not include the site domain). The middleware will then check each request and prompt the user to log in if required.

Contributing
------------

Review contribution guidelines at CONTRIBUTING.md_.

.. _CONTRIBUTING.md: CONTRIBUTING.md
