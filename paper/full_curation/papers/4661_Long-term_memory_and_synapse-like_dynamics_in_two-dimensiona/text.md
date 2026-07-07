## arXiv:2205.07653v4[cond-mat.soft]17Jan2023

# Long-term memory and synapse-like dynamics in two-dimensional nanoﬂuidic channels

P. Robin1,†, T. Emmerich1,†, A. Ismail,2,3,†, A. Nigu`es1, Y. You2,3, G.-H. Nam2,3, A. Keerthi2,4, A. Siria1, A.K. Geim2,3, B. Radha2,3,∗, L. Bocquet1,∗

1Laboratoire de Physique de l’Ecole normale Sup´erieure, ENS, Universit´e PSL, CNRS, Sorbonne Universit´e, Universit´e de Paris, 75005 Paris, France 2 National Graphene Institute, The University of Manchester, Manchester, UK 3 Department of Physics and Astronomy, The University of Manchester, Manchester, UK 4Department of Chemistry, University of Manchester, Manchester, UK ∗To whom correspondence should be addressed; E-mail: lyderic.bocquet@ens.fr,radha.boya@manchester.ac.uk † Equal contributions

One Sentence Summary: Electrolytes in 2D nanochannels develop long-term memory, allowing to implement Hebbian learning on a nanoﬂuidic chip.

Fine-tuned ion transport across nanoscale pores is key to many biological processes such as neurotransmission. Recent advances have enabled the conﬁnement of water and ions to two dimensions, unveiling transport properties unreachable at larger scales and triggering hopes to reproduce the ionic machinery of biological systems. Here we report experiments demonstrating the emergence of memory in the transport of aqueous electrolytes across (sub)nanoscale channels. We unveiled two types of nanoﬂuidic memristors, depending on channel material and conﬁnement, with memory from minutes to hours. We explained how large timescales could emerge from interfacial processes like ionic self-assembly or surface adsorption. Such behavior allowed us to implement Hebbian learning with nanoﬂuidic systems. This result lays the ground for biomimetic computations on aqueous electrolytic chips.

Over the past decade, research in nanoﬂuidics has shed the light on many unconventional phenoma arising in the transport of water and ions through nanometric channels (1–12). The ﬁeld has grown at a fast pace, driven by the discovery of new fundamental behaviors of aqueous

transport at nanoscales, but also by their potential for a wealth of applications, from water desalination to energy harvesting (2). Most notably, the recent development of two-dimensional (2D) channels made by van der Waals assembly of various materials (graphite, hexagonal boron nitride, MoS2, etc.) has enabled the study of ionic transport at the smallest scales, with unmatched versatility in terms of geometry or surface properties (13–16). Speciﬁcs of 2D interactions offer a new asset to ﬁne-tune the properties of electrolytes, at odds with their bulk response. A recent, noticable prediction is that two-dimensional ionic self-assembly should be at the root of memory effects associated with conductance hysteresis under electrical forcing (17), a phenomenon known as memristor effect. This effect could allow to emulate the brain’s neuronal computation using ions in water as charge carriers, but artiﬁcial systems capable of mimicking this behavior have eluded experimental inquiry in aqueous electrolytes until now.

A memristor – short for memory resistor – is a resistor with an internal state that is susceptible to change depending on the history of voltage seen by the system, thereby modifying its conductance (18, 19). As this feature makes them the analogues of biological synapses, memristors have drawn considerable attention for their potential use as building blocks of bioinspired neuromorphic computers (20). However, most of existing examples are based on solidstate devices (like the metallic-insulator-metallic, or MIM, architecture) and function with coupled ion and electron dynamics (21). Although a handful of ﬂuidic memristors were also designed (22–24), they require high voltage to operate, well above the water splitting threshold (1.23V with respect to normal hydrogen electrode), use non-aqueous environments, or far exceed the nanoscale dimensions of biological systems. More generally, a challenge is to replicate the mechanism found in biological systems, where the transport and accumulation of solvated ions (notably calcium) in water are used for signalization, information processing and the building of memory (25,26). Developing such bio-inspired memristors would notably allow to design artiﬁcial nanoﬂuidic chips for neuromorphic computation, build an interface between artiﬁcial nanoﬂuidics and biological systems and explore possible gains in efﬁciency from using solvated ions as charge carriers. Here we report on a series of experiments that 2D nanoﬂuidic channels do open this avenue towards neuromorphic iontronics.

### Experimental demonstration of nanoﬂuidic memristors

#### Pristine MoS2 channels vs. activated carbon channels

In this work, we investigated two types of 2D nanochannels, of similar geometry but different surface properties (Fig. 1A). “Pristine” channels were made of two atomically smooth ﬂakes of 2D material (here MoS2) separated by an array of multiple layers of graphene nanoribbons used as spacers. On the other hand, “activated” carbon channels consisted of two graphite ﬂakes, in which a nanoscale trench was milled into the bottom ﬂake using electron-beam-induced etching (EBIE) (16). In both cases, the bottom wall of the channel was pierced and deposited on the aperture of a SiNx membrane. Further details regarding the fabrication of activated and

pristine channels can be found in Refs. (13) and (16) respectively, and recalled in Supplementary Material (SM, Figs. S1, S2). Although similar in design, these channels differed on a few key properties. The height of pristine MoS2 channels could be precisely controlled in increments of 0.34nm, and here down to 0.68nm – the channel’s depth corresponding to the spacers’ thickness. Conversely, the depth of activated carbon channels was controlled by EBIE with a resolution limited to a few nanometers. As recently evidenced by Emmerich et al. (16), the latter carries a much stronger surface charge compared to pristine walls, due to the exposure of their bottom wall to the electron beam. Here, we used activated carbon channels with channel height between 4 and 13nm, and pristine MoS2 channels with height between 0.68 and 86nm.

Once fabricated, the 2D channels were embeded in a ﬂuidic cell connected to two reservoirs ﬁlled with electrolyte (KCl, NaCl, LiCl, CaCl2, NiSO4, AlCl3). Salt concentrations between 1mM and 3M were tested. Unless stated otherwise, the solution’s pH was not modiﬁed after salt dissolution in deionized water, resulting in a pH range of 5.1 − 5.5 depending on salt concentration. A patch-clamp ampliﬁer (KEITHLEY 2400 or 2600 Series) connected to Ag/AgCl electrodes allowed for ionic current measurements under imposed time-dependent voltage drop V (t) of various frequencies (0.1 − 200mHz), shapes (sinusoidal, triangular), and amplitude (0.1−1V). In each case, the channel’s conductance G(t) was determined from current measurements from an instantaneous Ohm’s law G(t) = I(t)/V (t). Further details regarding current measurements are reported in Supplementary Materials (SM). Typical examples of experimental results for both types of systems are shown in Fig. 1.

#### Two types of memristors

Firstly, our central result is that 2D nanoﬂuidic channels did exhibit a memristive effect (Fig. 1BE): when probed by a time-varying voltage, they displayed a non-linear current-voltage characteristics which was pinched at zero voltage, associated with a conductance hysteresis. This pinched loop under periodic forcing is the hallmark of memristors (27). Such behavior was found in both types of channels – pristine and activated – for all tested electrolytes and at all salt concentrations; see SM for exhaustive results. The memristive effect was found to take place at frequencies between 0.1 and 200mHz, well below frequencies where capacitive effects can introduce hysteresis. This result corresponds to dynamical timescales from seconds to hours. Moreover, the phenomenon was found to be robust and was observed in a wide range of parameters – notably salt concentration, channel height and pH (Figs. S9-S16). All tested salts displayed the same phenomenology. In particular, we did not observe signiﬁcantly different results with multivalent salts, suggesting that the materials used here (MoS2 and activated carbon) are not subject to phenomena like charge reversal commonly observed with divalent ions like calcium (28). Our channels typically displayed an overall conductance much higher than what could be expected from bulk estimates, due to their high surface charge and hydrodynamic slippage (16).

Secondly, we could identify two types of memristors, depending on whether the currentvoltage characteristics did, or did not self-cross at the origin, see Fig. 1B (pristine MoS2 chan-

###### A

C

|B<br><br>-0.2<br><br>Voltage (V)<br><br>5<br><br>10<br><br>15<br><br>Pristine MoS2|Current (nA)|
|---|---|
|-0.4<br><br>-10<br>-5<br>|0.2 0.4|

Conductance (nS)

30

Ag/AgCl electrode

Ionic current

25

A

| | |
|---|---|
| |SiN|

20

15

membrane

 V

10

5

Voltage (V)

-0.4 -0.2 0 0.2 0.4

Nanofluidic device: Pristine or Activated

D E

Conductance (nS)

[Figure 1]

|-0.2<br><br>50<br><br>Activated carbon|Voltage (V)<br><br>100<br><br>150<br><br>200<br><br>250<br><br>Current (nA)<br><br>|
|---|---|
|-0.6 -0.4<br><br>-50|0.2 0.4 0.6|

[Figure 2]

top layer

300

250

spacers

electron beam

200

150

bottom layer

100

MoS2 (graphene spacers) height 0.68 - 86 nm

Etched graphite height 4 - 13 nm

50

Voltage (V)

-0.6 -0.4 -0.2 0 0.2 0.4 0.6

- Figure 1: Experimental study of the memristor effect using two kinds of nanoﬂuidic devices. (A) Sketch of the nanoﬂuidic cell. A nanochannel was deposited on a membrane separating two reservoirs ﬁlled with an electrolytic solution. The red arrow indicates path taken

by water and ions accross the system. We used two types of nanochannels: pristine MoS2 channels (bottom left pannel) and activated carbon channels (bottom right pannel). (B and C) Typical example of a memristive current-voltage and conductance-voltage characteristics of a pristine MoS2 channel (height h = 1nm) under periodic voltage (triangular wave of frequency 8mHz, using 3M KCl). The IV curve displays a loop that is pinched (but does not intersect) at the origin, and the GV curve has a crossing point at zero voltage. (D and E) Typical example of a memristive current-voltage and conductance-voltage characteristics of an activated carbon channel (height h = 13nm) under periodic voltage (sinusoidal wave of frequency 1mHz, using 1mM CaCl2). Here, the IV curve crosses itself at the origin and the GV curve takes the form of a simple loop. For all data, pH was not modiﬁed after salt dissolution in deionized water, resulting in a pH range of 5.1 − 5.5.

nel) versus Fig. 1D (activated carbon channel). This fundamental difference is best illustrated by looking at the curve of conductance as function of voltage: it either displayed a twisted loop (with one crossing point, Fig. 1C) or open loop (no crossing point, Fig. 1E). Following the terminology introduced by Ref. (27), we classiﬁed our experimental data as follows. Systems that exhibited a self-crossing IV curve (Fig. 1D and 1E) were termed bipolar memristors. Conversely, those that instead displayed a self-crossing GV curve (Fig. 1B and 1C) were refered to as unipolar memristors.

A key aspect of memristors is their ability to switch between different internal conductance states. We observed that bipolar memristors change state when the polarity of voltage was reversed, with e.g. maximum conductance at +1V and minimum conductance at −1V (Fig. 1E) – hence the name bipolar. On the other hand, unipolar memristors generally exhibited symmetric IV and GV curves, that were however strongly non-linear when the amplitude of voltage was increased. Their conductance only weakly depended on voltage polarity, but could vary by up to two orders of magnitude between voltage V = 0 and V = ±1V (Fig. 1C) – hence the name unipolar. Together, these facts indicate that the possible internal states of unipolar and bipolar memristors were fundamentally different.

In addition, thinner pristine devices (channel height h < 10nm) could display either kind of behaviour depending on salt concentration (with unipolar memristors at 0.1 M or higher). Thicker pristine MoS2 channels, on the other hand, only displayed a weak bipolar memristor effect; however, the memory effect was not as signiﬁcant as that observed in thinner channels implying that conﬁnement in a 2D geometry is essential for attaining memory effects. Lastly, the phenomenon was found to be weakened at acidic pH in both types of systems. All corresponding data are provided in SM (Figs. S9 to S16).

This comparison sheds light on a possible explanation. Bipolar memristors were predominant for high surface charges (as found in activated carbon channels) and low salt concentration – in other words, for surface-dominated conduction. Instead, unipolar memristors existed for moderate surface charge (pristine MoS2 channels), high salt concentration and strong conﬁnement: these results corresponded to a ‘conﬁnement-dominated’ regime. In both cases, a prerequisite for memory effects was the system’s ability to display non-linear ion transport. Accordingly, we now focus on the description of the system’s various conductance states as function of applied voltage.

#### Two sources of non-linearity: collective ionic transport and ionic rectiﬁcation

The above observations suggested the existence of two distinct mechanisms behind the memristive behavior of nanoﬂuidic channels. Unipolar memristors only existed in thin channels (h < 10nm) and at high salt concentration (c ≥ 0.1M) and the corresponding experimental results directly echoed the theoretical mechanisms discussed in Ref. (17). In this picture, a non-linear response can be accounted for by the formation of tightly bound Bjerrum pairs of ions if conﬁnement is sufﬁciently strong (and the solution not too diluted), preventing conduc-

tion (Fig. 2A). The application of a sufﬁciently strong electric ﬁeld can break these pairs or assemble them into an arc-like polyelectrolyte, allowing in both cases electrical current to ﬂow, a process known as the (second) Wien effect. As a result, the system’s conductance G is a strongly non-linear function of voltage V that almost vanishes in absence of voltage, behaving as

G(V ) ∝ |V |α (1) with a predicted exponent α > 1, and usually around 2 (see SM, section 3 and Ref. (17) for the derivation). We can take into account the fact that not all ions may be paired up by adding a small constant term G0 = G(V = 0) into the above equation. This mechanism is independent of voltage sign, and thus does correspond to a unipolar memristor. It also allows the conductance to vary continuously over a large range of values, accounting for experimental observations. In theory, this process can only take place in thinner channels – less than 2nm in thickness – as Bjerrum pairs only exist under strong conﬁnement. In practice, the transition from unipolar to bipolar behavior was found to take place around a thickness of 10nm. A possible explanation for this robustness is that ion pairs could still exist in the few water layers next to the channel’s walls, even in slightly larger channels: in particular, the presence of a wall tends to lower the dielectric constant of the ﬁrst water layers (29), and ions are thus expected to experience stronger electrostatic interactions near surfaces. If that is the case, then ionic pairing near solid surfaces could be relevant in other contexts and their dynamics could be probed for with similar time-varying voltage.

On the other hand, bipolar devices changed state depending on the polarity of applied voltage, and their memory should therefore stem from an internal asymmetry. However, in some experimental conditions, pristine MoS2 channels did display this kind of hysteresis despite their internal surface being atomically smooth and controlled. Therefore, we attributed the source of asymmetry to entrance effects. By construction, the SiNx membrane was present on one side of the device only (Fig. 1A) and the two mouths of the channel did not have the same access resistance. Coupled with the exclusion of anions from the channel (due to its strong negative surface charge), this result is expected to result in ionic rectiﬁcation (Fig. 2B, Fig. S6): when cations ﬂow from the side with lower access resistance, ions will accumulate inside the channel as entry is ‘easier’ than exit, resulting in a conductance increase. If voltage is reversed, cations will ﬂow from the side of higher resistance, the channel will instead be depleted and conductance will drop. This mechanism is analogous to that of a PN junction, and results in a diode-like current-voltage characteristic (30) with two distinct possible values of conductance, deﬁning a rectiﬁcation factor βRect:

###### G(V > 0) G(V < 0)

βRect (2)

Experimentally, we found βRect = 1 − 5, consistent with the above analysis in terms of entry effects (see SM, section 3). Because this type of non-linearity depends on voltage sign, it corresponds to a bipolar memristor.

We stress that these two phenomena were not mutually exclusive: pristine MoS2 channels could show signs of both mechanisms at the same time. In such cases, the IV curve displayed two crossing points (rather than none or a single one); further analysis and experimental data can be found in SM (section 3.4 and Fig. S17).

Although any system presenting a strong enough non-linearity associated with various internal conductance states could in theory display a memristive behavior, it can only do so on a frequency range ﬁxed by the time required to switch between the conducting and the insulating states. However, such timescales are normally too short to be accessible in nanoﬂuidic systems, and this phenomenon requires peculiar transport processes to be observed.

#### Stop-and-go transport as a source of long-term memory

For both types of memristors, memory timescales were found to reach extremely large values, in the range of minutes to hours. Such long-term memory could be accounted for by taking ion pairing or surface adsorption into account in the dynamics of conﬁned ions. In the theoretical framework of Ref. (17), the electrolyte is indeed predicted to retain its conductance state through the formation of ion clusters, which was estimated to typically take a few milliseconds. More generally, one expects a nanoﬂuidic channel to retain a conductance state (deﬁned by the number of charge carriers present inside the channel) over a typical diffusion timescale, roughly L2/D, with L the channel length and D a typical ionic diffusion coefﬁcient in the channel. For channels of length around 10µm, this result would yield a maximum memory time of 0.1s, still orders of magnitude lower than experimental values. However, this picture changes if interfacial processes, rather than diffusion, govern ion transport. Consider a particle diffusing through a channel with chemically-active walls, such that it may adsorb on the surface (Fig. 2D). If the adsorption rate is much larger than the diffusion rate across the channel, then the particle will spend most of its time bound to the surface. As a result, the time it needs to escape the pore is the sum of the durations of all adsorption events. Let us deﬁne τdiff, the time needed to escape through diffusion alone and τd the time a particle bound to the surface takes to desorb. Then, if the particle is adsorbed every τa τdiff, there will be τdiff/τa such events along the particle’s trajectory as it crosses the channel. As a result, the residence time τm of the particle inside the pore reads:

τd τa

τdiff τa

τdiff τdiff (3)

τd =

τm =

In other words, the memory time of the system is the diffusion timescale times a ratio τd/τa measuring the strength of surface effects. At chemical equilibrium, this condition corresponds to the ratio of particle numbers on the surface and in the bulk of the channel, as quantiﬁed by the dimensionless Dukhin number Du = Σ/ehc, which compares the surface charge Σ to the charge density in the bulk of the electrolyte, ec. Putting numbers, activated carbon channels typically have Du ∼ 102−103, showing that surface effects strongly dominate the bulk. Eq.(3) then predicts a memory time in the range τm ∼ Du × τdiff ∼ 100s. This estimation is in agreement with experimental values, which were found to be in the range τm ∼ 50 − 400s (Figs. S12 and

Unipolar memristor Bipolar memristor

Ion flux

A

B

Ion pairs

Depletion

Voltage

ConductionstatesStop-and-gomechanism

VoltageVoltage

Polyelectrolytes

Accumulation

Voltage

C

D

###### Adsorption-desorption

###### Wien effect

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |

Pairing Unpairing (very fast) (slow)

Adsorption (very fast)

Desorption (slow)

Effective transport (very slow)

Effective transport (very slow)

- Figure 2: Theory of nanoﬂuidic memristors. (A and B) Description of the different conductance states explaining the memristor effect. (A) Wien effect as a source of the unipolar memristor effect. Under strong conﬁnement, ions assemble into non-conducting Bjerrum pairs. Conduction can then occur through the breaking of pairs (Wien effect) or their clustering into conducting arcs (polyelectrolytic Wien effect), under the action of a strong electric ﬁeld (regardless of sign). (B) Entry effects as a source of the bipolar memristor effect. The two mouths of the channel are asymmetric, resulting in ionic rectiﬁcation depending on the side from which charges enter the system. If they enter from the side of low resistance, ions accumulate and conductance rises. Otherwise, the channel is depleted and conductance is lowered. As the channel’s walls bear a strong negative charge, only positive ions are represented here. (C and D) Effective ‘stop-and-go’ transport and long-term memory. In both mechanisms (Wien effect or geometrical asymmetry), the system’s conductance state can be retained over large timescales if transport is governed by a stop-and-go motion, induced by repeated pairing/unpairing or adsorption/desorption events, respectively.

S14), and is consistent with previous reports of extremely slow diffusion of ions near a chemically active surface (31). Our prediction was found to generally underestimate experimental values: this can be attributed to the fact that our model assumes independent successive adsorption events, while in reality they tend to be correlated over long timescales (32). Moreover, this surface-driven mechanism could explain the disappearance of the phenomenon at low pH (Fig. S16), which is known to greatly inﬂuence the channels’ surface charge (16). The observed dependence of the memristor effect with the electrolyte could likewise result from difference in chemical afﬁnity between the various species of ions considered and surface defects (Figs. S9 and S14) – however, this depence is hard to analyze and would require further knowledge of the chemical nature of adsorption sites.

We note that this slow ‘stop-and-go’ motion of ions near the channel’s surface is not incompatible with the high conductance of some (notably activated) channels: although surface processes such as adsorption can slow down conductance changes, they do not modify the overall large number of ions present in the channel due to its strong surface charge. We recall how to link conductance to surface charge in SM (section 3.2). Similarly, we observe that the slow down of the dynamics on the timescales of minutes emerges from microscopic processes (adsorbing events) with molecular timescales (say 1µs at best). This is, however, reminiscent of previous studies that showed how chemical or physical surface processes, involving notably the Stern layer, can result in hour-long phenomena when coupled to a water ﬂow (33,34).

A similar argument can be formulated for unipolar memristors. This time, the conduction state of the system is encoded in the number of ions which are not part of tightly bound pair (and can therefore contribute to current) – according to the Wien effect. Similarly to surface adsorption, one expects that successive pairing-unpairing events will create a stop-and-go motion of ions through the system (Fig. 2C). The memory time is then again found to be given by diffusion times a ratio of pairing and unpairing times, potentially reaching minute- or even hour-long timescales.

Building on this qualitative picture, one may propose a minimal model, accounting for the memristor effect over minute-long times for both memory types, as detailed in SM (Fig. S7). We found that the system’s conductance at time t was given by the convolution of its quasistatic conductance, as given by Eqs. (1) and (2) depending on memristor type, with an exponential memory kernel:

∞

e−s/τ τ

ds (4)

Gqs[V (t − s)]

G(t) =

0

where Gqs is quasistatic (non-linear) conductance and τ a timescale of the order of the memory time τm. The resulting prediction was in good agreement with experimental data (Fig. 3A-B). According to this simple model, measuring the loop in the IV curve allowed to characterize the memristive effect (Fig. 3C). The curve of area as function of voltage frequency exhibited a maximum when the frequency matched the intrinsic memory time τm, akin to a resonance. The comparison to the prediction of the model showed again a good agreement and provided a direct measurement of τm (Fig. 3C).

###### B

|Unipolar memristor: pairing/unpairing<br><br>A<br><br>Voltage<br><br>Conductance<br><br>5<br><br>10<br><br>15|Voltage (V)<br><br>Current (nA)<br><br>|
|---|---|
|-0.4 -0.2<br><br>-10<br>-5<br>|0.2 0.4<br><br>|Exp. data<br><br>Eq. (4)|
|---|
|

U

|50<br><br>100<br><br>150<br><br>200<br><br>250<br><br>| | |
|---|---|
| |Voltage|
| | |
| | |
<br><br>Conductance<br><br>Bipolar memristors: absorption/desorption|Voltage (V)<br><br>Current (nA)<br><br>C|
|---|---|
|-0.5<br><br>-100<br>-50<br>|0.5<br><br>|Exp. data<br><br>Eq. (4)|
|---|
|

Bip abs

Looparea(normalized)

0.5

||Pristine<br><br>Eq. (S38) Activated Eq. (S38)<br><br>|
|---|
<br><br>Memory timescale|
|---|

0.4

0.3

0.2

0.1

0

10-3 10-2 10-1

Frequency (Hz)

- Figure 3: Comparison of theoretical models and experimental results. (A and B) Fit of experimental IV curves using the minimal model of the nanoﬂuidic memristor. For unipolar memristors (A), the quasistatic conductance was taken to be a power law of applied voltage (here with exponent α = 2), and a sign-dependent constant in the bipolar case (B), see insets. The experimental curves were then ﬁtted using the delay time τ as single free parameter, see Eq.

(4). Datasets correspond to devices presented in Fig. 1B-E: 3M KCl in pristine MoS2 channel (height 1nm) or 1mM CaCl2 in activated carbon channel (height 13nm). (C) Normalized area of the IV loop as function of voltage frequency. Data correspond to 100mM CaCl2 in 4nm activated carbon channel and 1M KCl in 0.68nm pristine MoS2 channel. The memory timescale τm could be extracted from experimental data by looking for the frequency where the loop was the largest. The curve of loop area as function of frequency was well described by that of the minimal model, see Eq. (S38) of SM (solid lines). See Fig. S8 for the normalization process.

### Hebbian learning with nanoﬂuidic memristors

#### Reversible modiﬁcation of a nanochannel’s conductance

This qualitative and quantitative rationalization of the ionic memristor effects paves the way for the implementation of learning algorithms using our nanoﬂuidic devices. As a proof of concept, we now show that they could be used to emulate some basic functionalities found in biological synapses. Because their memory was not lost when voltage was reset to zero, we only focused on bipolar memristors, as exhibited here with activated carbon channels. We ﬁrst conﬁrmed that their conductance could be increased or lowered through successive voltage sweeps of a given polarity (Fig. 4A). Following a positive spike, the conductance was abruptly increased for a short period (∼ 1min), before relaxing to a long-term value above its initial state (Fig. 4B). This result shows that our device displayed both short- and long-term memory, similar to biological synapses (35).

These neural connections act as resistors whose conductance can be tuned during learning processes, with reversible modiﬁcations both on short (milliseconds to minutes) and long (minutes to hours or more) timescales (36, 37). The latter, known as long-term potentiation (or depression, when the conductance is lowered) enables the storage of information through the synapse’s conductance state as a form of in-memory coding. Although the exact biological mechanisms are still debated, the transport and accumulation of calcium ions at speciﬁc places play a key role (26, 38). Taking inspiration from these features, we designed a protocol to implement in-memory computations with our nanoﬂuidic channel (Fig. 4C). We incremented a nanochannel’s conductance by applying a ‘write’ voltage spike (+1V during 10seconds). It could then be accessed to via a ‘read’ pulse (+0.1V during 5seconds), which did not perturb sensibly its value. It could also be reset to its original value with an ‘erase’ spike (−1V during 10seconds). This setup allowed for a versatile and reversible modiﬁcation and access to the stored value for computational applications. As a proof of concept, we show in Fig. 4C that the modiﬁcation process was indeed fully reversible and allowed to store an analog variable over long timescales, by applying a series of 60 write and erase spikes. We thus demonstrated that nanoscale channels could be ‘programmed’ through the tuning of their conductance, enabling the implementation of in-memory operations with ion-based nanoﬂuidic systems.

#### Hebbian learning algorithm

Building on the similarities between our nanoﬂuidic system and synapses, we now implemented a basic form of Hebbian learning. In biological neuron networks, this process consists in the modiﬁcation of synaptic weights depending on the relative activation timings of two neurons connected by a given synapse (Fig. 5A). If the presynaptic neuron repeatedly emits an action potential shortly before the activation of the postsynaptic neuron, the synapse is strengthened (meaning its conductance is increased), as this result suggests a form of causality between the two activation events. Conversely, the synapse is weakened (i.e., its conductance is decreased) if

- 99
- 100
- 101
- 102
- 103
- 104
- 105

- 0.8
- 1

Potential(V)

- -50
- -40
- -30
- -20
- -10

0

10

20

30

40

50

Current(nA)

|Voltage Current<br><br>|
|---|

0 10 20 30 40 50 60

Spike number

100

102

104

106

108

110

112

Conductance(%)

30 write spikes ‘Potentiation’

30 erase spikes ‘Depression’

A B C

0 50 100

Time (s)

0

- 0.5
- 1

Appliedpotential(V)

Write

Read

50

Time (s)

- -1
- -0.5

0

Appliedpotential(V)

Erase

Read

Figure 4: Programing a nanochannel through reversible conductance strenghening. (A) Evolution of the ionic current (orange) under voltage pulses of constant polarity (blue). Positive (resp. negative) pulses result in a increase (resp. decrease) of conductance. (B) Conductance change following a positive voltage pulse, exhibiting both short- (< 2min) and long-term (>

- 2min) memory. The conductance was read by applying a weak square voltage wave that had no sensible impact on the state of the system, and modiﬁed through a strong voltage spike. Blue points are experimental data. The red solid line is a guide for the eye. Inset: applied voltage as function of time. The red arrow indicates the beginning of the voltage spike. (C) Long-term modiﬁcation of a nanochannel’s conductance. 30 write spikes (+1 V, 10 s) were applied, followed by 30 erase spikes (-1 V, 10 s) which brought back the system to its initial state. Between each spike, the conductance was let to stabilize during two minutes and was then measured with a read pulse (0.1 V, 5 s), see Fig. S3. All data correspond to activated carbon channels with height h = 5nm ﬁlled with 1mM CaCl2.

|2 4 6<br><br>Time (min)<br><br>| |
|---|
<br><br>0<br><br>0.5<br>1<br><br><br>Voltage(V)<br><br>Short-term Long-term|
|---|

Voltage(V)

0.6

Conductance(%)

0.4

0.2

400 500 600 700

0

100 200 300

Time (s)

- -1
- -0.8
- -0.6
- -0.4
- -0.2

0 5 10 15

Time (min)

the ﬁring order is reversed, which would point at some anticausality relation. Importantly, these modiﬁcations occur even if the presynaptic neuron only causes a mild response (that is, too weak to initiate an action potential by itself) of the postsynaptic one. Altogether, this process implements a form of principal component analysis of the inputs received by the network (39), and is believed to play a major role in learning.

To mimick this mechanism, we designed the experiment presented in Fig. 5B. A computer generated a voltage time series that emulated the behaviour of two neurons. This time series was then applied on a nanoﬂuidic channel. The activation of the presynaptic neuron A was modeled by a weak positive voltage pulse. Whenever it activated, a ﬂip-ﬂop mechanism was triggered, connecting the channel to a generator E− that applied negative voltage spikes. This behaviour lasted until the postsynaptic neuron B activated and the system was branched on another generator E+ applying positive spikes instead. The opposite chain of events occured if neuron B activated ﬁrst: in that case, the channel ﬁrst received positive spikes from E+, followed by negative spikes from E− once neuron A activated. In both cases, the ﬂip-ﬂop reseted if a given total amount of time passed since its activation, allowing the process to start over. Further details regarding the implementation are provided in SM (Fig. S4).

If neuron A activated just before neuron B, then the system received a few negative spikes, followed by many positive spikes (Fig. 5C, left panel). Its conductance was thus globally increased. When the ﬁring order was reversed, conversely, the system received more negative than positive spikes (Fig. 5C, right panel), and its conductance was therefore lowered.

We implemented this protocol in the experiments as follows: we ﬁrst measured the system’s conductance, and ran the program which consisted in 8 successive activations of neurons A and B. Their relative spike timing – measured from the onset of the ﬁrst spike to be triggered to the onset of the second one – was used as a tuneable parameter. Then, we measured the resulting change in the conductance. The result is shown on Fig. 5D: when the presynaptic spike was followed (within a 40 seconds window) by a postsynaptic spike, conductance was increased – resulting in a strengthened connection between the two neurons. Otherwise, if the delay was too great or if the order was reversed, the connection was left unchanged or weakened, respectively. This phenomenology echoes the one observed in biological synapses, where the transient accumulation of certain ionic species triggers various mechanisms that ultimately result in the strengthening of neuron connections (38,40); here, the accumulation of ions inside the nanochannel directly causes a conductance increase.

In conclusion, two-dimensional nanochannels exhibited long-term memory, in the form of a memristor effect that could have two different physical origins - strong correlations between ions or entrance effects. In both cases, memory was retained over long timescales through interfacial processes that slowed down advection-diffusion across the channel. We fully characterized experimentally and theoretically both of these mechanisms. In particular, we showed they may be harnessed for ‘iontronics’ applications in a variety of contexts, as the memory effect was observed in all tested experimental conditions (salt concentration, electrolyte, pH). These systems reproduced the tuneability of synapses, through an accumulation (or depletion) of ions, and could implement basic learning algorithms such as Hebb’s rule within a simple

A

B

|A<br><br>40<br><br>80<br><br>[Figure 3]<br><br>Postsynaptic spike arrives before presynaptic spike|Conductance change (%)<br><br>Presynaptic spike before postsynaptic|
|---|---|
|-80 -40|40 80<br><br>Relative spike timing (ms)<br><br>-40|

Voltage

E+

Time

Switches to E- when A spikes Switches to E+ when B spikes

Earrives

P

spike

E+ E-

Presynaptic neuron A

Postynaptic neuron B

|D<br><br>B before A<br><br>10<br><br>20<br><br>[Figure 4]|A before B<br><br>Conductance change (%)|
|---|---|
|-40 -20<br><br>-20<br>-10<br>|20 40<br><br>Relative spike timing (s)|

Relative spike timing: -35s

C

(i) (ii)

Relative spike

- 0.5
- 1

- 0.5
- 1

|0.5<br><br>A spikes<br><br>timing: 35s| |
|---|---|
| |B<br><br>|

| |A<br><br>|
|---|---|
|0.5<br><br>B spikes| |

spikes

Voltage(V)

Time (min)

Time (min)

1 1.5

0

0

2

1 1.5 2

- -1
- -0.5

- -1
- -0.5

spikes

- Figure 5: Implementation of Hebb’s law using activated carbon channels. (A) Hebb’s law in biological synapses: a synapse’s conductance was increaseed (resp. decreased) when its presynaptic neuron ﬁred just before (resp. after) the postsynaptic one, adapted from Ref. (40). This process implemented a form of causality detection, known as spike-timing-dependent plasticity (STDP). Inset: rat hippocampal neuron (©ZEISS Microscopy from Germany, CC BY 2.0). (B) Hebb’s law with nanoﬂuidic memristors: voltage spikes were applied to a nanochannel, mimicking the activation of two neurons A and B. After each spike from the presynaptic (resp. postsynaptic) neuron, a series of erase (resp. write) spikes was applied. (C) Example of voltage spikes series depending on wether the presynaptic (i) or postsynaptic (ii) neuron activated ﬁrst. (D) Conductance change after 8 successive activations of the two neurons, in percentage of the initial conductance and as function of the relative activation timing of the neurons. Relative spike timing is measured from the onset of the ﬁrst spike to the onset of the second. Inset: SEM image of an activated carbon nanochannel. Data correspond to an activated carbon channel with height h = 5nm ﬁlled with 1mM CaCl2. See also Fig. S5 for additional data.

nanoﬂuidic architecture. More generally, our work illustrates how conﬁnement-induced effects could be harnessed to build ionic machines inspired by biological systems. This work paves the way for the development of more complex iontronic devices on nanoﬂuidic chips with advanced circuitry. The use of water and ions in the nanoﬂuidic memristors, which is shared by biological systems, furthermore suggests the possibility to interface artiﬁcial with biological devices.

### References

- 1. N. Kavokine, R. R. Netz, L. Bocquet, Annu. Rev. Fluid Mech. 53, 377–410 (2021).
- 2. L. Bocquet, Nat. Mater. 19, 254–256 (2020).
- 3. M. Wang, Y. Hou, L. Yu, X. Hou, Nano Lett. 20, 6937–6946 (2020).
- 4. K. Celebi, et al., Science 344, 289–292 (2014).
- 5. A. Marcotte, T. Mouterde, A. Nigu`es, A. Siria, L. Bocquet, Nat. Mater. 19, 1057–1061

(2020).

- 6. S. Garaj, et al., Nature 467, 190–193 (2010).
- 7. C. A. Merchant, et al., Nano Lett. 10, 2915–2921 (2010).
- 8. G. F. Schneider, et al., Nano Lett. 10, 3163–3167 (2010).
- 9. J. Feng, et al., Nature 536, 197–200 (2016).
- 10. E. Secchi, et al., Nature 537, 210–213 (2016).
- 11. R. H. Tunuguntla, et al., Science 357, 792–796 (2017).
- 12. N. Kavokine, M.-L. Bocquet, L. Bocquet, Nature 602, 84–90 (2022).
- 13. B. Radha, et al., Nature 538, 222–225 (2016).
- 14. A. Esfandiar, et al., Science 358, 511–513 (2017).
- 15. T. Mouterde, et al., Nature 567, 87–90 (2019).
- 16. T. Emmerich, et al., Nat. Mater. 21, 696–702 (2022).
- 17. P. Robin, N. Kavokine, L. Bocquet, Science 373, 687–691 (2021).
- 18. L. Chua, IEEE Trans. Circuit Theory 18, 507–519 (1971).
- 19. D. B. Strukov, G. S. Snider, D. R. Stewart, R. S. Williams, Nature 453, 80–83 (2008).
- 20. A. Sebastian, M. Le Gallo, R. Khaddam-Aljameh, E. Eleftheriou, Nat. Nanotechnol. 15, 529–544 (2020).
- 21. R. Ge, et al., Nano Lett. 18, 434–441 (2018).
- 22. Y. Bu, Z. Ahmed, L. Yobas, Analyst 144, 7168–7172 (2019).

- 23. Q. Sheng, Y. Xie, J. Li, X. Wang, J. Xue, Chem. Commun. 53, 6125–6127 (2017).
- 24. P. Zhang, et al., Nano Lett. 19, 4279–4286 (2019).
- 25. B. Hille, Biophys. J. 22, 283–294 (1978).
- 26. W. Gerstner, W. M. Kistler, Spiking Neuron Models: Single Neurons, Populations, Plasticity (Cambridge Univ. Press, 2002).
- 27. Y. V. Pershin, M. Di Ventra, Adv. Phys. 60, 145–227 (2011).
- 28. F. H. Van der Heyden, D. Stein, K. Besteman, S. G. Lemay, C. Dekker, Phys. Rev. Lett. 96, 224502 (2006).
- 29. L. Fumagalli, et al., Science 360, 1339–1342 (2018).
- 30. L. Bocquet, E. Charlaix, Chem. Soc. Rev. 39, 1073–1095 (2010).
- 31. J. Comtet, et al., Nature Nanotechnol. 15, 598–604 (2020).
- 32. S. Gravelle, R. R. Netz, L. Bocquet, Nano Lett. 19, 7265–7272 (2019).
- 33. B. L. Werkhoven, et al., Phys. Rev. Lett. 120, 264502 (2018).
- 34. P. Ober, et al., Nat. Commun. 12, 1–11 (2021).
- 35. J.-X. Bao, E. R. Kandel, R. D. Hawkins, Science 275, 969–973 (1997).
- 36. R. S. Zucker, W. G. Regehr, Annu. Rev. Physiol. 64, 355–405 (2002).
- 37. M. Bear, B. Connors, M. A. Paradiso, Neuroscience: Exploring the Brain, Enhanced Edition: Exploring the Brain (Jones & Bartlett Learning, 2020).
- 38. T. V. P. Bliss, G. L. Collingridge, Nature 361, 31–39 (1993).
- 39. W. Gerstner, W. M. Kistler, R. Naud, L. Paninski, Neuronal dynamics: From single neurons to networks and models of cognition (Cambridge Univ. Press, 2014).
- 40. G.-q. Bi, M.-m. Poo, J. Neurosci. 18, 10464–10472 (1998).
- 41. P. Robin, et al., Experimental data for: Long-term memory and synapselike dynamics in two-dimensional nanoﬂuidic channels, Zenodo (2022); https://doi.org/10.5281/zenodo.7085645
- 42. N. J. Bjerrum, Untersuchungen uber¨ Ionenassoziation (A. F. Høst,1926).
- 43. T. Prodromakis, C. Tomazou, L. Chua, Nat. Mater. 11, 478–481 (2012).

- 44. L. Onsager, J. Chem. Phys. 2, 599–615 (1934).
- 45. Z. Siwy, et al., Europhys. Lett. 60, 349 (2002).
- 46. C. B. Picallo, S. Gravelle, L. Joly, E. Charlaix, L. Bocquet, Phys. Rev. Lett. 111, 244501

(2013).

- 47. R. Karnik, C. Duan, K. Castelino, H. Daiguji, A. Majumdar, Nano Lett. 7, 547–551 (2007).
- 48. A. R. Poggioli, A. Siria, L. Bocquet, J. Phys. Chem. B 123, 1171–1185 (2019).

### Acknowledgments

Funding: L.B. acknowledges funding from the EU H2020 Framework Programme/ERC Advanced Grant agreement number 785911-Shadoks and ANR project Neptune. L.B. and A.S. acknowledge support from the Horizon 2020 program through Grant No. 899528- FET-OPENITS-THIN. A.K. acknowledges Ramsay Memorial Fellowship and also funding from Royal Society research grant RGS/R2/202036. B.R. acknowledges the Royal Society fellowship and funding from the EU H2020 Framework Programme/ERC Starting Grant number 852674 AngstroCAP. This work has received the support of Institut Pierre-Gilles de Gennes.

Authors contributions: L.B., R.B. conceived the project, designed the experiments and supervised the work, with inputs from P.R., A.K.G. and A.S.; T.E. and A.I. performed the measurements on the activated and pristine channels, respectively; A.K., Y.Y., G.-H.N., fabricated the pristine MoS2 channels, T.E., fabricated the activated carbon channels, with inputs from A.N. and A.S.; P.R. designed the experimental protocols for neuronal mimics and developed the theoretical modelling; T.E., A.I. and P.R. analyzed the experimental data with inputs from L.B., A.S., R.B., A.K.G.. The manuscript was written by P.R., L.B., R.B. with inputs from T.E. and A.I. All authors contributed to the review and editing of the manuscript.

Competing interests: None declared. Data and materials availability: All experimental data reported here are archived on Zenodo (41). All other data needed to evaluate the conclusions in the paper are present in the paper or the Supplementary Materials.

### Supplementary materials

Supplementary Text Figs. S1 to S17 References (42–48)

## arXiv:2205.07653v4[cond-mat.soft]17Jan2023

# Supplementary materials for: Long-term memory and synapse-like dynamics in two-dimensional nanoﬂuidic channels

P. Robin1,†, T. Emmerich1,†, A. Ismail,2,3,†, A. Nigu`es1, Y. You2,3, G.-H. Nam2,3, A. Keerthi2,4, A. Siria1, A.K. Geim2,3, B. Radha2,3,∗, L. Bocquet1,∗

1Laboratoire de Physique de l’Ecole normale Sup´erieure, ENS, Universit´e PSL, CNRS, Sorbonne Universit´e, Universit´e Paris Cit´e, 75005 Paris, France 2 National Graphene Institute, The University of Manchester, Manchester, UK 3 Department of Physics and Astronomy, The University of Manchester, Manchester, UK ∗To whom correspondence should be addressed; 4Department of Chemistry, University of Manchester, Manchester, UK E-mail: lyderic.bocquet@ens.fr,radha.boya@manchester.ac.uk † Equal contributions

Supplementary Text Figs. S1 to S17 References (42–48)

### Supplementary Materials Contents

- 1 Materials and methods 3

- 1.1 Nanofabrication of pristine MoS2 channels . . . . . . . . . . . . . . . . . . . . 3
- 1.2 Nanofabrication of activated carbon channels . . . . . . . . . . . . . . . . . . 4
- 1.3 Current measurements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5

- 2 Bio-inspired algorithms 6

- 2.1 Long-term potentiation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
- 2.2 Hebbian learing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6

- 3 Theory of the nanoﬂuidic memristor 7

- 3.1 Unipolar memristors – Wien effect under 2D conﬁnement . . . . . . . . . . . . 8
- 3.2 Bipolar memristors – Ionic rectiﬁcation . . . . . . . . . . . . . . . . . . . . . 10
- 3.3 Minimal model of a nanochannel with long-term memory . . . . . . . . . . . . 13

- 3.3.1 What does it mean for a nanochannel to have memory? . . . . . . . . . 13
- 3.3.2 Adsorption-desorption model . . . . . . . . . . . . . . . . . . . . . . 16
- 3.3.3 Wien effect . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
- 3.3.4 A simple ansatz - Determination of the memory time . . . . . . . . . . 18

- 3.4 Mixed mechanisms and shape of the IV curve . . . . . . . . . . . . . . . . . . 19

- 4 Additional experimental data 20

- 4.1 Pristine MoS2 channels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
- 4.2 Activated carbon channels . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

- 5 Detailed list of supplementary ﬁgures 21

### 1 Materials and methods

#### 1.1 Nanofabrication of pristine MoS2 channels

We fabricated the pristine MoS2 channels via van der Waals assembly following the protocol reported in our previous work (13). Brieﬂy, the process has two major parts: I) the preparation of the top-spacer layers, II) the assembly of the resulting top-spacer layers with the bottom layer to form tri-crystal (top-spacer-bottom) stack. Graphene and MoS2 ﬂakes were prepared by the mechanical exfoliation of their bulk layered forms, Graphenium graphite and natural MoS2 crystals (purchased from Manchester Nanomaterials). On a Si/SiO2 substrate, an exfoliated graphene ﬂake with a speciﬁc thickness between 0.68 and 86 nm, was searched for using an optical microscope, and the ﬂake thickness was conﬁrmed by atomic force microscopy (AFM) (Fig. S1A). Parallel strips (width of ∼120 nm, spacing ∼150 nm) were made from this graphene layer using e-beam lithography (EBL) and dry etching using oxygen plasma (Fig. S1B). The spacing between the graphene strips would become the channel width w in the ﬁnal device, while the thickness of the graphene would become the channel height h. Fig. S1B (bottom panel) shows the AFM height proﬁle of a three-layer thin graphene spacer, with channel width of ∼150 nm and a channel height of ∼ 1.2 ± 0.1 nm. Following this, a MoS2 crystal (thickness of 150 to 200 nm) was transferred on top of the graphene spacer (Fig. S1C). This MoS2 layer served as the top wall of the channel. The nanoﬂuidic chip fabrication process began by drilling a microhole (∼ 3µm × 50µm) in a SiNx membrane (thickness of 500 nm) on a silicon wafer, using photolithography and dry etching (mixture of SF6 and CHF3 gases). A thin MoS2 layer (thickness of 20 to 40 nm) was then transferred on top of the microhole on SiNx membrane to act

- as the bottom layer of the channel, using polymethylmethacrylate (PMMA) based wet transfer method (Fig. S1D). Then, the bottom layer was etched from the back of the SiNx membrane via dry etching with CHF3 and O2 gases, to protrude the microhole onto MoS2. Following this, the previously prepared stack of top MoS2-graphene spacer was wet-transferred onto the bottom MoS2 layer on SiNx (Fig. S1E). During this transfer, the spacer was oriented in such a way

that the channels are perpendicular to the rectangular microhole. Then, the graphene spacer was dry etched (O2 plasma) from the back of SiNx membrane to further open the microhole into the channels. At this stage, the resulting channels had variable lengths determined by the shape of the top MoS2 ﬂake, and any thin edges of the top layer could lead to its sagging into the channels thus blocking the channel entries. To address this, a Cr/Au strip (thickness 5 nm/70 nm, respectively) was deposited on the tri-crystal stack after photolithography to open the channels (Fig. S1E). The gold layer aided the device stability by minimizing the lifting of the MoS2 top layer during measurements at high voltages. Moreover, the gold strip served as a mask to create uniform and desired channel length for all channels across the device. Regions of the tri-crystal stack not masked by the Au strip were etched away, hence only the channel region underneath the gold strip remained (Fig. S1H). Throughout the device fabrication process, after each ﬂake transfer, the device was placed in a furnace under H2:Ar (1:10) gas for annealing (300°C for 3 hours and 400°C for 4 hours) to clean the polymer contamination. The optical images of the ﬁnal channel devices on SiNx are shown in Fig. S1I, both in reﬂection mode and transmission mode, with the channel length L (from the microhole to the end of the Au strip) indicated.

#### 1.2 Nanofabrication of activated carbon channels

We brieﬂy recall here the nanofabrication process of activated carbon nanochannels. A more detailed description can be found in Ref. (16). Bidimensional graphite crystals were obtained from commercially available graphite (GRAPHENIUM) by mechanical exfoliation on a Si/SiO2 substrate using cleanroom tape. A ﬁrst graphite ﬂake (‘bottom layer’) was pierced using electron beam induced direct etching (EBIE) in water vapor inside a scanning electron microscope, and then several trenches were dug from the hole using the same technique (Fig. S2, step 1). A second graphite crystal (‘top layer’) of roughly 50 nm in thickness was deposited above the hole and covered partially the trenches, closing them to form channels (Fig. S2, step 2). This ﬁrst transfer was realized using the dry-transfer techniques with a droplet-shaped polydimethyl-

siloxane (PDMS) stamp spin-coated with polypropylene carbonate (PPC). Finally, this bi-layer heterostructure was transferred above a Si/SiN window with a circular aperture in its middle, by making sure that the hole in the bottom layer landed above the aperture (Fig. S2, step 3). This second transfer was realized by wet transfer using a polymethylmethacrylate (PMMA) sacriﬁcial layer.

In typical cases, activated carbon channels are 5 − 10µm long, 100nm wide, with a height ranging from 5 to 15nm.

#### 1.3 Current measurements

Devices were placed into nanoﬂuidic measurement cells separating two reservoirs ﬁlled with electrolyte solutions of various salt concentrations and ionic species (KCl, CaCl2, AlCl3, NiSO4, NaCl, LiCl). We used Ag/AgCl electrodes to apply a potential drop across the channels and measure the resulting ionic current. Our electrodes were connected to KEITHLEY ampliﬁers (models 2636B and 2401). We used AC voltage of various frequencies (0.1 to 200mHz) with a sampling rate of 2Hz. Due to experimental technicalities, triangular waveforms were used to probe pristine MoS2 channels and sinusoidal for activated carbon channels; it was later checked, however, that our nanochannels react identically to both types of waveforms.

Even in the thinnest channels, the measured current was found to be several orders of magnitude higher than what was measured on a control system obtained by following the “pristine” protocol, but without spacers to create the channels. This shows that no leakage through the channel’s walls is not possible.

### 2 Bio-inspired algorithms

In this section, we detail how we performed basic neuromorphic operations with activated carbon channels. In all cases, input voltage was generated via MATLAB and exported as a text ﬁle, and then applied on the system by a LABVIEW program with a sampling rate of 2Hz.

#### 2.1 Long-term potentiation

Reversible long-term modiﬁcation of a nanochannel’s conductance was achieved by applying positive “write” pulses (+1V during 10s) or negative “erase” pulses (−1V during 10s). After each pulse, the conductance relaxation was tracked by applying 10 weak “read” pulses (∆Vread = +0.1V during 5s) separated by 5s (see Fig. S2A-B), and computing for each of these pulses the conductance from:

I ∆Vread

(S1) The conductance was found to stabilize after roughly two minutes of relaxation.

G =

We then checked that these modiﬁcations were incremental and reversible by applying 30 write pulses followed by 30 erase pulses, see Fig. 5C from main text. After each pulse, the system was let to relax for two minutes to let the conductance stabilize.

#### 2.2 Hebbian learing

The algorithm used to implement Hebbian learning is detailed in main text but we recall it here for the sake of clarity. A computer generated a voltage time series that emulated the behaviour of two neurons. This time series was then applied on a nanoﬂuidic channel. The activation of the presynaptic neuron A was modeled by a weak positive voltage pulse. Whenever it activated, a ﬂip-ﬂop mechanism was triggered, connecting the channel to a generator E− that applied negative voltage spikes. This behaviour lasted until the postsynaptic neuron B activated and the system was branched on another generator E+ applying positive spikes instead. The opposite chain of events occured if neuron B activated ﬁrst: in that case, the channel ﬁrst received positive

spikes from E+, followed by negative spikes from E− once neuron A activated. In both cases, the ﬂip-ﬂop reseted if a given total amount of time t0 passed since its activation, allowing the process to start over.

To mimick Hebbian learning, we assumed that neuron B always activated with a delay ∆t compared to neuron A. Note that ∆t could be negative, if B actually ﬁred before A. Then, for a given value of ∆t, we applied the above procedure 8 times, and measured the conductance change of the channel at the end (see Fig. S4).

If A activates just before B, the system will be subject to a few negative spikes followed by many positive ones, increasing its overall conductance (see Fig. S4D). Likewise, If A activates just after B, the system receives a few positive spikes and many negative spikes, and its conductance is lowered. On the other hand, if |∆t| is comparable to t0, the channel will receive an almost equal amount of positive and negative spikes, leaving its conductance unchanged.

Additional data measured on different systems than the ones presented in Fig. 5-6 from main text are displayed in Fig. S5, demonstrating the robustness of the observed phenomena.

In all cases, we prepared the channel in an intermediate conductance state so that saturation to the state of maximum or minimum conductance is not a problem during the learning process.

### 3 Theory of the nanoﬂuidic memristor

In this section, we detail an analytical model of the nanoﬂuidic memristor, highlighting two distinct mechanisms. The most illustrative difference between the two is the shape of the IV and GV curves under a periodic excitation. In some cases, the GV curve displayed a selfcrossing point (unipolar memristor, proposed mechanism based on Wien effect, section 3.1); in others, it had the shape of an open loop and the IV curve had a self-crossing point instead (bipolar memristor, proposed mechanism based on ionic rectiﬁcation, section 3.2).

If considered in a vacuum, both these effects only yield a memory time on the timescales of milliseconds at best. In section 2.3, we will therefore provide a minimal model explaining the emergence of long-term memory from the coupling of surface processes to bulk transport

between two reservoirs.

We start by recalling that a memristor is a resistor with a hysteretic conductance. In terms of elementary electronics, it is decribed by a set of two equations:

I = G[n(t)]∆V (t), (S2) n˙ = f(n,∆V (t)) (S3)

where I is the electrical current ﬂowing through the device under a time-varying voltage drop ∆V (t), G is the conductance that depends on an internal parameter n, which can be seen as the system’s memory. It evolves according to a dynamical equation (S3), where the dot represents the time derivative.

The goal of this section is to detail, for the two mechanisms, what n physically represents and to derive its evolution equation from the underlying physics. In other words, to explain the memristor effect observed in conﬁned electrolytes, we need to ﬁrst show that they possess several internal conductance states, and then that they are able to retain such states over long periods.

#### 3.1 Unipolar memristors – Wien effect under 2D conﬁnement

In this section, we discuss equation (1) from main text, which describes unipolar memristors (with a self-crossing GV curve). The full derivation can be found in Ref. (17): herein, we only state and discuss the various results for the sake of clarity. In this mechanism, n represents the proportion of ions which are able to move under an electric ﬁeld. All other ions form neutral (and therefore non-conducting) ion pairs, also refered to as Bjerrum pairs (42). If the ﬁeld is strong enough, it will tear some pairs apart, increasing n and the global conductance, in a process known as the (second) Wien effect. If the ﬁeld is turned off, pairs will eventually form again. However, this pairing and unpairing process takes some time, allowing for a memristor effect, akin to an electric arc in a discharge tube: an external voltage is required to ionize the gas and make it conduct current, but the gas will stay conducting for a short time after the voltage is removed (43).

The second Wien effect is a well-known phenomenon observed in weak electrolytes. It was extensively studied by Onsager for bulk electrolytes (44), resulting in an approximate law for the conductance G under an external ﬁeld E:

βe2 4π  E

G(E) G(0) 1 +

+ ... G(0) 1 + B

###### + ... (S4)

E

with β = 1/kBT, E = kBT/eE a lengthscale deﬁned by the external ﬁeld and B the Bjerrum length. Here, G(0) corresponds to the conductance of ions that are already free at thermal equilibrium (i.e. with no external ﬁeld). This results in a sligthly non-linear IV curve:

###### I = G(E)∆V G(0)∆V [1 + α∆V ] (S5)

∆V being the voltage drop associated with the ﬁeld E. Without detailing the (mathematically involved) exact derivation by Onsager, the critical point is that ion pairs form according to a chemical equilibrium given by:

1 τa

1 τd

np (S6) with np the proportion of ion pairs, nf the proportion of free ions, τa and τd the ion pair association and dissociation times, respectively. One has nf + np = 1 and the conductance is simply given by:

n2f −

n˙p =

G[nf] = nfG∞ (S7) where G∞ is the conductance in the fully dissociated case. Overall, the system is able to remember the application of an electric ﬁeld in its recent past over a timescale τa, and Bjerrum pairs can be used to create memristors.

The above process cannot be achieved in bulk water, which fully dissociates all commonly used salts. However, as noted by Ref. (17), ionic interactions are greatly increased under conﬁnement. This results in the formation of non-conducting Bjerrum pairs, sometimes to the point that there are no ‘free’ ions left at thermal equilibrium. In this case, the conductance vanishes in absence of an electric ﬁeld, G(0) = 0, and it can be shown that:

###### G(E) ∝ −Eα (S8)

with α > 1 scaling like the strength of ionic interactions. In typical cases, one has α ∼ 2. In many experimental examples, however, a non-zero conductance remains even in the absence of voltage. Taking into account the fact that there may actually be a few free ions left at equilibrium, we then write:

α

G(E) = G0 + G1 |E| E0

(S9) with G0 G1. This corresponds to equation (1) of main text. The number of ion pairs play the role of an internal state variable governing the system’s conductance. It should be noted, however, that the value of G0 was found to vary from device to device (even with similar dimensions), although the general shape of the IV curves was preserved, see Fig. S11.

#### 3.2 Bipolar memristors – Ionic rectiﬁcation

The above mechanism, based on Wien effect, can only provide an explanation for the unipolar memristor effect, as only the absolute magnitude of voltage, and not its sign, governs the dynamics of ion pairs. Consequently, bipolar memristors must have a different origin, as they display different conductance states depending on the sign of applied voltage

This observation is remindful of ionic rectiﬁcation and nanoﬂuidic diode (Fig. S6). This phenomenon typically appears in systems that are spatially asymmetric, e.g. conical pores (geometrical asymmetry) (45), channels connecting reservoirs of different salt concentrations (chemical asymmetry) (46) or with an inhomogeneous surface charge (electrostatic asymmetry) (47). In Ref. (48), the authors show that in all those cases the underlying mechanism is the same: the local value of the conductivity is increased where surface effects are the strongest (e.g., where the channel is the thinnest, salt concentration the lowest or surface charge the highest). Globally, the system then behaves like a PN junction: when current ﬂow from the side of highest conductivity to that of lowest conductivity, ions accumulate inside the channel and conductance increases. Conversely, conductance is lowered if current ﬂows from the side of lowest conductivity.

For the sake of example, let us consider a 2D nanochannel with varying thickness h(x) or

surface charge Σ(x), x being the direction along the channel. The local value of salt concentration c(x) will depend on h(x), Σ(x) and the salt concentration in the reservoirs c0. The exact relation will depend on wether or not the system is in the Debye overlap regime. If the Debye length is large compared to the channel’s thickness, then conductivity reads:

e2D kBT

g(x) = 2w

(ec0h(x))2 + Σ(x)2 (S10)

whereas in the opposite regime (Debye length small compared to h) it reads:

e2D kBT

g(x) = 2w

(ec0h(x) + |Σ(x)|) (S11)

with w the channel’s width, D the diffusion coefﬁcient of ions (assumed to be the same for both cations and anions), e the elementary charge and T temperature. In particular, in the case of strong surface charges (Σ hec), conductance is governed by the surface charge alone:

e2D kBT

g ∼ 2w

Σ (S12)

In addition, carbon-based nanochannels like activated carbon channels are known for their high hydrodynamic slip-length (16). Due to the differential friction of ions and water molecules on the channel’s walls, hydrodynamic slippage yields a correction to the conductance that scales like:

bΣ2 η

(S13)

∆g ∝

- where b is the slip length and η the viscosity of water. In what follows, we will not discuss further the impact of slippage, but the two above equations show how even thin channels can reach a conductance of the order of 100nS thanks to their strong surface charge.

In all cases, conductivity can always be expressed in terms of the Dukhin number deﬁned as:

Σ(x) ec0h(x)

(S14) and it increases with Du in all cases. Several regimes can now be identiﬁed:

Du(x) =

- 1. Du 1 in the entire channel: bulk conduction dominates and the system conducts linearly; there is no ionic rectiﬁcation.
- 2. Du 1 in the entire channel: surface conduction dominates, and conductance is essentially given by counterions of the surface charge. As the number of counterions is ﬁxed, there can be no accumulation nor depletion of ions in the channel, and no ionic rectiﬁcation.
- 3. Du ∼ 1 in at least parts of the channel, and is inhomogeneous: ionic rectiﬁcation can occur.

Quantitatively, Ref. (48) computes the global conductance of a channel with a constant gradient of Dukhin number, in the absence of Debye overlap. The obtained ratio of the maximum conductance of the channel (for a strongly positive voltage) to its minimum conductance (for a strongly negative voltage) is given by:

Gmax Gmin

β =

1 + 2Dumin 1 + 2Dumax

Dumax Dumin

=

(S15)

where Dumin and Dumax are the minimum and maximum values of the Dukhin number, respectively.

The bipolar memristor effect was typically observed in activated carbon channels at low salt concentration. Typical parameters are Σ ∼ 0.1C/m2, c0 ∼ 1mM and h ∼ 10nm, corresponding to Du ∼ 102. Yet, we observed ionic rectiﬁcation with β ∼ 1 − 5, corresponding to Dumin ∼ 1 in the above equation (assuming Dumax 1). Such variations of the Dukhin number over several orders of magnitude across the channel cannot be accounted for by ﬂuctuations of the channel’s height or surface charge, especially in the case of pristine MoS2 channels, which are atomically smooth throughout. Therefore, it seems more reasonable to attribute the ionic rectiﬁcation observed in 2D nanochannels to entry effects: the nanoﬂuidic device is deposited on a SiNx membrane, which is typically much thicker than the device itself (500nm versus ∼50nm, respectively). The hole in the bottom layer thus could act as an additional chan-

nel in series with the nanoﬂuidic device, with similar surface charge but much larger spatial extension (∼ 1µm), yielding Du ∼ 1.

This asymmetry in entry effects could be the source of an accumulation or a depletion of ions inside the channel, depending on the sign of voltage.

#### 3.3 Minimal model of a nanochannel with long-term memory

In this section, we complement the above analysis by showing how long-term memory can emerge from interfacial processes in 2D nanochannels. We ﬁrst show how the rectiﬁcation mechanism can be slowed down considerably if there is adsorption of ions on the channel’s walls. This allows us to derive a minimal model with analytical solutions, which can then be extended to more complex cases, like that of the second Wien effect. However, we start by taking a step back to analyze the nature of nanoﬂuidic memory.

###### 3.3.1 What does it mean for a nanochannel to have memory?

In this section, we discuss what we really measure in a memristor experiment, and how we can quantify a system’s memory, with the help of a simplistic advection-diffusion model.

We ﬁrst focus on channels exhibiting ionic rectiﬁcation. Rather than taking the model presented in previous section, with geometrical asymmetry, we simplify the problem even further. We assume that the channel has a concentration c of ions, and is connected to two reservoirs. We introduce an ad hoc asymmetry by assuming that the reservoir on the left of the channel has concentration cL and the reservoir on the right cR, to mimick ionic rectiﬁcation while keeping mathematical complexity at a minimal level. Lastly, we assume that there is an external forcing f driving particles from the left to the right. For the sake of simplicity, we work with units such that the diffusion time across the channel, L2/D, is equal to 1/2.

In a continuous problem, the particle ﬂux would be:

j(x,t) = −

- 1

- 2

∂xc + f(t)c(x,t) = jdiff + jadv (S16)

Note that the diffusive part jdiff is an artefact: it exists because we replaced a spatial asymmetry by a concentration gradient, resulting in a global diffusive ﬂux; it is irrelevant in actual experiments. The real physical quantity of interest is therefore jadv. In practice, we measure this ﬂux

- at the electrodes, i.e. at both ends of the channel, without access to the full spatial dependence of j. In a time-independent problem with f(t) = f0 at all times, ﬂux is conserved and this does

is the spatial average of c when the channel is subject for a forcing f0 for a very long time. In the quasistatic limit, one would replace f0 by a slow-varying forcing f(t):

, where c ∞,f

not matter; we obtain jmeasured = f0 × c ∞,f

0

0

###### jquasistatic = f(t) × c ∞,f(t) (S17)

- where c ∞,f(t) is now the spatial average of c when the channel is subject for a forcing “frozen” at a speciﬁc value f(t). A memory effect is any deviation from the above equation; it translates the fact that the forcing is varying faster than the time needed to equilibrate the system quasistatically. In other words, memory is stored in the number of particles that can contribute to conduction.

However, when the system is not in the quasistatic limit, ﬂux is not conserved across the system. It is then hard to make exact sense of what is being actually measured at the electrodes; in the following, we admit we may still assume we measure a spatial average of the advection ﬂux, but that this average is now instantaneous:

1 L

jmeasured f(t) c(x,t) x = f(t)

c(x,t)dx (S18)

Assuming the forcing is sinusoidal f(t) = f0 cosωt, one can then compute the area of the hysteretic loop in the conductance-voltage curve:

2π/ω

ωf0 c(x,t) x sinωtdt (S19) The bigger A is, the more memory the system has of its recent past. We thus deﬁne the memory timescale as τm = 2π/ωm such that A(ωm) is maximum.

A(ω) = c(x,t) x df =

0

There is, however, no simple way to solve the advection-diffusion equation under periodic forcing, even in 1D, so we simplify the problem further by writing an approximate equation for the mean c only, see Fig. S7A:

c˙ + c

cL − cR 2

cL + cR 2

+ f(t)

(S20)

This model is summed up in Fig. S7. In all what follows, we drop the  ·  for the sake of simplicity. This yields:

cL + cR 2

c(t) =

cL − cR 2

cosωt + ω sinωt 1 + ω2

+ f0

so that the loop area is:

cL − cR 2

ω ω2 + 1

A(ω) = f0

This yields τm = 2π, or, in dimensional terms:

(S21)

(S22)

L2 D

τm = π

(S23)

This is perfectly intuitive: since information is encoded in the particle number, it cannot be retained for more than the diffusion time. However, nanochannels have L < 10µm, meaning that the diffusion time cannot exceed a second, contrary to what is observed in experiments (τm ∼ 1 hour).

Before we move on to a slightly modiﬁed version of this model to account for this, let us make the following remark. The quasistatic solution to the above problem is:

cL − cR 2

cL + cR 2

cqs[f] =

+ f

(S24)

The instantaneous solution we obtained can be rewritten into the following form:

c(t) =

+∞

e−s/τ τ

cqs[f(t − s)]

0

ds (S25)

where τ = 1, equal to τm up to a factor of order unity. This equation will allow us to model more complex situation, where analytical solutions do not exist.

###### 3.3.2 Adsorption-desorption model

To complement the above model, which does not account for long memory times observed in experiments, we consider the possibility of ion adsorbing on the channel’s walls, and denote the number of adsorbed particles by σ. Introducing k and λ, the adsorption and desorption rates, respectively, we obtain (see Fig. S7B):

cL − cR

cL + cR 2

2 − kc + λσ (S26) σ˙ = kc − λσ (S27)

+ f(t)

c˙ + c =

It again can be solved analytically:

cL + cR 2

c(t) =

cL − cR 2

A(ω) = f0

[λ2 + (1 + k)ω2]cosωt + ω [λ(k + λ) + ω2]sinωt λ2 + (1 + k)2 + 2kλ + λ2 ω2 + ω4

cL − cR 2

+ f0

ω [λ(k + λ) + ω2] λ2 + (1 + k)2 + 2kλ + λ2 ω2 + ω4

The memory timescale is then given by:

(S28)

(S29)

λ(k + λ) + 3ω2 λ2 + (1 + k)2 + 2kλ + λ2 ω2 + ω4 (S30) ... = ω λ(k + λ) + ω2 2 (1 + k)2 + kλ + λ2 ω + 4ω3 (S31)

There is no closed-form solution to this last equation, but we can extract an approximate solution when surface effects strongly dominate (k λ and k 1):

λ k

ωm ∼

1 (S32)

In other words, the memory time reads in this case:

L2 D

σ∞ c∞

(S33)

τm = 2π

where σ∞ and c∞ are the values of σ and c at chemical equilibrium, respectively. The ratio σ∞/c∞ appearing in the above equation is the analogue of the Dukhin number (1), which measures the importance of the surface charge of a channel with respect to the bulk concentration in ions. This number can reach several hundreds, so τm can be of the order of several minutes.

Qualitatively, the above equation can be recovered from a semi-quantitative argument as follows. The memory time is given by the maximum time a particle can stay within the channel. It will reach one of the reservoirs if left free for more than L2/D, by randomly diffusing along the channel. However, every 1/k 1, the particle is adsorbed and stops moving, only liberated after a time 1/λ. Along its course through the channel, there will therefore be kL2/D 1 such events of duration 1/λ. The total time spent inside the channel is the sum of the “travelling time” and “resting time”:

kL2 D

L2 D ∼

L2 D

k λ

1 λ

(S34) The last approximation holds since we assumed that k λ, such that the total resting time is much larger than the travelling time.

τm ∼

+

To complement the above minimal model, we also computed a numerical solution of the 1D advection-diffusion under periodic forcing and with adsorption, yielding similar results (not reported here).

###### 3.3.3 Wien effect

In the previous model, long-term memory emerges from a stop-and-go mechanism of ions being adsorbed and desorbed. However, this process is more general than the speciﬁc physics of adsorption, and we can write a similar system taking into account a Wien effect mechanism:

c˙ + c = c0 −

1 τa

c2 −

p˙ =

1 τd[f(t)]

1 τa

p (S35)

c2 +

1 τd[f(t)]

p (S36)

Here, c is the concentration of ions that can contribute to conduction (free ions or polyelectrolytes), while p represents the concentration of pairs. This system is, however, non-linear in both c and f, and as such admits no analytical solution, but is qualitatively similar to the previous linear case. Rather than looking for an approximate solution of this already simplistic model, we instead use the ansatz derived above.

###### 3.3.4 A simple ansatz - Determination of the memory time

Here, we detail how we ﬁtted the curves presented in Figure 3 of main text. As per sections 3.1 and 3.2, we have two models describing the conductance of a 2D nanochannel under a constant electrical forcing. As shown by equation (S25), this conductance becomes in the timevaryingcase:

+∞

e−s/τ τ

ds (S37)

Gqs[∆V (t − s)]

G(t) =

0

where Gqs is the conductance in the stationary case (i.e. if the voltage was ‘frozen’ at the value ∆V (t − s) for an inﬁnite amount of time). Depending on cases, we use the following expressions:

Gqs(∆V ) = G1∆V α, α = 2 − 3 (Wien effect) (S38) Gqs(∆V ) =

G+, if ∆V > 0, G−, if ∆V < 0

(Ionic rectiﬁcation) (S39)

We ﬁrst use these models to extract the quasistatic limit of experimental curves, and we then “turn on” memory effects by plugging the chosen model into equation (S25). To assess the robustness of our approach, we can determine the memory time through two methods:

- • By using τ as a ﬁtting parameter in equation (S25).
- • By noticing that, upon correct renormalization (see below), the area of the loop in the IV curve should take the form:

ωτm 1 + ω2τm2

A∗(ω) K

(S40)

with a theoretical value K = 1 in the adsorption-desorption model, and using τm as a ﬁtting parameter in this last equation. In the case of the pairing-unpairing model, we cannot derive the exact expression of A∗, but we use the above expression as an approximative ansatz, with K as a ﬁtting parameter.

Both quantities τ and τm can be interpreted as memory timescales, being equal up to a factor π in the minimal model. In practice, both methods yield similar results (τ ∼ τm ∼ 100s,

see Figure 4 from main text), but we believe the second one (τm) to be more robust as it is determined using more experimental data points obtained using several frequencies.

Let us now detail how we normalize the loop area. Memristive devices cycle between different conductance states. The largest loop that could possibly be observed would be in the case where the device switches abruptly between the lowest and the highest conductance states, Goff and Gon, whenever it reaches ∆V = ±V0 (for bipolar memristors) or ∆V = 0 and |∆V | = V0 (for unipolar memristors). The conductance-voltage curve then takes the shape of a rectangle of size 2V0 × (Gon − Goff). The IV curve then takes the shape of two triangles of total area V02 × (Gon − Goff), which we therefore use for normalization. For each case, we determine Goff and Gon graphically using data with the lowest frequency for a given device and salt concentration. In the case of devices with mixed unipolar-bipolar behavior, we determined both extremal conductance for positive and negative voltage, and then used 0.5V02 × (Gon,+ − Goff,+) + 0.5V02 × (Gon,− − Goff,−) as normalization. This normalization process is summed up in Fig. S8.

#### 3.4 Mixed mechanisms and shape of the IV curve

The two mechanisms detailed above are not mutually exclusive, as some nanoﬂuidic systems can display both ionic rectiﬁcation and allow the formation of ionic pairs. In particular, pristine MoS2 were found to display both behaviour depending on experimental conditions (Fig. S10). Additionally, some of our experimental data do not fall in either of the two phenomenologies: they displayed two crossing points in their IV curve, for example.

To shed light on these ‘mixed’ cases, we designed a simple model of a memristor that is intermediate between unipolar and bipolar cases:

I(t) = G(t) × V (t) (S41) G(t) =

+∞

e−s/τ τ

(S42) Gqs(v) = Gunipolar(1 + αv2) + Gbipolar(1 + βv) (S43)

Gqs(V (t − s))

0

with I the ionic current, V voltage, G the instantaneous conductance, Gqs the quasistatic conductance and τ, Gunipolar, Gbipolar, α and β some constants. For different values of the parameters, this model can be purely unipolar, purely bipolar, or intermediate between the two. Various examples of IV and GV curves for different values of parameters are shown on Fig. S17, along an example of experimental data displaying this mixed behaviour. We note that there exists a “critical point” such that the GV curve has no crossing point; however, it develops a cusp, which transforms into a crossing point when parameters are varied.

### 4 Additional experimental data

#### 4.1 Pristine MoS2 channels

We provide additional data to characterize the memristor effect in pristine MoS2 channels, which is found to be robust when we vary salt concentration, channel height and the chemical nature of the electrolyte.

- On Fig. S9, we show that the memristor effect can be observed in pristine MoS2 channels

regardless of the electrolyte used (KCl, NaCl, LiCl, CaCl2, NiSO4), asserting its robustness. Despite variations in conductance, all these curves display the same non-linear general shape remindful of the Wien effect.

- On Fig. S10, we provide additional data for the memristor effect in bilayer pristine MoS2

channels with potassium chloride solutions of various concentrations. In particular, we notice that the system behaves like a bipolar memristor at low salt concentration.

- On Fig. S11, we show the evolution of loops in IV curve at ﬁxed frequency and salt con-

centration, but with increasing channel height. We ﬁnd that the effect is most visible in thin channels, and that the loop collapses to a straight line in larger channels. This shows that memory effects can only be observed if conﬁnement is sufﬁciently strong so that ion-ion interactions are enhanced, allowing the formation of ion pairs.

Lastly, Fig. S12 shows the determination of the memory time of three different devices (and two salt concentrations) from the evolution of the loop area with frequency. We obtain values

between 50 and 400s.

#### 4.2 Activated carbon channels

Additional data characterizing the inﬂuence of salt concentration on memristive effects in activated carbon channels are presented in Fig. S13. They notably include raw data for Fig. 2A of main text. We observe that salt concentration variations have little effect on the memory of thinner channels (Fig. S13A-B), while this inﬂuence is more visible for devices above 10nm in thickness. This notably shows that, in more conﬁned systems, interfacial processes are stronger than bulk effects.

In addition, the memristor effect can also be observed with salts other than CaCl2, as shown in Fig. S14 for KCl and AlCl3.

We also provide additional data regarding the effect of voltage frequency (Fig. S15), corresponding to Fig. 4C of main text. These data allow us to compute the memory time of each activated system as the inverse of the frequency such that the loop in the IV curve is the largest. We obtain values spanning from 50 to 400s, in a similar range as pristine MoS2 channels. Such variations may be explained by the variability of the surface state of activated carbon channels following the etching in low pressure water vapor.

### 5 Detailed list of supplementary ﬁgures

We summarize below the content of all supplementary ﬁgures:

- • Fig. S1: Nanofabrication of pristine MoS2 channels.
- • Fig. S2: Nanofabrication of activated carbon channels.
- • Fig. S3: Details of the long-term potentation algorithm.
- • Fig. S4: Details of the Hebbian learning algorithm
- • Fig. S5: Additional data for long-term potentiation and Hebbian learning.

- • Fig. S6: Sources of ionic rectiﬁcation in nanoﬂuidics.
- • Fig. S7: Minimal model of nanoﬂuidic memory.
- • Fig. S8: Normalization process of loop area in memristive GV curves.
- • Fig. S9: Additional data: pristine MoS2 channels with different salt types
- • Fig. S10: Additional data: pristine MoS2 channels with different salt concentrations.
- • Fig. S11: Additional data: pristine MoS2 channels of different heights.
- • Fig. S12: Determination of the memory time of pristine MoS2 channels.
- • Fig. S13: Additional data: activated carbon channels with different salt concentrations and different heights.
- • Fig. S14: Activated carbon channels with different salt types.
- • Fig. S15: Determination of the memory time of activated carbon channels.
- • Fig. S16: Inﬂuence of pH.
- • Fig. S17: ‘Mixed’ memristor types (theoretical model and experimental example).

[Figure 5]

- Fig. S1. Schematic ﬂow-chart in cross-sectional view and corresponding optical and AFM images. Step I: Preparation of the top-spacer layers on silicon/silicon oxide (SiO2) wafer.

- A Graphene is mechanically exfoliated; the thickness of this graphene ﬂake will determine the height (h) of the channel. Bottom panel: Optical image of a 3-layer graphene spacer.
- B Patterning of the spacer using electron beam lithography (EBL) and etching into parallel strips. Bottom panel: atomic force microscopy (AFM) image and height proﬁle of the patterned graphene-spacer (h ∼ 1.2 nm and w ∼ 150 nm). C Transfer of MoS2 ﬂake as a top layer over graphene spacer. Bottom panel: Optical image of the top-spacer stack. Step II: Assembly of the tri-crystal (top-spacer-bottom) stack on silicon/silicon nitride (SiNx) wafer. D Transfer of a MoS2 ﬂake onto SiNx membrane bearing a hole (∼ 3 × 50µm), to serve as bottom wall of the channel. E Dry etching of the MoS2 bottom layer from the back of the SiNx. F Transfer of the top (MoS2)-spacer (graphene) stack prepared in C over the bottom MoS2 prepared in E. G Patterned gold (Au) deposition over the tri-crystal stack. H With the Au strip as a mask to protect the underneath channels, the surrounding regions are etched away. The gold strip thus determines the channel length (L). I Optical images (left: reﬂection mode, right: transmission

mode) of the ﬁnal channel device. The tricrystal device is underneath the gold strip on the SiNx membrane. Scale bar in all images represents 20µm.

|1|
|---|

|2|
|---|

|3|
|---|

Graphite

SiN

Si02

Si

Si

Apperture

[Figure 6]

[Figure 7]

[Figure 8]

[Figure 9]

[Figure 10]

[Figure 11]

Bottom Layer

Top Layer

Top layer

Sin window edge

Channel

Bottom layer

###### Fig. S2. Fabrication of activated carbon channels. Step 1: Patterning of the bottom layer.

Up: 2D side view of a graphite bottom layer crystal after the patterning on a Si/SiO2 substrate. Middle: 3D view of the patterning process. A square-shaped hole and four trenches connected to the hole are represented. Bottom layer graphite is dark grey and the Si/SiO2 substrate is light pink. The electron ﬂux, represented as a green tip, enables selective removal of matter. Down: AFM image of the bottom layer after etching. Scale bar represents 1µm. Step 2: Dry transfer of the top layer. Up: 2D side view. A top layer crystal is added above the bottom layer. Middle: 3D view of the device after the transfer of the top layer, represented in glassy transparent grey. Down: SEM image of a device at that stage. Four channels are visible in white. The bottom layer hole remains visible through the top layer. Scale bar represents 5µm. Step 3: Wet transfer on the Si/SiNx membrane. Up: 2D side view. Middle: 3D view, with the SiN membrane in green. The circular aperture in the SiNx membrane is visible by transparency. Down: Optical microscope image of a ﬁnished device. Scale bar represents 10µm.

##### A B

- 0.8
- 1

0.2

0

Potential(V)

Potential(V)

- -1
- -0.8
- -0.6
- -0.4
- -0.2

n=10

0.6

0.4

n=10

0.2

0

0 50 100

0 20 40 60 80 100

Time (s)

Time (s)

###### Fig. S3. Long-term modiﬁcation of a nanochannel conductance using voltage pulses. (A) A ‘write’ pulse (+1V, 10s), followed by ten ‘read’ pulses (+0.1V, 10s) to study the relaxation of the conductance. (B) An ‘erase’ pulse (−1V, 10s), followed by ten ‘read’ pulses (+0.1V, 10s).

|450 500 550<br><br>Time (s)<br><br>|A spike|
|---|
<br><br>-0.2<br><br>0<br><br>0.2<br><br>0.4<br><br>0.6<br><br>0.8<br>1<br><br><br>Potential(V)<br><br>Relative spike timing: 5s<br><br>B|
|---|

A

- 0.8
- 1

0.6

Potential(V)

Potential(V)

0.4

0.2

0

-0.2

500 1000 1500

Time (s)

C D E

- 0.5
- 1

- 0.5
- 1

A spike

Relative spike timing: -5s

Relative spike timing: 55s

Relative spike timing: -55s

0.2

B spike

A spike

0

Potential(V)

Potential(V)

Potential(V)

- -1
- -0.8
- -0.6
- -0.4
- -0.2

0

0

B spike

B spike

A spike

-0.5

-0.5

2150 2200 2250

1.945 1.95 1.955

1.885 1.89 1.895

Time (s)

Time (s) 104

Time (s) 104

- Fig. S4. Algorithm for the implementation of Hebb’s rule with activated carbon channels. (A) Voltage input emulating 8 successive activation of a pre-synaptic and a post-synaptic neuron with a relative spike timing ∆t = 10s. The conductance is read before and after with low amplitude ‘read’ pulses, highlighted by red circles. (B to E) Examples of input voltage for various relative spike timings of the two neurons.

A B

88

86

- 0.5
- 1

30

84

Conductance(nS)

20

82

80

10

Potential(V)

Current(nA)

78

time(s)

500 600

0

0

76

100 200 300

74

- -30
- -20
- -10

72

- -1
- -0.5

70

0 200 400 600 800 1000

Time (s)

- C D

25

Conductance change (%)

30

Conductancechange(%)

20

20

15

10

-60 -40 -20 20 40 60

10

Relative Spike timing (s)

- -30

-20

- -10

5

0

0 20 40 60

Spike number

###### Fig. S5. Additional data for the implementation of neuromorphic computing with acti-

vated carbon channels. The salt used is CaCl2, 1mM. (A) Evolution of the ionic current (red) under voltage pulses of constant polarity (blue) (see Fig. 5A of main text). (B) Conductance change following a positive voltage pulse of 1V in amplitude and a duration of 20s (see Fig. 5B of main text). The conductance is read with an alternating square voltage of 0.1V in amplitude and a period of 20s. (C) Revsersible, long-term modiﬁcation of a nanochannel’s conductance. 30 write spikes (+1 V, 10 s) are applied, followed by 30 erase spikes (-1 V, 10 s) which bring back the system to its initial state. Between each spike, the conductance is let to stabilize during two minutes and is then measured with a read pulse (0.1 V, 5 s), see Fig. 5C of main text. (D) Conductance change after 8 successive activations of the two neurons, in percentage of the initial conductance and as function of the relative activation timing of the simulated neurons (see Fig. 6D of main text).

###### A B C

Confinement gradient Surface charge gradient Concentration gradient

- Fig. S6. Possible sources of ionic rectiﬁcation. Nanochannel with variable (A) height, (B) surface charge or (C) concentration gradient. In all three cases, a gradient of Dukhin number is established across the channel, resulting in a conductivity gradient and ionic rectiﬁcation.

- A Left reservoir Channel Right reservoir

- B Left reservoir Channel Right reservoir

Surface

Ionic rectification

Rectification + Surface effects

External force

C

|2<br><br>4<br><br>6<br><br>8<br><br>|Rectification<br><br>Rectification+Surface|
|---|
<br><br>|Forcing<br><br>Advection flux|
|---|---|
|-0.5<br><br>-2|0.5|

- Fig. S7. Minimal model of nanoﬂuidic memory. (A) Minimal model of purely diffusive memory. The nanochannel is modeled by a single point that exchanges particles with two reservoirs. The concentration difference between reservoirs plays the role of geometrical asymmetry. Memory is stored in the concentration inside the channel c, and the memory time is the diffusion timescale. (B) Same minimal model, but with particle adsorption on the channel’s walls. Transport is now limited by a stop-and-go mechanism of particles adsorbing and desorbing from the walls, giving rise to a memory time orders of magnitude larger than diffusion. (C) Memristor effect in the minimal model, as shown by the loop in the IV curve, in dimensionless units. The blue curve corresponds to the model described in panel A (section 3.3.1), and the red one in panel B (section 3.3.2). Memory effects are visible at low frequency only when surface effects are taken into account.

- A
- B

Gon

Conductance (nS)

300

250

Gon- Go 

200

150

V0

Go 

-1 -0.5 0 0.5 1

Voltage (V)

Gon

Conductance

Go 

0 Voltage

C

Gon,+

Conductance (nS)

Gon,-

30

25

20

Gon,+- Go ,+

15

10

5

Go ,- Go ,+

-0.4 -0.2 0 0.2 0.4

Voltage (V)

V0

###### D

Conductance

Gon,+ Gon,-

Go ,-

Go ,+

0 Voltage

- Fig. S8. Normalization of loop area. (A) Example of an experimental conductance-voltage curve for a bipolar memristor (see Figure 1C from main text), corresponding to an adsorption-

desorption memory mechanism, with the graphical determination of Gon and Goff. (B) Idealized loop in the conductance-voltage curve. Its area is used as a normalization factor for a bipolar memristor. (C) Example of an experimental conductance-voltage curve for a unipolar memristor (see Fig. 1B from main text), corresponding to an Wien effect memory mechanism, with the graphical determination of Gon,± and Goff,±. (D) Idealized loop in the conductance-voltage curve, deﬁning the normalization factor for a unipolar memristor. Note that the difference between Goff,− and Goff,+ is exaggerated compared to experimental data, to allow easier visualization.

B C

|20<br><br>40<br><br>60<br><br>NaCl 1M 2.7 nm 11mHz|Voltage (V)<br><br>Current (nA)|
|---|---|
|-0.5<br><br>-60<br>-40<br>-20<br><br><br>|0.5|

|100<br><br>200<br><br>300<br><br>A<br><br>KCl 3M 0.68 nm 3mHz|Voltage (V)<br><br>Current (nA)|
|---|---|
|-0.5<br><br>-300<br>-200<br>-100<br>|0.5<br><br>|

|20<br><br>LiCl 1M 40 2.7 nm 11mHz|Voltage (V)<br><br>Current (nA)|
|---|---|
|-0.5<br><br>-40<br>-20<br>|0.5<br><br>|

E

D

|5<br><br>10<br><br>15<br><br>NiSO4 2M 0.68 nm<br><br>3mHz|Voltage (V)<br><br>Current (nA)|
|---|---|
|-0.5<br><br>-15<br>-10<br>-5<br><br><br>|0.5|

|20<br><br>CaCl2 3M 40<br><br>0.68 nm 3mHz|Voltage (V)<br><br>Current (nA)|
|---|---|
|-0.5<br><br>-20|0.5|

- Fig. S9. Evolution of the memristor effect with various electrolytes (pristine channels). (A to E) Current-voltage characteristics of an activated carbon channel with height under a voltage sweep of amplitude 0.75V. Other parameters (salt type, salt concentration, channel height and frequency) are speciﬁed on each panel.

|A<br><br>0.5<br><br>KCl 0.01M 0.68 nm 3mHz|Voltage (V)<br><br>Current (nA)<br><br>|
|---|---|
|-0.5<br><br>-0.5|0.5<br><br>|

|C<br><br>KCl 1M 0.68 nm 3mHz<br><br>50<br><br>100<br><br>150|Voltage (V)<br><br>Current (nA)|
|---|---|
|-0.5<br><br>-150<br>-100<br>-50<br>|0.5<br><br>|

B

|5<br><br>KCl 0.1M<br><br>0.68 nm 3mHz|Voltage (V)<br><br>Current (nA)<br><br>|
|---|---|
|-0.5<br><br>-5|0.5|

D

|100<br><br>200<br><br>300<br><br>KCl 3M 0.68 nm 3mHz|Voltage (V)<br><br>Current (nA)|
|---|---|
|-0.5<br><br>-300<br>-200<br>-100<br><br><br>|0.5|

###### Fig. S10. Evolution of the memristor effect with salt concentration (pristine channels). (A

to D) Current-voltage characteristics of a pristine MoS2 channel with height h = 0.68nm, ﬁlled with potassium chloride at various concentrations, under a voltage sweep of amplitude 0.75V and frequency 3mHz. Orange curve indicates a self-crossing loop, while blue curves do not self-intersect.

|h = 0.68 nm KCl 1M<br><br>A<br><br>50<br><br>100<br><br>150|Voltage<br><br>Current (nA)|
|---|---|
|-0.5<br><br>-150<br>-100<br>-50<br>|0.5<br><br>|

|50<br><br>100<br><br>h = 0.68 nm KCl 1M (other device)<br><br>B|Voltage (V)<br><br>Current (nA)|
|---|---|
|-0.5<br><br>-100<br>-50<br>|0.5|

|50<br><br>h = 2.8 nm KCl 1M<br><br>C|Voltage (V)<br><br>Current (nA)|
|---|---|
|-0.5<br><br>-50<br><br>|0.5|

(V)

|5<br><br>10<br><br>h = 86 nm KCl 1M<br><br>E|Voltage (V)<br><br>Current (μA)|
|---|---|
|-0.5<br><br>-10<br>-5<br>|0.5|

|h = 8.5 nm KCl 1M<br><br>D<br><br>200<br><br>400<br><br>600|Current (nA)|
|---|---|
|-0.5<br><br>-600<br>-400<br>-200<br>|0.5Voltage (V)<br><br>|

)

###### Fig. S11. Evolution of memristive effects with channel height (pristine channels). Current-

voltage characteristics of pristine MoS2 channels of different heights ﬁlled with potassium chloride, under a voltage sweep (frequency f = 3mHz). (A and B) Two different devices with height h = 0.68nm (with salt concentration 1M, voltage amplitude 0.75V). (C to E) Devices with height h = 2.8, 8.5 and 86nm, respectively (salt concentration 1M, voltage amplitude 0.75V or 1V).

[Figure 12]

###### Fig. S12. Evolution of the memristor effect with voltage frequency (pristine channels).

Current-voltage characteristics of different pristine MoS2 channels with channel heights h = 0.68nm (A and B) and 7nm (C and D), the electrolyte is 1M KCl for A, C and 3M KCl for

- B, D; applied voltage is sinusoidal with frequency ranging from 0.6 mHz to 200 mHz. The normalized loop area vs frequency of A is presented in main Fig. 4C of main text. Insets represent the corresponding normalized areas of the different current-voltage characteristics for that device. The error bars represent the area variation between three successive voltage sweeps.

A Normalized current B

Normalized current

|CaCl2 5nm<br><br>1mHz|Potential (V)<br><br>0.5|
|---|---|
|-1 -0.5|0.5 1<br><br>-0.5<br><br>|1 mM<br><br>10 mM<br><br>100 mM<br><br>1M|
|---|
|

|CaCl2 7nm<br><br>1mHz|Potential<br><br>0.5|
|---|---|
|-0.5|0.5 1<br><br>-0.5<br><br>|1 mM<br><br>10 mM<br><br>100 mM<br><br>1M|
|---|
<br><br>|

(V)

-

-1

- C Normalized current D CaCl

|CaCl2 12nm<br><br>1mHz|Potential (V)<br><br>0.5|
|---|---|
|-1 -0.5<br><br>|0.5 1<br><br>-0.5<br><br>|1 mM<br><br>10 mM<br><br>100 mM<br><br>1M|
|---|
|

Normalized current

|-0.5<br><br>2<br><br>13nm 1mHz|0.5<br><br>0.5|
|---|---|
| |Potential (V)<br><br>-0.5<br><br>|1M<br><br>1 mM<br><br>10 mM<br><br>100 mM<br><br>|
|---|
<br><br>|

-1

-1

|1M<br><br>1 mM<br><br>10 mM<br><br>100 mM<br><br>|
|---|

-1

| | | |
|---|---|---|
| | | |

###### Fig. S13. Evolution of the memristor effect with salt concentration (activated channels).

(A to D) Current-voltage characteristics of four different activated carbon channels, with CaCl2 and AC voltage oscillating between ±0.8V at 1mHz. The current is normalized by its maximum value for each salt concentration. In each case, current is normalized by its maximum absolute value, to allow easier comparison between different datasets.

###### A B C

|0.05<br><br>0.1<br><br>0.15<br><br>CaCl2 1mM 0.2<br><br>|Voltage (V)<br><br>Current (μA)|
|---|---|
|-0.5|0.5<br><br>-0.05|

|-0.8 -0.4<br><br>20<br><br>40<br><br>KCl 1mM 60|0.4 0.8<br><br>Current (nA)|
|---|---|
|-80<br>-60<br>-40<br>-20<br>|Voltage (V)<br><br>|

|50<br><br>100<br><br>150<br><br>AlCl3 1mM|Voltage (V)<br><br>Current (nA)|
|---|---|
|-0.8 -0.4<br><br>-50|0.4 0.8|

- Fig. S14. Evolution of the memristor effect with various electrolytes (activated channels). (A to C) Current-voltage characteristics of an activated carbon channel with height h = 13nm, under a voltage sweep of frequency 1mHz and amplitude 0.8V.

###### A

|10<br><br>20<br><br>30<br><br>CaCl2 100mM 4nm<br><br>| |
|---|
<br><br>10-2 10-1<br><br>Frequency (Hz)|Potential (V)<br><br>Current (nA)<br><br>|
|---|---|
|-0.5<br><br>-20<br>-10<br>|0.5<br><br>|100 mHz<br><br>10 mHz<br><br>1 mHz|
|---|
<br><br>1|

0.4

Area

0.2

0

10-3

-1

###### C

|10<br><br>20<br><br>30<br><br>10-4 10-2<br><br>| |
|---|
<br><br>0<br><br>0.2<br><br>0.4<br><br>0.6<br><br>Frequency (Hz)<br><br>CaCl2 100mM 5nm|Potential (V)<br><br>Current (nA)<br><br>|
|---|---|
|-0.5<br><br>-20<br>-10<br>|0.5<br><br>|100 mHz<br><br>3 mHz 1 mHz<br><br>|
|---|
<br><br>1|

Area

-1

###### B

|20<br><br>40<br><br>10-4 10-2<br><br>Frequency (Hz)<br><br>0<br><br>0.2<br><br>0.4<br><br>Area<br><br>CaCl2 1mM 5nm|Potential (V)<br><br>Current (nA)|
|---|---|
|-0.5<br><br>-20|0.5<br><br>|100 mHz<br><br>10 mHZ<br><br>1 mHz<br><br>0.1 mHz|
|---|
<br><br>1|

Area

-1

|10<br><br>20<br><br>10-4 10-2<br><br>| |
|---|
<br><br>0<br><br>0.2<br><br>0.4<br><br>Frequency (Hz) Area<br><br>CaCl2 1mM 7nm|Voltage (V)<br><br>Current (nA)|
|---|---|
|-0.5<br><br>-10<br><br>-1|0.5<br><br>|100 mHz<br><br>30 mHz 10 mHz<br><br>3 mHz 1 mHz<br><br>|
|---|
<br><br>1|

D

-

- Fig. S15. Evolution of the memristor effect with voltage frequency (activated channels). (A to D) Current-voltage characteristics of four different devices ﬁlled with 100 mM or 1 mM CaCl2 (as indicated on each panel). Inset: Normalized area versus frequency. Squares are experimental values and solid lines are theoretical model with memory time parameter, τm equals to 50s (B), 100s (C) and 400s (D). The normalized area vs frequency of the 4nm device (A) is presented in main text Fig 4.C.

|B<br><br>1<br>2<br>3<br><br><br>Activated (10 nm) AlCl3 1 mM 1 mHz|Voltage (V)<br><br>Current (nA)|
|---|---|
|-0.8 -0.4<br><br>-2<br>-1<br>|0.4 0.8<br><br>|pH=9<br><br>pH=5.5<br><br>pH=3|
|---|
|

###### A

|20<br><br>40<br><br>Pristine (0.68 nm) KCl 3 M 10 mHz|Voltage (V)<br><br>Current (nA)|
|---|---|
|-0.4 -0.2<br><br>-40<br>-20<br>|0.2 0.4<br><br>|pH 2.0<br><br>pH 3.7<br><br><br>pH 6.4 pH 8.4<br><br>|
|---|
|

- Fig. S16. Evolution of the memristor effect with pH. (A) Current-voltage characteristics of a

pristine MoS2 channel (height 0.68nm) ﬁlled with 3M KCl under a voltage sweep at 10mHz, for different pH values. (B) IV curve of an activated carbon channel (height 10nm) ﬁlled with AlCl3 1mM under a voltage sweep at 1mHz, for different pH values.

Conductance

A B C

|5<br><br>10<br><br>-1 Voltage 1<br><br>Conductance|Voltage<br><br>Current|
|---|---|
|-1 -0.5<br><br>-5|0.5 1<br><br>Type I (bipolar)|

Conductance

|5<br><br>10<br><br>-1 Voltage 1<br><br>|Voltage<br><br>Current|
|---|---|
|-1 -0.5<br><br>-10<br>-5<br>|0.5 1<br><br>Intermediate|

|5<br><br>10<br><br>-1 Voltage 1<br><br>|Voltage<br><br>Current|
|---|---|
|-1 -0.5<br><br>-10<br>-5<br><br><br>|0.5 1<br><br>Type II (unipolar)|

Conductance (nS)

Conductance

|20<br><br>40<br><br>-1 -0.5 0 0.5 1<br><br>Voltage (V)<br><br>20<br><br>40<br><br>60<br><br>E 80|Voltage (V)<br><br>Current (nA)|
|---|---|
|-0.5<br><br>-20|0.5<br><br>Pristine (0.68 nm) CaCl2 3 M 3 mHz|

D

|5<br><br>10<br><br>-1 Voltage 1<br><br>|Voltage<br><br>Current|
|---|---|
|-1 -0.5<br><br>-5|Critical<br><br>0.5 1|

|-0.1<br><br>Current (nA)|1<br>2<br>3<br>|
|---|---|
|Voltage (V)|-4<br>-3<br>-2<br>-1<br><br><br>|

- Fig. S17. Transition between bipolar and unipolar behavior. (A to D) IV and GV (inset) curves for the minimal model of a ”mixed” memristor (equations S47-S49). All units are arbi-

trary. Parameters: Gunipolar = 3, Gbipolar = 2, τ = 1, V (t) = 1.5sint. (A) α = 0.8, β = 0.2 (bipolar case). The IV curve self-intersects once, but the GV curve does not. (B) α = 0, β = 0.8 (unipolar case). The IV curve does not self-intersect; the GV curve self-intersects on the y axis. (C) α = β = 0.8 (intermediate case). The IV curve self-intersects twice and the GV curves selfintersects outside of the y axis. (D) α = 0.8, β = 0.45 (criticality). The IV curve self-intersects once and the GV curve develops a cusp. (E) Left panel: Example of experimental IV curve showing a ”mixed” memristor behavior, obtained for a pristine MoS2 channel (height 0.68nm) ﬁlled with CaCl2 3M at voltage frequency 3mHz. Red arrows indicate the two crossing points. Inset is the corresponding GV curve. Right panel: Zoom-in on the two crossing points of the IV curve.

