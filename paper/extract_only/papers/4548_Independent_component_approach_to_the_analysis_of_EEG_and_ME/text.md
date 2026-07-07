IEEE TRANSACTIONS ON BIOMEDICAL ENGINEERING, VOL. 47, NO. 5, MAY 2000 589

Independent Component Approach to the Analysis of EEG and MEG Recordings

Ricardo Vigário*, Jaakko Särelä, Veikko Jousmäki, Matti Hämäläinen, and Erkki Oja

Abstract—Multichannel recordings of the electromagnetic fields emergingfrom neural currents inthe brain generate largeamounts of data. Suitable feature extraction methods are, therefore, useful to facilitate the representation and interpretation of the data.

Recently developed independent component analysis (ICA) has been shown to be an efficient tool for artifact identification and extraction from electroencephalographic (EEG) and magnetoencephalographic (MEG) recordings. In addition, ICA has been applied to the analysis of brain signals evoked by sensory stimuli. This paper reviews our recent results in this field.

Index Terms—Independent component analysis (ICA), blind source separation (BSS), unsupervised learning, electroencephalography (EEG), magnetoencephalography(MEG), artifact removal, auditory evoked field (AEF), somatosensory evoked field (SEF).

I. INTRODUCTION

# W

ITH the advent of new anatomical and functional imaging methods, it is now possible to collect vast

amounts of data from the living human brain. It has thus become very important to extract the essential features from the data to allow an easier representation or interpretation of their properties. Traditional approaches to solve this feature extraction or dimension reduction problem include, e.g., principal component analysis (PCA), projection pursuit, and factor analysis. This paper focuses on a novel signal processing technique, independent component analysis (ICA), which allows blind separation of sources, linearly mixed at the sensors, assuming only the statistical independence of these sources.

Electroencephalograms (EEG) and magnetoencephalograms (MEG) are recordings of electric and magnetic fields of signals emerging from neural currents within the brain. The challenges presented to the signal processing community by the researchers employing EEG and MEG include the identification and removal of artifacts from the recordings and the analysis of the brain signals themselves.

In Section II, we present a short description of the independent component analysis theory, together with an algorithm capable of performing such analysis. In Section III, we validate

Manuscript received June 10, 1999; revised January 6, 2000. Asterisk indicates corresponding author.

*R. Vigário is with the Laboratory of Computer and Information Science, Helsinki University of Technology, P.O. Box 5400, FIN-02015 HUT, Finland (e-mail: Ricardo.Vigario@hut.fi).

J. Särelä and E. Oja are with the Laboratory of Computer and Information Science, Helsinki University of Technology, FIN-02015 HUT, Finland.

V. Jousmäki and M. Hämäläinen are with the Brain Research Unit, Low Temperature Laboratory, Helsinki University of Technology, FIN-02015 HUT, Finland.

Publisher Item Identifier S 0018-9294(00)03276-6.

the application of the ICA model to EEG and MEG. The use of ICA for identification of artifacts in EEG and MEG as well as the decomposition of event-related activity is presented in Section IV.

II. ICA

- A. The Model

ICA [2], [8], [10], [13], [20] is a novel statistical technique that aims at finding linear projections of the data that maximize their mutual independence. Its main applications are in feature extraction [12], [25], and blind source separation (BSS) [2], [8], with special emphasis to physiological data analysis [29], [31], [33], [19], [3], [23], [34], [17], and audio signal processing [28].

As in many other linear transformations, it is assumed that at time instant the observed -dimensional data vector,

[Figure 1]

[Figure 2]

[Figure 3]

[Figure 4]

[Figure 5]

[Figure 6]

[Figure 7]

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

[Figure 18]

[Figure 19]

[Figure 20]

[Figure 21]

[Figure 22]

[Figure 23]

[Figure 24]

is given by the model

[Figure 25]

[Figure 26]

[Figure 27]

[Figure 28]

[Figure 29]

[Figure 30]

[Figure 31]

[Figure 32]

[Figure 33]

[Figure 34]

[Figure 35]

[Figure 36]

[Figure 37]

[Figure 38]

[Figure 39]

[Figure 40]

[Figure 41]

[Figure 42]

[Figure 43]

[Figure 44]

[Figure 45]

[Figure 46]

[Figure 47]

[Figure 48]

(1)

The source signals, , are supposed to be stationary, independent and, together with the coefficients of the mixing matrix , unknown. The goal is to estimate both unknowns from , with appropriate assumptions on the statistical properties of the source distributions. The solution is sought in the form

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

[Figure 86]

[Figure 87]

[Figure 88]

[Figure 89]

(2) where is called the separating matrix.

[Figure 90]

The general BSS problem requires to be an matrix of full rank, with (i.e., there are at least as many mixtures as the number of independent sources). In most algorithmic derivations, an equal number of sources and sensors is assumed. Furthermore, only up to one source may be Gaussian.

[Figure 91]

[Figure 92]

[Figure 93]

[Figure 94]

[Figure 95]

[Figure 96]

[Figure 97]

In model (1), schematically illustrated in Fig. 1, we omit additive noise; some analysis of the noisy model can be found in [16] and [30].

- B. The FastICA Algorithm

In the FastICA algorithm, to be described below, the initial step is whitening or sphering. By a linear transformation, the measurements and , for all , are made uncorrelated and unit-variance [14]. The whitening facilitates the separation of the underlying independent signals [21]. In [15], it has been shown that a well-chosen compression, during this stage, may be necessary in order to reduce the overlearning (overfitting), typical of ICA methods. The result of a poor compression

[Figure 98]

[Figure 99]

[Figure 100]

[Figure 101]

[Figure 102]

[Figure 103]

[Figure 104]

[Figure 105]

[Figure 106]

[Figure 107]

0018–9294/0$10.00 © 2000 IEEE

[Figure 108]

- Fig. 1. Schematical illustration of the mathematical model used to perform the ICA decomposition.

Consider a linear combination of a white random vector , with . Then and

[Figure 109]

[Figure 110]

[Figure 111]

[Figure 112]

[Figure 113]

[Figure 114]

[Figure 115]

[Figure 116]

[Figure 117]

[Figure 118]

[Figure 119]

[Figure 120]

[Figure 121]

[Figure 122]

[Figure 123]

[Figure 124]

[Figure 125]

[Figure 126]

[Figure 127]

[Figure 128]

[Figure 129]

[Figure 130]

[Figure 131]

[Figure 132]

, whose gradient with respect to is .

[Figure 133]

[Figure 134]

[Figure 135]

[Figure 136]

[Figure 137]

[Figure 138]

[Figure 139]

[Figure 140]

[Figure 141]

[Figure 142]

[Figure 143]

[Figure 144]

[Figure 145]

[Figure 146]

[Figure 147]

[Figure 148]

[Figure 149]

[Figure 150]

[Figure 151]

The FastICA [14] is a fixed point algorithm which, maximizing the absolute value of the kurtosis, finds one of the columns of the separating matrix (noted ) and so identifies one independent source at a time. The corresponding independent source signal can then be found using (4). Each

[Figure 152]

[Figure 153]

th iteration of this algorithm is defined as

[Figure 154]

choice is the production of solutions practically zero almost everywhere, except at the point of a single spike or bump. In the studies reported in this paper, the number of important sources (both in the artifact detection and the averaged evoked response experiments) is assumed to be smaller than the total amount of sensors used, justifying such signal compression.

The whitening may be accomplished by PCA projection: , with . The whitening matrix is given by , where

[Figure 155]

[Figure 156]

[Figure 157]

[Figure 158]

[Figure 159]

[Figure 160]

[Figure 161]

[Figure 162]

[Figure 163]

[Figure 164]

[Figure 165]

[Figure 166]

[Figure 167]

[Figure 168]

[Figure 169]

[Figure 170]

[Figure 171]

[Figure 172]

[Figure 173]

[Figure 174]

[Figure 175]

[Figure 176]

[Figure 177]

[Figure 178]

[Figure 179]

[Figure 180]

[Figure 181]

[Figure 182]

[Figure 183]

[Figure 184]

[Figure 185]

[Figure 186]

[Figure 187]

is a diagonal matrix with the eigenvalues of the data covariance matrix , and is a matrix with the corresponding eigenvectors as its columns. The transformed vectors are called white or sphered, because all directions have equal unit variance.

[Figure 188]

[Figure 189]

[Figure 190]

[Figure 191]

[Figure 192]

[Figure 193]

[Figure 194]

[Figure 195]

[Figure 196]

[Figure 197]

[Figure 198]

[Figure 199]

[Figure 200]

[Figure 201]

[Figure 202]

[Figure 203]

[Figure 204]

[Figure 205]

[Figure 206]

[Figure 207]

[Figure 208]

[Figure 209]

[Figure 210]

[Figure 211]

[Figure 212]

[Figure 213]

[Figure 214]

[Figure 215]

[Figure 216]

[Figure 217]

[Figure 218]

[Figure 219]

[Figure 220]

[Figure 221]

[Figure 222]

[Figure 223]

[Figure 224]

In terms of , the model (1) becomes

[Figure 225]

[Figure 226]

[Figure 227]

[Figure 228]

[Figure 229]

[Figure 230]

[Figure 231]

[Figure 232]

[Figure 233]

[Figure 234]

[Figure 235]

[Figure 236]

[Figure 237]

[Figure 238]

(3)

and we can show that matrix is orthogonal [7]. Therefore, the solution is now sought in the form:

[Figure 239]

[Figure 240]

[Figure 241]

[Figure 242]

[Figure 243]

[Figure 244]

[Figure 245]

[Figure 246]

[Figure 247]

[Figure 248]

[Figure 249]

[Figure 250]

[Figure 251]

[Figure 252]

[Figure 253]

[Figure 254]

[Figure 255]

(4)

Uncorrelation and independence are equivalent concepts in the case of Gaussian distributed signals. PCA is therefore sufficient for finding independent components. However, standard PCA is not suited for dealing with non-Gaussian data, where independence is a more restrictive requirement than uncorrelation. Several authors have shown [20], [10], [5], [9], [13] that higher-order statistics are required to deal with the independence criterion.

According to the Central Limit Theorem (CLT), the sum of independent random variables, with identical distribution functions approaches the normal distribution as tends to infinity [26]. We may thus replace the problem of finding the independent source signals by a suitable search for linear combinations of the mixtures that maximize a certain measure of non-Gaussianity.

[Figure 256]

[Figure 257]

In FastICA, as in many other ICA algorithms, we use the fourth-order cumulant also called the kurtosis. For the th source signal, the kurtosis is defined as

[Figure 258]

. denotes the mathematical expectation value of the bracketed quantity. The kurtosis is negative for source signals whose amplitude has sub-Gaussian probability densities (distributions flatter than Gaussian), positive for super-Gaussian (sharper than Gaussian), and zero for Gaussian densities. Maximizing the norm of the kurtosis leads to the identification of non-Gaussian sources.

[Figure 259]

[Figure 260]

[Figure 261]

[Figure 262]

[Figure 263]

[Figure 264]

[Figure 265]

[Figure 266]

[Figure 267]

[Figure 268]

[Figure 269]

[Figure 270]

[Figure 271]

[Figure 272]

[Figure 273]

[Figure 274]

[Figure 275]

[Figure 276]

[Figure 277]

[Figure 278]

[Figure 279]

[Figure 280]

[Figure 281]

[Figure 282]

[Figure 283]

[Figure 284]

[Figure 285]

[Figure 286]

[Figure 287]

[Figure 288]

[Figure 289]

[Figure 290]

[Figure 291]

[Figure 292]

[Figure 293]

[Figure 294]

[Figure 295]

[Figure 296]

[Figure 297]

[Figure 298]

[Figure 299]

[Figure 300]

[Figure 301]

[Figure 302]

[Figure 303]

[Figure 304]

[Figure 305]

[Figure 306]

[Figure 307]

[Figure 308]

[Figure 309]

[Figure 310]

[Figure 311]

[Figure 312]

[Figure 313]

[Figure 314]

[Figure 315]

[Figure 316]

[Figure 317]

[Figure 318]

[Figure 319]

[Figure 320]

[Figure 321]

[Figure 322]

[Figure 323]

[Figure 324]

(5)

In order to estimate more than one solution, and up to a maximum of , the algorithm may be run repeatedly. It is, nevertheless, necessary to remove the information contained in the solutions already found, to estimate a different independent component each time. For details, see [14].

[Figure 325]

All studies reported in this paper were carried out using MATLAB code, based on the FastICA package [1].

III. VALIDATING THE ICA MODEL IN ELECTROENCEPHALOGRAPHY (EEG)/MAGNETOENCEPHALOGRAPHY (MEG)

The application of ICA to the study of EEG and MEG signals assumes that several conditions are verified: the existence of statistically independent source signals, their instantaneous linear mixing at the sensors, and the stationarity of both the source signals and the mixing process.

The independence criterion applies solely to the statistical relations between the amplitude distributions of the signals involved, and not to considerations upon the morphology or physiology of certain neural structures. However, the different nature of the sources of the artifacts from those of the actual brain signals has been the driving thought to the application of ICA to the removal of artifacts from EEG and MEG. Analysis of the distributions of artifacts such as the cardiac cycle, ocular activity or a digital watch has shown the statistical independence approximation to be accurate.

Furthermore, often the search for independent components can be replaced by a search for maximally non-Gaussian linear transformations of the data. Typically, the artifacts encountered, as well as the different components in evoked field studies, present clear non-Gaussian distributions. Although the direct independence criterion may sometimes be difficult to justify, the ICA model may still be useful.

Rhythmic activity in the brain poses a different problem. In fact, pure oscillatory activity has negative kurtosis. Yet in reality this neural activity often comes as bursts of limited time span. Depending on the length of these bursts, the sign of the kurtosis may be positive. In the worst case, the global kurtosis may even be zero, i.e., the desired component is then interpreted as Gaussian. An illustration of the changes in kurtotic behavior is shown in Fig. 2, where a sinusoidal signal is masked with Gaussian windows of different durations. A different strategy may be required to cope with this problem, such as using methods based on the time correlation in the data [4], [35].

[Figure 326]

- Fig. 2. Changes in kurtotic behavior of bursts of oscillatory signals, as a function of the duration of the burst.

[Figure 327]

- Fig. 3. A subset of 12 spontaneous MEG signals from the frontal, temporal and occipital areas. The data contains several types of artifacts, including ocular andmuscle activity,the cardiaccycle,and environmentalmagneticdisturbances. Adapted from [29].

Because most of the energy in EEG and MEG signals lies below 1 kHz, the quasistatic approximation of Maxwell equations holds, and each time instance can be considered separately [11]. Therefore, there is no need for introducing any time-delays, and the instantaneous mixing model is valid. The linearity of the mixing follows from the Maxwell’s equations as well.

The nonstationarity of EEG and MEG signals is well documented [6]. When considering the underlying source signals as stochastic processes, the requirement of stationarity is in theory necessary to guarantee the existence of a representative (nonGaussian) distribution of the sources. Yet, in the implementation of the batch FastICA algorithm, the data are considered as random variables, their distributions estimated from the whole data set. This removes the strict requirement of stationarity.

The stationarity of the mixing process corresponds to the existence of a constant mixing matrix . In the dipole source model used throughout this paper, the mixing stationarity leads to the existence of sources with fixed locations and orientations, with amplitude varying with time. Such models [27], [24] have been extensively and efficiently used in the analysis of MEG data, which justifies the use of constant mixing vectors in our ICA model.

[Figure 328]

[Figure 329]

[Figure 330]

IV. THE ANALYSIS OF EEG AND MEG DATA

- A. Artifact Identification and Removal from EEG/MEG

When performing EEG or MEG measurements, physicians have often to deal with considerable amounts of artifacts, that may render impossible the extraction of valuable information

[Figure 331]

- Fig. 4. Six independent components extracted from the MEG data containing several artifacts. For each component the left, back and right views of the field patterns are shown. Full lines stand for magnetic flux coming from the head, and dotted lines the flux inwards. Adapted from [29].

[Figure 332]

(a) (b) (c) (d)

[Figure 333]

(e)

- Fig. 5. Results of the application of FastICA to averaged brain MEG responses to a vibrotactile stimulation. (a)-(c) present, respectivelly, a sample of the original MEG data, the whitened and the independent signals. Each tick corresponds to a time interval of 100 ms. (e) shows the field patterns associated with the first two independent components, and the localization of IC1 and IC2 superimposed onto an MRI scan.

[Figure 334]

Fig. 6. Principal (a) and independent (b) components found on the auditory evoked field study. Each tick in (a) and (b) corresponds to 100 ms, going from 100 ms before stimulation onset to 500 ms after. In (c) and (d), the four IC’s are plotted after scaling to one left and right MEG original signal.

therein. The amplitude of an artifact may well exceed that of brain signals, thus obscuring the brain activity. Moreover, many artifacts resemble the neural responses, leading to a misinterpretation of the resulting data. Typical artifacts, present in many EEG and MEG measurements, include eye and muscle activity, the activity of the heart, and environmental electric and magnetic disturbances.

Recent research on artifact identification in EEG and MEG recordings, using ICA, has been reported in, e.g., [19], [29], and [31]. Fig. 3 presents a subset of 12 MEG signals, from a total of 122 used in the experiment. Several artifact structures are evident, such as eye and muscle activity. These can be extracted using ICA, as shown in Fig. 4 (IC1 and IC2 are clearly activation of two different muscle sets, whereas IC3 and IC5 are, respectively, horizontal eye movements and blinks). Furthermore, other disturbances with weaker signal-to-noise ratio, such as the heart beat and a digital watch, are as well extracted (IC4 and IC5, respectively). For each component the left, back and right views of the field patterns are shown. These field patterns are given by the corresponding mixing vector .

[Figure 335]

[Figure 336]

- B. Multimodal Event-Related Components

The application of ICA in studies of event-related brain activity was first introduced in the blind separation of auditory evoked potentials in [22]. This method was further developed for the analysis of magnetic auditory and somatosensory evoked fields (AEFs and SEF’s, respectively) in [33] and [32]. We will review here the most relevant results obtained in our studies.

Most of the time we are combining information from several sensory systems to perceive the world. In this example, we show how ICA can be used to analyze responses to simultaneous somatosensory and auditory stimulation. Vibrotactile stimuli were presented to the subject via a balloon, coupled to a loudspeaker through atube. Both tactile andthe concomitant auditory stimuli were thus present [18], [32]. The results of an ICA for these data are shown in Fig. 5.

The evoked responses elicited by the two stimuli peak at different latencies, which is already evident from the signals at some MEG channels, as shown in Fig. 5(a). The somatosensory signal peaks at around 60 ms after the stimulus onset, whereas

the auditory peaks later, around 110 ms. Nevertheless, in most of the recorded signals this separation is far from complete. Fig. 5(b) shows the results obtained after whitening (PCA projection),where we can seethat themixing is still present.In 5(c), auditory and somatosensory responses are clearly separated in the first two independent components. The corresponding field patterns in Fig. 5(d), together with the superimposition of the corresponding dipolar sources on MRI slices in 5(e), agree with results obtained by conventional methods for this type of brain responses.

C. Segmenting Auditory Evoked Fields

A final experiment, using only averaged auditory evoked fields, illustrated the decomposition capabilities of ICA in such setups. The stimuli consisted of 200 tone bursts that were presented to the subject’s right ear, using 1s interstimulus interval. These bursts had a duration of 100 ms, and a frequency of 1 KHz [33].

As in the previous experiment, we can see from Fig. 6(a) and (b) that PCA is unable to resolve the complex brain response, whereas the new ICA technique produces cleaner and sparser responses. From Fig. 6(c) and (d), it is visible that IC1 and IC2 correspond to responses typically labeled as N1m, with the characteristic latency of around 100 ms after the onset of the stimulation. IC1, with a shorter latency, is particularly strong in the left hemisphere, as can be seen in 6(c). Conversely, IC2 is nearly solely responsible for the N1m component in the right hemisphere. Another component, IC4, exhibiting a longer latency (around 180 ms), fully explains the later responses in the contra-lateral brain hemisphere (see [33] for the field patterns associated to these IC’s).

V. CONCLUDING REMARKS

In this paper, we have shown examples of ICA in the analysis of biomagnetic brain signals. A special emphasis has been given to the justification of the ICA model for EEG and MEG signals.

The FastICA algorithm is suitable for extracting different types of artifacts from EEG and MEG data, even in situations where these disturbances are smaller than the background brain activity.

ICA has shown to be able to differentiate between somatosensory and auditory brain responses in the case of vibrotactile stimulation. In addition, the independent components, found with no other modeling assumption than their statistical independence, exhibit field patterns that agree with the conventional current dipole models. The equivalent current dipole sources corresponding to the independent components fell on the brain regions expected to be activated by the particular stimulus.

Finally, we have shown that the application of ICA to an averaged auditory evoked response nicely isolates the main response, with alatency of about100 ms, from subsequentcomponents. Furthermore, it discriminates between the ipsi- and contralateral principal responses in the brain. ICA may thus facilitate the understanding of the functioning of the human brain, as a finer mapping of the brain’s responses may be achieved.

REFERENCES

- [1] FastICA MATLAB Package [Online]. Available: HTTP: http://www.cis.hut.fi/projects/ica/fastica
- [2] S. Amari and A. Cichocki, “Adaptive blind signal processing—Neural network approaches,” Proc. IEEE, vol. 86, pp. 2026–2048, Oct. 1998.
- [3] A. K. Barros, A. Mansour, and N. Ohnishi, “Adaptive blind elimination of artifacts in ECG signals,” in Proc. 1998 Workshop on Independence and Artificial Neural Networks, Tenerife, Spain, 1998, pp. 1380–1386.
- [4] A. K. Barros, R. Vigário, V. Jousmäki, and N. Ohnishi, “Extraction of periodic signals from multi-channel bioelectrical measurements,” IEEE Trans. Biomed. Eng., vol. 47, pp. 583–588, May 2000.
- [5] A. Bell and T. Sejnowski, “An information-maximization approach to blind separation and blind deconvolution,” Neural Computation, vol. 7, pp. 1129–1159, 1995.
- [6] S. Blanco, H. Garcia, R. Q. Quiroga, L. Romanelli, and O. A. Rosso, “Stationarity of the EEG series,” IEEE Eng. Med. Biol., pp. 395–399, 1995.
- [7] J.-F. Cardoso, “Source separation using higher oerder moments,” in Proc. 1989 IEEE Int. Conf. Acoustics, Speech, and Signal Processing (ICASSP’89), Glasgow, Scotland, 1989, pp. 2109–2112.
- [8] , “Blind signal separation: Statistical principles,” Proc. IEEE, vol. 86, pp. 2009–2025, Oct. 1998.

- [9] , “High-order contrasts for independent component analysis,” Neural Computation, vol. 11, pp. 157–192, 1999.

- [10] P. Comon, “Independent component analysis—A new concept?,” Signal Processing, vol. 36, pp. 287–314, 1994.
- [11] M. Hämäläinen, R. Hari, R. Ilmoniemi, J. Knuutila, and O. V. Lounasmaa, “Magnetoencephalography—Theory, instrumentation, and applications to noninvasive studies of the working human brain,” Rev. Modern Phys., vol. 65, no. 2, pp. 413–497, 1993.
- [12] J. Hurri, A. Hyvärinen, J. Karhunen, and E. Oja, “Image feature extraction using independent component analysis,” in Pro. 1996 IEEE Nordic Signal Processing Symp. NORSIG’96, Espoo, Finland, 1996, pp. 475–478.
- [13] A. Hyvärinen, “Survey on independent component analysis,” Neural Computing Surveys, vol. 2, pp. 94–128, 1999.
- [14] A. Hyvärinen and E. Oja, “A fast fixed-point algorithm for independent componentanalysis,” Neural Computation, vol. 9,pp. 1483–1492, 1997.
- [15] A. Hyvärinen, J. Särelä, and R. Vigário, “Spikes and bumps: Artefacts generated by independent component analysis with insufficient sample size,” presented at the Int. Workshop on Independent Component Analysis and Blind Separation of Signals (ICA’99), Aussois, France, 1999.

- [16] A. Hyvärinen, “Gaussian moments for noisy independent component analysis,” IEEE Signal Processing Lett., vol. 6, no. 6,pp. 145–147, 1999.
- [17] O. Jahn and A. Cichocki, “Identification and elimination of artifacts from MEG signals using efficient independent components analysis,” presented at the 11th Int. Conf. on Biomagnetism BIOMAG-98, Sendai, Japan, 1998.
- [18] V. Jousmäki and R. Hari, “Somatosensory evoked fields to large-area vibrotactile stimuli,” Clin. Neurophysiol., vol. 110, pp. 905–909, 1999.
- [19] T.-P. Jung, C. Humphries, T.-W. Lee, S. Makeig, M. J. McKeown, V. Iragui, and T. Sejnowski, “Extended ICA removes artifacts from electroencephalographic recordings,” presented at the Neural Information Processing Systems 10 (Proc. NIPS’97), 1998.
- [20] C. Jutten and J. Herault, “Blind separation of sources, part I: An adaptive algorithm based on neuromimetic architecture,” Signal Processing, vol. 24, pp. 1–10, 1991.
- [21] J. Karhunen, E. Oja, L. Wang, R. Vigário, and J. Joutsensalo, “A class of neural networks for independent component analysis,” IEEE Trans. Neural Networks, vol. 8, no. 3, pp. 486–504, 1997.
- [22] S. Makeig, T.-P. Jung, A. Bell, D. Ghahremani, and T. Sejnowski, “Blind separation of auditory event-related brain responses into independent components,” Proc. Nat. Acad. Sci. USA, vol. 94, pp. 10979–10984, 1997.
- [23] M. McKeown, S. Makeig, S. Brown, T.-P. Jung, S. Kindermann, A. Bell, V. Iragui, and T. Sejnowski, “Blind separation of functional magnetic resonance imaging (fMRI) data,” Human Brain Mapping, vol. 6, no. 5–6, pp. 368–372, 1998.
- [24] J. Mosher, P. Lewis, and R. Leahy, “Multidipole modeling and localization from spatio-temporal MEG data,” IEEE Trans. Biomed. Eng., vol. 39, pp. 541–557, 1992.
- [25] B. A. Olshausen and D. J. Field, “Emergence of simple-cell receptive field properties by learning a sparse code for natural images,” Nature, vol. 381, pp. 607–609, 1996.
- [26] A. Papoulis, Probability, Random Variables, and Sochastic Processes (Electrical & Electronic Engineering), 3rd ed, Singapore: McGraw-Hill, 1991.
- [27] M. Scherg and D. von Cramon, “Two bilateral sources of the late AEP as identified by a spatio-temporal dipole model,” Electroenceph. Clin. Neurophysiol, vol. 62, pp. 32–44, 1985.
- [28] K. Torkkola, “Blind separation for audio signals: Are we there yet?,” presented at the Int. Workshop on Independent Component Analysis and Blind Separation of Signals (ICA’99), Aussois, France, 1999.
- [29] R. Vigário, “Extraction of ocular artifacts from EEG using independent component analysis,” Electroenceph. Clin. Neurophysiol., vol. 103, pp. 395–404, 1997.
- [30] , “Independent Component Approach to the Analysis of EEG and MEG Recordings,” Ph.D. dissertation, Helsinki Univ. Technol., Helsinki, Finland, 1999.

- [31] R. Vigário, V. Jousmäki, M. Hämäläinen, R. Hari, and E. Oja, “Independent component analysis for identification of artifacts in magnetoencephalographic recordings,” in Neural Information Processing Systems 10 (Proc. NIPS’97), M. I. Jordan, M. J. Kearns, and S. A. Solla, Eds. Cambridge, MA: MIT Press, 1998.
- [32] R. Vigário, J. Särelä, V. Jousmäki, and E. Oja, “Independent component analysis in decomposition of auditory and somatosensory evoked fields,” presented at the Int. Workshop on Independent Component Analysis and Blind Separation of Signals (ICA’99), Aussois, France, 1999.
- [33] R. Vigário, J. Särelä, and E. Oja, “Independent component analysis in wave decomposition of auditory evoked fields,” presented at the Int. Conf. on Artificial Neural Networks (ICANN’98), Skövde, Sweden, 1998.
- [34] A. Ziehe, K. Müller, G. Nolte, B.-M. Mackert, and G. Curio, “Artifact reduction in magnetoneurography based on time-delayed second-order correlations,” IEEE Trans. Bimed. Eng., vol. 47, pp. 75–87, Jan. 2000.
- [35] A. Ziehe and K.-R. Müller, “TDSEP—An effective algrithm for blind separation using time structure,” in Proc. Int. Conf. Artificial Neural Networks (ICANN’98), Skövde, Sweden, 1998, pp. 675–680.

