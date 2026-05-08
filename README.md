# Task 4: Data Storytelling & Statistical Validation 📊🧪

## Project Overview
Is project ka maqsad business data se ek compelling narrative (kahani) taiyar karna aur statistical methods ka use karke findings ko validate karna hai. Humne website ke do alag layouts (**Control vs Test**) ke beech A/B testing perform ki hai taaki ye pata lag sake ki naya layout conversion aur sales badhane mein asardaar hai ya nahi.

**Timeline:** 16 Days  
**Tools Used:** Python (Pandas, Seaborn, Matplotlib, SciPy), VS Code, GitHub.

---

## 📂 File Structure
- `ecommerce_data.csv`: Isme 500 users ka raw data hai (Age, Device, Layout Group, Conversion, Purchase Amount).
- `task4_analysis.py`: Main Python script jo data cleaning, visualization, aur statistical testing karti hai.
- `README.md`: Project documentation (Ye file).

---

## 🎯 Objectives
1.  **Data Storytelling**: Sabhi analysis ko ek business narrative mein badalna.
2.  **Hypothesis Testing**: Statistical rigor add karna (T-test) taaki results ki accuracy confirm ho sake.
3.  **Actionable Insights**: Data ke basis par batana ki business ko naya layout adopt karna chahiye ya nahi.

---

## 🛠️ Step-by-Step Implementation

### 1. Data Generation & Cleaning
Humne ek synthetic dataset taiyar kiya hai jo real-world ecommerce behavior ko mimic karta hai.
- **Control Group**: Purana website design.
- **Test Group**: Naya website design.

### 2. Hypothesis Formulation
- **Null Hypothesis ($H_0$):** Dono layouts ke average purchase amount mein koi significant farq nahi hai.
- **Alternative Hypothesis ($H_1$):** New layout (Test) ka average purchase amount Control group se zyada hai.

### 3. Statistical Test (T-Test)
Humne **Independent Two-Sample T-Test** ka use kiya hai:
- **Confidence Level**: 95% ($\alpha = 0.05$)
- Agar **P-Value < 0.05**, to hum Null Hypothesis ko reject karte hain.

---

## 🚀 How to Run the Project

1.  **Repository Clone Karein:**
    ```bash
    git clone <your-repo-link>
    ```

2.  **Requirements Install Karein:**
    ```bash
    pip install pandas matplotlib seaborn scipy
    ```

3.  **Analysis Script Run Karein:**
    ```bash
    python task4_analysis.py
    ```

---

## 📊 Deliverables Included
* **Analysis Script**: Pura Python code documentation ke sath.
* **Visualizations**: Bar plots aur Boxplots jo groups ka comparison dikhate hain.
* **Final Conclusion**: Business decision (Rollout recommendation).

---

## 💡 Conclusion
Analysis ke mutabiq, agar P-Value 0.05 se kam aati hai, to hum ye claim kar sakte hain ki naya layout conversion aur revenue badhane mein kamyab raha hai. Ye sirf luck nahi balki ek statistically proven growth hai.
