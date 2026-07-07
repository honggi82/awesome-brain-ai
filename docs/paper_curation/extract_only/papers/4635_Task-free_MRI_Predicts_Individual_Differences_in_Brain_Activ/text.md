# Europe PMC Funders Group

#### Author Manuscript Science. Author manuscript; available in PMC 2018 December 28.

Published in final edited form as:

Science. 2016 April 08; 352(6282): 216–220. doi:10.1126/science.aad8127.

[Figure 1]

# Task-free MRI Predicts Individual Differences in Brain Activity During Task Performance

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

##### I Tavor1,2, O Parker Jones1, RB Mars1,3, SM Smith1, TE Behrens1,4, and S Jbabdi1,*

1Oxford Centre for Functional Magnetic Resonance Imaging of the Brain (FMRIB), Nuffield Department of Clinical Neurosciences, John Radcliffe Hospital, Oxford OX3 9DU, UK

- 2Department of Diagnostic Imaging, Sheba Medical Center, Tel Hashomer, 52621, Israel
- 3Donders Institute for Brain, Cognition and Behaviour, Radboud University Nijmegen, 6525 EZ Nijmegen, The Netherlands 4Wellcome Trust Centre for Neuroimaging, University College London, London, WC1N 3BG, UK

## Abstract

When asked to perform the same task, different individuals exhibit markedly different patterns of brain activity. This variability is often attributed to volatile factors such as task strategy or compliance. We propose that individual differences in brain responses are, to a large degree, inherentto the brain, and can be predicted from task-independentmeasurements collected at rest. Using a large set of task conditions, spanning several behavioral domains, we train a simple model that relates task-independent measurements to task activity and evaluate the model by predicting task activation maps for unseen subjects. Our model can accurately predict individual differences in brain activity highlighting a coupling between brain connectivity and function that can be captured at the level of individual subjects.

[Figure 2]

We all differ in how we perceive, think, and act. Our brains also differ in how they solve tasks. Understanding these individual differences in brain activity is an important goal in neuroscience, as it provides a route for linking brain and behavior.

Often individual differences in brain activity induced by an experimental task are attributed to two possible factors. Firstly, they may be accounted for by differences in gross brain morphology. The vast majority of brain imaging studies rely on the spatial alignment of different brains (registration) to account for between-subject discrepancies in gross anatomy

(1). Secondly, subjects may use different strategies or cognitive processes that involve different brain circuits. Psychologists design their tasks with great care to limit this source of variability. Nevertheless individual variations are seen in all behavioral domains (2–6). These between-subject differences are often treated as ‘noise’ in imaging studies and discarded through the process of averaging individual responses (7). Importantly, it is thought that such individual differences are mainly explained by volatile factors related to the behavior.

*Correspondence to: Saad Jbabdi; saad@fmrib.ox.ac.uk; tel: 44 1865 222466, fax: 44 1865 222717, address: FMRIB Centre, University of Oxford, John Radcliffe Hospital, Oxford OX3 9DU, UK.

[Figure 3]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 4]

We investigated the possibility that individual differences in brain activation are inherent features of individuals, and to a large degree independent of volatile factors. We explored the extent to which individual differences in task-evoked brain activity can be predicted by differences in the functional connectivity of the brain, acquired in an MRI scanner while the subjects are at rest, and not performing any explicit task. We aimed to predict severaltaskevoked activity maps matching individual subjects' maps in multiple behavioral domains based on a single task-free scan (i.e., unconstrained cognition during rest, with no explicit experimental task) of any given subject.

We designed a set of regression-based models that use task-independentfeatures to predict individual task-evokedresponses. Based on the hypothesis that functional differentiation in the brain can be understood in terms of the underlying long-range brain connections and interactions (8, 9), we used predictors based on functional connectivity at rest (10). Brain networks, extracted from resting-state data sets, qualitatively resemble task-evoked networks at the group level (11). We therefore hypothesized that using functional connectivity at rest we could predict individual variations in task responses. We also used predictors encoding individual brain morphology (gross structure) and microstructure to yield a total of 107 predictors (see Materials and Methods). All of our predictors were based on imaging subjects at rest, and were independent of any given task. The model was trained to map between the predictors and task activations in a cohort of subjects for each task, and subsequently the trained model was applied to out-of-sample (unseen) subjects to predict their task activations (leave-one-out approach, see Materials and Methods for details). Throughout, we focused on predicting task activations on the cortex, though the approach can easily be extended to incorporate subcortical gray matter.

Our data were a subset (98 subjects) of the Human Connectome Project (HCP) database (12). HCP data were chosen for their inclusion of resting-state measurements, diffusionweighted MRI, structural MRI as well as task-evoked data spanning several behavioral domains. We could therefore use the same set of task-free data to test predictions of several different tasks. The HCP task data include 7 behavioral domains, and each task set comprises several statistical maps pertaining to different aspects of each task (all tasks and derived parametric maps are described in (13)). A total of 47 independent task maps (zscores) were available for each subject (see Materials and Methods).

We aimed to predict not how subjects activate on average in a given task, but how they differ (from each other) in their activation patterns. Figure 1 illustrates this aspect of the model in four different task conditions (maps thresholded as described in Materials and Methods). The model could predict qualitative differences between subjects, in terms of shape, position, size and topography of activations. Figures S1-S3 and supplementary movies SM1SM6 show similar individual variations predicted across more subjects and all behavioral domains used by the HCP. The model could precisely predict individual task variations across all behavioral domains, based on a single task-free dataset. To get an impression of how similar our predictions are to the actual task maps, we overlapped the predictions for three subjects with their actual activation maps (Fig. 2A) for the contrast MATH-STORY from the LANGUAGE task. For comparison, we also overlapped the same subjects with the actual activation map of a canonical (median) subject. The maximum overlap was obtained

[Figure 5]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 6]

when comparing a given subject's prediction to their actual map. This was despite our use of a leave-one-out approach: the predictive model for subject X had not seen the activation map of subject X during training, but it had seen the maps of all other subjects. Nevertheless, the prediction was more similar to the map it had not seen (subject X) than to the maps it had seen (all but subject X). The model did not learn what the activations for a given task looked like, but rather it learned how to mapfrom the features (resting-state connectivity and morphology) to the task maps in individual subjects.

To quantitatively assess the performance of the model, we estimated the spatial correlation between the (unthresholded) predictions and actual maps for all pairs of subjects (Fig. 2B and 2C). Each entry in the matrix is the Pearson correlation between the task map of one subject and the predicted map of another (off-diagonal) or the same (on-diagonal) subject. The correlation matrix is noticeably diagonal-dominant, indicating that on average the model prediction for any given subject is more similar to the subject's own map than to other subjects' maps (see also the histograms shown in figures 2B-C comparing on-diagonal to offdiagonal entries). Normalising rows and columns of the correlation matrix (which removes the overall mean correlation and accounts for the fact that the actual maps are more variable than the predicted maps) shows the diagonal-dominance even more clearly (see also figures S4-6 in which we show the same results for all contrast maps). The diagonal-dominance is apparent for all tasks and contrast maps, with the exception of one contrast map (GAMBLING PUNISH-REWARD). The reason is that activations for this contrast are restricted to sub-cortical gray matter, whereas our model only makes predictions for the cortex. This result, i.e., the diagonal dominance of the spatial correlation matrix, is nontrivial considering that our leave-one-out procedure ensures that whenever a model is applied to predict a given subject, it has never seen that subject's task map during training. Yet, the prediction matches that subject's task data better than the subjects that it has seen during training. The model's ability to generalize beyond the training subjects has important implications. It can predict activations in individuals for which there are no available task data (e.g. patients who cannot perform the task).

The model can precisely capture inter-individual variability (Table S3). There are different types of such variations. Functional brain areas in individual subjects can greatly vary in size, location, and shape (14). Primary visual cortex, for instance, can vary (across different subjects) by a factor of two or more in surface area (15). Such variability still allows one-toone mapping of brain areas across subjects, provided that individual areas can be mapped in individual subjects. But another type of variation is topological variability, which for example means that different subjects may have different patterns of activity with no obvious one-to-one correspondence between subjects. Both types of variability (shape/size vs topological) can be captured by this model (Fig. 3A). Importantly, topological variability cannot be accounted for using spatial alignment between subjects, and thus comparing or averaging subjects' activations when they have different topologies is an open problem. The fact that we can predict such variability from task-free data may enable new strategies for matching brain networks, as opposed to brain areas, across subjects.

Our model can also make predictions on the distribution of activity across different systems, such as in the case of hemispheric lateralization. Lateralization of function is seen

[Figure 7]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 8]

commonly in the domain of language (16), but also in attentional processing (17). Figure 3B shows how our model can predict such differences across individuals in a language task. We estimated a lateralization index defined as the difference between right hemisphere and left hemisphere peak Z (averaged over a 10 mm radius sphere around the predicted peak) from the predictions and the actual data. The model is able to precisely predict individual subjects' lateralization index. We also predicted two different contrasts from the same task (MATHSTORY and STORY-MATH) where the former tends to show an approximately equal distribution among left and right lateralized individuals, whereas the latter shows more left lateralized subjects. The model can capture the lateralized language trend, even for the minority of right-lateralized subjects, despite the fact that, for the STORY-MATH contrast, it has been trained on subjects the majority of whom are left-lateralized.

The model could also predict atypical activation patterns. In Fig. 4, we show in five different behavioral domains examples of subjects that either do or do not conform to the pattern seen in the average subject. The model predicted activations in regions that were not activated on average. Conversely the model correctly predicted the lackof activations in regions that were activated on average.

Overall, a simple set of models trained to learn a mapping between task-free and taskevoked maps could be used to predict individual differences in activation maps accurately across a wide range of behavioral domains. The predicted maps matched even large individual variations in the spatial layout of brain activity, including position, shape, size and topology of functional activations (e.g. whether the activity is localised or spread-out, or whether it consists of a single region or multiple sub-regions). The model could also predict individual differences in the amountof activation in a given task from a task-free data set.

The model mainly used resting-state connectivity in addition to a few structural features capturing local morphology and micro-structure (see Materials and Methods). On average across all tasks, all features participated in the predictions except for sub-cortical connectivity features (excluding the cerebellum - see Figs. S7 and S8). Although the structural features were exploited by the model (Fig. S7), removing them did not affect the performance of the model (Fig. S9), and using a model purely based on structural features abolishes inter-individual variability in the predictions (Fig S10). This suggests that restingstate connectivity alone is sufficient to predict individual variability in task maps, independently from variations of morphology as captured by our handful of structural features. It is however possible that additional anatomical variability may also be indirectly captured by the resting-state data.

Why can we predict task-evoked activity from resting-state data? A good match between resting state networks and task networks at the group level has been shown before (11, 18), where it has been argued that functional networks are continuously interacting with each other at rest, with the same functional hierarchy that is seen during action and cognition. Our model provides an explicit mapping from resting-state data to task maps that corroborates this assumption, but it is important to consider alternative explanations of our result. Intersubject alignment may be sub-optimal when using anatomy alone. Our model is therefore possibly accounting for functional misalignment between subjects (19). However, the model

[Figure 9]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 10]

not only tracks variation in the position and shape of functional areas, but also captures variations in the topology of the brain networks activated in individual subjects, and can predict activations of atypical subjects. Therefore, it is unlikely that the standard approach of aligning subjects while preserving the brain topology will be able to fix these types of misalignments. Our model can make quantitative predictions, in terms of the amount of activity that individual subjects display during task. Such predictions are unlikely to arise from misalignment considerations. Resting-state data may provide a means for "calibration" of the BOLD signal (20). However, our predictors are based on measures of connectivity rather than raw BOLD signal strength per se (although signal-to-noise may still affect functional connectivity at rest (21)). Determining what information in the resting-state signal is driving our predictions will be important for understanding its nature and potential. Because all the predictors that were used in this study are based on scans acquired at rest, our model is blind to different strategies that are chosen by the participants in performing a given task. We refer to these features as "inherent", but we acknowledge that these can be "structurally inherent" (related to brain organization and connectivity) or "functionally inherent" (related to the cognitive state of subjects during the resting state scan).

The idea that brain connectivity can predict activation has previously been reported for different modalities (22), where diffusion MRI tractography was used (23) to measure connectivity. This study was limited to a specific cognitive task and a pre-defined anatomical region. More recently, resting-state connectivity has been shown to be predictive of subjects' identity, in a similar way to a fingerprint (24). Rather than simply identifying subjects, our goal was to predict the entire layout of brain activity for each subject. Moreover, we also aim to predict such layout of activity in a number of different cognitive domains, from a single task-free scan, including in subjects that show patterns of activation that are different from the group average (perhaps most strikingly in right-lateralized subjects when the majority of training subjects are left-lateralized).

There are significant practical implications to the proposed framework in basic research and translational neuroscience. It provides a method for inferring multiple individualized functional localizers based on a singleresting state scan. Such a tool could be used to investigate in detail the response profiles of localized brain regions without the need to acquire often time-consuming task localizers. Importantly, such a tool, if generalizable beyond the young, healthy population that makes up the HCP database, could be used to investigate functional regions in subjects who cannot perform tasks, such as paralyzed patients or infants.

## Supplementary Material

Refer to Web version on PubMed Central for supplementary material.

## Acknowledgments

Data were provided by the Human Connectome Project, WU-Minn Consortium (Principal Investigators: David Van Essen and Kamil Ugurbil; 1U54MH091657) funded by the 16 NIH Institutes and Centers that support the NIH Blueprint for Neuroscience Research; and by the McDonnell Center for Systems Neuroscience at Washington University. The data are available for download at www.humanconnectome.org. Data from the Q3 release (September 2013) were used in this paper. All code available upon request from the corresponding author. Funding

[Figure 11]

EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 12]

was provided by the UK Medical Research Council (MR/L009013/1 to SJ), UK EPSRC (EP/L023067/1 to SJ and TEB), James S McDonnell Foundation (JSMF220020372 to TEB), the Wellcome Trust (WT104765MA to TEB and 098369/Z/12/Z to SMS) and the Netherlands Organization for Scientific Research NWO (452-13-015 to RBM). Author contributions were as follows: SJ and IT built the model and performed the analyses. SJ, IT, RBM, OPJ, SMS and TEB wrote the paper.

## References and Notes

- 1. Jenkinson M, Smith S. A global optimisation method for robust affine registration of brain images. Medical Image Analysis. 2001; 5:143–156. [PubMed: 11516708]
- 2. Besle J, Sanchez-Panchuelo RM, Bowtell R, Francis S, Schluppeck D. Single-subject fMRI mapping at 7 T of the representation of fingertips in S1: a comparison of event-related and phaseencoding designs. J Neurophysiol. 2013; 109:2293–2305. DOI: 10.1152/jn.00499.2012 [PubMed: 23427300]
- 3. McNab F, Klingberg T. Prefrontal cortex and basal ganglia control access to working memory. Nat Neurosci. 2008; 11:103–107. DOI: 10.1038/nn2024 [PubMed: 18066057]
- 4. Mukai I, Kim D, Fukunaga M, Japee S, Marrett S, Ungerleider LG. Activations in visual and attention-related areas predict and correlate with the degree of perceptual learning. J Neurosci. 2007; 27:11401–11411. DOI: 10.1523/JNEUROSCI.3002-07.2007 [PubMed: 17942734]
- 5. Tom SM, Fox CR, Trepel C, Poldrack RA. The neural basis of loss aversion in decision-making under risk. Science. 2007; 315:515–518. DOI: 10.1126/science.1134239 [PubMed: 17255512]
- 6. Wig GS, Grafton ST, Demos KE, Wolford GL, Petersen SE, Kelley WM. Medial temporal lobe BOLD activity at rest predicts individual differences in memory ability in healthy young adults. Proc Natl Acad Sci U S A. 2008; 105:18555–18560. DOI: 10.1073/pnas.0804546105 [PubMed: 19001272]
- 7. Kanai R, Rees G. The structural basis of inter-individual differences in human behaviour and cognition. Nat Rev Neurosci. 2011; 12:231–242. DOI: 10.1038/nrn3000 [PubMed: 21407245]
- 8. Behrens TE, Johansen-Berg H. Relating connectional architecture to grey matter function using diffusion imaging. Philos Trans R Soc Lond B Biol Sci. 2005; 360:903–911. [PubMed: 16087435]
- 9. Passingham RE, Stephan KE, Kotter R. The anatomical basis of functional localization in the cortex. Nat Rev Neurosci. 2002; 3:606–616. [PubMed: 12154362]
- 10. Yeo BT, Krienen FM, Sepulcre J, Sabuncu MR, Lashkari D, Hollinshead M, Roffman JL, Smoller JW, Zollei L, Polimeni JR, Fischl B, et al. The organization of the human cerebral cortex estimated by intrinsic functional connectivity. J Neurophysiol. 2011; 106:1125–1165. DOI: 10.1152/jn. 00338.2011 [PubMed: 21653723]
- 11. Smith SM, Fox PT, Miller KL, Glahn DC, Fox PM, Mackay CE, Filippini N, Watkins KE, Toro R, Laird AR, Beckmann CF. Correspondence of the brain's functional architecture during activation and rest. Proc Natl Acad Sci U S A. 2009; 106:13040–13045. [PubMed: 19620724]
- 12. Van Essen DC, Smith SM, Barch DM, Behrens TE, Yacoub E, Ugurbil K, W. U.-M. H. Consortium. The WU-Minn Human Connectome Project: an overview. Neuroimage. 2013; 80:62–

79. DOI: 10.1016/j.neuroimage.2013.05.041 [PubMed: 23684880]

- 13. Barch DM, Burgess GC, Harms MP, Petersen SE, Schlaggar BL, Corbetta M, Glasser MF, Curtiss S, Dixit S, Feldt C, Nolan D, et al. Function in the human connectome: task-fMRI and individual differences in behavior. Neuroimage. 2013; 80:169–189. DOI: 10.1016/j.neuroimage.2013.05.033 [PubMed: 23684877]
- 14. Fischl, B, Rajendran, N, Busa, E, Augustinack, J, Hinds, O, Yeo, B, Mohlberg, H, Amunts, K, Zilles, K. Cereb Cortex. Department of Radiology, Harvard Medical School; Charlestown, MA 02129, USA: 2007.
- 15. Andrews TJ, Halpern SD, Purves D. Correlated size variations in human visual cortex, lateral geniculate nucleus, and optic tract. J Neurosci. 1997; 17:2859–2868. [PubMed: 9092607]
- 16. Knecht S, Deppe M, Drager B, Bobe L, Lohmann H, Ringelstein E, Henningsen H. Language lateralization in healthy right-handers. Brain. 2000; 23(Pt 1):74–81.
- 17. Thiebaut de Schotten M, Urbanski M, Duffau H, Volle E, Levy R, Dubois B, Bartolomeo P. Direct evidence for a parietal-frontal pathway subserving spatial awareness in humans. Science. 2005; 309:2226–2228. DOI: 10.1126/science.1116251 [PubMed: 16195465]

[Figure 13]

EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 14]

- 18. Cole MW, Bassett DS, Power JD, Braver TS, Petersen SE. Intrinsic and task-evoked network architectures of the human brain. Neuron. 2014; 83:238–251. DOI: 10.1016/j.neuron.2014.05.014 [PubMed: 24991964]
- 19. Robinson EC, Jbabdi S, Glasser MF, Andersson J, Burgess GC, Harms MP, Smith SM, Van Essen DC, Jenkinson M. MSM: a new flexible framework for Multimodal Surface Matching. Neuroimage. 2014; 100:414–426. DOI: 10.1016/j.neuroimage.2014.05.069 [PubMed: 24939340]
- 20. Logothetis NK, Wandell BA. Interpreting the BOLD signal. Annual review of physiology. 2004; 66:735–769. DOI: 10.1146/annurev.physiol.66.082602.092845
- 21. Friston K. Functional and effective connectivity: a review. Brain Connectivity. 2011
- 22. Saygin ZM, Osher DE, Koldewyn K, Reynolds G, Gabrieli JDE, Saxe RR. Wired for function: Anatomical connectivity patterns predict face-selectivity in the fusiform gyrus. Nat Neurosci. 2012; 15
- 23. Basser PJ, Pajevic S, Pierpaoli C, Duda J, Aldroubi A. In vivo fiber tractography using DT-MRI data. Magn Reson Med. 2000; 44:625–632. [PubMed: 11025519]
- 24. Finn ES, Shen X, Scheinost D, Rosenberg MD, Huang J, Chun MM, Papademetris X, Constable RT. Functional connectome fingerprinting: identifying individuals using patterns of brain connectivity. Nat Neurosci. 2015; 18:1664–1671. DOI: 10.1038/nn.4135 [PubMed: 26457551]

[Figure 15]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 16]

|One Sentence Summary<br><br>Resting-state connectivity predicts individual task activation maps across several behavioral domains.|
|---|

[Figure 17]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 18]

[Figure 19]

Fig. 1. Predicting individual variations in task maps.

Figure shows actual and predicted thresholded task maps in 3 subjects and 4 different task contrasts. The model is able to capture striking variations between subjects in the shape, topology and extent of their activation maps. Predictions and comparisons to actual maps for all behavioral domains and more subjects are shown in Figures S1-S3 and movies SM1SM6.

[Figure 20]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 21]

[Figure 22]

Fig. 2. Specificity of the individual predictions.

A subject’s prediction map is more similar to the subject’s actual map than to the rest of the subjects. (A) Predicted maps (zoomed on the right frontal lobe) of the MATH-STORY contrast from the LANGUAGE task of 3 subjects are overlapped with their actual activation maps (top row). We also overlap the subjects' predictions with the activation map of the median subject (bottom row). Blue represents actual activation, red is the predicted activation and yellow is the overlap. The maximum overlap is obtained when comparing a given subject's prediction to their own actual map. (B) Pearson correlation matrix between actual (columns) and predicted activations (rows). The correlation matrix is noticeably diagonal-dominant, indicating that on average the model prediction for any given subject is more similar to the subject's own map than to other subjects' maps. This is also shown as a histogram plot, where the extra-diagonal elements of the correlation matrix (subject X vs subject Y) are compared to the diagonal elements (subject X vs subject X). The vertical dashed line corresponds to the median of the correlation coefficients along the diagonal. (C) Correlation matrices and histograms for 6 additional behavioral domains. When normalizing the rows and columns of the correlation matrices (which removes the mean and accounts for higher variability in actual than predicted maps), the diagonal-dominance is even more

[Figure 23]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 24]

prominent. In all cases, a Kolmogorov-Smirnov test between the two distributions (self vs other) gives a highly significant difference (p < 10-10).

[Figure 25]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 26]

[Figure 27]

Fig. 3. Capturing qualitative and quantitative inter-individual differences.

A. Variations in location, shape and topology are predicted by the model (contrast: LANGUAGE MATH-STORY). B. Peak Z scores were calculated for each hemisphere to examine how well the model can predict the amount of activation for each subject. A lateralization index (difference between right and left peak activation levels) is then calculated for each subject for both predicted and actual data and is shown as red and blue bars, respectively (LANGUAGE task). The model is able to predict individual subjects' lateralization index for both contrasts, including in the case where the majority of the subjects are left-lateralized. Statistical tests: MATH-STORY (r = 0.47, p < 10-5), STORYMATH (r = 0.48, p < 10-6).

[Figure 28]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 29]

[Figure 30]

Fig. 4. Predictions in atypical subjects.

The figure demonstrates the ability of our prediction model to detect inter-subject variability when subjects differ from the group-averaged activation. In each row the group activation for each behavioral domain is shown on the left, and the actual and predicted activations for 2 subjects are shown on the right. In each row we show activations and predictions for one subject that is similar to the group activation (A) and one that differs from it (B) as shown by the black circles. The model can capture the presence of clusters that are not active in the group (rows 1,4,5) as well as the absence of clusters that are active in the group (rows 2,3). Note that subjects A and B are not the same pair of subjects across behavioral domains.

