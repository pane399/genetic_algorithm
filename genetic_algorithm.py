import fuctions as fun
import random
from matplotlib import pyplot as plt

answer = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2]
population = 10
max_fitness = 0
result = 1

avg_fitness = []
    
next_gen = [[col for col in range(10)] for row in range(10)]
new_parents = [[col for col in range(10)] for row in range(10)]
    
# 1st generation 생성
new_parents = fun.make_gen(new_parents)

new_parents = fun.fit_gen(new_parents, new_parents, answer, population)

avg_fitness.append(fun.average_fitness(new_parents))

new_parents = sorted(new_parents, reverse = True)[:5]

fun.del_fit(new_parents, next_gen, population)

max_fitness = fun.check_max(new_parents, answer, max_fitness)

next_gen = fun.crossover(new_parents)

# algorithm 반복
while max_fitness != 10:
    new_parents = next_gen
    
    new_parents = fun.fit_gen(new_parents, next_gen, answer, population)
    
    avg_fitness.append(fun.average_fitness(new_parents))
    
    new_parents = sorted(new_parents, reverse = True)[:5]    
    
    fun.del_fit(new_parents, next_gen, population)
    
    max_fitness = fun.check_max(new_parents, answer, max_fitness)
       
    next_gen = fun.crossover(new_parents)
    
    result += 1
    if result >= 1000000:
        break

# Result
print("max", max_fitness)
print("The result is %d" %result)

# Graph 출력
plt.plot(avg_fitness)
plt.xlabel('Generation')
plt.ylabel('Avg fitness')
plt.title('Mutation random')
plt.show()