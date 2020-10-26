{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.029632767723285252\n",
      "0.9703672322767147\n",
      "0.9769568982251158\n",
      "0.023043101774884223\n"
     ]
    }
   ],
   "source": [
    "from scipy import stats\n",
    "from scipy.stats import t as t_dist\n",
    "from scipy.stats import chi2\n",
    "import math\n",
    "from abtesting_test import *\n",
    "\n",
    "# You can comment out these lines! They are just here to help follow along to the tutorial.\n",
    "print(t_dist.cdf(-2, 20)) # should print .02963\n",
    "print(t_dist.cdf(2, 20)) # positive t-score (bad), should print .97036 (= 1 - .2963)\n",
    "\n",
    "print(chi2.cdf(23.6, 12)) # prints 0.976\n",
    "print(1 - chi2.cdf(23.6, 12)) # prints 1 - 0.976 = 0.023 (yay!)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# TODO: Fill in the following functions! Be sure to delete \"pass\" when you want to use/run a function!\n",
    "# NOTE: You should not be using any outside libraries or functions other than the simple operators (+, **, etc)\n",
    "# and the specifically mentioned functions (i.e. round, cdf functions...)\n",
    "\n",
    "def slice_2D(list_2D, start_row, end_row, start_col, end_col):\n",
    "    '''\n",
    "    Splices a the 2D list via start_row:end_row and start_col:end_col\n",
    "    :param list: list of list of numbers\n",
    "    :param nums: start_row, end_row, start_col, end_col\n",
    "    :return: the spliced 2D list (ending indices are exclsive)\n",
    "    '''\n",
    "    to_append = []\n",
    "    for l in range(start_row, end_row):\n",
    "        to_append.append(list_2D[l][start_col:end_col])\n",
    "\n",
    "    return to_append\n",
    "\n",
    "def get_avg(nums):\n",
    "    '''\n",
    "    Helper function for calculating the average of a sample.\n",
    "    :param nums: list of numbers\n",
    "    :return: average of list\n",
    "    '''\n",
    "    #TODO: fill me in!\n",
    "    mysum = 0\n",
    "    for num in nums:\n",
    "        mysum+=num\n",
    "    return mysum/len(nums)\n",
    "\n",
    "def get_stdev(nums):\n",
    "    '''\n",
    "    Helper function for calculating the standard deviation of a sample.\n",
    "    :param nums: list of numbers\n",
    "    :return: standard deviation of list\n",
    "    '''\n",
    "    #TODO: fill me in!\n",
    "    mymean = get_avg(nums)\n",
    "    mysum = 0\n",
    "    for num in nums:\n",
    "        mysum+= (num-mymean)**2\n",
    "    return math.sqrt(mysum/(len(nums)-1))\n",
    "\n",
    "def get_standard_error(a, b):\n",
    "    '''\n",
    "    Helper function for calculating the standard error, given two samples.\n",
    "    :param a: list of numbers\n",
    "    :param b: list of numbers\n",
    "    :return: standard error of a and b (see studio 6 guide for this equation!)\n",
    "    '''\n",
    "    #TODO: fill me in!\n",
    "    return math.sqrt(get_stdev(a)**2/len(a)+ get_stdev(b)**2/len(b)) \n",
    "\n",
    "def get_2_sample_df(a, b):\n",
    "    '''\n",
    "    Calculates the combined degrees of freedom between two samples.\n",
    "    :param a: list of numbers\n",
    "    :param b: list of numbers\n",
    "    :return: integer representing the degrees of freedom between a and b (see studio 6 guide for this equation!)\n",
    "    HINT: you can use Math.round() to help you round!\n",
    "    '''\n",
    "    #TODO: fill me in!\n",
    "    se = get_standard_error(a, b)\n",
    "    stda = get_stdev(a)\n",
    "    stdb = get_stdev(b)\n",
    "    na = len(a)\n",
    "    nb = len(b)\n",
    "    x = se**4/((((stda**2)/na)**2/(na-1))+(((stdb**2)/nb)**2/(nb-1)))\n",
    "    return round(x)\n",
    "\n",
    "def get_t_score(a, b):\n",
    "    '''\n",
    "    Calculates the t-score, given two samples.\n",
    "    :param a: list of numbers\n",
    "    :param b: list of numbers\n",
    "    :return: number representing the t-score given lists a and b (see studio 6 guide for this equation!)\n",
    "    '''\n",
    "    #TODO: fill me in!\n",
    "    t = (get_avg(a)-get_avg(b))/get_standard_error(a,b)\n",
    "    if(t>0):\n",
    "        t = t*-1\n",
    "    return t\n",
    "\n",
    "def perform_2_sample_t_test(a, b):\n",
    "    '''\n",
    "    ** DO NOT CHANGE THE NAME OF THIS FUNCTION!! ** (this will mess with our autograder)\n",
    "    Calculates a p-value by performing a 2-sample t-test, given two lists of numbers.\n",
    "    :param a: list of numbers\n",
    "    :param b: list of numbers\n",
    "    :return: calculated p-value\n",
    "    HINT: the t_dist.cdf() function might come in handy!\n",
    "    '''\n",
    "    #TODO: fill me in!\n",
    "    t = get_t_score(a,b)\n",
    "    return t_dist.cdf(t, get_2_sample_df(a,b))\n",
    "\n",
    "\n",
    "# [OPTIONAL] Some helper functions that might be helpful in get_expected_grid().\n",
    "def row_sum(observed_grid, ele_row):\n",
    "    mysum = 0\n",
    "    for col in range(len(observed_grid[0])):\n",
    "        #print(ele_row, col)\n",
    "        mysum+=observed_grid[ele_row][col]\n",
    "    return mysum\n",
    "        \n",
    "def col_sum(observed_grid, ele_col):\n",
    "\n",
    "    mysum = 0\n",
    "    for row in range(len(observed_grid)):\n",
    "        mysum+=observed_grid[row][ele_col]\n",
    "    return mysum\n",
    "\n",
    "def total_sum(observed_grid):\n",
    "    mysum = 0\n",
    "    for row in range(len(observed_grid)):\n",
    "        for col in range(len(observed_grid[0])):\n",
    "            mysum+=observed_grid[row][col]\n",
    "    return mysum\n",
    "\n",
    "def calculate_expected(row_sum, col_sum, tot_sum):\n",
    "    return (row_sum*col_sum)/tot_sum\n",
    "\n",
    "def get_expected_grid(observed_grid):\n",
    "    '''\n",
    "    Calculates the expected counts, given the observed counts.\n",
    "    ** DO NOT modify the parameter, observed_grid. **\n",
    "    :param observed_grid: 2D list of observed counts\n",
    "    :return: 2D list of expected counts\n",
    "    HINT: To clean up this calculation, consider filling in the optional helper functions below!\n",
    "    '''\n",
    "    #TODO: fill me in!\n",
    "    bigls = []\n",
    "    tot_sum = total_sum(observed_grid)\n",
    "    for row in range(len(observed_grid)):\n",
    "        rowls = []\n",
    "        for col in range(len(observed_grid[0])):\n",
    "            rowls.append(calculate_expected(row_sum(observed_grid,row),col_sum(observed_grid,col),tot_sum))\n",
    "        bigls.append(rowls)\n",
    "    return bigls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def df_chi2(observed_grid):\n",
    "    '''\n",
    "    Calculates the degrees of freedom of the expected counts.\n",
    "    :param observed_grid: 2D list of observed counts\n",
    "    :return: degrees of freedom of expected counts (see studio 6 guide for this equation!)\n",
    "    '''\n",
    "    #TODO: fill me in!\n",
    "    return ((len(observed_grid)-1) * (len(observed_grid[0])-1))\n",
    "\n",
    "def chi2_value(observed_grid):\n",
    "    '''\n",
    "    Calculates the chi^2 value of the expected counts.\n",
    "    :param observed_grid: 2D list of observed counts\n",
    "    :return: associated chi^2 value of expected counts (see studio 6 guide for this equation!)\n",
    "    '''\n",
    "    expected_grid = get_expected_grid(observed_grid)\n",
    "    mysum = 0\n",
    "    for row in range(len(observed_grid)):\n",
    "        for col in range(len(observed_grid[0])):\n",
    "            mysum+= ((observed_grid[row][col] - expected_grid[row][col])**2)/expected_grid[row][col]\n",
    "    return mysum\n",
    "\n",
    "def perform_chi2_homogeneity_test(observed_grid):\n",
    "    '''\n",
    "    ** DO NOT CHANGE THE NAME OF THIS FUNCTION!! ** (this will mess with our autograder)\n",
    "    Calculates the p-value by performing a chi^2 test, given a list of observed counts\n",
    "    :param observed_grid: 2D list of observed counts\n",
    "    :return: calculated p-value\n",
    "    HINT: the chi2.cdf() function might come in handy!\n",
    "    '''\n",
    "    #TODO: fill me in!\n",
    "    return 1-chi2.cdf(chi2_value(observed_grid),df_chi2(observed_grid))\n",
    "\n",
    "# These commented out lines are for testing your main functions. \n",
    "# Please uncomment them when finished with your implementation and confirm you get the same values :)\n",
    "def data_to_num_list(s):\n",
    "  '''\n",
    "    Takes a copy and pasted row/col from a spreadsheet and produces a usable list of nums. \n",
    "    This will be useful when you need to run your tests on your cleaned log data!\n",
    "    :param str: string holding data\n",
    "    :return: the spliced list of numbers\n",
    "    '''\n",
    "  return list(map(float, s.split()))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-129.50006781955568\n",
      "0.0\n"
     ]
    }
   ],
   "source": [
    "# t_test 1:\n",
    "a_t1_list = data_to_num_list(a1) \n",
    "b_t1_list = data_to_num_list(b1)\n",
    "print(get_t_score(a_t1_list, b_t1_list)) # this should be -129.500\n",
    "print(perform_2_sample_t_test(a_t1_list, b_t1_list)) # this should be 0.0000\n",
    "# why do you think this is? Take a peek at a1 and b1 in abtesting_test.py :)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-1.4883415839372593\n",
      "0.08237935428773466\n"
     ]
    }
   ],
   "source": [
    "# t_test 2:\n",
    "a_t2_list = data_to_num_list(a2) \n",
    "b_t2_list = data_to_num_list(b2)\n",
    "print(get_t_score(a_t2_list, b_t2_list)) # this should be -1.48834\n",
    "print(perform_2_sample_t_test(a_t2_list, b_t2_list)) # this should be .082379\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-2.8896915231301823\n",
      "0.005091269015030475\n"
     ]
    }
   ],
   "source": [
    "\n",
    "# t_test 3:\n",
    "a_t3_list = data_to_num_list(a3) \n",
    "b_t3_list = data_to_num_list(b3)\n",
    "print(get_t_score(a_t3_list, b_t3_list)) # this should be -2.88969\n",
    "print(perform_2_sample_t_test(a_t3_list, b_t3_list)) # this should be .005091\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4.103526475356585\n",
      "0.04279386669738383\n"
     ]
    }
   ],
   "source": [
    "\n",
    "# chi2_test 1:\n",
    "a_c1_list = data_to_num_list(a_count_1) \n",
    "b_c1_list = data_to_num_list(b_count_1)\n",
    "c1_observed_grid = [a_c1_list, b_c1_list]\n",
    "print(chi2_value(c1_observed_grid)) # this should be 4.103536\n",
    "print(perform_chi2_homogeneity_test(c1_observed_grid)) # this should be .0427939\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "33.8644445445335\n",
      "2.1161221397392183e-07\n"
     ]
    }
   ],
   "source": [
    "\n",
    "# chi2_test 2:\n",
    "a_c2_list = data_to_num_list(a_count_2) \n",
    "b_c2_list = data_to_num_list(b_count_2)\n",
    "c2_observed_grid = [a_c2_list, b_c2_list]\n",
    "print(chi2_value(c2_observed_grid)) # this should be 33.86444\n",
    "print(perform_chi2_homogeneity_test(c2_observed_grid)) # this should be 0.0000\n",
    "# Again, why do you think this is? Take a peek at a_count_2 and b_count_2 in abtesting_test.py :)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.3119402081820378\n",
      "0.576492029430312\n"
     ]
    }
   ],
   "source": [
    "\n",
    "# chi2_test 3:\n",
    "a_c3_list = data_to_num_list(a_count_3) \n",
    "b_c3_list = data_to_num_list(b_count_3)\n",
    "c3_observed_grid = [a_c3_list, b_c3_list]\n",
    "print(chi2_value(c3_observed_grid)) # this should be .3119402\n",
    "print(perform_chi2_homogeneity_test(c3_observed_grid)) # this should be .57649202\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Metric</th>\n",
       "      <th>Method</th>\n",
       "      <th>Chi2 Value</th>\n",
       "      <th>P-value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Return Rate</td>\n",
       "      <td>Chi-squared</td>\n",
       "      <td>0.3119</td>\n",
       "      <td>0.5765</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Metric       Method Chi2 Value P-value\n",
       "0  Return Rate  Chi-squared     0.3119  0.5765"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "['Time-to-complete-task', '2-sample t test', 'T-Score', 'P-value']"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "28426.833333333332 19058.777777777777\n",
      "-0.7951172488506587\n",
      "0.21794019450997243\n"
     ]
    }
   ],
   "source": [
    "#Calling Script for actual test\n",
    "import numpy as np\n",
    "a_list = [5449, 4879, 12027, 11884, 12163, 7447, 72481, 19995, 4722, 28675, 5922, 15992, 20488, 78763, 8194, 43247, 30635, 128720]\n",
    "b_list = [6716, 4200, 7020, 83496, 36912, 3611, 16756, 8069, 4749]\n",
    "\n",
    "print(np.mean(a_list),np.mean(b_list))\n",
    "print(get_t_score(a_list, b_list))\n",
    "print(perform_2_sample_t_test(a_list, b_list))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.8895202514513258\n",
      "0.34560734831052853\n"
     ]
    }
   ],
   "source": [
    "a_count = [16, 7]\n",
    "b_count = [7, 6]\n",
    "c2_observed_grid = [a_count, b_count]\n",
    "print(chi2_value(c2_observed_grid))\n",
    "print(perform_chi2_homogeneity_test(c2_observed_grid)) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Metric</th>\n",
       "      <th>Method</th>\n",
       "      <th>Chi2 Value</th>\n",
       "      <th>P-value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Return Rate</td>\n",
       "      <td>Chi-squared</td>\n",
       "      <td>0.8895</td>\n",
       "      <td>0.3456</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Metric       Method Chi2 Value P-value\n",
       "0  Return Rate  Chi-squared     0.8895  0.3456"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Metric</th>\n",
       "      <th>Method</th>\n",
       "      <th>T-score</th>\n",
       "      <th>P-value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Time to Complete Task</td>\n",
       "      <td>2-sample T test</td>\n",
       "      <td>-0.7951</td>\n",
       "      <td>0.2179</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                  Metric           Method  T-score P-value\n",
       "0  Time to Complete Task  2-sample T test  -0.7951  0.2179"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "df = pd.DataFrame([\n",
    "    ['Return Rate','Chi-squared','0.8895','0.3456']\n",
    "])\n",
    "df.columns = ['Metric','Method','Chi2 Value', 'P-value']\n",
    "display(df)\n",
    "\n",
    "\n",
    "df = pd.DataFrame([\n",
    "    ['Time to Complete Task','2-sample T test','-0.7951','0.2179']\n",
    "])\n",
    "df.columns = ['Metric','Method','T-score', 'P-value']\n",
    "display(df)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "28426.833333333332 32364.298291739102 128720 4722\n",
      "19058.777777777777 24851.636077497897 83496 3611\n"
     ]
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "print(np.mean(a_list),np.std(a_list), max(a_list), min(a_list))\n",
    "print(np.mean(b_list),np.std(b_list), max(b_list), min(b_list))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x432 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10,6))\n",
    "plt.pie([23,13], colors = ['green','orange'], labels = ['A(23)','B(13)'],autopct='%1.1f%%')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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y/L+Nix4RcQmEfG7iJgREX+JiFPK5edGxJMRMbV87N+oGiRJUvMMGDCAtrY2ttlmGw444ABeeOGFbrefPHky06dPr6i65mjkGK9FwOmZeV9EDAWmRMRvynUXZeb5DTy3JEmqEf/et61feU72uM0qq6zC1KlTATjuuOO45JJL+PznP9/l9pMnT2bs2LGMGjWq7joWLVrEwIH9Z8h6w1q8MnN2Zt5XTi8AZgAbNep8kiRpxbXrrrvy5JNPAjBz5kz2228/dtxxR97//vfz4IMPcuedd3LjjTdy5pln0tbWxsyZM9lzzz3fvHPN3Llzab994KRJkzj00EM54IAD2GeffZg0aRIHH3ww++23H1tssQWf/exnm/Uye1RJRIyIEcBo4G5gd+DkiBgH3EvRKvZ8J/uMB8YDbLrpplWUKUmSGmDx4sXccsstHH/88QCMHz+eSy+9lC222IK7776bE088kd/+9rcceOCBjB07lkMOOaTHY951111MmzaNddZZh0mTJjF16lT+9Kc/MXjwYLbccks+9alPsckmmzT6pfVawwfXR8TqwI+BUzPzReB7wOZAGzAbuKCz/TLzsswck5lj1l230/tMSpKkFdirr75KW1sbw4YN47nnnmPvvffmpZde4s477+TQQw+lra2NE044gdmzZ/f62HvvvTfrrLPOm/N77bUXa665JkOGDGHUqFE89liXt0tsqoYGr4gYRBG6rsrMGwAy85nMXJyZS4D/AnZuZA2SJKk52sd4PfbYY7z++utccsklLFmyhLXWWoupU6e++ZgxY0an+w8cOJAlS5YAvO2yDautttpS84MHD35zesCAASxatKiPX03faOSvGgOYCMzIzAtrlm9Qs9nHgQcaVYMkSWq+Nddck4svvpjzzz+fVVZZhZEjR3LdddcBxYVI77//fgCGDh3KggUL3txvxIgRTJkyBYDrr7+++sIboJEtXrsDxwIf7nDpiG9GxJ8jYhrwIeC0BtYgSZJWAKNHj2b77bfnmmuu4aqrrmLixIlsv/32bL311vz0pz8F4IgjjmDChAmMHj2amTNncsYZZ/C9732P3Xbbjblz5zb5FfSNyOz556DNNmbMmGz/VYMkSerZjBkz2GqrrZpdRsvr7H2OiCmZOaaz7b1yvSRJUkUMXpIkSRUxeEmSJFXE4CVJklQRg5ckSVJFDF6SJEkVMXhJkqSGiAhOP/30N+fPP/98zj333G73mTx5MtOnT+903bnnnstGG21EW1sbo0aN4uqrr+72WC+88ALf/e53e113I1Vyk2xJktRkP4y+Pd5RPV8HdPDgwdxwww2cffbZDB8+vK7DTp48mbFjxzJq1KhO15922mmcccYZPPzww+y4444ccsghDBo0qNNt24PXiSeeWNe52y1evJgBAwb0ap962eIlSZIaYuDAgYwfP56LLrrobesee+wx9tprL7bbbjv22msvHn/8ce68805uvPFGzjzzTNra2pg5c2aXx95iiy1YddVVef755wGYMGECO+20E9tttx3nnHMOAGeddRYzZ86kra2NM888k1tvvZWxY8e+eYyTTz6ZSZMmAcXtib785S+zxx57cN111zFixAjOOeccdthhB7bddlsefPDBPnlPDF6SJKlhTjrpJK666irmz5+/1PKTTz6ZcePGMW3aNI4++mg+/elPs9tuu3HggQcyYcIEpk6dyuabb97lce+77z622GIL1ltvPW6++WYefvhh7rnnHqZOncqUKVO4/fbbOe+889h8882ZOnUqEyZM6LHWIUOGcMcdd3DEEUcAMHz4cO677z7+9V//lfPPP3/53oiSwUuSJDXMGmuswbhx47j44ouXWn7XXXdx1FFHAXDsscdyxx131HW8iy66iC233JJddtnlzfFiN998MzfffDOjR49mhx124MEHH+Thhx/uda2HH374UvMHH3wwADvuuCOPPvpor4/XGYOXJElqqFNPPZWJEyfy8ssvd7lNRH1j0E477TQeeughrr32WsaNG8fChQvJTM4++2ymTp3K1KlTeeSRRzj++OPftu/AgQNZsmTJm/MLFy5cav1qq6221PzgwYMBGDBgAIsWLaqrvp4YvCRJUkOts846HHbYYUycOPHNZbvtthvXXHMNAFdddRV77LEHAEOHDmXBggU9HvPggw9mzJgxXHHFFey7775cfvnlvPTSSwA8+eSTPPvss2871mabbcb06dN57bXXmD9/Prfccktfvsy6GLwkSVLDnX766cydO/fN+Ysvvpjvf//7bLfddvzgBz/g29/+NgBHHHEEEyZMYPTo0d0Orgf40pe+xIUXXshHPvIRjjrqKHbddVe23XZbDjnkEBYsWMCwYcPYfffd2WabbTjzzDPZZJNNOOyww9huu+04+uijGT16dENfc2cis+efgzbbmDFj8t577212GZIk9RszZsxgq622anYZLa+z9zkipmTmmM62t8VLkiSpIgYvSZKkihi8JEmSKmLwkiSpRfWHcdz92bK8v96rsV1f38NKUu/Vce83SfUZMmQI8+bNY9iwYXVfI0v1y0zmzZvHkCFDerWfwUuSpBa08cYbM2vWLObMmdPsUlrWkCFD2HjjjXu1j8FLkqQWNGjQIEaOHNnsMtSBY7wkSZIqYvCSJEmqiMFLkiSpIgYvSZKkihi8JEmSKmLwkiRJqojBS5IkqSIGL0mSpIoYvCRJkipi8JIkSaqIwUuSJKkiBi9JkqSKGLwkSZIqYvCSJEmqiMFLkiSpIgYvSZKkihi8JEmSKmLwkiRJqojBS5IkqSIGL0mSpIoYvCRJkipi8JIkSaqIwUuSJKkiBi9JkqSKGLwkSZIqYvCSJEmqiMFLkiSpIgYvSZKkihi8JEmSKmLwkiRJqojBS5IkqSINC14RsUlE/C4iZkTEXyLilHL5OhHxm4h4uHxeu1E1SJIkrUga2eK1CDg9M7cC3gecFBGjgLOAWzJzC+CWcl6SJKnlNSx4ZebszLyvnF4AzAA2Ag4Crig3uwL4WKNqkCRJWpEMrOIkETECGA3cDayfmbOhCGcRsV4VNag1jTgFHptb//bfHw//+MHG1SNJUncaPrg+IlYHfgycmpkv9mK/8RFxb0TcO2fOnMYVqHeUbTdtdgWSpHeyhrZ4RcQgitB1VWbeUC5+JiI2KFu7NgCe7WzfzLwMuAxgzJgx2cg61X9N/yYs6ebTkQlbnQlPPg9bbQg7jqyuNkmSOmrkrxoDmAjMyMwLa1bdCBxXTh8H/LRRNaj1rToYVh/S9eO+R4vQBXDsHk0tVZKkhrZ47Q4cC/w5IqaWyz4HnAf8KCKOBx4HDm1gDXqH+8EdxXMEHGPwkiQ1WcOCV2beAUQXq/dq1Hmldgtfh+vvKab33Ao2GdbceiRJ8sr1alk33gfzXymmx9naJUlaARi81LLauxlXWRk+sXNza5EkCQxealFzF8CvpxXTH9sRhq7S3HokSQKDl1rU1XfCG4uL6XHvb24tkiS1M3ipJf3374vnd60Fe2/b3FokSWpn8FLL+etsuGdmMX3UrjDAT7kkaQXhV5JaTvugevCiqZKkFYvBSy0l861uxm02hrYRTS1HkqSlGLzUUu54CB4t76nuoHpJ0orG4KWW0t7NuFLAUbs1txZJkjoyeKllvPYGXHd3Mb3X1rDROs2tR5Kkjgxeahk/uw9eKG8R5KB6SdKKyOClltHezbjaYDh4p+bWIklSZwxeagnzFsAv7y+mD94JVhvS3HokSerMwGYXIPWFYUPh9SubXYUkSd2zxUuSJKkiBi9JkqSKGLwkSZIqYvCSJEmqiMFLkiSpIgYvSZKkihi8JEmSKmLwkiRJqojBS5IkqSIGL0mSpIoYvCRJkipi8JIkSaqIwUuSJKkiBi9JkqSKGLwkSZIqYvCSJEmqiMFLkiSpIgYvSZKkihi8JEmSKmLwkiRJqojBS5IkqSIGL0mSpIoYvCRJkipi8JIkSaqIwUuSJKkiBi9JkqSKGLwkSZIqYvCSJEmqSI/BKyI2j4jB5fSeEfHpiFir8aVJkiS1lnpavH4MLI6I9wATgZHADxtalSRJUgsaWMc2SzJzUUR8HPhWZv5HRPyp0YVVLR5udgWSstkFSFKD1dPi9UZEHAkcB/y8XDaocSVJkiS1pnqC1yeBXYGvZebfI2Ik8N+NLUuSJKn1dNvVGBEDgM9l5jHtyzLz78B5jS5MkiSp1XTb4pWZi4F1I2LliuqRJElqWfUMrn8U+H1E3Ai83L4wMy9sVFGSJEmtqJ7g9VT5WAkY2thyJEmSWlePwSsz/x0gIlbLzJd72l6SJEmdq+fK9btGxHRgRjm/fUR8t+GVSZIktZh6LifxLWBfYB5AZt4PfKCnnSLi8oh4NiIeqFl2bkQ8GRFTy8f+y1q4JElSf1PXTbIz84kOixbXsdskYL9Oll+UmW3l46Z6zi9JktQK6gleT0TEbkBGxMoRcQZlt2N3MvN24LnlLVCSJKlV1BO8/gU4CdgImAW0lfPL6uSImFZ2Ra69HMeRJEnqV3oMXpk5NzOPzsz1M3O9zDwmM+ct4/m+B2xOEd5mAxd0tWFEjI+IeyPi3jlz5izj6SRJklYc9fyq8ZsRsUZEDIqIWyJibkQc09N+ncnMZzJzcWYuAf4L2LmbbS/LzDGZOWbdddddltNJkiStUOrpatwnM18ExlJ0Nf4DcOaynCwiNqiZ/TjwQFfbSpIktZp6rlw/qHzeH7g6M5+LiB53ioirgT2B4RExCzgH2DMi2oCkuBXRCctQsyRJUr9UT/D6WUQ8CLwKnBgR6wILe9opM4/sZPHEXtYnSZLUMuoZXH8WsCswJjPfoLhR9kGNLkySJKnV9NjiFRHjaqZrV13ZiIIkSZJaVT1djTvVTA8B9gLuw+AlSZLUKz0Gr8z8VO18RKwJ/KBhFUmSJLWouu7V2MErwBZ9XYgkSVKrq2eM188oLv8ARVAbBfyokUVJkiS1onrGeJ1fM70IeCwzZzWoHkmSpJZVzxiv26ooRJIkqdUtyxgvSZIkLQODlyRJUkW6DF4RcUv5/I3qypEkSWpd3Y3x2iAiPggcGBHXAEtdtj4z72toZZIkSS2mu+D1JeAsYGPgwg7rEvhwo4qSJElqRV0Gr8y8Hrg+Ir6YmV+psCZJkqSWVM/lJL4SEQcCHygX3ZqZP29sWZIkSa2nx181RsTXgVOA6eXjlHKZJEmSeqGeK9f/L6AtM5cARMQVwJ+AsxtZmCRJUqup9zpea9VMr9mIQiRJklpdPS1eXwf+FBG/o7ikxAewtUuSJKnX6hlcf3VE3ArsRBG8/i0zn250YZIkSa2mnhYvMnM2cGODa5Gk1vbD6HkbSY11VDb19N6rUZIkqSIGL0mSpIp0G7wiYqWIeKCqYiRJklpZt8GrvHbX/RGxaUX1SJIktax6BtdvAPwlIu4BXm5fmJkHNqwqSZKkFlRP8Pr3hlchSZL0DlDPdbxui4jNgC0y8/9FxKrAgMaXJkmS1FrquUn2PwPXA/9ZLtoImNzIoiRJklpRPZeTOAnYHXgRIDMfBtZrZFGSJEmtqJ7g9Vpmvt4+ExEDgeZe9lWSJKkfqid43RYRnwNWiYi9geuAnzW2LEmSpNZTT/A6C5gD/Bk4AbgJ+EIji5IkSWpF9fyqcUlEXAHcTdHF+FBm2tUoSZLUSz0Gr4j4X8ClwEwggJERcUJm/rLRxUmSJLWSei6gegHwocx8BCAiNgd+ARi8JEmSeqGeMV7Ptoeu0t+AZxtUjyRJUsvqssUrIg4uJ/8SETcBP6IY43Uo8McKapMkSWop3XU1HlAz/QzwwXJ6DrB2wyqSJElqUV0Gr8z8ZJWFSJIktbp6ftU4EvgUMKJ2+8w8sHFlSZIktZ56ftU4GZhIcbX6JY0tR5IkqXXVE7wWZubFDa9EkiSpxdUTvL4dEecANwOvtS/MzPsaVpUkSVILqid4bQscC3yYt7oas5yXJElSneoJXh8H3p2Zrze6GEmSpFZWz5Xr7wfWanQhkiRJra6eFq/1gQcj4o8sPcbLy0lIkiT1Qj3B65yGVyFJkvQO0GPwyszbqihEkiSp1dVz5foFFL9iBFgZGAS8nJlrNLIwSZKa6dfT4Irb4a5H4OkXYNXBsNHa8L73wME7wX7bN7tC9Uf1tHgNrZ2PiI8BOzesIkmSmujlhTDuUrjhj0svX/gGPPcS/PkJ+OvTBi8tm3rGeC0lMydHxFmNKEaSpGZ6fRGMPR9unQEDVoITPgzH7gGbrw+Ll8CMJ+HHf4TZLzS7UvVX9XQ1HlwzuxIwhre6HiVJahnn3ViEroED4IZT4YAdll7/rrXgQ1s3pza1hnpavA6omV4EPAoc1NNOEXE5MBZ4NjO3KZetA1wLjCiPc1hmPt+riiVJaoB5C+DrNxbTJ+399tAl9YV6xnh9chmPPQn4DnBlzbKzgFsy87yyu/Is4N+W8fiSJPWZH9xRjOOKgM98tNnVqFV1Gbwi4kvd7JeZ+ZXuDpyZt0fEiA6LDwL2LKevAG7F4CVJWgH8alrxvP2msOnwt5YvWlyM94poTl1qLd21eL3cybLVgOOBYUC3wasL62fmbIDMnB0R63W1YUSMB8YDbLrppstwKkmS6jfl78XzmJHwymvwjZ/Bf/8eHp1ThK4t3gUfHwOn7w/DhnZ/LKkrXQavzLygfToihgKnAJ8ErgEu6Gq/vpKZlwGXAYwZM8bB/JKkhnn1dZi7oJhedTDs9EWY/mTNBgkPPlWMAbvyf+CXn4VtbRPQMuj2JtkRsU5EfBWYRhHSdsjMf8vMZ5fxfM9ExAblsTcAlvU4kiT1mfmvvDV96S1F6PrETjDt6/DaFfD4xXDOwbBSwJPPw0EXwksLm1ev+q8ug1dETAD+CCwAts3Mc/vgF4g3AseV08cBP13O40mStNwWL3lr+vVF8OGt4bpTilatlQfCJsPg3E/AN48stvn7HLjst82pVf1bdy1epwMbAl8AnoqIF8vHgoh4sacDR8TVwF3AlhExKyKOB84D9o6Ih4G9y3lJkppq9SFLz3/5E50Ppv/UvjBs9WJ68r2Nr0utp7sxXt12Q/YkM4/sYtVey3NcSZL62tAhMHgQvPZG0Z045t2db7fyQNjlPXDT1A5jwKQ69fqWQVKlEpgLPFnzeAZYDAwAvtiLY70MTAEeBJ4H3qD4ne4wYCSwQzkv6R1npZVgi/XhgVmw9mpFCOvK2uW/Ey++Wk1tai0GL63YXgAu6YPjPEQxovCVDsvnl4+/ARtTBDBJ70hj3l0Er+dehoWvw5CVO99uXvnrxzVXra42tQ6Dl/qPocBGFOHp8V7s91eKG1UtAYYDewCbAUOAl8pjTQW8OKL0jnbQjjDpdsiEPzwCe456+zavvQF3zyym2zartj61BoOXVmyrAkdQBK72Cxb+jvqD1yvAZIrQtRlwDFDbhbAKsC6wY18UK6k/278NRq5b/GLxi9fDbV8ouiBrTfg5PF9eXvyIXauvUf3fcg2glxpuMPBe3gpdvXUHRfgaBHyCpUOXJNVYeX1+zL8AAAwTSURBVCBcdEzxa8Y7HoKx58NdDxdB68Gn4Iyr4Es/LrbdcSSM26O59ap/ssVLrWsxRRciwDbAGk2sRVK/cNAY+NYxcPoP4Zf3F4+O2jaDn34GBvkNqmXgx0at6yneGky/ZYd17b+KlKQOPr0f7LElfPvXcOt0eHo+rLoybLtJ0b34vz9UtI5Jy8KPjlrX7JrpDYHHKLoeH6W4lMRgYFNgF+A9VRcnaUW2w0i44l+aXYVakcFLrWt++RzADOBXFNcFa/ca8HD52AX4aKXVSZLegQxeal21N7D9FcXlI/ah6HYcBDwB/Jrigqx3U1xIdeeKa5QkvaP4q0a1rqx5TuBwYDTFJSoGAe8G/pG3Bt3fStEFKUlSgxi81Lpqrzr9bmBEJ9usAryvnH6FohVMkqQGMXipddXezmOjbrarvfr0nAbVIkkSBi+1suE106t3s92QmunXGlSLJEkYvNTKNqyZXtDNdq/WTA/pcitJkpabwUutay1g/XK6u7Fbj9ZMv6th1UiSZPBSi2u/PMRjwCOdrH8Z+EM5vRbdjwWTJGk5eR0vrfieZemxVy/WTHdsydqApT/Vo4EpFLcPug7Yi+I6XgOBWcDNwEvltvvgbYQkSQ1l8NKK7xcULVYdLQYmdlh2CrB2zfxKwJHADygC3E3lo1YA+wKj+qJYSZK6ZvBS6xsKjAf+CDwAzKO4UOpQYCTFdbzW73JvSZL6jMFLK75P9sExBgK7lg9JkprEwfWSJEkVMXhJkiRVxOAlSZJUEYOXJElSRQxekiRJFTF4SZIkVcTgJUmSVBGDlyRJUkUMXpIkSRUxeEmSJFXE4CVJklQR79UoSRWJh5tdgaRs8vlt8ZIkSaqIwUuSJKkiBi9JkqSKGLwkSZIqYvCSJEmqiMFLkiSpIgYvSZKkihi8JEmSKmLwkiRJqojBS5IkqSIGL0mSpIoYvCRJkipi8JIkSaqIwUuSJKkiBi9JkqSKGLwkSZIqYvCSJEmqiMFLkiSpIgYvSZKkihi8JEmSKmLwkiRJqsjAZpw0Ih4FFgCLgUWZOaYZdUiSJFWpKcGr9KHMnNvE80uSJFXKrkZJkqSKNCt4JXBzREyJiPGdbRAR4yPi3oi4d86cORWXJ0mS1PeaFbx2z8wdgI8CJ0XEBzpukJmXZeaYzByz7rrrVl+hJElSH2tK8MrMp8rnZ4GfADs3ow5JkqQqVR68ImK1iBjaPg3sAzxQdR2SJElVa8avGtcHfhIR7ef/YWb+qgl1SJIkVary4JWZfwO2r/q8kiRJzdbM63hJkrTiuAiY34vtDwJGN6gWtSyv4yVJ0rJYv9kFqD+yxUuSJICTKK4y2Z3vUNzwbjiwYcMrUgsyeEmSBLByD+sfpQhd4EhlLTO7GiVJqsf9NdPbNa0K9XMGL0mSevIGML2cHgGs2bxS1L8ZvCRJ6slDwGvltN2MWg4GL0mSejKtfB4IjGpmIervDF6SJHXnZeCRcvq9wOAm1qJ+z+AlSVJ3HgCWlNN2M2o5GbwkSepOezfj6sDmzSxErcDgJUlSV+YCT5bT2+K3ppabHyFJkroyrWbaa3epDxi8JEnqTPJW8FoP2KCJtahlGLwkSerM48AL5bSD6tVHDF6SJHWm/RZBQTG+S+oDBi9JkjpaxFu3CBoJrNHEWtRSDF6SJHX0ELCwnLabUX3I4CVJUkftg+oHAVs1sxC1GoOXJEm1XgEeLqe3AlZuYi1qOQObXYAkSSuUVYEvNbsItSpbvCRJkipi8JIkSaqIwUuSJKkiBi9JkqSKGLwkSZIqYvCSJEmqiMFLkiSpIgYvSZKkihi8JEmSKmLwkiRJqojBS5IkqSIGL0mSpIoYvCRJkipi8JIkSaqIwUuSJKkiBi9JkqSKGLwkSZIqYvCSJEmqiMFLkiSpIgYvSZKkihi8JEmSKmLwkiRJqojBS5IkqSIGL0mSpIoYvCRJkipi8JIkSaqIwUuSJKkiBi9JkqSKGLwkSZIqYvCSJEmqiMFLkiSpIgYvSZKkijQleEXEfhHxUEQ8EhFnNaMGSZKkqlUevCJiAHAJ8FFgFHBkRIyqug5JkqSqNaPFa2fgkcz8W2a+DlwDHNSEOiRJkirVjOC1EfBEzfyscpkkSVJLG9iEc0Yny/JtG0WMB8aXsy9FxEMNrUqtYDgwt9lFaNnFuZ398yCtUPx3pp+r6N+Zzbpa0YzgNQvYpGZ+Y+Cpjhtl5mXAZVUVpf4vIu7NzDHNrkNS6/LfGS2vZnQ1/hHYIiJGRsTKwBHAjU2oQ5IkqVKVt3hl5qKIOBn4NTAAuDwz/1J1HZIkSVVrRlcjmXkTcFMzzq2WZte0pEbz3xktl8h827h2SZIkNYC3DJIkSaqIwUstISI+HhEZEe9tdi2SWktELI6IqRFxf0TcFxG7Nbsm9V8GL7WKI4E7KH4lK0l96dXMbMvM7YGzga83uyD1XwYv9XsRsTqwO3A8Bi9JjbUG8Hyzi1D/1ZRfNUp97GPArzLzrxHxXETskJn3NbsoSS1jlYiYCgwBNgA+3OR61I/Z4qVWcCTFzdYpn49sYi2SWk97V+N7gf2AKyPC+1tpmXg5CfVrETGM4jZUz1Lc83NA+bxZ+uGW1Aci4qXMXL1m/hlg28x8tollqZ+yxUv93SHAlZm5WWaOyMxNgL8DezS5LkktqPzl9ABgXrNrUf/kGC/1d0cC53VY9mPgKOB/qi9HUgtqH+MFEMBxmbm4mQWp/7KrUZIkqSJ2NUqSJFXE4CVJklQRg5ckSVJFDF6SJEkVMXhJkiRVxOAlqWEi4qKIOLVm/tcR8X9r5i+IiM90s/+tETGmznNtGBHXl9NtEbF/L2v9e0Rs2WHZtyLis705TifH/ZeIGLc8x5DUOgxekhrpTmA3gIhYCRgObF2zfjfg931xosx8KjMPKWfbgF4FL4rbTb15k/Wy3kOAa+vZOSIGdFHXpZl5ZS9rkdSiDF6SGun3lMGLInA9ACyIiLUjYjCwFfCniNgxIm6LiCllq9gGNcc4JiLujIgHImJngIj4YERMLR9/ioihETGi3GZl4MvA4eX6wyNitYi4PCL+WG5/UCe1Xk1N8AI+ADyamY9FxDERcU95vP9sD1kR8VJEfDki7gZ2jYjzImJ6REyLiPPLbc6NiDPK6baI+EO5/icRsXa5/NaI+EZ5jr9GxPv75u2XtKIxeElqmMx8ClgUEZtSBLC7gLuBXYExwDSKe2v+B3BIZu4IXA58reYwq2XmbsCJ5TqAM4CTMrMNeD/was05Xwe+BFxb3tj4WuDzwG8zcyfgQ8CEiFitQ63TgCURsX256Ajg6ojYCjgc2L0832Lg6PbagAcycxdgOvBxYOvM3A74aidvyZXAv5Xr/wycU7NuYGbuDJzaYbmkFuItgyQ1Wnur127AhcBG5fR8iq7ILYFtgN9EBBT3wZtds//VAJl5e0SsERFrlce8MCKuAm7IzFnlvl3ZBziwveUJGAJsCszosN3VwBER8RfgIIoAdxiwI/DH8hyrUNyUHYoQ9uNy+kVgIfB/I+IXwM9rDxwRawJrZeZt5aIrgOtqNrmhfJ4CjOjuxUjqvwxekhqtfZzXthRdjU8Ap1MElcsp7n33l8zctYv9O97XLDPzvDLc7A/8ISI+QhF6uhLAJzLzoR5qvRq4GbgNmJaZz0aRtq7IzLM72X5h+z37MnNR2RW6F0Vr2cnAh3s4X63XyufF+G+z1LLsapTUaL8HxgLPZebizHwOWIuiu/Eu4CFg3YjYFSAiBkVE7QD8w8vlewDzM3N+RGyemX/OzG8A9wLv7XDOBcDQmvlfA58qQxQRMbqzQjNzJjCP4sbrV5eLbwEOiYj1yn3XiYjNOu4bEasDa2bmTRTdhW0djj0feL5m/NaxFAFP0juIwUtSo/2Z4teMf+iwbH5mzi3HZB0CfCMi7gem8taAfCjCyp3ApcDx5bJTy4H091OM7/plh3P+DhjVPrge+AowCJgWEQ+U8125miLI/QQgM6cDXwBujohpwG+ADTrZbyjw83Kb24DTOtnmOIrxZdMogtmXu6lDUguKzI6t+JIkSWoEW7wkSZIqYvCSJEmqiMFLkiSpIgYvSZKkihi8JEmSKmLwkiRJqojBS5IkqSIGL0mSpIr8f9t/waXFq7z9AAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 720x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10,6))\n",
    "plt.title('Return Result between Version A and B')\n",
    "plt.bar([0,1],[16,7], color = 'green')\n",
    "plt.bar([0,1],[7,6], bottom = [16,7], color = 'orange' )\n",
    "\n",
    "plt.text(-0.05,8,'16', size = 26)\n",
    "plt.text(-0.02,18.5,'7', size = 26)\n",
    "\n",
    "\n",
    "plt.text(0.96,3,'7', size = 26)\n",
    "plt.text(0.96,9,'6', size = 26)\n",
    "\n",
    "plt.xticks([0,1], ['A','B'])\n",
    "plt.ylim(0,26)\n",
    "plt.xlabel('Website Version')\n",
    "plt.ylabel('Number of users')\n",
    "plt.legend(['Return','Not Return'])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
