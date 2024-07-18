import numpy as np
import matplotlib.pyplot as plt

smoking_years = [10, 5, 20, 15, 8]  
lung_cancer_rates = [150, 100, 200, 180, 120] 

correlation_coefficient = np.corrcoef(smoking_years, lung_cancer_rates)[0, 1]

print(f"Correlation coefficient: {correlation_coefficient}")

plt.figure(figsize=(8, 6))
plt.scatter(smoking_years, lung_cancer_rates, color='blue', alpha=0.7)
plt.title('Relationship Between Smoking Years and Lung Cancer Rates')
plt.xlabel('Years of Smoking')
plt.ylabel('Lung Cancer Rates per 100,000 individuals')
plt.grid(True)
plt.tight_layout()
plt.show()
