# Everything should be immutable (until it needs to be mutable)
# e.g. use tuple rather than list

# In the stateful pattern, we can make EVERYTHING immutable
# when things change we destroy the old state and create abrand new (immutable) state

# remember - Python is written in C. It is known as cPython
#there are other implementations of Python:
# jython - written in Java
# ironpython - written in .net
# ipython is written in C (interactive python)

# The GIL (Global Interpreter Lock)