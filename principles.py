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

# Multi Threading
# - each thread is closely related to the main thread
# - they all share the same resources (so lock, sem etc realyl easy)
# Multip Processing
# - each process has its own copy of Python
# - they have theier own resources