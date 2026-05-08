import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

# =========================================================
# STEP 0: DATA GENERATION (CSV File banana)
# =========================================================
def generate_data():
    print("--- Step 0: CSV File Generate Ho Rahi Hai ---")
    np.random.seed(42)
    n_rows = 500
    
    data = {
        'User_ID': range(1, n_rows + 1),
        'Layout_Group': np.random.choice(['Control', 'Test'], n_rows), # Control=Old, Test=New
        'Converted': np.random.choice([0, 1], n_rows, p=[0.82, 0.18]),
        'Purchase_Amount': np.zeros(n_rows)
    }
    
    df = pd.DataFrame(data)
    
    # Logic: Test group (New Layout) ka purchase amount thoda zyada rakha hai
    for i in range(n_rows):
        if df.loc[i, 'Converted'] == 1:
            if df.loc[i, 'Layout_Group'] == 'Test':
                df.loc[i, 'Purchase_Amount'] = np.round(np.random.normal(85, 15), 2)
            else:
                df.loc[i, 'Purchase_Amount'] = np.round(np.random.normal(70, 12), 2)
    
    df.to_csv('ecommerce_data.csv', index=False)
    print("✅ 'ecommerce_data.csv' successfully ban gayi hai!\n")

# =========================================================
# STEP 1: DATA STORYTELLING (Analysis & Plots)
# =========================================================
def perform_analysis():
    df = pd.read_csv('ecommerce_data.csv')
    
    print("--- Step 1: Data Storytelling & Insights ---")
    # Conversion Rate calculate karna
    conv_stats = df.groupby('Layout_Group')['Converted'].mean() * 100
    print(f"Old Layout Conversion Rate: {conv_stats['Control']:.2f}%")
    print(f"New Layout Conversion Rate: {conv_stats['Test']:.2f}%")
    
    # Plotting
    plt.figure(figsize=(12, 5))
    
    # Plot 1: Average Purchase Value
    plt.subplot(1, 2, 1)
    sns.barplot(data=df[df['Purchase_Amount'] > 0], x='Layout_Group', y='Purchase_Amount', palette='viridis')
    plt.title('Average Purchase Amount ($)')
    
    # Plot 2: Boxplot for Distribution
    plt.subplot(1, 2, 2)
    sns.boxplot(data=df[df['Purchase_Amount'] > 0], x='Layout_Group', y='Purchase_Amount', palette='Set2')
    plt.title('Purchase Value Distribution')
    
    plt.tight_layout()
    plt.show()
    print("📊 Graphs generate ho gaye hain.\n")

# =========================================================
# STEP 2: STATISTICAL VALIDATION (Hypothesis Testing)
# =========================================================
    print("--- Step 2: Statistical Validation (T-Test) ---")
    
    # Hypothesis:
    # H0: Dono layouts ke purchase amount mein koi farq nahi hai.
    # H1: New layout (Test) Control se behtar hai.
    
    test_group = df[(df['Layout_Group'] == 'Test') & (df['Purchase_Amount'] > 0)]['Purchase_Amount']
    control_group = df[(df['Layout_Group'] == 'Control') & (df['Purchase_Amount'] > 0)]['Purchase_Amount']
    
    t_stat, p_value = stats.ttest_ind(test_group, control_group)
    
    print(f"T-Statistic: {t_stat:.4f}")
    print(f"P-Value: {p_value:.6f}")
    
    # Conclusion based on P-Value (Alpha = 0.05)
    alpha = 0.05
    print("\n--- Step 3: Final Business Conclusion ---")
    if p_value < alpha:
        print("✅ RESULT: Statistically Significant!")
        print("Story: Data se sabit hota hai ki New Layout ne sales badhayi hai.")
        print("Action: New Layout ko 100% users ke liye live kar dein.")
    else:
        print("❌ RESULT: Not Significant.")
        print("Story: Layout change karne ka koi bada asar nahi dikha.")
        print("Action: Design ko aur behtar karein ya purana hi rehne dein.")

# Run everything
if __name__ == "__main__":
    generate_data()
    perform_analysis()
