import numpy as np
from scipy import stats


def perform_gene_expression_ttest(group_a: list, group_b: list):
  """Performs an independent two-sample t-test to compare gene expression levels

  between two experimental groups (e.g., Control vs. Treated).

  Parameters:
      group_a (list): Expression values for control group.
      group_b (list): Expression values for treated group.

  Returns:
      dict: Dictionary containing t-statistic and p-value.
  """
  # Convert inputs to numpy arrays
  arr_a = np.array(group_a)
  arr_b = np.array(group_b)

  # Perform independent t-test
  t_stat, p_value = stats.ttest_ind(arr_a, arr_b, nan_policy='omit')

  # Determine significance at alpha = 0.05
  is_significant = p_value < 0.05

  print(f'T-statistic: {t_stat:.4f}')
  print(f'P-value: {p_value:.4f}')
  print(f'Statistically significant difference: {is_significant}')

  return {
      't_statistic': float(t_stat),
      'p_value': float(p_value),
      'significant': bool(is_significant),
  }


if __name__ == '__main__':
  # Simulated gene expression data for two groups
  np.random.seed(42)
  control_group = np.random.normal(loc=5.0, scale=1.2, size=30)
  treated_group = np.random.normal(loc=6.5, scale=1.5, size=30)

  print('Running Biostatistics Hypothesis Testing...')
  perform_gene_expression_ttest(control_group, treated_group)
