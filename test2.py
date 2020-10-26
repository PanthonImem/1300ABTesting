from scipy import stats
from scipy.stats import t as t_dist
from scipy.stats import chi2
import math
from abtesting_test import *

# TODO: Fill in the following functions! Be sure to delete "pass" when you want to use/run a function!
# NOTE: You should not be using any outside libraries or functions other than the simple operators (+, **, etc)
# and the specifically mentioned functions (i.e. round, cdf functions...)

def slice_2D(list_2D, start_row, end_row, start_col, end_col):
    '''
    Splices a the 2D list via start_row:end_row and start_col:end_col
    :param list: list of list of numbers
    :param nums: start_row, end_row, start_col, end_col
    :return: the spliced 2D list (ending indices are exclsive)
    '''
    to_append = []
    for l in range(start_row, end_row):
        to_append.append(list_2D[l][start_col:end_col])

    return to_append

def get_avg(nums):
    '''
    Helper function for calculating the average of a sample.
    :param nums: list of numbers
    :return: average of list
    '''
    #TODO: fill me in!
    mysum = 0
    for num in nums:
        mysum+=num
    return mysum/len(nums)

def get_stdev(nums):
    '''
    Helper function for calculating the standard deviation of a sample.
    :param nums: list of numbers
    :return: standard deviation of list
    '''
    #TODO: fill me in!
    mymean = get_avg(nums)
    mysum = 0
    for num in nums:
        mysum+= (num-mymean)**2
    return math.sqrt(mysum/(len(nums)-1))

def get_standard_error(a, b):
    '''
    Helper function for calculating the standard error, given two samples.
    :param a: list of numbers
    :param b: list of numbers
    :return: standard error of a and b (see studio 6 guide for this equation!)
    '''
    #TODO: fill me in!
    return math.sqrt(get_stdev(a)**2/len(a)+ get_stdev(b)**2/len(b)) 

def get_2_sample_df(a, b):
    '''
    Calculates the combined degrees of freedom between two samples.
    :param a: list of numbers
    :param b: list of numbers
    :return: integer representing the degrees of freedom between a and b (see studio 6 guide for this equation!)
    HINT: you can use Math.round() to help you round!
    '''
    #TODO: fill me in!
    se = get_standard_error(a, b)
    stda = get_stdev(a)
    stdb = get_stdev(b)
    na = len(a)
    nb = len(b)
    x = se**4/((((stda**2)/na)**2/(na-1))+(((stdb**2)/nb)**2/(nb-1)))
    return round(x)

def get_t_score(a, b):
    '''
    Calculates the t-score, given two samples.
    :param a: list of numbers
    :param b: list of numbers
    :return: number representing the t-score given lists a and b (see studio 6 guide for this equation!)
    '''
    #TODO: fill me in!
    t = (get_avg(a)-get_avg(b))/get_standard_error(a,b)
    if(t>0):
        t = t*-1
    return t

def perform_2_sample_t_test(a, b):
    '''
    ** DO NOT CHANGE THE NAME OF THIS FUNCTION!! ** (this will mess with our autograder)
    Calculates a p-value by performing a 2-sample t-test, given two lists of numbers.
    :param a: list of numbers
    :param b: list of numbers
    :return: calculated p-value
    HINT: the t_dist.cdf() function might come in handy!
    '''
    #TODO: fill me in!
    t = get_t_score(a,b)
    return t_dist.cdf(t, get_2_sample_df(a,b))


# [OPTIONAL] Some helper functions that might be helpful in get_expected_grid().
def row_sum(observed_grid, ele_row):
    mysum = 0
    for col in range(len(observed_grid[0])):
        #print(ele_row, col)
        mysum+=observed_grid[ele_row][col]
    return mysum
        
def col_sum(observed_grid, ele_col):

    mysum = 0
    for row in range(len(observed_grid)):
        mysum+=observed_grid[row][ele_col]
    return mysum

def total_sum(observed_grid):
    mysum = 0
    for row in range(len(observed_grid)):
        for col in range(len(observed_grid[0])):
            mysum+=observed_grid[row][col]
    return mysum

def calculate_expected(row_sum, col_sum, tot_sum):
    return (row_sum*col_sum)/tot_sum

def get_expected_grid(observed_grid):
    '''
    Calculates the expected counts, given the observed counts.
    ** DO NOT modify the parameter, observed_grid. **
    :param observed_grid: 2D list of observed counts
    :return: 2D list of expected counts
    HINT: To clean up this calculation, consider filling in the optional helper functions below!
    '''
    #TODO: fill me in!
    bigls = []
    tot_sum = total_sum(observed_grid)
    for row in range(len(observed_grid)):
        rowls = []
        for col in range(len(observed_grid[0])):
            rowls.append(calculate_expected(row_sum(observed_grid,row),col_sum(observed_grid,col),tot_sum))
        bigls.append(rowls)
    return bigls

def df_chi2(observed_grid):
    '''
    Calculates the degrees of freedom of the expected counts.
    :param observed_grid: 2D list of observed counts
    :return: degrees of freedom of expected counts (see studio 6 guide for this equation!)
    '''
    #TODO: fill me in!
    return ((len(observed_grid)-1) * (len(observed_grid[0])-1))

def chi2_value(observed_grid):
    '''
    Calculates the chi^2 value of the expected counts.
    :param observed_grid: 2D list of observed counts
    :return: associated chi^2 value of expected counts (see studio 6 guide for this equation!)
    '''
    expected_grid = get_expected_grid(observed_grid)
    mysum = 0
    for row in range(len(observed_grid)):
        for col in range(len(observed_grid[0])):
            mysum+= ((observed_grid[row][col] - expected_grid[row][col])**2)/expected_grid[row][col]
    return mysum

def perform_chi2_homogeneity_test(observed_grid):
    '''
    ** DO NOT CHANGE THE NAME OF THIS FUNCTION!! ** (this will mess with our autograder)
    Calculates the p-value by performing a chi^2 test, given a list of observed counts
    :param observed_grid: 2D list of observed counts
    :return: calculated p-value
    HINT: the chi2.cdf() function might come in handy!
    '''
    #TODO: fill me in!
    return 1-chi2.cdf(chi2_value(observed_grid),df_chi2(observed_grid))

# These commented out lines are for testing your main functions. 
# Please uncomment them when finished with your implementation and confirm you get the same values :)
def data_to_num_list(s):
  '''
    Takes a copy and pasted row/col from a spreadsheet and produces a usable list of nums. 
    This will be useful when you need to run your tests on your cleaned log data!
    :param str: string holding data
    :return: the spliced list of numbers
    '''
  return list(map(float, s.split()))
a_count = [16, 7]
b_count = [7, 6]
observed_grid = [a_count, b_count]
print(chi2_value(observed_grid))
print(perform_chi2_homogeneity_test(observed_grid)) 