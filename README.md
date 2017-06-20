Dehumanize
==========

This package is designed to help with scraping projects. Often we come across a
date which has been rendered in a way that makes it easy for humans to
comprehend, but not so easy for bots and spiders.

The `dehumanize` project aims to reverse Django's humanized naturaltime strings
so that they are more useful for our spiders and bots.

## Example

    >>>from dehumanize import dehumanize
    >>>dehumanize.naturaltime("2 days ago")
    datetime.datetime(2017, 6, 18, 11, 52, 10, 11000)
    >>>dehumanize.naturaltime("5 days, 2 hours from now")
    datetime.datetime(2017, 6, 25, 13, 54, 30, 78000)
