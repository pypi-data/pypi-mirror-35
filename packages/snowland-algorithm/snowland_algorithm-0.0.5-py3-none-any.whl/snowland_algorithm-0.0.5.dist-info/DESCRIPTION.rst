=========
slapy
=========
1. install
pip install -r requirements.txt

#. dirs
    1. graph

    #. swarm
        a. pso(v0.0.1+)
        b. ga(v0.0.1+)
        #. gso(v0.0.2+)
        #. fa(v0.0.3+)
#. quick use
    1. pso
        def fun(vars):
            # fitness function
            x, y = vars
            if 1 <= x <= 2 * np.pi and 1 <= y <= np.pi:
                return np.cos(x) + np.sin(x) - x * y
            else:
                return -2 - 4 * np.pi ** 2  # return a small float number can not reach

        if __name__ == '__main__':
            engine = PSOEngine(vmax=0.01, bound=[[1, 2 * np.pi]], min_fitness_value=-1, dim=2, fitness_function=fun, steps=100)
            engine.run()
            x, y = engine.gbest.indv
            print('max value', fun(engine.gbest.indv))
            print('x:', x, 'y:', y)

    #. gso
        def fun(vars):
            # fitness function
            x, y = vars
            if 0 <= x <= 2 * np.pi and 0 <= y <= 2 * np.pi:
                return -np.cos(x) - np.sin(y) + 10
            else:
                return -10  # return a small float number can not reach


        if __name__ == '__main__':
            engine = GSOEngine(vmax=0.01, bound=[[0, 2 * np.pi]], rs=1, min_fitness_value=np.inf, dim=2, l0=1, fitness_function=fun,
                               steps=30)
            engine.run()
            x, y = engine.gbest.indv
            print('max value', fun(engine.gbest.indv))
            print('x:', x, 'y:', y)


