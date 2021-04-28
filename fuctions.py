import random

def fit_gen(parents, solution, answer, num):
    for i in range(0, num): # 답안 생성 후 fitness check
        parents[i].insert(0, fitness_check(solution[i], answer))
    return parents
       
def del_fit(parents, solution, num):    
    for i in range(0, num): # fitness값 list에서 제거
        solution[i] = solution[i][1:]
        
    for i in range(0, int(num / 2)): # fitness값 list에서 제거
        parents[i] = parents[i][1:]
    

def mutation_swap(solution): # swap하는 mutation
    pivot = random.randrange(0, len(solution) - 1)
    temp = solution[pivot + 1]
    solution[pivot + 1] = solution[pivot]
    solution[pivot] = temp
    
    return solution

def mutation_rand(solution): # random한 수를 random한 자리에 넣는 mutation
    pivot = random.randrange(0,len(solution))
    solution[pivot] = random.randrange(1,5)
    
    return solution
    
def make_gen(array): # 무작위 답안 생성
    for i in range(0, 10):
        for j in range(0, 10):
            array[i][j] = random.randrange(1, 5)
    return array

def print_check(array): # 리스트 출력
    for i in array:
        for j in i:
            print(j, end = " ")
        print()
        
def fitness_check(parents, answer): # fitness 값 확인
    count = 0;
    for i in range(0, len(parents)):
        if parents[i] == answer[i]:
            count += 1
    return count

def crossover(parents): # parents를 통한 crossover
    mutation_rate = 0.10
    
    child = [[col for col in range(10)] for row in range(10)]
    
    child[0] = parents[0]
    for i in range(1, 4):
        child[i] = parents[i][:6] + parents[i + 1][6:]
    child[4] = parents[4][:6] + parents[0][6:]
    
    for i in range(0, 4):
        child[i + 5] = parents[i][:4] + parents[i + 1][4:]
    child[9] = parents[4][:4] + parents[0][4:]
    
    for i in range(1, 10):
        if mutation_rate > random.random():
            # child[i] = mutation_swap(child[i])
            child[i] = mutation_rand(child[i])
    return child

def check_max(parents, answer, max):
    max_fitness = max
    
    for i in range(0, 5):
        if fitness_check(parents[i], answer) > max_fitness:
            max_fitness = fitness_check(parents[i], answer)
    return max_fitness

def average_fitness(parents):
    total_fit = 0
    for i in range(0, 10):
        total_fit += sum(parents[i][:1])
    total_fit /= 10
    return total_fit