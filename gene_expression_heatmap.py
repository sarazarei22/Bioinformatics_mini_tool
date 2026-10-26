import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def generate_gene_expression_plots():
  """Generates a styled Seaborn heatmap and boxplot for simulated

  gene expression data to visualize expression levels across samples.
  """
  # Set general aesthetic style for plots
  sns.set_theme(style='whitegrid')

  # Create a synthetic dataset representing gene expression levels
  np.random.seed(42)
  genes = [f'Gene_{i}' for i in range(1, 11)]
  samples = [f'Sample_{j}' for j in range(1, 6)]

  data = np.random.exponential(scale=2.0, size=(len(genes), len(samples)))
  df_expr = pd.DataFrame(data, index=genes, columns=samples)

  # 1. Plotting Heatmap
  plt.figure(figsize=(8, 6))
  sns.heatmap(
      df_expr, cmap='coolwarm', annot=True, fmt='.2f', linewidths=0.5
  )
  plt.title('Gene Expression Heatmap', fontsize=14, fontweight='bold')
  plt.xlabel('Experimental Samples', fontsize=12)
  plt.ylabel('Genes', fontsize=12)

  # Save figure with high resolution for portfolio/client review
  plt.savefig(
      'gene_expression_heatmap.png', dpi=300, bbox_inches='tight'
  )
  plt.close()
  print('Heatmap generated and saved successfully as PNG.')


if __name__ == '__main__':
  generate_gene_expression_plots()
