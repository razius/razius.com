Ditching Wordpress and becoming one of the cool kids
####################################################
:date: 2013-12-21 10:58
:tags: wordpress, static, pygments, python, restructured text
:slug: ditching-wordpress-and-becoming-one-of-the-cool-kids

I've been a Wordpress user and developer for a long long time but lately this nagging idea kept crawling in the back of my head, why not switch my website to a statically generated one? Well, a 3 hour train journey and a lot of boredom finally pushed me to just make the switch and to write a short post about it.

What is a statically generated website?
---------------------------------------

Compared to dynamic web pages, where the web page is rendered by server-side logic and usually require a database, with statically generated websites you feed files written in a markup language like Markdown, reStructuredText, Textile, etc. to a static site generator which spits them out as a static website that is ready for deployment.

They are useful when the content doesn't vary based on parameters provided by a user, like in the case of a personal web page where the content is delivered to the user exactly as it was stored.

Why bother switching?
---------------------

**reStructuredText**

I could write my articles as simple flat files using the `reStructuredText`_ format, goodbye storing of articles in a database. Having the articles as simple text files would allow me to easily edit them using my editor of choice, sublime text, so no more editing of text in a form on a web page, copy/pasting code snippets in it and painfully adjusting the indentation. Just take a look at the source of this article and see how easy it is to embed different code snippets, it feels just like editing a source file. I would also have syntax highlighting powered by the excellent `pygments`_ syntax highlighter.

.. code-block:: python

    print("Hello, World!")

.. code-block:: c

    #include <stdio.h>

    int main(void) {
        printf("Hello, world!\n");
        return 0;
    }

.. code-block:: java

    public class HelloWorld {
        public static void main(String[] args) {
            System.out.println("Hello, world!");
        }
    }

.. code-block:: go

    package main

    import "fmt"

    func main() {
        fmt.Println("Hello, world!")
    }

Plus, having the articles as flat files would allow me to keep the entire website in a git repository really easy.

**Faster page loads**

Because there is no need to build the web page each time upon serving it, page load would be faster. I made a test of a page load before and after the switch.

.. figure:: {filename}/images/articles/wordpress-page-speed.png
    :alt: Page load speed for Wordpress
    :align: center

    Page load speed for Wordpress

.. figure:: {filename}/images/articles/static-page-speed.png
    :alt: Page load speed for static website
    :align: center

    Page load speed for static website

Not bad, a whole second. Yes, it's not really a fair comparison, I also changed the theme to a much simpler one which is a big boost too, but still.

**Github pages**

I could host my page for free using `Github pages`_, which is a free hosting for static pages offered by Github, using git repositories for file storing. No, I'm not killing the little curious sysadmin in me, it's just that for my humble page administration is starting to feel like a hassle.

**The geek factor**

In the end, why not? I keep this website to toy around with it and this would allow me to play around more with Python, Jinja2 and reStructuredText plus I could test a new flow for writing articles.

Making the switch
-----------------

I picked `Pelican`_ over the two most popular static web site generators, `Jekyll`_ and `Octopress`_ because being a python developer, and Pelican being python based, it would feel a bit more natural than Jekyll or Octopress which are Ruby based.

If you think something else would suit you more, you can take a look at a complete list of static website generators at `staticsitegenerators.net`_

Installing Pelican, it's as simple as running:

.. code-block:: console

    $ pip install pelican

Next, kickstart a new project. Do do this run ``pelican-quickstart``, it will ask us a few questions about you site to generate a config file named ``pelicanconf.py`` and create a project skeleton with some helper scripts inside.

.. code-block:: console

    $ pelican-quickstart

You can edit you ``pelicanconf.py`` to further tune your configuration, take a look at the `manual`_ for the available options or you can check out `my pelicanconf.py`_ for some inspiration.

All the content goes into the `content`_ folder and I like to keep all my `articles`_ and `posts`_ in separate folders by setting the following in ``pelicanconf.py``:

.. code-block:: python

    PATH = 'content'
    PAGE_DIR = 'pages'
    ARTICLE_DIR = 'articles'

You can export your articles from Wordpress into an XML file by going to Tool -> Export and then run ``pelican-import`` to generate the appropriate text files into the ``content`` folder.

.. code-block:: console

    $ pelican-import --wpfile -o content/ wordpress-export.xml

You can preview your files by running ``make devserver``, this will start a webserver that serves your build html files under ``http://localhost:8000/`` and a process that watches the ``content`` folder for file changes and rebuilds the served html files.

.. code-block:: console

    make devserver

Hosting on Github
-----------------

Instead of using Github pages, where you are required to have your html pages under the project root and because pelican puts them under the output folder, I chose to use project pages. With project pages you keep the html files in a separate git branch called ``gh-pages`` and Github will publish those pages for you under ``GITHUB_USERNAME.github.com/GITHUB_PROJECTNAME.`` from that branch. Ex. my web address would be ``http://razius.github.com/razius.com``, don't worry, you can use your custom domain too.

Notice the difference between the `master <https://github.com/razius/razius.com/tree/master>`_ branch and the `gh-pages <https://github.com/razius/razius.com/tree/gh-pages>`_ branch.

Luckily, you don't have to maintain this branch manually, there's a script called ``ghp-import`` which will manage it for you. It copies a directory to the ``gh-pages`` branch, that is the site's document root.

.. code-block:: console

    pip install ghp-import

Now with ``ghp-import`` installed you can publish your project pages by simply running ``make github`` command which will build the html pages for publishing under the ``output/`` folder, call ``ghp-import`` to copy the files under that folder to the ``gh-pages`` branch and do a ``git push`` to push the new changes to Github.

.. code-block:: console

    make github

You can also use your own `custom domain`_, I keep my ``CNAME`` file in a static folder called ``files`` and I've added the file's path to `EXTRA_PATH_METADATA`_ in ``pelicanconf.py`` so that pelican copies it each time on build.

.. code-block:: python

    STATIC_PATHS = ['files']
    EXTRA_PATH_METADATA = {
        'files/CNAME': {'path': 'CNAME'},
    }

*PS: Yes, the title is a bit ironic.*

.. _reStructuredText: http://docutils.sourceforge.net/docs/user/rst/quickref.html
.. _pygments: http://pygments.org/
.. _Github pages: http://pages.github.com/
.. _Pelican: http://blog.getpelican.com/
.. _Jekyll: http://jekyllrb.com/
.. _Octopress: http://octopress.org/
.. _staticsitegenerators.net: http://staticsitegenerators.net/
.. _manual: http://docs.getpelican.com/en/3.3.0/settings.html
.. _my pelicanconf.py: https://github.com/razius/razius.com/blob/master/pelicanconf.py
.. _content: https://github.com/razius/razius.com/blob/09dfd41f842d9b3b1a514816fa550423fc9b35e4/pelicanconf.py#L37
.. _articles: https://github.com/razius/razius.com/blob/09dfd41f842d9b3b1a514816fa550423fc9b35e4/pelicanconf.py#L39
.. _posts: https://github.com/razius/razius.com/blob/09dfd41f842d9b3b1a514816fa550423fc9b35e4/pelicanconf.py#L38
.. _custom domain: https://help.github.com/articles/setting-up-a-custom-domain-with-pages
.. _EXTRA_PATH_METADATA: https://github.com/razius/razius.com/blob/master/pelicanconf.py#L43

