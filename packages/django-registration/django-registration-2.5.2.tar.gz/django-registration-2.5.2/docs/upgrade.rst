.. _upgrade:


Upgrading from previous versions
================================

Prior to 2.0, the last widely-deployed release of
django-registration was 0.8; a 1.0 release was published, and
|version| is mostly backwards-compatible with it, but 1.0 appears not
to have seen wide adoption. As such, this guide covers the process of
upgrading from django-registration 0.8, as well as from 1.0.


Backends are now class-based views
----------------------------------

In django-registration 0.8, a registration workflow was
implemented as a class with specific methods for the various steps of
the registration process. In django-registration 2.0 and later, a
registration workflow is implemented as one or more class-based views.

In general, the required changes to implement a 0.8 registration
workflow in django-registration |version| is:

+-------------------------------------------------------------+------------------------------------------------------------------+
| 0.8 backend class implementation                            | 2.0+      view subclass implementation                           |
+=============================================================+==================================================================+
| Backend class implementing ``register()``                   | :meth:`registration.views.RegistrationView.register`             |
+-------------------------------------------------------------+------------------------------------------------------------------+
| Backend class implementing ``activate()``                   | :meth:`registration.views.ActivationView.activate`               |
+-------------------------------------------------------------+------------------------------------------------------------------+
| Backend class implementing ``registration_allowed()``       | :meth:`registration.views.RegistrationView.registration_allowed` |
+-------------------------------------------------------------+------------------------------------------------------------------+
| Backend class implementing ``get_form_class()``             | :meth:`registration.views.RegistrationView.get_form_class()`     |
+-------------------------------------------------------------+------------------------------------------------------------------+
| Backend class implementing ``post_registration_redirect()`` | :meth:`registration.views.RegistrationView.get_success_url()`    |
+-------------------------------------------------------------+------------------------------------------------------------------+
| Backend class implementing ``post_activation_redirect()``   | :meth:`registration.views.ActivationView.get_success_url()`      |
+-------------------------------------------------------------+------------------------------------------------------------------+


URLconf changes
---------------

If you were using one of the provided workflows in
django-registration 0.8 without modification, you will not need to
make any changes; both ``registration.backends.default.urls`` and
``registration.backends.simple.urls`` have been updated in
django-registration 2.0+ to correctly point to the new
class-based views:

+---------------------------------+---------------------------------------------------+
| 0.8 URLconf view reference      | |version| URLconf view reference                  |
+=================================+===================================================+
| ``registration.views.register`` | ``registration.views.RegistrationView.as_view()`` |
+---------------------------------+---------------------------------------------------+
| ``registration.views.activate`` | ``registration.views.ActivationView.as_view()``   |
+---------------------------------+---------------------------------------------------+

However, if you were using the two-step model-activation workflow, you
should begin referring to
``registration.backends.model_activation.urls`` instead of
``registration.backends.default.urls`` or ``registration.urls``, as
the latter two are deprecated and support for them will be removed in
a future release.

If you were passing custom arguments to the built-in registration
views, those arguments should continue to work, so long as your
URLconf is updated to refer to the new class-based views. For details
of how to pass custom arguments to class-based views, see `the Django
class-based view documentation
<https://docs.djangoproject.com/en/stable/topics/class-based-views/#simple-usage-in-your-urlconf>`_.


Template changes
----------------

When using :class:`~registration.forms.RegistrationForm`, the error
from mismatched passwords now is attached to the ``password2`` field
rather than being a form-level error. To check for and display this
error, you will need to change to accessing it via the ``password2``
field rather than via ``non_field_errors()`` or the ``__all__`` key in
the errors dictionary.


Changes since 1.0
-----------------

If you used django-registration 1.0, or a pre-2.0 checkout of the
code, you will need to make some minor adjustments.

If you previously used ``registration.backends.default``, you will now
see deprecation warnings, as the former "default" workflow is now
found in ``registration.backends.model_activation``. Use of
``registration.backends.default`` continues to work in
django-registration |version|, but will be removed in the future.

Similarly, references to ``registration.urls`` should become
references to ``registration.backends.model_activation.urls``, and
``registration.urls`` is deprecated and will be removed in a future
release.

If you had written custom subclasses of
:class:`~registration.views.RegistrationView` or of
``RegistrationView`` subclasses in the built-in workflows, the
following changes need to be noted:

* The ``register`` method now receives the
  :class:`~registration.forms.RegistrationForm` instance used during
  signup, rather than keyword arguments corresponding to the form's
  ``cleaned_data``.

* ``RegistrationForm`` itself is now a subclass of Django's built-in
  ``UserCreationForm``, and as such is now a ``ModelForm``
  subclass. This can cause metaclass conflict errors if you write a
  class which is a subclass of both ``RegistrationForm`` and a
  non-``ModelForm`` form class; to avoid this, ensure that subclasses
  of ``RegistrationForm`` and/or ``ModelForm`` come first in your
  subclass' method resolution order.

* As noted above, the password-mismatch error message is now attached
  to the ``password2`` field rather than being a form-level error.


Changes since 2.0
-----------------

One major change occurred between django-registration 2.0 and 2.1: the
addition in version 2.1 of the
:class:`~registration.validators.ReservedNameValidator`, which is now
used by default on :class:`~registration.forms.RegistrationForm` and
its subclasses.

This is technically backwards-incompatible, since a set of usernames
which previously could be registered now cannot be registered, but was
included because the security benefits outweigh the edge cases of the
now-disallowed usernames. If you need to allow users to register with
usernames forbidden by this validator, see its documentation for notes
on how to customize or disable it.

In 2.2, the behavior of the
:meth:`~registration.models.RegistrationProfile.expired` method was
clarified to accommodate user expectations; it does *not* return (and
thus,
:meth:`~registration.models.RegistrationProfile.delete_expired_users`
does not delete) profiles of users who had successfully activated.

In django-registration 2.3, the new validators
:func:`~registration.validators.validate_confusables` and
:func:`~registration.validators.validate_confusables_email` were
added, and are applied by default to the username field and email
field, respectively, of registration forms. This may cause some
usernames which previously were accepted to no longer be accepted, but
like the reserved-name validator this change was made because its
security benefits significantly outweigh the edge cases in which it
might disallow an otherwise-acceptable username or email address. If
for some reason you need to allow registration with usernames or email
addresses containing potentially dangerous use of Unicode, you can
subclass the registration form and remove these validators, though
doing so is not recommended.