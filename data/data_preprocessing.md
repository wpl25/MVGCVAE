### Data Preprocessing

To ensure data consistency and eliminate redundancy, we performed the following preprocessing steps on the three benchmark datasets:

#### - HMDAD Dataset
- The HMDAD database contains experimentally verified microbe–disease associations.
- Some microbe–disease pairs appeared multiple times due to being supported by different evidence sources.
- We treated these repeated associations as a single unique pair to avoid duplication.
- **After removing redundant entries**, we obtained a total of **450 unique microbe–disease associations**.

#### - Disbiome Dataset
- In the Disbiome dataset, the same microbe–disease association may be reported multiple times due to different detection methods.
- We did **not distinguish between detection techniques** and considered all entries for the same pair as a single association.
- After deduplication, we extracted **4351 unique associations** involving **218 diseases** and **1052 microbes**.

#### - Peryton Dataset
- The Peryton dataset provides a curated collection of **experimentally supported microbe–disease associations**.
- We directly used the provided associations without further filtering, as the dataset had already undergone curation.
- The dataset includes **4172 associations**, covering **43 diseases** and **1396 microbes**.

> **Note:** All datasets were preprocessed to retain only non-redundant, experimentally validated microbe–disease pairs to ensure fairness and reliability in the subsequent model evaluation.