arXiv:cond-mat/0309092v3[cond-mat.dis-nn]13Jan2005

.

Scale-free brain functional networks

Victor M. Egu´ıluz,1 Dante R. Chialvo,2 Guillermo A. Cecchi,3 Marwan Baliki,2 and A. Vania Apkarian2

1Instituto Mediterr´aneo de Estudios Avanzados, IMEDEA (CSIC-UIB), E07122 Palma de Mallorca, Spain 2Department of Physiology, Northwestern University, Chicago, Illinois, 60611 3IBM T.J. Watson Research Center, 1101 Kitchawan Rd., Yorktown Heights, NY 10598 (Dated: February 2, 2008)

Functional magnetic resonance imaging (fMRI) is used to extract functional networks connecting correlated human brain sites. Analysis of the resulting networks in diﬀerent tasks shows that: (a) the distribution of functional connections, and the probability of ﬁnding a link vs. distance are both scale-free, (b) the characteristic path length is small and comparable with those of equivalent random networks, and (c) the clustering coeﬃcient is orders of magnitude larger than those of equivalent random networks. All these properties, typical of scale-free small world networks, reﬂect important functional information about brain states.

[Figure 1]

PACS numbers: 87.18.Sn 87.19.La 89.75.Da 89.75.Hc

Recent work has shown that disparate systems can be described as complex networks, that is assemblies of nodes and links with nontrivial topological properties, examples of which include technological, biological and social systems [1]. The brain is inherently a dynamic system, in which the traﬃc between regions, during behavior or even at rest, creates and reshapes continuously complex functional networks of correlated dynamics. An important goal in neuroscience is to understand these spatio-temporal patterns of brain activity. This Letter proposes a method to extract functional networks, as revealed by fMRI in humans, and analyze them in the context of the current understanding of complex networks (for reviews see [1, 2, 3]).

Figure 1 shows how underlying functional networks are exposed during any given task. In these experiments, at each time step (typically 400 spaced 2.5 sec.), magnetic resonance brain activity is measured in 36 × 64 × 64 brain sites (so-called “voxels” of dimension 3 × 3.475 × 3.475 mm3). The activity of voxel x at time t is denoted as V (x,t). We deﬁne that two voxels are functionally connected if their temporal correlation exceeds a positive pre-determined value rc, regardless of their anatomical connectivity [4, 5]. Speciﬁcally, we calculate the linear correlation coeﬃcient between any pair of voxels, x1 and x2, as:

FIG. 1: (Color online) Methodology used to extract functional networks from the signals. The correlation matrix is calculated and then used to deﬁne the network among the highest correlated nodes. Top four images represent snapshots of activity and the three traces correspond to selected voxels from visual (V1), motor (M1) and posterio-parietal (PP) cortices.

V (x1,t)V (x2,t) − V (x1,t) V (x2,t) σ(V (x1))σ(V (x2))

,

r(x1,x2) =

[Figure 2]

(1) where σ2(V (x)) = V (x,t)2 − V (x,t) 2, and  ·  represents temporal averages.

Figure 2 shows the degree distributions of networks extracted using this method. The data was collected while the subject was opposing ﬁngers 1 and 2 during 10 seconds, and then resting during 10 sec. We ﬁnd a skewed distribution of links with a tail approaching a distribution p(k) ∼ k−γ, with γ around 2. This power law is more ev-

ident for networks constructed with higher thresholds rc (more correlated conditions). For decreasing rc, a maximum appears which shifts to the right. Despite changes in parameters, networks remain clearly deﬁned indicating that the main conclusions are robust with respect to the selection of parameters. The small inset in Fig. 2 shows the distribution of links of a network constructed from the randomly shuﬄed (in time) voxels’ signal. This network displays a Gaussian degree distribution in which the mean and width depend on rc. The largest values of

- 100
- 101
- 102
- 103
- 104
- 105

- 100
- 101
- 102
- 103
- 104

500

- rc = 0.6

- rc = 0.7

- rc = 0.8

Counts(k)

Counts(k)

Counts(k)

0

700 800 Degree K

- rc= 0.5

- rc= 0.6

- rc= 0.7

100 101 102 103 Degree K

100 101 102 103 Degree K

100

FIG. 2: (Color online) Degree distribution for three values of the correlation threshold. The inset depicts the degree distribution for an equivalent randomly connected network.

10-1

Prob.()k

the correlation thresholds used to construct the random networks are usually extremely low (rc ∼ 0.1) compared to that used to deﬁne the functional networks (rc ∼ 0.7). Our data was also compared with values from a randomly re-wired network, where nodes keep their degree by permuting links (i.e., the link connecting nodes i,j is permuted with that connecting nodes k,l) [6] (see below). In this control the degree of each node is maintained but all other correlations (including clustering) are destroyed.

∆

10-2

10-3

10-4

100 101 102 (mm)

∆

To test the generality of these ﬁndings the same analysis was performed in 7 subjects across 3 task conditions. During data acquisition [7] subjects perform on-oﬀ ﬁnger tapping with three diﬀerent protocols. In one case they are instructed verbally to start and stop tapping, in the other one the start/stop cue is a small green/red dot in a video screen, and in the last one the start/stop cue is the entire screen turning green or red. The results are very robust across subjects and task conditions. In particular, the average of degree distribution (see Fig. 3) shows a clear power law scaling decaying as p(k) ∼ k−γ, with an exponent close to 2. Although a precise ﬁtting is arguably diﬃcult, we ﬁnd that for rc=0.6 γ = 2, for rc=0.7 is 2.1 and for rc=0.8 is 2.2. This power law, indicating that the functional networks are scale-free, implies that there is always a small but ﬁnite number of brain sites having broad “access” to most other brain regions. Those well connected nodes are comparatively much more numerous in these networks than in a randomly connected network.

FIG. 3: (Color online) Average scaling taken from 22 networks extracted from seven subjects. Top Panel: Average degree distribution. The straight line illustrates a decay of k−2. Bottom panel: Average probability of ﬁnding a link between two nodes separated by a distance larger than ∆ (using rc = 0.6).

further corroborated this feature by analyzing two radically diﬀerent brain states: listening to music and ﬁnger tapping. As shown in Fig. 4, although the topographic distribution of the functional networks is very diﬀerent for the two tasks, they have similar scaling behavior. For comparison, the standard activation map derived with the generalized linear model [8] is also shown.

Now we turn to describe statistical properties of these networks: path length and clustering. The path length (L) between two voxels is the minimum number of links necessary to connect both voxels. Clustering (C) is the fraction of connections between the topological neighbors of a voxel with respect to the maximum possible. If voxel i has degree ki, then the maximum number of links between the ki neighbors is ki(ki − 1)/2. Thus, if Ei is the number of links connecting the neighbors then the clustering of voxel i, Ci = 2Ei/ki(ki − 1). The average clustering of a network is given by C = 1/N i Ci, where N is the number of voxels. Clustering was analyzed also with respect to degree. The average clustering over voxels with the same degree C(k) = 1/Nk j={i|k

As shown in the bottom panel of Fig. 3 the average probability of ﬁnding a link between two nodes, separated at least by a distance ∆, also decays as a power law. The signiﬁcance of the scaling with distance is unclear because of the well known extensive cortex folding, which makes linear distance a dubious parameter.

The scale-free character remains unaltered even for tasks engaging diﬀerent brain regions. This is already implicit in the aggregated data of Fig. 3 (top panel), but we

i=k} Cj, where the sum runs over the Nk voxels with degree k.

[Figure 3]

[Figure 4]

A B

[Figure 5]

[Figure 6]

C D

[Figure 7]

- FIG. 4: (Color online) Comparison for two tasks: Panels A and B correspond to a ﬁnger tapping task while C and D to listening to music analyzed with our method or the standard fMRI linear model. Colors in pictures of panels A and C code the number of links detected with our method, and those in panels B and D the activation map build with standard model [8]. The link distributions (lower panel) show that the networks for both tasks are scale free.

Table 1 summarizes the results for the networks analyzed showing the average values (n = 22 datasets) for each threshold (rc, ﬁrst column) used to construct the networks. Listed are N, C, L, the average degree k , and γ. The clustering (Crand) and path length (Lrand) values of an equivalent random network are also included for comparison. Note that as the threshold rc increases the total number of nodes N decreases substantially, resulting by deﬁnition in more correlated networks. As a result, the number of nodes with at least one link decreases, and consequently the k value decreases as well. In all cases, the coeﬃcient C remains four orders of magnitude larger than Crand. Networks randomized using the rewiring described by Maslov et al. [6] also have clustering signiﬁcantly smaller than the raw data (the order of 10−2). This feature, together with the similarity of path length of the original nets and their randomized controls (L and Lrand), is indicative of a small-world structure [2, 3]. This property is robust as it does not depend on parameter rc.

[Figure 8]

[Figure 9]

[Figure 10]

[Figure 11]

[Figure 12]

[Figure 13]

[Figure 14]

[Figure 15]

[Figure 16]

[Figure 17]

rc N C L k γ Crand Lrand

[Figure 18]

[Figure 19]

- 0.6 31503 0.14 11.4 13.41 2.0 4.3×10−4 3.9

[Figure 20]

[Figure 21]

[Figure 22]

[Figure 23]

[Figure 24]

[Figure 25]

[Figure 26]

[Figure 27]

[Figure 28]

- 0.7 17174 0.13 12.9 6.29 2.1 3.7×10−4 5.3

[Figure 29]

[Figure 30]

[Figure 31]

[Figure 32]

[Figure 33]

[Figure 34]

[Figure 35]

[Figure 36]

[Figure 37]

- 0.8 4891 0.15 6. 4.12 2.2 8.9×10−4 6.0

[Figure 38]

[Figure 39]

[Figure 40]

[Figure 41]

[Figure 42]

[Figure 43]

[Figure 44]

[Figure 45]

[Figure 46]

- TABLE I: Average statistical properties of the brain functional networks.

[Figure 47]

[Figure 48]

Network N C L k γ Crand Lrand C. Elegans 282 0.28 2.65 7.68 NA 0.025 2.1

[Figure 49]

[Figure 50]

[Figure 51]

[Figure 52]

[Figure 53]

[Figure 54]

[Figure 55]

[Figure 56]

[Figure 57]

[Figure 58]

[Figure 59]

[Figure 60]

[Figure 61]

[Figure 62]

[Figure 63]

[Figure 64]

[Figure 65]

[Figure 66]

[Figure 67]

Macaque VC 32 0.55 1.77 9.85 NA 0.318 1.5 Cat Cortex 65 0.54 1.87 17.48 NA 0.273 1.4

[Figure 68]

[Figure 69]

[Figure 70]

[Figure 71]

[Figure 72]

[Figure 73]

[Figure 74]

[Figure 75]

[Figure 76]

[Figure 77]

[Figure 78]

[Figure 79]

[Figure 80]

[Figure 81]

[Figure 82]

[Figure 83]

[Figure 84]

[Figure 85]

- TABLE II: Previously reported statistics of relatively smaller networks. None of these networks is scale-free.

To our knowledge, this is the ﬁrst report on the topological structure of a large scale brain network. Previous studies employing these statistical analyses have been limited to the small data sets of C. Elegans [2], and two neuro-anatomical databases [9, 10], the macaque visual cortex [11] and the cat cortex [12](see Table 2). These studies did not demonstrate scale-free features. Comparison with the previous two reports indicate the following: although clustering in the present study is smaller in absolute value, it is still orders of magnitude larger than the random case (10−1 vs. 10−4), while in the previous reports the clustering of the experimental data was just one order of magnitude larger than the randomized controls in the best case. Interestingly, the average connectivity k in all cases is of the same order, despite the huge diﬀerences in networks’ origins and sizes. Accordingly, this consistency may reﬂect some constraint(s) inherent to network construction. These quantitative features show that the human brain network examined here has small world properties, a ﬁnding that was previously postulated [2, 3].

Figure 5 illustrates the dependence of two important features upon a voxel’s degree. The ﬁrst is clustering, found in many cases to scale as C(k) ∼ k−α, an indication of hierarchical organization [13, 14]. We see, instead, a relative independence of clustering from degree. The second feature is that a highly connected node tends to connect with other well connected nodes. As shown in the bottom panel of Figure 5, there is a positive correlation between the degrees of adjacent vertices. This correlation, also called assortative mixing, is not typical of biological networks, but rather is distinctive of social networks [15]. Transitivity in correlations contributes to increase artifactually the clustering coeﬃcient, using partial directed coherence or Granger causality [16] in the future should clarify this.

In summary, we report statistical measures showing that the functional correlations of the human brain form a scale-free network with small world properties and as-

[Figure 86]

4

laws. Overall, the network properties uncovered here, offer a novel window to investigate the dynamics of brain states particularly in cases of dysfunction.

Work supported by MCyT of Spain (Projects CONOCE2, BFM2002-12792-E and FIS2004-05073-C0403) and NIH NINDS of USA (Grants 42660 and 35115). DRC is grateful for the hospitality and support of the Universitat de les Illes Balears, Mallorca, Spain.

[Figure 87]

[Figure 88]

[Figure 89]

[Figure 90]

- [1] R. Albert and A.-L. Barab´asi, Rev. Mod. Phys. 74, 47

(2002); M.E.J. Newman, SIAM Review 45, 167 (2003).

- [2] D.J. Watts and S.H. Strogatz, Nature 393, 440 (1998).
- [3] S.H. Strogatz, Nature 410, 268 (2001).
- [4] S. Dodel, J.M. Herrmann, and T. Geisel, Neurocomputing 44, 1065 (2002).
- [5] Networks can be deﬁned using negative correlations, we restrict ourselves to the positive case only for simplicity.
- [6] S. Maslov, K. Sneppen, and U. Alon, in Handbook of graphs and networks,S. Bornholdt and H.G. Schuster(Eds.)(Wiley -VCH and Co. Weinheim, 2003).
- [7] Seven healthy, right-handed human subjects were studied using a Siemens-Trio 3.0 Tesla imaging system using a birdcage radio-frequency head coil. Blood oxygenation level-dependent single-shot echo-planar T2weighted imaging was obtained using scan repeat time of 2500 ms, echo time of 30 ms, ﬂip angle 90, ﬁeld 256 mm. The data were preprocessed using the package FSL (http://www.fmrib.ox.ac.uk/fsl). All procedures employed were approved by Northwestern University Institutional Review Board.
- [8] K.J. Friston, in Brain Mapping: The Methods,Toga and Mazziotta (Eds.),(2002).
- [9] O. Sporns, G. Tononi, and G.M. Edelman, Cerebral Cortex 10, 127, (2000); O. Sporns and G. Tononi, Complexity 7, 28 (2003).
- [10] C.C. Hilgetag, G.A.P.C. Burns, M.A. O’Neill, J.W. Scannell, and M.P. Young, Phil. Trans. R. Soc. Lond.B 355, 91 (2000).
- [11] D.J. Felleman and D.C. Van Essen, Cerebral Cortex 1, 1

(1991).

- [12] J.W. Scannell, G.A.P.C. Burns, C.C. Hilgetag, M.A. O’Neil, and M.P. Young , Cerebral Cortex 9, 277 (1999).
- [13] E. Ravasz and A.-L. Barab´asi, Phys. Rev. E 67, 026112

(2003).

- [14] H. Jeong, S.P. Mason, A.-L. Barab´asi, and Z.N. Oltvai, Nature 411, 41 (2001).
- [15] M.E.J. Newman, Phys. Rev. Lett. 89, 208701 (2002).
- [16] L. Baccala and K. Sameshima, Biol. Cybern. 84, 463474.(2001).
- [17] B. Biswal, F.Z. Yetkin, V.M. Haughton, and J.S. Hyde, Magn Reson Med. 34, 537 (1995).
- [18] L.F. Lago-Fernandez, R. Huerta, F. Corbacho, and J.A. Siguenza. Phys. Rev. Lett. 84, 2758 (2000).
- [19] F. Radicchi, C. Castellano, F. Cecconi, V. Loreto, and D. Parisi, Proc. Natl. Acad. Sci. USA 101, 2658 (2004)
- [20] G. Caldarelli, A. Capocci, P. De Los Rios, and M.A. Mun˜oz, Phys. Rev. Lett. 89, 258702 (2002).

- FIG. 5: (Color online) Top Panel: Plot of clustering vs. degree. Bottom panel: Plot of a neighboring node’s degree vs. degree illustrates the assortative feature. Symbols represents individual data and continuous lines the average values for nodes with the same degree. (Same subject shown in Fig. 2, with rc=0.6).

sortative mixing. While some of these properties have been informally discussed, this work is the ﬁrst quantitative description of these large-scale topological properties, as well as the ﬁrst report of an assortative biological network. The scaling laws demonstrated here are robust across parameters (Fig. 1), subjects (Fig. 3), and task conditions (Fig. 4), suggesting they are invariant properties of an underlying dynamical network. The present results complement the extensive work done in the context of brain functional and eﬀective connectivity [8, 17]. The present approach has additional important implications. Namely, these studies can be extended to cases in which standard fMRI techniques cannot be used for lack of subject cooperation, (e.g., Alzheimer’s patients). Because scale-free complex networks are known to show resistance to failure, facility of synchronization, and fast signal processing [18], it would be important to see whether brain networks scaling properties are altered under various pathologies. In that regard, techniques for investigation of communities’ structures [19] should be useful to analyze these aspects. Work on models [20], is needed to further clarify speciﬁc origins of the scaling

