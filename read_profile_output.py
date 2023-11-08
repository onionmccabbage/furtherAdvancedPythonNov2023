import pstats

def main():
    '''open a cProfile report and show the results'''
    p = pstats.Stats('performance/prof_out')
    p.print_stats()

if __name__ == '__main__':
    main()