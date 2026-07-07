arXiv:1610.02365v1[physics.optics]7Oct2016

# Deep Learning with Coherent Nanophotonic Circuits

Yichen Shen1∗, Nicholas C. Harris1∗, Scott Skirlo1, Mihika Prabhu1, Tom Baehr-Jones2, Michael Hochberg2, Xin Sun3, Shijie Zhao4, Hugo Larochelle5, Dirk Englund1, and Marin Soljačić1

1Research Laboratory of Electronics, Massachusetts Institute of Technology, Cambridge, MA 02139, USA 2Coriant Advanced Technology, 171 Madison Avenue, Suite 1100, New York, NY 10016, USA

- 3Department of Mathematics, Massachusetts Institute of Technology, Cambridge, MA 02139, USA
- 4Department of Biology, Massachusetts Institute of Technology, Cambridge, MA 02139, USA 5Twitter Inc., 141 Portland St, Cambridge, MA 02139, USA

#### These authors contributed equally to this work.

Artiﬁcial Neural Networks are computational network models inspired by signal processing in the brain. These models have dramatically improved the performance of many learning tasks, including speech and object recognition. However, today’s computing hardware is ineﬃcient at implementing neural networks, in large part because much of it was designed for von Neumann computing schemes. Signiﬁcant eﬀort has been made to develop electronic architectures tuned to implement artiﬁcial neural networks that improve upon both computational speed and energy eﬃciency. Here, we propose a new architecture for a fully-optical neural network that, using unique advantages of optics, promises a computational speed enhancement of at least two orders of magnitude over the state-of-the-art and three orders of magnitude in power eﬃciency for conventional learning tasks. We experimentally demonstrate essential parts of our architecture using a programmable nanophotonic processor.

Modern computers based on the von Neumann architecture are far more power-hungry and less eﬀective than their biological counterparts – central nervous systems – for a wide range of tasks including perception, communication, learning, and decision making. With the increasing data volume associated with processing big data, developing computers that learn, combine, and analyze vast amounts of information quickly and eﬃciently is becoming increasingly important. For example, speech recognition software (e.g., Apple’s Siri) is typically executed in the cloud since these computations are too taxing for mobile hardware; realtime image processing is an even more demanding task [1]. To address the shortcomings of von Neumann computing architectures for neural networks, much recent work has focused on increasing artiﬁcial neural network computing speed and power eﬃciency by developing electronic architectures (such as ASIC and FPGA chips) speciﬁcally tailored to a task [2–5]. Recent demonstrations of electronic neuromorphic hardware architectures have reported improved computational performance [6]. Hybrid optical-electronic systems that implement spike processing [7–9] and reservoir computing [10, 11] have also been investigated recently. However, the computational speed and power eﬃciency achieved with these hardware architectures are still limited by electronic clock rates and ohmic losses.

Fully-optical neural networks oﬀer a promising alternative approach to microelectronic and hybrid optical-electronic implementations. Linear transformations (and certain nonlinear transformations) can be performed at the speed of light and detected at rates exceeding 100 GHz [12] in photonic networks, and in some cases, with minimal power consumption [13]. For example, it is well known that a common lens performs Fourier transform without any power

consumption, and that certain matrix operations can also be performed optically without consuming power. However, implementing such transformations with bulk optical components (such as ﬁbers and lenses) has been a major barrier because of the need for phase stability and large neuron counts. Integrated photonics solves this problem by providing a scalable solution to large, phase-stable optical transformations [14].

Here, we experimentally demonstrate on-chip, coherent, optical neuromorphic computing on a vowel recognition dataset. We achieve a level of accuracy comparable to a conventional digital computer using a fully connected neural network algorithm. We show that, under certain conditions, the optical neural network architecture can be at least two orders of magnitude faster for forward propagation while providing linear scaling of neuron number versus power consumption. This feature is enabled largely by the fact that photonics can perform matrix multiplications, a major part of nerual network algorithms, with extreme energy eﬃciency. While implementing scalable von Neumann optical computers has proven challenging, artiﬁcial neural networks implemented in optics can leverage inherent properties, such their weak requirements on nonlinearities, to enable a practical, all-optical computing application. An optical neural network architecture can be substantially more energy eﬃcient than conventional artiﬁcial neural networks implemented on current electronic computers.

#### OPTICAL NEURAL NETWORK DEVICE ARCHITECTURE

An artiﬁcial neural network (ANN) [15] consists of a set of input artiﬁcial neurons (represented as circles in Fig. 1(a))

- a
- b
- c

h(i) = f(Z(i))

###### Z(1) = W0X

Y = Wnh(n)

- X1

- X2

- X3

- X4

- Y1

- Y2

- Y3

- Y4

- h1

(1)

- h2

(1)

- h3

(1)

- h4

- h1

(i)

- h2

(i)

- h3

(i)

- h4

- h1

(n)

- h2

(n)

- h3

(n)

- h4

(1)

(i)

(n)

Input Layer

Output Layer

Hidden Layers

Input Optical Signal

Output Result

X Layer 1 Y

Layer i Layer n

| | |
|---|---|
| | |
| | |
| | |
|Unit| |

0 0

0 0

xin xout

Vˆ   Uˆ

h

Optical Interference Unit Optical Nonlinearity

Waveguide

- FIG. 1. General Architecture of Optical Neural Network a. General artiﬁcial neural network architecture composed of an input layer, a number of hidden layers, and an output layer. b. Decomposition of the general neural network into individual layers. c. Optical interference and nonlinearity units that compose each layer of the artiﬁcial neural network.

connected to at least one hidden layer and an output layer. In each layer (depicted in Fig. 1(b)), information propagates by linear combination (e.g. matrix multiplication) followed by the application of a nonlinear activation function. ANNs can be trained by feeding training data into the input layer and then computing the output by forward propagation; weighting parameters in each matrix are subsequently optimized using back propagation [16].

The Optical Neural Network (ONN) architecture is depicted in Fig. 1 (b,c). As shown in Fig. 1(c), signals are encoded in the amplitude of optical pulses propagating in integrated photonic waveguides where they pass through an optical interference unit (OIU) and ﬁnally an optical nonlinearity unit (ONU). Optical matrix multiplication is implemented with an OIU and nonlinear activation is realized with an ONU.

To realize an OIU that can implement any real-valued matrix, we use the singular value decomposition (SVD) [17] since a general, real-valued matrix (M) may be decomposed as M = UΣV∗, where U is an m × m unitary matrix, Σ is a m × n diagonal matrix with non-negative real numbers on the diagonal, and V∗ is the complex conjugate of the n × n unitary matrix V. It was theoretically shown that any unitary transformations U,V∗ can be implemented with optical beamsplitters and phase shifters [18, 19]. Matrix multipli-

cation implemented in this manner consumes, in principle, no power. The fact that a major part of ANN calculations involves matrix products enables the extreme energy eﬃciency of the ONN architecture presented here. Finally, Σ can be implemented using optical attenuators; optical ampliﬁcation materials such as semiconductors or dyes could also be used [20].

The ONU can be implemented using optical nonlinearities such as saturable absorption [21–23] and bistability [24–28] that have been demonstrated seperately in photonic circuits. For an input intensity Iin, the optical output intensity is thus given by a nonlinear function Iout = f(Iin) [29].

#### EXPERIMENT

For an experimental demonstration of our ONN architecture, we implement a two layer, fully connected neural network with the OIU shown in Fig. 2 and use it to perform vowel recognition. To prepare the training and testing dataset, we use 360 datapoints that each consist of four log area ratio coeﬃcients [30] of one phoneme. The log area ratio coeﬃcients, or feature vectors, represent the power contained in diﬀerent logarithmically-spaced frequency bands and are derived by computing the Fourier transform of the

[Figure 1]

- FIG. 2. Illustration of Optical Interference Unit a. Optical micrograph of an experimentally fabricated 22-mode on-chip optical interference unit; the physical region where the optical neural network program exists is highlighted in grey. The system acts as an optical ﬁeld-programmable gate array–a test bed for optical experiments. b. Schematic illustration of the optical neural network program demonstrated here which realizes both matrix multiplication and ampliﬁcation fully optically. c. Schematic illustration of a single phase shifter in the Mach-Zehnder Interferometer (MZI) and the transmission curve for tuning the internal phase shifter of the MZI.

voice signal multiplied by a Hamming window function. The 360 datapoints were generated by 90 diﬀerent people speaking 4 diﬀerent vowel phonemes [31]. We use half of these datapoints for training and the remaining half to test the performance of the trained ONN. We train the matrix parameters used in the ONN with the standard back propagation algorithm using stochastic gradient descent method [1], on a conventional computer. Further details on the dataset and backpropagation procedure are included in Supplemental Information Section 3.

The coherent ONN is realized with a programmable nanophotonic processor [14] composed of an array of 56 Mach-Zehnder interferometers (MZIs) and 213 phase shifting elements, as shown in Fig. 2. Each interferometer is composed of two evanescent-mode waveguide couplers sandwiching an internal thermo-optic phase shifter [32] to control the splitting ratio of the output modes, followed by a second modulator to control the relative phase of the output modes. By controlling the phase imparted by these

two phase shifters, these MZIs perform all rotations in the SU(2) Lie group given a controlled incident phase on the two electromagnetic input modes of the MZI. The nanophotonic processor was fabricated in a silicon-on-insulator photonics platform with the OPSIS Foundry [33].

To experimentally realize arbitrary matrices by SVD, we programmed an SU(4) core [18, 34] and a non-unitary diagonal matrix multiplication core (DMMC) into the nanophotonic processor [14, 32], as shown in Fig. 2 (b). The SU(4) core implements operators U and V by a Givens rotations algorithm [18, 34] that decomposes unitary matrices into sets of phase shifters and beam splitters, while the DMMC implements Σ by controlling the splitting ratios of the DMMC interferometers to add or remove light from the optical mode relative to a baseline amplitude. The measured ﬁdelity for the 720 OIU and DMMC cores used in the experiment was 99.8 ± 0.003 %; see methods for further detail.

In this analog computer, ﬁdelity is limited by practical non-idealities such as (1) ﬁnite precision with which an op-

tical phase can be set using our custom 240-channel voltage supply with 16-bit voltage resolution per channel (2) photodetection noise, and (3) thermal cross-talk between phase shifters which eﬀectively reduces the number of bits of resolution for setting phases. As with digital ﬂoating-point computations, values are represented to some number of bits of precision, the ﬁnite dynamic range and noise in the optical intensities causes eﬀective truncation errors. A detailed analysis of ﬁnite precision and low-ﬂux photon shot noise is presented in Supplement Section 1.

In this proof-of-concept demonstration, we implement the

nonlinear transformation Iout = f(Iin) in the electronic domain, by measuring optical mode output intensities on a

photodetector array and injecting signals Iout into the next stage of OIU. Here, f models the mathematical function associated with a realistic saturable absorber (such as a dye, semiconductor or graphene saturable absorber or saturable ampliﬁer) that could, in future implementations, be directly integrated into waveguides after each OIU stage of the circuit. For example, graphene layers integrated on nanophotonic waveguides have already been demonstrated as saturable absorbers [35]. Saturable absorption is modeled as [21] (Supplement Section 2),

ln(Tm/T0) 1 − Tm

- 1

- 2

, (1)

στsI0 =

where σ is the absorption cross section, τs is the radiative lifetime of the absorber material, T0 is the initial transmittance (a constant that only depends on the design of saturable absorbers), I0 is the incident intensity, and Tm is the transmittance of the absorber. Given an input intensity I0, one can solve for Tm(I0) from Eqn. 1, and the output intensity can be calculated as Iout = I0 · Tm(I0). A plot of the saturable absorber’s response function Iout(Iin) is shown in supplement Section 2.

After programming the nanophotonic processor to implement our ONN architecture, which consist of 4 layers of OIUs with 4 neurons on each layer (which requires training a total of 4 · 6 · 2 = 48 phase shifter settings), we evaluated it on the vowel recognition test set. Our ONN correctly identiﬁed 138/180 cases (76.7%) [36] compared to a simulated correctness of 165/180 (91.7%).

Since our ONN processes information in the analog signal domain, the architecture can be vulnerable to computational errors. Photodetection and phase encoding are the dominant sources of error in the ONN presented here (as discussed above). To understand the role of phase encoding noise and photodection noise in our ONN hardware architecture and to develop a model for its accuracy, we numerically simulate the performance of our trained matrices with varying degrees of phase encoding noise (σΦ) and photodection noise (σD) (detailed simulation steps can be found in methods section). The distribution of correctness percentage vs σΦ and σD is shown in Fig. 3 (a), which serves as a guide to understanding experimental performance of the ONN. Improvements to the control and readout hardware, includ-

ing implementing higher precision analog-to-digital converters in the photodetection array and voltage controller, are practical avenues towards approaching the performance of digital computers. Well-known techniques can be applied to engineer the photodiode array to achieve signiﬁcantly higher dynamic range; for example, using logarithmic or multi-stage gain ampliﬁers. Addressing these managable engineering problems can further enhance the correctness performance of the ONN to ultimately achieve correctness percentages approaching those of error-corrected digital computers. In addition, ANN parameters trained by conventional back propagation algorithm can become suboptimal when encoding errors are encountered. In such a case, robust simulated annealing algorithms [37] can be used to train ANN parameters which is error-tolerant, hence when encoded in the ONN, will have better performance.

#### DISCUSSION

Processing big data at high speeds and with low power is a central challenge in the ﬁeld of computer science, and, in fact, a majority of the power and processors in data centers are spent on doing forward propagation (test-time prediction). Furthermore, low forward propagation speeds limit applications of ANNs in many ﬁelds including self-driving cars which require high speed and parallel image recognition.

Our optical neural network architecture takes advantage of high detection rate, high-sensitivity photon detectors to enable high-speed, energy-eﬃcient neural networks compared to state-of-the-art electronic computer architectures. Once all parameters have been trained and programmed on the nanophotonic processor, forward propagation computing is performed optically on a passive system. In our implementation, maintaining the phase modulator settings requires some (small) power of ∼10 mW per modulator on average. However, in future implementations, the phases could be set with nonvolatile phase-change materials[38], which would require no power to maintain. With this change, the total power consumption is limited only by the physical size, the spectral bandwidth of dispersive components (THz), and the photo-detection rate (100GHz). In principle, such a system can be at least 2 orders of magnitude faster than electronic neural networks (which are restricted at GHz clock rate). Assuming our ONN has N nodes, implementing m layers of N×N matrix multiplication and operating at a typical 100 GHz photo-detection rate, the number of operations per second of our system would be

R = 2m · N2 · 1011operations/s

ONN power consumption during computation is dominated by the optical power necessary to trigger an optical nonlinearity and achieve a suﬃciently high signal-to-noise ratio (SNR) at the photodetectors (assuming shot-noise limited detection on n photons per pulse, SNR √1/n). We

a

0.20

|[Figure 2]<br><br>50 60<br><br>70 80<br><br>76.7|
|---|

|[Figure 3]|
|---|

0.15

σ(rad)Φ

0.10

0.05

0.00

0.00 0.05 0.10 0.15 0.20

σD

90

75

Correctness(%)

60

45

50

b

40

Counts

30

20

10

0

##### d

40

30

Counts

20

10

0

| |
|---|

Measured

| | |
|---|---|

A B C D

| | |
|---|---|
| | |

| | |
|---|---|
| | |

| | |
|---|---|
| | |

A B C D Vowel

Simulated

| |
|---|

50 c

| | |
|---|---|
| | |

40

30

20

10

0

A B C D

##### e

40

| | |
|---|---|
| | |

30

20

| | |
|---|---|
| | |

10

0

A B C D Vowel

- FIG. 3. Vowel recognition. (a) Correct rate for vowel recognition problem with various phase encoding error (σΦ) and photo-

detection error (σD), the deﬁnition of these two variables can be found in method section. The solid lines are the contours for different level correctness percentage. (b-e) Simulated and experimental vowel recognition results for an error-free training matrix where (b) vowel A was spoken, (c) vowel B was spoken, (d) vowel C was spoken, and (e) vowel D was spoken.

assume a saturable absorber threshold of p 1 MW/cm2 – valid for many dyes, semiconductors, and graphene [21, 22]. Since the cross section for the waveguide is A = 0.2µm ×0.5µm, the total power needed to run the system is therefore estimated to be: P ≈ N mW. Therefore, the energy per operation of ONN will scale as R/P = 2m · N ·1014 operations/J (or P/R = mN5 fJ/operation). Almost the same energy performance and speed can be obtained if optical bistability [24, 27, 39] is used instead of saturable absorption as the enabling nonlinear phenomenon. Even for very small neural networks, the above power eﬃciency is already at least 3 orders of magnitude better than that in conventional electronic CPUs and GPUs, where P/R ≈ 1pJ/operation (not including the power spent on data movement) [40], while conventional image recognition tasks require tens of millions of training parameters and thousands of neurons (mN ≈ 105)[41]. These considerations suggest that the optical NN approach may be tens of millions times more eﬃcient than conventional computers for standard problem sizes. In fact, the larger the neural network, the bigger the advantage of using optics is: this comes from the fact that evaluating an N × N matrix in electronics requires O(N2) energy, while in optics, it requires in principle no energy. Further details on power eﬃciency calculation can be found in the Supplementary information section 3.

ONNs enable new ways to train ANN parameters. On a conventional computer, parameters are trained with back propagation and gradient descent. However, for certain ANNs where the eﬀective number of parameters substantially exceeds the number of distinct parameters (includ-

ing recurrent neural networks (RNN) and convolutional neural networks(CNN)), training using back propagation is notoriously ineﬃcient. Speciﬁcally the recurrent nature of RNNs gives them eﬀectively an extremely deep ANN (depth=sequence length), while in CNNs the same weight parameters are used repeatedly in diﬀerent parts of an image for extracting features. Here we propose an alternative approach to directly obtain the gradient of each distinct parameter without back propagation, using forward propagation on ONN and the ﬁnite diﬀerence method. It is well known that the gradient for a particular distinct weight parameter ∆Wij in ANN can be obtained with two forward propagation steps that compute J(Wij) and J(Wij + δij),

followed by the evaluation of ∆Wij = J(Wij+δδij)−J(Wij)

(this step only takes two operations). On a conventional computer, this scheme is not favored because forward propagation (evaluating J(W)) is computationally expensive. In an ONN, each forward propagation step is computed in constant time (limited by the photodetection rate which can exceed 100 GHz [12]), with power consumption that is only proportional to the number of neurons–making the scheme above tractable. Furthermore, with this on-chip training scheme, one can readily parametrize and train unitary matrices–an approach known to be particularly useful for deep neural networks [42]. As a proof of concept, we carry out the unitary-matrix-on-chip training scheme for our vowel recognition problem (see Supplementary Information Section 4).

ij

Regarding the physical size of the proposed ONN, current technologies are capable of realizing ONNs exceeding

the 1000 neuron regime – photonic circuits with up to 4096 optical components have been demonstrated [43]. 3-D photonic integration could enable even larger ONNs by adding another spatial degree of freedom [44]. Furthermore, by feeding in input signals (e.g. an image) via multiple patches over time (instead of all at once) – an algorithm that has been increasingly adopted by deep learning community [45] – the ONN should be able to realize much bigger eﬀective neural networks with relatively small number of physical neurons.

#### CONCLUSION

The proposed architecture could be applied to other artiﬁcial neural network algorithms where matrix multiplications and nonlinear activations are heavily used, including convolutional neural networks and recurrent neural networks. Further, the superior forward propagation speed and power eﬃciency of our ONN can potentially enable training the neural network on the photonics chip directly, using only forward propagation. Finally, it needs to be emphasized that another major portion of power dissipation in current NN architectures is associated with data movement–an outstanding challenge that remains to be addressed. However, recent dramatic improvements in optical interconnects using integrated photonics technology has the potential to significantly reduce data-movement energy cost [46]. Further integration of optical interconnects and optical computing units need to be explored to realize the full advantage of all-optical computing.

METHODS

Fidelity Analysis

We evaluated the performance of the SU(4) core with the ﬁdelity metric f = ∑i √piqi where pi, qi are experimental and simulated normalized (∑i xi = 1 where x ∈ {p, q}) optical intensity distributions across the waveguide modes, respectively.

## Simulation Method for Noise in ONN

We carry out the following steps to numerically simulate the performance of our trained matrices with varying degrees of phase encoding (σΦ) and detection (σD) noise.

- 1. For each of the four trained 4 × 4 unitary matrices

Uk, we calculate a set of {θik, φik} that encode the matrix.

- 2. We add a set of random phase encoding errors, {δθik, δφik} to the old calculated phases {θik, φik},

where we assume each δθik and δφik is a random variable sampled from a Gaussian distribution G(µ, σ)

with µ = 0 and σ = σΦ. We obtain a new set of perturbed phases {θik , φik } = {θik + δθik, φik + δφik}.

- 3. We encode the four perturbed 4 × 4 unitary matrices Uk based on the new perturbed phases {θik , φik }.
- 4. We carry out the forward propagation algorithm based on the perturbed matrices Uk with our test data set. During the forward propagation, every time when a matrix multiplication is performed (let’s say when we compute −→v = Uk · −→u ), we add a set of random photo-detection errors −→δv to the resulting −→v , where we assume each entry of −→δv is a random variable sampled from a Gaussian distribution G(µ, σ) with µ = 0 and σ = σD · |−→v |. We obtain the perturbed output vector −→v = −→v + −→δv.
- 5. With the modiﬁed forward propagation scheme above, we calculate the correctness percentage for the perturbed ONN.
- 6. Steps 2)-5) are repeated 50 times to obtain the distribution of correctness percentage for each phase encoding noise (σΦ) and photodetection noise (σD).

#### ACKNOWLEDGEMENTS

We thank Yann LeCun, Max Tegmark, Isaac Chuang and Vivienne Sze for valuable discussions. This work was supported in part by the Army Research Oﬃce through the Institute for Soldier Nanotechnologies under contract W911NF-13-D0001, and in part by the Air Force Oﬃce of Scientiﬁc Research Multidisciplinary University Research Initiative (FA9550-14-1-0052) and the Air Force Research Laboratory RITA program (FA8750-14-2-0120). M.H. acknowledges support from AFOSR STTR grants, numbers FA955012-C-0079 and FA9550-12-C-0038 and Gernot Pomrenke, of AFOSR, for his support of the OpSIS eﬀort, though both a PECASE award (FA9550- 13-1-0027) and funding for OpSIS (FA9550-10-1-0439). N. H. acknowledges support from the National Science Foundation Graduate Research Fellowship grant no. 1122374.

#### AUTHOR CONTRIBUTIONS

Y.S., N.H., S.S., X.S., S.Z., D.E., and M.S., developed the theoretical model for the optical neural network. N.H., M.P., and Y.S. performed the experiment. N.H. developed the cloud-based simulation software for collaborations with the programmable nanophotonic processor. Y.S., S.S., and X.S. prepared the data and developed the code for training MZI parameters. T.B.J. and M.H. fabricated the photonic integrated circuit. All authors contributed in writing the paper.

- [1] Hinton, G. E. & Salakhutdinov, R. R. Reducing the dimensionality of data with neural networks. Science 313, 504–507 (2006).
- [2] Mead, C. Neuromorphic electronic systems. Proceedings of the IEEE 78, 1629–1636 (1990).
- [3] Poon, C.-S. & Zhou, K. Neuromorphic silicon neurons and large-scale neural networks: challenges and opportunities. Frontiers in Neuroscience 5 (2011). URL http://www.frontiersin.org/neuromorphic_ engineering/10.3389/fnins.2011.00108/full.
- [4] Shaﬁee, A. et al. Isaac: A convolutional neural network accelerator with in-situ analog arithmetic in crossbars. In Proc. ISCA (2016).
- [5] Misra, J. & Saha, I. Artiﬁcial neural networks in hardware: A survey of two decades of progress. Neurocomputing 74, 239–255 (2010).
- [6] Silver, D. et al. Mastering the game of go with deep neural networks and tree search. Nature 529, 484–489 (2016).
- [7] Tait, A. N., Nahmias, M. A., Tian, Y., Shastri, B. J. & Prucnal, P. R. Photonic neuromorphic signal processing and computing. In Nanophotonic Information Physics, 183–222 (Springer, 2014).
- [8] Tait, A. N., Nahmias, M. A., Shastri, B. J. & Prucnal, P. R. Broadcast and weight: an integrated network for scalable photonic spike processing. Journal of Lightwave Technology 32, 3427–3439 (2014).
- [9] Prucnal, P. R., Shastri, B. J., de Lima, T. F., Nahmias, M. A. & Tait, A. N. Recent progress in semiconductor excitable lasers for photonic spike processing. Advances in Optics and Photonics 8, 228–299 (2016).
- [10] Vandoorne, K. et al. Experimental demonstration of reservoir computing on a silicon photonics chip. Nature communications 5 (2014).
- [11] Appeltant, L. et al. Information processing using a single dynamical node as complex system. Nature communications 2, 468 (2011).
- [12] Vivien, L. et al. Zero-bias 40gbit/s germanium waveguide photodetector on silicon. Opt. Express 20, 1096– 1101 (2012). URL http://www.opticsexpress.org/ abstract.cfm?URI=oe-20-2-1096.
- [13] Cardenas, J. et al. Low loss etchless silicon photonic waveguides. Opt. Express 17, 4752 (2009). URL http: //dx.doi.org/10.1364/OE.17.004752.
- [14] Harris, N. C. et al. Bosonic transport simulations in a large-scale programmable nanophotonic processor. arXiv:1507.03406 (2015).
- [15] LeCun, Y., Bengio, Y. & Hinton, G. Deep learning. Nature 521, 436–444 (2015). URL http://dx.doi.org/10.1038/ nature14539.
- [16] Schmidhuber, J. Deep learning in neural networks: An overview. Neural Networks 61, 85–117 (2015).
- [17] Lawson, C. L. & Hanson, R. J. Solving least squares problems, vol. 15 (SIAM, 1995).
- [18] Reck, M., Zeilinger, A., Bernstein, H. J. & Bertani, P. Experimental realization of any discrete unitary operator. Phys. Rev. Lett. 73, 58–61 (1994). URL http://link. aps.org/doi/10.1103/PhysRevLett.73.58.
- [19] Miller, D. A. B. Perfect optics with imperfect components. Optica 2, 747–750 (2015). URL http://www.osapublishing.org/optica/abstract. cfm?URI=optica-2-8-747.

- [20] Connelly, M. J. Semiconductor optical ampliﬁers (Springer Science & Business Media, 2007).
- [21] Selden, A. Pulse transmission through a saturable absorber. British Journal of Applied Physics 18, 743 (1967).
- [22] Bao, Q. et al. Monolayer graphene as a saturable absorber in a mode-locked laser. Nano Res. 4, 297–307 (2010). URL http://dx.doi.org/10.1007/s12274-010-0082-9.
- [23] Schirmer, R. W. & Gaeta, A. L. Nonlinear mirror based on two-photon absorption. JOSA B 14, 2865–2868 (1997).
- [24] Soljačić, M., Ibanescu, M., Johnson, S. G., Fink, Y. & Joannopoulos, J. Optimal bistable switching in nonlinear photonic crystals. Physical Review E 66, 055601 (2002).
- [25] Xu, B. & Ming, N.-B. Experimental observations of bistability and instability in a two-dimensional nonlinear optical superlattice. Phys. Rev. Lett. 71, 3959–3962 (1993). URL http://link.aps.org/doi/10.1103/PhysRevLett. 71.3959.
- [26] Centeno, E. & Felbacq, D. Optical bistability in ﬁnite-size nonlinear bidimensional photonic crystals doped by a microcavity. Phys. Rev. B 62, R7683–R7686 (2000). URL http: //link.aps.org/doi/10.1103/PhysRevB.62.R7683.
- [27] Nozaki, K. et al. Sub-femtojoule all-optical switching using a photonic-crystal nanocavity. Nature Photonics 4, 477– 483 (2010). URL http://dx.doi.org/10.1038/nphoton. 2010.89.
- [28] Ríos, C. et al. Integrated all-photonic non-volatile multilevel memory. Nature Photonics 9, 725–732 (2015). URL http://dx.doi.org/10.1038/nphoton.2015.182.
- [29] Krizhevsky, A., Sutskever, I. & Hinton, G. E. Imagenet classiﬁcation with deep convolutional neural networks. In Pereira, F., Burges, C. J. C., Bottou, L. & Weinberger, K. Q. (eds.) Advances in Neural Information Processing Systems 25, 1097–1105 (Curran Associates, Inc., 2012). URL http://papers.nips.cc/paper/ 4824-imagenet-classification-with-deep-convolutional-neural-networks. pdf.
- [30] Chow, D. & Abdulla, W. H. Speaker identiﬁcation based on log area ratio and gaussian mixture models in narrow-band speech. In PRICAI 2004: Trends in Artiﬁcial Intelligence, 901–908 (Springer, 2004).
- [31] Deterding, D. H. Speaker normalisation for automatic speech recognition. Ph.D. thesis, University of Cambridge

(1990).

- [32] Harris, N. C. et al. Eﬃcient, compact and low loss thermooptic phase shifter in silicon. Optics Express 22 (2014). URL http://dx.doi.org/10.1364/OE.22.010487.
- [33] Baehr-Jones, T. et al. A 25 Gb/s Silicon Photonics Platform. ArXiv e-prints (2012). URL http://adsabs. harvard.edu/abs/2012arXiv1203.0767B. 1203.0767.
- [34] Miller, D. A. B. Self-conﬁguring universal linear optical component [invited]. Photonics Research 1 (2013). URL http://dx.doi.org/10.1364/PRJ.1.000001.
- [35] Cheng, Z., Tsang, H. K., Wang, X., Xu, K. & Xu, J.-B. In-plane optical absorption and free carrier absorption in graphene-on-silicon waveguides. IEEE Journal of Selected Topics in Quantum Electronics 20, 43–48 (2014).
- [36] On the repeatability of this experiment: we have carried out the entire testing run 3 times. The reported result (76.7% correctness percentage) is associated with the best calibrated run (highest measured ﬁdelity). The other two less calibrated runs exceeded 70% correctness percentage. For further discussion on enhancing the correctness percentage, see S.I. (Section 6).

- [37] Bertsimas, D. & Nohadani, O. Robust optimization with simulated annealing. Journal of Global Optimization 48, 323–334 (2010).
- [38] Ríos, C. et al. Integrated all-photonic non-volatile multilevel memory. Nature Photonics 9, 725–732 (2015).
- [39] Tanabe, T., Notomi, M., Mitsugi, S., Shinya, A. & Kuramochi, E. Fast bistable all-optical switch and memory on a silicon photonic crystal on-chip. Opt. Lett. 30, 2575– 2577 (2005). URL http://ol.osa.org/abstract.cfm? URI=ol-30-19-2575.
- [40] Horowitz, M. 1.1 computing’s energy problem (and what we can do about it). In 2014 IEEE International Solid-State Circuits Conference Digest of Technical Papers (ISSCC), 10–14 (IEEE, 2014).
- [41] Krizhevsky, A., Sutskever, I. & Hinton, G. E. Imagenet classiﬁcation with deep convolutional neural networks. In Advances in neural information processing systems, 1097–

- 1105 (2012).
- [42] Arjovsky, M., Shah, A. & Bengio, Y. Unitary evolution recurrent neural networks. arXiv preprint arXiv:1511.06464

(2015).

- [43] Sun, J., Timurdogan, E., Yaacobi, A., Hosseini, E. S. & Watts, M. R. Large-scale nanophotonic phased array. Nature 493, 195–199 (2013). URL http://dx.doi.org/10. 1038/nature11727.
- [44] Rechtsman, M. C. et al. Photonic ﬂoquet topological insulators. Nature 496, 196–200 (2013).
- [45] Jia, Y. et al. Caﬀe: Convolutional architecture for fast feature embedding. In Proceedings of the 22Nd ACM International Conference on Multimedia, MM ’14, 675–678 (ACM, New York, NY, USA, 2014). URL http://doi.acm.org/ 10.1145/2647868.2654889.
- [46] Sun, C. et al. Single-chip microprocessor that communicates directly using light. Nature 528, 534–538 (2015). URL http://dx.doi.org/10.1038/nature16454.

