# Alzheimers-Disease

**Introduction**

Alzheimer’s is a widespread, irreversible, progressive neurodegenerative disease, with complex genetic architecture.

Previous prediction methods can be roughly divided into five types1. Methods studying protein-protein interaction networks
2. Gene functional annotations
3. Sequence-based features patterns
4. Machine learning and network topological features
5. Information about tissue-specific networks
● These methods predict associated genes or biomarkers
● Few reports on brain gene expression data

● Key goal is to seek out disease risk genes (predict candidate genes)
● Various machine learning algorithms are used to classify candidate genes as
Alzheimer’s Disease associated and unassociated.

Revealing Alzheimer’s disease genes spectrum in the whole-genome by machine
learning.

The <a href = "https://pubmed.ncbi.nlm.nih.gov/29320986/">research paper</a> by Huang et al. on Revealing Alzheimer’s disease genes spectrum in the whole-genome by machine learning was used as a reference for this project.

<img src = "https://github.com/isha-git/Alzheimers-Disease/blob/master/Images/ResearchPaper.PNG" width = "600">

**Dataset**

The dataset used in the above-mentioned research paper was taken from the <a href = "http://www.alzgene.org/"> AlzGene archive </a>. The featurs include number of positive and negative Alzheimer's cases in control studies and family-based studies.

**Code Output**

**Note:** The current code prints the output according to the RBF kernel. If you want to use other kinds of Kernel, un-comment lines 35-38 as per your convenience.

1. SVM Method (Radial Kernel, C=1)

<img src = "https://github.com/shripriyamaheshwari/Alzheimers-Disease/blob/master/Images/SVM_radial_kernel.PNG" width = 600>

2. SVM Method (Gaussian Kernel, C=2)

<img src = "https://github.com/shripriyamaheshwari/Alzheimers-Disease/blob/master/Images/gaussian_kernel.PNG" width=600>

3. Using Classification and Regression Trees (CART)

<img src = "https://github.com/shripriyamaheshwari/Alzheimers-Disease/blob/master/Images/CART_Algorithm.PNG" width=600>

**Comparsion Results**

<img src = "https://github.com/shripriyamaheshwari/Alzheimers-Disease/blob/master/Images/comp_table.PNG" width = "600">

**Note:** The accuracy in the case of R-library (i.e. the first row in the table above), is referenced from the research paper mentioned above. We have not implemented the code in R.

**ROC Curve**

1. Using Linear Kernel

<img src = "https://github.com/shripriyamaheshwari/Alzheimers-Disease/blob/master/Images/ROC_linear_kernel.PNG" width=500>

2. Using Polynomial Kernel

<img src = "https://github.com/shripriyamaheshwari/Alzheimers-Disease/blob/master/Images/ROC_Polynomial_Kernel.PNG" width=500>

3. Using Radial Basis Function Kernel (RBF)

<img src = "https://github.com/shripriyamaheshwari/Alzheimers-Disease/blob/master/Images/ROC_RBF.PNG" width=500>
