# Chemprop for the discovery of Abaucin
Personal branch of chemprop used to predict the antibiotic Abaucin.
The latest and up-to-date chemprop project can be found [here](https://github.com/chemprop/chemprop "Chemprop's Github"). In order to preserve reproducability of data, this fork contains the snapshot of chemprop used to predict for Abaucin in the paper Deep learning-guided discovery of a narrow-spectrum antibiotic against *Acinetobacter baumannii*[^1]. 

## Installation

By clicking [**here**](/chemprop) to the chemprop subdirectory, detailed instructions on the installation of chemprop can be found. Specfically, we stalled via source for this project.

## Training
A model similar to that used to predict Abaucin can be found [**here**](models/final_model).

If you wish to train a new model on different data, continue on here, replacing paths where appropriate. 

If you wish to use the model to predict for antimicrobial activities on other data sets, move to the Prediction subheader. Training data for this data set is made available in the supplementary section of the paper[^1]. 

Using the given data sets as an example, to train a baseline Chemprop model with ensembling, use the following while in the chemprop conda environment.
```chemprop_train --data_path```

To train a Chemprop model supplemented by additional RDKit Features, use:
```TODO ```




## Prediction
Activity scores produced by the model were used as the main method of prioritizing molecules. In the paper described, we used the Broad Drug Repurposing Hub as a prediction set (raw data [**here**](data/Broad_DRH_smiles.csv)) 

## Additional Tools

### Tanimoto Nearest Neighbor Calculations




[^1]: Currently under review. Link and doi of the paper will be updated as soon as it is available. 

