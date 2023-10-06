# File Name : SC_stats_module.py

# judgement of whether it is a valid input
def is_numeric(num) :
    try :
        float(num)
        return True
    except ValueError :
        return False

# another way to do the is_numeric() is :
# "3.14".replace('.','',1).isdigit()


# all the functions defined
def menu():
    print('''Hello Dear user, this is a statistic tool that you can use to compute the following statistics. Please enter the number and then \"done\" to indicate you finish entering the number. Here are some statistics you can compute: \n
    1. Enter 1 to Return the Mean \n
    2. Enter 2 to Return the Variance \n
    3. Enter 3 to Return the Standard Deviation \n
    4. Enter 4 to Return the Standard Error \n
    5. Enter 5 to Return the Z-score \n
    6. Enter 6 to Return the Summary of Basic Statistics \n
    7. Enter \"restart\" to restart the program \n
    8. Enter \"quit\" if you want to quit the program \n ''')

    
def mean(all_nums) : 
    avg = sum(all_nums) / len(all_nums)
    return avg

def variance(all_nums) :
    avg = mean(all_nums)
    sumV = sum([(num - avg) ** 2 for num in all_nums])
    var = sumV / len(all_nums)
    return var

def sd(all_nums) :
    from math import sqrt
    var = variance(all_nums)
    standardD = sqrt(var)
    return standardD

def se(all_nums) :
    from math import sqrt
    avg = mean(all_nums)
    standardD = sd(all_nums)
    standardE = (avg - standardD) / sqrt(len(all_nums))
    return standardE

def zscore(observation, all_nums) :
    avg = mean(all_nums)
    standardD = sd(all_nums)
    z_score = (observation - avg) / standardD
    return z_score

# Summary of the statistics
def summary(observation, all_nums) :
    avg = mean(all_nums)
    var = variance(all_nums)
    standardD = sd(all_nums)
    standardE = se(all_nums)
    z_score = zscore(observation, all_nums)
    
    print(f'''Summary of Basic Statistics : \n 
    Mean : {avg} \n
    Variance : {var} \n
    Standard Deviation : {standardD} \n
    Standard Error : {standardE} \n
    Z-score for {observation} : {z_score} \n ''')
    
 