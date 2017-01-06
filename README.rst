Say It To My Face
=================

Have you ever written a bunch of code and everything is going well for the
first time in computer history, and then some dreaded exception kills your
hopes and dreams? Did you then make menacing glances at the computer,
the source of all of your problems, and mutter "I bet you wouldn't say
that to my face."

Well now it can.

And it will.

Usage
=====

To have the interpreter tell you about your failings,
the `say_exceptions_to_my_face` function is available. It uses a logging
handler to read exception messages that come in through an exception hook. ::

    >>> import say_it_to_my_face
    >>> say_it_to_my_face.say_exceptions_to_my_face()
    >>> raise AttributeError("lol that's not an attribute")
    # A voice will read the message to you
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: lol that's not an attribute

You can also have all of your logs read to you via that log handler.
You can also pass it the name of a voice to use, though by default it
picks this up from your locale. ::

    >>> import logging
    >>> import say_it_to_my_face
    >>> handler = say_it_to_my_face.SayItToMyFace(voice="Daniel")
    >>> logger = logging.getLogger()
    >>> logger.addHandler(handler)
    >>> logger.critical("why did you do that?")


Requirements
============

* Python >= 3.3
* The `say` program on OS X or apparently the `espeak` on Ubuntu,
  though I haven't tried it, it just looks similar.
