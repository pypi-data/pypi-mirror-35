import cProfile
import pyade.de
import pyade.jade
import pyade.sade
import pyade.shade
import numpy as np
import pstats
import io
import pyade.lshade
import pyade.lshadecnepsin
import pyade.jso
import scipy.optimize
import pyade.mpede
import cec2014
import pyade.ilshade
import pyade.saepsdemmts




def my_callback(**kwargs):
    global output
    if kwargs['current_generation'] % round(kwargs['max_iters'] * 0.1) == 0 \
      or kwargs['current_generation'] + 1 == kwargs['max_iters']:
            best = np.argmin(kwargs['fitness'])
            output.append((kwargs['current_generation'] * 100 + 100, kwargs['fitness'][best]))

def my_callback_evals(**kwargs):
    global output

    if len(output) == 0 or kwargs['max_evals'] / 10 * (len(output) + 1 ) < kwargs['num_evals'] \
            or kwargs['num_evals'] >= kwargs['max_evals']:
        best = np.argmin(kwargs['fitness'])
        output.append((kwargs['num_evals'], kwargs['fitness'][best]))

if __name__ == '__main__':
    global output
    dim = 30

    modules =  [pyade.lshadecnepsin
                ]

    for module in modules:
        current_module = module
        find_max = 0

        with open(f'C:\\Users\\xKuZz\\Desktop\\TFG\\Resultados\\{current_module.__name__}.csv', mode='w') as archivo:
            for i in range(51):
                print(f'Ejecución {i}')
                for j in range(30):
                    num_func = j + 1
                    print(f'Función {num_func}')
                    bench = cec2014.Benchmark(num_func)
                    func = lambda x: bench.get_fitness(x)
                    output = []
                    params = current_module.get_default_params(dim)
                    #params['cross'] = 'exp'
                    params['bounds'] = np.array([[-100, 100]] * params['individual_size'])
                    params['func'] = func
                    params['seed'] = i

                    params['callback'] = my_callback
                    sol, fit = current_module.apply(**params)
                    print(fit)
                    for generacion, fitness in output:
                        archivo.write(f'{generacion}, {num_func}, {fitness - 100 * num_func}\n')

