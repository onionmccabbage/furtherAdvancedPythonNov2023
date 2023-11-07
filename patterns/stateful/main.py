from _on import On
from _off import Off
from _sleep import Sleep
from _hybernate import Hybernate
from _laptop import Laptop


def main():
    '''exercise the stateful laptop'''
    c = Laptop()
    c.change(On)
    c.change(Off)
    c.change(On)
    c.change(Sleep)
    c.change(On)
    c.change(Hybernate)
    c.change(Off) # not permitted

if __name__ == '__main__':
    main()