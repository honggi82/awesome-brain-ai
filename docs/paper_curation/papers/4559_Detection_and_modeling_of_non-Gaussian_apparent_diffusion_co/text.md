#### Magnetic Resonance in Medicine 48:331–340 (2002)

# Detection and Modeling of Non-Gaussian Apparent Diffusion Coefﬁcient Proﬁles in Human Brain Data

D.C. Alexander,1* G.J. Barker,2 and S.R. Arridge1

in all directions. The amount of diffusion or water mobility is thus approximately equal in all directions, i.e., isotropic. Other types of tissue, however, have ordered structure that hinders diffusion to different degrees in different directions, causing diffusion anisotropy. White matter in the brain, for example, consists of bundles of axon ﬁbers, and water is free to diffuse along the axis of the ﬁbers but is hindered in the perpendicular directions.

This work details the observation of non-Gaussian apparent diffusion coefﬁcient (ADC) proﬁles in multi-direction, diffusionweighted MR data acquired with easily achievable imaging parameters (b 1000 s/mm2). A technique is described for modeling the proﬁle of the ADC over the sphere, which can capture non-Gaussian effects that can occur at, for example, intersections of different tissue types or white matter ﬁber tracts. When these effects are signiﬁcant, the common diffusion tensor model is inappropriate, since it is based on the assumption of a simple underlying diffusion process, which can be described by

The diffusion of water molecules in tissue over some time interval, t, can be described by a probability density function, pt, on the displacement, x, of water molecules after time t. pt reﬂects the underlying tissue microstructure, because it is largest in the directions of least hindrance to diffusion and smaller in other directions. In white matter, for example, pt is largest in directions parallel to ﬁbers, but is small in perpendicular directions and thus reveals ﬁber orientations. The goal of diffusion imaging is to obtain information about pt that leads to meaningful inferences about the microstructure of the material being imaged.

- a Gaussian probability density function. A sequence of models of increasing complexity is obtained by truncating the spherical harmonic (SH) expansion of the ADC measurements at several orders. Further, a method is described for selection of the most appropriate of these models, in order to describe the data adequately but without overﬁtting. The combined procedure is used to classify the proﬁle at each voxel as isotropic, anisotropic Gaussian, or non-Gaussian, each with reference to the underlying probability density function of displacement of water molecules. We use it to show that non-Gaussian proﬁles arise consistently in various regions of the human brain where complex tissue structure is known to exist, and can be observed in data typical of clinical scanners. The performance of the procedure developed is characterized using synthetic data in order to demonstrate that the observed effects are genuine. This characterization validates the use of our method as an indicator of pathology that affects tissue structure, which will tend to reduce the complexity of the selected model. Magn Reson Med 48:331–340, 2002. © 2002 Wiley-Liss, Inc. Key words: diffusion tensor magnetic resonance imaging; human brain; non-Gaussian; spherical harmonic; model selection

pt can be shown to relate to the NMR signal attenuation, S(q), measured through a pulsed gradient spin-echo experiment, via a Fourier transform (FT) with respect to q

G kˆ (4,5):

S q pt x exp( iq x )dx . [1]

The spin-echo attenuation, S(q ), is deﬁned as the normalized diffusion-weighted signal, s(q )/s(0), where s(q ) is the NMR signal in the presence of a diffusion-weighting gradient of magnitude G and direction kˆ, and s(0) is the signal in the absence of any such gradient. is the length of the gradient pulse, and is the magneto-gyric ratio of protons in water. We note that Eq. [1] relies on the fact that

Diffusion imaging, particularly diffusion tensor magnetic resonance imaging (DT-MRI) (1) has become popular because of the insight it provides into the structural connectivity of tissue (2,3). Water is a large constituent of biological tissue, and water molecules in tissue constantly undergo random, Brownian motion. Tissue also contains rigid structures, such as the walls of cells, that form barriers to diffusion, and it is this hindrance to diffusion that allows tissue structure to be probed through measurements of water mobility due to diffusion processes. In some types of tissue, such as most gray matter in the brain, the structure has no preferred orientation and so causes approximately the same amount of hindrance to diffusion

is negligibly small compared to t. This assumption is rarely justiﬁed in practice, but the effect of non-negligible

is merely to introduce a convolution over a range of diffusion times (6) into the measurements, which generally preserves the large-scale structure and orientation of the inferred pt.

Given enough measurements of S(q ) spread over a suitable range of q , the FT can be inverted to obtain an estimate of pt. A more common approach, however, is to assume a simple model for pt the FT of which can be related directly to the spin-echo attenuation, which allows pt to be inferred from a much sparser set of measurements. The simplest model for pt that incorporates second-order statistics (anisotropy) is a multivariate, zero-mean Gaussian, which has covariance 2Dt at time t:

1Department of Computer Science, University College London, London, UK. 2Institute of Neurology, University College London, London, UK.

Grant sponsor: Multiple Sclerosis Society of Great Britain and Northern Ireland.

*Correspondence to: Daniel Alexander, Dept. of Computer Science, University College London, Gower Street, London WC1E 6BT, UK. E-mail: Daniel.Alexander@cs.ucl.ac.uk

Received 27 July 2001; revised 7 March 2002; accepted 9 March 2002. DOI 10.1002/mrm.10209 Published online in Wiley InterScience (www.interscience.wiley.com).

x T D 1x 4t

1 4 t 3 D

pt x

exp

. [2]

© 2002 Wiley-Liss, Inc. 331

This is the distribution of an initial point concentration at x 0, t 0, diffusing according to the simple anisotropic diffusion equation (7):

pt t

D pt . [3]

The FT of pt is then also Gaussian, which gives rise to a simple relationship between the parameters of pt (the elements of D) and the spin-echo attenuation:

S q exp tq TDq exp bkˆ T Dkˆ . [4]

In Eq. [4], b is the diffusion-weighting factor given by

- b t|q |2. The simplest form of diffusion-weighted (DW) MRI (8)

models pt with a Gaussian in one dimension. A single spin-echo attenuation measurement allows the single pa-

rameter of pt—its scalar variance—to be estimated from Eq. [4]:

d kˆ

1 b

log S q . [5]

The diffusion coefﬁcient, d(kˆ), is proportional to the variance of the Gaussian model, which describes the root mean squared displacement of water molecules in the direction of the applied DW gradient kˆ. In DW-MRI, the measure of d(kˆ) obtained from Eq. [5] is often called the apparent diffusion coefﬁcient (ADC) (1), both because it represents a spatial average of the diffusion coefﬁcient over an image voxel and because it is based on this Gaussian assumption, which may be unjustiﬁed.

DT-MRI extends this basic idea to 3D, where the diffusion coefﬁcient is described by a diffusion tensor (DT), D, which is proportional to the covariance matrix of the trivariate Gaussian, as in Eq. [2]. D relates to the 1D diffusion coefﬁcient d(kˆ) in any chosen direction kˆ as follows:

d kˆ kˆ T Dkˆ . [6]

In 3D, D is a symmetric 3 3 matrix and thus has six free parameters. A minimum of six estimates of d(kˆ) in independent directions is thus required to estimate D, which requires six measurements of the spin-echo attenuation (seven MR measurements in total) to be made with the DW gradient applied in these independent directions. The estimate of D obtained from such a set of measurements is referred to as the apparent diffusion tensor (ADT) (1), as in the case of the ADC.

We deﬁne the “ADC proﬁle” to be the estimate of d(kˆ) over the range of kˆ, which is the unit sphere. When pt is Gaussian, the ADC proﬁle is described by Eq. [6], and a standard approach (9) to the estimation of D is to acquire DW images in a large number of directions (many more than six) spread evenly over the unit hemisphere. This oversampling of the ADC proﬁle provides a more robust estimate of D. Note that the antipodal symmetry of pt and hence d(kˆ) is assumed, so that d(kˆ) d( kˆ) and only half of the sphere needs to be sampled. When pt is not Gaussian

the ADC proﬁle deviates from that described by Eq. [6], and this kind of multiple gradient direction scheme affords the possibility of observing signiﬁcant deviations should they arise.

It has long been recognized (1,10–14) that the Gaussian, DT model is inappropriate when complex tissue structure is found within a single image voxel. There are alternative models for pt that can capture certain non-Gaussian effects that occur in these circumstances. A simple alternative is the multi-Gaussian model (10,11). This model is based on the assumption that a voxel contains n separate compartments, each containing a different tissue type in proportion ai ( i ai 1, i 1, . . . n) and that the diffusion within each compartment can be described by a Gaussian pt with DT, Di. The model assumes further that there is no exchange of molecules between these separate compartments. pt then becomes a weighted sum of Gaussians and Eq. [4] becomes:

S q

n

ai exp( bkˆ T Dikˆ ). [7]

i 1

With this model for pt, the ADC proﬁle can have shape very different from that described by Eq. [6], which is often modeled poorly by a single DT (10). Figure 1 shows ADC proﬁles simulated from prolate, oblate, and isotropic Gaussian pt’s, together with proﬁles obtained from biGaussian pt’s that combine them. Note the characteristic peanut shape of the prolate Gaussian ADC proﬁles and the “ﬁlled bagel” or red blood cell shape of the oblate Gaussian proﬁle, which are typical of Gaussian functions plotted over a sphere. The contours of the corresponding Gaussian functions in 3D have the more familiar ellipsoidal contours: cigar-shaped in the prolate case, and Frisbee-shaped in the oblate case.

Alexander et al. (10) analyzed the behavior of the ADC proﬁle within voxels containing multiple tissue compartments. They showed how the observability of higher-order proﬁles increases (their non-Gaussian shape becomes more pronounced) with the size of the diffusion-weighting factor, b. They used the instability of the DT and its derived scalar measures, such as the mean diffusivity and fractional anisotropy, to locate regions in the brain where the DT description of the ADC proﬁle is poor. Several regions in data acquired with b 3000 s/mm2 were highlighted by this approach, including the pons, corpus callosum, cingulum, internal capsule, and arcuate fasciculus.

Frank (11) showed that a 4th-order SH series provides a ﬁrst approximation to the ADC proﬁle obtained from a multi-Gaussian pt. Frank ﬁtted a 4th-order SH series to ADC measurements acquired with b 3000 s/mm2 and showed that signiﬁcant 4th-order (i.e, non-Gaussian) components arise in locations of the human brain similar to those highlighted in Ref. 10 (see above).

In other related work, Wedeen and Tuch et al. (12,13) used q-space techniques (4) to measure pt. This technique exploits the Fourier relationship between pt and the spinecho attenuation directly by acquiring a large number of measurements of S(q ) over a wide range of q in order to obtain enough samples of the FT of pt to perform a stable

[Figure 1]

- FIG. 1. Simulated examples of ADC proﬁles. Top row: proﬁles corresponding to Gaussian diffusion processes: (i) prolate DT oriented along the x-axis (eigenvalues [1700, 200, 200] 10–6 mm2/s), (ii) prolate DT oriented along the z-axis (eigenvalues [200, 200, 1700] 10–6 mm2/s), (iii) oblate DT (eigenvalues [950, 950, 200] 10–6 mm2/s), and (iv) isotropic DT (eigenvalues [700, 700, 700] 10–6 mm2/s). Bottom row: ADC proﬁles corresponding to the bi-Gaussian model combining pairs of DTs from the top row in equal proportion with b set to 1000 s/mm2; (v) combines (i) and (ii), (vi) combines (i) and (iii), (vii) combines (ii) and (iii), and (viii) combines (i) and (iv).

inversion. Distinctly non-Gaussian pt’s have been observed in both the human brain and heart, particularly at locations where anisotropic ﬁbers cross within a single voxel.

In this work, we investigate the observability of nonGaussian ADC proﬁles in DW data acquired using acquisition parameters more typical of those used clinically. Our sequence consists of a multiple gradient direction scheme based on the work of Jones et al. (9) using a 1.5T scanner, with a maximum b of approximately 1000 s/mm2. We use the spherical harmonic (SH) series to provide a hierarchy of models for the ADC proﬁle. In the Methods section, an efﬁcient and robust method for ﬁtting the SH series to DW-MRI data is described together with a method, based on the analysis of variance (ANOVA) test for addition/deletion of variables, for selecting the most appropriate level of truncation of the series. The combined ﬁtting and model selection procedures developed are used to classify the proﬁle in each voxel as arising from isotropic, anisotropic Gaussian, or non-Gaussian pt, and thus to produce maps of where these different types of behavior occur. Non-Gaussian behavior is most likely to arise and be observed in regions of high tissue complexity containing distributions of ﬁber orientations with multiple peaks, such as ﬁber intersections. The maps generated from the model selection procedure provide extra diagnostic information in pathologies involving neuronal loss, degeneration, or demyelination, since non-Gaussian behavior will tend to disappear in the affected areas because the complexity of the tissue structure is reduced. These maps can

also be used to highlight regions in which the ADT and its derived indices are unreliable. We apply the method to both in vivo human brain data and to synthetic data for performance evaluation and validation.

METHODS Models for the ADC Proﬁle

In this section, we describe how the SH series can be used to model the ADC proﬁle. We deﬁne the SH series, describe how its coefﬁcients are computed for a given function or set of sampled data, and discuss the relationship to more familiar models of the ADC.

SH Series

The SH series (15) is analogous to the rectilinear Fourier series, and provides an orthonormal basis of functions on the sphere that can be combined linearly to represent any complex valued spherical function. It consists of a set of functions Yl, m: S2 3 C, where S2 is the unit sphere in 3D, which we parametrize by [0, ) and [0, 2 ), the angles of colatitude and longitude, respectively; C is the set of complex numbers. l 0, 1, 2, . . . deﬁnes the order of the SH and m {–l, . . ., 0, . . .l} indexes the 2l 1 SH functions of order l.

Any spherical function, f: S2 3 C, can be written as a linear combination of the SHs:

### f ,

l

cl,m Yl,m , . [8]

l 0 m l

The complex coefﬁcients, cl, m, of the SHs in Eq. [8] are given by:

cl,m

2

f , Y*l,m , sin d d . [9]

0

0

In Eq. [9] and henceforward, * denotes the complex conjugate.

Fitting the Series to Sampled Data In the discrete case, where we have sampled data, F {f( i,

i), i 1, . . ., n}, one way to estimate the cl, m is to replace the integral in Eq. [9] by a summation. However, as noted by Brechbuhler et al. (16), this approach often provides poor estimates, and a more robust approach is to compute the least-squares solution. We adopt a similar approach here. First, we deﬁne an enumeration of the SH series, so that each SH is indexed by a single, unique integer, j(l, m) l2 l m. We select a maximum order for the series, lmax, and then deﬁne an n j(lmax, lmax) complex matrix, X, to be the matrix with elements Xi, j(l, m) Yl, m( i, i). If we deﬁne C to be the j(lmax, lmax) component vector of SH coefﬁcients, then (16):

C M F , where M (X*T X) 1 X*T. [10]

lmax can be chosen by consideration of the number of free parameters deﬁning the series up to each order, which should be less than or equal to the number of sampled points.

Modeling DW-MR Data

In its most general form, the SH series can represent any complex-valued function of the sphere in 3D. The set of functions required to model ADC proﬁles, however, is more constrained. In particular, the ADC is real-valued and exhibits antipodal symmetry (d(kˆ) d( kˆ)).

The real-valued constraint ensures both that the imaginary part of cl, 0 is zero for all l, and that cl,m ( 1)m c*l, m. The SHs of odd order all deﬁne asymmetric functions on the sphere, whereas the even orders are all symmetric. The antipodal symmetry of the ADC proﬁle thus ensures that it can be represented by a series consisting only of evenorder SHs.

These constraints dramatically reduce the number of parameters required to describe SH models truncated at each order. The numbers of free parameters required for a SH series including terms up to order 2N for general spherical functions is 2(2N 1)2, which is reduced to (2N 1)(N 1) for our real, symmetric functions.

Equation [10] shows that the calculation of the SH coefﬁcients from the set of sampled points on the ADC proﬁle is a linear transformation and so can be computed very

efﬁciently. Moreover, the set of sampled points at each voxel in the image correspond to the same set of directions, so that {( i, i), i 1, . . . n} is ﬁxed over the image. The matrix M, of Eq. [10], therefore need only be calculated once in order to compute C at each voxel.

Models at Different Orders

If the SH series is truncated at order 0, the series provides an isotropic model, since the single 0th-order SH is constant over the sphere. If the series is truncated at order 2, it provides a model that is completely equivalent to the familiar DT model. An expression for the DT in terms of the 0th- and 2nd-order SH coefﬁcients can be obtained if we express kˆ in Eq. [6] in terms of and , as in Eq. [8], and equate the right sides of these two equations. When we include higher-order members of the series, a range of more complex shapes becomes available. In particular, at order 4 we can obtain models with two pairs of peaks that have similar shape to the proﬁles obtained from the biGaussian model, shown in Fig. 1.

Model Selection

Once we have computed the coefﬁcients of the SH series for a set of measurements, a hierarchy of increasingly complex models is obtained by truncating the series at each order, l 0, 2, 4, , lmax (the coefﬁcients of the SHs above order l are set to zero). Although higher-order models are more descriptive, in many cases they are not necessary to describe the underlying function from which the measurements were taken. For example, if the underlying function is isotropic, we only need a series up to order 0 to describe it, and higher-order terms will only represent noise added to the data during the imaging process.

We use ANOVA to determine whether the addition of more parameters to the model, i.e., truncating the series at a higher order as opposed to a lower order, signiﬁcantly changes the ﬁt of the model to the data (17). Given a set of N sampled points, together with a lower order model M1 with p1 free parameters and a higher order model M2 with p2 free parameters, the appropriate statistic for the F-test of the hypothesis that the two models are equivalent, i.e., the lower order model is sufﬁcient, is

F(M1, M2)

(N p2 1)(Var(M2) Var(M1)) (p2 p1)E(M2)

. [11]

The degrees of freedom are N – p2 – 1 and p2 – p1 (17). In Eq. [11], Var(M) denotes the variance of model M about its mean value, and E(M) denotes the mean squared error between model M and the N sampled points.

The full algorithm for modeling the ADC proﬁle in one voxel is outlined below:

- ● Compute the coefﬁcients of the even SH series up to order lmax using Eq. [10].
- ● Truncate the series at order 0 to obtain model M .
- ● Set i 2 and 0.
- ● While (i lmax),

X Truncate the series at order i to obtain model Mi. X Compute F(M , Mi) using Eq. [11].

X Deﬁne the null hypothesis to be that models Mi and

M are equivalent.

X Compute the critical value, T, for F(M , Mi) such that if F(M , Mi) T then the probability of the null hypothesis is less than a decision threshold, .

X If F(M , Mi) T (null hypothesis is rejected) y Set i.

X Set i i 2. ● Select model M .

## EXPERIMENTS

The central hypothesis to be tested is that ADC proﬁles corresponding to non-Gaussian diffusion processes occur in the human brain, and that their effects can be observed in data collected with parameters typical of standard clinical MR scanners, using the methods described in the previous section. In order to verify this hypothesis we apply our methods to a variety of synthetic data and to human brain DW-MR data.

The synthetic data is created by a Monte Carlo simulation of the imaging process. This data is ﬁrst used to set the parameters of the model selection procedure, and subsequently to characterize its performance in terms of the number and type of misclassiﬁcations that occur for noisy proﬁles of known order. We go on to show the results of applying our procedure to human brain data, which exhibit clusters of non-Gaussian proﬁles in various welldeﬁned regions. In order to conﬁrm that the higher-order regions observed in the human brain data genuinely correspond to non-Gaussian behavior, we perform a ﬁnal simulation in which parameters derived from ﬁtting Gaussian (order 2 SH) models in these regions are used to generate synthetic data, which is then reprocessed to show that if the data were truly Gaussian this would have been detected reliably. For brevity, only the most signiﬁcant results are included, but more comprehensive results can be found in Ref. 23.

Simulation Experiments

We simulate the imaging sequence used to acquire the human brain data described in the next section in order to generate noisy measurements of various ideal ADC proﬁles. A range of DTs is used to provide models for proﬁles corresponding to isotropic and anisotropic Gaussian diffusion, and we use a bi-Gaussian model, c.f. Eq. [7], to obtain non-Gaussian ADC proﬁles corresponding to mixed tissue and ﬁber crossings.

For a given proﬁle, we simulate a 128 128 2D array of noisy measurements of the proﬁle. Isotropic complex Gaussian noise is added to the simulated data in the time domain, at a level corresponding to that observed in the scanner in the absence of any signal. Noisy magnitude images are reconstructed from this data, which correspond to each of the 60 DW images acquired in our sequence (see next section) together with three unweighted images. Spin-echo attenuation and thence ADC measurements in each of the 60 sampled directions are then calculated, and our procedure is applied.

The ﬁrst set of experiments performed are designed to provide appropriate settings for the decision thresholds,

, used in the F-test in the algorithm described in the Model Selection section. Lower settings of the ’s cause the null hypotheses to be more difﬁcult to reject, which will generally result in an increase in the proportions of lower-order models. Higher values of the ’s result in a greater proportion of higher-order models, and in general there is a trade-off between the number of overﬁtted and underﬁtted voxels, the occurrence of both of which we would like to minimize. We simulate the following Gaussian ADC proﬁles for testing using typical values as given in Ref. 3:

- 1. Gray matter (GM). Approximately isotropic diffusion with eigenvalues [700, 700, 700] ( 10–6 mm2/s) and the unweighted signal is chosen so that its signal-to-

noise ratio (SNR), 0 35, which is typical in our scanner data.

- 2. Prolate white matter (WM). Eigenvalues [1700, 200, 200] ( 10–6 mm2/s), 0 35.
- 3. Oblate WM. Eigenvalues [950, 950, 200] ( 10–6 mm2/ s), 0 35.

We also simulate proﬁles from orthogonal crossing ﬁbers in equal proportions, where each ﬁber is represented by a prolate DT with eigenvalues [1700, 200, 200] ( 10–6 mm2/s) and 0 35.

For each proﬁle, is varied and the number of voxels at which each model order is selected is recorded. For each model order , we choose to be the value for which the sum of the rate of overﬁtting of proﬁles of known order and the rate of underﬁtting of proﬁles of known order 2 is minimized.

Once appropriate decision thresholds for our F-tests have been chosen in this way, we can characterize the performance of our procedure on a wider range of input data, which enables us to interpret results obtained from scanner data reliably. A series of oblate and prolate Gaussian ADC proﬁles are tested in which the anisotropy is increased from zero to approximately the highest levels observed in our brain data. The classiﬁcation rates of our procedure applied to the prolate data are plotted in Fig. 2, and similar results were obtained from the oblate proﬁles. These results demonstrate that with the selected ’s our procedure will identify anisotropic, Gaussian proﬁles correctly at order 2, with a classiﬁcation rate over 92%, when the difference ratio of the largest and smallest eigenvalues of the DT is approximately 1.5 or greater. At this lowest level of detected anisotropy, the rate of overﬁtting at order

- 4 is around 2%, but the rate increases steadily with increasing anisotropy to about 8% for the most anisotropic DT tested. This is reasonable to expect, because highly anisotropic DTs contain very low ADC measurements in which the noise component is high (19) and hence more likely to cause signiﬁcant deviation from the Gaussian proﬁle. Misclassiﬁcation at orders above 4 is negligible. Figure 2 also demonstrates the classiﬁcation of isotropic GM proﬁles, which is reliably order 0—the rate of misclassiﬁcation at order 2 is less than 0.1%. These rates are consistent for other isotropic DTs with larger eigenvalues.

We also simulate bi-Gaussian proﬁles to emulate the behavior at crossing ﬁbers intersecting at angles of 90°, 67.5°, 45°, and 22.5°, and in proportions 1:1 and 3:1. Each ﬁber is represented by a prolate DT with eigenvalues

[Figure 2]

- FIG. 2. Proportions of SH series model orders selected for proﬁles of simulated measurements from prolate DTs with varying levels of anisotropy (increasing right to left).

[1700, 200, 200] ( 10–6 mm2/s) and 0 35. Classiﬁcation rates from these proﬁles are plotted in Fig. 3. Figure

- 3 shows that our simulated ﬁber intersection proﬁles are classiﬁed as order 4 consistently when the ﬁbers are in equal proportion and are orthogonal, when only 3% of the proﬁles are underﬁt as order 2 proﬁles. However, the rate of misclassiﬁcation at order 2 increases signiﬁcantly as the proportion of the two ﬁbers becomes less balanced and as the two ﬁbers become more parallel. This is again reasonable to expect, because both these effects cause the deviation of the proﬁle from Gaussian to decrease. Classiﬁcation above order 4 for all these bi-Gaussian proﬁles varies between 0.5% and 1%. Other results (not shown, but see Ref.

23) demonstrate that the deviation from Gaussian behavior that is obtained by mixing isotropic and anisotropic Gaussian diffusion with the bi-Gaussian model is not reliably detected by our procedure with these imaging parame-

ters—only a minor increase in the order 4 classiﬁcation rate (from 7% to 18%) is observed for these mixed proﬁles.

Human Data Experiments

DW-MRI data was acquired from four healthy volunteers using a protocol similar to that outlined by Jones et al. (9). All subjects were scanned with the approval of the joint National Hospital and Institute of Neurology ethics committee and gave informed, written consent. Three unweighted (b 0 s/mm2) images were acquired together with 60 DW images with different gradient directions spread evenly over the hemisphere, with gradient pulse width 0.032 s, pulse separation 0.04 s, and gradient strength G 0.022 Tm–1, which gives b 1000 s/mm2 in each case. The reconstructed image array is 128 128 in plane with a ﬁeld of view (FOV) of 220 mm, and a

[Figure 3]

FIG. 3. Proportions of SH series model orders selected for proﬁles of simulated measurements of a bi-Gaussian ADC proﬁle from a combination of two prolate DTs intersecting at various angles, A. Results are included for cases in which there are equal proportions (Q 0.5) of the two tissue types, and three times more of one type (Q 0.75).

[Figure 4]

- FIG. 4. Order maps from human brain data (left) together with color-coded principal DT direction maps (middle) and mean diffusivity maps (right). The key below the images refers to the order maps in the left column.

total of 42 slices evenly spaced at 2.5 mm intervals were acquired.

The procedures described in Methods were applied to this data. Since 60 samples are available for each ADC proﬁle, the maximum series order that we can ﬁt is 8 (45 parameters). We thus compute the coefﬁcients of all evenorder SHs up to and including order 8 and then apply the

model selection procedure described above, with the decision thresholds determined from the simulated data, to choose the appropriate level of truncation of the series. Prior to model selection, two thresholds on 0 are applied: if 0 8.5, the voxel is classiﬁed as background and no model is assigned; if 0 85, we assume the voxel corresponds to CSF and assign an order 0 model, since ﬂow

[Figure 5]

- FIG. 5. Typical measurements (left) together with SH models of orders 0, 2, 4, 6, and 8 (second from left to right) from each of the three higher-order clusters labeled in Fig. 4. Top: measurement from the pons (order 4 model selected). Middle: measurement from the optic radiation (order 4 model selected). Bottom: measurement from the corona radiata (order 4 model selected).

artifacts in these regions make the measurements unreliable.

Figure 4 shows maps of the order chosen by our model selection procedure (left) for three axial slices of one of our data sets (results from the other data sets can be found in Ref. 23), together with mean diffusivity (right) and anisotropy-weighted color maps indicating the principal direction of the DT at each point (middle). In the images in the middle column, the red, green, and blue intensities correspond to the size of the x, y, and z components of the DT principal direction unit vector, weighted by the fractional anisotropy (2) as proposed by Pajevic and Pierpaoli (18).

A detailed anatomical analysis of the results is beyond the scope of this work, but we will highlight some interesting features. First, our procedure appears to separate regions of isotropic and anisotropic diffusion successfully. Regions of GM are mostly assigned order zero models, while regions of WM, both dense and peripheral, are mostly assigned order 2. A signiﬁcant percentage of voxels are assigned higher order models. The spatial distribution of these voxels exhibits distinct clusters in the image, which have clear symmetry about the midline of the brain. The clustering and symmetry strongly suggest that the higher-order models correspond to genuine anatomical effects.

Each slice shown in Fig. 4 contains an anatomic region that contains clusters of higher-order voxels consistently in each of our four data sets. In the top slice, the region corresponding to the pons contains a dense cluster of order

- 4 voxels (label 1). In this region, the right–left trans-pontine tracts cross the inferior-superior pyramidal tracts, causing partial volume effects between these two orthogonal ﬁbers. In the middle slice, dense clusters of order 4 voxels are found in the optic radiation on both sides of the brain (label 2). These occur precisely at the points where the anterior–posterior tracts of the optic radiation cross the predominantly right–left ﬁbers of the corpus callosum. In the bottom slice, large clusters of order

4 voxels can be observed within the corona radiata (label 3). Again this is reasonable to expect, since the diverging ﬁbers of the corona radiation are crossed by U-ﬁbers in these areas.

Figure 5 shows typical ADC proﬁles from each of these three regions, together with the order 0, 2, 4, 6, and 8 SH models. In each case, it is clear that there is signiﬁcant difference between the order 4 and order 2 models, which indicates signiﬁcant non-Gaussian behavior. The models with order greater than 4 do not appear to change the overall proﬁle shape signiﬁcantly further, and serve only to incorporate noise effects. The measurement from the pons is particularly striking and is typical of that predicted by the bi-Gaussian model for two orthogonally intersecting WM ﬁbers (see Fig. 1). The measurement from the optic radiation is similar but oriented within the axial plane and somewhat less pronounced, possibly due to a less balanced mix between the two ﬁbers, or a smaller angle of intersection. The proﬁle from the corona radiata is more difﬁcult to interpret, and may be the result of effects that are not modeled naturally by a bi-Gaussian model, such as ﬁber divergence or compartments with exchange.

Further Synthetic Experiments

Since the set of DTs tested in the synthetic experiments described in the Simulation Experiments section is not exhaustive, it is possible that the regions we observe in the human brain data simply exhibit Gaussian diffusion processes that are particularly prone to overﬁtting in our procedure. Thus, for completeness, we include an additional set of experiments to test this assertion. In each region, we ﬁt the DT (rather than the full SH series) at each voxel and model the distribution of DT eigenvalues, 1

2 3, together with the value of 0. We then use a Monte Carlo method to draw samples from this distribution and test the likelihood that the corresponding Gaussian ADC proﬁles are overﬁtted with SH models with order greater

than 2. 0 is included in this model, because the noise levels in ADC measurements depend on 0 as well as the magnitude of the ADC itself (19).

For each of the regions highlighted in the previous section (the pons, optic radiation, and corona radiata), a subregion of the order 4 cluster was selected. A model of the distribution of DT shapes in each subregion was obtained by ﬁtting a 4D multivariate Gaussian model to the distribution of vectors ( 1, 2, 3, and 0). Our procedure was then applied to large numbers of samples drawn from each of these distributions, and the rate of classiﬁcation above order 2 was found to be less than 5% in each case. These results verify that if the underlying diffusion process had been Gaussian, our procedure would have been effective and assigned most proﬁles in these regions order 2 models. Thus we conclude that we are observing genuine nonGaussian effects in these regions.

## DISCUSSION

We have described methods for modeling and detection of non-Gaussian ADC proﬁles and shown that such proﬁles can be observed with scanning parameters typical of standard clinical DW-MRI data. The SH series up to order 8 was ﬁt to samples of the ADC proﬁle in each voxel, which provides a sequence of models of increasing complexity. A series of ANOVA tests was used to ﬁnd the simplest of these models that adequately describes the data. This latter procedure classiﬁes the proﬁle at each voxel as isotropic, anisotropic Gaussian, or non-Gaussian, and allows maps of these different types of behavior to be produced, as shown in Fig. 4.

Our procedure was applied to human brain data collected with parameters typical of those used in clinical scans, and appeared to classify isotropic (GM) and anisotropic (WM) regions correctly as order 0 and order 2, respectively. On average, 5% of proﬁles in voxels within the brain were classiﬁed as order 4 or above (non-Gaussian). Several regions—in particular, the pons, optic radiation, and corona radiation—were found consistently to contain dense clusters of order 4 models. Validation of our method was performed by characterizing its performance using synthetic data with realistic noise properties, as well as applying it to DT models of data in regions of the brain that were consistently classiﬁed as non-Gaussian. Although results from only one data set are shown here, our method was applied to four data sets and other results can be found in Ref. 23. Acquisition of a larger ensemble of data sets is currently underway, which will enable parametric mapping to be performed in order to allow comparisons to be made between the occurrence of non-Gaussian diffusion in different population groups.

The behavior maps produced by our method provide new insights into the complexity of tissue structure in the brain. These maps have a number of practical applications. As mentioned in the Introduction, one aim is to use these maps as a stain for diagnosis of structure-reducing pathology. Furthermore, these maps can be used in postprocessing algorithms, such as tractography algorithms, which need to identify when diffusion is anisotropic and when the principal direction of the DT can be relied upon to describe the orientation of the underlying tissue. Finally,

these maps indicate when a more complex model (for example, a bi-Gaussian model) than the DT needs to be used to describe pt adequately. Typically, such models are more difﬁcult to ﬁt to data than the DT and nonlinear ﬁtting algorithms must be employed (see for example Ref. 21). Such procedures are computationally expensive, so it is advantageous to be able to identify only when they need to be performed.

It seems likely that most of the non-Gaussian behavior we observe is due to the intersection of WM ﬁbers with different orientation. This kind of tissue structure gives rise to proﬁles similar to those that are derived from multiGaussian pt’s (22), although it is also likely that some exchange of particles between the tissue compartments corresponding to each ﬁber occurs in the timescale of the diffusion measurement, which will cause pt to deviate from the multi-Gaussian (22). Other types of non-Gaussian processes almost certainly occur in the brain, caused by restriction due to impermeable barriers (22). However, the deviation from Gaussian that is caused by these effects is less marked than those due to multicompartmentation, so such behavior may not be observed reliably—particularly at low b-values such as those used here.

The advantages of the SHs as models for ADC proﬁles lie both in their generality and in the simplicity and robustness of the ﬁtting procedure. Linearity of the ﬁtting procedure is a signiﬁcant advantage in terms of computational effort, but also ensures that the ﬁtting procedure is well posed and is not prone to spurious erroneous results. There is little physical justiﬁcation for the use of the SHs in this context, and there may be more appropriate sets of basis functions that better reﬂect the kind of ADC proﬁles that are likely to arise given the underlying physical processes. An advantage of this series, however, is its generality: any proﬁle can be represented, and we do not limit ourselves to particular models of the underlying processes. We note for clarity that when pt is non-Gaussian the shape of the ADC proﬁle does not relate to pt in a straightforward way, and thus the SH shape does not provide any direct information about the underlying tissue structure. Although it is possible to extract some information of this type from non-Gaussian proﬁles on the sphere (21), this issue is beyond the scope of this work.

There are many techniques for model selection in the literature. The use of ANOVA and the F-test for deletion of variables has proved more successful than most in our application, but there may be others that improve performance to some extent. The test we used is based on an assumption of Gaussian errors in the measurements. Although this is a reasonable ﬁrst approximation for our data (23), the full analytic form of the errors in ADC measurements is not Gaussian. There are tests that incorporate noise models for the data, which may improve classiﬁcation performance, particularly in extreme cases such as very anisotropic diffusion. We note that the same technique could be used to produce a ﬁner classiﬁcation of diffusion proﬁles; for example, we could distinguish between axisymmetric (two eigenvalues equal) and nonsymmetric (all eigenvalues unequal), anisotropic Gaussian diffusion.

In the present study we used only data acquired with common clinical imaging parameter settings, and one of

our goals was to demonstrate that signiﬁcant non-Gaussian behavior can be observed at b-values as low as 1000 s/mm2. Recently there has been a trend to move toward higher b-values, which can produce proﬁles richer in information; in particular, non-Gaussian behavior becomes more pronounced (10). Our methods are equally applicable to data acquired with higher b-values, and we would expect to observe a higher proportion of non-Gaussian proﬁles in such data, which may highlight other regions of the brain in which non-Gaussian behavior occurs.

## ACKNOWLEDGMENTS

Gareth Barker is funded by the Multiple Sclerosis Society of Great Britain and Northern Ireland. Thanks to Dr. Claudia Wheeler-Kingshott and Dr. Philip Boulby for pulse sequence development, and to Dr. Olga Ciccarelli for providing data and aiding in the initial interpretation of the results.

## REFERENCES

- 1. Basser PJ, Matiello J, Le Bihan D. MR diffusion tensor spectroscopy and imaging. Biophys J 1994;66:259–267.
- 2. Basser PJ, Pierpaoli C. Microstructural and physiological features of tissues elucidated by quantitative diffusion tensor MRI. J Magn Reson B 1996;111:209–219.
- 3. Pierpaoli C, Jezzard P, Basser PJ, Barnett A, Di Chiro G. Diffusion tensor MR imaging of the human brain. Radiology 1996;201:637–648.
- 4. Callaghan PT. Principles of magnetic resonance microscopy. Oxford, UK: Oxford Science Publications; 1991.
- 5. Karger J, Pfeifer H, Heink W. Principles and applications of self diffusion measurements by nuclear magnetic resonance. Adv Magn Reson 1988;12:1–89.
- 6. Mitra PP, Halperin BI. Effects of ﬁnite gradient pulse widths in pulsed ﬁeld gradient diffusion measurements. J Magn Reson 1995;113:94–101.
- 7. Crank J. The mathematics of diffusion. Oxford, UK: Oxford University Press; 1975.
- 8. Stejskal EO, Tanner JE. Spin diffusion measurements: spin echoes in the presence of time-dependent ﬁeld gradient. J Chem Phys 1965;42: 288–292.

- 9. Jones DK, Horsﬁeld MA, Simmons A. Optimal strategies for measuring diffusion in anisotropic systems by magnetic resonance imaging. Magn Reson Med 1999;42:515–525.
- 10. Alexander AL, Hasan KM, Lazar M, Tsuruda JS, Parker DL. Analysis of partial volume effects in diffusion-tensor MRI. Magn Reson Med 2001; 45:770–780.
- 11. Frank LR. Characterization of anisotropy in high angular resolution diffusion weighted MRI. In: Proceedings of the 9th Annual Meeting of ISMRM, Glasgow, Scotland, 2001. p 1531.
- 12. Tuch DS, Weisskoff RM, Belliveau JW, Wedeen VJ. High angular resolution diffusion imaging of the human brain. In: Proceedings of the 7th Annual Meeting of ISMRM, Philadelphia, 1999. p 321.
- 13. Wedeen VJ, Reese TG, Tuch DS, Weigel MR, Dou J-G, Weisskoff RM, Chesler D. Mapping ﬁber orientation spectra in cerebral white matter with Fourier transform diffusion MRI. In: Proceedings of the 8th Annual Meeting of ISMRM, Denver, 2000. p 82.
- 14. Frank LR. Anisotropy in high angular resolution diffusion-weighted MRI. Magn Reson Med 2001;45:935–939.
- 15. Nikiforov AF, Uvarov VB. Special functions of mathematical physics. Basel: Birkhauser Verlag; 1988.
- 16. Brechbuhler CH, Gerig G, Kubler O. Parametrization of closed surfaces for 3D shape description. Comput Vis Image Underst 1995;61:154–170.
- 17. Armitage P, Berry G. Statistical methods in medical research. Oxford, UK: Blackwell Scientiﬁc Publications; 1971.
- 18. Pajevic S, Pierpaoli C. Color schemes to represent the orientation of anisotropic tissues from diffusion tensor data: application to white matter ﬁber tract mapping in the human brain. Magn Reson Med 1999;42:526–540.
- 19. Armitage PA, Bastin ME. Utilizing the diffusion-to-noise ratio to optimize magnetic resonance diffusion tensor acquisition strategies for improving measurements of diffusion anisotropy. Magn Reson Med 2001;45:1056–1065.
- 20. Alexander DC, Barker GJ, Arridge SR. Detection and modelling of non-Gaussianity in MR diffusion imaging. UCL, Department of Computer Science Research Note, RN/01/35, 2001. http://www.cs.ucl. ac.uk/staff/D.Alexander/Papers/RN35–2001.pdf
- 21. Alexander DC, Jansons KM. Spin echo attenuation to diffusion displacement density: a general inversion for measurements on a sphere. In: Proceedings of the ISMRM Workshop on Diffusion MRI: Biophysical issues (what can we measure?), St. Malo, France, 2002.
- 22. Le Bihan D. Molecular diffusion, tissue microdynamics and microstructure. NMR Biomed 1995;8:375–386.
- 23. Anderson AW. Theoretical analysis of the effects of noise of diffusion tensor imaging. Magn Reson Med 2001;46:1174–1188.

