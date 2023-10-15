import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def explore_page():
    dataset = pd.read_csv('heart.csv')

    st.write("""### Proportion of Chance of Heart Attack""")
    output_counts = dataset["output"].value_counts(normalize=True)
    plt.figure(figsize=(4,4))
    plt.bar(x=output_counts.index, height=output_counts.values, color=["#90E353", "#537AE3"])
    plt.xticks([0, 1], ["less chance", "more chance"])
    plt.xlabel("Chance of Heart Attack")
    plt.ylabel("Proportion")
    st.pyplot(plt.gcf())

    st.divider()

    st.write("""### Distribution of Age""")
    sns.set_style('whitegrid')
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(14,6))
    sns.histplot(data=dataset, x='age', kde=False, ax=ax1, color='#537AE3')
    ax1.set_xlabel('Age', fontsize=14)
    ax1.set_ylabel('Count', fontsize=14)
    sns.kdeplot(data=dataset, x='age', fill=True, ax=ax2, color='#537AE3')
    ax2.set_xlabel('Age', fontsize=14)
    ax2.set_ylabel('Density', fontsize=14)
    fig.suptitle('Distribution of Age', fontsize=18, fontweight='bold')
    st.pyplot(plt.gcf())

    st.divider()

    st.write("""### Proportion of Chance of Heart Attack""")
    age_prop = dataset.groupby('age')['output'].mean()
    fig, ax = plt.subplots(figsize=(16,6))
    ax.plot(age_prop.index, age_prop.values, marker='o', markersize=8, linewidth=2, color='blue')

    ax.set_xlabel('Age')
    ax.set_ylabel('Proportion')
    ax.set_xticks(age_prop.index)
    ax.tick_params(axis='x', which='major', labelsize=12, pad=10, rotation=45)
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    ax.set_yticks([0.2, 0.4, 0.6, 0.8])
    ax.tick_params(axis='y', which='major', labelsize=12, pad=10)
    ax.grid(axis='y', linestyle='--', alpha=0.5)

    avg_prop = age_prop.mean()
    ax.axhline(avg_prop, linestyle='--', color='red', linewidth=1)
    ax.text(age_prop.index[-1], avg_prop+0.02, f'Avg. Proportion: {avg_prop:.2f}', ha='right', fontsize=12, color='red')
    st.pyplot(plt.gcf())

    st.divider()

    st.write("""### Chance of Heart Attack by Chest Pain type""")
    colors = ["#537AE3", "#90E353"]
    cross_tab = pd.crosstab(dataset['cp'], dataset['output'], normalize='index')
    ax = cross_tab.plot(kind='bar', stacked=True, color=colors, figsize=(8,6))
    ax.set_xlabel('Chest Pain type', fontsize=12)
    ax.set_ylabel('Proportion', fontsize=12)
    ax.legend(title='Chance of Heart Attack', loc='center left', bbox_to_anchor=(1.0, 0.5), fontsize=12)
    plt.xticks(rotation=45)
    plt.xticks([0, 1, 2, 3], ["typical angina", "atypical angina", "non-anginal pain", "asymptomatic"])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.set_ylim(0, 1)
    for i in range(len(cross_tab)):
        for j in range(len(cross_tab.columns)):
            plt.text(i, cross_tab.iloc[i, :j+1].sum() - 0.05, str(round(cross_tab.iloc[i, j]*100,1)) + '%', ha='center', va='top', fontsize=12, fontweight='bold', color='white')
    st.pyplot(plt.gcf())

    st.divider()

    st.write("""### Chance of Heart Attack vs resting electrocardiographic results""")
    colors = ["#537AE3", "#90E353"]
    cross_tab = pd.crosstab(dataset['restecg'], dataset['output'], normalize='index')
    ax = cross_tab.plot(kind='bar', stacked=True, color=colors, figsize=(8,6))
    ax.set_xlabel('resting electrocardiographic results', fontsize=12)
    ax.set_ylabel('Proportion', fontsize=12)
    ax.legend(title='Chance of Heart Attack', loc='center left', bbox_to_anchor=(1.0, 0.5), fontsize=12)
    plt.xticks(rotation=45)
    plt.xticks([0, 1, 2], ["Value 0", "Value 1", "Value 2"])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.set_ylim(0, 1)
    for i in range(len(cross_tab)):
        for j in range(len(cross_tab.columns)):
            plt.text(i, cross_tab.iloc[i, :j+1].sum() - 0.05, str(round(cross_tab.iloc[i, j]*100,1)) + '%', ha='center', va='top', fontsize=12, fontweight='bold', color='white')
    st.pyplot(plt.gcf())

    st.divider()

    st.write("""### Chance of Heart Attack vs Gender""")
    colors = ["#537AE3", "#90E353"]
    cross_tab = pd.crosstab(dataset['sex'], dataset['output'], normalize='index')
    ax = cross_tab.plot(kind='bar', stacked=True, color=colors, figsize=(8,6))
    ax.set_xlabel('Gender', fontsize=12)
    ax.set_ylabel('Proportion', fontsize=12)
    ax.legend(title='Chance of Heart Attack', loc='center left', bbox_to_anchor=(1.0, 0.5), fontsize=12)
    plt.xticks(rotation=45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.set_ylim(0, 1)
    for i in range(len(cross_tab)):
        for j in range(len(cross_tab.columns)):
            plt.text(i, cross_tab.iloc[i, :j+1].sum() - 0.05, str(round(cross_tab.iloc[i, j]*100,1)) + '%', ha='center', va='top', fontsize=12, fontweight='bold', color='white')
    st.pyplot(plt.gcf())

    st.divider()

    st.write("""### Chance of Heart Attack vs Exercise Induced Angina""")
    colors = ["#537AE3", "#90E353"]
    cross_tab = pd.crosstab(dataset['exng'], dataset['output'], normalize='index')
    ax = cross_tab.plot(kind='bar', stacked=True, color=colors, figsize=(8,6))
    ax.set_xlabel('Exercise Induced Angina', fontsize=12)
    ax.set_ylabel('Proportion', fontsize=12)
    ax.legend(title='Chance of Heart Attack', loc='center left', bbox_to_anchor=(1.0, 0.5), fontsize=12)
    plt.xticks(rotation=45)
    plt.xticks([0, 1], ["No", "Yes"])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.set_ylim(0, 1)
    for i in range(len(cross_tab)):
        for j in range(len(cross_tab.columns)):
            plt.text(i, cross_tab.iloc[i, :j+1].sum() - 0.05, str(round(cross_tab.iloc[i, j]*100,1)) + '%', ha='center', va='top', fontsize=12, fontweight='bold', color='white')
    st.pyplot(plt.gcf())

    st.divider()

    st.write("""### Chance of Heart Attack by number of major vessels""")
    colors = ["#537AE3", "#90E353"]
    cross_tab = pd.crosstab(dataset['caa'], dataset['output'], normalize='index')
    ax = cross_tab.plot(kind='bar', stacked=True, color=colors, figsize=(8,6))
    ax.set_xlabel('number of major vessels ', fontsize=12)
    ax.set_ylabel('Proportion', fontsize=12)
    ax.legend(title='Chance of Heart Attack', loc='center left', bbox_to_anchor=(1.0, 0.5), fontsize=12)
    plt.xticks(rotation=45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.set_ylim(0, 1)
    for i in range(len(cross_tab)):
        for j in range(len(cross_tab.columns)):
            plt.text(i, cross_tab.iloc[i, :j+1].sum() - 0.05, str(round(cross_tab.iloc[i, j]*100,1)) + '%', ha='center', va='top', fontsize=12, fontweight='bold', color='white')
    st.pyplot(plt.gcf())

    st.divider()

    st.write("""### Chance of Heart Attack by fasting blood sugar > 120 mg/dl""")
    colors = ["#537AE3", "#90E353"]
    cross_tab = pd.crosstab(dataset['fbs'], dataset['output'], normalize='index')
    ax = cross_tab.plot(kind='bar', stacked=True, color=colors, figsize=(8,6))
    ax.set_xlabel('fasting blood sugar > 120 mg/dl', fontsize=12)
    ax.set_ylabel('Proportion', fontsize=12)
    ax.legend(title='Chance of Heart Attack', loc='center left', bbox_to_anchor=(1.0, 0.5), fontsize=12)
    plt.xticks(rotation=45)
    plt.xticks([0, 1], ["False", "True"])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.set_ylim(0, 1)
    for i in range(len(cross_tab)):
        for j in range(len(cross_tab.columns)):
            plt.text(i, cross_tab.iloc[i, :j+1].sum() - 0.05, str(round(cross_tab.iloc[i, j]*100,1)) + '%', ha='center', va='top', fontsize=12, fontweight='bold', color='white')
    st.pyplot(plt.gcf())

    st.divider()

    st.write("""### Correlations with 'output'""")
    limit = -1.0
    data = dataset.corr()["output"].sort_values(ascending=False)
    indices = data.index
    labels = []
    corr = []
    for i in range(1, len(indices)):
        if data[indices[i]]>limit:
            labels.append(indices[i])
            corr.append(data[i])
    fig, ax = plt.subplots(figsize=(8,8))
    sns.barplot(x=corr, y=labels, ax=ax)
    plt.title('Correlations with "output"')
    st.pyplot(plt.gcf())

    st.divider()

    st.write("""### Relationship between Age and Chance of Heart Attack""")
    age_grouped = dataset.groupby('age')['output'].mean()
    plt.figure(figsize=(4,4))
    sns.regplot(x=age_grouped.index, y=age_grouped, color='blue', scatter_kws={'s': 50})
    sns.despine()
    plt.xlabel('Age', fontsize=12)
    plt.ylabel('Chance of Heart Attack', fontsize=12)
    plt.grid(axis='both', alpha=0.3)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    st.pyplot(plt.gcf())

    st.divider()
