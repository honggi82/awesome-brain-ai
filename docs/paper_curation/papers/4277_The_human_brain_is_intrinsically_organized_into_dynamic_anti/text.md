[Figure 1]

## The human brain is intrinsically organized into dynamic, anticorrelated functional networks

#### Michael D. Fox*†, Abraham Z. Snyder*‡, Justin L. Vincent*, Maurizio Corbetta‡, David C. Van Essen§, and Marcus E. Raichle*‡§¶

Departments of *Radiology, ‡Neurology, §Anatomy and Neurobiology, and ¶Biomedical Engineering, Washington University, St. Louis, MO 63110 Contributed by Marcus E. Raichle, May 19, 2005

During performance of attention-demanding cognitive tasks, certain regions of the brain routinely increase activity, whereas others routinely decrease activity. In this study, we investigate the extent to which this task-related dichotomy is represented intrinsically in the resting human brain through examination of spontaneous ﬂuctuations in the functional MRI blood oxygen level-dependent signal. We identify two diametrically opposed, widely distributed brain networks on the basis of both spontaneous correlations within each network and anticorrelations between networks. One network consists of regions routinely exhibiting task-related activations and the other of regions routinely exhibiting task-related deactivations. This intrinsic organization, featuring the presence of anticorrelated networks in the absence of overt task performance, provides a critical context in which to understand brain function. We suggest that both task-driven neuronal responses and behavior are reﬂections of this dynamic, ongoing, functional organization of the brain.

functional MRI functional connectivity spontaneous activity

# F

unctional imaging techniques such as positron emission tomography and functional MRI (fMRI) have proven to be

valuable tools in the investigation of human brain function. Typically a task or stimulus is presented and changes in brain activity in response to the stimulus are recorded. For example, a flashing checkerboard stimulus is associated with spatially specific activity increases in the visual cortex and an auditory stimulus with increased activity in the auditory cortex.

During performance of attention-demanding cognitive tasks, two opposite types of responses are commonly observed. A specific set of frontal and parietal cortical regions routinely exhibit activity increases (1, 2), whereas a different set of regions, including posterior cingulate, medial and lateral parietal, and medial prefrontal cortex (MPF), routinely exhibit activity decreases (3–7). As the attentional demand of the task is increased, this dichotomy generally becomes more pronounced; activity in positive regions is further increased (8), whereas activity in negative regions is further decreased (6).

Activity increases in frontal and parietal regions have been associated with top-down modulation of attention and working memory (1, 2, 9), processes commonly recruited by cognitive task paradigms. Activity decreases are generally proportional to task difficulty (6), but may be attenuated by self-referential aspects of a task such as emotion (4, 10, 11) or episodic memory (12) as well as the intrusion of task-independent thoughts (13). Simply stated, the dichotomy observed in response to attentiondemanding cognitive tasks involves increased activity in regions whose function supports task execution and decreased activity in regions presumably supporting unrelated or irrelevant processes.

Although the majority of researchers performing functional imaging studies continue to examine changes in brain activity associated with task performance, some now study spontaneous brain activity present in the absence of a task. These resting-state functional connectivity studies examine correlations in slow ( 0.1 Hz) spontaneous fluctuations in the blood oxygen leveldependent (BOLD) signal (14). Biswal and colleagues (15) were

the first to show that these spontaneous fluctuations were coherent within specific neuro-anatomical systems such as the somatomotor system (15). Their results have been confirmed and extended to several other systems, including visual, auditory, and language processing networks (15–19). Important for the present study, correlated fluctuations have been demonstrated between frontal and parietal areas often observed to increase activity during task performance (19, 20) and within the network of regions commonly exhibiting activity decreases during task performance (16, 20, 21).

The collective result of the above studies is that regions similarly modulated by tasks or stimuli tend to exhibit correlated spontaneous fluctuations even in the absence of tasks or stimuli. This result holds true even at different spatial and temporal scales, for example, in orientation columns in the visual cortex (22). An important question is the extent to which task-related functionality is represented intrinsically in the brain. If regions with similar task-related responses are correlated, what is the relationship between regions with dissimilar task-related responses? Specifically, is the task-related dichotomy between regions routinely exhibiting task-positive responses and those routinely exhibiting task-negative responses represented intrinsically in the resting brain? To address this question, we examine both correlations and anticorrelations in spontaneous BOLD fluctuations associated with six predefined regions of interest. Three of these regions are known to routinely exhibit taskpositive responses (activations) and three are known to routinely exhibit task-negative responses (deactivations) during attentiondemanding tasks (1–7, 9).

### Methods

Data Acquisition. Ten normal right-handed subjects underwent three 5.5-min scans in three different rest conditions: visual fixation on a crosshair, eyes closed, and eyes open in low-level illumination (without fixation). All imaging was performed on a 3T Siemens Allegra system (Erlagen, Germany). Electroencephalograms were also obtained during the functional scans, but were not used in the present analysis. Functional data were collected by using an asymmetric spin-echo, echo-planar sequence sensitive to BOLD contrast [echo time (TE) 25 ms, flip angle 90°, 4 4 4-mm isotropic voxels, volume repetition time (TR) 3.013 s). The volume TR included a 1-s pause between frames. Whole brain coverage was obtained with 32 contiguous slices. Structural data (for definitive atlas transformation) included two high-resolution (1 1 1.25 mm) sagittal, T1-weighted magnetization-prepared rapid gradient-echo scans (TR 2.1 s, TE 3.93 ms, flip angle 7°) and a T2-weighted fast spin echo scan.

Freely available online through the PNAS open access option.

Abbreviations: fMRI, functional MRI; BOLD, blood oxygen level-dependent; IPS, intraparietal sulcus; FEF, frontal eye ﬁeld; MT , middle temporal region; MPF, medial prefrontal cortex;PCC,posteriorcingulate precuneus;LP,lateralparietalcortex;SMA,supplementary motor area.

†To whom correspondence should be addressed. E-mail: foxm@npg.wustl.edu. © 2005 by The National Academy of Sciences of the USA

##### NEUROSCIENCE

www.pnas.org cgi doi 10.1073 pnas.0504136102 PNAS July 5, 2005 vol. 102 no. 27 9673–9678

[Figure 2]

Preprocessing of Functional Data. fMRI preprocessing steps included: first, compensation of systematic, slice-dependent time shifts; second, elimination of systematic odd-even slice intensity differences caused by interleaved acquisition; and, third, rigid body correction for interframe head motion within and across runs. Step three provided a record of head position within and across all fMRI runs. Each fMRI run was intensity scaled (one multiplicative constant over all voxels and frames) to yield a whole brain mode value of 1,000 (not counting the first four frames) (23). Atlas registration was achieved by computing affine transforms connecting the fMRI run first frame (averaged over all runs after cross-run realignment) with the T2-weighted and average T1-weighted structural images (23). Our atlas representative template includes magnetization-prepared rapid gradient-echo data from 12 normal individuals and was made to conform to the 1988 Talairach atlas (24). To prepare the BOLD data for the present main analyses, each fMRI run was transformed to atlas space and resampled to 3-mm cubic voxels.

Correlation Techniques. Several processing steps were used to optimally condition the functional data for analysis of voxelbased correlations. Data were temporally band-pass filtered (0.009 f 0.08) and spatially smoothed (6-mm full width at half maximum Gaussian blur). Several sources of spurious variance along with their temporal derivatives were then removed from the data through linear regression: (i) six parameters obtained by rigid body correction of head motion, (ii) the whole-brain signal averaged over a fixed region in atlas space, (iii) signal from a ventricular region of interest, and (iv) signal from a region centered in the white matter. This regression procedure removes fluctuations unlikely to be involved in specific regional correlations. Correlation maps were produced by extracting the BOLD time course from a seed region then computing the correlation coefficient between that time course and the time course from all other brain voxels. Seed regions were 12-mm-diameter spheres centered on previously published foci. For the current study we examined correlations associated with six predefined seed regions: three regions, referred to as task-positive regions, routinely exhibiting activity increases during task performance, and three regions, referred to as tasknegative regions, routinely exhibiting activity decreases during task performance (2, 5, 9). Task-positive regions were centered in the intraparietal sulcus (IPS; 25, 57, 46), the frontal eye field (FEF) region of the precentral sulcus (25, 13, 50), and the middle temporal region (MT , 45, 69, 2) by using the three most significant foci exhibiting activity increases from a study of externally cued attention and working memory (9). Although these foci were defined on the basis of a single study, similar foci have been reported in numerous studies of external attention and or working memory (1). Task-negative regions were centered in the MPF ( 1, 47, 4), posterior cingulate precuneus (PCC, 5, 49, 40), and lateral parietal cortex (LP, 45, 67, 36) by using the three most significant foci from a metaanalysis of decreases during task performance (5).

Correlation Statistics. To combine results across subjects and compute statistical significance, correlation coefficients were converted to a normal distribution by Fischer’s z transform (25). These values were converted to z scores (i.e., zero mean, unit variance, Gaussian distributions) by dividing by the square root of the variance, computed as 1 (n 3), where n is the degrees of freedom in the measurement. Because individual time points in the BOLD signal are not statistically independent, the degrees of freedom must be corrected according to Bartlett’s theory (25). The correction factor for independent frames was calculated to be 2.34, resulting in 318 2.34 135.9 df. Z-score maps were combined across subjects by using a fixed-effects analysis. Finally, population-based z-score maps were corrected for multiple

[Figure 3]

Fig. 1. Intrinsic correlations between a seed region in the PCC and all other voxels in the brain for a single subject during resting ﬁxation. The spatial distribution of correlation coefﬁcients shows both correlations (positive values) and anticorrelations (negative values), thresholded at R 0.3. The time course for a single run is shown for the seed region (PCC, yellow), a region positively correlated with this seed region in the MPF (orange), and a region negatively correlated with the seed region in the IPS (blue).

comparisons at a significance level of P 0.05 (z 3, cluster size 17 voxels).

Conjunction Analysis. Population-based z-score maps for the six seed regions were combined by using a conjunction analysis. First, the correlation maps for the three task-negative seed regions were multiplied by 1 then averaged with the correlation maps from the task-positive seed regions. This average was then masked by using a conservative conjunction procedure. Voxels were included in the mask only if they were significantly correlated or anticorrelated with five of the six seed regions. Peak foci in this conjunction map were identified by using an automated peak search algorithm with an absolute value threshold of 7.5. Peak foci of the same sign closer than 25 mm were combined through algebraic averaging (26).

Surface-Based Mapping. The volumetric statistical results were projected onto the cortical surface of the PALS (populationaverage landmark- and surface-based) atlas by using a multifiducial mapping method that circumvents the biases of choosing a hemisphere from a single individual as an atlas target (49). The visualization threshold for the average activation pattern was set at a level that yielded a surface area equaling the average surface area for the mappings to each of the 12 individual target surfaces.

### Results

We examined resting state correlations associated with six predefined seed regions, three regions routinely exhibiting activity increases (task-positive regions) and three regions routinely exhibiting activity decreases (task-negative regions) during attention-demanding cognitive tasks (2, 5, 9). Taskpositive regions included the IPS, FEF region of the precentral sulcus, and MT . Task-negative regions included the MPF, PCC, and LP.

The correlation coefficients between time courses from each of the six seed regions and all other voxels in the brain were then computed for each individual. The results from a single individual for a seed region in the PCC are shown in Fig. 1. Fig. 1 Upper shows the regional distribution of correlation coefficients, and Fig. 1 Lower shows time courses for the PCC seed region (yellow), a MPF region positively correlated with the seed

[Figure 4]

[Figure 5]

- Fig. 2. Population-based z-score maps showing nodes signiﬁcantly correlated or anticorrelated with six seed regions (small circles). (Upper) (Left) Results from three task-negative seed regions: MPF, PCC, and LP. (Right) Results from three task-positive seed regions: IPS, FEF, and MT . (Lower) The conjunction map is an average, including only nodes signiﬁcantly correlated or anticorrelated with ﬁve of the six seed regions. White contours are drawn on the conjunction map and copied onto the other maps to facilitate comparison.

(orange), and an IPS region anticorrelated with the seed (blue). The PCC is positively correlated with regions in the MPF and LP, an observation in agreement with previous results (16). However, we also note strong anticorrelations with regions including the IPS, FEF, MT , the supplementary motor area (SMA), and insula.

To assess statistical significance and combine results across subjects, correlation coefficients for each subject were converted to z-score values (see Methods). The population-averaged correlation maps for each of the six regions of interest are displayed on the flattened left hemisphere in Fig. 2 Upper. Each map has been corrected for multiple comparisons at a significance level of P 0.05. Positive z-score values are significantly correlated with the seed region, whereas negative z-score values are significantly anticorrelated.

Fig. 2 Upper Left displays correlation maps for the three task-negative seed regions, and Fig. 2 Upper Right shows maps for the three task-positive seed regions. All three task-positive seed maps are strikingly similar, as are all three task-negative seed maps, although potentially interesting variations depending on seed region can be seen. Critically, the task-positive seed maps (Fig. 2 Upper Right) are to a large extent sign-inverted versions

of the task-negative seed maps (Fig. 2 Upper Left). These results indicate that BOLD fluctuations are correlated within two widely distributed systems and further that these two systems are largely anticorrelated.

To confirm the above impressions, the six correlation maps were combined by using a modified conjunction analysis (see Methods). Voxels were included in the conjunction map only if they were significantly correlated or anticorrelated with five of the six seed regions. The resulting conjunction map is shown on a flattened brain in Fig. 2 Lower, on the surface of an inflated brain in Fig. 3, and for selected slices in Fig. 4, which is published as supporting information on the PNAS web site. Positive values are significantly correlated with task-positive seed regions and significantly anticorrelated with task-negative seed regions, whereas the inverse is true for negative values. This procedure thus defines two widely distributed, anticorrelated brain networks on the basis of intrinsic fluctuations in neuronal activity. Parallel analyses were conducted for the eyes closed and eyes open (no-fixation) conditions with similar results (Fig. 5, which is published as supporting information on the PNAS web site), including regions in the parahippocampal gyri and cerebellar tonsils.

Automated peak search was used to identify foci of maximum significance in the fixation condition conjunction map (Table 1). Fifteen foci were identified as part of the task-positive network and 15 as part of the task-negative network. The task-positive network consists of regions in the IPS and inferior parietal lobule, precentral sulcus including FEF, dorsal lateral prefrontal cortex, MT , insula frontal operculum, and the SMA. The task-negative network consists of regions in the PCC, retrosplenial cortex, medial prefrontal, lateral parietal, superior frontal, parahippocampal gyri, inferior temporal, and cerebellar tonsils.

### Discussion

Our current results demonstrate that the activation deactivation dichotomy routinely observed in response to attentiondemanding tasks is represented intrinsically in the resting human brain, demonstrable in the absence of any overt task or behavior. We show that widely distributed neuro-anatomical networks are organized through both correlated spontaneous fluctuations within a network and anticorrelations between networks.

The task-positive network consists of regions routinely activated during goal-directed task performance (1). It includes a set of regions previously termed the ‘‘endogenous’’ or ‘‘dorsal attention system’’ (IPS, FEF) active during directed attention (2). In addition, the task-positive network includes dorsal-lateral and ventral prefrontal regions, insula, and SMA, activated by a variety of demanding cognitive tasks (1, 27).

The task-negative network consists of regions commonly exhibiting activity decreases during task performance (4–6) and implicated in various aspects of self-referential processing (3). Our currently defined task-negative network includes a set of regions often referred to as a ‘‘default system’’ to connote greater activity at rest than during the performance of various goal-directed tasks (3, 28). One component of the task-negative network, the cerebellar tonsils, has not been previously noted. This unexpected finding was replicated in all three resting conditions, suggesting that this poorly understood region of the cerebellum may contribute in some unique way to the functionality of the task-negative network.

In addition to the regions included in our current task-positive and task-negative networks, it is important to comment on the regions not included, specifically primary sensory and motor cortices. Although one might expect that these areas would be correlated with the task-positive network because of their common activation during task paradigms, it is clear that they show no intrinsic preference for either network. Neither the taskpositive nor task-negative network is intrinsically linked to our

##### NEUROSCIENCE

[Figure 6]

[Figure 7]

- Fig. 3. Intrinsically deﬁned anticorrelated processing networks in the brain. Positive nodes are signiﬁcantly correlated with seed regions involved in focused attention and working memory (task-positive seeds) and signiﬁcantly anticorrelated with seed regions routinely deactivated during attention demanding cognitive tasks (task-negative seeds). Negative nodes are signiﬁcantly correlated with task-negative seed regions and signiﬁcantly anticorrelated with task-positive seed regions. (Left) Lateral and medial views of left hemisphere. (Center) Dorsal view. (Right) Lateral and medial views of right hemisphere.

direct interfaces with the external world, an observation relevant to understanding the functionality of these widely distributed networks of higher-order brain structures.

The reproducibility of the current findings across three different resting states (fixation, eyes closed, and eyes open) demonstrates that our results cannot be attributed to the imposition of a low-level task (fixation), eye movements, or the presence or absence of visual input. Rather our results appear to be robust with respect to variation in the resting state. This stability across different conditions is consistent with the literature in which similar correlations in slow ( 0.1 Hz) spontaneous fluctuations have been observed during task performance (17, 21, 29), at rest in the absence of a task (16–18, 30), and even under anesthesia (31).

The current results confirm and expand observations from previous resting-state functional connectivity studies. Both correlations and anticorrelations have been reported between some subcomponents of our currently defined task-positive and task-

negative networks. Correlated fluctuations have been demonstrated between frontal and parietal attentional areas (19, 20), part of our task-positive network, and between the majority of regions implicated in our task-negative network (16, 20, 21). Anticorrelations have been previously noted between a seed region in the premotor cortex (BA6), part of our task-positive network, and the posterior cingulate and medial prefrontal cortex, components of our task-negative network (17). Similarly, anticorrelations have been observed between seed regions in the lateral prefrontal cortex, part of our task-positive network, and voxels in the posterior cingulate, part of our task-negative network (16). Commenting on these results, Greicius and colleagues (16) suggested that intrinsic anticorrelated activity might relate to the differential task-related responses in these regions, a conclusion in line with our present interpretation. Our current results expand these previous observations both spatially and conceptually, defining widely distributed networks on the basis

Table 1. Peak foci for intrinsically deﬁned anticorrelated networks

Brodmann’s areas Common names Talairach coordinates The task-positive network

7 IPS ( 23, 66, 46) (25, 58, 52) 7 40 Inferior parietal lobule ( 42, 44, 49) (47, 37, 52)

19 Orbital gyrus (vIPS) ( 26, 80, 26) (35, 81, 29) 6 FEF (SPrCeS) ( 24, 12, 61) (28, 7, 54) 6 Inferior precentral sulcus ( 54, 0, 35) 6 32 SMA pre-SMA ( 2, 1, 51)

46 DLPFC ( 40, 39, 26) (38, 41, 22) 19 37 MT ( 47, 69, 3) (54, 63, 8)

Insula frontal operculum ( 45, 5, 8) (45, 4, 14) The task-negative network

- 31 PCC ( 2, 36, 37) 30 Retro-splenial (3, 51, 8) 39 LP ( 47, 67, 36) (53, 67, 36)
- 32 10 MPF ( 3, 39, 2) (1, 54, 21) 8 Superior frontal ( 14, 38, 52) (17, 37, 52)

20 21 Inferior temporal ( 61, 33, 15) (65, 17, 15) 35 Parahippocampal gyrus ( 22, 26, 16) (25, 26, 14)

Cerebellar tonsils (7, 52, 44)

vIPS, ventral intraparietal sulcus; SPreCes, superior precentral sulcus; DLPFC, dorsal lateral prefrontal cortex.

[Figure 8]

of both correlations and anticorrelations between multiple seed regions.

The present findings regarding spontaneous BOLD correlations should be considered in the context of the rich neurophysiological literature on coherent neuronal fluctuations or oscillations. Synchronous neuronal fluctuations have been reported across a broad range of frequencies and spatial scales (22, 32–37). These correlations can be spontaneous (22, 32, 33) or related to particular tasks or goals (35, 36). Synchrony may be present only transiently (35, 36) or more temporally stable (22, 32, 33, 38). It has likewise been suggested that neuronal fluctuations at high and low frequencies may be related, with lowerfrequency fluctuations corresponding to power modulations of higher-frequency bands, both demonstrating coherence at their respective spatial scales (33, 34, 37).

Correlations in the BOLD signal fall at a particular point along this synchrony spectrum. They occur over very slow frequencies ( 0.1 Hz) and large spatial scales and seem fairly consistent across time (15–18, 38). What then is the relationship between these coherent BOLD fluctuations and the synchrony observed at the other end of the spectrum, namely high-frequency (e.g., 40 Hz), spatially confined, transient correlations often discussed in relation to the ‘‘binding problem’’ (35, 36)?

Neuronal synchrony may serve a similar purpose regardless of the frequency, spatial scale, or temporal permanence. Specifically, synchrony could facilitate the coordination and organization of information processing in the brain across several spatial and temporal ranges (34). Thus, transient binding of perceptual fragments into a unified percept and sustained large-scale organization of distributed neuro-anatomical networks both may be mediated through similar mechanisms.

Although our current results share important theoretical properties with synchrony and coherence reported across different temporal and spatial scales, they extend this thinking in a critical way, suggesting that anticorrelations may be as important as correlations in brain organization. Little has been said previously in the neuronal synchrony literature regarding the role of anticorrelations. While correlations may serve an integrative role in combining neuronal activity subserving similar goals or representations, anticorrelations may serve a differentiating role segregating neuronal processes subserving opposite goals or competing representations.

The notion of opposing or competitive processes is well represented in the psychological, behavioral, and functional imaging literature.Examplesincludecompetitiveinteractionsbetweenemotion and cognition (4, 39, 40), focused attention vs. monitoring of one’s environment for behaviorally relevant events (2), and task focus vs. stimulus independent thought (41–44).

Perhaps most relevant to the current findings is the observed behavioral competition between task-focused attention and processes subserving stimulus-independent thought. During performance of cognitive tasks, thoughts occasionally emerge unrelated to the task or goal (41–44). The more stimulusindependent thoughts that occur during a task session, the worse the subject’s performance (42). Conversely, increasing the difficulty and attentional demand of the task results in fewer stimulus-independent thoughts (42–44). The suppression of stimulus-independent thoughts or ruminations through focus on

a cognitively engaging task has been applied therapeutically in psychiatric disorders such as depression and anxiety (41).

There is reason to believe there is a relationship between such behavioral phenomenon and our current results. Focused attention and goal-directed behavior are generally associated with increased activity in our task-positive network and decreased activity in our task-negative network (1–7, 9), whereas the emergence of stimulus-independent thought has been associated with increased activity in our task-negative network and a trend toward decreased activity in our task-positive network (13). It is therefore quite possible that this behavioral phenomenon emerges as a simple reflection of the underlying intrinsic and dynamic organization of the brain.

The demonstration of an anticorrelated relationship between the two networks presumably underlying focused attention and stimulus independent thought alters the interpretation of the origin of this behavioral effect. This phenomenon has been previously explained as a competition for processing resources from a poorly defined ‘‘central executive’’ (43) or ‘‘central cognitive operator’’ (44), a notion with strong conceptual ties to a ‘‘homunculus’’ controlling access to conscious awareness (45). Our current findings eliminate the need for a homunculus by suggesting the emergence of the phenomenon through intrinsic anticorrelated interactions occurring naturally and spontaneously in the human brain.

Many important questions remain regarding coherent neuronal fluctuations, and in particular the slow spontaneous fluctuations observable in the BOLD signal. Although it is clear that these fluctuations are coherent within specific neuro-anatomical systems, the origin of this synchrony and its function in neurological processingremainobscure.Whatistherelationshipbetweentheseslow spontaneous fluctuations, the brain’s response to a task or stimulus, and behavior? Likewise, are anticorrelations, like correlations, an organizational principal across various spatial and temporal scales? Understanding these relationships will likely become a key pursuit in understanding brain function.

Our current results extend the concept of a default mode (3, 28) or resting-state functionality of the brain by demonstrating a dynamic interplay within and between large, spatially distributed systems representing opposing components of our mental lives. The fact that task-evoked neuronal responses and, likely, behavioral phenomena mimic or reflect this underlying intrinsic organization encourages shifting one’s perspective of brain function from the view of a system simply responding to changing contingencies to one operating on its own, intrinsically, with sensory information modulating rather than determining the operation of the system. This view has both historical (46) and recent experimental support (22, 47, 48) and suggests a unique approach to understanding brain function.

Note Added in Proof. During preparation of this article a relevant article (50) became available noting the presence of anticorrelations between a seed region in the posterior cingulate precuneus and many of our currently defined task-positive regions, thus providing additional support for the current results.

We thank Linda Larson-Prior and John Zempel for help with data acquisition and Mike Posner, Michael Greicius, and Gyorgy Buzsaki for insightful comments and suggestions. This work was supported by National Institutes of Health Grant NS 06833.

##### NEUROSCIENCE

- 1. Cabeza, R. & Nyberg, L. (2000) J. Cognit. Neurosci. 12, 1–47.
- 2. Corbetta, M. & Shulman, G. L. (2002) Nat. Rev. Neurosci. 3, 201–215.
- 3. Gusnard, D. A. & Raichle, M. E. (2001) Nat. Rev. Neurosci. 2, 685–694.
- 4. Simpson, J. R. J., Snyder, A. Z., Gusnard, D. A. & Raichle, M. E. (2001) Proc. Natl. Acad. Sci. USA 98, 683–687.
- 5. Shulman, G. L., Fiez, J. A., Corbetta, M., Buckner, R. L., Miezin, F. M., Raichle, M. E. & Petersen, S. E. (1997) J. Cognit. Neurosci. 9, 648–663.
- 6. McKiernan, K. A., Kaufman, J. N., Kucera-Thompson, J. & Binder, J. R. (2003) J. Cognit. Neurosci. 15, 394–408.

- 7. Mazoyer, B., Zago, L., Mellet, E., Bricogne, S., Etard, O., Houde, O., Crivello, F., Joliot, M., Petit, L. & Tzourio-Mazoyer, N. (2001) Brain Res. Bull. 54, 287–298.
- 8. Wojciulik, E. & Kanwisher, N. (1999) Neuron 23, 747–764.
- 9. Corbetta, M., Kincade, J. M. & Shulman, G. I. (2002) J. Cognit. Neurosci. 14, 508–523.
- 10. Maddock, R. J. (1999) Trends Neurosci. 22, 310–316.
- 11. Gusnard, D. A., Akbudak, E., Shulman, G. L. & Raichle, M. E. (2001) Proc. Natl. Acad. Sci. USA 98, 4259–4264.

[Figure 9]

- 12. Shannon, B. & Buckner, R. L. (2004) J. Neurosci. 24, 10084–10092.
- 13. McGuire, P. K., Paulesu, E., Frackowiak, R. S. J. & Frith, C. D. (1996) NeuroReport 7, 2095–2099.
- 14. Cordes, D., Haughton, V. M., Arfanakis, K., Wendt, G. J., Turski, P. A., Moritz, C. H., Quigley, M. A. & Meyerand, M. E. (2001) Am. J. Neuroradiol. 22, 1326–1333.
- 15. Biswal, B., Yetkin, F., Haughton, V. & Hyde, J. (1995) Magn. Reson. Med. 34, 537–541.
- 16. Greicius, M. D., Krasnow, B., Reiss, A. L. & Menon, V. (2003) Proc. Natl. Acad. Sci. USA 100, 253–258.
- 17. Hampson, M., Peterson, B. S., Skudlarski, P., Gatenby, J. C. & Gore, J. C.

(2002) Hum. Brain Mapp. 15, 247–262.

- 18. Lowe, M. J., Mock, B. J. & Sorenson, J. A. (1998) NeuroImage 7, 119–132.
- 19. Van de Ven, V. G., Formisano, E., Prvulovic, D., Roeder, C. H. & Linden, D. E. J. (2004) Hum. Brain Mapp. 22, 165–178.
- 20. Laufs, H., Krakow, K., Sterzer, P., Egger, E., Beyerle, A., Salek-Haddadi, A. & Kleinschmidt, A. (2003) Proc. Natl. Acad. Sci. USA 100, 11053–11058.
- 21. Greicius, M. D. & Menon, V. (2004) J. Cognit. Neurosci. 16, 1484–1492.
- 22. Kenet, T., Bibitchkov, D., Tsodyks, M., Grinvald, A. & Arieli, A. (2003) Nature 425, 954–956.
- 23. Ojemann, J. G., Akbudak, E., Snyder, A. Z., McKinstry, R. C., Raichle, M. E. & Conturo, T. E. (1997) NeuroImage 6, 156–167.
- 24. Talairach, J. & Tournoux, P. (1988) Co-Planar Stereotaxic Atlas of the Human Brain (Thieme Medical Publishers, New York).
- 25. Jenkins, G. M. & Watts, D. G. (1968) Spectral Analysis and Its Applications (Holden-Day, San Francisco).
- 26. Kerr, D. L., Gusnard, D. A., Snyder, A. Z. & Raichle, M. E. (2004) NeuroReport 15, 607–610.
- 27. Duncan, J. & Owen, A. M. (2000) Trends Neurosci. 23, 475–483.
- 28. Raichle, M. E., MacLeod, A. M., Snyder, A. Z., Powers, W. J., Gusnard, D. A. & Shulman, G. L. (2001) Proc. Natl. Acad. Sci. USA 98, 676–682.
- 29. Arfanakis, K., Cordes, D., Haughton, V. M., Moritz, C. H., Quigley, M. A. & Meyerand, M. E. (2000) Magn. Reson. Imaging 18, 921–930.
- 30. Cordes, D., Haughton, V. M., Arfanakis, K., Wendt, G. J., Turski, P. A., Moritz, C. H., Quigley, M. A. & Meyerand, M. E. (2000) Am. J. Neuroradiol. 21, 1636–1644.

- 31. Kiviniemi, V., Kantola, J. H., Jauhiainen, J., Hyvarinen, A. & Tervonen, O.

(2003) NeuroImage 19, 253–260.

- 32. Grinvald, A., Arieli, A., Tsodyks, M. & Kenet, T. (2003) Biopolymers 68,

- 422–436.

33. Leopold, D. A., Murayama, Y. & Logothetis, N. K. (2003) Cerebral Cortex 13,

- 423–433.

- 34. Buzsaki, G. & Draguhn, A. (2004) Science 304, 1926–1929.
- 35. Engel, A. K., Fries, P. & Singer, W. (2001) Nat. Rev. Neurosci. 2, 704–716.
- 36. Varella, F., Lachaux, J.-P., Rodriguez, E. & Martinerie, J. (2001) Nat. Rev. Neurosci. 2, 229–239.
- 37. Bruns, A., Eckhorn, R., Jokeit, H. & Ebner, A. (2000) NeuroReport 11, 1509–1514.
- 38. Waites, A. B., Stanislavsky, A., Abbott, D. F. & Jackson, G. D. (2005) Hum. Brain Mapp. 24, 59–68.
- 39. Greene, J. D., Sommerville, R. B., Nystrom, L. E., Darley, J. M. & Cohen, J. D.

(2001) Science 293, 2105–2108.

- 40. Simpson, J. R. J., Drevets, W. C., Snyder, A. Z., Gusnard, D. A. & Raichle, M. E. (2001) Proc. Natl. Acad. Sci. USA 98, 688–691.
- 41. Clark, D. M. & Fairburn, C. G. (1997) Science and Practice of Cognitive Behavioral Therapy (Oxford Univ. Press, Oxford), pp. 27–46.
- 42. Giambra, L. M. (1995) Consciousness Cognit. 4, 1–21.
- 43. Teasdale, J. D., Dritschel, B. H., Taylor, M. J., Proctor, L., Lloyd, C. A., Nimmo-Smith, I. & Baddeley, A. D. (1995) Memory Cognit. 23, 551– 559.
- 44. Antrobus, J. S. & Singer, J. L. (1970) Trans. N.Y. Acad. Sci. 32, 242–252.
- 45. Shallice, T. (1988) From Neuropsychology to Mental Structure (Cambridge Univ. Press, Cambridge, U.K.).
- 46. Llinas, R. (1988) Science 242, 1654–1664.
- 47. Fiser, J., Chiu, C. & Weliky, M. (2004) Nature 431, 573–578.
- 48. Arieli, A., Sterkin, A., Grinvald, A. & Aertsent, A. (1996) Science 273, 1868–1871.
- 49. Van Essen, D. C. (2005) NeuroImage, in press.
- 50. Fransson, P. (2005) Hum. Brain Mapp., in press.

