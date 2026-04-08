# Phorid-Microbiota
This repository contains scripts and data used in the article "What lurks in the dark? An innovative framework for studying diverse wild insect microbiota", published in the Microbiome journal, August 12, 2025, by Karol H. Nowak, Emily Hartop, Monika Prus-Frankowska, Mateusz Buczek, Michał R. Kolasa, Tomas Roslin, Otso Ovaskainen & Piotr Łukasik. Link to the article: https://link.springer.com/article/10.1186/s40168-025-02169-9
A copy of the supplementary data is available in the Figshare repository: https://doi.org/10.6084/m9.figshare.c.7862042

Repository contents:
  Analytical scripts - Initial bioinformatic pipeline used for processing raw reads into tables found in the Supplementary materials
  HMSC analysis - Scripts and data used for statistical modelling
  Species assignment - Phylogenetic tree used for phorid species delimitation
  Supplementary materials - Processed data supporting the publication statements
  Visualisation scripts - Processing 3 scripts and data used for generating the figures 
  Collection map - Sample collection locations in compressed geographical format
  Collection metadata - A table with the exact sample collection coordinates and characteristics provided by the sampling team

Detailed breakdown:

Analytical scripts:
  Multisplit.py - Script for splitting the demultiplexed reads into batches corresponding to COI and 16S-V4 targets
  LSD.py - Library Single Denoising wrapper script that merges forward and reverse reads, filters reads based on their quality, dereplicates them, clusters into OTUs and conducts the taxonomy assignment
  QUACK.py - Decontamination script that removes putative contaminants and non-bacterial sequences. Additionally, it provides the symbiont-to-spikein ratio, used in quantification of bacterial absolute abundance

HMSC analysis:
  HMSC input files - Tab-delimited files containing the input data for the HMSC scripts
  HMSC scripts - R scripts providing a step by step guidance through the statistical analysis 
  HMSC results - Full output obtained using the scripts above
  
Species assignment: 
  Files supporting the phylogenetic tree clustering the species with known phorid morphotypes and the phylogenetic tree in pdf file

Supplementary materials: 
  Supplementary Figure S1: Ordination of host communities' composition among sites and seasons (NMDS plot based on Bray-Curtis dissimilarity)
  Supplementary Figure S2: The number of 16S-V4 OTUS (a) and ZOTUS (b) present in at least a hundred copies, across the six sites and between females and males of the five most common host species
  Supplementary Figure S3: The distribution of the most common bacterial 97% OTUs across the most common fly species. For each OTU-host category, we show infection prevalence (fraction of insects harbouring at least a hundred copies of 16S-V4 rRNA - pie charts), and estimated absolute abundance of that OTU (box plot). Data is shown separately for the two sexes, across (a) the five most common fly species, from across the sampled sites; and (b) from across sites for the three most common fly species
  Supplementary Figure S4: Relationship between the explained variance (R2) of bacterial taxa presence and their prevalence
  Supplementary Figure S5: Proportion of variance explained per microbial taxon by the presence-absence model and the abundance conditional of presence model at the levels of microbial 16S-V4 OTUs (a), 16S-V4 ZOTUs (b) and Wolbachia COI ZOTUs (c)
  Supplementary Figure S6: Residual associations in the presence-absence model and the abundance conditional of presence model among bacterial taxa at the levels of microbial 16S-V4 OTUs (a), 16S-V4 ZOTUs (b) and Wolbachia COI ZOTUs (c)

  Supplementary Table S1: Details of the sampling sites and the numbers of processed insect specimens passing the quality criteria
  Supplementary Table S2: List of sample barcodes, species and genotype assignments, along with their sexes, sampling locations and accession numbers
  Supplementary Table S3: Numbers and proportions of 16S rRNA reads classified as contaminants, spikeins, and symbionts across the samples, identified by the QUACK script
  Supplementary Table S4: List of 16S rRNA OTUs, their prevalence and abundance across samples
  Supplementary Table S5: Comparison of Wolbachia presence between COI and 16S-V4 datasets
  Supplementary Table S6: Results of the HMSC models

  Supplementary File 1: Compressed table of COI ZOTUs read counts and taxonomic assignments across the samples
  Supplementary File 2: Compressed, decontaminated table of 16S-V4 ZOTU read counts and taxonomic assignments across the samples
  Supplementary File 3: Compressed, decontaminated table of estimated 16S-V4 ZOTU copies and taxonomic assignments across the samples

  Supplementary materials legend: List and description of supplementary materials

Visualisation scripts:
  Detailed description available within the directory
