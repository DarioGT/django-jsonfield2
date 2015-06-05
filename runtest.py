#!/usr/bin/env python

import os, sys
import django

from django.conf import settings
from django.test.utils import get_runner


DEFAULT_SETTINGS = dict(
    INSTALLED_APPS=(
        'qjsonfield',
        'qjsonfield.tests',
        ),
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3"
            }
        },
    MIDDLEWARE_CLASSES=[],
    )


def runtests():

    settings.configure(**DEFAULT_SETTINGS)
    django.setup()

    parent = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, parent)

    TestRunner = get_runner(settings)

    test_runner = TestRunner()
    failures = test_runner.run_tests(["qjsonfield.tests"])
    sys.exit(bool(failures))

    # from django.test.runner import DiscoverRunner
    # runner_class = DiscoverRunner
    # test_args = ['qjsonfield.tests']

    # failures = runner_class( verbosity=1, interactive=True, failfast=False ).run_tests(test_args)
    # sys.exit(failures)


if __name__ == '__main__':
    runtests()
