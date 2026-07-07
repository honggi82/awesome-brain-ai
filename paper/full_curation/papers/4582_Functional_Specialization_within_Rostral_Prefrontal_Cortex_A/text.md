# Functional Specialization within Rostral Prefrontal Cortex (Area 10): A Meta-analysis

## Sam J. Gilbert1, Stephanie Spengler1, Jon S. Simons1, J. Douglas Steele2, Stephen M. Lawrie3, Christopher D. Frith1, and Paul W. Burgess1

Abstract

& One of the least well understood regions of the human brain is rostral prefrontal cortex, approximating Brodmann’s area 10. Here, we investigate the possibility that there are functional subdivisions within this region by conducting a meta-analysis of 104 functional neuroimaging studies (using positron emission tomography/functional magnetic resonance imaging). Studies involving working memory and episodic memory retrieval were disproportionately associated with lateral activations, whereas studies involving mentalizing (i.e., attending to one’s own emotions and mental states or those of other agents) were disproportionately associated with me-

dial activations. Functional variation was also observed along a rostral–caudal axis, with studies involving mentalizing yielding relatively caudal activations and studies involving multipletask coordination yielding relatively rostral activations. A classification algorithm was trained to predict the task, given the coordinates of each activation peak. Performance was well above chance levels (74% for the three most common tasks; 45% across all eight tasks investigated) and generalized to data not included in the training set. These results point to considerable functional segregation within rostral prefrontal cortex. &

### INTRODUCTION

Rostral prefrontal cortex (PFC), approximating Brodmann’s area (BA) 10, is probably the single largest cytoarchitectonic area of human PFC (Ramnani & Owen, 2004; Ongur, Ferry, & Price, 2003). This region has undergone great evolutionary expansion, doubling in relative size in the human compared with the chimpanzee brain (Semendeferi, Armstrong, Scheleicher, Ziles, & von Hoesen, 2001), suggesting that it plays an important role in human cognition. However, the functions of rostral PFC are not currently well understood despite a rapid acceleration in research into this region over the past few years (e.g., Burgess, Gilbert, Okuda, & Simons, in press; Gilbert, Simons, Frith, & Burgess, 2006; Burgess, Simons, Dumontheil, & Gilbert, 2005; Gilbert, Frith, & Burgess, 2005; Simons, Gilbert, Owen, Fletcher, & Burgess, 2005; Simons, Owen, Fletcher, & Burgess, 2005; Pollmann, 2004; Ramnani & Owen, 2004; Burgess, Scott, & Frith, 2003; Okuda et al., 2003; Braver & Bongiolatti, 2002; Janata et al., 2002; Burgess, Quayle, & Frith, 2001; Gusnard, Akbudak, Shulman, & Raichle, 2001; Christoff & Gabrieli, 2000; Craik et al., 1999; Koechlin, Basso, Pietrini, Panzer, & Grafman, 1999).

1University College London, UK, 2University of Aberdeen, UK, University of Edinburgh, UK

One important question is whether rostral PFC is a functionally homogenous region or whether it may be subdivided into functionally distinct subregions. If such functional subdivisions exist, this may help to resolve the debate between supporters of theoretical accounts that ascribe different roles to rostral PFC. For example, in a recent review, Ramnani and Owen (2004) point to five theoretical accounts that have been put forward to describe the functions of this region (‘‘processing of internal states,’’ ‘‘memory retrieval models,’’ ‘‘prospective memory,’’ ‘‘branching and reallocation of attention,’’ ‘‘relational integration’’) as well as suggesting an additional account of their own (‘‘integrating the outcomes of two or more separate cognitive operations’’). However, their review discussed rostral PFC as a functionally homogenous region and sought to provide a single account that could ‘‘accommodate the range of tasks that reliably recruit [rostral PFC]’’ (p. 185). Here, we investigate the possibility that different subregions of rostral PFC may support different processes, perhaps corresponding to these various accounts.

Most of the evidence relevant to the question of functional specialization within rostral PFC has come from functional neuroimaging studies using positron emission tomography (PET) and functional magnetic resonance imaging (fMRI). Other techniques (e.g., EEG, neuropsychological investigations) may lack the

D 2006 Massachusetts Institute of Technology Journal of Cognitive Neuroscience 18:6, pp. 932–948

spatial resolution to distinguish subregions of rostral PFC and have less often been used to investigate the functions of this region (although see Burgess, Gilbert, et al., in press; Burgess, 2000, for discussion of neuropsychological evidence on the functions of rostral PFC). In the present article, we therefore undertake a metaanalysis of functional neuroimaging studies using PET and fMRI in order to assess the evidence for functional segregation within rostral PFC.

Previous meta-analyses investigating other PFC regions have produced mixed evidence for functional specialization within human PFC. For example, Duncan and Owen (2000) found that functional neuroimaging studies investigating a variety of cognitive domains provoked activations in dorsolateral PFC and anterior cingulate cortex, but the location of these activations did not differ reliably according to the domain. Consequently, Duncan (2001) proposed an ‘‘adaptive coding’’ model of neural function in the PFC, according to which certain PFC regions are able to adapt their functions to support a wide variety of tasks rather than being tied to any one domain (see also Duncan, 2005). However, Duncan and Owen also found that rostral PFC was functionally dissociable from more caudal regions, because studies involving episodic memory were disproportionately associated with activations in this area. This raises the possibility that functional specialization may be particularly apparent within more rostral PFC regions.

One possible axis of functional specialization is between lateral and medial regions. Some authors have emphasized the role of rostral PFC in tasks requiring high-level guidance of behavior based on abstract information, for example, those involving problem solving (Christoff, Prabhakaran, et al., 2001), maintaining intentions over a delay (Burgess, Scott, et al., 2003; Burgess, Quayle, et al., 2001), coordinating goals and subgoals (Ramnani & Owen, 2004; Braver & Bongiolatti, 2002; Koechlin, Basso, et al., 1999), and basing responses on information recalled from episodic memory (Koechlin, Ody, & Kouneiher, 2003). Such studies have focused particularly on lateral regions of rostral PFC. Other studies have focused on tasks involving reflection on one’s own emotions and mental states (e.g., Johnson et al., 2002; Kelley et al., 2002; Gusnard et al., 2001; Damasio et al., 2000; Craik et al., 1999; Lane, Fink, Chau, & Dolan, 1997) or on the emotions and mental states of other agents (i.e., ‘‘mentalizing’’; Frith & Frith, 2003). These studies have typically focused on medial regions of rostral PFC. Thus, one aim of the present study is to investigate formally whether a distinction may be drawn between high-level cognitive tasks, which may be more likely to lead to activation in lateral rostral PFC, and tasks involving reflection on one’s own emotions and mental states, and the emotions and mental states of others, which may be more likely to lead to activation in medial rostral PFC.

A further aim is to investigate whether evidence can be found for functional specialization along a rostral– caudal axis within BA 10. The importance of this axis for the functional organization of human PFC has been emphasized for both medial and lateral aspects. For example, on the medial wall, Bush, Luu, and Posner (2000) suggest that a distinction may be made between caudal and rostral anterior cingulate cortex, involved in ‘‘cognitive’’ and ‘‘affective’’ functions, respectively (see also Steele & Lawrie, 2004). Koechlin, Ody, & Kouneiher (2003) suggest that the lateral PFC is hierarchically organized, with more anterior regions representing more abstract types of information (see also Kringelbach & Rolls, 2004). However, these studies have included regions posterior to BA 10, so it is not known whether similar variation between rostral and caudal areas may be found within BA 10 itself. A suggestion that such a distinction may be found comes from the literature on mentalizing, which has often emphasized the importance of the ‘‘paracingulate’’ cortex, near BA 10’s border with BA 32 (Frith & Frith, 1999, 2003). This suggests that relatively posterior regions of BA 10 may be involved in mentalizing, compared with other processes supported by this region.

### METHODS

Studies were identified by searches of the PubMed and ScienceDirect databases for articles that included either the word ‘‘PET’’ or ‘‘fMRI’’ along with at least one of the following phrases: ‘‘anterior prefrontal,’’ ‘‘medial prefrontal,’’ ‘‘rostral prefrontal,’’ ‘‘Brodmann’s area 10,’’ ‘‘BA 10,’’ ‘‘frontal pole,’’ ‘‘frontopolar,’’ ‘‘frontomedian,’’ ‘‘middle frontal gyrus,’’ ‘‘superior frontal gyrus.’’ In addition, reference lists of several review articles were inspected for further relevant studies (Ochsner et al., 2004; Ramnani & Owen, 2004; Wager, Jonides, & Reading, 2004; Fink, 2003; Gallagher & Frith, 2003; Friederici, 2002; Lee, Robbins, Graham, & Owen, 2002; Fletcher & Henson, 2001; Cabeza & Nyberg, 2000; Christoff & Gabrieli, 2000; MacLeod, Buckner, Miezin, Petersen, & Raichle, 1998; Nolde, Johnson, & Raye, 1998), and we included three recent studies from our own laboratory (Gilbert, Frith, et al., 2005; Simons, Gilbert, et al., 2005; Simons, Owen, et al., 2005). All relevant studies from these review articles were included, regardless of publication date. However, because the comprehensive review of neuroimaging studies conducted by Cabeza and Nyberg (2000) included studies published up to January 1999, our own literature search for additional studies was restricted to the period of January 1999 to October 2004.

Studies were included only if (1) they investigated unmedicated healthy young adults, (2) they reported the coordinates of activations in the space of the MNI template brain (Collins, Neelin, Peters, & Evans, 1994) or

according to the atlas of Talairach and Tournoux (1988), and (3) they reported one or more activations with peak coordinates falling within BA 10, according to the atlas of Talairach and Tournoux or as defined by the Brodmann map in MNI space supplied with MRIcro (Rorden & Brett, 2000). In addition, the meta-analysis was restricted to contrasts involving a comparison between two behavioral tasks, where reaction times (RTs) were available for each, in order to permit an analysis of RT effects. However, because this study focuses on variation in the location of rostral PFC activation peaks according to functional domain, consideration of accompanying behavioral effects is outside the scope of the present article (see Gilbert, Spengler, Simons, Frith & Burgess, in press, for discussion of RT effects). When activations were reported in Talairach and Tournoux coordinates, they were transformed into MNI space using a nonlinear transformation (www.mrc-cbu.cam.ac.uk/ Imaging; Brett, Christoff, Cusack, & Lancaster, 2001) so that all coordinates were in a common stereotaxic framework.

Activations were accepted as significant according to the criteria set by each individual study, although z values representing the level of significance for each contrast were noted when they were available. Other measures of significance (e.g., t or F values) were converted to z values via associated p values. Both ‘‘activations’’ (i.e., greater blood oxygen level dependent [BOLD] signal or regional cerebral blood flow [rCBF] in a task of interest than a control task) and ‘‘deactivations’’ (i.e., greater BOLD signal or rCBF in a control task) were included. In other words, any change in BOLD signal or rCBF was taken as potentially noteworthy, regardless of whether activity was greater in a task of interest than a control task, or vice versa.

Each activation peak was classified as lateral or medial by calculating whether the x coordinate was closer to the midpoint or lateral edge of the MNI template brain (Collins et al., 1994), given the y and z coordinates (where x defines a left–right axis, y defines a rostral– caudal axis, and z defines a superior–inferior axis). If a contrast yielded more than one activation peak falling within BA 10, only the most statistically significant was retained in the meta-analysis to ensure that the activation peaks entered into the analysis resulted from independent contrasts. If multiple conditions were compared against a common baseline (or, conversely, if one condition was compared against multiple control conditions), only the contrast producing the most significant activation was included in the analysis. When the same region was reported to be activated in two or more independent contrasts, using a conjunction analysis (Friston, Penny, & Glaser, 2005; Nichols, Brett, Anderson, Wager, & Poline, 2005; Price & Friston, 1997), the activation peak was entered into the metaanalysis more than once, corresponding to each contrast included in the conjunction analysis.

Each study was categorized by two raters (SJG and SS) in the following respects:

. Verbal/Nonverbal. Studies were classified as verbal if they included contrasts between tasks using linguistic materials.

. Emotional/Nonemotional. Studies were classified as emotional if they involved any emotional materials, that is, any materials that would typically be classified as positively or negatively valenced (e.g., photographs from the International Affective Pictorial System; Lang, Bradley, & Cuthbert, 1997).

. Task. Each study in the meta-analysis was placed into one of the following categories, depending on the task involved: Attention, Perception, Language, Working Memory, Episodic Retrieval, Other Memory, Mentalizing, Multitask. The first six of these categories were based on the categorization adopted by Cabeza and Nyberg (2000), with the modification that Cabeza and Nyberg’s categories of ‘‘priming,’’ ‘‘procedural memory,’’ and ‘‘semantic memory’’ were combined into a single Other Memory category, because there were few studies in each of these three categories. There was an Episodic Retrieval category but not an Episodic Encoding category because, although previous studies have reported rostral PFC activation associated with episodic memory encoding (e.g., Fletcher, Shallice, & Dolan, 1998), none matched the present inclusion criteria. The final two categories in this meta-analysis were additions to the categories proposed by Cabeza and Nyberg. The Mentalizing category encompassed studies involving reflection on one’s own emotions and mental states, or those of other agents. The Multitask category encompassed all studies that involved the performance of more than one task within any given block of trials (e.g., task switching, prospective memory, ‘‘branching,’’ ‘‘goal–subgoal integration’’). These latter two categories were specified because much recent research has suggested the involvement of BA 10 in tasks requiring mentalizing (see Ochsner et al., 2004; Frith & Frith, 2003, for reviews) or the coordination of multiple tasks (see Ramnani & Owen, 2004, for a review).

Because some statistical tests involved relatively small samples, all p values for chi-square tests were calculated using exact tests implemented in SPSS Exact Tests 7.0 for Windows (Mehta & Patel, 1996). These tests are reliable even when sample sizes are small (e.g., when there are cells with expected counts below 5).

### RESULTS

One hundred four studies were identified, yielding 133 independent contrasts. Interrater reliability was 99% for the verbal/nonverbal categorization, 94% for the

934 Journal of Cognitive Neuroscience Volume 18, Number 6

emotional/nonemotional categorization, and 94% for the task categorization. All disagreements between raters were resolved by discussion. Seven of the contrasts reflected greater rCBF or BOLD signal in a control or ‘‘baseline’’ task than a task of experimental interest. All conclusions below were similar, regardless of whether these ‘‘deactivations’’ were included or excluded from the analyses. We therefore present results below from all 133 contrasts, and use the term ‘‘activation’’ to refer to any significant change in rCBF or BOLD signal between two conditions.

A list of all contrasts included in the meta-analysis is presented in Table 1, and a breakdown of results by task is presented in Tables 2 and 3. The significance level (i.e., z values) of neuroimaging results did not differ according to task category (F < 1), suggesting that statistical thresholds did not differ systematically between studies investigating different categories of task. As Table 2 shows, the proportion of contrasts involving verbal versus nonverbal and emotional versus nonemotional materials differed widely between tasks. Studies in the Mentalizing category (compared with all other categories) and in the Multitask category (compared with all other categories) differed significantly in the proportion of contrasts involving emotional materials (x2 > 7.2; df = 1; p < .01). Similar differences in the proportion of contrasts involving verbal materials were observed in the Attention, Perception, Other Memory, and Mentalizing categories. Thus, in the analyses below, where an effect of a particular task on the location of BA 10 activations could also be explained by the type of materials used (e.g., if there were similar significant effects of a comparison between emotional and nonemotional materials, and also between Mentalizing and non-Mentalizing tasks), follow-up analyses were conducted to investigate whether these effects could be disentangled.

Hemispheric Asymmetry

First we investigated the evidence for differences between contrasts activating left versus right BA 10. In these analyses, all contrasts yielding activation peaks at x = 0 (n = 9) were excluded. There was no significant effect of whether the study involved verbal materials (verbal materials: 43 out of 80 activations [54%] in the left hemisphere; nonverbal materials: 25 out of 44 activations [57%] in the left hemisphere; x2 = .03; df = 1; p = .88); nor was there a significant effect of whether the contrast involved emotional materials (emotional materials: 20 out of 30 activations [67%] in the left hemisphere; nonemotional materials: 48 out of 94 activations [51%] in the left hemisphere; x2 = 2.2; df = 1; p = .15). There was a marginally significant effect of task category on the proportion of left- versus right-hemisphere activations (see Table 3 for results; x2 = 13.5, df = 7; p = .06). However, none of the individual task categories, com-

pared against the other studies included in the metaanalysis, differed significantly in the proportion of leftversus right-hemisphere activations (x2 < 4.1; df = 1; p > .05). Thus, there was no clear evidence for functional differences between left and right BA 10.

Medial versus Lateral BA 10

Next we investigated the evidence for differences between contrasts yielding activations in lateral versus medial BA 10. The analyses below investigated the number of activations classified as lateral versus medial. However, all results were similar if absolute x coordinate (i.e., x coordinate regardless of hemisphere) was used as the dependent measure instead. There was no significant effect of whether the study involved verbal materials (verbal materials: 50 out of 86 activations [58%] in lateral BA 10; nonverbal materials: 26 out of 47 activations (55%) in lateral BA 10; x2 = 0.01; df = 1; p = .86). By contrast, there was a highly significant effect of whether the study involved emotional materials (emotional materials: 6 out of 32 activations (19%) in lateral BA 10; nonemotional materials: 70 out of 101 activations (69%) in lateral BA 10; x2 = 25.4; df = 1; p < 10 7). Furthermore, there was a highly significant effect of task category on the proportion of lateral versus medial activations (see Table 3 and Figure 1 for results: x2 = 40.5; df = 7; p < .00001). Considering each category separately, there were significant effects of membership of the categories of Working Memory (x2 =5.4; df = 1; p < .05) and Episodic Retrieval (x2 = 15.8; df = 1; p < .0005), both of which were associated with a higher proportion of lateral activations. In addition there was a highly significant effect of membership of the mentalizing category, which was associated with a higher proportion of medial activations (x2 = 27.4; df = 1; p < 10 7).

Because there was a strong (but not perfect) overlap between contrasts in the Mentalizing category and contrasts involving emotional materials, both of which were associated with an increased proportion of activations in medial BA 10, we further investigated the contributions of these two factors. Figure 2 illustrates the percentage of activations in medial versus lateral BA 10 according to whether the contrast involved Mentalizing, emotional materials, both, or neither. When the contrast involved emotional materials but not a mentalizing task, or involved a mentalizing task but not emotional materials, the proportion of activations in medial versus lateral BA 10 was not significantly different from the proportion observed when the contrast involved neither emotional materials nor a Mentalizing task (x2 < .91; df = 1; p > .57). Conversely, contrasts involving both emotional materials and a Mentalizing task were associated with a significantly greater proportion of activations in medial BA 10 than contrasts involving one or the other of these factors, but not both (x2 > 13.4; df = 1; p = .005). Thus, it appears that activations in medial BA 10 were associ-

936JournalofCognitiveNeuroscienceVolume18,Number6

Study Task Emotional Materials Verbal Materials Coordinate Medial/Lateral Z Value

Table 1. Contrasts Included in the Meta-analysis Study Task Emotional Materials Verbal Materials Coordinate Medial/Lateral z Value

Badgaiyan, R. D., et al. (2001). Neuroimage, 13, 272–282 Other Memory X 8 51 3a M 6.62 Badre, D., & Wagner, A. D. (2004). Neuron, 41, 473–487 Multitask X 33 54 3 L 2.08 Bernard, F. A., et al. (2004). Neuroimage, 22, 1704–1714 Other Memory 6 62 8 M 4.17 Brass, M., et al. (2001). Neuroimage, 14, 1416–1423 Attention 6 60 21 M 3.95 Brass, M., et al. (2005). Neuropsychologia, 43, 89–98 Attention 1 51 12 M 4.04 Braver, T. S., et al. (2001). Neuroimage, 14, 48–59 Working Memory X 37 49 19 L –

X 20 55 13 L – Buckner, R. L., et al. (1995). Journal of Neuroscience, 15, 12–29 Episodic Retrieval X 35 62 10 L – Buckner, R. L., et al. (1998). Neuroimage, 7, 151–162 Episodic Retrieval X 34 61 6 L – Bunge, S. A., et al. (2004). Brain and Cognition, 56, 141–152 Episodic Retrieval 12 51 3 M 3.48 Burgess, P. W., et al. (2001). Neuropsychologia, 39, 545–555 Multitask X 40 51 3 L 4.36 Burgess, P. W., et al. (2003). Neuropsychologia, 41, 906–918 Multitask X 2 63 27a M 5.24

X 30 65 27 L 2.83

- Cabeza, R., et al. (2002). Neuroimage, 16, 317–330 Episodic Retrieval X 21 60 11 L 4.44
- Cabeza, R., et al. (2003). Neuropsychologia, 41, 390–399 Episodic Retrieval X 19 63 11 L 5.09 Chee, M. W., et al. (2004). Neuroimage, 22, 1456–1465 Episodic Retrieval X 41 47 12 L 3.63 Christoff, K., et al. (2001). Neuroimage, 14, 1136–1149 Working Memory 34 50 9 L 3.33 Christoff, K., et al. (2003). Behavioral Neuroscience, 117, 1161–1168 Working Memory 34 64 4 L 4.57 Collette, F., et al. (2001). Neuroimage, 14, 258–267 Attention X 38 66 2 L 3.42 Craik, F. I. M., et al. (1999). Psychological Science, 10, 26–34 Mentalizing X X 6 54 2 M 6.09 de Zubicaray, G. I., et al. (2000). Neuropsychologia, 38, 1292–1304 Attention X 0 49 6 M – Desmond, J. E., et al. (1998). Neuroimage, 7, 368–376 Language X 32 54 19 L – DiGirolamo, G. J., et al. (2001). NeuroReport, 12, 2065–2071 Multitask 20 70 4 L 3.04 Dobbins, I. G., et al. (2002). Neuron, 35, 989–996 Episodic Retrieval X 36 57 3 L 3.40

Dobbins, I. G., et al. (2004). Journal of Cognitive Neuroscience, 16, 908–920

Episodic Retrieval 39 53 3 L 4.58

Donaldson, D. I., et al. (2001). Neuron, 31, 1047–1059 Episodic Retrieval X 22 61 13 L 4.77

X 25 58 16 L 9.65 Dreher, J. C., et al. (2002). Neuroimage, 17, 95–109 Multitask X 0 64 8 M 4.45

X 36 60 4 L 7.17

Gilbertetal.937

Dreher, J. C., et al. (2003). Cerebral Cortex, 13, 329–339 Multitask X 8 56 28 M 6.71

X 28 60 4 L 5.40 Duzel, E., et al. (1999). Proceedings of the National Academy

Episodic Retrieval X 22 58 1 L 3.60

of Sciences, U.S.A., 96, 1794–1799

Elliott, R., et al. (1997). Neuropsychologia, 35, 1395–1404 Working Memory X X 6 53 16a M 6.63 Fan, J., et al. (2003). Neuroimage, 18, 42–57 Attention 12 64 12 M 2.36

34 54 10 L 3.63 X 26 56 2 L 2.72

- Fossati, P., et al. (2003). American Journal of Psychiatry, 160, 1938–1945

Mentalizing X X 11 50 18 M 4.24

- Fossati, P., et al. (2004). Neuroimage, 22, 1596–1604 Mentalizing X X 23 54 8 L 3.25 Ganis, G., et al. (2003). Cerebral Cortex, 13, 830–836 Mentalizing X 30 54 7 L 2.85

X 31 51 29 L 3.67 Gilbert, S. J., et al. (2005). European Journal of Neuroscience,

Multitask 0 64 26 M 3.41

21, 1423–1431

0 64 26 M 3.80 X 0 64 26 M 3.20

- 34 60 4 L 1.90
- 34 60 4 L 2.46

X 34 60 4 L 3.42 Goel, V., et al. (1997). NeuroReport, 8, 1305–1310 Working Memory X 36 53 12 L 3.88 Gorno-Tempini, M. L. (1998). Brain, 121, 2103–2118 Other Memory X 8 62 3 M 4.10 Greene, J. D., et al. (2001). Science, 293, 2105–2108 Mentalizing X X 1 52 17 M – Gusnard, D. A., et al. (2001). Proceedings of the National Academy

Mentalizing X 3 53 24 M 5.29

of Sciences, U.S.A., 98, 4259–4264

Harrington, D. L., et al. (2004). Cognitive Brain Research, 21, 193–205 Perception 32 56 12 L – Haxby, J. V., et al. (1996). Proceedings of the National Academy of

Episodic Retrieval 34 55 7 L 3.98

Sciences, U.S.A., 93, 922–927

Heekeren, H. R., et al. (2003). NeuroReport, 14, 1215–1219 Mentalizing X X 1 55 2 M –

- Henson, R. N., et al. (1999). Brain, 122, 1367–1381 Episodic Retrieval X 9 45 6a M 7.11
- Henson, R. N., et al. (2000). Neuropsychologia, 38, 426–440 Working Memory X 0 54 3a M 5.52

Henson, R. N., et al. (2000). Journal of Cognitive Neuroscience, 12, 913–923

Episodic Retrieval X 21 63 21 L 3.28

938JournalofCognitiveNeuroscienceVolume18,Number6

Table 1. (continued) Study Task Emotional Materials Verbal Materials Coordinate Medial/Lateral z Value Jansma, J. M., et al. (2001). Journal of Cognitive Neuroscience,

Working Memory X 38 59 10 L 3.88

13, 730–743

Jenkins, I. H., et al. (1994). Journal of Neuroscience, 14, 3775–3790 Other Memory 28 52 2 L 7.28 Johnson, S. C., et al. (2002). Brain, 125, 1808–1814 Mentalizing X X 0 54 8 M 5.30 Kelley, W. M., et al. (2002). Journal of Cognitive Neuroscience,

Mentalizing X X 10 52 2 M –

14, 785–794

Kircher, T. T., et al. (2000). Cognitive Brain Research, 10, 133–144. Mentalizing X 6 43 0 M – Klein, D., et al. (1995). Proceedings of the National Academy of

Language X 29 50 1 L 5.17

Sciences, U.S.A., 92, 2899–2903

- Koechlin, E., et al. (1999). Nature, 399, 148–151 Multitask X 30 75 12 L 7.60 X 36 66 21 L 7.27
- Koechlin, E., et al. (2000). Proceedings of the National Academy of Sciences, U.S.A., 97, 7651–7656

Multitask X 9 42 6 M 5.90

X 15 63 21 M 8.20 Konishi, S., et al. (2000). Neuroimage, 12, 276–286 Episodic Retrieval X 33 52 16 L 3.84 Konishi, S., et al. (2002). Journal of Neuroscience, 22, 9549–9555 Episodic Retrieval X 36 54 6 L 3.50 Koutstaal, W., et al. (2001). Neuropsychologia, 39, 184–199 Other Memory 25 60 19 L 5.55 Lee, A. C., et al. (2002). Neuroimage, 16, 724–735 Other Memory X 20 46 24 M 4.70 Lepsien, J., & Pollmann, S. (2002). Journal of Cognitive

Attention 26 54 8 L 4.72

Neuroscience, 14, 127–144

Leung, H. C., & Zhang, J. X. (2004). Neuroimage, 23, 1013–1019 Working Memory 32 55 13 L 2.78 Lieberman, M. D., et al. (2004). Journal of Personality of Social

Mentalizing X X 6 54 10 M 3.07

Psychology, 87, 421–435

Macaluso, E., et al. (2001). Experimental Brain Research, 137, 445–454

Attention 30 64 6 L 2.40

24 64 6 L 3.30 Macrae, C. N., et al. (2004). Cerebral Cortex, 14, 647–654 Mentalizing X X 9 50 0 M 2.04 Maguire, E. A., & Frith, C. D. (2003). Brain, 126, 1511–1523 Mentalizing X X 6 57 0 M 4.76

X X 3 54 0 M 5.58 Manoach, D. S., et al. (2004). Neuroimage, 21, 894–903 Working Memory 26 63 10 L 3.55

38 47 11 L 3.20

Gilbertetal.939

Maratos, E. J., et al. (2001). Neuropsychologia, 39, 910–920 Episodic Retrieval X X 36 58 18 L 3.43

McDermott, K. B., et al. (2000). Journal of Cognitive Neuroscience, 12, 965–976

X X 34 54 4 L – X X 34 54 4 L –

Episodic Retrieval X 35 52 7 L 2.72

X 37 54 14 L 3.08 Mitchell, J. P., et al. (2002). Proceedings of the National Academy

Mentalizing X X 0 54 21 M –

of Sciences, U.S.A., 99, 15238–15243

Muller, R. A., et al. (2002). Cognitive Brain Research, 14, 277–293 Other Memory 30 51 15 L 5.32 Nagahama, Y., et al. (1996). Brain, 119, 1667–1675 Working Memory 32 61 16 L 3.87 Nakamura, K., et al. (1998). NeuroReport, 9, 753–757 Perception X 4 70 1 M 3.40 Nakamura, K., et al. (2001). Neuropsychologia, 39, 1047–1054 Mentalizing X X 2 62 3 M 4.99 Ochsner, K. N., et al. (2004). Journal of Cognitive Neuroscience,

Mentalizing X 10 56 14 M 3.95

16, 1746–1772

Peyrin, C., et al. (2004). Neuroimage, 23, 698–707 Perception 8 51 3 M 3.77 Poldrack, R. A., et al. (1999). Neuroimage, 10, 15–35 Language X 10 52 7 M 2.94

Pollmann, S., et al. (2000). Journal of Cognitive Neuroscience, 12, 480–494

X 46 51 4 L 4.41 Language X 30 56 25a L 2.77

Attention 18 51 9 M 6.86

Ranganath, C., et al. (2000). Journal of Neuroscience, 20, RC108 (1–5). Episodic Retrieval 45 49 5 L 3.12 Ranganath, C., et al. (2004). Journal of Neuroscience, 24, 3917–3925 Episodic Retrieval 35 60 14 L 4.25 Reber, P. J., et al. (1998). Proceedings of the National Academy

Other Memory 16 63 28 L –

of Sciences, U.S.A., 95, 747–750

Reber, P. J., et al. (2002). Cognitive Brain Research, 14, 245–257 Other Memory 27 63 9 L – Rubia, K., et al. (2003). Neuroimage, 20, 351–358 Attention 0 58 19 M – Ruby, P., & Decety, J. (2004). Journal of Cognitive Neuroscience,

Mentalizing X X 4 54 22 M 3.79

16, 988–999

Rugg, M. D., et al. (1999). Neuroimage, 10, 520–529 Episodic Retrieval X 22 61 16 L 4.69

X 44 58 1 L 3.67 Rypma, B., et al. (1999). Neuroimage, 9, 216–226 Working Memory X 25 55 4 L 4.07 Saxe, R., & Kanwisher, N. (2003). Neuroimage, 19, 1835–1842 Mentalizing X X 6 57 18 M – Schmitz, T. W., et al. (2004). Neuroimage, 22, 941–947 Mentalizing X X 4 58 4 M 5.29

940JournalofCognitiveNeuroscienceVolume18,Number6

Table 1. (continued) Study Task Emotional Materials Verbal Materials Coordinate Medial/Lateral z Value

Seger, C. A., et al. (2004). Neuropsychologia, 42, 1168–1177 Mentalizing X X 2 54 22 M – Simons, J. S., et al. (2001). Journal of Cognitive Neuroscience,

Episodic Retrieval 40 45 2 L 3.75

13, 430–443

Simons, J. S., et al. (2003). Neuroimage, 19, 613–626 Other Memory X 30 60 0 L 4.05 Simons, J. S., et al. (2005). Neuropsychologia, 43, 1774–1783 Episodic Retrieval X 9 63 21 M 4.70

X 30 63 0 L 4.60 Simons, J. S., et al. (2005). Journal of Neurophysiology, 94, 813–820 Episodic Retrieval X 39 57 3 L 6.00

X 30 60 12 L 4.50 Small, D. M., et al. (2003). Neuroimage, 18, 633–641 Attention 9 66 6 M 3.40 Smith, A., et al. (2003). Neuroimage, 20, 344–350 Perception 14 55 12a M 5.48 Smith, A. P. R., et al. (2004). Neuroimage, 22, 868–878 Episodic Retrieval X 10 62 10 M 4.02

X 32 50 0 L 3.97 Sugiura, M., et al. (2000). Neuroimage, 11, 36–48 Mentalizing X 7 45 2 M 3.94 Sylvester, C. Y., et al. (2003). Neuropsychologia, 41, 357–370 Multitask 22 49 10 M 3.21 Taylor, S. F., et al. (1997). Neuroimage, 6, 81–92 Attention X 28 51 15 L 3.11

X X 24 64 8 L 4.01 Tillmann, B., et al. (2003). Cognitive Brain Research, 16, 145–161 Other Memory 8 64 5 M 2.9 Velanova, K., et al. (2003). Journal of Neuroscience, 23, 8460–8470 Episodic Retrieval X 35 52 11 L 3.82 Wagner, A. D., et al. (1998). NeuroReport, 9, 3711–3717 Episodic Retrieval X 12 58 1 M 2.77 Wallentin, M., et al. (2005). Brain Language, 92, 221–233 Language X 10 52 12 M 3.67 Weidner, R., et al. (2002). Cerebral Cortex, 12, 318–328 Attention 14 49 31 M 4.87 Weis, S., et al. (2004). Cerebral Cortex, 14, 256–267 Episodic Retrieval 37 65 15 L 4.02 Zhang, J. X., et al. (2003). Neuroimage, 20, 1531–1539. Working Memory X 33 49 28 L –

- Zysset, S., et al. (2001). Neuroimage, 13, 29–36 Attention X 31 54 19 L 8.67
- Zysset, S., et al. (2002). Neuroimage, 15, 983–991 Mentalizing X X 6 56 17 M 4.36 X X 6 56 17 M 4.37
- Zysset, S., et al. (2003). Neuroscience Letters, 335, 183–186 Mentalizing X X 5 49 16 M 5.42

An X in the relevant column indicates that the task involved emotional or verbal materials. All coordinates refer to the MNI template brain. aIndicates a ‘‘deactivation,’’ that is, greater BOLD signal rCBF in a control or baseline condition than a condition of interest.

Table 2. Breakdown of Studies and Contrasts Included in the Meta-analysis, According to Task

No. of Studies

No. of Contrasts

% Verbal

% Emotional

Task

Attention 13 17 35 6 Perception 4 4 0 25 Language 4 6 100 0 Working Memory 12 14 57 7 Episodic Retrieval 27 35 74 14 Other Memory 11 11 36 0 Mentalizing 23 26 85 92 Multitask 10 20 70 0 Overall 104 133 65 24

Table 3. Location of Activations, According to Task

Mean y (SD)

Mean z (SD)

Task % LH % Lateral

Attention 47 53 57.4 (6.3) 8.7 (10.6) Perception 75 25 58.0 (8.3) 6.5 (6.6) Language 33 67 52.5 (2.2) 7.0 (13.4) Working Memory 31 86 54.8 (5.3) 11.4 (7.6) Episodic Retrieval 69 86 56.4 (5.4) 7.5 (7.6) Other Memory 73 55 57.6 (6.3) 8.7 (11.4) Mentalizing 63 12 53.4 (3.9) 9.8 (9.9) Multitask 31 55 60.5 (7.4) 12.0 (12.0) Overall 55 57 56.4 (6.0) 9.2 (9.7)

LH = left hemisphere.

ated with tasks that involved both mentalizing and emotional materials. In accordance with this conclusion, when the absolute x coordinate of each activation peak was analyzed in an ANOVA with factors Mentalizing (Mentalizing/non-Mentalizing) and Emotion (emotional/ nonemotional materials), there was a significant interaction, F(1,129) = 5.8; p < .02). However, because there were only two contrasts involving Mentalizing but not emotional materials, it should be noted that this conclusion is based on a very limited number of observations.

y/z Coordinates

Having considered the evidence for functional differences between lateral and medial BA 10 (i.e., according to the x coordinate of the activation) we now turn to the evidence for functional specialization according to the y and z coordinates. There was no significant effect of

verbal versus nonverbal materials, emotional versus nonemotional materials, or task on the z coordinates of activation peaks (all Fs < 1). The y coordinates of activation peaks did not differ significantly according to whether the contrast involved verbal or nonverbal materials (F < 1), but there was a marginally significant effect of emotional versus nonemotional materials (emotional: mean y = 54.6; nonemotional; mean y = 56.9; F(1,131) = 3.6; p = .061). In addition, there was a significant effect of task on the y coordinates of activation peaks (see Table 3 and Figure 3), F(7,125) = 3.3; p < .005. Considering each task separately, there were significant effects of membership of the categories of Mentalizing [Mentalizing: mean y = 53.4; non-Mentalizing: mean y = 57.1; F(1,131) = 8.3, p < .005] and Multitask [Multitask: mean y = 60.5; non-Multitask: mean y = 55.6; F(1,131) = 12.1, p < .001]. Thus, contrasts involving Mentalizing yielded activations that were significantly

- Figure 1. Percentage of activations in medial versus lateral BA 10, plotted separately according to task. Horizontal line indicates mean across all contrasts. * indicates significant difference from mean of other categories ( p < .05).

|[Figure 1] A Meta-analysis_images/imageFile1.png>)|
|---|

|[Figure 2] A Meta-analysis_images/imageFile2.png>)|
|---|

- Figure 2. Percentage of activations in medial versus lateral BA 10 (and the number of contrasts on which this is based) according to whether the contrast involves emotional materials, a Mentalizing task, both, or neither.

caudal to contrasts involving other domains, and contrasts in the Multitask domain yielded activations that were significantly rostral to contrasts involving other domains. Even when contrasts in the Multitask domain were excluded from the analysis, contrasts in the mentalizing domain yielded activations that was significantly caudal to those from other domains, F(1,111) = 6.0, p < .02. Likewise, activations in the Multitask domain were significantly rostral to those in other domains, even after Mentalizing contrasts were excluded, F(1,105) = 7.9, p < .01. Activation peaks from these two domains are illustrated in Figure 4.

One possible explanation of the relatively caudal activation foci for the Mentalizing category might be that this category included a relatively high proportion of studies involving emotional materials. Alternatively,

the high proportion of medial activations in this category may have been responsible for the relatively caudal activation foci (i.e., for anatomical reasons). In order to investigate these possibilities, we subjected the y coordinates of activation peaks to a multiple regression analysis, with factors Mentalizing (Mentalizing/ non-Mentalizing), Emotion (emotional/nonemotional materials), and Region (medial/lateral). This analysis showed that even after accounting for variance attributable to Emotion and Region, there was still a significant effect of Mentalizing, t(128) = 2.1; p < .05. By contrast, the effects of Emotion and Region were not significant in this analysis, t(128) < .7; p > .5. Thus, the association between Mentalizing and the y coordinates of activation peaks could not be attributed to these other factors.

Predictive Validity of x and y Coordinates

The locations of activation peaks derived from different categories of task were most reliably distinguished according to two variables: absolute x coordinate (i.e., distance from midline, regardless of hemisphere) and y coordinate. In order to assess the predictive validity of these two variables, we built a classification algorithm that attempted to predict the category of task from the location of each activation peak. Separately for each task category, we constructed a probability density function (PDF) across the two-dimensional space spanned by |x| = 0–60 (i.e., the x coordinate, regardless of hemisphere) and y = 40–75, to represent the likelihood of observing an activation peak in each location. These PDFs were generated from two-dimensional Gaussian functions defined by the means and standard deviations of x and y coordinates in each category. Each PDF was scaled in proportion to the relative preponderance of each category of task in the sample, so that a PDF representing a relatively frequent category was given more weight than

Figure 3. Mean y coordinates of activations, plotted separately according to task. Horizontal line indicates mean across all contrasts.

* indicates significant difference from mean of other categories ( p < .05).

|[Figure 3] A Meta-analysis_images/imageFile3.png>)|
|---|

Figure 4. Location of activations in the Mentalizing and Multitask categories, plotted separately on axial (projected onto z = 0), coronal (projected onto y = 60), and sagittal (projected onto x = 0) slices of a structural scan (mean of 14 normalized T1-weighted images). Where more than one activation occupies the same location, the area of each blob is increased proportionately.

|[Figure 4] A Meta-analysis_images/imageFile4.png>)|
|---|

a PDF representing a relatively infrequent category (cf. Bayes’ rule). In order to make a prediction of the most likely task category for a particular x/y coordinate, the task category associated with the PDF that had the greatest height at that coordinate was picked. This procedure is illustrated in Figure 5.

When presented with the absolute x coordinate and y coordinate of each contrast included in the meta-

analysis, this classification algorithm correctly identified the task category on 45% of occasions, well above the success rate that would be expected if a random task category were chosen for each contrast (12.5%), or if Episodic Retrieval, the most numerous category, were chosen for every contrast (26%) (binomial tests: p < .000001).

More importantly, even when the classification algorithm was ‘‘trained’’ on data from just half of the con-

|[Figure 5] A Meta-analysis_images/imageFile5.png>)|
|---|

- Figure 5. Illustrative probability density functions (PDFs) from the Episodic Retrieval and Mentalizing categories. Each PDF was generated from a two-dimensional Gaussian distribution defined by the mean and standard deviation of the x and y coordinates of activation peaks in the relevant task category. Note that the PDFs are scaled according to the number of contrasts in each category, hence the greater peak height of the PDF representing Episodic Retrieval, even though the standard deviations in the mentalizing category were smaller. In order to predict the most likely task category for an activation peak with particular x and y coordinates, the category associated with the PDF with greatest height at that coordinate was picked. For example, given an x coordinate of 6 and y coordinate of 54 (taken from the study of Craik et al., 1999, and illustrated with a white circle on both PDFs), the Mentalizing category would be picked.

ns. Thus, taking account of the x and y coordinates of each activation peak in rostral PFC, but not the z coordinate, gave rise to a significantly increased chance of predicting the task category with which it was associated, and this predictive ability consistently generalized from one half of the data to the other.

|[Figure 6] A Meta-analysis_images/imageFile6.png>)|
|---|

Analysis of the classification algorithm’s output showed that in 92% of cases it picked one of the three most numerous categories in the meta-analysis: Episodic Retrieval, Mentalizing, and Multitask. Assignment of activation peaks into one of these three categories was dependent on the x and y coordinates; the way that the classification algorithm partitioned rostral PFC into these three categories is illustrated in Figure 6. It is clear from the figure that relatively rostral activations (both medial and lateral) were assigned to the Multitask category, whereas relatively caudal activations were assigned to the Mentalizing category if they were medial and the Episodic Retrieval category if they were lateral. When the classification algorithm was trained and tested on just those activations falling into these three categories, 74% were correctly classified, well above the level expected by chance (33%) or if Episodic Retrieval were chosen for every contrast (43%; p < 10 8). The corresponding figure, when the algorithm was trained on one half of the contrasts and tested on the other half, was 71%. The data from these final analyses are illustrated in Figure 7, which shows that the majority of predictions were correct in all three categories.

- Figure 6. Partitioning of rostral PFC according to a classification algorithm that predicted the task category from the absolute x coordinate and y coordinate of each activation peak. The algorithm predicted Episodic Retrieval, Mentalizing, or Multitask on 92% of occasions, so only these three categories are presented. Because the algorithm used the absolute x coordinate to make predictions, left- and right-hemisphere color overlays are mirror images of one another. Results are plotted on an axial slice of a normalized T1-weighted image (z = 0).
- Figure 7. Percentage of contrasts in the Episodic Retrieval, Mentalizing, and Multitask categories, presented separately according to the classification algorithm’s predicted category.

trasts, it was still able to predict the task category of the other contrasts that were not included in the training set. In these analyses, a randomly selected 50% of the contrasts in each category were used to generate the PDFs used by the classification algorithm. The algorithm was then tested on the remaining novel data. This procedure was repeated 50 times. Mean classification performance was 40% in these tests, still well above the highest score (26%) that could be achieved if x and y coordinates were not taken into account, t(49) = 24; p < 10 28. However, we found that additionally taking into account the z coordinates of activation peaks in order to generate three-dimensional PDFs did not lead to any significant further improvement in performance: two-dimensional PDFs: 40% correct; three-dimensional PDFs: 41% correct; t(98) = .65;

### DISCUSSION

A striking finding from the present meta-analysis is that activation in rostral PFC (approximating BA 10) has been reported in studies involving a wide variety of tasks. Thus, it appears that rostral PFC, considered as a whole, supports processes that are involved in many different situations, rather than being limited to a single domain

|[Figure 7] A Meta-analysis_images/imageFile7.png>)|
|---|

(e.g., episodic retrieval; see Duncan and Owen, 2000, for a similar result in other frontal lobe regions). However, the meta-analysis also provides clear evidence for functional specialization within rostral PFC. First, there was functional variation between lateral and medial subregions of BA 10. Contrasts in the Mentalizing category were more likely to be associated with activation in medial BA 10 than contrasts in other categories, provided that they also involved emotional materials. Conversely, contrasts in the Working Retrieval and Episodic Retrieval categories were associated with a greater proportion of lateral BA 10 activations than the other categories. In addition to this specialization along the lateral–medial dimension, functional specialization was also observed along the rostral–caudal dimension, with studies in the Mentalizing category being associated with relatively caudal activations, and studies in the Multitask category being associated with relatively rostral activations.

The association between medial activations and contrasts involving emotional materials (at least in Mentalizing tasks) is consistent with previous investigations suggesting that medial and lateral rostral prefrontal regions are preferentially involved in emotional and cognitive tasks, respectively. For example, in a metaanalysis of neuroimaging studies investigating emotion, Phan, Wager, Taylor, and Liberzon (2002) found that medial PFC (corresponding to BAs 9 and 10) was more commonly activated than lateral prefrontal regions, consistent with previous reports of strong interconnections between the limbic system and medial prefrontal regions (e.g., Porrino, Crane, & Goldman-Rakic, 1981). By contrast, Christoff and Gabrieli (2000), in a review of studies involving reasoning and episodic memory retrieval, reported activations within lateral BA 10. However, as far as we are aware, this is the first study to formally demonstrate the existence of variation between regions within rostral PFC activated by cognitive and emotional tasks. This finding extends the work of others revealing segregation between cognitive and emotional tasks along a rostral–caudal axis (Steele & Lawrie, 2004; Bush et al., 2000) by additionally revealing a specialization within rostral PFC according to a medial–lateral axis.

Perhaps more surprising than the variation between lateral and medial subregions of BA 10 was the variation between rostral and caudal subregions. Several authors have argued for functional differences between BA 10 and more posterior PFC regions (e.g., Ramnani & Owen, 2004; Christoff & Gabrieli, 2000; Koechlin, Basso, et al., 1999). However, the present results suggest that a distinction between rostral and caudal regions may be made even within BA 10, with relatively rostral regions supporting processes involved in coordinating performance of two or more tasks, and relatively caudal regions supporting processes involved in mentalizing.

The finding that studies in the Multitask category were associated with relatively rostral activation peaks would

be consistent with previous suggestions of a hierarchical organization of PFC regions, with more rostral regions supporting high-level guidance of task performance over extended periods of time, rather than being involved in the moment-by-moment processes required for task execution (Braver, Reynolds, & Donaldson, 2003; Koechlin, Ody, et al., 2003; Wood & Grafman, 2003; Koechlin, Basso, et al., 1999). The coordination of two or more tasks may provoke subjects to process high-level information about the various tasks being performed, over and above processing related to the individual tasks themselves, potentially accounting for the relatively rostral activation peaks in this category.

Interestingly, the activation peaks of studies involving Mentalizing were reliably caudal to those involving other tasks, as well as being predominantly located in medial BA 10. This region was generally not activated by contrasts involving emotional materials when the task did not involve Mentalizing; nor was it activated in the contrasts involving Mentalizing but not emotional materials. One possibility, therefore, is that this region plays a role in attending to one’s own emotional states, rather than representing the emotional states themselves (Ochsner et al., 2004; Frith & Frith, 2003; Gusnard et al., 2001; Damasio et al., 2000; Lane et al., 1997). This process may play a critical role not only in reflecting on one’s own emotional states, but also in ascribing mental states to other agents. For example, according to some theories, we ascribe mental states to others, at least in part, by using our own mental states as a model (e.g., Carruthers & Smith, 1996; Davies & Stone, 1995; Harris, 1992).

An important theme in research into functional subdivisions of PFC is the distinction between domain-specific and process-specific models. According to domain-specific models, functional subdivisions between different regions reflect the same fundamental process operating on different categories of information. Such models may be contrasted with process-specific models, according to which functional subdivisions between different regions reflect the operation of different processes, regardless of the type of information being processed. Christoff, Ream, Geddes, and Gabrieli (2003) have suggested a domainspecific model of functional subdivisions within BA 10, according to which BA 10 as a whole is specialized for the processing of self-generated information, but lateral and medial subregions are specialized for processing cognitive and emotional information, respectively. The present meta-analysis supports the suggestion that lateral and medial subregions of BA 10 may have a greater involvement in processing cognitive and emotional information, respectively, although the results suggested that neither subregion processes cognitive or emotional information exclusively. However, this distinction between contrasts involving emotional and nonemotional materials seemed to be task specific because it was only observed within the Mentalizing category. This finding suggests some degree

of process specificity. Furthermore, the suggestion by Christoff, Ream, et al. that all regions of BA 10 are specialized for the processing of self-generated information is hard to reconcile with the findings of Gilbert, Frith, et al. (2005) and Small et al. (2003). Both of these studies revealed activation in medial BA 10 associated with tasks involving attention toward perceptual information (see also Gilbert, Simons, et al., 2006; Janata et al., 2002, for further examples). These results are more consistent with a related model, proposed by Burgess, Gilbert, et al. (in press) and Burgess, Simons, et al. (2005; see also Gilbert, Simons, et al., 2006; Gilbert, Frith, et al. 2005; Simons, Gilbert, et al., 2005; Simons, Owen, et al., 2005), according to which medial BA 10 influences the attentional balance between self-generated and perceptual information, rather than being exclusively involved in processing self-generated information.

In addition to the suggestion of domain-specific segregation between subregions of BA 10 involved in processing emotional and cognitive information, the present results also point to the existence of process-specific distinctions between subregions of BA 10. For example, studies involving mentalizing were associated with more caudal activations than other studies, and studies involving coordination of two or more tasks were associated with more rostral activations than other studies. These findings suggest that different subregions of BA 10 may be distinguished not only in terms of their involvement in different domains (e.g., emotional vs. nonemotional materials) but also in terms of their role in different cognitive processes (e.g., those involved in mentalizing vs. those involved in multiple-task coordination). The observed degree of functional specialization was particularly remarkable given that tasks in the different categories will probably have relied on some shared cognitive processes. For example, the Multitask category included studies investigating prospective memory, which is likely to involve many cognitive processes, including episodic memory retrieval (e.g., Cohen, West, & Craik, 2001).

We note that the number of studies in each category is not necessarily informative as to the functions of rostral PFC (compared with other brain regions). For example, the preponderance of studies in the meta-analysis investigating episodic memory retrieval may simply reflect the large number of published studies that have investigated this process, rather than any specific link between studies in this category and the probability of observing activation in rostral PFC. Thus, the finding that studies in different categories were associated with activation peaks in different parts of rostral PFC is more theoretically important than the absolute numbers of activations in each category. Of course, owing to the inclusion criteria, some potentially relevant studies will undoubtedly have been excluded from the meta-analysis. However, this is unlikely to have led to any systematic bias in the location of BA 10 activations in different categories.

In summary, the present meta-analysis indicates that it may be oversimplistic to consider BA 10 a functionally homogenous region, and that its functions may vary according to both a lateral–medial and a rostral–caudal axis. Functional variation across these two axes was sufficiently consistent that knowledge of the absolute x coordinate (i.e., distance from midline) and y coordinate of the activation peaks permitted 40% of the contrasts to be correctly assigned to one of eight categories of task, and 71% of the contrasts from the three most numerous categories to be correctly classified, even when the classification algorithm was trained on one set of data and tested on another. We are not aware of any previous meta-analyses that have investigated the ability of such classification algorithms to describe their data. However, the relatively accurate classification performance in the present study suggests that similar algorithms may be useful in future meta-analyses of neuroimaging findings for investigating the reliability of regional specializations, and the ability to generalize from one data set to another. It is of course possible that future meta-analyses, including additional studies and adopting a more finegrained categorization of tasks, will reveal further functional subdivisions beyond those established here.

The present evidence for functional variation within BA 10 mirrors neurophysiological evidence for cytoarchitectonic differences both between lateral and medial subregions of rostral PFC (Petrides & Pandya, 1999) and between rostral and caudal subregions within rostral PFC (Carmichael & Price, 1994). However, the activation peaks from different types of study were extremely close to one another. For example, although studies involving mentalizing yielded activation peaks that were reliably caudal to those from other studies, the mean difference between the y coordinates in these two categories was only 4 mm and there was substantial overlap between the two distributions. This suggests that future studies investigating functional specialization within BA 10 will be most successful if they compare tasks that might recruit different subregions of BA 10 within a single study. Comparisons between experiments may be insensitive to functional variation unless a large number of studies are considered.

Acknowledgments

This work was supported by the Wellcome Trust (061171) and ESRC (PTA-026-27-0317).

Reprint requests should be sent to Sam Gilbert, Institute of Cognitive Neuroscience, 17 Queen Square, London WC1N 3AR, UK, or via e-mail: sam.gilbert@ucl.ac.uk.

### REFERENCES

Braver, T. S., & Bongiolatti, S. R. (2002). The role of frontopolar cortex in subgoal processing during working memory. Neuroimage, 15, 523–536.

Braver, T. S., Reynolds, J. R., & Donaldson, D. I. (2003). Neural mechanisms of transient and sustained cognitive control during task switching. Neuron, 39, 713–726. Brett, M., Christoff, K., Cusack, R., & Lancaster, J. (2001). Using the Talairach atlas with the MNI template. Neuroimage, 13, 85.

Burgess, P. W. (2000). Strategy application disorder: The role of the frontal lobes in human multitasking. Psychological Research, 63, 279–288.

Burgess, P. W., Gilbert, S. J., Okuda, J., & Simons, J. S. (in press). Rostral prefrontal brain regions (area 10). A gateway between inner thought and the external world? In W. Prinz & N. Sebanz (Eds.), Disorders of volition. Cambridge: MIT Press.

Burgess, P. W., Quayle, A., & Frith, C. D. (2001). Brain regions involved in prospective memory as determined by positron emission tomography. Neuropsychologia, 39, 545–555.

Burgess, P. W., Scott, S. K., & Frith, C. D. (2003). The role of the rostral frontal cortex (area 10) in prospective memory: A lateral versus medial dissociation. Neuropsychologia, 41, 906–918.

Burgess, P. W., Simons, J. S., Dumontheil, I., & Gilbert, S. J.

(2005). The gateway hypothesis of rostral prefrontal cortex (area 10) function. In J. Duncan, L. Phillips, & P. McLeod (Eds.), Measuring the mind: Speed, control, and age (pp. 217–248). Oxford: Oxford University Press.

Bush, G., Luu, P., & Posner, M. I. (2000). Cognitive and emotional influences in anterior cingulate cortex. Trends in Cognitive Sciences, 4, 215–222.

Cabeza, R., & Nyberg, L. (2000). Imaging cognition II: An empirical review of 275 PET and fMRI studies. Journal of Cognitive Neuroscience, 12, 1–47.

Carmichael, S. T., & Price, J. L. (1994). Architectonic subdivision of the orbital and medial prefrontal cortex in the macaque monkey. Journal of Comparative Neurology, 346, 366–402.

Carruthers, P., & Smith, P. K. (1996). Theories of theories of mind. Cambridge: Cambridge University Press.

Christoff, K., & Gabrieli, J. D. E. (2000). The frontopolar cortex and human cognition: Evidence for a rostrocaudal hierarchical organization within the human prefrontal cortex. Psychobiology, 28, 168–186.

Christoff, K., Prabhakaran, V., Dorfman, J., Zhao, Z., Kroger, J. K., Holyoak, K. J., & Gabrieli, J. D. (2001). Rostrolateral prefrontal cortex involvement in relational integration during reasoning. Neuroimage, 14, 1136–1149.

Christoff, K., Ream, J. M., Geddes, L. P., & Gabrieli, J. D. (2003). Evaluating self-generated information: Anterior prefrontal contributions to human cognition. Behavioral Neuroscience, 117, 1161–1168.

Cohen, A. L., West, R., & Craik, F. I. M. (2001). Modulation of the prospective and retrospective components of memory for intentions in younger and older adults. Aging, Neuropsychology and Cognition, 8, 1–13.

Collins, D. L., Neelin, P., Peters, T. M., & Evans, A. C. (1994). Automatic 3D intersubject registration of MR volumetric data in standardized Talairach space. Journal of Computer Assisted Tomography, 18, 192–205.

Craik, F. I. M., Moroz, T. M., Moscovitch, M., Stuss, D. T., Winocur, G., Tulving, E., & Kapur, S. (1999). In search of the self: A positron emission tomography study. Psychological Science, 10, 26–34.

Damasio, A. R., Grabowski, T. J., Bechara, A., Damasio, H., Ponto, L. L., Parvizi, J., & Hichwa, R. D. (2000). Subcortical and cortical brain activity during the feeling of self-generated emotions. Nature Neuroscience, 3, 1049–1056.

Davies, M., & Stone, T. (1995). Folk psychology: The theory of mind debate. Oxford: Blackwell.

Duncan, J. (2001). An adaptive coding model of neural function in prefrontal cortex. Nature Reviews Neuroscience, 2, 820–829.

Duncan, J. (2005). Prefrontal cortex and Spearman’s g. In J. Duncan, L. Phillips, & P. McLeod (Eds.), Measuring the mind: Speed, control, and age (pp. 249–272). Oxford: Oxford University Press.

Duncan, J., & Owen, A. M. (2000). Common regions of the human frontal lobe recruited by diverse cognitive demands. Trends in Neuroscience, 23, 475–483.

Fink, G. R. (2003). In search of one’s own past: The neural basis of autobiographical memories. Brain, 126, 1509–1510.

Fletcher, P. C., & Henson, R. N. A. (2001). Frontal lobes and human memory. Insights from functional neuroimaging. Brain, 124, 849–881.

Fletcher, P. C., Shallice, T., & Dolan, R. J. (1998). The functional roles of prefrontal cortex in episodic memory.

I. Encoding. Brain, 121, 1239–1248.

Friederici, A. D. (2002). Towards a neural basis of auditory sentence processing. Trends in Cognitive Sciences, 6, 78–84.

Friston, K. J., Penny, W. D., & Glaser, D. E. (2005).

Conjunction revisited. Neuroimage, 25, 661–667. Frith, C. D., & Frith, U. (1999). Interacting minds:

A biological basis. Science, 286, 1692–1695.

Frith, U., & Frith, C. D. (2003). Development and neurophysiology of mentalizing. Philosophical Transactions of the Royal Society of London, Series B, 358, 459–473.

Gallagher, H. L., & Frith, C. D. (2003). Functional imaging of ‘‘theory of mind.’’ Trends in Cognitive Sciences, 7, 77–83.

Gilbert, S. J., Frith, C. D., & Burgess, P. W. (2005). Involvement of rostral prefrontal cortex in selection between stimulus-oriented and stimulus-independent thought. European Journal of Neuroscience, 21, 1423–1431.

Gilbert, S. J., Simons, J. S., Frith, C. D., & Burgess, P. W.

(2006). Performance-related activity in rostral prefrontal cortex (area 10) during low-demand tasks. Journal of Experimental Psychology: Human Perception and Performance, 32, 45–58.

Gilbert, S. J., Spengler, S., Simons, J. S., Frith, C. D., & Burgess, P. W. (in press). Differential functions of lateral and medial rostral prefrontal cortex (area 10) revealed by brain-behavior associations. Cerebral Cortex.

Gusnard, D. A., Akbudak, E., Shulman, G. L., & Raichle, M. E. (2001). Medial prefrontal cortex and self-referential mental activity: Relation to a default mode of brain function. Proceedings of the National Academy of Sciences, U.S.A, 98, 4259–4264.

Harris, P. (1992). From simulation to folk psychology: The case for development. Mind and Language, 7, 120–144.

Janata, P., Birk, J. L., Van Horn, J. D., Leman, M., Tillmann, B., & Bharucha, J. J. (2002). The cortical topography of tonal structures underlying Western music. Science, 298, 2167–2170.

Johnson, S. C., Baxter, L. C., Wilder, L. S., Pipe, J. G., Heiserman, J. E., & Prigatano, G. P. (2002). Neural correlates of self-reflection. Brain, 125, 1808–1814.

Kelley, W. M., Macrae, C. N., Wyland, C. L., Caglar, S., Inati, S., & Heatherton, T. F. (2002). Finding the self? An event-related fMRI study. Journal of Cognitive Neuroscience, 14, 785–794.

Koechlin, E., Basso, G., Pietrini, P., Panzer, S., & Grafman, J.

(1999). The role of the anterior prefrontal cortex in human cognition. Nature, 399, 148–151.

Koechlin, E., Ody, C., & Kouneiher, F. (2003). The architecture of cognitive control in the human prefrontal cortex. Science, 302, 1181–1185.

Kringelbach, M. L., & Rolls, E. T. (2004). The functional neuroanatomy of the human orbitofrontal cortex: Evidence from neuroimaging and neuropsychology. Progress in Neurobiology, 72, 341–372.

Lane, R. D., Fink, G. R., Chau, P. M., & Dolan, R. J.

(1997). Neural activation during selective attention to subjective emotional responses. NeuroReport, 8, 3969–3972.

Lang, P. J., Bradley, M. M., & Cuthbert, B. N. (1997). The International Affective Picture System (IAPS): Photographic slides (1997). Gainesville, FL: University of Florida.

Lee, A. C., Robbins, T. W., Graham, K. S., & Owen, A. M.

(2002). ‘‘Pray or prey?’’ dissociation of semantic memory retrieval from episodic memory processes using positron emission tomography and a novel homophone task. Neuroimage, 16, 724–735.

MacLeod, A. K., Buckner, R. L., Miezin, F. M., Petersen, S. E., & Raichle, M. E. (1998). Right anterior prefrontal cortex activation during semantic monitoring and working memory. Neuroimage, 7, 41–48.

Mehta, C. R., & Patel, N. R. (1996). SPSS exact tests 7.0 for windows. Chicago, IL: SPSS Inc. Nichols, T., Brett, M., Andersson, J., Wager, T., & Poline, J.-B.

(2005). Valid conjunction inference with the minimum statistic. Neuroimage, 25, 653–660.

Nolde, S. F., Johnson, M. K., & Raye, C. L. (1998). The role of prefrontal cortex during tests of episodic memory. Trends in Cognitive Sciences, 2, 399–406.

Ochsner, K. N., Knierim, K., Ludlow, D. H., Hanelin, J., Ramachandran, T., Glover, G., & Mackey, S. C. (2004). Reflecting upon feelings: An fMRI study of neural systems supporting the attribution of emotion to self and other. Journal of Cognitive Neuroscience, 16, 1746–1772.

Okuda, J., Fujii, T., Ohtake, H., Tsukiura, T., Tanki, K., Suzuki, K., Kawashima, R., Fukuda, H., Itoh, M., & Yamadori, A. (2003). Thinking of the future and past: The roles of the frontal pole and the medial temporal lobes. Neuroimage, 19, 1369–1380.

Ongur, D., Ferry, A. T., & Price, J. L. (2003). Architectonic subdivision of the human orbital and medial prefrontal cortex. Journal of Comparative Neurology, 460, 425–449.

Petrides, M., & Pandya, D. N. (1999). Dorsolateral prefrontal cortex: Comparative cytoarchitectonic analysis in the human and the macaque brain and corticocortical connection

patterns. European Journal of Neuroscience, 11, 1011–1036.

Phan, K. L., Wager, T., Taylor, S. F., & Liberzon, I. (2002). Functional neuroanatomy of emotion: A meta-analysis of emotion activation studies in PET and fMRI. Neuroimage, 16, 331–348.

Pollmann, S. (2004). Anterior prefrontal cortex contributions to attention control. Experimental Psychology, 51, 270–278.

Porrino, L. J., Crane, A. M., & Goldman-Rakic, P. S. (1981). Direct and indirect pathways from the amygdala to the frontal lobe in rhesus monkeys. Journal of Comparative Neurology, 198, 121–136.

Price, C. J., & Friston, K. J. (1997). Cognitive conjunction: A new approach to brain activation experiments. Neuroimage, 5, 261–270.

Ramnani, N., & Owen, A. M. (2004). Anterior prefrontal

cortex: Insights into function from anatomy and neuroimaging. Nature Reviews Neuroscience, 5, 184–194.

Rorden, C., & Brett, M. (2000). Stereotaxic display of brain lesions. Behavioral Neurology, 12, 191–200.

Semendeferi, K., Armstrong E., Schleicher, A., Ziles, K., & von Hoesen, G. W. (2001). Prefrontal cortex in humans and apes: A comparative study of area 10. American Journal of Physical Anthropology, 114, 224–241.

Simons, J. S., Gilbert, S. J., Owen, A. M., Fletcher, P. C., & Burgess, P. W. (2005). Distinct roles for lateral and medial anterior prefrontal cortex in contextual recollection. Journal of Neurophysiology, 94, 813–820.

Simons, J. S., Owen, A. M., Fletcher, P. C., & Burgess, P. W.

(2005). Anterior prefrontal cortex and the recollection of contextual information. Neuropsychologia, 43, 1774–1783.

Small, D. M., Gitelman, D. R., Gregory, M. D., Nobre, A. C., Parrish, T. B., & Mesulam, M. M. (2003). The posterior cingulate and medial prefrontal cortex mediate the anticipatory allocation of spatial attention. Neuroimage, 18, 633–641.

Steele, J. D., & Lawrie, S. M. (2004). Segregation of cognitive and emotional function in the prefrontal cortex: A stereotactic meta-analysis. Neuroimage, 21, 868–875.

Talairach, J., & Tournoux, P. (1988). Co-planar stereotaxic atlas of the human brain. Stuttgart: Thieme.

Wager, T. D., Jonides, J., & Reading, S. (2004). Neuroimaging studies of shifting attention: A meta-analysis. Neuroimage, 22, 1679–1693.

Wood, J. N., & Grafman, J. (2003). Human prefrontal cortex: Processing and representational perspectives. Nature Reviews Neuroscience, 4, 139–147.

