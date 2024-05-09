import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


chat_id = 1265544018 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
  alpha = 0.08
  res = ttest_ind(x, y, equal_var=False, 
                  alternative='greater')

  return res.pvalue < alpha
