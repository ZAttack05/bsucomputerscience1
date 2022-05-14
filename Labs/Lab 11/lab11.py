import time

'''The main function of the program.'''
def main():
    c = 0 #Final time variable
    offset = 1000 #Offset variable
    times = [] #List for time results 
    results = [] #List for results results
    o = [] #List for range results
    f = open("times.csv", "w")
    '''Runs and times the recursive algorithm'''
    for i in range(-offset, offset, 10):
        o.append(i)
        a = time.time()
        results.append(solvie(i, offset))
        b = time.time()
        times.append(b - a)
    '''Creates the CSV file.'''
    f.write("%s, %s, %s\n"%("Iterations", "Results", "Times"))
    for i in range(len(results)):
        f.write("%f, %f, %f\n"%(o[i], results[i], times[i]))
    f.close()
    
    '''Creates a result list and calls the recursive function'''
def solvie(n, offset):
    results = [None for i in range(offset * 2)]
    return h(n, results, offset)

'''Checks if result is saved to save time, otherwise calculates.'''
def h(n, results, offset):
    if results[n + offset] != None:
        return results[n + offset]
    if n < -5:
        results[n + offset] = h(n+4,results, offset) + h(n+2,results, offset)
        return results[n + offset]
    elif -5 <= n and n < 2:
        results[n + offset] = n * 2
        return results[n + offset]
    elif n >= 2:
        results[n + offset] = h(n-8, results, offset) - h(n-4,results, offset) + h(n-3,results, offset)
        return results[n + offset]

'''Calls main'''
if __name__ == '__main__':
    main()