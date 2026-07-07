See	discussions,	stats,	and	author	profiles	for	this	publication	at: https://www.researchgate.net/publication/306337420

## Brain–computer interfaces for communication and rehabilitation

Article in Nature	Reviews	Neurology	·	August	2016

DOI:	10.1038/nrneurol.2016.113

CITATIONS

4

READS

605

3	authors,	including:

[Figure 1]

Ujwal	Chaudhary University	of	Tuebingen

49 PUBLICATIONS 71 CITATIONS

[Figure 2]

SEE	PROFILE

Ander	Ramos-Murguialday University	of	Tuebingen

76 PUBLICATIONS 1,550 CITATIONS

SEE	PROFILE

#### Some	of	the	authors	of	this	publication	are	also	working	on	these	related	projects:

[Figure 3]

Brain	Computer	interface	for	communication	in	complete	locked-in	state View	project

All	content	following	this	page	was	uploaded	by Ujwal	Chaudhary on	24	August	2016.

The	user	has	requested	enhancement	of	the	downloaded	file.	All	in-text	references underlined	in	blue are	added	to	the	original	document and	are	linked	to	publications	on	ResearchGate,	letting	you	access	and	read	them	immediately.

REVIEWS

# Brain–computer interfaces for communication and rehabilitation

Ujwal Chaudhary1, Niels Birbaumer1,2 and Ander Ramos-Murguialday1,3

Abstract | Brain–computer interfaces (BCIs) use brain activity to control external devices, thereby enabling severely disabled patients to interact with the environment. A variety of invasive and noninvasive techniques for controlling BCIs have been explored, most notably EEG, and more recently, near-infrared spectroscopy. Assistive BCIs are designed to enable paralyzed patients to communicate or control external robotic devices, such as prosthetics; rehabilitative BCIs are designed to facilitate recovery of neural function. In this Review, we provide an overview of the development of BCIs and the current technology available before discussing experimental and clinical studies of BCIs. We first consider the use of BCIs for communication in patients who are paralyzed, particularly those with locked-in syndrome or complete locked-in syndrome as a result of amyotrophic lateral sclerosis. We then discuss the use of BCIs for motor rehabilitation after severe stroke and spinal cord injury. We also describe the possible neurophysiological and learning mechanisms that underlie the clinical efficacy of BCIs.

###### Alpha waves

Neural oscillations in the frequency range of 8–13Hz, indicating widespread inhibitory activity in neuronal tissue.

1Institute of Medical Psychology and Behavioural Neurobiology, University of Tübingen, Silcherstrasse 5, 72076 Tübingen, Germany. 2Wyss-Center for Bio- and Neuro-Engineering, Chenin de Mines 9, Ch 1202, Geneva, Switzerland. 3TECNALIA, Health Department, Neural Engineering Laboratory, San Sebastian, Paseo Mikeletegi 1, 20009 San Sebastian, Spain.

Correspondence to U.C. and A.R.M. chaudharyujwal@gmail.com; ander.ramos@gmail.com

doi:10.1038/nrneurol.2016.113 Published online 19 Aug 2016

Philosophers throughout history have contemplated whether the brain can be used to interact directly with the external world without the mediation of the peripheral somatomotor nervous system. Such control of external devices could not be considered without the technology to acquire brain signals and translate them into commands. In 1929, however, Hans Berger made a decisive breakthrough with the development of EEG to enable the noninvasive recording of neuroelectrical signals from the human brain. The subsequent advent of fast computing, real-time analysis systems and expanding knowledge of brain function have laid the foundation for realizing the dream of controlling external devices directly with brain signals. During the past two decades, experimental research into such brain–computer-interfaces (BCIs) has expanded rapidly, with promising results in healthy people but few controlled clinical outcome studies.

In this Review, we discuss the different kinds of BCIs that have been developed and tested to date in patients with severe paralysis. In particular, we will discuss assistive BCIs for communication in paralysis, with a focus on patients who are disabled as a result of amyotrophic lateral sclerosis (ALS), and rehabilitative BCIs for the restoration of movement, particularly in patients with chronic stroke.

##### History of BCIs

The first attempt to control brain signals on a neurophysiological basis was reported in 1968. Wyrwicka and Sterman recorded sensorimotor rhythms (also known

as rolandic α rhythms or μ rhythms) in cats1 and translated these sensorimotor rhythms into sensory feedback that was used to reward the animals and increase their generation of sensorimotor rhythms. At approximately the same time, research was being conducted into a technique for regulation of brain activity in humans, which came to be known as neurofeedback; the first scientific report of volitional control of human brain oscillation was published by Kamiya in 1969 (REF. 2). Kamiya and colleagues showed that healthy individuals could quickly learn to change the alpha waves in their brain (recorded with EEG) if they were given continuous sensory feedback, such as a rising and falling tone, that was derived from their brain activity. Also in 1969, Fetz demonstrated that operant conditioning could be used to control the firing of single cortical neurons in monkeys3. These findings triggered extensive research into the link between brain physiology and behaviour with instrumental learning, and laid the foundations for the development of most current BCIs. The term ‘brain– computer interface’ was first proposed by Jacques Vidal in 1973, when he presented a system that could translate EEG signals into computer control signals4.

Interest in the field of BCIs was sparked by further experiments by Sterman and colleagues. They serendipitously found that instrumental training of sensorimotor rhythms in cats increased seizure thresholds5; subsequent controlled, single-case studies showed that similar techniques in humans with epilepsy led to a

NATURE REVIEWS | NEUROLOGY ADVANCE ONLINE PUBLICATION | 1

© 2016 Mac millan Publishers Li mited, part of Springer Nature. All rights reserved.

Key points

- • Brain–computer interfaces (BCIs) are starting to prove their efficacy as assistive and rehabilitative technologies in patients with severe motor impairments
- • BCIs can be invasive or noninvasive, and designed to detect and decode a variety of brain signals
- • Assistive BCIs are intended to enable paralyzed patients to communicate or control external robotic devices; rehabilitative BCIs are intended to facilitate neural recovery
- • EEG-based BCIs have enabled some paralyzed patients to communicate, but near-infrared spectroscopy combined with a classical conditioning paradigm is the only successful approach for complete locked-in syndrome
- • The combination of EEG-based BCIs with behavioural physiotherapy is a feasible option for rehabilitation in stroke; the approach is to induce neuroplasticity and restore lost function after stroke
- • There is an urgent need for more large randomized controlled clinical trials using invasive and noninvasive BCIs with long-term follow-ups in patients rather than healthy populations

###### Instrumental learning

A type of learning in which the strength of a behaviour or a physiological response is modified by its consequences (reward or punishment).

###### Local field potentials

Graded neuroelectrical changes in voltage, generated by the summed synaptic currents flowing from multiple nearby neurons within a small volume of nervous tissue, recorded from inserted microelectrodes.

###### Single-unit acitivity

Action potentials of single neurons, recorded using inserted microelectrodes

###### Multi-unit activity

Action potentials of multiple neurons,recorded using an array of multiple microelectrodes.

###### Cortical preparation

Cortical preparation occurs before a cognitive, motor or emotional response, and is detectable with EEG as a negatively polarized voltage shift.

significant reduction in grand-mal seizures6. These findings formed the basis of clinical trials to evaluate the potential of neurofeedback training in the treatment of various disorders. The most promising were treatment studies of children with attention deficit– hyperactivity disorder7 and intractable seizures8. Just a few years after Sterman’s studies, however, the entire field of neurofeedback-related behavioural effects fell into disrepute, as many premature claims made on the basis of successes in single patients could not be validated in larger, controlled trials.

During the past 20 years, research into BCIs has been rekindled and fuelled by microelectrode, single-neuron recordings in rodents9 and nonhuman primates10–15. In these experiments, animals learned to use their own brain activity to control movement of computer cursors13,16 or robotic arms9,15,17. Similar single-neuron recording approaches were later tested in humans with tetraplegia18,19. Despite the earlier setbacks with neurofeedback experiments, several studies provided evidence for instrumental conditioning of brain activity with effects on neuronal functions and some brain pathologies20–23, and formed the basis for current work in the field of BCIs.

##### Types of BCI

At the beginning of 21st century, progress in BCI research was rapid. This progress has been driven by an increase in the number of available techniques to record different brain signals. BCIs can be classified as invasive or noninvasive (FIG. 1), and these two general types enable detection of different types of brain signal.

The general principles of all BCIs are similar. The brain signals that are detected are amplified, filtered and decoded using online classification algorithms. The brain signals are classified according to relevant characteristics (for example, sensorimotor rhythms over the motor cortex), filtered and smoothed before being fed back to users as a reward, thereby increasing the probability that they will reproduce the rewarded brain response. After processing and decoding of the

brain signals, the output of the BCI can be used to control movement of a prosthesis, orthosis, wheelchair, robot or cursor24–26, or to direct electrical stimulation of muscles or the brain27. The brain response can also be fed back as visual18,28, auditory29,30 or haptic stimuli that vary in relation to the measured brain activity31,32.

##### Invasive BCIs

Use of invasive BCIs involves surgical implantation of electrodes or multi-electrode grids10,18,19. Invasive BCIs measure activity patterns of neurons, which encode behaviourally relevant information. Five main types of brain activity are measured with invasive BCIs: local field potentials (LFPs)33–35, single-unit activity (SUA)9,13,17,36–39, multi-unit activity (MUA)33, electrocorticographic oscillations recorded from electrodes on the cortical surface (electrocorticography, ECoG)40,41, and calcium channel permeability42.

##### Noninvasive BCIs

Noninvasive BCIs require no surgical implantation, and enable recording of brain signals from the external surface of the scalp. These interfaces can detect seven types of brain signal, described below.

Slow cortical potentials. Slow cortical potentials are measures of cortical polarization recorded with direct current amplifiers from any location on the scalp preferably a frontocentral region — over 0.5–10.0 s. Voltage changes can be positive or negative; negative shifts indicate cortical preparation (an increase in excitation of underlying neuronal tissue) and positive shifts indicate decreased preparation and decreased activation43,44. Users of BCIs that measure slow cortical potentials learn to select on-screen options by controlling slow cortical potential amplitudes to move a cursor and select letters45.

Sensorimotor rhythms. Sensorimotor rhythms are sinusoidal frequencies in the alpha range (8–13 Hz) that can be detected at the somatosensory and motor cortical regions. Sensorimotor rhythms decrease in amplitude with movement, preparation for movement or motor imagery46. Users of BCIs that measure sensorimotor rhythms learn to select on-screen options by controlling sensorimotor rhythms to move a cursor and select letters47,48.

P300 event-related potential. The P300 evoked brain potential occurs ~300 ms after a new, surprising stimulus and can be recorded with EEG. The signal has a positive electrical polarity, and increases in amplitude when greater attention is given to the particular stimulus. Experiments in which the P300 event-related potential (ERP) is monitored are based on a paradigm introduced in 1988 (REF. 49) that is the most commonly used BCI spelling application50–54. Patients select a letter from a matrix in which each letter is transiently illuminated at random. The user concentrates on their desired letter, and when it becomes illuminated, a P300 ERP is elicited that triggers selection of the letter53.

Invasive Non-invasive

NIRS source NIRS detector

NIRS

SUA

LFP < 500 Hz

BOLD signal

MUA > 1000 Hz ECoG

fMRI

+ –

EEG

Signal acquisition and processing

Signal acquisition and processing

Decoding algorithm

Feature extraction

Control signal

Machine learning and pattern classiﬁcation

Robot or cursor control

Assistive BCI Control signal Rehabilitative BCI

Figure 1 | General framework of brain–computer interface (BCI) systems. Invasive BCI approaches (left) include the measurement of local field potentials (LFPs), single-unit activity (SUA), multi-unit activity (MUA), and electrocorticography (ECoG). Noninvasive BCI approaches (right) include EEG, blood oxygenation level-dependent (BOLD) functional MRI, and near-infrared spectroscopy (NIRS). Brain signals are processed to extract features relevant to the aim of the BCI (for example, communication) and then classified using a translational algorithm to construct a control signal that drives the BCI. BCIs can be classified as assistive to help patients with communication or movement, or as rehabilitative to help recover neural function.

Nature Reviews | Neurology

Steady-state visual evoked potentials. BCIs that detect steady-state visual evoked potentials (SSVEPs) record the EEG signal from the occipital cortex during high-frequency (>6 Hz) periodic presentation of visual stimuli. Patients select on-screen options by focusing on their target stimulus55,56. This type of BCI depends on attentional capacity and vision to be intact, and both are often compromised in patients with advanced and severe neurological disease.

Error-related negative evoked potentials. An errorrelated negative evoked brain potential (ERNP) occurs 200–250 ms after the detection of an erroneous response in a continuous stimulus–response sequence. BCIs that detect ERNPs enable users to identify cursor movements outside a defined visual field or to detect an error in a sequence of target stimuli57. Usually, the observer listens to a sequence of letters, and a P300 event-related potential is evoked if the intended target letter appears; if a letter other than the target letter is

presented, an ERNP occurs and the BCI suppresses the reward stimulus that would usually follow detection of the target letter.

Blood oxygenation level. Blood oxygen level-dependent (BOLD) functional MRI can be used to detect changes in metabolic activity within the brain, which are thought to reflect changes in neural activity58. fMRI has also been explored for the development of BCIs59–63. In some studies, patients with neuropsychiatric disorders64–66 have been successfully trained in an instrumental learning task that enables control of the BOLD signal. In one study, neurofeedback training to increase the BOLD response of the anterior insula (which responds to peripheral signals of aversive emotions such as fear) led people to subsequently rate negative emotional slides as more negative than before training65. Detection of BOLD signals that result from specific mental imagery has also been used in healthy participants to enable selection of all letters of the alphabet62.

Cerebral oxygenation changes. Changes in cerebral oxygenation can be detected in healthy and neurologically impaired adults and children by using noninvasive or invasive near-infrared spectroscopy (NIRS)67–69. An NIRS-based BCI, unlike one based on fMRI, can be easily applied at the bedside of patients who have severe impairments and who are difficult to move, but are in serious need of a communication route70,71.

##### Clinical classification of BCIs

BCIs can be classified as assistive or rehabilitative according to their clinical application (FIG. 1). Assistive BCI systems aim to substitute lost functions, such as communication or motor function24–26,72,73, enable control of robotic devices, or provide functional electrical stimulation27 to assist with daily life. By contrast, rehabilitative BCI systems (also known as restorative or neurofeedback-based BCI systems), aim to facilitate the restoration of brain function and/or behaviour by manipulation or self-regulation of neurophysiological activity73,74. In the remainder of the Review, we first consider the use of assistive BCIs for communication in patients who are paralyzed, with a focus on those who have locked-in syndrome or complete locked-in syndrome (CLIS) as a result of ALS. We then discuss the application of rehabilitative BCIs for functional recovery in patients with stroke, before reviewing the uses of BCIs for assistance with movement.

##### BCIs for communication

The primary clinical populations of the BCIs described below are patients with extensive impairments in communication and motor function as a result of amyotrophic lateral sclerosis (ALS) or severe CNS damage, such as stroke or spinal cord injury. To date, the application of BCIs for communication in paralysis has largely focused on patients with ALS. ALS is a progressive motor neuron disease that leads to complete destruction of the peripheral and central motor system but affects sensory and cognitive functions to a relatively minor degree75. No treatment is available, and patients who do not accept permanent ventilation die from respiratory or respiratory-related complications. With ventilation, disease progression leads to complete loss of muscular responses; the last remaining muscular control is usually that of the eye muscle. Patients with complete paralysis except for vertical eye movement and blinking but preserved consciousness are classified as having locked-in syndrome76. Total immobility and loss of eye movements with preserved awareness and cognition means a patient has CLIS76.

People with ALS eventually become unable to speak at all77 and consequently benefit from systems that enable them to communicate. Patients with several remaining functional motor channels can benefit from assistive communication that uses a range of augmentative and alternative communication (AAC) strategies, such as eye trackers with speech-generating devices78. However, AAC strategies do not work for patients with locked-in syndrome or CLIS owing to the loss of all motor channels, so the patients are unable to communicate. Invasive and

noninvasive BCIs have been used in attempts to address communication in locked-in syndrome and CLIS74,79. In general, BCI-based communication involves generation of brain signals by the patient to control alphanumeric grids, cursors, and/or web browsing tools to formulate sentences and express feelings, thoughts and desires.

##### Invasive BCIs for communication

Invasive BCIs were first implanted into the brains of patients with ALS in 1989 (REF. 80); the patients were at different stages of disease, but none had locked-in syndrome or CLIS81,82. In these experiments, electrodes filled with a neurotrophic factor were implanted into the brains of patients, who subsequently learned to control an on-screen cursor by modulating the firing patterns of axons that had grown into the electrode.

More recent studies have demonstrated improvements in invasive approaches. In 2006, implantation of 100 microelectrodes in the motor cortex of two patients with tetraplegia markedly improved BCI performance, and the patients learned to use the neural interface system to move a computer cursor18 or a hand robot in all desired directions, a task that is difficult or impossible with a noninvasive EEG BCI or functional near infrared spectroscopy BCI. A study published in 2015 (REF. 24) demonstrated that an invasive neural prosthesis enabled two patients with ALS to control a cursor to type words freely at a speed of up to 115 words in <19 min. Neither patient, however, had locked-in syndrome or CLIS.

Attempts at using invasive BCIs for communication in patients with CLIS have not been successful. For example, implantation of electrocorticography electrodes at the cortical surface of two patients with CLIS as a result of ALS has not produced positive outcomes83,84. Patients were trained to select letters or yes–no responses by using cortical oscillations and ERPs, but this system did not enable meaningful communication74,84,85. Some possible reasons for the failure have been proposed (see Shortfalls in CLIS, below), but the explanation remains unclear. Regardless, a few case reports of invasive BCIs in patients with ALS are insufficient to support any solid conclusions about the efficacy of the invasive approach in CLIS. In order to determine the most effective type of BCI in this context, more patients with CLIS need to be trained to use the systems that have been developed, and invasive and noninvasive BCIs need to be compared.

##### Noninvasive BCIs for communication

The first clinically relevant application of a noninvasive BCI for communication in patients with locked-in syndrome as a result of ALS was reported in 1999 (REF. 72). Since then, several kinds of EEG-based BCIs for communication in patients with locked-in syndrome have been developed and tested.

Slow cortical potential BCIs. In the first successful use of noninvasive BCIs for communication in locked-in syndrome72, patients were able to communicate by controlling slow cortical potentials to select letters on a computer screen. Subsequent studies have shown that

###### Contingency

Contingency is an associative connection between stimuli or responses that are usually paired within a short time period of milliseconds to seconds.

###### Classical conditioning

Classical conditioning, also called Pavlovian conditioning, is a learning process in which two stimuli are repeatedly paired until one elicits a reflexive behavioural or physiological response that relates to the other.

slow cortical potentials can be used to control external devices46,45,72,86, leading to the conclusion that slow cortical potential-based BCIs can provide basic communication capabilities in locked-in syndrome. However, attempts to use this approach for some patients with CLIS have not successfully established communication.

Sensorimotor rhythm BCIs. BCIs that make use of sensorimotor rhythms have been developed48, and used with some success. For example, in a study published in 2004 (REF. 87), patients with locked-in syndrome or high spinal cord lesions were able to use sensorimotor rhythms to control cursor movements or select letters or words from a computer menu47,88.

P300 BCIs. The majority of patients with locked-in syndrome as a result of ALS who have functioning vision and eye control are able to learn brain self-regulation, or to ‘create’ a P300 ERP, with the potential to control a BCI. One case study has shown that spelling is possible for patients with advanced ALS when they use a BCI controlled by P300 ERPs over >2.5 years54. The patient had locked-in syndrome, but retained some muscular responses (eye movements), and the approach has not been tested in patients with CLIS.

##### Shortfalls in CLIS

The patients with locked-in syndrome who participated in the above studies of noninvasive EEG-based BCIs never transitioned to CLIS. Use of the same BCIs in patients with CLIS has been completely unsuccessful89. One study published in 2008 (REF. 86) showed that patients with CLIS do not achieve sufficient control of their brain signals to enable communication with the use of EEG signals. Specific cognitive problems and abnormal neurophysiological signatures of particular neuroelectrical processes might be, at least in part, responsible for the failure in CLIS. Kübler and Birbaumer86 speculated that extinction of goal-directed thinking that occurs in CLIS might prohibit instrumental learning that is required for communication via BCIs. Whether or not communication via BCIs is even possible for patients with CLIS, therefore, remained unclear until recently. One study has shown that ERPs in response to auditory and proprioceptive stimuli are intact in patients with CLIS84, indicating that communication via BCIs should be possible by harnessing these EEG signatures, although these findings were case reports and might not be applicable to all patients with CLIS. The predominantly negative results to date, however, show that we need a better understanding of the underlying neurophysiological mechanisms of BCI learning, particularly in paralyzed patients, and raise the possibility that an alternative learning paradigm or use of other neuroimaging techniques might be necessary for patients with CLIS.

##### Towards BCIs for complete locked‑in syndrome

Birbaumeret al.90 speculated that “loss of thecontingency” between a voluntary response and/or intention and its feedback owing to a lack of immediate reinforcement

would prevent instrumental learning in any context, even if auditory afferent input and cognitive processing is preserved. In CLIS, the complete social isolation means that any intended response or desire has no contingent consequence, so intentions are likely to extinguish at the cognitive and physiological level. Similarly, a lack of contingencies in instrumental learning is likely to lead to the extinction of goal-directed thinking and imagery.

This proposed explanation for the failure of instrumental learning in patients with CLIS is supported by animal model investigations that showed the anterior striatum region of the basal ganglia to be activated during instrumental brain control and BCI training, confirming that these regions have a critical role in reinforcement learning91,92,93. In one of these studies, rats were rewarded for simultaneous increases in the firing rate of particular cells in the motor cortex and decreases in the firing rate of adjacent neurons. The animals learnt to use neurofeedback to control the changes in firing rates, but blockade of the cortex–thalamus–striatum loop with NMDA receptor antagonists eliminated the learning and execution of the self-regulation94. The loss of instrumental contingencies in patients with CLIS could lead to a similar loss of cortex–thalamus–striatum loop activation that extinguishes goal-directed intentions that drive communication in a similar way. If this is the case, all training procedures based on instrumental learning and volitional attention, including the control of BCIs, would be ineffective owing to extinction and consequent loss of control95,96.

The only learning strategy that circumvents a lack of goal-directed thinking and movement is classical conditioning, which requires no volition or cognitive effort. The preservation of classical conditioning when instrumental learning is lost is demonstrated by experiments in rats treated with curare, which leaves them completely paralyzed and requiring artificial respiration, similar to patients with CLIS. These rats exhibited excellent classical learning of autonomic functions, but failed to learn instrumental control of physiological responses94. We argue that a classical conditioning paradigm could, therefore, provide a suitable learning paradigm to enable patients with CLIS to communicate. Indeed, such paradigms have been successful in several studies of patients with CLIS as a result of ALS97–99. These experiments showed that, although classical conditioning paradigms seem to work, the EEG alone as the critical BCI signal could not be used reliably for successful communication.

The first case report of successful communication from a patient with CLIS as a result of ALS came from an experiment in which a BCI-based fNIRS was used with a classical conditioning paradigm70. The BCI was based on fNIRS, and enabled the patient to communicate yes and no responses to simple questions (that either had known answers or were open) over a period of >1 year70. In this approach, fNIRS was used to measure and classify cortical oxygenation and deoxygenation after presentation of each question. The classical conditioning paradigm meant that responses to questions were reflexive, making it easier to distinguish between yes and no responses that the patient was thinking.

The fNIRS-based BCI enabled the patient to communicate 72–100% correct answers over more than 14 consecutive sessions.

To validate the preliminary findings with the fNIRS BCI and refine the technology, extensive studies have been performed with four patients with CLIS as a result of ALS, using a BCI that uses a combination of NIRS and EEG. The NIRS–EEG BCI has enabled the four patients to respond to spoken questions via control of fronto-central brain oxygenation. (Chaudhary et al., unpublished work). The patients learned to answer personal questions with known answers and open questions, all of which required a yes or no answer. If replicated in more patients with CLIS, these results could abolish complete locked-in states, at least in ALS. With satisfactory care at home, quality of life is acceptable even in advanced ALS100–102, so the ability to communicate could have a great impact on the quality of life for patients with CLIS.

##### Communication in brainstem stroke

As in ALS, brainstem stroke can lead to locked-in syndrome so that patients require assistance to communicate. To date, research into the application of BCIs for communication in patients with locked-in syndrome after brainstem stroke103,104 is limited, but some studies do exist105–107. In one, the patient was trained to control her slow cortical potentials, but the study was terminated because she spontaneously regained some muscular control105. In another single-patient study, a P300 ERP-based BCI was used to train a patient to perform an on-screen task in which a ball was moved towards a target106. To date, only one successful study of BCIs for communication has involved two patients with locked-in syndrome after brainstem stroke107.

##### BCIs for movement rehabilitation

Current estimations suggest that >1% of the world’s population are living with the effects of cerebrovascular events such as stroke. These conditions are often accompanied by a deterioration or loss of function that manifests as paralysis (for example, hemiplegia or locked-in syndrome), speech apraxia or cognitive deficits. 85% of all stroke survivors are affected by deficits of movement control108–111, with a devastating effect on quality of life and ability to carry out activities of daily living. For this reason, the most common application of rehabilitative BCIs is in patients with stroke, and we focus on this application below.

##### Network reorganization after stroke

Many therapeutic strategies have been developed to help stroke patients regain some function, but many patients do not benefit from these approaches; estimates suggest that ~80% of all stroke survivors with upper limb motor deficits do not fully regain the function of the affected limb112. Consequently, alternative therapeutic approaches are needed, and the use of BCIs is one possibility.

BCIs that have been developed for stroke rehabilitation have been designed to manipulate the brain reorganization that is thought to occur after a stroke.

The present view of brain reorganization in chronic stroke is that overuse of the healthy contralesional hemisphere and underuse of the ipsilesional hemisphere leads to increased inhibition of the ipsilesional hemisphere by the contralesional hemisphere. This inhibition is thought to block excitatory reorganization of the intact ipsilesional areas and block recovery of the affected motor system113. This hypothesis is supported by the positive effects of constraint movement therapy114 in chronic stroke and other motor and language disorders115. In this therapy, physical restraint of the healthy limb for an extended period of time forces the patient to use the paretic limb and increases excitatory neural activity in the lesioned hemisphere. The technique offers no clinical benefit for patients without residual movement 1 year after stroke115, but does still increase the flow of information from the contralesional hemisphere to the ipsilesional hemisphere116.

In light of these findings, modern approaches to stroke rehabilitation have begun to focus on top-down rehabilitation for stroke recovery, with the aim of assisting or inducing the reorganization of neural circuits117. Examples of such methods include functional electrical stimulation, stem cell based therapies, pharmacological interventions and the use of BCIs118,119.

##### BCIs and network‑based rehabilitation

Patients with severe hemiparesis after stroke generally exhibit limited to no recovery in response to conventional treatment strategies73, but evidence suggests that BCIs could offer an effective rehabilitation strategy for patients with severe impairments. The learning of neuroprosthetic control has been shown to reshape cortical networks120 and trigger large-scale modifications of the cortical network, even in perilesional areas121. The overall principle is thought to be that closing the loop between cortical activity (motor intention) and movement73,122,123 — thereby producing afferent feedback activity — might restore functional corticospinal and corticomuscular connections.

In a double-blinded, controlled study, even patients with chronic stroke and severe upper limb impairment markedly improved as a result of proprioceptive BCI training (FIG. 2) (REF. 73). Over 20 sessions, patients learned to control a neuroprosthetic device fixed to their paretic limb by decreasing the power of the sensorimotor rhythm in the ipsilesional motor cortex. They were instructed to change their brain rhythm by attempting to move their paralyzed arm, even if no movement was possible. In the initial proof-of-concept study116, improvements did not generalize to everyday function outside the laboratory. Results of the follow-up study were more promising. In this study, patients received additional behavioural physiotherapy to facilitate the generalization of improvements, and received online proprioceptive feedback of brain oscillations; half of the participants received contingent reward feedback, whereas the other half received feedback of random brain activity. Marked improvements in motor function were seen in the patients that received contingent reward feedback, but not in the group that received random

feedback73. Furthermore, a consistent pattern of brain reorganization and connectivity changes was seen in the patients who improved, but not in the controls. The behavioural benefits remained stable during a 6-month follow-up period.

This study proved that use of BCIs can be effective in chronic stroke motor rehabilitation and demonstrated that cortical and subcortical reorganization (including functional and structural connectivity) in stroke patients without residual movement73 is a consequence of BCI use. Subsequent controlled clinical studies have confirmed these results124–126 and have combined the use of BCIs with noninvasive brain stimulation, such as transcranial direct current stimulation, with promising results127.

##### Future advances in rehabilitative BCIs

Most existing neural interfaces are used to control only the kinematics (velocity, acceleration, position) of paretic limb movement and not the kinetics (forces and torques)128. However, kinetics are essential for any functional movement required for specific skills, so the incorporation of kinetics into the decoding of brain activity via a BCI is needed. Use of brain control, such as neurofeedback learning, without involvement of the muscles — and consequently no kinetic control — might impede functional reorganization of the neural networks involved in functional visuomotor tasks, meaning that removal of the assistive technology results in the patient returning to their previous level of motor impairment. Therefore, a hybrid approach should

400 200

- -200
- -400 200
- -200
- -400
- -400

400 200

- -200

400

()μν

EEG

-1.50

-1.00 -0.50 0.00 0.50 1.00 1.50 2.00 2.50 3.00 3.50

Time (sec)

Signal processing

SMR

]Power [2μν

0 SMR frequency (Hz) 60

SMR

Movement decoding

Power []2μν

0 SMR frequency (Hz) 60

Nature Reviews | Neurology

Figure 2 | Use of a brain–computer interface in severe chronic stroke. EEG activity recorded over the motor perilesional area (top) is used to drive an exoskeleton attached to a patient’s arm or hand (bottom right). The patients are instructed to try to move their limb, and if they produce a desynchronization of sensorimotor rhythm (SMR), their limb moves. In the bottom left spectograms, the red traces are example spectrograms of SMR power when at rest and the blue traces are example spectrograms of SMR power when attempting to move. The blue area of the bar represents desynchronization or low power, and the red area of the bar represents synchronization or high power. If the participant generates a trace like the grey one in the lower spectrogram, the intent to move is detected and the device moves their arm. If the trace is like the grey one in the upper spectrogram, no intent to move is detected, and the device does not move the arm. This contingent association between motor intention and the movement facilitates instrumental learning and rewiring of brain areas that are responsible for motor intention and execution. Permission obtained from John Wiley and Sons © Ramos-Murguialday, A. Ann. Neurol. 74, 100–108 (2013).

###### Table 1 | Ongoing clinical trials of brain–computer interfaces, arranged by technology

Official Title Trial ID Disorder EEG

Brainwave control of a wearable robotic arm for rehabilitation and neurophysiological study in cervical spine injury (CSI: Brainwave)

NCT02443558 Spinal cord injury

BCI and neuromuscular stimulation for rehabilitation following acute stroke (BCI-NMES-CVA)

DRKS00007832 Stroke

BMI control of a robotic exoskeleton in training upper extremity functions in stroke

NCT01948739 Stroke

BMI for upper extremity function among patients with chronic hemiparetic stroke

JPRN-UMIN000008468 Stroke

BCI for communication in ventilated patients NCT02791425 Critical illness with nonverbal communication but need for mechanical ventilation and intratracheal intubation

Feasibility study of the mindBEAGLE device in patients with disorders of consciousness or locked-in syndrome

NCT02772302 Consciousness disorders, locked-in syndrome

A BCI-driven paired associative stimulation (PAS) protocol: an investigation of the effects of a 4-week BCI-PAS intervention on cortical excitability and walking performance in people with stroke

ACTRN12615001380583 Stroke

Transcranial direct current stimulation modulates EEG signals of BCI in stroke patients: a randomized controlled pilot study

TCTR20160606003 Stroke

BCI and brain-controlled stroke rehabilitation method utilizing EEG in hemiparetic and hemiplegic stroke patients to achieve thought control of machines and a better understanding of brain function

NCT02552368 Stroke

Effects of neurofeedback training with an EEG-based BCI for hand paralysis with stroke

JPRN-UMIN000017233 Stroke

A novel BCI-controlled pneumatic glove system for neurorehabilitation post-stroke

NCT02404857 Chronic stroke

BCI-assisted motor imagery for gait retraining in neurorehabilitation

NCT02507895 Stroke

BCI system for stroke rehabilitation NCT02323061 Stroke Brain training system using EEG for neurorehabilitation of hand function after stroke

NCT02323074 Stroke

A multicentre randomized single-blinded placebo-controlled study to assess efficacy of hand exoskeleton controlled by motor imagery based BCI for post stroke patients movement rehabilitation

NCT02325947 Stroke

Clinical validation protocol for BCI for the communication of patients suffering from neuromuscular disorders (PVCAFM)

NCT02284022 Neuromuscular disease

A brain centered neuroengineering approach for motor recovery after stroke: combined repetitive transcranial magnetic stimulation and BCI training

NCT02132520 Stroke

Communication by BCI in amyotrophic lateral sclerosis: feasibility study

NCT01897818 Amyotrophic lateral sclerosis

Evaluating the effectiveness of wireless EEG-based BCI-controlled neurorehabilitation system in patients with stroke

NCT01880268 Stroke

EEG-based BCI project for individuals with ALS NCT00718458 Amyotrophic lateral sclerosis

BCI control of functional electrical stimulation for hand therapy in tetraplegic patients

NCT01852279 Spinal cord injury

Electrocorticography BCI interface: neuroprosthetic control of a motorized exoskeleton NCT02550522 Spinal cord injury Clinical research on motor and communication BMIs JPRN-UMIN000007676 Amyotrophic lateral

sclerosis

###### Table 1 (cont.) | Ongoing clinical trials of brain–computer interfaces arranged by technology

Official Title Trial ID Disorder

Electrocorticography

Utrecht Neural Prosthesis (UNP): a pilot study on controllability of brain signals and application in locked-in patients

NCT02224469 Locked-in syndrome (trauma, stroke, neurodegeneration)

Multi-unit activity recordings

A neurorehabilitation therapy based on a BMI for the restoration of themotor function restoration of the upper limb in chronic stroke patients

ISRCTN10150672 Stroke

A sensorimotor microelectrode BMI for individuals with tetraplegia

NCT01894802 Spinal cord injury

Microelectrode BMI for individuals with tetraplegia NCT01364480 Spinal cord injury Feasibility study for use of a brain implant for neural control of a computer

NCT01958086 Spinal cord injury

A feasibility study of the ability of the neural prosthetic system to provide direct brain control of extracorporeal devices in patients with quadriplegia due to high spinal cord injury

NCT01849822 Spinal cord injury

A feasibility study of the ability of the neural prosthetic system 2 to provide direct closed loop cortical control of extracorporeal devices through the use of intracortical microstimulation in patients with quadriplegia

NCT01964261 Spinal cord injury

Deep-brain stimulation-like approach

Early feasibility study of a Medtronic Activa® PC+S system (Medtronic, Dublin, Ireland) for persons living with spinal cord injury

NCT02564419 Spinal cord injury

BCI, brain–computer interface; BMI, brain–machine interface.

be considered, in which residual muscle activity is related to the contingent connection between activity in the perilesional cortical areas and movement-related afferent feedback or passive movement of a prosthesis. Similarly, residual EMG activity can be detected in the paralyzed limbs of ~45% of patients with severe chronic stroke and can be used to decode movement intention73, so could be used to control rehabilitative robotic devices.

Further work is needed to overcome specific technical challenges associated with BCI learning and rehabilitation. For example, studies of BCI-based neurorehabilitation have shown that neural plasticity is induced if the response latency relative to the user’s intention is in the order of a few hundred milliseconds or less129. With longer time delays between the intention to move (detected as the neuroelectric signal) and the feedback from the movement, learning was less efficient. More work is needed to determine the optimal timings required to maximize learning.

A broader area that requires further investigation is rehabilitaton of the lower limbs. Upper-limb recovery has been investigated extensively, but approaches to lower-limb rehabilitation have been explored only relatively recently with BCIs to detect movement intention130. In this study, slow cortical potentials with a negative polarity were successfully used to detect preparation for movement of the lower limbs, indicating that slow cortical potentials could be used to drive a BCI for rehabilitation of leg movements after stroke.

In addition, we think that more demanding rehabilitation therapies are needed to increase the motivation and intensity of rehabilitative training. Videogames and virtual or augmented reality platforms should have an important role at this front.

We are aware of several ongoing clinical trials of BCIs for communication and rehabilitation in paralyzed patients (TABLE 1). Several of these trials are based on BCIs to control body actuators, such as exoskeletons and functional electrical stimulation, and we are convinced that data gathered in the coming years will help us to understand the functional neuroplastic mechanisms of BCI learning and, hopefully, motor recovery. There is a clear need for more randomized clinical trials of BCI-mediated stroke rehabilitation using multimodal imaging techniques.

##### BCIs for movement assistance

In addition to rehabilitation of movement after stroke, BCIs have the potential to provide assistance with movement in patients who are paralyzed as a result of ALS, stroke or spinal cord injury. A number of studies have been conducted in these contexts, using both invasive and noninvasive BCI systems.

##### Paralysis in ALS

Several studies have used an invasive BCI to enable patients with ALS to control a robotic hand. In one of these studies, an implanted microelectrode array provided patients with an astonishing range of performance:

the patients were able to perform reach and grasp movements in three dimensions25. However, although neither of the two patients in this study could speak, both were in possession of head and minimal arm movements, and one did not need artificial ventilation during the night, so the benefits to patients with more severe paralysis are unclear. Another study in which an invasive BCI was used provided patients with even more complex movement control131.

##### Spinal cord injury

Assistive BCIs offer great potential for patients with spinal cord injury. Currently, ~330,000 people in Europe are survivors of SCI, and ~11,000 new injuries occur each year132,133. Prevalence in the USA is similar, according to the National Spinal Cord Injury Statistical Center 2016. For these patients, the aim of BCIs is to provide assistive technologies that enable them to communicate and/or control body actuators, such as a robotic arm, a wheelchair or functional electrical stimulation. The spinal cord system exhibits considerable plasticity in instrumental and classical learning procedures134, which enables flexible adaptation of the spinal neurons to changing environmental conditions, and BCIs have the potential to act as an associative bridge between intention and skilled motor action in a similar way to that described above for stroke rehabilitation.

Only ~5% of studies of BCIs for spinal cord injury have involved end users, but evidence has shown that online use of invasive or noninvasive BCIs can be used by patients with spinal cord injury to control on-screen cursors, move external devices or directly control the upper or lower limbs18,25,122,131,134–138. The first proof-of-concept experiments demonstrated that patients had the ability to control their brain activity after a spinal cord injury18,135; patients learned to control an artificial output and control a computer via a cursor and ‘click’ control to communicate.

Subsequent studies have demonstrated that online brain control of functional electric stimulation is possible for patients with spinal cord injury using invasive and noninvasive techniques for control of the upper limbs136,139 and only noninvasive techniques for control of the lower limbs140. In these studies, a functional electric stimulation sequence that was preprogrammed to provoke functional movements of the paralyzed limbs was activated via the BCI. This so-called trigger approach exploited sensorimotor rhythms to detect the patient´s intention to move, which triggered stimulation and consequent contraction of muscles in the paralyzed limb. In this paradigm, patients must wait until the stimulation sequence has finished and the EEG recordings return to baseline to be able to control the functional electric stimulation again, so the approach is very limited for everyday use.

Invasive and noninvasive BCI systems have also been used to enable neural control of a robotic arm25,131,135,141. Approaches that used noninvasive systems provided limited control, and most complex movement relied on the artificial intelligence of the robot. However, use of implantable electrodes allowed patients to

control movement with several degrees of freedom, enabling them to make more complex and functional movements.

Finally, patients with spinal cord injuries have been able to control a wheelchair with a noninvasive EEGbased BCI137. For patients with severe paralysis, this system has the potential to provide patients a new way of controlling their wheelchair, but the EEG signal is currently too unreliable to be used as the only control signal for any assistive device.

All of these approaches to assistive technology for patients with spinal cord injury have aimed to provide patients with control of their paralyzed limbs. However, the possibility that similar systems could bring about neuroplastic changes that contribute to functional rehabilitation remains open, and the technologies described in combination with existing pharmacological and neurostimulation interventions142,143 could hold the key to motor recovery after spinal cord injury.

##### Conclusions and future perspectives

At present, the data on the use of BCIs to enable communication for patients who are completely paralyzed are limited, and clinically applicable BCIs have only recently become available for patients with CLIS as a result of ALS. Invasive and noninvasive BCIs that use more than one type of brain signal have considerable potential, because no alternative exists for communication in CLIS and no alternative to BCIs will exist in the foreseeable future. Of the utmost clinical importance is the extension of the promising results in patients with ALS or subcortical stroke to patients with varying degrees of traumatic144,145 and neurodegenerative brain damage and generalization to patients with disorders of consciousness146,147, such as minimal conscious state148; the combined BCIs offer a good chance of at least minimal social interaction and communication in these patient groups. Still unclear, however, is which subgroups of patients with brain damage and/or minimal conscious state would benefit from a BCI. Diagnostic criteria for MCS, vegetative state and CLIS lack specificity and do not allow clear differentiation between these disorders, so only studies of BCIs in large patient groups will enable definite conclusions to be reached about the value of BCIs in specific patient subsets.

For severe chronic stroke without residual hand movement, noninvasive neuroelectric-based BCI training combined with physiotherapy to facilitate generalization to everyday life is a promising and economically feasible option. However, an increase in the degrees of freedom provided in motor restoration (and probably neuronal plasticity and recovery at a cellular level) in chronic stroke and SCI, will require an invasive approach with implanted, wireless electrode arrays that are permanently connected to peripheral neuroprosthetic devices, exoskeletons and functional electric stimulation devices at the cortical, spinal and/or neuromuscular levels. In summary, over the relatively short period of two decades, clinical research into BCIs has provided us with extremely promising strategies to improve the prospects for patients with otherwise debilitating neurological disorders that are currently difficult or impossible to treat.

- 1. Wyrwicka, W. & Sterman, M. B. Instrumental conditioning of sensorimotor cortex EEG spindles in the waking cat. Physiol. Behav. 3, 703–707

(1968).

- 2. Kamiya, J. in Altered states of consciousness. (ed Tart, C.) 519–529 (New York: Wiley, 1969).
- 3. Fetz, E. E. & Baker, M. A. Operantly conditioned patterns on precentral unit activity and correlated responses in adjacent cells and contralateral muscles. J. Neurophysiol. 36, 179–204 (1973).
- 4. Vidal, J.-J. Toward direct brain-computer communication. Annu. Rev. Biophys. Bioeng. 2, 157–180 (1973). The first paper describing a brain computer interface and the hypothetical learning mechanisms involved.
- 5. Sterman, M. B., Wyrwicka, W. & Roth, S. Electrophysiological correlates and neural substrates of alimentary behavior in the cat. Ann. NY Acad. Sci. 157, 723–739 (1969).
- 6. Sterman, M. & Friar, L. Suppression of seizures in epileptic Following on sensorimotor EEG feedback training. Electroencephalogr. Clin. Neurophysiol. 33, 89–95 (1972).
- 7. Lubar, J. F. & Shouse, M. N. EEG and behavioral changes in a hyperkinetic child concurrent with training of the sensorimotor rhythm (SMR) - A preliminary report. Biofeedback Self Regul. 1, 293–306 (1976).
- 8. Sterman, M. B. & Macdonald, L. R. Effects of central cortical EEG feedback training on incidence of poorly controlled seizures. Epilepsia 19, 207–222

(1978).

- 9. Chapin, J. K., Moxon, K. A., Markowitz, R. S. & Nicolelis, M. A. L. Real-time control of a robot arm using simultaneously recorded neurons in the motor cortex. Nat. Neurosci. 2, 664–670 (1999).
- 10. Donoghue, J. P. Connecting cortex to machines: recent advances in brain interfaces. Nat. Neurosci. 5, 1085–1088 (2002).
- 11. Nicolelis, M. A. L. Actions from thoughts. Nature 409, 403–407 (2001).
- 12. Velliste, M., Perel, S., Spalding, M. C., Whitford, A. S. & Schwartz, A. B. Cortical control of a prosthetic arm for self-feeding. Nature 453, 1098–1101 (2008).
- 13. Taylor, D. M., Tillery, S. I. H. & Schwartz, A. B. Direct Cortical Control of 3D Neuroprosthetic Devices. Sci. 296, 1829–1832 (2002).
- 14. Santhanam, G., Ryu, S. I., Yu, B. M., Afshar, A. & Shenoy, K. V. A high-performance brain-computer interface. Nature 442, 195–198 (2006).
- 15. Wessberg, J. et al. Real-time prediction of hand trajectory by ensembles of cortical neurons in primates. Nature 408, 361–365 (2000).
- 16. Serruya, M. D., Hatsopoulos, N. G., Paninski, L., Fellows, M. R. & Donoghue, J. P. Brain-machine interface: Instant neural control of a movement signal. Nature 416, 141–142 (2002).
- 17. Carmena, J. M. et al. Learning to control a brain– machine interface for reaching and grasping by primates. PLoS Biol. 1, e2 (2003). This paper provides the most advanced and detailed neurophysiological analysis of the neuronal mechanisms behind brain–computer interface control of complex movements.
- 18. Hochberg, L. R. et al. Neuronal ensemble control of prosthetic devices by a human with tetraplegia. Nature 442, 164–171 (2006).
- 19. Donoghue, J. P., Nurmikko, A., Black, M. & Hochberg, L. R. Assistive technology and robotic control using motor cortex ensemble-based neural interface systems in humans with tetraplegia. J. Physiol. 579, 603–611 (2007).
- 20. Birbaumer, N., Ramos Murguialday, A., Weber, C. & Montoya, P. Chapter 8 neurofeedback and braincomputer Interface: clinical applications. Int. Rev. Neurobiol. 86, 107–117 (2009).
- 21. Fuchs, T., Birbaumer, N., Lutzenberger, W., Gruzelier, J. H. & Kaiser, J. Neurofeedback treatment for attention-deficit / hyperactivity disorder in children: a comparison with methylphenidate. Appl. Psychophysiol. Biofeedback 28, 1–12 (2003).
- 22. Monastra, V. J. et al. Electroencephalographic biofeedback in the treatment of attention-deficit / hyperactivity disorder. J. Neurother. 9, 5–34

(2006).

- 23. Kotchoubey, B. et al. Modification of slow cortical potentials in patients with refractory epilepsy: a controlled outcome study. Epilepsia 42, 406–416

- 24. Gilja, V. et al. Clinical translation of a highperformance neural prosthesis. Nat. Med. 21, 1142–1145 (2015).
- 25. Hochberg, L. R. et al. Reach and grasp by people with tetraplegia using a neurally controlled robotic arm. Nature 485, 372–375 (2012). The first paper describing multidemensional movement control of an arm–hand robotic device using an implanted microelectrode array in the primary motor cortex of a paralyzed patient.
- 26. Jarosiewicz, B. et al. Virtual typing by people with tetraplegia using a stabilized, self-calibrating intracortical brain-computer interface. IEEE BRAIN Gd. Challenges Conf. Washington, DC 7, 1–11

(2014).

- 27. Pfurtscheller, G., Müller, G. R., Pfurtscheller, J., Gerner, H. J. & Rupp, R. ‘Thought ’ – control of functional electrical stimulation to restore hand grasp in a patient with tetraplegia. Neurosci. Lett. 351, 33–36 (2003).
- 28. Caria, A., Sitaram, R. & Birbaumer, N. Real-time fMRI: a tool for local brain regulation. Neuroscientist. 18, 487–501 (2012).
- 29. Chaudhary, U., Birbaumer, N. & Curado, M. R. Brainmachine interface (BMI) in paralysis. Ann. Phys. Rehabil. Med. 58, 9–13 (2015).
- 30. Nijboer, F. et al. An auditory brain–computer interface (BCI). J. Neurosci. Methods 167, 43–50

(2008).

- 31. Chatterjee, A., Aggarwal, V., Ramos, A., Acharya, S. & Thakor, N. V. A brain-computer interface with vibrotactile biofeedback for haptic information. J. Neuroeng. Rehabil. 4, 1–12 (2007).
- 32. Lugo, Z. R. et al. A vibrotactile p300-based braincomputer interface for consciousness detection and communication. Clin. EEG Neurosci. 45, 14–21

(2014).

- 33. Bansal, A. K., Truccolo, W., Vargas-Irwin, C. E. & Donoghue, J. P. Decoding 3D reach and grasp from hybrid signals in motor and premotor cortices: spikes, multiunit activity, and local field potentials. J. Neurophysiol. 107, 1337–1355 (2012).
- 34. Flint, R. D., Wright, Z. A., Scheid, M. R. & Slutzky, M. W. Long term, stable brain machine interface performance using local field potentials and multiunit spikes. J. Neural Eng. 10, 056005

(2013).

- 35. So, K., Dangi, S., Orsborn, A. L., Gastpar, M. C. & Carmena, J. M. Subject-specific modulation of local field potential spectral power during brain-machine interface control in primates. J. Neural Eng. 11, 026002 (2014).
- 36. Mehring, C. et al. Comparing information about arm movement direction in single channels of local and epicortical field potentials from monkey and human motor cortex. J. Physiol. Paris 98, 498–506

(2004).

- 37. Georgopoulos, A. P., Schwartz, A. B. & Kettner, R. E. Neuronal population coding of movement direction. Science 233, 1416–1419 (1986).
- 38. Georgopoulos, A. P. & Kettner, R. E. & Schwartz, A. B. Primate motor cortex and free arm movements to visual targets in three-dimensional space. II. Coding of the direction of movement by a neuronal population. J. Neurosci. 8, 2928–2937 (1988).
- 39. Serruya, M., Hatsopoulos, N., Paninski, L., Fellows, M. R. & Donoghue, J. P. Brain-machine interface: Instant neural control of a movement signal. Nature 416, 121–142 (2002).
- 40. Leuthardt, E. C., Schalk, G., Wolpaw, J. R., Ojemann, J. G. & Moran, D. W. A brain–computer interface using electrocorticographic signals in humans. J. Neural Eng. 1, 63–71 (2004).
- 41. Felton, E. a, Wilson, J. A., Williams, J. C. & Garell, P. C. Electrocorticographically controlled brain-computer interfaces using motor and sensory imagery in patients with temporary subdural electrode implants. Report of four cases. J. Neurosurg. 106, 495–500

(2007).

- 42. Clancy, K. B., Koralek, A. C., Costa, R. M., Feldman, D. E. & Carmena, J. M. Volitional modulation of optically recorded calcium signals during neuroprosthetic learning. Nat. Neurosci. 17, 807–809 (2014).
- 43. Birbaumer, N., Elbert, T., Canavan, A. & Rockstroh, B. Slow potentials of the cerebral cortex and behavior. Physiol. Rev. 70, 1–41 (1990).
- 44. Kubler, A. et al. Brain-computer communication: self regulation of slow cortical potentials for verbal communication. Arch. Phys. Med. Rehabil. 82, 1533–1539 (2001).

- 45. Birbaumer, N., Hinterberger, T., Kübler, A. & Neumann, N. The thought-translation device (TTD): neurobehavioral mechanisms and clinical outcome. IEEE Trans. Neural Syst. Rehabil. Eng. 11, 120–123 (2003).
- 46. Pfurtscheller, G. & Aranibar, A. Evaluation of eventrelated desynchronization (ERD) preceding and following voluntary self-paced movement. Electroencephalogr. Clin. Neurophysiol. 46, 138–146

(1979).

- 47. Kübler, A. et al. Patients with ALS can use sensorimotor rhythms to operate a brain-computer interface. Neurology 64, 1775–1777 (2005).
- 48. Wolpaw, J. R. et al. Brain-computer interfaces for communication and control. Clin. Neurophysiol. 113, 767–791 (2002).
- 49. Farwell, L. A. & Donchin, E. Talking off the top of your head: toward a mental prosthesis utilizing eventrelated brain potentials. Electroencephalogr. Clin. Neurophysiol. 70, 510–523 (1988).
- 50. Kübler, A. et al. A brain-computer interface controlled auditory event-related potential (p300) spelling system for locked-in patients. Ann. NY Acad. Sci. 1157, 90–100 (2009).
- 51. Halder, S. et al. An auditory oddball brain-computer interface for binary choices. Clin. Neurophysiol. 121, 516–523 (2010).
- 52. Pires, G., Nunes, U. & Castelo-Branco, M. Statistical spatial filtering for a P300-based BCI: Tests in ablebodied, and patients with cerebral palsy and amyotrophic lateral sclerosis. J. Neurosci. Methods 195, 270–281 (2011).
- 53. Sellers, E. W. & Donchin, E. A P300-based braincomputer interface: Initial tests by ALS patients. Clin. Neurophysiol. 117, 538–548 (2006).
- 54. Sellers, E. W., Vaughan, T. M. & Wolpaw, J. R. A brain-computer interface for long-term independent home use. Amyotroph. Lateral Scler. 11, 449–455

(2010).

- 55. Lesenfants, D. et al. An independent SSVEP-based brain-computer interface in locked-in syndrome. J. Neural Eng. Neural Eng. 11, 035002 (2014).
- 56. Zhu, D., Bieger, J., Molina, G. G. & Aarts, R. M. A survey of stimulation methods used in SSVEP-based BCIs. Comput. Intell. Neurosci. http://dx.doi.org/ 10.1155/2010/702357 (2010).
- 57. Chavarriaga, R. & Millán, J. del R. Learning from EEG error-related potentials in noninvasive brain-computer interfaces. IEEE Trans. Neural Syst. Rehabil. Eng. 18, 381–388 (2010).
- 58. Logothetis, N. K., Pauls, J., Augath, M., Trinath, T. & Oeltermann, A. Neurophysiological investigation of the basis of the fMRI signal. Nature 412, 150–157

(2001).

- 59. Birbaumer, N., Ruiz, S. & Sitaram, R. Learned regulation of brain metabolism. Trends Cogn. Sci. 17, 295–302 (2013). An extensive review of basic and clinical neurofeedback studies using learning of metabolic brain resonses (BOLD or oxygenation) and the effects on behaviour and cognition.
- 60. DeCharms, R. C. et al. Learned regulation of spatially localized brain activation using real-time fMRI. Neuroimage 21, 436–443 (2004).
- 61. Rota, G., Handjaras, G., Sitaram, R., Birbaumer, N. & Dogil, G. Reorganization of functional and effective connectivity during real-time fMRI-BCI modulation of prosody processing. Brain Lang. 117, 123–132

(2011).

- 62. Weiskopf, N. et al. Physiological self-regulation of regional brain activity using real-time functional magnetic resonance imaging (fMRI): methodology and exemplary data. Neuroimage 19, 577–586 (2003).
- 63. Yoo, S. S. et al. Brain computer interface using fMRI: spatial navigation by thoughts. Neuroreport 15, 1591–1595 (2004).
- 64. Birbaumer, N. et al. Deficient fear conditioning in psychopathy: a functional magnetic resonance imaging study. Arch. Gen. Psychiatry 62, 799–805

(2005).

- 65. Linden, D. E. J. et al. Real-time self-regulation of emotion networks in patients with depression. PLoS One http://dx.doi.org/10.1371/journal.pone.0038115

(2012).

- 66. Li, X. et al. Volitional reduction of anterior cingulate cortex activity produces decreased cue craving in smoking cessation: A preliminary real-time fMRI study. Addict. Biol. 18, 739–748 (2013).
- 67. Chaudhary, U., Hall, M., DeCerce, J., Rey, G. & Godavarty, A. Frontal activation and connectivity using near-infrared spectroscopy: verbal fluency language study. Brain Res. Bull. 84, 197–205 (2011).

(2001).

- 68. Chaudhary, U. et al. Motor response investigation in individuals with cerebral palsy using near infrared spectroscopy: pilot study. Appl. Opt. 53, 503–510

(2014).

- 69. Obrig, H. NIRS in clinical neurology - a ‘promising’ tool? Neuroimage 85, 535–546 (2014).
- 70. Gallegos-Ayala, G. et al. Brain communication in a completely locked-in patient using bedside nearinfrared spectroscopy. Neurology 82, 1930–1932

(2014). The first report of a controlled case study with BCI in a completely paralyzed, locked‑in patient restoring communication.

- 71. Naito, M. et al. A communication means for totally locked-in ALS patients based on changes in cerebral blood volume measured with near-infrared light. IEICE Trans. Inf. Syst. E90D, 1028–1037 (2007).
- 72. Birbaumer, N. et al. A spelling device for the paralysed. Nature 398, 297–298 (1999).
- 73. Ramos-Murguialday, A. et al. Brain-machine interface in chronic stroke rehabilitation: a controlled study. Ann. Neurol. 74, 100–108 (2014).
- 74. Birbaumer, N., Murguialday, A. R. & Cohen, L. Braincomputer interface in paralysis. Curr. Opin. Neurol. 21, 634–638 (2008).
- 75. Chou, S. M. & Norris, F. H. Amyotrophic lateral sclerosis: Lower motor neuron disease spreading to upper motor neurons. Muscle Nerve 16, 864–869

(1993).

- 76. Bauer, G., Gerstenbrand, F. & Rumpl, E. Varieties of the Locked-in Syndrome. J. Neurol. 221, 77–91

(1979).

- 77. Beukelman, D., Fager, S. & Nordness, A. Communication support for people with ALS. Neurol. Res. Int. 2011, 714693 (2011).
- 78. Beukelman, D. & Mirenda, P. Augmentative & alternative communication: Supporting children & adults with complex communication needs. (Paul, H. Brookes, Baltimore, MD, 2005).
- 79. Birbaumer, N. & Cohen, L. G. Brain-computer interfaces: communication and restoration of movement in paralysis. J. Physiol. 579, 621–636

(2007).

- 80. Kennedy, P. R. & Bakay, R. A. Restoration of neural output from a paralyzed patient by a direct brain connection. Neuroreport 9, 1707–1711 (1998).
- 81. Kennedy, P. R., Bakay, R. A., Moore, M. M., Adams, K. & Goldwaithe, J. Direct control of a computer from the human central nervous system. IEEE Trans. Rehabil. Eng. 8, 198–202 (2000).
- 82. Kennedy, P. et al. Using human extra-cortical local field potentials to control a switch. J. Neural Eng. 1, 72–77 (2004).
- 83. Wilhelm, B., Jordan, M. & Birbaumer, N. Communication in locked-in syndrome: effects of imagery on salivary pH. Neurology 67, 534–535

(2006).

- 84. Murguialday, A. R. et al. Transition from the locked in to the completely locked-in state: a physiological analysis. Clin. Neurophysiol. 122, 925–933 (2011).
- 85. Birbaumer, N. Breaking the silence: brain-computer interfaces (BCI) for communication and motor control. Psychophysiology 43, 517–532 (2006).
- 86. Kübler, A. & Birbaumer, N. Brain-computer interfaces and communication in paralysis: extinction of goal directed thinking in completely paralysed patients? Clin. Neurophysiol. 119, 2658–2666 (2008).
- 87. Wolpaw, J. R. & McFarland, D. J. Control of a twodimensional movement signal by a noninvasive braincomputer interface in humans. Proc. Natl Acad. Sci. USA 101, 17849–17854 (2004).
- 88. Bai, O., Lin, P., Huang, D., Fei, D. Y. & Floeter, M. K. Towards a user-friendly brain-computer interface: initial tests in ALS and PLS patients. Clin. Neurophysiol. 121, 1293–1303 (2010).
- 89. Thorns, J. et al. Movement initiation and inhibition are impaired in amyotrophic lateral sclerosis. Exp. Neurol. 224, 389–394 (2010).
- 90. Birbaumer, N., Piccione, F., Silvoni, S. & Wildgruber, M. Ideomotor silence: the case of complete paralysis and brain-computer interfaces (BCI). Psychol. Res. 76, 183–191 (2012).
- 91. Hinterberger, T. et al. Neuronal mechanisms underlying control of a brain – computer interface. Eur. J. Neurosci. 21, 3169–3181 (2005).
- 92. Hinterberger, T. et al. Voluntary brain regulation and communication with electrocorticogram signals. Epilepsy Behav. 13, 300–306 (2008).
- 93. Koralek, A. C. et al. Corticostriatal plasticity is necessary for learning intentional neuroprosthetic skills. Nature 483, 331–335 (2012).

- 94. Dworkin, B. R. & Miller, N. E. Failure to replicate visceral learning in the acute curarized rat preparation. Behav. Neurosci. 100, 299–314

(1986). This paper describes the failure to establish instrumental learning of physiological responses in the curarized rat and possible reasons for this problem.

- 95. Stocco, A., Lebiere, C. & Anderson, J. R. Conditional routing of information to the cortex: a model of the basal ganglia’s role in cognitive coordination. Psychol. Rev. 117, 541–574 (2010).
- 96. Birbaumer, N. & Chaudhary, U. Learning from brain control: clinical application of brain–computer interfaces. e-Neuroforum 6, 87–95 (2015).
- 97. Furdea, A. et al. A new (semantic) reflexive braincomputer interface: in search for a suitable classifier. J. Neurosci. Methods 203, 233–240 (2012).
- 98. Ruf, C. A., De Massari, D., Wagner-Podmaniczky, F., Matuz, T. & Birbaumer, N. Semantic conditioning of salivary pH for communication. Artif. Intell. Med. 59, 1–8 (2013).
- 99. De Massari, D. et al. Brain communication in the locked-in state. Brain 136, 1989–2000 (2013).
- 100. Lulé, D. et al. Brain responses to emotional stimuli in patients with amyotrophic lateral sclerosis (ALS). J. Neurol. 254, 519–527 (2007).
- 101. Lulé, D. et al. Life can be worth living in locked-in syndrome. Prog. Brain Res. 177, 339–351 (2009).
- 102. Lulé, D. et al. Quality of life in fatal disease: the flawed judgement of the social environment. J. Neurol. 260, 2836–2843 (2013).
- 103. Chaudhary, U. & Birbaumer, N. Communication in locked-in state after brainstem stroke: a braincomputer-interface approach. Ann. Transl. Med. 3, 2–4 (2015).
- 104. Simeral, J. D., Kim, S. P., Black, M. J., Donoghue, J. P. & Hochberg, L. R. Neural control of cursor trajectory and click by a human with tetraplegia 1000 days after implant of an intracortical microelectrode array. J. Neural Eng. 8, 025027 (2011).
- 105. Kübler, A. et al. Self-regulation of slow cortical potentials in completely paralyzed human patients. Neurosci. Lett. 252, 171–174 (1998).
- 106. Piccione, F. et al. P300-based brain computer interface: reliability and performance in healthy and paralysed participants. Clin. Neurophysiol. 117, 531–537 (2006).
- 107. Sellers, E. W., Ryan, D. B. & Hauser, C. K. Noninvasive brain-computer interface enables communication after brainstem stroke. Sci. Transl. Med. 6, 257re7

(2014).

- 108. Cirstea, M. C., Ptito, A. & Levin, M. F. Arm reaching improvements with short-term practice depend on the severity of the motor deficit in stroke. Exp. Brain Res. 152, 476–488 (2003).
- 109. Young, J. & Forster, A. Review of stroke rehabilitation. BMJ 334, 86–90 (2007).
- 110. Saka, O., McGuire, A. & Wolfe, C. Cost of stroke in the United Kingdom. Age Ageing 38, 27–32 (2008).
- 111. Langhorne, P., Bernhardt, J. & Kwakkel, G. Stroke rehabilitation. Lancet 377, 1693–1702 (2015).
- 112. Hendricks, H. T., van Limbeek, J., Geurts, A. C. & Zwarts, M. J. Motor recovery after stroke: a systematic review of the literature. Arch. Phys. Med. Rehabil. 83, 1629–1637 (2002).
- 113. Ward, N. S. & Cohen, L. G. Mechanisms underlying recovery of motor function after stroke. Arch. Neurol. 61, 1844–1848 (2004).
- 114. Taub, E., Uswatte, G. & Pidikiti, R. Constraintinduced movement therapy: a new family of techniques with broad application to physical rehabilitation – a clinical review. J. Rehabil. Res. Dev. 36, 237–251 (1999).
- 115. Wolf, S. L. et al. Effect of constraint-induced movement therapy on upper extremity function 3 to 9 months after stroke: the EXCITE randomized clinical trial. JAMA 296, 2095–2104 (2006).
- 116. Buch, E. R. et al. Parietofrontal integrity determines neural modulation associated with grasping imagery after stroke. Brain 135, 596–614 (2012).
- 117. Belda-Lois, J.-M. et al. Rehabilitation of gait after stroke: a review towards a top-down approach. J. Neuroeng. Rehabil. 8, 66 (2011).
- 118. Chollet, F. et al. Fluoxetine for motor recovery after acute ischaemic stroke (FLAME): a randomised placebo-controlled trial. Lancet Neurol. 10, 123–130

(2011).

- 119. Savitz, S. I. et al. Stem cells as an emerging paradigm in stroke 3: enhancing the development of clinical trials. Stroke 45, 634–639 (2014).

- 120. Ganguly, K., Dimitrov, D. F., Wallis, J. D. & Carmena, J. M. Reversible large-scale modification of cortical networks during neuroprosthetic control. Nat. Neurosci. 14, 662–667 (2011).
- 121. Gulati, T. et al. Robust neuroprosthetic control from the stroke perilesional cortex. J. Neurosci. 35, 8653–8661 (2015).
- 122. Nishimura, Y., Perlmutter, S. I., Eaton, R. W. & Fetz, E. E. Spike-timing-dependent plasticity in primate corticospinal connections induced during free behavior. Neuron 80, 1301–1309 (2013). This paper describes the neurophysiological bases of BCI applications in spinal cord injury.
- 123. Lucas, T. H. & Fetz, E. E. Myo-cortical crossed feedback reorganizes primate motor cortex output. J. Neurosci. 33, 5261–5274 (2013).
- 124. Ang, K. K. et al. Brain-computer interface-based robotic end effector system for wrist and hand rehabilitation: results of a three-armed randomized controlled trial for chronic stroke. Front. Neuroeng. http://dx.doi.org/10.3389/fneng.2014.00030 (2014).
- 125. Ono, T. et al. Brain-computer interface with somatosensory feedback improves functional recovery from severe hemiplegia due to chronic stroke. Front. Neuroeng. http://dx.doi.org/10.3389/ fneng.2014.00019 (2014).
- 126. Pichiorri, F. et al. Brain–computer interface boosts motor imagery practice during stroke recovery. Ann. Neurol. 77, 851–865 (2015).
- 127. Kasahara, K., DaSalla, C. S., Honda, M. & Hanakawa, T. Neuroanatomical correlates of brain– computer interface performance. Neuroimage 110, 95–100 (2015).
- 128. Bensmaia, S. J. & Miller, L. E. Restoring sensorimotor function through intracortical interfaces: progress and looming challenges. Nat. Rev. Neurosci. 15, 313–325

(2014).

- 129. Ren, X. et al. Enhanced low-latency detection of motor intention from EEG for closed-loop brain-computer interface applications. Biomed. Eng. IEEE Trans. 61, 288–296 (2014).
- 130. Jiang, N., Gizzi, L., Mrachacz-Kersting, N., Dremstrup, K. & Farina, D. A brain–computer interface for single-trial detection of gait initiation from movement related cortical potentials. Clin. Neurophysiol. 126, 154–159 (2015).
- 131. Collinger, J. L. et al. High-performance neuroprosthetic control by an individual with tetraplegia. Lancet 381, 557–564 (2013).
- 132. Ouzký, M. Towards concerted efforts for treating and curing spinal cord injury (Council of Europe Parliamentary Assembly document 9401). https:// assembly.coe.int/nw/xml/XRef/X2H-Xref-ViewHTML. asp?FileID=9680&lang=en (2002)
- 133. Van Den Berg, M. E., Castellote, J. M., MahilloFernandez, I. & De Pedro-Cuesta, J. Incidence of spinal cord injury worldwide: a systematic review. Neuroepidemiology 34, 184–192 (2010).
- 134. Wolpaw, J. R. The complex structure of a simple memory. Trends Neurosci. 20, 588–594 (1997).
- 135. Wang, W. et al. An electrocorticographic brain interface in an individual with tetraplegia. PLoS ONE http:// dx.doi.org/10.1371/journal.pone.0055344 (2013).
- 136. Pfurtscheller, G., Müller, G. R., Pfurtscheller, J. & Gerner, H. J. & Rupp, R. ‘Thought’ - Control of functional electrical stimulation to restore hand grasp in a patient with tetraplegia. Neurosci. Lett. 351, 33–36 (2003).
- 137. Nguyen, J. S., Su, S. W. & Nguyen, H. T. Experimental study on a smart wheelchair system using a combination of stereoscopic and spherical vision. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2013, 4597–4600 (2013).
- 138. Kasashima-Shindo, Y. et al. Brain–computer interface training combined with transcranial direct current stimulation in patients with chronic severe hemiparesis: proof of concept study. J. Rehabil. Med. 47, 318–324 (2015).
- 139. Enzinger, C. et al. Brain motor system function in a patient with complete spinal cord injury following extensive brain-computer interface training. Exp. Brain Res. 190, 215–223 (2008).
- 140. King, C. E. et al. The feasibility of a brain-computer interface functional electrical stimulation system for the restoration of overground walking after paraplegia. J. Neuroeng. Rehabil. 12, 80 (2015).
- 141. Pfurtscheller, G., Guger, C., Müller, G., Krausz, G. & Neuper, C. Brain oscillations control hand orthosis in a tetraplegic. Neurosci. Lett. 292, 211–214 (2000). The first paper demonstrating noninvasive brain control using a sensorimotor rhythm brain– computer interface in a high spinal cord patient.

- 142. Courtine, G. & Bloch, J. Defining Ecological Strategies in Neuroprosthetics. Neuron 86, 29–33

(2015).

- 143. van den Brand, R. et al. Restoring voluntary control of locomotion after paralyzing spinal cord injury. Science 336, 1182–1185 (2012).
- 144. Combaz, A. et al. A comparison of two spelling braincomputer interfaces based on visual P3 and SSVEP in locked-in syndrome. PLoS ONE http://dx.doi.org/ 10.1371/journal.pone.0073691 (2013).
- 145. Bardin, J. C. et al. Dissociations between behavioural and functional magnetic resonance imaging-based evaluations of cognitive function after brain injury. Brain 134, 769–782 (2011).
- 146. Monti, M. M. et al. Willful modulation of brain activity in disorders of consciousness. N. Engl. J. Med. 362, 579–589 (2010).

- 147. Schnakers, C. et al. Detecting consciousness in a total locked-in syndrome: an active event-related paradigm. Neurocase 15, 271–277 (2009).
- 148. Lulé, D. et al. Probing command following in patients with disorders of consciousness using a braincomputer interface. Clin. Neurophysiol. 124, 101–106 (2013).

###### Acknowledgements

The authors are funded by Deutsche Forschungsgemeinschaft (DFG, Bi195, Kosellek), Stiftung Volkswagenwerk (VW), German Ministry of Education and Research (BMBF, grant number MOTOR-BIC (FKZ 136W0053), Ministry of Science, Research and the Arts of Baden Wüttemberg (Az: 32–729.63-0/5-5), Baden-Württemberg Stiftung (ROB-1), EMOIO from the Federal Ministry of Education and Research (BMBF, 524-4013-16SV7196) and Eva and Horst

Köhler-Stiftung, (Berlin), EU (Horizon 2020) grant “Brain Train” and “Luminous”, Brain Products, Munich, Germany, and the Wyss Foundation, Geneva, Switzerland.

###### Author contributions

All authors contributed equally to all aspects of preparing the manuscript.

###### Competing interests statement

The authors declare no competing interests.

###### FURTHER INFORMATION

National Spinal Cord Injury Statistical Center http://www.uab.edu/NSCISC

###### ALL LINKS ARE ACTIVE IN THE ONLINE PDF

NATURE REVIEWS | NEUROLOGY ADVANCE ONLINE PUBLICATION | 13 © 2016 Mac millan Publishers Li mited, part of Springer Nature. All rights reserved. © 2016 Mac millan Publishers Li mited, part of Springer Nature. All rights reserved.

View publication stats

