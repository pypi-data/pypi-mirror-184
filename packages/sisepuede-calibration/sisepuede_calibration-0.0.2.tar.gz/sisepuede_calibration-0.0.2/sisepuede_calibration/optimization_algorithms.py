import random
import numpy as np
from multiprocessing import Pool,cpu_count, Value, Array

# Para hacer el muestreo por Latin Hypecube
from scipy.stats.qmc import LatinHypercube,scale
import math
import ctypes


# Genera población aleatoria binaria de m bit-string y cromosomas de tamaño n
def rand_population_binary(m,n):
    return [[random.randint(0, 1) for j in range(n)]for i in range(m)]

# Función que codifica las variables
def length_variable(i_sup,i_inf,precision):
    return int(math.ceil(math.log2((i_sup-i_inf)*10**(precision))))

# Función que obtiene las potencias en base dos de un vector de bits
def to_decimal(dimension,v):
    v.reverse()
    return sum(np.array([2**(i) for i in range(dimension)])*np.array(v))

# Función que codifica el vector de bits a un valor real
def binary2real(i_sup,i_inf,dimension,pob):
     return [i_inf + (to_decimal(dimension,v)*(i_sup-i_inf)/(2**(dimension)-1)) for v in pob]

# Función que genera la estructura de datos Fenotipo
def DECODE(n_variables,m,i_sup_vec,i_inf_vec,dimension_vec,pob_vec):

    feno = [[] for i in range(m)]

    for i in range(n_variables):
        i_sup = i_sup_vec[i]
        i_inf = i_inf_vec[i]
        pob = pob_vec[i]
        dim = dimension_vec[i]
        b2r = binary2real(i_sup,i_inf,dim,pob)
        for k in range(m):
            feno[k].append(b2r[k])

    return feno

# Funcion que genera la estructura de datos de la función objetivo
def OBJFUN(f,feno,bandera,procesos):
    if bandera == True:
        nproc = cpu_count()
        p = Pool(nproc-2)
        with p:
            resultado = p.map(f, feno)
        #return list(map(ackley,feno))
        return resultado
    else:
        p = Pool(procesos)
        with p:
            resultado = p.map(f, feno)
        #return list(map(ackley,feno))
        return resultado
# Función que genera la aptitud de los individuos
def APTITUD(objv,operacion):

    val_max = max(objv)
    val_min = min(objv)

    if operacion == "min":
        objv_norm = [(((i-val_min)/(val_max-val_min))+0.01)**-1 for i in objv]
        suma = sum(objv_norm)
        key_objv = [(k,i/suma) for (k,i) in enumerate(objv_norm)]
        objv_sort = sorted(key_objv,key=lambda tup: tup[1],reverse=True)

    elif operacion == "max":
        objv_norm = [(((i-val_min)/(val_max-val_min))+0.1) for i in objv]
        suma = sum(objv_norm)
        key_objv = [(k,i/suma) for (k,i) in enumerate(objv_norm)]
        objv_sort = sorted(key_objv,key=lambda tup: tup[1],reverse=True)

    return objv_sort

# Función que selecciona a los mejores individuos
def SELECCION(aptitud,tipo,n_variables,población):
    if tipo == "ruleta":
        n = int(len(aptitud)/2)
        suma_acumulada = np.cumsum([v for (k,v) in aptitud])

        individuos_dict = {i:{} for i in range(n)}

        for pareja in range(n):
            for individuo in range(2):
                aleatorio = random.random()
                index_ind = np.where(suma_acumulada >= aleatorio)[0][0]
                cromosoma = []
                for gen in range(n_variables):
                    cromosoma.append(población[gen][aptitud[index_ind][0]])

                cromosoma = sum(cromosoma,[])
                individuos_dict[pareja][individuo] = cromosoma

    return individuos_dict

def CRUZA(seleccion,tipo,length_total_cromosoma,prob_c):
    if tipo == "unpunto":
        n = len(seleccion)

        nueva_poblacion = []

        for pareja in range(n):
            
            aleatorio_pc = random.random()
            
            if aleatorio_pc < prob_c:
                punto_cruza = random.randint(0, length_total_cromosoma)

                primer_nuevo_individuo = seleccion[pareja][0][0:punto_cruza] + seleccion[pareja][1][punto_cruza:length_total_cromosoma]
                segundo_nuevo_individuo = seleccion[pareja][1][0:punto_cruza] + seleccion[pareja][0][punto_cruza:length_total_cromosoma]

                nueva_poblacion.append(primer_nuevo_individuo)
                nueva_poblacion.append(segundo_nuevo_individuo)
            else:
                nueva_poblacion.append(seleccion[pareja][0])
                nueva_poblacion.append(seleccion[pareja][1])

    return nueva_poblacion

def MUTACION(nueva_poblacion,length_total_cromosoma,n_variables,dimension_vec):

    mutacion_param = 2/length_total_cromosoma
    n = len(nueva_poblacion)

    for individuo in range(n):
         muta_random = np.array([random.random() for i in range(length_total_cromosoma)])
         muta_index = np.where(muta_random < mutacion_param)[0]

         for i in muta_index:
             nueva_poblacion[individuo][i] = int(not nueva_poblacion[individuo][i])

    inicio = 0
    fin = 0
    nueva_poblacion_format = []

    for gen in range(n_variables):
        nueva_poblacion_gen = []
        fin += dimension_vec[gen]
        for individuo in nueva_poblacion:
            nueva_poblacion_gen.append(individuo[inicio:fin])

        nueva_poblacion_format.append(nueva_poblacion_gen)
        inicio +=dimension_vec[gen]

    return nueva_poblacion_format

class BinaryGenetic(object):
    """docstring for BinaryGenetic."""

    def __init__(self,population,n_variables,i_sup_vec,i_inf_vec,precision,maxiter,pc):
        self.m = population
        self.n_variables = n_variables
        self.i_sup_vec = i_sup_vec
        self.i_inf_vec = i_inf_vec
        self.precision = precision
        self.maxiter = maxiter
        self.pc = pc

    def run_optimization(self,f):
        dimension_vec = []
        genotipo = []
        length_total_cromosoma = 0

        ## Generamos población inicial
        for i in range(self.n_variables):
            length_cromosoma = length_variable(self.i_sup_vec[i],self.i_inf_vec[i],self.precision)
            length_total_cromosoma += length_cromosoma
            dimension_vec.append(length_cromosoma)
            genotipo.append(rand_population_binary(self.m, length_cromosoma))

        ## Iniciamos el algoritmo genético
        feno = DECODE(self.n_variables,self.m,self.i_sup_vec,self.i_inf_vec,dimension_vec,genotipo)
        print("Evaluando poblacion inicial")
        objv = OBJFUN(f,feno,True,1)

        resultados = []
        mejor_individuo = 0
        mejor_valor = 100000000000000

        fitness_values = []

        for it in range(self.maxiter):
            print("-----------------------------")
            print("-%%%%%%%%%%%%%%%%%%%%%%%%%%%-")
            print("        Iteración {}".format(it))
            print("-%%%%%%%%%%%%%%%%%%%%%%%%%%%-")
            print("-----------------------------")

            aptitud = APTITUD(objv,"min")
            seleccion = SELECCION(aptitud,"ruleta",self.n_variables,genotipo)
            genotipo = CRUZA(seleccion,"unpunto",length_total_cromosoma, self.pc)
            genotipo = MUTACION(genotipo,length_total_cromosoma,self.n_variables,dimension_vec)
            feno = DECODE(self.n_variables,self.m,self.i_sup_vec,self.i_inf_vec,dimension_vec,genotipo)
            objv = OBJFUN(f,feno,True,1)
            resultados.append(min(objv))
            mejor_individuo = objv.index(min(objv))
            #print("Mejor valor fun.obj ---> {}. Variables de decision ---> {}".format(objv[mejor_individuo],feno[mejor_individuo]))
            #print("Mejor valor fun.obj ---> {}".format(objv[mejor_individuo]))
            if objv[mejor_individuo] < mejor_valor:
                mejor_valor = objv[mejor_individuo]
                mejor_vector = feno[mejor_individuo]

            print("It {}  gbest_val {}".format(it, mejor_valor))
            
            fitness_values.append(mejor_valor)
        best_vector = mejor_vector

        return fitness_values, best_vector,mejor_valor

'''
------------------------------------------
                    DE
Classic Differential Evolution

-------------------------------------------
## Implemented as a minimization algorithm

# Inputs:
    * f_cost        - function to be minimized
    * pop_size      - number of individuals in the population
    * max_iters     - maximum number of optimization iterations
    * pc            - crossover probability
    * lb
    * ub
    * step_size
    * theta_0

# Output
    * best_theta    - best solution found
    * best_score    - history of best score
'''

def DE(f_cost,pop_size,max_iters,pc,lb,ub,step_size = 0.4, theta_0 = None):
    # problem dimension
    n_dim = np.shape(lb)[0]
    # randomly initialize the population
    pop_chrom = (ub - lb) * np.random.random_sample(size = (pop_size,n_dim)) + lb

    if theta_0 is not None:
        pop_chrom[0] = theta_0
    # obtain the cost of each solution
    pop_cost = np.zeros(pop_size)

    for id_p in range(pop_size):
        pop_cost[id_p] = f_cost(pop_chrom[id_p])

    # optimization
    for id_iter in range(max_iters):
        print("-----------------------------")
        print("-%%%%%%%%%%%%%%%%%%%%%%%%%%%-")
        print("        Iteración {}".format(id_iter))
        print("-%%%%%%%%%%%%%%%%%%%%%%%%%%%-")
        print("-----------------------------")

        for id_pop in range(pop_size):
            # pick candidate solution
            xi = pop_chrom[id_pop]
            # ids_cs vector containing the indexes of
            # the all other candidate solution but xi
            ids_cs = np.linspace(0, pop_size - 1, pop_size, dtype = int)
            # remove id_pop from ids_cs
            ids_cs = np.where(ids_cs != id_pop)
            # convert tuple to ndarray
            ids_cs = np.asarray(ids_cs)[0]
            # randomly pick 3 candidate solution using indexes ids_cs
            xa , xb , xc = pop_chrom[np.random.choice(ids_cs, 3, replace = False)]
            V1 = xa
            V2 = xb
            Vb = xc
            # create the difference vector
            Vd = V1 - V2
            # create the mutant vector
            Vm = Vb + step_size*Vd
            # make sure the mutant vector is in [lb,ub]
            Vm = np.clip(Vm,lb,ub)
            # create a trial vector by recombination
            Vt = np.zeros(n_dim)
            jr = np.random.rand()   # index of the dimension
                                    # that will under crossover
                                    # regardless of pc
            for id_dim in range(n_dim):
                rc = np.random.rand()
                if rc < pc or id_dim == jr:
                    # perform recombination
                    Vt[id_dim] = Vm[id_dim]
                else:
                    # copy from Vb
                    Vt[id_dim] = xi[id_dim]
            # obtain the cost of the trial vector
            vt_cost = f_cost(Vt)
            # select the id_pop individual for the next generation
            if vt_cost < pop_cost[id_pop]:
                pop_chrom[id_pop] = Vt
                pop_cost[id_pop] = vt_cost
        # store minimum cost and best solution
        ind_best = np.argmin(pop_cost)
        if id_iter == 0:
            minCost = [pop_cost[ind_best]]
            bestSol = [pop_chrom[ind_best]]
        else:
            minCost = np.vstack((minCost,pop_cost[ind_best]))
            bestSol = np.vstack((bestSol,pop_chrom[ind_best]))

    # return values
    ind_best_cost = np.argmin(minCost)
    best_theta = bestSol[ind_best_cost]
    best_score = minCost

    return best_score.flatten() ,best_theta.flatten(),best_score[-1]


'''
------------------------------------------
                    DE_par
Paralell Classic Differential Evolution

-------------------------------------------
## Implemented as a minimization algorithm

# Inputs:
    * f_cost        - function to be minimized
    * pop_size      - number of individuals in the population
    * max_iters     - maximum number of optimization iterations
    * pc            - crossover probability
    * lb
    * ub
    * step_size
    * theta_0

# Output
    * best_theta    - best solution found
    * best_score    - history of best score
'''




def init_pool(main_nparray_chrom_par,main_nparray_cost_par):
    global main_nparray_chrom
    global main_nparray_cost

    main_nparray_chrom = main_nparray_chrom_par
    main_nparray_cost = main_nparray_cost_par

def eval_de(arguments):
    id_iter,id_pop,pc,n_dim,step_size,pop_size,lb,ub,f_cost = arguments
    # pick candidate solution
    xi = main_nparray_chrom[id_iter][id_pop]
    # ids_cs vector containing the indexes of
    # the all other candidate solution but xi
    ids_cs = np.linspace(0, pop_size - 1, pop_size, dtype = int)
    # remove id_pop from ids_cs
    ids_cs = np.where(ids_cs != id_pop)
    # convert tuple to ndarray
    ids_cs = np.asarray(ids_cs)[0]
    # randomly pick 3 candidate solution using indexes ids_cs
    xa , xb , xc = main_nparray_chrom[id_iter][np.random.choice(ids_cs, 3, replace = False)]
    V1 = xa
    V2 = xb
    Vb = xc
    # create the difference vector
    Vd = V1 - V2
    # create the mutant vector
    Vm = Vb + step_size*Vd
    # make sure the mutant vector is in [lb,ub]
    Vm = np.clip(Vm,lb,ub)
    # create a trial vector by recombination
    Vt = np.zeros(n_dim)
    jr = np.random.rand()   # index of the dimension
                            # that will under crossover
                            # regardless of pc
    for id_dim in range(n_dim):
        rc = np.random.rand()
        if rc < pc or id_dim == jr:
            # perform recombination
            Vt[id_dim] = Vm[id_dim]
        else:
            # copy from Vb
            Vt[id_dim] = xi[id_dim]
    # obtain the cost of the trial vector
    vt_cost = f_cost(Vt)
    # select the id_pop individual for the next generation
    if vt_cost < main_nparray_cost[id_iter][id_pop]:
        main_nparray_chrom[id_iter][id_pop] = Vt
        main_nparray_cost[id_iter][id_pop] = vt_cost

        
def DE_par(f_cost,pop_size,max_iters,pc,lb,ub,step_size = 0.4, theta_0 = None):
    # problem dimension
    n_dim = np.shape(lb)[0]
    # randomly initialize the population
    pop_chrom = (ub - lb) * np.random.random_sample(size = (pop_size,n_dim)) + lb

    if theta_0 is not None:
        pop_chrom[0] = theta_0
    
    NBR_ITEMS_IN_ARRAY_CHROM = pop_size * max_iters * n_dim
    NBR_ITEMS_IN_ARRAY_COST = pop_size * max_iters

    # Create shared array by pop_chrom
    shared_array_based = Array(ctypes.c_double,NBR_ITEMS_IN_ARRAY_CHROM,lock = False)
    main_nparray_chrom = np.frombuffer(shared_array_based, dtype = ctypes.c_double)
    main_nparray_chrom = main_nparray_chrom.reshape((max_iters,
                                        pop_size,
                                        n_dim))

    main_nparray_chrom[0] = pop_chrom

    # Create shared array by pop_cost
    shared_array_based = Array(ctypes.c_double,NBR_ITEMS_IN_ARRAY_COST,lock = False)
    main_nparray_cost = np.frombuffer(shared_array_based, dtype = ctypes.c_double)
    main_nparray_cost = main_nparray_cost.reshape((max_iters,pop_size))
    # obtain the cost of each solution
    pop_cost = np.zeros(pop_size)

    for id_p in range(pop_size):
        pop_cost[id_p] = f_cost(pop_chrom[id_p])

    main_nparray_cost[0] = pop_cost

        # optimization
    for tiempo in range(max_iters-1):
        id_iter = 0
        print("-----------------------------")
        print("-%%%%%%%%%%%%%%%%%%%%%%%%%%%-")
        print("        Iteración {}".format(tiempo))
        print("-%%%%%%%%%%%%%%%%%%%%%%%%%%%-")
        print("-----------------------------")

        # start the MP pool for asynchronous parallelization
        pool = Pool(int(cpu_count()/2),initializer=init_pool, initargs=(main_nparray_chrom,main_nparray_cost,))
        pool.map(eval_de,[(id_iter,i,pc,n_dim,step_size,pop_size,lb,ub,f_cost) for i in range(pop_size)])
        pool.close()
        pool.join()
        print(np.min(main_nparray_cost[0]))
        # store minimum cost and best solution
        ind_best = np.argmin(main_nparray_cost[id_iter])
        if tiempo == 0:
            minCost = [main_nparray_cost[id_iter][ind_best]]
            bestSol = [main_nparray_chrom[id_iter][ind_best]]
        else:
            minCost = np.vstack((minCost,main_nparray_cost[id_iter][ind_best]))
            bestSol = np.vstack((bestSol,main_nparray_chrom[id_iter][ind_best]))

    # return values
    ind_best_cost = np.argmin(minCost)
    best_theta = bestSol[ind_best_cost]
    best_score = minCost

    print(best_score)
    return best_score.flatten() ,best_theta.flatten(),best_score[-1]

'''
------------------------------------------
                    PSO
        Particle Swarm Optimization

-------------------------------------------
## Implemented as a minimization algorithm

# Inputs:
    * f_cost        - function to be minimized
    * pop_size      - number of individuals in the population
    * max_iters     - maximum number of optimization iterations
    * lb            - lower bounds
    * ub            - upper bounds
    * α             - cognitive scaling parameter
    * β             - social scaling parameter
    * w             - velocity inertia 
    * w_min         - minimum value for the velocity inertia
    * w_max         - maximum value for the velocity inertia
# Output
    * best_theta    - best solution found
    * best_score    - history of best score
'''

    
def init_pso(gbest_val_arg, gbest_pos_arg, position_arg, velocity_arg, pbest_val_arg, 
         pbest_pos_arg,f_optim,α_arg,β_arg,w_arg,vMax_arg,vMin_arg,
         u_bounds_arg,l_bounds_arg):
    global gbest_val
    global gbest_pos
    global position
    global velocity
    global pbest_val
    global pbest_pos
    global f
    global α
    global β
    global w
    global vMax
    global vMin
    global u_bounds
    global l_bounds

    gbest_val = gbest_val_arg
    gbest_pos = gbest_pos_arg
    position = position_arg
    velocity = velocity_arg
    pbest_val = pbest_val_arg
    pbest_pos = pbest_pos_arg
    f = f_optim
    
    # Cognitive scaling parameter
    α = α_arg
    # Social scaling parameter
    β = β_arg
    
    # velocity inertia
    w = w_arg
    
    vMax = vMax_arg
    vMin = vMin_arg
    u_bounds = u_bounds_arg
    l_bounds = l_bounds_arg
    
def evalua_f_pso(i):    
    # Actualiza velocidad de la partícula
    ϵ1,ϵ2 = np.random.RandomState().uniform(), np.random.RandomState().uniform()
    with gbest_pos.get_lock():
        velocity[i] = w.value*velocity[i] + α*ϵ1*(pbest_pos[i] -  position[i]) + β*ϵ2*(np.array(gbest_pos[:]) - position[i])

            
    # Ajusta velocidad de la partícula
    index_vMax = np.where(velocity[i] > vMax)
    index_vMin = np.where(velocity[i] < vMin)

    if np.array(index_vMax).size > 0:
        velocity[i][index_vMax] = vMax[index_vMax]
    if np.array(index_vMin).size > 0:
        velocity[i][index_vMin] = vMin[index_vMin]

    # Actualiza posición de la partícula
    position[i] = position[i] + velocity[i] 

    # Ajusta posición de la particula
    index_pMax = np.where(position[i] > u_bounds)
    index_pMin = np.where(position[i] < l_bounds)

    if np.array(index_pMax).size > 0:
        position[i][index_pMax] = u_bounds[index_pMax]
    if np.array(index_pMin).size > 0:
        position[i][index_pMin] = l_bounds[index_pMin]

    # Evaluamos la función
    y = f(position[i])
    with gbest_val.get_lock():
        if y < gbest_val.value:
            with gbest_pos.get_lock(): 
                gbest_pos[:] = np.copy(position[i]) 
                pbest_pos[i] = np.copy(position[i])
                gbest_val.value = y
        if y < pbest_val[i]:
            pbest_pos[i] = np.copy(position[i])

def PSO(f_cost,pop_size,max_iters,lb,ub,α,β,w,w_max,w_min):
    # Tamaño de la población
    n = pop_size
    maxiter = max_iters
    # Número de variables
    n_var = len(lb)

    # Cognitive scaling parameter
    α = α
    # Social scaling parameter
    β = β

    # velocity inertia
    w = Value(ctypes.c_double,w)
    # minimum value for the velocity inertia
    w_min = w_min
    # maximum value for the velocity inertia
    w_max = w_max

    # Usamos Latin Hypercube Sampling para muestrear puntos en el espacio de búsqueda
    engine = LatinHypercube(d=n_var)
    sample = engine.random(n=n)

    # Definimos los límites superiores e inferiores para las variables de decisión
    l_bounds = np.array(lb)
    u_bounds = np.array(ub)

    # Creamos un arreglo compartido para el vector de limites superiores
    mp_l_bounds = Array(ctypes.c_double,l_bounds)
    # Creamos un nuevo arreglo de numpy usando el arreglo compartido
    np_l_bounds = np.frombuffer(mp_l_bounds.get_obj(), ctypes.c_double) 

    # Creamos un arreglo compartido para el vector de limites superiores
    mp_u_bounds = Array(ctypes.c_double,u_bounds)
    # Creamos un nuevo arreglo de numpy usando el arreglo compartido
    np_u_bounds = np.frombuffer(mp_u_bounds.get_obj(), ctypes.c_double) 

    # Velocidad máxima
    vMax = np.multiply(u_bounds-l_bounds,0.2)
    # Creamos un arreglo compartido para el vector de velocidad máxima
    mp_vMax = Array(ctypes.c_double,vMax) 
    # Creamos un nuevo arreglo de numpy usando el arreglo compartido
    np_vMax = np.frombuffer(mp_vMax.get_obj(), ctypes.c_double) 

    # Velocidad mínima
    vMin = -vMax
    # Creamos un arreglo compartido para el vector de velocidad máxima
    mp_vMin = Array(ctypes.c_double,vMin) 
    # Creamos un nuevo arreglo de numpy usando el arreglo compartido
    np_vMin = np.frombuffer(mp_vMin.get_obj(), ctypes.c_double) 


    # Escalamos los valores muestreados de LHS
    sample_scaled = scale(sample,l_bounds, u_bounds)

    # Creamos un arreglo compartido para el vector de velocidad
    mp_vel = Array(ctypes.c_double,n*n_var)
    # Creamos un nuevo arreglo de numpy usando el arreglo compartido
    vel = np.frombuffer(mp_vel.get_obj(), ctypes.c_double)
    # Convertimos a un arreglo 2-dimensional
    vel_resh = vel.reshape((n,n_var))

    # Creamos un arreglo compartido para el vector de posición
    mp_pos = Array(ctypes.c_double,n*n_var)
    # Creamos un nuevo arreglo de numpy usando el arreglo compartido
    pos = np.frombuffer(mp_pos.get_obj(), ctypes.c_double)
    # Convertimos a un arreglo 2-dimensional
    pos_resh = pos.reshape((n,n_var))
    # Inicializamos el vector de posición con el vector muestreado por LHS
    for i,v in enumerate(sample_scaled):
        pos_resh[i] = v

    # Mejor valor global (compartido) de la función objetivo
    gbest_val = Value(ctypes.c_double,math.inf)
    # Mejor vector de posición global (compartido)
    gbest_pos = Array(ctypes.c_double, sample_scaled[0])

    # Mejor valor para cada partícula
    pbest_val_arg = Array(ctypes.c_double, [math.inf]*n )

    # Mejor vector de posición individual para cada partícula
    pbest_pos_mp = Array(ctypes.c_double,n*n_var)
    # Creamos un nuevo arreglo de numpy usando el arreglo compartido
    pbest_pos = np.frombuffer(pbest_pos_mp.get_obj(), ctypes.c_double)
    # Convertimos a un arreglo 2-dimensional
    pbest_pos_arg = pbest_pos.reshape((n,n_var))
    # Inicializamos el vector de posición con el vector muestreado por LHS
    for i,v in enumerate(sample_scaled):
        pbest_pos_arg[i] = v

    p = Pool(processes = int(cpu_count()),initializer=init_pso,
            initargs=(gbest_val,gbest_pos,pos_resh, vel_resh, 
                      pbest_val_arg, pbest_pos_arg, f_cost,α,β,w,
                      np_vMax,np_vMin,np_u_bounds,np_l_bounds,))

    fitness_values = []
    for k in range(maxiter):
        p.map(evalua_f_pso, range(n))
        print("It {}  gbest_val {}".format(k, gbest_val.value))

        # Actualizamos w
        w.value = w_max - k * ((w_max-w_min)/maxiter)

        fitness_values.append(gbest_val.value)

    return fitness_values, gbest_pos[:], gbest_val.value

