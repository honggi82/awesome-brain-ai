[Figure 1]

## A neuronal network model linking subjective reports and objective physiological data during conscious perception

#### Stanislas Dehaene*†, Claire Sergent*, and Jean-Pierre Changeux‡

*Institut National de la Sante´ et de la Recherche Me´dicale, Unite´ 562, Cognitive Neuroimaging, Institut Fe´de´ratif de Recherche 49, Service Hospitalier Fre´de´ric Joliot, Commissariat a` l’Energie Atomique DSV, 4 Place du Ge´ne´ral Leclerc, 91401 Orsay Cedex, France; and ‡Centre National de la Recherche Scientiﬁque Unite´ de Recherche Associe´e 2182, Re´cepteurs et Cognition, Institut Pasteur, 25 Rue du Dr Roux, 75015 Paris, France

Contributed by Jean-Pierre Changeux, April 30, 2003

The subjective experience of perceiving visual stimuli is accompanied by objective neuronal activity patterns such as sustained activity in primary visual area (V1), ampliﬁcation of perceptual processing, correlation across distant regions, joint parietal, frontal, and cingulate activation, -band oscillations, and P300 waveform. We describe a neuronal network model that aims at explaining how those physiological parameters may cohere with conscious reports. The model proposes that the step of conscious perception, referred to as access awareness, is related to the entry of processed visual stimuli into a global brain state that links distant areas including the prefrontal cortex through reciprocal connections, and thus makes perceptual information reportable by multiple means. We use the model to simulate a classical psychological paradigm: the attentional blink. In addition to reproducing the main objective and subjective features of this paradigm, the model predicts an unique property of nonlinear transition from nonconscious processing to subjective perception. This all-or-none dynamics of conscious perception was veriﬁed behaviorally in human subjects.

# S

tudies of consciousness yield two types of data: subjective reports of perceived stimuli and objective measurements of

neural activity. In recent years, a diversity of putative objective correlates of consciousness have been described. Candidates include sustained activity in primary visual area V1 (1–3), amplification of perceptual processing (4, 5), correlation across distant regions (6, 7), joint parietal, frontal, and cingulate activation (4, 8, 9), cortico–cortical or thalamo–cortical -band oscillations (10, 11), and P300 waveform (12). Although these diverse measurements are often viewed as incompatible findings about the nature of conscious states, an increasingly attractive alternative is that they constitute different reflections of a single underlying phenomenon: the settling of brain activity into a temporary metastable state of global activity. This article introduces a simple neuronal model that illustrates how this view can account simultaneously for psychological and neurophysiological data on consciousness.

Our model focuses on the issue of conscious access: the fact that a piece of information, once conscious, becomes selectively available for multiple processes of attention, intention, memory, evaluation, and verbal report. In agreement with psychological models of a bottleneck stage in perception (13), we postulate that this availability results from the entry of sensory stimuli processed by the posterior visual areas into a global neuronal workspace (14–16), which mobilizes excitatory neurons with long-distance axons, capable of interconnecting sensory and high level areas into global brain-scale states of activity (Fig. 1A). The neurons that are temporarily mobilized inhibit other surrounding workspace neurons, which thus become unavailable for processing other stimuli. As a consequence of this selection process, when a piece of information such as the identity of a stimulus accesses a sufficient subset of workspace neurons, their activity becomes self-sustained and can be broadcasted via

long-distance connections to a vast set of defined areas, thus creating a global and exclusive availability for a given stimulus, which is then subjectively experienced as conscious.

In the present article, we use the model to simulate a classical perceptual phenomenon: the attentional blink (17). In a typical paradigm, participants are asked to process two successive targets, 1 (T1) and 2 (T2). When T2 is presented between 100 and 500 ms after T1, the ability to report it drops, as if the participants’ attention had ‘‘blinked.’’ Objective physiological data indicate that during this blink, T2 fails to evoke a P300 potential but still elicits event-related potentials associated with visual and semantic processing (P1, N1, and N400) (12). Our simulations aim at clarifying why some patterns of brain activity are selectively associated with subjective experience. In short, during the blink, bottom-up activity, presumably generating the P1, N1, and N400 waveforms, would propagate without necessarily creating a global reverberant state. However, a characteristic neural signature of long-lasting distributed activity and

-band emission, presumably generating the P300 waveform, would be associated with global access.

The elementary components of our simulation are singlecompartment spiking neurons that, when depolarized beyond a certain threshold by neuromodulatory inputs, exhibit spontaneous activity through intrinsic membrane oscillations in the range (18). They are organized in schematic cortical columns with distinct infragranular, granular, and supragranular layers, reciprocally connected to a thalamic network that receives external inputs (Fig. 1). In agreement with anatomical (19) and physiological (2) models of cortical organization, we distinguish a nearest-neighbor, bottom-up network that propagates sensory stimulation across the hierarchy of areas, and a long-distance, top-down network that sends amplification signals back to all levels below it. A possible implementation, amongst others (20), proposes that bottom-up propagation is supported by fast glumatergic -amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid (AMPA) receptors, whereas top-down amplification is supported by slower glutamatergic N-methyl-D-aspartate (NMDA) receptors (21, 22). This gives top-down projections a mainly modulatory role, because the efficacy of voltage-gated NMDA receptors is enhanced if there is a concomitant depolarization by sensory inputs. Thus, global activity is more likely to be achieved if there is ‘‘resonance’’ (10) between bottom-up sensory information and top-down signals.

It is currently out of reach to simulate the entire postulated architecture at the single-neuron level. We therefore present a minimal network, which models only the cell assemblies evoked by stimuli T1 and T2 through four hierarchical stages of processing (Fig. 1B). T1 and T2 are initially processed by separate

Abbreviations:T1,target1;T2,target2;V1,primaryvisualarea;SRA,spike-rateadaptation; GABA, -aminobutyric acid; AMPA, -amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid; NMDA, N-methyl-D-aspartate.

†To whom correspondence should be addressed. E-mail: dehaene@shfj.cea.fr.

8520–8525 PNAS July 8, 2003 vol. 100 no. 14 www.pnas.org cgi doi 10.1073 pnas.1332574100

[Figure 2]

[Figure 3]

- Fig. 1. Neuronal workspace model of conscious access. (A) Schematic architecture of brain areas (redrawn from ref. 14) comprising multiple specialized processors and a central network of high-level areas temporarily interconnecting them. During the attentional blink, T1 invades the workspace, where areas lock intoasingleassemblysupportingconsciousreportability.ThisinvasionbyT1blockstheprocessingofT2atasimilardepth.(B)Subsetofthalamo–corticalcolumns included in the present simulation. (C) Structure of a single simulated thalamo–cortical column, reproducing the laminar distribution of projections between excitatory neurons (triangles) and inhibitory neurons (stars; see Materials and Methods for details).

neural assemblies in two perceptual areas A and B (assemblies A1 and B1 for T1, and assemblies A2 and B2 for T2). Those assemblies do not inhibit each other because the attentional blink is known to occur between distinct visual stimuli, spatially separate visual streams, or even across the auditory and visual modalities (23). Further on, T1 and T2 reach higher association areas, also limited to two areas, C and D, where they compete for global access via reciprocal inhibitory interactions. In actual anatomy, areas A and B might correspond to a series of fast bottom-up cortical processors such as areas V1 or frontal eye field (2), whereas areas C and D would implement higher association areas of temporal, parietal, frontal, and cingulate cortex (14, 15).

### Materials and Methods

Model Neurons. Neurons are modeled as single-compartment integrate-and-fire units with membrane potential V. When V exceeds a threshold of 48 mV, a spike is recorded and transmitted to other neurons with an appropriate delay, and V is reset to 80 mV for a refractory period of 4 ms. The temporal evolution of V, expressed in millivolts, is given by

CdV/dt gLeak V Vrest INaP IKS IGABA IAMPA INMDA ISRA Iinput Ineuromodul, [1]

where C 1 F cm2 and currents are expressed in A cm2. The leak conductance is gleak 0.1 mS cm2, so that the membrane time constant C gleak is 10 ms.

INaP and IKS are persistent sodium and slowly inactivating potassium currents, the interplay of which can generate intrinsic

-band oscillations (18). Their simplified expression is

INaP gNaPmNaP V VNa , [2] where mNaP (1 e (V 51)/5) 1, and

IKS gKSmKS V VK , [3]

where KS dmKS dt (1 e (V 34)/6.5) 1 mKS, with KS 6 ms.

IGABA, IAMPA, and INMDA are the total synaptic currents respectively from fast gabaergic, AMPA, and NMDA glutamatergic synapses (21),

IGABA i t

gGABA i,jhGABA j t tdelay i,j Vi t VGABA

j 1. . .n

[4a] IAMPA i t

gAMPA i,jhAMPAj t tdelay i,j Vi t VAMPA

j 1. . .n

[4b] INMDA i t

gNMDA i,jmNMDA Vi t hNMDAj t tdelay i,j

j 1. . .n

Vi t VNMDA , [4c]

where the sum in each case is over all relevant neurons connected to postsynaptic neuron i (inhibitory interneurons for IGABA, bottom-up and intracolumn excitatory neurons for IAMPA, and top-down excitatory neurons for INMDA). The gi,j are the synaptic strengths and tdelay i,j the transmission delays in milliseconds from neuron j to neuron i. The functions hj(t) characterize the synaptic inputs from neuron j and are given by the convolution of the spike train sj(t) with the synaptic activation profile a(t),

hj t sj t a t , [5] where a(t) (e t/ 1 e t/ 2) (e tpeak/ 1 e tpeak/ 2), with tpeak

1 2 ( 1 2), where 1 and 2 are rise and decay constants characteristic of each channel (21). In the NMDA case only, the effective conductance is scaled by mNMDA(V), a factor that characterizes the voltage dependence of NMDA channels (24).

mNMDA V 1 0.280 e V/16.1 1. [6]

ISRA is an additional current used to model spike-rate adaptation (24).

ISRA gSRA V VSRA , [7] with SRA dgSRA dt gSRA.

Iinput is the current applied during stimulus presentation to thalamic neurons of the lowest hierarchical level to simulate a visual or auditory input.

Iinput t ginput V t VAMPA [8]

##### NEUROSCIENCE

[Figure 4]

Wakefulness and Spontaneous Activity. A final current, Ineuromodul, summarizes the known depolarizing effects of ascending activating systems such as those from cholinergic, noradrenergic, and serotoninergic nuclei in the brainstem, basal forebrain, and hypothalamus (25). This parameter is used to control the level of wakefulness. When Ineuromodul is low, membrane potentials converge to a stable asymptote in the absence of external stimulation. Beyond a threshold, individual neurons generate intrinsic -band membrane oscillations, first below the spiking threshold and then with an occasional occurrence of spikes (18). Because of those intrinsic properties, the network exhibits structured but semirandom patterns of spontaneous cortico– thalamic oscillatory activity, similar to empirical observations (10, 26), although our simulation, contrary to other similar work (21), is strictly deterministic. In the present work, we placed the network in a low spontaneous firing range (Ineuromodul 1

A cm2), presumably corresponding to wakefulness and attentive readiness. Work in preparation studies interactions between internal activity and stimulus processing at a higher spontaneous firing rate, which may provide a more realistic model for autonomous conscious states. We have observed that such states of elevated spontaneous activity can prevent the entry of external inputs into the workspace for a greater duration than during the blink. This effect may account for the empirical observation of long-lasting inattentional blindness in human subjects (27).

Parameter Values. The following parameter values were taken from references (18, 21, 24): VRest 67 mV, VNa 55 mV, VK 90 mV, VGABA VSRA 70 mV, VAMPA VNMDA

0 mV; GABA 0.175, AMPA 0.05, NMDA 0.0075; 1GABA 1 ms, 1AMPA 0.5 ms, 1NMDA 4 ms, 2GABA 7 ms,

2AMPA 2.4 ms, 2NMDA 40 ms, SRA 200 ms; ginput 0.06 mS cm2. The following parameters were generated randomly for each neuron, from a Gaussian distribution with a 5% SD and the following mean: gNaP 0.2 mS cm2, gKS 8 mS cm2; Ineuromodul 1 A cm2.

Columnar Organization and Connectivity. Each thalamo–cortical column comprised 80 excitatory and 40 inhibitory neurons organized in a three-layered structure, schematizing supragranular, infragranular, and layer IV cortical neurons, and a corresponding thalamic sector (see Fig. 1C). Within each layer, there were 20 excitatory and 10 inhibitory neurons.

Connections were established with a 60% probability. Connection parameters (synaptic strength , unit mS cm2, and transmission latency tdelay i,j, unit ms) were drawn from a Gaussian distribution with 10% SD around a fixed mean. All neurons connecting to given area randomly contacted excitatory and inhibitory neurons with the same probability and strength.

Inhibition. Inhibitory neurons sent only intralaminar horizontal connections both within a column ( GABA 0.12, delay 2) and toward other competing columns within the same area ( GABA 0.60, delay 2).

Intracolumnar Connectivity. Thalamic excitatory neurons projected to layer IV ( AMPA 0.20, delay 3) and, with lesser strength, to infragranular neurons ( AMPA 0.10, delay 3). Layer IV excitatory neurons projected to supragranular neurons ( AMPA 0.15, delay 2). Supragranular excitatory neurons projected to infragranular neurons ( AMPA 0.10, delay 2). Finally, infragranular excitatory neurons projected to layer 4 ( AMPA 0.05, delay 7), to supragranular neurons ( AMPA 0.05, delay 7), and to the thalamus ( AMPA 0.075, delay 8). Those principles and parameter values, inspired by ref. 21, capture the major properties of translaminar connections, although they do not attempt to capture the possible functional roles of the different layers (20). Latencies were adjusted to

take into account the coarseness of the present three-layer model and the fact that, in reality, some of these pathways are disynaptic (21).

Cortico–Cortical Projections. Supragranular excitatory neurons of each area projected to layer IV of the next area ( AMPA 0.05,

delay 3). In agreement with physiological observations (19, 22), top-down connections were slower, more numerous, and more diffuse. They connected the supra- and infra-granular excitatory neurons of a given column to the supra- and infragranular layers of all areas of a lower hierarchical level (Fig. 1B). Strong top-down connections linked columns coding for the same stimulus ( NMDA 0.05), whereas weaker top-down connections projected to all columns of a lower area ( NMDA 0.025). Transmission delays increased with cortical distance ( delay 5 3 , with 1 for consecutive areas, 2 for areas two levels apart in the hierarchy, etc.).

Attentional Blink Experiment. The goal of this experiment was to measure the subjective perception of targets presented during the attentional blink. Ten French students participated after giving informed consent. On each trial, participants saw a rapid serial visual presentation of distractors, amidst which two targets T1 and T2 could appear. They were asked to rate T2 visibility, then to report T1 identity. Each rapid serial visual presentation element was presented for 43 ms, followed by a 43-ms blank. Distractors were four-letter uppercase consonant strings (4° 1°). Except for critical items preceding and following T1 and T2, each distractor had a 20% chance of being replaced by a blank. T1, which appeared as the 7th or 10th element in the RVSP sequence, was the letter string XOOX or OXXO. T2, which could appear with a lag of 1, 2, 3, 4, 6, or 8 stimuli after T1, was a French uppercase number word (DEUX, CINQ, SEPT, or HUIT) on one-half of the trials, and a blank screen on the other one-half (384 trials total). After T2, two more distractor strings were presented, and then participants were immediately asked to rate their perception of T2 by placing a cursor on a continuous horizontal scale labeled with ‘‘not seen’’ at left and with ‘‘maximal visibility’’ at right. They then reported the identity of the middle letters of T1, by pressing a left-hand button for O and a right-hand button for X. This procedure minimized the latency between the visual presentation of T2 and the report of its subjective visibility (215 ms), thus reducing the possibility that participants forgot having seen T2.

### Results

We placed the network in a parameter regime in which it exhibited spontaneous thalamo–cortical oscillations, plausibly corresponding to a state of wakefulness (10). We then exposed it to the conditions of the attentional blink: a brief (40 ms) stimulation of thalamic neurons coding for T1, followed at a variable lag (0–400 ms) by a similar stimulation of T2 neurons (Fig. 2). Consider first the activation evoked by T1. A short burst of phasic stimulus activity was first propagated across the cortico–thalamic hierarchy. The highest cortical levels generated top-down amplification signals that, 80 ms later, caused sustained firing in T1 neurons, accompanied by hyperpolarization of T2 neurons in areas C and D. In a larger-scale simulation, this long-lasting dynamic state would permit the brain-scale propagation of stimulus information about T1. We hypothesize that this global broadcasting constitutes the physiological correlate of conscious reportability.

Compared to this dynamic state reliably evoked by T1 presentation, the activation evoked by T2 depended tightly on the timing of T2 presentation. T2 targets presented simultaneously with T1, or long after, elicited sustained firing supported by joint bottom-up activation and top-down amplification (Fig. 2 Left). However, T2 targets presented during T1-elicited global firing

[Figure 5]

[Figure 6]

- Fig. 2. Simulation of two trials of the attentional blink task. In each case, boxesshowthetemporalevolutionofﬁringrateinexcitatorycorticalneurons within each of the eight columns of Fig. 1B. (Upper) ‘‘Seen’’ trial with long

- T1–T2 lag (250 ms). T2 is presented at a time when the sustained activity evoked by T1 has decayed. T2 is therefore able to invade all cortical levels and elicits long-lasting activity comparable to T1. (Lower) ‘‘Blinked’’ trial with short T1–T2 lag (150 ms). When T2 is presented during T1-evoked activity, it fails to evoke neural activity beyond an initial bottom-up activation in areas A and B.

elicited only bottom-up activation in assemblies A2 and B2 (Fig. 2 Right). T1-elicited inhibition prevented T2 activation from propagating to higher cortical levels. As a result, the second phase of top-down amplification did not occur.

By using as an index of T2 reportability the firing rate of pyramidal cells coding for T2 in areas C or D, our simulation reproduced the temporary drop in performance typical of the attentional blink (Fig. 3A). It also showed a global drop of power emitted in the -band (Fig. 3C) and of crosscorrelations between distant T2-coding neurons (data not shown). Thus, several indexes of firing and synchrony all pointed to a drop in global activity during the blink, particularly evident in the higher areas C and D.

As a test for the requirement of long-distance top-down connections, we ran simulations at a critical T1–T2 lag of 100 ms for which the blink normally occurs, but with the top-down connections eliminated, weakened by 50%, or reduced to nearest-neighbors. In all cases, T2 activation extended to areas C and D, and thus the blink did not occur (data not shown). This indicates that a key feature of the workspace model, the contribution of long-distance axons, is critical to the blink phenomenon.

An original property of the model is the prediction of a dynamic all-or-none bifurcation in neural activity. Across sim-

[Figure 7]

Fig. 3. Comparison of network simulations (A, C, and E) with experimental subjective and objective data on T2 processing (B, D, and F). (A) In the simulation, the peak ﬁring rate of T2 neurons (shown in Hz) is unaffected by T1–T2 lag in low-level areas but shows a temporary drop at intermediate lags in higher areas C and D. (B) Likewise, experimentally recorded event-related potentials evoked by T2 (shown in V) exhibit a preservation of P1, N1, and N400 components but a drop of the P300 waveform during the attentional blink [redrawn from data by Vogel, et al. (12)]. (C) Mean power in the -band (20–100Hz)emittedbysimulatedpyramidalneuronsduringa200-mswindow after T2 presentation. (E) Distribution of ﬁring in area D. In the simulation, reverberant activation of workspace neurons is all-or-none such that parameters such as peak ﬁring rate and -band power are distributed bimodally. Such a bimodal distribution was observed in an experiment in which we collected subjective ratings of T2 perception from 0% (not seen) to 100% (maximal visibility) (D, mean rating; F, distribution of ratings).

ulated trials, depending on random fluctuations in spontaneous activity before stimulus arrival, ascending activity could be sufficient to trigger self-amplifying recurrent activity, or it remained below threshold and only transient bottom-up activity was seen. Thus, for a fixed T1–T2 lag, simulated firing rates in higher areas and other indices of global activity ( -band power and long-distance crosscorrelation) were found to be distributed bimodally across trials (Fig. 3E). The model therefore predicts that the apparent gradual drop in reportability observed during the attentional blink may be an artificial consequence of averaging across trials with full access awareness and others with no awareness.

To test this prediction experimentally, we used a modified attentional blink paradigm in which human subjects merely had to report to what extent they had seen a word (T2) within a rapid letter stream that contained another target letter string (T1). To obtain a continuous measure of subjective perception, we asked

##### NEUROSCIENCE

[Figure 8]

subjects to move a cursor on a continuous scale, from ‘‘not seen’’ on the left to ‘‘maximal visibility’’ on the right. The results indicated that subjective perception during the blink is indeed all-or-none (Fig. 3F). At the peak of the blink, which occurred

260 ms after T1, T2 was fully perceived in approximately one-half of the trials, as indicated by a cursor position identical to ‘‘seen’’ trials with a long T1–T2 lag or without attention on T1. In the other one-half, T2 was totally unseen, as indicated by a cursor position identical to T2-absent trials. Participants almost never used intermediate cursor positions.

The same participants also took another set of trials with identical stimuli but with the instruction to ignore T1. We verified that the blink was much reduced in this condition, with T2 perception ratings clustering at the higher end of the scale. Two control experiments were also run to verify that participants could use the continuous rating scale (C.S. and S.D., unpublished data). In one, on each trial we presented a single T2 target for a variable duration (14, 29, 43, 57, 71, or 86 ms), followed by a single mask. In this situation, subjective ratings of T2 perception showed a unimodal distribution, the peak location of which varied continuously with T2 duration. This result indicated that subjects could use the response scale in a graded manner as a reliable indicator of subtle perceptual changes. We then combined the blink and masking experiments by presenting variableduration T2 targets at lag 3 after T1 in the same sequence as above. The results showed a coexistence of two effects in the same trials: a continuous influence of T2 duration and an all-or-none effect of the blink. At each T2 duration, the response distribution was bimodal, with one peak at 0% visibility and the other peak at a location that increased progressively with T2 duration. Thus, even when participants show evidence of using the subjective rating scale as a graded measure of their perception, they still rate a significant fraction of blinked trials as totally unseen. These data suggest that the attentional blink in humans is associated with a stochastic all-or-none blocking of processing, which is accounted for in the model by an interaction between spontaneous activity and the nonlinear dynamics of bottom-up and top-down reverberation.

### Discussion

Our model is coherent with previous proposals of a role of top-down recurrent (2), reentrant (28, 29), or resonant (10, 20) connections in the integrative processes underlying conscious perception. Nevertheless, it goes beyond those proposals by presenting a detailed simulation of a cognitive task, which tentatively links subjective reports with objective physiological correlates of consciousness on the basis of a neurally plausible architecture.

Despite the relative simplicity of the postulated neuronal architecture, simulation of the model captures the main physiological observations on the attentional blink. In the simulation, blinked T2 targets evoke unchanged bottom-up activity in areas A and B, but a much reduced activity in high-level areas C and D. This matches the empirically observed preservation of the P1, N1, and N400 components, but the drastic drop of the P300 component of event-related potentials evoked by T2 during the attentional blink (12). We hypothesize that the former components reflect the bottom-up progression of activation in a nested hierarchy of perceptual and semantic processors, whereas P300 reflects the sudden and global activation of workspace neurons.

Because the blink is attributed to competition for workspace access, the proportion of T2 targets that are blinked, as a function of time, roughly traces the inverse shape of the neural activity evoked by T1 in higher-level areas C and D. In actual experiments, similarly, there is an inverse relation between the P300 waveform evoked by T1 and the size of the blink (30). Furthermore, the functional MRI activation elicited by T1 in parietal, frontal, and cingulate areas predicts the size of the blink

[Figure 9]

Fig.4. NeuralactivityevokedbyseenandunseenT2targetsinsimulation(A) and actual experimental recordings (B and C). For lags between 0 and 200 ms, simulated trials were sorted as a function of the amount of pyramidal neuron activity that reached area D in a 250-ms window after T2 presentation. (A) Averages of ﬁring rate as a function of time show that trials with area D activity are characterized by long-lasting ampliﬁcation in lower areas C, B2, and A2. (B) The curves from assembly B2, showing earlier ampliﬁcation and a small difference in the amplitude of the initial peak, are similar to activity evoked in monkey frontal eye ﬁeld area during a masking paradigm [redrawn fromdatabyThompsonandSchall(34)].(C)ThecurvesfromassemblyA2,with unchanged initial peak and small subsequent ampliﬁcation, are similar to actual electrophysiological recordings from monkey area V1 during attention and conscious perception paradigms [redrawn from data by Roelfsema et al. (39)].

(31). Both observations are compatible with our hypothesis that the global neuronal workspace, formed by neurons distributed in higher areas including prefrontal cortex, operates functionally as a processing bottleneck that cannot simultaneously process two targets (13).

Although there have been no single-neuron recordings during the attentional blink, the simulated profiles of single-neuron activity to seen and blinked T2 targets can be compared to electrophysiological recordings obtained in other paradigms of conscious and unconscious processing. In perceptual areas A and B of the model, neurons fire phasically in tight synchrony with the stimulus, then show a broader period of late amplification only in seen trials, not in blinked trials. This parallels experimental recordings in areas V1 and IT under conditions of inattention, reduced contrast, masking, or anesthesia, where late amplification occurs only for reportable stimuli (1–3, 32) (Fig. 4C).

In the model, fluctuations in the state of the network before the stimulus, particularly in the spontaneous oscillations of membrane potential, create variability in the activity evoked by identical stimuli. When intrinsic fluctuations are in phase with stimulus presentation, bottom-up activation is enhanced. This coincidence has a cascading effect on subsequent areas and eventually affects the probability of the entire network falling into a global active state. Similarly, experimental recordings in V1 during the perception of ambiguous stimuli have shown that both late amplification and visibility vary in an all-or-none

[Figure 10]

manner (1) and can be partially predicted by the state of activity of V1 before stimulus arrival (33). This suggests that, as in our model, the resonance of incoming stimuli with spontaneous brain activity is essential for perception.

In our simulation, comparing seen and unseen trials also revealed a small difference in the amplitude of the first phasic peak in assembly B2 (Fig. 4). Likewise, experiments that sort trials based on the presence or absence of a subsequent conscious report occasionally show early differences in neural activity in V1 or frontal eye field (34, 35). In our interpretation, however, such early effects are only secondary correlates of consciousness because they are merely an indirect consequence of selective averaging over a fluctuating baseline. That those early differences are not associated with a conscious content is seen most clearly when they are found even before the stimulus is presented (33).

Obviously, our simulation is still simplified in many ways. First, in actual attentional blink experiments, backward masking of T2 is essential (36, 37). We suggest that masking is necessary for the blink to occur because it reduces T2-induced activation to a brief pulse (3, 32), which then acts as a ‘‘tracer’’ of the occupancy of the conscious workspace at a given moment. In our simulation, this could be achieved by directly stimulating T2-coding thalamic neurons with a temporally delimited pulse and thus no masking was necessary. Another difference is that, in actual experiments, the presence of the attentional blink depends on the T1 task, and disappears when subjects are instructed to ignore T1. For simplicity, our network had a fixed connectivity set to process both T1 and T2. Neural mechanisms of task switching have been proposed, however, and could be combined with the present work (14). Finally, although the present model reproduces the qualitative features of the attentional blink, there are quantitative difference in timing, particularly in the onset and duration of the blink (Fig. 2). This is due in part to the value of the propagation delays, which were extrapolated from monkey visual areas and should be slower for the more distant areas of the human brain. Blink duration, which corresponds to the duration of T1-induced activity, is jointly determined in our simulation by the strength of excitatory connections and by the amount of spike-rate adaptation. In a more realistic model, it should also

vary with the task, with additional circuits providing taskdependent reverberation, possibly associated with a subjective feeling of conscious effort (14).

According to the present model, the primary correlate of conscious access is a sudden self-amplifying bifurcation leading to a global brain-scale pattern of activity. This leads to several critical predictions for neuroimaging and pharmacological experiments. First, in experiments with a continuously varying and increasingly visible stimulus, we predict a sudden nonlinear transition toward a state of globally increased brain activity (‘‘ignition’’), particularly evident in prefrontal, cingulate, and parietal cortices, accompanied by a synchronous amplification of posterior perceptual activation and by thalamo–cortical brain-scale synchrony in the range (20–100 Hz). Finer scale electrophysiological or optical recordings should demonstrate that this state is selective to a subset of neurons codingforthestimulusandisaccompaniedinhigherareasbybroad inhibition of neurons cording for other stimuli. Even higherresolution experiments should reveal a layer-specific distribution of active workspace neurons, with intense top-down activity originating from a subpopulation of cells with long axons in supra- and infra-granular layers of prefrontal, cingulate and parietal cortices. Second, we predict a bimodal distribution of activation during individual attentional blink trials, which could be demonstrated by single-event functional MRI or by distributional analysis of intracranial or even scalp measurements of the P300. Third, experimental interventions that affect top-down connections or inhibitory interactions in higher cortical areas should alter this dynamic transition, and therefore subjective perception, without necessarily affecting subliminal bottom-up processing. This prediction could be tested by using pharmalogical agents such as for instance general anesthetics known to affect NMDA or GABA receptors, or effectors of cholinergic receptors that may globally gate the access to the global workspace (38).

We thank V. Lamme and Y. Rossetti for helpful comments. This work was supported by Institut National de la Sante´ et de la Recherche Me´dicale, Commissariat `a l’Energie Atomique, the McDonnell Foundation, Centre National de la Recherche Scientifique, Colle`ge de France, the French Ministry of Research, the Association pour la Recherche sur le Cancer, the Association Franc¸aise contre les Myopathies, and the Commission of the European Communities.

- 1. Super, H., Spekreijse, H. & Lamme, V. A. (2001) Nat. Neurosci. 4, 304–310.
- 2. Lamme, V. A. & Roelfsema, P. R. (2000) Trends Neurosci. 23, 571–579.
- 3. Lamme, V. A., Zipser, K. & Spekreijse, H. (2002) J. Cognit. Neurosci. 14, 1044–1053.
- 4. Dehaene, S., Naccache, L., Cohen, L., Le Bihan, D., Mangin, J. F., Poline, J. B. & Rivie`re, D. (2001) Nat. Neurosci. 4, 752–758.
- 5. Moutoussis, K. & Zeki, S. (2002) Proc. Natl. Acad. Sci. USA 99, 9527–9532.
- 6. Engel, A. K. & Singer, W. (2001) Trends Cognit. Sci. 5, 16–25.
- 7. Rodriguez, E., George, N., Lachaux, J. P., Martinerie, J., Renault, B. & Varela, F. J. (1999) Nature 397, 430–433.
- 8. Lumer, E. D. & Rees, G. (1999) Proc. Natl. Acad. Sci. USA 96, 1669–1673.
- 9. Kleinschmidt, A., Buchel, C., Hutton, C., Friston, K. J. & Frackowiak, R. S.

(2002) Neuron 34, 659–666.

- 10. Llinas, R., Ribary, U., Contreras, D. & Pedroarena, C. (1998) Philos. Trans. R. Soc. London B 353, 1841–1849.
- 11. Tallon-Baudry, C. & Bertrand, O. (1999) Trends Cognit. Sci. 3, 151–162.
- 12. Vogel, E. K., Luck, S. J. & Shapiro, K. L. J. (1998) J. Exp. Psychol. Hum. Percept. Perform. 24, 1656–1674.
- 13. Chun, M. M. & Potter, M. C. (1995) J. Exp. Psychol. Hum. Percept. Perform. 21, 109–127.
- 14. Dehaene, S., Kerszberg, M. & Changeux, J. P. (1998) Proc. Natl. Acad. Sci. USA 95, 14529–14534.
- 15. Dehaene, S. & Naccache, L. (2001) Cognition 79, 1–37.
- 16. Baars, B. J. (1989) A Cognitive Theory of Consciousness (Cambridge Univ. Press, Cambridge, U.K.).
- 17. Raymond, J. E., Shapiro, K. L. & Arnell, K. M. (1992) J. Exp. Psychol. Hum. Percept. Perform. 18, 849–860.
- 18. Wang, X.-J. (1993) NeuroReport 5, 221–224.
- 19. Felleman, D. J. & Van Essen, D. C. (1991) Cereb. Cortex 1, 1–47.
- 20. Raizada, R. D. & Grossberg, S. (2003) Cereb. Cortex 13, 100–113.

- 21. Lumer, E. D., Edelman, G. M. & Tononi, G. (1997) Cereb. Cortex 7, 207–227.
- 22. Salin, P. A. & Bullier, J. (1995) Physiol. Rev. 75, 107–154.
- 23. Arnell, K. M. & Jolicoeur, P. (1999) J. Exp. Psychol. Hum. Percept. Perform. 25, 630–648.
- 24. Dayan, P. & Abbott, L. F. (2001) Theoretical Neuroscience: Computational and Mathematical Modeling of Neural Systems (MIT Press, Cambridge, MA).
- 25. Steriade, M., McCormick, D. A. & Sejnowski, T. J. (1993) Science 262, 679–685.
- 26. Llinas, R. R. & Pare´, D. (1991) Neuroscience 44, 521–535.
- 27. Mack, A. & Rock, I. (1998) Inattentional Blindness (MIT Press, Cambridge, MA).
- 28. Di Lollo, V., Enns, J. T. & Rensink, R. A. (2000) J. Exp. Psychol. Gen. 129, 481–507.
- 29. Edelman, G. M. (1993) Neuron 10, 115–125.
- 30. McArthur, G., Budd, T. & Michie, P. (1999) NeuroReport 10, 3691–3695.
- 31. Marois, R., Chun, M. M. & Gore, J. C. (2000) Neuron 28, 299–308.
- 32. Kovacs, G., Vogels, R. & Orban, G. A. (1995) Proc. Natl. Acad. Sci. USA 92, 5587–5591.
- 33. Super, H., van der Togt, C., Spekreijse, H. & Lamme, V. A. (2003) J. Neurosci. 23, 3407–3414.
- 34. Thompson, K. G. & Schall, J. D. (1999) Nat. Neurosci. 2, 283–288.
- 35. Pins, D. & Ffytche, D. (2003) Cereb. Cortex 13, 461–474.
- 36. Brehaut, J. C., Enns, J. T. & Di Lollo, V. (1999) Percept. Psychophys. 61, 1436–1448.
- 37. McLaughlin, E. N., Shore, D. I. & Klein, R. M. (2001) Q. J. Exp. Psychol. A 54, 169–196.
- 38. Granon, S., Faure, P. & Changeux, J. P. (2003) Proc. Natl. Acad. Sci. USA 100, in press.
- 39. Roelfsema, P. R., Lamme, V. A. & Spekreijse, H. (1998) Nature 395, 376–381.

##### NEUROSCIENCE

