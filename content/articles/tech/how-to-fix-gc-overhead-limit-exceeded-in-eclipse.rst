How to fix GC overhead limit exceeded in Eclipse
################################################
:date: 2012-03-27 10:13
:tags: eclipse, java, linux
:slug: how-to-fix-gc-overhead-limit-exceeded-in-eclipse

.. raw:: html

   <p>

If you're performing memory intensive operations such as building
workspace on big projects, Eclipse will throw this error when it runs
out of memory:

    An internal error occurred during: "Building workspace". GC overhead
    limit exceeded

    .. raw:: html

       </p>

In order to fix it, you need to increase the memory allocation for
Eclipse. To do this, open **eclipse.ini** and increase the **Xms**
(heap's start memory) and **Xmx** (heap's maximum memory) values to a
value that you think is reasonable with your system and projects, for
example:

    -Xms512m
     -Xmx1024m
