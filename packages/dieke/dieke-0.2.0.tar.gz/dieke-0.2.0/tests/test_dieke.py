#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `dieke` package."""

import pytest
# from multiprocessing import Pool

import dieke


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    rare_earths = ["La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd",
                   "Tb", "Dy", "Ho", "Er", "Tm", "Yb"]

    for k in [2]:  # range(2, 13):
        print("Making matricies for %s (nf=%d)\n" % (rare_earths[k], k))
        dieke.RareEarthIon(k)

    # This "works" but only if you have a lot of ram
    # p = Pool(8)
    # p.map(dieke.RareEarthIon, range(2, 13))
