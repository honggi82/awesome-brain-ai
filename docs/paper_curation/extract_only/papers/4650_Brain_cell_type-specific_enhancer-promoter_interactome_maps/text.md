[Figure 1]

## University of Groningen

[Figure 2]

## Brain cell type-specific enhancer-promoter interactome maps and disease-risk association

### Nott, Alexi; Holtman, Inge R.; Coufal, Nicole G.; Schlachetzki, Johannes C. M.; Yu, Miao; Hu, Rong; Han, Claudia Z.; Pena, Monique; Xiao, Jiayang; Wu, Yin

#### Published in:

Science

#### DOI:

10.1126/science.aay0793

IMPORTANT NOTE: You are advised to consult the publisher's version (publisher's PDF) if you wish to cite from it. Please check the document version below.

Document Version

Publisher's PDF, also known as Version of record

#### Publication date:

2019

Link to publication in University of Groningen/UMCG research database

Citation for published version (APA): Nott, A., Holtman, I. R., Coufal, N. G., Schlachetzki, J. C. M., Yu, M., Hu, R., Han, C. Z., Pena, M., Xiao, J., Wu, Y., Keulen, Z., Pasillas, M. P., O'Connor, C., Nickl, C. K., Schafer, S. T., Shen, Z., Rissman, R. A., Brewer, J. B., Gosselin, D., ... Glass, C. K. (2019). Brain cell type-specific enhancer-promoter interactome maps and disease-risk association. Science, 366(6469), 1134-1139. https://doi.org/10.1126/science.aay0793

Copyright Other than for strictly personal use, it is not permitted to download or to forward/distribute the text or part of it without the consent of the author(s) and/or copyright holder(s), unless the work is under an open content license (like Creative Commons).

The publication may also be distributed here under the terms of Article 25fa of the Dutch Copyright Act, indicated by the “Taverne” license. More information can be found on the University of Groningen website: https://www.rug.nl/library/open-access/self-archiving-pure/taverneamendment.

Take-down policy If you believe that this document breaches copyright please contact us providing details, and we will remove access to the work immediately and investigate your claim.

Downloaded from the University of Groningen/UMCG research database (Pure): http://www.rug.nl/research/portal. For technical reasons the number of authors shown on this cover page is limited to 10 maximum.

Download date: 01-07-2026

RESEARCH

[Figure 3]

according to cell type of origin and exhibited cell-type–specific patterns (Fig. 1A and fig. S1, C to E). Promoter H3K27ac signal correlated with gene expression of the corresponding cell type more closely thanATAC-seq and H3K4me3 ChIP-seq (fig. S1F) (12). Promoters associated with cell-type signature genes preferentially exhibited corresponding H3K27ac profiles (fig. S1G) (13). Oligodendrocyte nuclei contain a low signal for oligodendrocyte precursor cell signature genes, whereas neuronal nuclei represent a mixture of excitatory and inhibitory subtypes (fig. S1G). ATAC-seq and H3K27ac ChIP-seq profiles generated from PU.1 nuclei were highly correlated with those previously defined in ex vivo microglia (fig. S1, C and D) (14). Promoter H3K27ac signal was increased at microglia signature genes compared with genes associated with other myeloid populations (fig. S1H) (15). Cell-type– specific promoter activity defined by differential H3K27ac mirrored cell-type patterns of gene expression (12), as well as ATAC-seq and H3K4me3 enrichment, and were associated with gene ontologies representative of each cell type (fig. S2, A to D, and table S2).

[Figure 4]

[Figure 5]

ENHANCER GENOMICS

# Brain cell type–specific enhancer–promoter interactome maps and disease-risk association

Alexi Nott1*, Inge R. Holtman1,2*, Nicole G. Coufal3,4*, Johannes C. M. Schlachetzki1, Miao Yu5, Rong Hu5, Claudia Z. Han1, Monique Pena3, Jiayang Xiao3, Yin Wu3, Zahara Keulen3, Martina P. Pasillas1, Carolyn O’Connor6, Christian K. Nickl1, Simon T. Schafer3, Zeyang Shen1,7, Robert A. Rissman8,9, James B. Brewer8, David Gosselin1,10, David D. Gonda11, Michael L. Levy11, Michael G. Rosenfeld12, Graham McVicker13, Fred H. Gage3, Bing Ren5,14, Christopher K. Glass1,15†

Noncoding genetic variation is a major driver of phenotypic diversity, but functional interpretation is challenging. To better understand common genetic variation associated with brain diseases, we defined noncoding regulatory regions for major cell types of the human brain. Whereas psychiatric disorders were primarily associated with variants in transcriptional enhancers and promoters in neurons, sporadic Alzheimer’s disease (AD) variants were largely confined to microglia enhancers. Interactome maps connecting disease-risk variants in cell-type–specific enhancers to promoters revealed an extended microglia gene network in AD. Deletion of a microglia-specific enhancer harboring AD-risk variants ablated BIN1 expression in microglia, but not in neurons or astrocytes. These findings revise and expand the list of genes likely to be influenced by noncoding variants in AD and suggest the probable cell types in which they function.

T

he central nervous system is a complex organ consisting of diverse and highly interconnected cells. Single-cell–sequencing technologies have advanced our understanding of the molecular phenotypes of

ger RNA expression from target promoters. Clusters of multiple enhancers, referred to as super-enhancers, are particularly important in driving the expression of cell-identity genes (6). Enhancer repertoires underlie particular patterns of gene expression and enable celltype–specific responses (7). The activity of enhancers depends on three-dimensional enhancer–promoter interactions (8); however, the enhancer–promoter interactome of different brain cell types in vivo remains largely unknown.

We identified putative active promoters and enhancers in each cell type and found a oneto-many relationship between promoters and enhancers (8). Whereas active promoters are largely shared between cell types (Fig. 1B), a relatively small fraction of active enhancers overlap between cell types (Fig. 1C), indicating that cell-type specificity is mainly captured withintheenhancerrepertoire.Mostbulkbrainenhancer regions identified by PsychENCODE overlapped with the nuclei cell-type enhancers (94%) (13). However, analysis of cell-specific nuclei expanded the total number of putative brain enhancers by 87%.

human neurons, microglia, astrocytes, oligodendrocytes, and other cell types that reside within the brain (1–3), but the transcriptional mechanisms that control their developmental and functional properties in health and disease remain less well understood. Genome-wide association studies (GWASs) provide a genetic approach to identify molecular pathways involved in complex traits and diseases by defining associations between genetic variants and phenotypes of interest (4, 5). Large-scale GWASs have discovered hundreds of singlenucleotide polymorphisms (SNPs) associated with the risk of neurological and psychiatric disorders. The vast majority of these diseaserisk genetic variants are located in noncoding regions of the genome (5). The causal variants and the specific cell type(s) in which the disease-risk variants may be active is often unclear. GWAS-identified risk variants in noncoding regions of the genome can exert phenotypic effects through perturbation of transcriptional gene promoters and enhancers (4). Enhancers are short regions of DNA that bind transcription factors to enhance messen-

To characterize transcriptional regulatory elements within different cell types of the human brain, PU.1+ microglia, NEUN+ neuronal, OLIG2+ oligodendrocyte, and NEUNneg LHX2+ astrocyte nuclei were isolated from resected cortical brain tissue from six individuals by fluorescent-activated nuclei sorting (fig. S1, A and B, and table S1). Cell-type– specific populations of 200,000 nuclei were subjected to the assay for transposase-accessible chromatin sequencing (ATAC-seq), which identifies open regions of chromatin (9), and celltype–specific populations of 500,000 nuclei were subjected to H3K27ac and H3K4me3 chromatin immunoprecipitation sequencing (ChIP-seq), which predominantly identifies active chromatin regions and promoters, respectively (10, 11). These datasets clustered

To determine the enrichment of genetic variants associated with complex traits and diseasesincell-type–specific regulatoryregions, we performed linkage disequilibrium score (LDSC) regression analysis of heritability (16). LDSC uses GWAS summary statistics to determine whether genetic heritability for a trait or disease is enriched for SNPs within genome annotations while accounting for linkage disequilibrium. We obtained GWAS summary statistics for neurological and psychiatric disorders and neurobehavior traits (17) (table S3). We found a strong enrichment of heritability for variants within neuronal

[Figure 6]

1Department of Cellular and Molecular Medicine, University of California, San Diego, La Jolla, CA 92093, USA. 2Section Molecular Neurobiology, Department of Biomedical Sciences of Cells & Systems, University Medical Center Groningen, University of Groningen, 9713 AV Groningen, the Netherlands. 3Laboratory of Genetics, The Salk Institute for Biological Studies, La Jolla, CA 92037, USA. 4Department of Pediatrics, University of California, San Diego, La Jolla, CA 92093, USA. 5Ludwig Institute for Cancer Research, La Jolla, CA 92093, USA. 6Flow Cytometry Core Facility, The Salk Institute for Biological Studies, La Jolla, CA 92037, USA. 7Department of Bioengineering, University of California, San Diego, La Jolla, CA 92093, USA. 8Department of Neurosciences, University of California, San Diego, La Jolla, CA 92093, USA. 9Veterans Affairs San Diego Healthcare System, San Diego, CA 92161, USA. 10Centre de Recherche du Centre Hospitalier Universitaire de Québec–Université Laval, Département de Médecine Moléculaire, Faculté de Médecine, Université Laval, Québec G1V 4G2, Canada. 11Department of Neurosurgery, University of California, San Diego–Rady Children’s Hospital, San Diego, CA 92123, USA. 12Howard Hughes Medical Institute, Department and School of Medicine, University of California, San Diego, La Jolla, CA 92093, USA. 13The Salk Institute for Biological Studies, La Jolla, CA 92037, USA. 14Department of Cellular and Molecular Medicine, Center for Epigenomics, University of California, San Diego, School of Medicine, La Jolla, CA 92093, USA. 15Department of Medicine, University of California, San Diego, La Jolla, CA 92093, USA.

*These authors contributed equally to this work. †Corresponding author. Email: ckg@ucsd.edu

onDecember24,2019 http://science.sciencemag.org/Downloadedfrom

[Figure 7]

enhancers and promoters for all psychiatric disorders and behavioral traits (Fig. 1D), which was substantially lower in PsychENCODE bulk brain enhancers (Fig. 1D) (13). By contrast, AD SNP heritability was most highly enriched in microglia-regulatory elements (Fig. 1D), specifically microglia enhancers (18–23).

disease (fig. S5 and table S4). Integrating celltype–specific transcription factors with enhancer motifs of the corresponding cell type identifies major drivers of cell ontogeny.

enhancers, including chromatin loops to a microglia-specific super-enhancer (Fig. 2A). There were 219,509 significant interactions across cell types, and replicates clustered according to origin (fig. S6, A and B, and table S5). A strong H3K4me3 signal did not dictate that an interaction would occur (fig. S6C), suggesting that PLAC-seq captures a unique dimension of the chromatin conformation.

[Figure 8]

[Figure 9]

The relationship between promoters and distal regulatoryregions for different cell types in the brain is largely unknown. We used proximity ligation-assisted ChIP-seq (PLACseq), in which proximity ligation preceded an enrichment for active promoters by H3K4me3 ChIP-seq (25). Chromatin loops were identified betweenactivepromotersanddistalregulatory regions in microglia, neurons, and oligodendrocytes (26). An example is the SALL1 locus, which has interactions with cell-type–specific

De novo motif analyses at open chromatin within enhancers identified transcription factor–binding motifs associated with each cell type (fig. S3). In addition, H3K27ac-defined active promoters identified 288 human transcription factors that were active in a cell-type– specific manner (fig. S4 and table S2) (24), several of which have been associated with

A subset of chromatin interactions was significantly more active in each cell type and colocalized withincreasedATAC-seq,H3K27ac, and H3K4me3 ChIP-seq signal in a cell-type– specific manner (Fig. 2B and fig. S6D). Active

|[Figure 10]| |
|---|---|
| | |
| | |
| | |
| | |

of promoter regions defined for cell populations. (C) Chow–Ruskey plot of enhancer regions defined for cell populations and PsychENCODE enhancers defined using bulk brain. (D) Heatmap of LDSC analysis for genetic variants associated with brain disorders and behavior traits displayed as –log10(q) value for significance of enrichment for promoter and enhancer regions of cell populations and PsychENCODE bulk brain enhancers. OL, oligodendrocytes.

- Fig. 1. Cell-type–specific genomic regulatory region enrichments for GWAS risk variants for brain disorders and behavioral traits. (A) UCSC genome browser visualization of ATAC-seq (top panel), H3K4me3 ChIP-seq (middle panel), and H3K27ac ChIP-seq (bottom panel) for brain nuclei populations. Shown is a representative gene for microglia (CX3CR1), neurons (NEFL), oligodendrocytes (MOG), and astrocytes (GJA1). (B) Chow–Ruskey plot

onDecember24,2019 http://science.sciencemag.org/Downloadedfrom

[Figure 11]

[Figure 12]

[Figure 13]

- Fig. 2. Chromatin loops link promoters to active gene-regulatory regions. (A) UCSC genome browser visualization of ATAC-seq, H3K27ac ChIP-seq, H3K4me3 ChIP-seq and PLAC-seq loops at the SALL1 locus. The microgliaspecific super-enhancer is associated with microglia interactions (highlighted yellow). (B) Violin plots of ATAC-seq, H3K27ac ChIP-seq, H3K4me3 ChIP-seq and

RNA-seq log2(CPM+1) values at PLAC-seq up-regulated interactions shown in fig. S6D for microglia, neurons, and oligodendrocytes; ***p < 1e-12; **p < 1e-5;

*p < 1e-3 by Kruskal–Wallis between-groups test. (C) Metascape enrichment analyses of active genes identified at PLAC-seq up-regulated interactions shown in fig. S6D for microglia, neurons, and oligodendrocytes shown as –log10(q) values.

of genes: TRIM35, CHRNA2, SCARA3, and CCDC25 (Fig. 3D). Finally, we identified celltype–specific enhancers harboring AD-risk variants that were linked to genes expressed in multiple cell types, implicating cell-type– specific disease susceptibility. Examples are the PICALM and BIN1 loci, which, despite being expressed in multiple cell types (12), had microglia-specific enhancers harboring AD-risk variants (Figs. 3E and 4A).

promoters linked to microglia-, neuron-, and oligodendrocyte-enriched interactions were associated with gene ontology terms representative of each cell type, supporting the ability of the PLAC interactome to annotate cell-type–specific promoter–enhancer interactions (Fig. 2C).

tectedintheothercelltypes(Fig.3Bandfig.S8). A broader set of 134 putative risk genes were identified by applying the same analysis to all genome-wide significant variants found in two AD GWASs (figs. S8 and S9, A and B, and table S7) (18, 19).

Protein–protein interaction (PPI) network analysis showed that microglia AD-risk genes identified by PLAC-seq were highly connected with GWAS-assigned genes and centered around APOE, whereas PPI networks for neurons and oligodendrocytes were smaller in scope (fig. S9, C to E). Microglia AD-assigned genes were associated with gene ontology terms for immune function, whereas gene ontology terms for amyloid-beta processing were associated with neurons, microglia, and oligodendrocytes (fig. S9F).

We identified 2,954 super-enhancers in microglia, neurons, and oligodendrocytes, of which 83% had PLAC interactions and were linked to promoters with elevated H3K27ac levels compared with promoters linked to regular enhancers (fig. S7, A and B). Many super-enhancers harbored GWAS diseaseriskvariants and were connected to cell-type– specific genes,suggesting that a subset of GWAS variants act on super-enhancersto affectgene expression (fig. S7A and table S6).

The BIN1 microglia-specific enhancer is PLAC linked to the BIN1 promoter (Fig. 4A), binds to PU.1 (14), and contains the AD-risk variant rs6733839, which has the secondhighest AD-risk score after APOE and was fine mapped as a casual variant (Fig. 3A). Functionality of this microglia-specific enhancer was validated by CRISPR/Cas9-mediated deletion of a 363-bp region in two human pluripotentstemcell(PSC)lines(fig.S10,AtoC).PSC control (BIN1control) and BIN1 enhancer deletion (BIN1enh_del) lines had normal karyotypes (fig. S10D) and were differentiated into microglia, neurons, and astrocytes (Fig. 4B and figs. S11, A to D, and S12, A and B). Gene-expression analysis of BIN1control and BIN1enh_del lines in PSC and PSC-derived microglia, neurons, and astrocytes showed high correlation between samples, with clustering according to cell type (fig. S12, C and D). However, gene expression of BIN1 was nearly absent in the BIN1enh_del PSC-derived microglia, whereas BIN1 expression in BIN1enh_del PSCs and PSC-derived neurons and astrocytes was equivalent to that in

To better understand AD genetics and the microglia interactome, we distinguished likely causal variants from those in linkage disequilibrium by applying fine mapping and identified 261 credible set variants (18). In many instances, such as the BIN1, PICALM, and SORL1 loci, the fine-mapped variants overlapped with microglia-specific enhancers that were PLAC linked to corresponding gene promoters (Fig. 3A). Next, we determined PLAC interactions between active promoters and AD-risk–credible set variants (19) and identified 41 genes that were linked to these variants across cell types (fig. S8). Twenty-five of the PLAC-linked AD-risk genes were identified in microglia, of which 14 were not de-

PLACinteractionsaltered the interpretation of AD-risk variants for three reasons. First, we found AD-risk variants that were linked to more distal active promoters and not the closest gene promoter. An example is the SLC24A4 locus, which had AD-risk variants that were connected to the proximal active promoters of ATXN3, TRIP11, and CPSF2, but not to SLC24A4 (Fig. 3C). Second, we observed enhancers harboring AD-risk variants that were PLAC linked to active promoters of both GWAS-assigned genes and an extended subset of genes not assigned to GWAS loci. An example is the CLU locus, which had PLAClinked AD-risk variants to the GWAS-assigned genes CLU and PTK2B and an extended set

onDecember24,2019 http://science.sciencemag.org/Downloadedfrom

[Figure 14]

[Figure 15]

[Figure 16]

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

| | | |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

- (B) Chow–Ruskey plot of genes that are GWAS assigned and PLAC-seq linked to AD-risk–credible set variants in microglia, neurons, and oligodendrocytes.
- (C to E) UCSC genome browser visualization of interactions at AD-risk loci demonstrating: (C) reassignment of GWAS-assigned genes, (D) extension of GWAS-assigned genes, and (E) cell-type–specific gene-regulatory regions. The AD GWAS track shows meta-analysis p-values of stage 2 variants (18); line indicates p = 5e-8; blue dots are fine-mapped 95% credible set variants.

- Fig. 3. Expanded gene network of AD-risk loci. (A) Circos plot of AD GWAS loci showing microglia enhancers (gold bars), promoters (turquoise), open chromatin regions (black bars), and PLAC-seq interactions (black loops). Dots show z-score values of high-confidence AD variants identified by fine mapping (Kunkle stage 1) with a log10 p-value < 6e-5 (18). Blue dots represent z-score values of the credible set of AD SNPs (95% confidence); red lines show 15 high-confidence AD SNPs with a posterior probability > 0.2.

onDecember24,2019 http://science.sciencemag.org/Downloadedfrom

[Figure 17]

- Fig. 4. Deletion of a microglia-specific enhancer harboring a lead AD-risk variant affects microglia BIN1 expression. (A) UCSC genome browser visualization of the BIN1 locus showing AD-risk variants, ATAC-seq, H3K27ac ChIP-seq, H3K4me3 ChIP-seq, and PLAC-seq in different brain cell types. The shared active promoter region is highlighted in light blue; the microglia-specific enhancer region is highlighted in pink. The AD GWAS track shows meta-analysis p-values of stage 2 variants (18); line indicates p-value = 5e-8; blue dots are fine-mapped 95% credible set variants. (B) Immunohistochemistry of PSCs, microglia, neurons, and astrocytes in control and BIN1enh_del lines stained for the indicated cell lineage markers. (C) BIN1 gene expression in control and BIN1enh_del PSCs (N = 8,7), microglia (N = 6,5), neurons (N = 6,5), and astrocytes (N = 4,5) as RNA-seq TPM.

[Figure 18]

[Figure 19]

[Figure 20]

[Figure 21]

****p < 0.0001, Benjamini–Hochberg adjusted. (D) Western blot of BIN1 and GAPDH in control and BIN1enh_del PSC-derived microglia (top) and neurons (bottom). (E) Protein expression of BIN1 in control and BIN1enh_del PSCs, microglia, neurons, and astrocytes determined as Western blot BIN1/ GAPDH mean gray intensity. N = 4 controls, 3 BIN1enh_del per cell type. **p < 0.01 by unpaired two-tailed t test.

[Figure 22]

[Figure 23]

[Figure 24]

[Figure 25]

[Figure 26]

[Figure 27]

[Figure 28]

[Figure 29]

[Figure 30]

[Figure 31]

| |
|---|

BIN1control cells (Fig. 4C, fig. S12E, and table S8). Western blot confirmed BIN1 protein in BIN1control PSCs and PSC-derived microglia, neurons, and astrocytes (Fig. 4, D and E, and fig. S12F). BIN1 expression was unchanged in BIN1enh_del PSC-derived microglia precursor hematopoietic stem cells, indicating that microglia derivation was unaffected (fig. S12F). However, BIN1 was substantially reduced in BIN1enh_del microglia and not in neurons and astrocytes (Fig. 4, D and E). This finding that the most significant GWAS risk allele associated with BIN1 resides in a microglia-specific enhancer provides a rationale for further investigation of its function in these cells (27).

ments are likely to be influenced by genetic variation, which, because of our limited sample size, may partly explain the lack of overlap of a subsetof riskalleleswiththe currentregulatory atlases. The acquisition of more samples will provide further opportunity to evaluate interindividual variation on enhancer selection and function. We expect that these approaches will provide qualitatively new insights into disease mechanisms that may be of value in developing new approaches for prevention and treatment.

- 15. M. J. C. Jordão et al., Science 363, eaat7554 (2019).
- 16. B. Bulik-Sullivan et al., Nat. Genet. 47, 1236–1241

(2015).

- 17. Materials and methods are available as supplementary materials.
- 18. B. W. Kunkle et al., Nat. Genet. 51, 414–430 (2019).
- 19. I. E. Jansen et al., Nat. Genet. 51, 404–413 (2019).
- 20. K. L. Huang et al., Nat. Neurosci. 20, 1052–1061 (2017).
- 21. G. Novikova, G. Novikova, M. Kapoor, J. TCW, E. M. Abud, A. G. Efthymiou, H. Cheng, J. F. Fullard, J. Bendl, P. Roussos, W. W. Poon, K. Hao, E. Marcora, A. M. Goate, Integration of Alzheimer’s disease genetics and myeloid cell genomics identifies novel causal variants, regulatory elements, genes and pathways. bioRxiv 694281 [Preprint]. 6 July 2019. https://www.biorxiv.org/content/10.1101/694281v1.
- 22. K. E. Tansey, M. J. Hill, Transl. Psychiatry 8, 7 (2018).
- 23. K. E. Tansey, D. Cameron, M. J. Hill, Genome Med. 10, 14

(2018).

- 24. S. A. Lambert et al., Cell 175, 598–599 (2018).
- 25. R. Fang et al., Cell Res. 26, 1345–1348 (2016).
- 26. I. Juric et al., PLOS Comput. Biol. 15, e1006982 (2019).
- 27. A. Crotti et al., Sci. Rep. 9, 9477 (2019).
- 28. H. Keren-Shaul et al., Cell 169, 1276–1290.e17 (2017).

REFERENCES AND NOTES

- 1. B. B. Lake et al., Science 352, 1586–1590 (2016).
- 2. B. B. Lake et al., Nat. Biotechnol. 36, 70–80 (2018).
- 3. H. Mathys et al., Nature 570, 332–337 (2019).
- 4. M. D. Gallagher, A. S. Chen-Plotkin, Am. J. Hum. Genet. 102, 717–730 (2018).
- 5. M. T. Maurano et al., Science 337, 1190–1195 (2012).
- 6. D. Hnisz et al., Cell 155, 934–947 (2013).
- 7. S. Heinz, C. E. Romanoski, C. Benner, C. K. Glass, Nat. Rev. Mol. Cell Biol. 16, 144–154 (2015).
- 8. M. R. Mumbach et al., Nat. Methods 13, 919–922 (2016).
- 9. X. Chen et al., Nat. Methods 13, 1013–1020 (2016).
- 10. M. P. Creyghton et al., Proc. Natl. Acad. Sci. U.S.A. 107, 21931–21936 (2010).
- 11. N. D. Heintzman et al., Nat. Genet. 39, 311–318 (2007).
- 12. Y. Zhang et al., Neuron 89, 37–53 (2016).
- 13. D. Wang et al., Science 362, eaat8464 (2018).
- 14. D. Gosselin et al., Science 356, eaal3222 (2017).

The present study provides evidence that the identification of cell-type–specific promoter– enhancer interactomes enables substantial advances in the interpretation of GWAS-risk alleles and establishes a new resource for this purpose in a broad spectrum of neurological and psychiatric diseases. Major goals will be to extend these approaches to diseased tissues and to refine nuclear-sorting protocols to interrogate enhancer landscapes of informative cell subsetssuch as amyloid plaque–associated microglia (28). Disease-specific regulatory ele-

ACKNOWLEDGMENTS

We thank J. Collier for technical assistance, L. Van Ael for manuscript preparation, D. Skola and M. L. Gage for manuscript editing, and M. Gymrek and S. Konermann for scientific discussions. Funding: Support was provided by NIH grant nos. RF1 AG061060-01, R01 AG056511-01A1, and R01 AG057706-01; the Cure Alzheimer’s Fund Gifford Neuroinflammation Consortium; and UCSD Shiley-Marcos ADRC grant no. 1P30AG062429. A.N. was supported by the Alzheimer’s Association (grant no. AARF-18-

531498) and the Altman Clinical & Translational Research Institute

onDecember24,2019 http://science.sciencemag.org/Downloadedfrom

[Figure 32]

[Figure 33]

[Figure 34]

at UCSD (National Center for Advancing Translational Sciences, supported by NIH grant no. KL2TR001444). I.R.H. was supported by the VENI research program, which is financed by the Netherlands Organization for Scientific Research. N.G.C. was supported by NIH grant no. K08 NS109200-01 and The Hartwell Foundation. C.Z.H. was supported by the Cancer Research Institute Irvington Postdoctoral Fellowship Program. C.O. was funded by NIHNCI CCSG grant nos. P30 014195 and S10-OD023689. Salk facilities are supported by the Salk Cancer Center (NCI grant no. P30-CA014195). F.H.G. was supported by the JPB Foundation, the Engman Foundation, an AHA-Allen Initiative in Brain Health and Cognitive Impairment award made jointly through the American Heart Association and The Paul G. Allen Frontiers Group: 19PABH134610000, and the Dolby Foundation. J.B.B. and R.A.R. were supported by the UCSD Shiley-Marcos ADRC grant no.

AG062429-01. Sequencing was conducted at the IGM Genomics Center, UCSD; the center was supported by grant nos. P30DK063491 and P30CA023100. Author contributions: A.N., N.G.C., J.C.M.S., and C.K.G. conceived the study. N.G.C. coordinated tissue acquisition. D.D.G. and M.L.L. resected brain tissue. A.N., C.K.N., M.P.P., and D.G. isolated nuclei and cells. N.G.C., M.P., J.X., Y.W., Z.K., and C.O. performed PSC experiments. A.N., M.Y., and R.H. prepared sequencing libraries. I.R.H., A.N., and Z.S. analyzed datasets. A.N., I.R.H., and C.K.G. wrote the manuscript with contributions from N.G.C., C.Z.H., J.C.M.S., M.G.R., F.H.G., and B.R. Competing interests: B.R. is a cofounder of Arima Genomics, Inc., which sells Hi-C and PLAC-seq kits. Data and materials availability: Data are available on dbGap (https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi? study_id=phs001373.v2.p2). The UCSC genome browser session

(hg19) containing the processed ATAC-seq, ChIP-seq, and PLACseq datasets for each brain cell type is available at: https:// genome.ucsc.edu/s/nottalexi/glassLab_BrainCellTypes_hg19.

SUPPLEMENTARY MATERIALS

science.sciencemag.org/content/366/6469/1134/suppl/DC1 Materials and Methods Figs. S1 and S2 Captions for Tables S1 to S8 References (29–66) Tables S1 to S8

View/request a protocol for this paper from Bio-protocol.

27 May 2019; accepted 30 October 2019 10.1126/science.aay0793

onDecember24,2019 http://science.sciencemag.org/Downloadedfrom

[Figure 35]

##### Brain cell type specific enhancer promoter interactome maps and disease-risk association

Alexi Nott, Inge R. Holtman, Nicole G. Coufal, Johannes C. M. Schlachetzki, Miao Yu, Rong Hu, Claudia Z. Han, Monique

Pena, Jiayang Xiao, Yin Wu, Zahara Keulen, Martina P. Pasillas, Carolyn O'Connor, Christian K. Nickl, Simon T. Schafer,

Zeyang Shen, Robert A. Rissman, James B. Brewer, David Gosselin, David D. Gonda, Michael L. Levy, Michael G. Rosenfeld,

Graham McVicker, Fred H. Gage, Bing Ren and Christopher K. Glass

Science 366 (6469), 1134-1139.

DOI: 10.1126/science.aay0793originally published online November 14, 2019

###### Linking enhancers to disease

Enhancers are genomic regions that regulate gene expression, sometimes in a cell-dependent manner. However,

most of our knowledge of human brain cell type enhancers derives from studies of bulk human brain tissue. Nott et al.

examined chromatin and promoter activity in cell nuclei isolated from human brains. Genetic variants associated with

brain traits and disease showed cell-specific patterns of enhancer enrichment. These data indicate that Alzheimer's

disease is regulated by genetic variants within microglial cells, whereas psychiatric diseases tend to affect neurons.

Science, this issue p. 1134

ARTICLE TOOLS http://science.sciencemag.org/content/366/6469/1134

SUPPLEMENTARY http://science.sciencemag.org/content/suppl/2019/11/13/science.aay0793.DC1

MATERIALS

###### REFERENCES

This article cites 65 articles, 10 of which you can access for free

http://science.sciencemag.org/content/366/6469/1134#BIBL

PERMISSIONS http://www.sciencemag.org/help/reprints-and-permissions

onDecember24,2019 http://science.sciencemag.org/Downloadedfrom

Use of this article is subject to the Terms of Service

Science (print ISSN 0036-8075; online ISSN 1095-9203) is published by the American Association for the Advancement of

Science, 1200 New York Avenue NW, Washington, DC 20005. The title Science is a registered trademark of AAAS.

Copyright © 2019 The Authors, some rights reserved; exclusive licensee American Association for the Advancement of

Science. No claim to original U.S. Government Works

