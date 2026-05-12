# Culinary-Phylogeny

This is a professional **README.md** structure for your GitHub repository. It is designed to be scannable, informative, and to highlight your technical decision-making to anyone reviewing your code.

---

#  Culinary Phylogeny: Mapping Global Flavor DNA

### An End-to-End Agglomerative Hierarchical Clustering Project

This project uses **Unsupervised Machine Learning** to discover the "Evolutionary Tree" of global cuisines. By analyzing the ingredient profiles of over 39,000 recipes, the model identifies how different cultures are mathematically related, visualizing these connections through an interactive Dendrogram.

##  Project Overview

Most clustering projects focus on simple customer segmentation. This project applies **Agglomerative Hierarchical Clustering** to abstract cultural data. It treats ingredients as the "genetic code" of a cuisine, merging similar flavor profiles from the bottom up to create a "Culinary Family Tree."

##  Technical Stack

* **Language:** Python
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning:** Scipy (Clustering & Linkage), Scikit-learn (Preprocessing)
* **Visualization:** Plotly, Matplotlib
* **Frontend/Deployment:** Streamlit (Zomato-inspired UI)

##  The Workflow

### 1. Data Engineering

* **Source:** Kaggle "What's Cooking?" Dataset (JSON).
* **Transformation:** Implemented **Multi-Label Binarization** to convert list-based ingredient data into a high-dimensional sparse matrix (1s and 0s).
* **Feature Scaling:** Aggregated recipes by cuisine to create "Cuisine Profiles" representing the average ingredient usage per culture.

### 2. Modeling (Agglomerative Clustering)

The core logic uses a bottom-up approach where each cuisine starts as its own cluster.

* **Linkage Criteria:** Primary use of **Ward’s Method** to minimize intra-cluster variance, producing balanced and distinct groups.
* **Distance Metric:** Euclidean distance used to measure the dissimilarity between ingredient vectors.

### 3. Interactive Visualization

A **Dendrogram** was constructed to visualize the hierarchy.

* **Horizontal Bars:** Represent the distance at which two clusters merged.
* **Similarity Threshold:** A user-defined cutoff that determines the final number of "Flavor Families."
* 
##  Frontend Features

The application features a dark-themed, Zomato-inspired interface built with **Streamlit**:

* **Dynamic Controls:** Users can switch between **Ward, Single, and Complete** linkage methods to observe changes in the tree structure.
* **Cluster Deep-Dive:** Interactive selection of cuisines to view their top signature ingredients.
* **Threshold Slider:** Real-time coloring of the dendrogram based on the chosen similarity distance.

##  File Structure

```text
├── data/
│   ├── train.json             # Raw recipe data
│   └── cuisine_profiles.csv    # Processed ingredient matrix
├── app.py                      # Streamlit UI & Application Logic
├── model_logic.py              # Clustering and Linkage functions
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation

```

##  Key Insights

* **Regional Clusters:** The model successfully groups cuisines like Thai, Vietnamese, and Filipino together, separate from European groups like Italian and French.
* **Linkage Impact:** Demonstrated how **Single Linkage** can lead to "chaining" while **Ward's Method** creates clean, interpretable cultural clusters.

---

### How to Run

1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `streamlit run app.py`

---

**Author:** [Your Name]
**Focus:** Data Science, Machine Learning, Engineering.
