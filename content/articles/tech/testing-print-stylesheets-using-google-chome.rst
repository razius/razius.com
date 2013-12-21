Testing print stylesheets using Google Chrome
#############################################
:date: 2013-05-14 21:46
:slug: testing-print-stylesheets-using-google-chome

Testing CSS print media queries is really difficult but `a new featured`_ was introduced in Google Chrome in December that allows you to apply different CSS media types like handheld, print, screen and so on.

1. `Open Developer Tools`_ in Google Chrome by clicking the menu icon at the top-right of your browser window, then select Tools → Developer tools.

2. Open up the Overrides menu in the Developer Tools by clicking the gear in the bottom right corner:

.. figure:: {filename}/images/articles/dev-tools-settings.png
    :align: center

3. Enable "Emulate CSS media" and select the "print" media type option from the drop-down box:

.. figure:: {filename}/images/articles/emulate-css-print.png
    :align: center

You can find more information and nifty tricks in the `official documentation`_.

.. _a new featured: https://plus.google.com/+AddyOsmani/posts/MgpioU84JPe
.. _Open Developer Tools: https://developers.google.com/chrome-developer-tools/docs/shortcuts#opening-devtools
.. _official documentation: https://developers.google.com/chrome-developer-tools/docs/mobile-emulation
