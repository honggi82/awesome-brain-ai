### Review ARticle

published 07 September 2010 doi:10.3389/fnins.2010.00161

# Combining brain–computer interfaces and assistive technologies: state-of-the-art and challenges

## J. d. R. Millán1*, R. Rupp2, G. R. Müller-Putz3, R. Murray-Smith4, C. Giugliemma5, M. Tangermann6, C. Vidaurre6, F. Cincotti7, A. Kübler8, R. Leeb1, C. Neuper3, K.-R. Müller6 and D. Mattia7

- 1 Defitech Chair in Non-Invasive Brain-Machine Interface, Center for Neuroprosthetics, School of Engineering, Ecole Polytechnique Fédérale de Lausanne, Lausanne, Switzerland
- 2 Stiftung Orthopädische Universitätsklinik Heidelberg, Heidelberg, Germany
- 3 Laboratory of Brain-Computer Interfaces, Institute for Knowledge Discovery, Graz University of Technology, Graz, Austria
- 4 Department of Computing Science, Glasgow University, Glasgow, Scotland
- 5 QualiLife S.A., Paradiso-Lugano, Switzerland
- 6 Chair Machine Learning, Technical University of Berlin, Berlin, Germany
- 7 Clinical Neurophysiology, Fondazione Santa Lucia, Rome, Italy
- 8 Lehrstuhl für Psychologie I, Universität Würzburg, Würzburg, Germany

Edited by: Cuntai Guan, Institute for Infocomm Research, Singapore Reviewed by: Fabien Lotte, Institute for Infocomm Research, Singapore Ranganatha Sitaram, Eberhard-KarlsUniversität Tübingen, Germany

*Correspondence: J. d. R. Millán, Defitech Chair in Non-Invasive Brain-Machine Interface, Center for Neuroprosthetics, School of Engineering, Ecole Polytechnique Fédérale de Lausanne, Lausanne, Switzerland. e-mail: jose.millan@epfl.ch

In recent years, new research has brought the field of electroencephalogram (EEG)-based brain–computer interfacing (BCI) out of its infancy and into a phase of relative maturity through many demonstrated prototypes such as brain-controlled wheelchairs, keyboards, and computer games. With this proof-of-concept phase in the past, the time is now ripe to focus on the development of practical BCI technologies that can be brought out of the lab and into realworld applications. In particular, we focus on the prospect of improving the lives of countless disabled individuals through a combination of BCI technology with existing assistive technologies (AT). In pursuit of more practical BCIs for use outside of the lab, in this paper, we identify four application areas where disabled individuals could greatly benefit from advancements in BCI technology, namely, “Communication and Control”, “Motor Substitution”, “Entertainment”, and “Motor Recovery”. We review the current state of the art and possible future developments, while discussing the main research issues in these four areas. In particular, we expect the most progress in the development of technologies such as hybrid BCI architectures, user–machine adaptation algorithms, the exploitation of users’ mental states for BCI reliability and confidence measures, the incorporation of principles in human–computer interaction (HCI) to improve BCI usability, and the development of novel BCI technology including better EEG devices.

Keywords: assistive technology, BCI, communication and control, entertainment, motor recovery, motor substitution

## IntroductIon

Imagine being able to control a robot or other machine using only your thoughts – this fanciful notion has long since captured the imagination of humankind, and, within the past decade, the ability to actually bypass conventional channels of communication (i.e., muscles or speech) between a user’s brain and a computer has become a demonstrated reality. Known as brain–computer interfaces (BCIs), the field has already seen several early prototypes (Nicolelis, 2001; Millán, 2002; Wolpaw et al., 2002; Wickelgren, 2003; Allison et al., 2007; Dornhege et al., 2007). A BCI monitors the user’s brain activity and translates their intentions into commands without activating any muscle or peripheral nerve. BCI as a proof-of-concept has already been demonstrated in several contexts; driving a robot or wheelchair (Millán et al., 2004a,b, 2009), operating prosthetic devices (Müller-Putz et al., 2005, 2006; Pfurtscheller et al., 2000, 2003), selecting letters from a virtual keyboard (Birbaumer et al., 1999; Donchin et al., 2000; Millán, 2003; Obermaier et al., 2003; Millán et al., 2004a; Scherer et al., 2004; Müller and Blankertz, 2006; Sellers et al., 2006; Williamson et al., 2009), internet browsing (Karim et al., 2006; Bensch et al., 2007; Mugler et al., 2008), navigating in virtual realities (Bayliss,

- 2003; Leeb et al., 2007a,b), and playing games (Millán, 2003; Krepki et al., 2007; Nijholt et al., 2008b; Tangermann et al., 2008).

Such a kind of BCI is a natural way to augment human capabilities by providing a new interaction link with the outside world and is particularly relevant as an aid for disabled people. The central tenet of a BCI is the capability to distinguish different patterns of brain activity, each being associated to a particular intention or mental task. Hence adaptation is a key component of a BCI because users must learn to modulate their brainwaves so as to generate distinct brain patterns. In some cases, user training is complemented with machine learning techniques to discover the individual brain patterns characterizing the mental tasks executed by the user.

With the field now entering a more mature phase of development, the time is ripe to focus on the development of practical BCI applications aimed at improving the lives of physically disabled individuals1. Furthermore, if our goal is to offer solutions to

1That is, people with different degrees of stabilized motor disability as a consequence of traumatic lesions (spinal cord injury), cerebrovascular diseases (stroke), or degenerative neuromuscular diseases (muscular dystrophies and motor neuron disorders such as amyotrophic lateral sclerosis and spinal muscular atrophies) that are characterized by a progressive loss of muscular activity. In all these cases, however, cognitive functions are spared to a large, if not complete, extent.

these people, and to augment their capabilities, then BCIs must be combined with existing assistive technologies (AT), especially those they already utilize.

Most BCIs for human subjects rely on non-invasive electroencephalogram (EEG) signals; i.e., the electrical brain activity recorded from electrodes placed on the scalp. The reason is that EEG is a practical modality if we want to bring BCI technology to a large population2. For this reason, in this review, we focus on EEG-based BCIs and how to combine them with AT. We also identify and review some principles and research challenges that we consider fundamental to bring BCI technology out of the lab. These principles include the development of hybrid BCI (hBCI) architectures, the design of user–machine adaptation algorithms, the exploitation of users’ mental states for BCI reliability and confidence measures, the incorporation of principles in human–computer interaction (HCI) to improve BCI usability, and the development of novel BCI technology including better EEG devices. Note, however, that most of the principles we put forward here can also be applied to other types of BCI, either invasive (single-unit activity, Carmena et al., 2003; Hochberg et al., 2006; electrocorticogram, Leuthardt et al., 2004; Pistohl et al., 2008) or non-invasive (MEG, Kauhanen et al., 2006; Mellinger et al., 2007; fMRI, Weiskopf et al.,

- 2004; Yoo et al., 2004; NIRS,Coyle et al., 2007; Sitaram et al., 2007). In this paper, we identify four application areas where BCI

assistive technology can have a real, measurable impact for people with motor disabilities; namely “Communication and Control”, “Motor Substitution”, “Entertainment”, and “Motor Recovery”. The remainder of the paper is organized as follows. The rest of this section is devoted to the research challenges currently faced by BCI-based assistive technology. Then, in Sections “Communication and Control”, “Motor Substitution”, “Entertainment”, and “Motor Recovery”, each application area is discussed, and the current stateof-the-art of each is reviewed. Finally, in Section “Summary”, we summarize the main message of this review paper.

HybrId bcI

What kind of assistance can BCI actually offer to disabled persons? Despite progress in AT, there is still a large number of people with severe motor disabilities who cannot fully benefit from AT due to their limited access to current assistive products (APs). For them, BCI is the solution. However, notwithstanding the impressive demonstrations of BCI technology around the world, today’s state-ofthe-art is such that BCI alone cannot make patients interact with and control assistive devices over long periods of time and without expert assistance. But this doesn’t mean that there is no place for BCI. The solution is to use BCI as an additional channel. Such a hybrid approach, where conventional APs (operated using some residual muscular functionality) are enhanced by BCI technology, leads to what we call hybrid BCI (hBCI).

2Besides electrical activity, neural activity also produces other types of signals, such as magnetic and metabolic, that can be also measured non-invasively. Magnetic fields can be recorded with magnetoencephalography (MEG), while brain metabolic activity – reflected in changes in blood flow – can be observed with positron emission tomography (PET), functional magnetic resonance imaging (fMRI), and optical imaging (NIRS). Unfortunately, such alternative techniques require sophisticated equipment that can be operated only in special facilities. Moreover, techniques for measuring blood flow have long latencies and thus are less appropriate for interaction.

As a general definition, a hBCI is a combination of different signals including at least one BCI channel. Thus, it could be a combination of two BCI channels but, more importantly, also a combination of BCI and other biosignals [such as electromyographic (EMG), etc.] or special AT input devices (e.g., joysticks, switches, etc.). The control channels (BCI and other modalities) can operate different parts of the assistive device or all of them could be combined to allow users to smoothly switch from one control channel to the other depending on their preference and performance. An example of the former case is a neuroprostheses that uses residual movements for reaching objects and BCI for grasping. In the latter case, a muscular dystrophy patient may prefer to speak in the morning and switch to BCI in the afternoon when fatigue prevents him from being able to speak intelligibly. Moreover, in the case of progressive loss of muscular activity [as in muscular dystrophy, amyotrophic lateral sclerosis (ALS), and spinal muscular atrophies] early BCI training while the user can still exploit her/his residual motor functions will increase long-term use of APs by smoothing the transition between the hybrid assistive device and pure BCI when muscular activity is too weak to operate the APs.

An effective way for a hBCI to combine all the control channels is to merge their individual decisions – i.e., the estimation of the user’s intent – by weighting the contribution of each modality. These weights reflect the reliability of the channel, or confidence/certainty the system has regarding its output. The weights can be estimated from supervision signals such as mental states [e.g., fatigue, error potentials (ErrPs)] and physiological parameters (e.g., muscular fatigue). Another source to derive the weights is to analyze the performance of the individual channels in achieving the task at hand (e.g., stability over time).

There exist a few examples of hybrid BCIs. Some are based on multiple brain signals. One of such hBCIs is the combination of motor imagery (MI)-based BCI with ErrP detection and correction of false mental commands (Ferrez and Millán, 2008b). A second example is the combination of MI with steady state visual evoked potentials (SSVEPs) explored in some offline studies (Allison et al., 2010; Brunner et al., 2010). Other hBCIs combine brain and other biosignals. For instance,Scherer et al. (2007b) combined a standard SSVEP BCI with an on/off switch controlled by heart rate variation. Here the focus is to give users the ability to use the BCI only when they want or need to use it. Alternatively, and following the idea of enhancing people’s residual capabilities with a BCI,Leeb et al. (2010b) fused EMG with EEG activity, so that the subjects could achieve a good control of their hBCI independently of their level of muscular fatigue. Finally, EEG signals could be combined with eye gaze (Danoczy et al., 2008).Pfurtscheller et al. (2010) have recently reviewed preliminary attempts, and feasibility studies, to develop hBCIs combining multiple brain signals alone or with other biosignals. Finally, hybrid BCIs could exploit several brain imaging techniques simultaneously; i.e., EEG together with MEG, fMRI, NIRS, and even TMS. As mentioned above, our focus in this review paper is on principles to develop hBCI that, when coupled with existing AT used by disabled people, can effectively improve their quality of life.

AdAptAtIon

The kind of switch mentioned above offers a first level of selfadaptation, in that the user can dynamically choose the best interaction channel at any time. To the best of our knowledge, this is a

aspect of BCI that has not been addressed before. A second level of self-adaptation concerns the choice of the EEG phenomena that each user better controls, which can range from evoked potentials like P300 (Farwell and Donchin, 1988; Nijboer et al., 2008) or SSVEP (Sutter, 1992; Gao et al., 2003; Brunner et al., 2010) to spontaneous signals like slow cortical potentials (Birbaumer et al., 1999) and rhythmic activity (Babiloni et al., 2000; Wolpaw et al.,

- 2000; Pfurtscheller and Neuper, 2001; Millán et al., 2002; Blankertz

- et al., 2007). This necessitates the development of novel training protocols to determine the optimal EEG phenomenon for each user, building upon work on psychological factors in BCI (Neumann and Kübler, 2003; Nijboer et al., 2007).

Still another aspect of self-adaptation is the need for online calibration of the decoding module (which translates EEG activity into external actions) to cope with the inherent non-stationarity of EEG signals. Recently, a number of papers have studied how EEG signals change during BCI sessions (Shenoy et al., 2006; Sugiyama et al., 2007; Vidaurre et al., 2008; von Bünau et al., 2009). This non-stationarity can be addressed in three different ways. First, by rejecting the variation of the signals and retaining the stationary part as in Kawanabe et al. (2009) and von Bünau et al. (2009). In these works, different methods to design robust BCI systems against non-stationarities are described. Second, by choosing features from the EEG that carry discriminative information and, more importantly, that are stable over time (Galán et al., 2007, 2008). Third, by applying adaptation techniques. This adaptation can, as well, be carried out at different modules of the BCI: in the feature extraction (for example with the use of adaptive autoregressive coefficients or time domain parameters, Schlögl, 2000; Vidaurre et al., 2009) in the spatial filtering (Zhang et al., 2007; Vidaurre and Blankertz, 2010) or at the classifier side. Adaptation of any of the modules can be done in a supervised way (when the task to perform is known beforehand) or in an unsupervised manner (no class labels are used to adapt the system). Although not very common, supervised adaptation of the classifier has been explored in several studies (Millán, 2004; Buttfield et al., 2006; Shenoy et al., 2006; Vidaurre et al., 2006; Millán et al., 2007). Recently, some groups have also performed unsupervised adaptation of the features (Schlögl, 2000; Vidaurre et al., 2009) and of the classifier. Unsupervised classifier adaptation has also been applied to P300 data (Lu et al., 2009) and to MI data (Blumberg et al., 2007; Sugiyama et al., 2007; Vidaurre

- et al., 2008). Regardless whether adaptivity is applied in one or more modules

of the BCI, it allows the simultaneous co-adaptation of the BCI to the user and vice versa. A recent study with healthy volunteers (Vidaurre and Blankertz, 2010) who either had no experience or had not been able to control a BCI with sufficient level of control for a communication application (70% of accuracy in a two class system) has shown the advantage of this approach. During the BCI session, of approximately 2 h, some users could develop SMR. This is a big step forward in BCI research, because at least 25–30% of all users are not able to use a BCI with sufficient level of control (Guger et al., 2003). We hypothesize that selection of stable discriminant features and BCI adaptation could facilitate and accelerate subject training. Indeed, these techniques increase the likelihood of providing stable feedback to the user, a necessary condition for people to learn to modulate their brain activity.

HumAn–computer InterActIon

A related issue is how to improve the performance and reliability of current BCIs, which are characterized by noisy and low-bit-rate outputs. A promising possibility is the use of modern HCI principles to explicitly take into account the noisy and lagged nature of the BCI control signals to adjust the dynamics of the interaction as a function of the reliability of user’s control capabilities. Such a HCI approach can also include the ability to “degrade gracefully” as the inputs become increasingly noisy (Williamson, 2006).

Human–computer interaction principles can lead to a new generation of BCI assistive devices by designing more suitable and comfortable interfaces that will speed up interaction, as demonstrated by the recent virtual keyboard “Hex-O-Spell” (Müller and Blankertz, 2006; Williamson et al., 2009). Regarding interaction and control of complex devices like neuroprostheses and mobile robots (or wheelchairs), it has recently been shown how shared autonomy techniques can drastically enhance the performance and robustness of a brain-controlled wheelchair (Vanacker et al., 2007; Galán et al., 2008; Millán et al., 2009). In a shared autonomy framework, the outputs of the BCI are combined with the information about the environment (obstacles perceived by the robot sensors) and the robot itself (position and velocities) to better estimate the user’s intent. Some broader issues in human–machine interaction are discussed in Flemisch et al. (2003), where the H-Metaphor is introduced, suggesting that interaction should be more like riding a horse, with notions of “loosening the reins”, allowing the system more autonomy.

Shared autonomy (or shared control) is a key component of future hybrid BCI as it will shape the closed-loop dynamics between the user and the brain-actuated device such that tasks are able to be performed as easily as possible. As mentioned above, the idea is to integrate the user’s mental commands with the contextual information gathered by the intelligent brain-actuated device so as to help the user to reach the target or override the mental commands in critical situations. In other words, the actual commands sent to the device and the feedback to the user will adapt to the context and inferred goals. In such a way, shared control can make target-oriented control easier, can inhibit pointless mental commands, and can help determine meaningful motion sequences (e.g., for a neuroprostheses). Examples of shared control applications are neuroprostheses such as robots and wheelchairs (Millán et al., 2004b, 2009; Vanacker et al., 2007; Galán et al., 2008; Tonin et al., 2010), as well as smart virtual keyboards (Müller and Blankertz, 2006; Wills and MacKay, 2006; Williamson et al., 2009), and other AT software with predictive capabilities.

The issue of improving the user interface is not a new problem; in addition some of the issues such as error rate and time taken to make a selection are not new in the general area of AT. The emphasis has mainly been on improving controllability and accuracy. Applications designed for BCI should be able to use different methods of BCI control, account for individual differences, optimize the user interface and incorporate artificial intelligence techniques. Simulation techniques can provide helpful information about the expected usability of a system. For instance, Biswas and Robinson (2007) describes a simulator which incorporates models of the application, interface and user to predict the performance of assistive technology devices.

Finally, until fairly recently, the focus of software design and evaluation has been on usability and functionality in what are referred to as instrumental qualities. Current trends emphasize non-instrumental aspects of interface design and evaluation. These can be separated into the three categories; hedonics (concerned with [un]pleasant sensations), esthetics, and pleasure/fun (Mahlke, 2005). This development might be seen as attempting to establish the basics first before fine-tuning the details later. Nevertheless, Tractinsky et al. (2000) demonstrates that the perception of how usable a system is increases as visual esthetics of the system increases, although its actual usability remains unchanged. A valid question to ask, then, is whether BCI application design and evaluation can and should follow the same pattern of developing usable systems first before “targeting” the non-instrumental qualities. Given the current limitations of BCIs, how much of the existing knowledge of HCI design and evaluation can be applied to BCIs? It depends on the purpose of the application and how much control is required for the application to be used. Computer applications for BCI might be divided into three broad categories – programs for communication, tools for functional control, and entertainment applications. Entertainment programs can further be subdivided into games, tools for creativity and interactive media. The focus of evaluation for communication and functional applications should be on usability and functionality, while the focus of entertainment applications should be on pleasure and entertainment.

mentAl stAtes

A fourth area where BCI assistive technology can benefit from recent research is in the recognition of the user’s mental states (mental workload, stress level, tiredness, attention level) and cognitive processes (awareness to errors made by the BCI), which could facilitate interaction and reduce the user’s cognitive effort by making the BCI assistive device react to the user. This is again another aspect of self-adaptation: for instance, in case of high mental workload or stress level, the dynamics and complexity of the interaction will be simplified or it will trigger the switch to stop brain interaction and move on to muscle-based interaction (see above). As another example, in the case of detection of excessive fatigue, the mobile robot would take over complete control and move autonomously to its base station close to the user’s bed. Pioneering work in this area deals with the recognition of mental states (such as mental workload,Kohlmorgen et al., 2007; attention levels, Hamadicharef et al., 2009; and fatigue, Trejo et al., 2005) and cognitive processes (such as error-related potentials,Blankertz et al., 2003; Ferrez and Millán, 2005, 2008a,b; and anticipation, Gangadhar et al., 2009) from EEG. In the latter case, Ferrez and Millán (2008a,b) have shown that errors made by the BCI can be reliably recognized and corrected, thus yielding significant improvements in performance.

Also, as mentioned before, mental states can provide useful information to estimate the reliability of the individual channels. For instance, in the case of a high attention level, we could assign a large weight to the EEG channel, while this weight would be small in the case of high mental workload. Also, repetitive error-related potentials should reduce the weight of the channels that mainly contributed to the estimation of the user’s intent.

new eeG devIces

The fifth and final area of necessary progress surrounds the development of a new class of BCI devices based on easy-to-use and esthetic EEG equipment. So far, laboratory experimentation has never required attention to issues like portability, esthetic design, conformity, certification, etc. Many current BCI applications exist in the form of software running on a personal computer; but many users will not accept the burden of a desktop PC and its screen to utilize a BCI. In addition, there is a need for a common implementation architecture to facilitate commercial take-up – and the field is taking steps toward standardization in the design of BCI (Cincotti et al., 2010). The merger of esthetic and engineering design is a key issue that any practical BCI for disabled people must overcome. Users don’t want to look unusual– therefore, social acceptability is a key concern for them3. For this reason we expect new EEG technology based on dry electrodes and esthetic wireless helmets. Different teams have recently developed some prototypes of dry electrodes that overcome the need of gel, one of the main limitations of current EEG technology (Popescu et al., 2007). Moreover, different companies like Quasar Inc. (San Diego, USA) (Sellers et al., 2009), Emotiv Systems Inc. (San Francisco, USA), NeuroSky Inc. (San Jose, USA) (Sullivan et al., 2008), and Starlab (Barcelona, Spain) (Ruffini et al., 2007) are now commercializing dry electrodes, mainly for gaming. Although some doubts exist about the kind of physiological signals these systems actually exploit for control, they are definitely pushing the field forward.

dIscussIon

In summary, time is ripe to develop a new generation of hybrid BCI assistive technology for people with physical disabilities that will advance the state of the art in a number of ways:

- • Conventional AP will be enhanced by BCI technology: the incorporation of a brain channel can provide an additional degree of freedom, enhance the robustness of the control signals by combining EEG and other AT, or be the only means of interaction. BCI will expand the range of opportunities available to AT teams worldwide for building flexible and personalized solutions for their clients needs.
- • BCI assistive devices will be endowed with novel self-adaptive capabilities: this will be achieved through the incorporation of fusion techniques for combining EEG with other signals, automatic choice of EEG phenomena, online adaptation to changing EEG signals, the use of modern HCI principles for shaping the interaction, and recognition of user’s mental states and cognitive processes.
- • Brain–computer interaction will become more robust: combination of EEG with other signals allow users to become more autonomous and interact over long periods of time.
- • Brain–computer interaction will increase its performance and reliability significantly: the use of modern HCI and shared autonomy principles will make it possible.
- • Brain–computer interaction will reduce user’s cognitive effort: this will be possible because of the use of modern HCI as well as the recognition of user’s mental states and cognitive processes.

3Clearly, all these issues (from standardization to esthetics) are relevant to any kind of BCI, regardless of the kind of brain signal in use.

- • Brain–computer interaction will be easier: the design of efficient training protocols will accelerate, improve and make more intuitive user’s mastering of the BCI assistive technology; also, the development of new electrodes and esthetic helmets will facilitate operation of BCI by laypeople.
- • Novel BCI designs will ensure the outcome follows standard BCI assistive technology: past lack of coordination in BCI research has thus far impeded the creation of a shared model and standards among BCI groups.

## communIcAtIon And control

Brain–computer interfaces have the potential to enable severely disabled individuals to communicate with other people and to control their environment. Communication functions consist mainly of sending/receiving emails, chatting, using VoIP phones and surfing the web. During the last 10 years, it has been proven in the labs that persons, even those suffering of severe disabilities, may interact with computers by only using their brain – in the extreme case using the brain channel as a single switch, just like a computer mouse.

There is also a commercial system that, in principle, allows BCI communication and control. Brain Actuated Technologies introduced “Cyberlink” in 1996, a system that records electrical signals from three electrodes integrated into a headband on the subject’s forehead (Junker et al., 2002). Because of the location of the electrodes, users mainly use subtle facial muscles activity and eye movement for control, although the electrodes can also measure brain activity in the usual theta, alpha, and beta frequency bands. Recently OCZ Technology Inc. (San Jose, USA) acquired the company and is now commercializing the “Neural Impulse Actuator (NIA)”, the first consumer device that can be used for controlling standard video games without using mouse or joystick. OCZ is available since 2008 at a cost of about 300 USD.

bcI-drIven spellInG devIces

In 1999, the Tübingen BCI group developed the ThoughtTranslation-Device (TTD; Birbaumer et al., 1999), a system that could be operated by patients suffering from ALS through the modulation of brain rhythms. Binary decisions made by the BCI were used to select letters in a procedure where the alphabet was iteratively split into halves. The achieved spelling rate was about 0.5 char/min. Since then, other groups have developed BCI-driven spelling devices based on the detection of voluntarily patterns of activity in the spontaneous EEG. These systems can operate synchronously (Birbaumer et al., 1999; Obermaier et al., 2003) or asynchronously (Millán, 2003; Millán et al., 2004a; Scherer et al., 2004; Müller and Blankertz, 2006; Williamson et al., 2009). Interestingly, one patient suffering from severe cerebral palsy could operate the Graz system at about 1 char/min. In the case of Millán’s approach, trained subjects have taken 22.0 s on average to select a letter, including recovery from errors, with peak performances of 7.0 s per letter. Particularly relevant is the spelling system developed by the Berlin group in cooperation with the University of Glasgow, called Hex-o-Spell (Williamson et al., 2009), which illustrates how a normal BCI can be significantly improved by state-of-the-art HCI principles. The idea for Hex-o-Spell was taken from the Hex system which was designed for use on mobile devices augmented with

accelerometers, where tilt control was used to maneuver through a hexagonal tessellation. The text entry system is controlled by the two mental states imagined right hand movement and imagined right foot movement. Expert subjects achieved typing speed of up to 7.5 char/min. A recent development in the field of HCI, inspired by a similar approach to Hex, is the Nomon selection system, based on the use of phase angle in clock-like displays (Broderick and MacKay, 2009). Still another speller designed upon efficient HCI principles is DASHER (Wills and MacKay, 2006).

Most BCI spelling devices, especially those actually used by disabled people, are based on the detection of potentials that are evoked by external stimuli rather than spontaneous mental states. The most prominent is the approach that elicits a P300 component (Donchin et al., 2000). In this approach, all characters are presented in a matrix, and the symbol which the user focuses her/his attention on can be predicted from the brain potentials that are evoked by random flashing of rows and columns. Similar P300-based spelling devices have since been extensively investigated and developed (e.g., Sellers et al., 2006; Nijboer et al., 2008; Silvoni et al., 2009).

bcI control of web browsers

The history of providing internet access to ALS patients dates back to 1999 when the TTD developed in Tübingen was used to operate a standard web browser. In a first implementation, called “Descartes” (Karim et al., 2006), the web window was shown for a certain amount of time (about 120 s), then a navigation screen would present the links from the current web page as leaves in a tree. A more advanced prototype, called “Nessi” (Bensch et al., 2007), allowed a more flexible selection of links thanks to a better user interface, again highlighting how BCI operation can be facilitated and improved by better HCI principles. More recently, this group has developed another browser based on P300 (Mugler et al., 2008). Theoretically, a browser with P300 control can enable selection from as many links as the elements in the P300 matrix (for a 6 × 6 matrix, 36), and the selection of a link could be completed in one step, although reliable recognition requires several iterations of the presentations of row/columns.

bcI And AssIstIve tecHnoloGy

Brain–computer interface technology can be seen as a special Assistive technology in the area of Information and Communication Technologies (AT ICT), which is defined the Class 22 of ISO 9999:2007 (APs for communication and information):

“AT ICT products are understood to be devices for helping a person to receive, send, produce and/or process information in different forms. Included are, e.g., devices for seeing, hearing, reading, writing, telephoning, signalling and alarming, and information technology.”

A large variety of assistive technology is available today, providing the opportunity for nearly all people to access ICT. However, an individual with proper assistive technology has no guarantee of access. ICT products must be designed and created in ways that allow all users to access them, including those who need AT. It is for this reason that BCI must be combined with state-of-the-art AT ICT.

The standard user interface of a personal computer is powerful and flexible, but this flexibility is often a barrier to accessibility for many people with disabilities: many small icons, multiple open windows on a complex desktop, drag-and-drop, and so on.

This kind of interface makes using a PC difficult and confusing for many people, like people with physical disabilities or first time users such as elderly people. A common approach to assisting people in using ICT is to add some assistive technology on top of the standard interface, such as text-to-speech or screen magnifiers. This approach has provided considerable benefit to specific user groups, but it does not remove the main limitation of standard user interfaces. The solution is then to design simpler user interfaces from scratch whose interaction principles and graphical appearance is uniform across applications. One of the few commercial state-of-the-art AT ICT products is “QualiWORLD” by QualiLife Inc. (Paradiso-Lugano, Switzerland).

## motor substItutIon

GrAspInG

In Europe alone, an estimated number of 300,000 people are suffering from a spinal cord injury (SCI) with 11,000 new injuries per year (Wyndaele and Wyndaele, 2006). Forty percent of the total population of the SCI patients are tetraplegics. Loss of motor functions, especially grasping, leads to a life-long dependency on care-givers and to a dramatic decrease in quality of life (Anderson, 2004).

Beside SCI persons, other neurological patients also suffer from paralysis of the upper extremities and the related restrictions in terms of independence and life quality. In Germany, 60% of the 150,000 patients affected by a stroke for the first time survive the first year, one-third of them with a hemiplegia (Exner, 2004). In Germany, 10% of the annual 250,000 traumatic brain injury patients live with motor deficits at the upper extremities.

Today, if surgery is not an option, functional electrical stimulation (FES) is the only possibility for partially restoring lost motor functions (Hentz and Le Clercq, 2002). In this context, the term neuroprostheses is used to describe FES systems aiming at the restoration of a weak or lost grasping function of the hand. Some of these neuroprostheses are based on surface electrodes for external stimulation of muscles of the hand and forearm. Examples are the commercially available NESS-H200 System (Bioness Inc., Valencia, USA) (Ijzermann et al., 1996) and other more sophisticated research prototypes (Thorsen et al.,

- 2001; Mangold et al., 2005). The Freehand system (NeuroControl, Cleveland, USA), an implantable neuroprostheses, overcomes the limitations of surface stimulation electrodes concerning selectivity and reproducibility (Keith and Hoyen, 2002). All FES systems for grasp restoration have in common the fact that they can only be used by patients with preserved voluntary shoulder and elbow function, which is the case in patients with an injury of the spinal cord below C5. Only two groups have dealt with the problem of restitution of elbow and shoulder movement. Memberg et al. (2003) used an extended Freehand system, while Handa’s group (Kameyama et al., 1999) developed a system based on intramuscular electrodes. Both systems represent exclusive FES systems, which stimulate the appropriate muscle groups not only for dynamic movements but also for maintaining a static posture. Due to the weight of the upper limb and the non-physiologic synchronous activation of the paralyzed muscles through external electrical pulses, rapid muscle fatiguing occurs. An alternative is, as for the case of standing and walking neuroprosthesis, to use a combination of FES with a mechanical orthosis (Goldfarb

and Durfee, 1996; Kobetic et al., 2003). A passive, but lockable orthosis stabilizes the knee joint during the stance phase without the need for a continuous co-contraction of antagonistic muscle groups. For the restoration of an elbow function much less torque has to be generated and held, thus supporting the idea that a passive, lockable orthosis combined with a FES-system will be successful in restoration of upper limb function. Up to now such a system does not exist.

Current neuroprosthesis for the restoration of forearm function (hand, finger, and elbow) require the use of residual movements not directly related to the grasping process. Traditional APs like head, mouse, or control devices using tongue or eye movements have not been accepted by patients for control of neuroprosthesis, because these APs hinder their communication ability, which is most important to patients for participation in normal social activities, and the design is not esthetic. It is for this reason that recently some groups have started to explore BCI approaches in the case where no, or only minor, residual motor control is available. For a review see Müller-Putz et al. (2006).

Pioneering work by the groups in Heidelberg and Graz showed for the first time the feasibility of the combination of BCI and a FES-system with surface electrodes (Pfurtscheller et al., 2003). In this study the restoration of a lateral grasp was achieved in a spinal cord injured subject, who suffers from a complete motor paralysis with missing hand and finger function. The patient is able to trigger sequential grasp phases by the imagination of foot movements. After many years of training and use of his BCI, the patient is able to control the system even during conversation with other persons. The same groups did a short-term BCI training of another tetraplegic patient who was provided with a Freehand system in the year 2000. After 3 days of training the patient was able to control the grasp sequence of the implanted neuroprosthesis sufficiently (Müller-Putz et al., 2005). More recently, they introduced a new method for the control of the grasp and elbow function by a BCI (Müller-Putz et al., 2007). The idea is to use a low number of pulsewidth coded brain patterns to control sequentially more degrees of freedom. Millán’s group used the MI of hand movements to stimulate the same hand for a grasping and writing task (Tavella et al., 2010), so the subjects thought about moving the right arm and the system stimulated the right arm. Furthermore, they used an adaptable passive hand orthosis, which evenly synchronizes the grasping movements and applied forces on all fingers. This orthosis also avoids fatigue in long-term stimulation situations by locking the position of the fingers and switching the stimulation off (Leeb et al., 2010a).

It’s worth noting that Fetz’s group (Moritz et al., 2008) has recently described an invasive approach to brain-controlled orthosis conceptually similar to previous attempts based on non-invasive BCI mentioned above. In this experiment, a monkey, paralyzed via a nerve block, can regain control of its forearm by using FES and single cell recordings of the motor cortex. This brings us to an important underlying issue in the development of neuroprosthesis, namely the choice of the kind of mental task to use for control. In most work in non-invasive BCI, people use imagination of different limbs (right/ left hand, feet) to deliver different commands to the neuroprosthesis for, say, the right hand. However, it seems more natural to rely on the recognition of different imagined movements of the same limb the

neuroprosthesis controls. Initial evidence for such a possibility has been recently provided in an offline study where subjects imagined the execution of different wrist movements (Gu et al., 2009).

Finally, a BCI-controlled FES orthosis can be also relevant for motor recovery of the upper extremities in stroke patients. Despite the fact that there is no literature available on the use of such a type of device in this patient population, some studies on the topic of FES training have emerged recently. For example, Hara (2008) claims that user-driven electrical muscle stimulation – but not machine-paced electrical muscle stimulation – improves the motor function of the hemiparetic arm and hand. A new hybrid FES therapy comprising proportional EMG-controlled FES and motor point block for antagonist muscles have been applied with good results in an outpatient rehabilitation clinic for patients with stroke. Additionally, Hara et al. (2008) have shown that a daily task-oriented FES home therapy program can effectively improve wrist and finger extension and shoulder flexion. Furthermore, proprioceptive sensory feedback might play an important role in this kind of therapy. The results of the single-case study from Page et al. (2009) supports these promising results. Moreover, another recent single-case study supports the benefit of a combination of FES and BCI (Daly et al., 2009). However, this use of BCI plus FES in the field of motor recovery has to be investigated more extensively.

AssIstIve mobIlIty

A second area where BCI technology can support motor substitution is in assisting user’s mobility, either directly through braincontrolled wheelchairs (e.g., Millán et al., 2009) or by mentally driving a telepresence mobile robot – equipped with sensors for obstacle detection as well as with a camera and a screen – to join relatives and friends located elsewhere and participate in their activities (Tonin et al., 2010). Several commercial platforms already exist for allowing this kind of interaction: e.g., peoplebot (Mobile Robots Inc., Amherst, USA), iRobot (iRobot Corp., Bedford, USA), robotino (Festo AG, Dietikon, Switzerland).

Underlying all assistive mobility scenarios, there is the issue of shared autonomy. The crucial design question for a shared control system is: who – man, machine or both – gets control over the system, when, and to what extent? Several approaches have been developed, in particular for intelligent wheelchairs. A common aspect in all these approaches is the presence of different assistance modes. These modes can either be different levels of autonomy or different algorithms for different maneuvers. Based on these modes, existing approaches can be classified into two categories. Firstly, there are approaches where mode changes are triggered by a user’s action through the operation of an extra switch or button. Examples of smart wheelchairs of this category are SENARIO (Katevas et al., 1997), OMNI (Hoyer, 1995), MAid (Prassler et al., 2001), Wheelesley (Yanco, 1998), VAHM (Bourhis and Agostini, 1998), and SmartChair (Parikh et al., 2004). However, those explicit interventions can be difficult and tiring for the users. These users have problems operating a conventional interface, and adding buttons or functionality for mode selection makes this interface only more complex to operate and less user-friendly. Secondly, there are approaches with implicit mode changes where the shared control system automatically switches from one mode to another without

the need for a manual user intervention. The NavChair (Levine et al., 1999; Simpson and Levine, 1999) and the Bremen Autonomous Wheelchair (Röfer and Lankenau, 2000) are examples of this second category. The problem with all these approaches is, however, that the switching is hard-coded and independent of the individual user and his specific handicap. An extensive literature overview of intelligent wheelchair projects can also be found in Simpson (2005).

In the case of brain-controlled robots and wheelchairs, Millán’s group has lead the development of a shared autonomy approach in the framework of the European MAIA project that solves the two problems mentioned above. This approach estimates the user’s mental intent asynchronously and provides appropriate assistance for navigation of the wheelchair. This approach has shown to drastically improve BCI driving performance (Vanacker et al., 2007; Galán et al., 2008; Millán et al., 2009; Tonin et al., 2010). Despite that asynchronous spontaneous BCIs seem to be the most natural and suitable alternative, there are a few examples of evoked BCIs for the control of wheelchairs (Rebsamen et al., 2007; Iturrate et al., 2009). Both systems are based on P300, a potential evoked by an awaited infrequent stimulus. To evoke the P300, the system flashes the possible predefined target destinations several times in a random order. The subject’s choice is the stimulus that elicits the largest P300. Then, the intelligent wheelchair reaches the selected target autonomously. Once there, it stops and the subject can select another destination – a process that takes around 10 s. A similar P300 approach has been followed to control a humanoid robot (Bell et al., 2008).

## entertAInment

The area of entertainment has typically had a lower priority in BCI work, compared to more “functional” activities such as basic communication or control tasks. For the purposes of this survey, entertainment encompasses everything from video games, to interaction with collections of media to control of ambient features, such as wall displays, lighting, and music. In tasks such as music or images, the feedback from even a “wrong” selection is usually pleasant (assuming the user likes the music or images in their collection), and interaction techniques can be focused on more exploratory approaches to browsing collections. This is sometimes called hedonic interaction in distinction from utilitarian interaction, and it leads to a need for a more broad set of metrics for evaluation of user experience. In this context, a BCI will facilitate activities such as browsing digital photo collections or music collections, where the control might be at the level of specifying a mood or genre. Such systems might also provide opportunities for users to express their emotional state, or desires to a caregiver more rapidly and expressively than using written language.

As an example of this BCI approach to entertainment, very recent work has begun to gather experience with synchronous and asynchronous BCI “painting” applications which allow the user creative expression. Preliminary results indicate that the application provides pleasure to patients, healthy volunteers, and artists (Kübler et al., 2008; Halder et al., 2009).

GAmInG

Although gaming has not been the main focus of BCI research, there exist some prototypes that demonstrate the feasibility of games controlled by a BCI (Millán, 2003; Lalor et al., 2005; Krepki et al.,

2007; Nijholt et al., 2008b; Tangermann et al., 2008; Finke et al., 2009; Nijholt, 2009). Such BCI games could allow severely disabled persons to not only experience a little bit of entertainment, but to also to improve their quality of life, mainly through social interaction. For instance, Tangermann et al. (2008) shows evidence that real-time BCI control of a physical game machine is possible with little subject training. The gaming machine studied (a standard pinball machine) required only two classes for control with fast and precise reaction; predictive behavior and learning are mandatory. Games can be either competitive (requiring fast responses) or strategic (usually slower).

These BCI games are based on different BCI protocols, from spontaneous EEG (Millán, 2003; Krepki et al., 2007; Tangermann

- et al., 2008) to evoked EEG potentials (Lalor et al., 2005; Finke
- et al., 2009), where the user delivers (as usual for a BCI) mental commands to control some aspect of the game. Another alternative is to determine the user’s mental or affective state from their EEG and to use this information to adapt the dynamics of the game to the user’s affective state (Nijholt et al., 2008b). As stated in Nijholt et al. (2008a), “Measuring brain activity for gamers can be used so that the game environment (1) knows what a subject experiences and can adapt game and interface in order to keep the gamer “in the flow” of the game, and (2) allows the gamer to add brain control commands to the already available control commands for the game.” This perspective matches well that described in Williamson (2006) when discussing a general framework for interaction design.

It is usually assumed that, because of the huge yearly turnovers of the game industry, once BCI games reach the mass market, BCI technology would become so cheap that every disabled person would be able to afford it for functional interaction. Some support this view. For instance, commercial “BCI” sensors are coming into the mainstream gaming world (e.g., Emotiv and Neurosky). Also, as Nijholt (2009) points out: “There are also other reasons that make games, gamers and the game industry interesting. Gamers are early adaptors. They are quite happy to play with technology, to accept that strong efforts have to be made in order to get minimal advantage, and they are used to the fact that games have to be mastered by training, allowing them to go from one level to the next level and to get a higher ranking than their competitors”. However, we cannot take for granted that the kind of BCI technology (sensors and brain signals) that the game industry would eventually develop will automatically be appropriate for functional interaction. This is the case for current “BCI” game sensors that are limited in number and position over the users head (normally just over the forefront, where there is no hair).

One concern with the mass-produced BCI games is proper evaluation; namely, how to prove that the user’s brainwaves are the actual control signals driving the game. Of course, from a hybrid BCI perspective, gamers can (and must) also use other physiological signals and interaction modalities. The point, however, is to demonstrate that users have a sufficient degree of mental control for those aspects of the game that require so, as advertised. This issue also raises the question of how to evaluate games as a whole to ensure that they provide a valuable and enjoyable experience. In this respect, the Fun of Gaming (FUGA) project advocates a multidimensional evaluation using self-reports, behavioralobservations

and psychophysiological measures as each in itself is insufficient to get the full picture (IJsselsteijn et al., 2008). Much of the research in pleasure and satisfaction in entertainment focuses on gaming but some might be applied to entertainment in general. For example, “fun” in a game includes challenge, curiosity, fantasy, and Csikszentmihalyi’s theory of flow (level of engagement that one is completely absorbed in the current activity and enjoys it in itself without any need for future benefit), but these can also apply to interactive art and creativity (and by extension interactive media, Costello and Edmonds, 2007). Only such a kind of evaluation will prove beneficial for BCI games in general, and for disabled people in particular. Otherwise, BCI games will be just another “fast-food toy” that customers buy and stop using quickly, thus risking to seriously damage the credibility of the BCI field – such a blow that early in its development stage could cripple the field, by projecting a negative image to the public, other industrial sectors, and to funding agencies.

vIrtuAl reAlIty

Because BCI are a closed-loop systems, feedback is an important component. Various methods of providing feedback can inform the participant about success or failure of an intended act. Thus, feedback either supports reinforcement during the learning/training process or in controlling the application. In particular, the use of virtual reality (VR) has been proven to be an interesting and promising way to realize such feedback.

Several prototypes have enabled users to navigate in virtual scenes solely by means of their oscillatory cerebral activity, recorded on the scalp via EEG electrodes. Healthy participants were exploring virtual spaces (Leeb et al., 2007b,c; Scherer et al., 2008; Ron-Angevin et al., 2009), were manipulating virtual objects (Lecuyer et al., 2008), and a spinal-cord injured patient was controlling a wheelchair through a virtual street (Leeb et al., 2007a). Additionally, evoked potentials (P300, Bayliss, 2003; and SSVEPs,Lalor et al., 2005) have been used to control VR feedback as well. In these studies, BCI users who use immersive Virtual Environments (VEs) make fewer errors, report that BCIs are easier to learn and use, and state that they enjoy BCI use more (Leeb et al., 2006, 2007b; Ron-Angevin et al., 2009). These benefits may occur because VEs enhance vividness and mental effort, which may lead to more distinct brain patterns and improve pattern recognition performance. Nevertheless, VR technologies provide motivating, safe, and controlled conditions that enable improvement of BCI learning as well as the investigation of the brain responses and neural processes involved, meanwhile testing new virtual prototypes.

musIc browsInG

Since the introduction of mp3 compression technology and easyto-use mobile music players (such as Apple’s iPod player, and iTunes software), there has been an explosion in the use of computers for listening to music. For example, listeners can create “playlists” of their favorite tracks to listen to, burn tracks to CDs, or share with friends. In many cases, though, typical users find that this requires too much effort. Recently a lot of publicity has been given to the “Genius” feature on Apple’s widely used iTunes software, although a range of alternatives have been in existence for some

time (e.g., websites such as last.fm, pandora.com, www.spotify. com). Moodplayer is an application that lets you create playlists on the go based on your mood and the mood of songs in your music library, and which can be installed on iPhones or Nokia phones. This is a natural application area for BCI. Although no BCI music browser has been developed yet, some BCI for music composition (Miranda, 2006) do exist.

pHoto browsInG

Existing research has focused on determining what kinds of photographs people have, what tasks they perform with them (and what tasks they would like to perform but cannot), and what structure the collections have. In particular, Frohlich et al. (2002) and Kirk et al. (2006) examine how users utilize their personal digital photographs. Both noted the general lack of organization of digital photographs, and the use of very simple exploration techniques. Complex searching activities were not found to be of particular benefit to users when dealing with their personal archives.Rodden and Wood (2003) also examined digital photograph activities, observing a distinct lack of annotation activity and the utility of temporal structuring in exploration of photo archives. An individual picking up an interactive photo display often does not have a clear idea of what images he or she wishes to see. This partially explains why many sophisticated and powerful organization and query interfaces are not widely adopted. Few users know what they want to see before they begin; fewer still are able to distill those intents into meaningful queries across the attributes of images which the system observes. Photo journalists, archivists or other workers with very specific and well-defined needs may benefit from such interactions. This use case, however, is exceedingly rare among home users exploring personal photograph collections.

Although users may not have a definite idea of what images they would be interested in seeing, or are unable to communicate their preferences given the available metadata attributes, they may instead be able to iteratively refine selections to find images of interest. The presentation of a sample from a large set of images can stimulate memories; user can then follow paths through photo space by indicating that they would like to see more images “similar” to one or more of those displayed. Using rich similarity metrics is essential in obtaining effective navigation by this means. This style of interaction has much in common with Bates’ “berry picking” model of information retrieval (Bates, 1989). In this model, users wander through an information space, finding results and modifying their queries as they go. The final goal of the user adapts as they bounce through the results from each previous query. This approach is well-suited to develop BCI tools for photo browsing. The idea is to combine BCI with simple image search techniques. Users will mentally select pictures representing possible categories in their photo archives with a P300-based BCI, and image search techniques will provide similar pictures. In fact, there is some preliminary work that follow this P300 approach (Touyama, 2008). Also of interest is the use of rapid serial visual presentation (RSVP) paradigms for image triage (Gerson et al., 2006). In this approach, users watch many images presented a high rate (say, 4 Hz) and the presence of a P300 evoked potential indicates images of interest that are ranked on top of the final selection.

## motor recovery

Motor impairment after stroke is the major cause of permanent disability. Recovery of hand motor function is crucial in order to perform activities of daily living, but is often variable and incomplete (Duncan et al., 1992). Indeed, stroke rehabilitation efficacy is limited (de Pedro-Cuesta et al., 1992; Duncan, 1997) with 30 to 60% of patients unable to use their more affected arms functionally after discharge (Kwakkel et al., 1999; Lai et al., 2002). Currently, neuroscience-based rehabilitation seeks to stimulate spontaneous functional motor recovery by capitalizing on the inherent potential of the brain for plastic reorganization after stroke (Chollet et al., 1991; Netz et al., 1997; Platz et al., 2000; Feydy et al., 2002; Cramer, 2004; Dobkin, 2004; Ward and Cohen, 2004; Gerloff et al., 2006; Nudo, 2006).

In this regard, evidence from animal studies encourage the parallelism between plasticity mechanisms in the developing nervous system and those taking place in adult brain after stroke (Murphy and Corbett, 2009). On the other hand, understanding the effect of rehabilitative practices on brain plasticity has the potential to provide a neural substrate to underpin rehabilitation and hence, in developing novel rehabilitation strategies (Liepert et al., 2000).

Rehabilitative interventions aimed at functional motor recovery in stroke patients are based mainly on active movement training such as constraint-induced therapy and/or passive mobilization (Liepert et al., 2000; Schaechter, 2004; Wolf et al., 2006). Recent clinical trials have provided new insights into the methods to assist motor recovery after stroke (Dobkin, 2008; Langhorne et al., 2009; Subramanian et al., 2010). A recurrent theme is that interventions emphasizing intense active repetitive task-oriented movements are of high value in this regard. To promote the effects of training and practice, biomedical engineers, neuroscientists, and clinicians have started an intense joint collaboration over the past 10 years. This technological approach holds a promise for enhancing traditional post-stroke recovery in different ways: exercise in virtual environments could provide feedback to aid skills learning (Jack et al., 2001; Holden et al., 2005; Merians et al., 2006); robotic assistive devices with sensory feedback for repetitive practice could provide therapy for a long periods of time, in a consistent and measurable manner (Takahashi et al., 2008; Volpe et al., 2009); FES of muscles might enable movements not otherwise possible during the practice of tasks such as reaching to grasp an object (Alon et al., 2007). These are only a part of the increasing technological developments which have been recently applied in sample of stroke patients and showed the feasibility in providing a clear incremental reduction of motor impairments offering, therefore the opportunity to build a better outcome for patients.

These treatments are based on the ability of the patients to perform actions with the affected hand or arm and therefore, require residual motor ability. Many patients however, are prevented from training based on the above treatments due to having no residual hand motor functions. In case of moderate to severe motor deficits, MI represents an intriguing new “backdoor” approach to access the motor system and rehabilitation at all stages of stroke recovery (Sharma et al., 2006, 2009a,b; Page et al., 2007). MI can be defined as a dynamic state during which the representation of a specific motor action is internally rehearsed without any overt motor output, and that is governed by the principles of central and peripheral motor

control (Decety and Jeannerod, 1995; Berthoz, 1996; Jeannerod and Frak, 1999; Lotze and Halsband, 2006). This is likely the reason why mental practice using MI training results in motor performance improvements (for a review in athletes, see Feltz and Landers, 1983; Dickstein and Deutsch, 2007). In addition, MI training can independently improve motor performance and produce similar cortical plastic changes (Lotze and Halsband, 2006), providing a useful alternative when physical training is not possible.

Despite this evidence, imagery training of movements combined with conventional physiotherapy of the hand has been reported in few structured clinical trials including subacute to chronic stroke patients and they demonstrated a greater improvement of hand function with the additional mental practice (Braun et al., 2006; Page et al., 2007; Malouin et al., 2008; Simmons et al., 2008; Verbunt et al., 2008). Up to now, no definite conclusions can be drawn, except that further research using a clear definition of mental practice content and standard outcome measurements are needed. As for the first point, it follows from the definition of MI that because of its concealed nature, a subject may surreptitiously use alternative cognitive strategies that, if not screened for, could confound investigations and produce conflicting results. Because the aim of MI is to activate the motor networks, it is crucial that subjects perform the mental task from the first person perspective (so called kinesthetic MI), in contrast to third person perspective or visual imagery (Decety and Grezes, 1999; Neuper et al., 2005). In this regard, a recent fMRI study on MI (Guillot et al., 2008) has looked at this issue by assessing subjects’ imagery abilities using well-established psychological, chronometric, and new physiological measures from the autonomic nervous system. The results suggest that visual and kinesthetic imagery are mediated through separate neural systems, which contribute differently during processes of motor learning and neurological rehabilitation.

Beyond these overall considerations, the challenge neurorehabilitators are faced with is clear: to modulate the sensorimotor experience of stroke patients to induce specific form of plasticity to boost relearning processes. Pulling all previous evidence together, a promising and challenging approach is to deploy BCI technology as a tool to tackle the challenge in the field of functional motor recovery after stroke. Indeed, the inherent BCI training paradigms will be exploited as a behavioral, controlled strategy to recruit and/or reinforce patient’s sensorimotor experience (like MI and/or residual motor ability) during functional motor recovery after stroke and, thus to enhance those physiological plasticity phenomena which are the substrate for the functional motor recovery itself. The feasibility and effectiveness of a BCI-based neurofeedback paradigm will be enhanced by combining MI with motor action observation; this latter cognitive strategy will be allowed via technology such as visual representation and FES of the hand. Moreover, a multimodal brain imaging approach will provide detailed knowledge of how the brain encodes and processes information when it imagines the control or actually controls a peripheral device. This knowledge will, in turn, unravel to what extent long-term use of BCI “per se” affects the brain activity of the user.

The BCI community has a long-standing experience with one of the employed strategies for operating EEG-based BCI systems – the modulation of sensorimotor EEG reactivity induced by movement imagery tasks (Pfurtscheller et al., 1997; Neuper et al., 1999, 2006;

Cincotti et al., 2003; Kübler et al., 2005). This makes possible the development of flexible and affordable BCI tools to objectify and to monitor individual MI execution both in terms of performance (relation between subject MI performance and subject level of accuracy in controlling BCI-operated basic applications) and compliance (identification of a correct MI task which is needed to achieve BCI-system control).

Within the BCI community, the opportunity to use BCI protocols to promote recovery of motor function by encouraging and guiding plasticity phenomena occurring after stroke (or more generally after brain injury) is at a very preliminary stage (for review see Birbaumer et al., 2008; Daly and Wolpaw, 2008; Mak and Wolpaw, 2010). Discussion is currently underway over several factors including: the extent to which patients have detectable brain signals that can support training strategies; which brain signal features are best suited for use in restoring motor functions and how these features can be used most effectively; and what the most effective formats are for the BCIs aimed at improving motor functions (for instance, what guidance should be provided to the user to maximize training that produces beneficial changes in brain signals). So far, preliminary findings are promising: Scherer et al. (2007a) suggested that event-related EEG activity time-frequency maps of event-related EEG activity and their classification are proper tools to monitor MI related brain activity in stroke patients and to contribute to quantify the effectiveness of MI.Buch et al. (2008) have shown that six out of eight chronic stroke patients suffering from a handplegia learned to control a magnetoencephalography-based BCI by MI. In all these cases, the best signals were depicted over the ipsilateral (unaffected hemisphere). Other attempts to use non-invasive BCI for rehabilitation includeAng et al. (2009) andPrasad et al. (2009). Finally, the idea that BCI technology can induce neuroplasticity has received remarkable support from the community based on invasive detection of brain electrical signals (for recent review see Wang et al., 2010).

As mentioned above, a general consensus from the clinical point of view is still lacking on the content, dose, and strategy of the MI intervention in stroke rehabilitation. What’s more, there is no evidence so far, that one intervention protocol can be more effective with respect to another, for the mental practice of motor actions. According to the extensive review by Sharma et al. (2006) only few studies have paid attention to the previous issues and the conclusion can be summarized as follows: (i) MI training has to be provided in addition to a background rehabilitation therapy; (ii) MI tasks should be practiced in the patient’s functional context to be most effective; in this regard, the MI tasks can be chosen from activities of daily life (i.e., reaching for and grasping a cup or other objects, turning page in a book, proper use of writing tool) from the content of the occupational therapy (Page et al., 2007). A more recent approach suggests MI interventions to be tailored on specific individual possibilities, skills, and needs of the patient in accordance with evidence-based practice (Braun et al., 2008).

Finally, the measurement of the impact of new rehabilitative interventions on patient motor impairment is another issue of utmost importance. One valuable instrument which can offer a solid way to generalize results obtained from clinical/research trials, is represented by International Classification of Functioning (ICF). In a recent study, the effectiveness of a mentalpractice-basedtraining

on post-stroke rehabilitation has been evaluated by considering primary and secondary outcome measures according to the ICF domains (impairment; activity; participation and quality of life) (Verbunt et al., 2008).

## summAry

As shown in this review, recent progress in BCI seems to indicate that time is ripe for developing practical technology for brain– computer interaction; i.e., BCI prototypes combined with other AT that will have a real impact in improving the quality of life of disabled people. This is particularly the case for four application areas, namely “Communication and Control”, “Motor Substitution”,

“Entertainment”, and “Motor Recovery”. We expect further progress during the next years driven by new research and developments in key areas such as design of hybrid BCI architectures, conception of adaptation algorithms, exploitation of mental states, incorporation of HCI principles, and development of novel BCI technology and EEG devices.

## AcknowledGments

This work is supported by the European ICT Programme Project FP7-224631. This paper only reflects the authors’ views and funding agencies are not liable for any use that may be made of the information contained herein.

## references

Allison, B. Z., Brunner, C., Kaiser, V., Müller-Putz, G. R., Neuper, C., and Pfurtscheller, G. (2010). Toward a hybrid brain–computer interface based on imagined movement and visual attention. J. Neural Eng. 7, 26007. Allison, B. Z., Wolpaw, E. W., and Wolpaw, J. R. (2007). Brain–computer interface systems: progress and prospects.Expert Rev. Med. Devices 4, 463–474.

Alon, G., Levitt, A. F., and McCarthy, P. A. (2007). Functional electrical stimulation enhancement of upper extremity functional recovery during stroke rehabilitation: a pilot study. Neurorehabil. Neural Repair 21, 207–215.

Anderson. K. D. (2004). Targeting recovery: priorities of the spinal cord-injured population. J. Neurotrauma 21, 1371–1383.

Ang, K. K., Guan, C., Chua, K. S. G., Ang, B. T., Kuah, C., Wang, C., Phua, K. S., Chin, Z. Y., and Zhang, H. (2009). “A clinical study of motor imagerybased brain–computer interface for upper limb robotic rehabilitation,” in Proceedings of the 31st Annual International Conference of the IEEE Engineering in Medicine and Biology Society. Minneapolis, MN.

Babiloni, F., Cincotti, F., Lazzarini, L., Millán, J. d. R., Mouriño, J., Varsta, M., Heikkonen, J., Bianchi, L., and Marciani, M. G. (2000). Linear classification of low-resolution EEG patterns produced by imagined hand movements. IEEE Trans. Neural Syst. Rehabil. Eng. 8, 186–188.

Bates, M. J. (1989). The design of browsing and berrypicking techniques for the online search interface.Online Rev. 13, 407–424.

Bayliss, J. D. (2003). Use of the evoked potential P3 component for control in a virtual apartment. IEEE Trans. Neural Syst. Rehabil. Eng. 11, 113–116.

Bell, C. J., Shenoy, P., Chalodhorn, R., and Rao, R. P. N. (2008). Control of a humanoid robot by a noninvasive brain–computer interface in humans. J. Neural Eng. 5, 214–220.

Bensch, M., Karim, A. A., Mellinger, J., Hinterberger, T., Tangermann, M., Bogdan, M., Rosenstiel, W., and Birbaumer, N. (2007). Nessi: an EEGcontrolled web browser for severely paralyzed patients. Comput. Intell. Neurosci. 2007, 5, Article ID 71863. doi:10.1155/2007/71863.

Berthoz, A. (1996). The role of inhibition in the hierarchical gating of executed and imagined movements. Cogn. Brain Res. 3, 101–113.

Birbaumer, N., Ghanayim, N., Hinterberger, T., Iversen, I., Kotchoubey, B., Kübler, A., Perelmouter, J., Taub, E., and Flor, H. (1999). A spelling device for the paralysed. Nature 398, 297–298.

Birbaumer, N., Murguialday, A. R., and Cohen, L. (2008). Brain–computer interface in paralysis. Curr. Opin. Neurol. 21, 634–638.

Biswas, P., and Robinson, P. (2007). “Simulation to predict performance of assistive interfaces,” in Proceedings of the 9th International ACM SIGACCESS Conference on Computers and Accessibility, Tempe, AZ.

Blankertz, B., Dornhege, D., Krauledat, M., Müller, K.-R., and Curio, G. (2007). The non-invasive Berlin brain– computer interface: fast acquisition of effective performance in untrained subjects. Neuroimage 37, 539–550. Blankertz, B., Dornhege, G., Schäfer, C., Krepki, R., Kohlmorgen, J., Müller, K.-R., Kunzmann, V., Losch, F., and Curio, G. (2003). Boosting bit rates and error detection for the classification of fast-paced motor commands based on single-trial EEG analysis. IEEE Trans. Neural Syst. Rehabil. Eng. 11, 127–131.

Blumberg, J., Rickert, J., Waldert, S., Schulze-Bonhage, A., Aertsen, A., and Mehring, C. (2007). Adaptive classification for brain computer interfaces. in Proceedings of the 29th Annual International Conference of the IEEE Engineering Medicine and Biology Society, Lyon, 2536–2539.

Bourhis, G., and Agostini, Y. (1998). The Vahm robotized wheelchair: system

architecture and human–machine interaction. J. Intell. Robot. Syst. 22, 39–50.

Braun, S. M., Beurskens, A. J., Borm, P. J., Schack, T., and Wade, D. T. (2006). The effects of mental practice in stroke rehabilitation: a systematic review. Arch. Phys. Med. Rehabil. 87, 842–852.

Braun, S., Kleynen, M., Schols, J., Schack, T., Beurskens, A., and Wade, D. (2008). Using mental practice in stroke rehabilitation: a framework.Clin. Rehabil. 22, 579–591.

Broderick, T., and MacKay, D. J. C. (2009). Fast and flexible selection with a single switch. PLoS ONE 4, e7481. doi:10.1371/journal.pone.0007481.

Brunner, C., Allison, B. Z., Krusienski, D. J., Kaiser, V., Müller-Putz, G. R., Neuper, C., and Pfurtscheller, G. (2010). Improved signal processing approaches in an offline simulation of a hybrid brain–computer interface. J. Neurosci. Methods 188, 165–173.

Buch, E., Weber, C., Cohen, L. G., Braun, C., Dimyan, M. A., Ard, T., Mellinger, J., Caria, A., Soekadar, S., Fourkas, A., and Birbaumer, N. (2008). Think to move: a neuromagnetic brain– computer interface (BCI) system for chronic stroke. Stroke 39, 910–917. Buttfield, A., Ferrez, P. W., and Millán, J. d. R. (2006). Towards a robust BCI: error recognition and online learning. IEEE Trans. Neural Syst. Rehabil. Eng. 14, 164–168.

Carmena, J. M., Lebedev, M. A., Crist, R. E., O’Doherty, J. E., Santucci, D. M., Dimitrov, D. F., Patil, P. G., Henriquez, C. S., and Nicolelis, M. A. L. (2003). Learning to control a brain–machine interface for reaching and grasping by primates. PLoS Biol. 1, 193–208. doi:10.1371/journal.pbio.0000042. Chollet, F., DiPiero, V., Wise, R. J., Brooks, D. J., Dolan, R. J., and Frackowiak, R. S. (1991). The functional anatomy of motor recovery after stroke in humans: a study with positron emission tomography. Ann. Neurol. 29, 63–71.

Cincotti, F., Mattia, D., Babiloni, C., Carducci, F., Salinari, S., Bianchi,

L., Marciani, M. G., and Babiloni, F. (2003). The use of EEG modifications due to motor imagery for brain–computer interfaces. IEEE Trans. Neural Syst. Rehabil. Eng. 11, 131–133.

Cincotti, F., Schreuder, E. J. M., Bianchi, L., Breitwieser, C., Tavella, M., Leeb, R., Müller-Putz, G. R., Tangermann, M., Kübler, A., and Millán, J. d. R. (2010). “Fostering BCI interoperability,” in Proceedings of the 4th International BCI Meeting, Asilomar, CA, USA. Costello, B., and Edmonds, E. (2007). “A study in play, pleasure and interaction design,” inProceedings of the 2007 Conference on Designing Pleasurable Products and Interfaces, Helsinki, Finland.

Coyle, S. M., Ward, T. E., and Markham, C. M. (2007). Brain–computer interface using a simplified functional nearinfrared spectroscopy system.J. Neural Eng. 4, 219–226.

Cramer, S. C. (2004). Functional imaging in stroke recovery. Stroke 35, 2695–2698.

Daly, J., Cheng, R., Rogers, J., Litinas, K., Hrovat, K., and Dohring, M. (2009). Feasibility of a new application of noninvasive brain computer interface (BCI): a case study of training for recovery of volitional motor control after stroke. J. Neurol. Phys. Ther. 33, 203–211.

Daly, J. J., and Wolpaw, J. R. (2008). Brain–computer interfaces in neurological rehabilitation. Lancet Neurol. 7, 1032–1043.

Danoczy, M., Fazli, S., Grozea, C., Müller, K. R., and Popescu, F. (2008). “Brain2robot: a grasping robot arm controlled by gaze and asynchronous EEG BCI,” in Proceedings of the 4th International Brain–Computer Interface Workshop and Training Course, Graz, Austria.

Decety, J., and Grezes, J. (1999). Neural mechanisms subserving the perception of human actions. Trends Cogn. Sci. 3, 172–178.

Decety, J., and Jeannerod, M. (1995). Mentally simulated movements in

virtual reality: does Fitts’s law hold in motor imagery? Behav. Brain Res. 72, 127–134.

de Pedro-Cuesta, J., Widen-Holmqvist, L., and Bach-y-Rita, P. (1992). Evaluation of stroke rehabilitation by randomized controlled studies: a review. Acta Neurol. Scand. 86, 433–439.

Dickstein, R., and Deutsch, J. E. (2007). Motor imagery in physical therapist practice. Phys. Ther. 87, 942–953. Dobkin, B. H. (2004). Neurobiology of rehabilitation. Ann. N. Y. Acad. Sci. 1038, 148–170.

Dobkin, B. H. (2008). Training and exercise to drive poststroke recovery. Nat. Clin. Pract. Neurol. 4, 76–85.

Donchin, E., Spencer, K. M., and Wijesinghe, R. (2000). The mental prosthesis: assessing the speed of a P300-based brain–computer interface. IEEE Trans. Neural Syst. Rehabil. Eng. 8, 174–179.

Dornhege, G., Millán, J. d. R., Hinterberger, T., McFarland, D. J., and Müller, K. -R. (eds). (2007). Towards Brain– Computer Interfacing. Cambridge, MA: MIT Press.

Duncan, P. W. (1997). Synthesis of intervention trials to improve motor recovery following stroke. Top. Stroke Rehabil. 3, 1–20.

Duncan, P. W., Goldstein, L. B., Matchar, D., Divine, G. W., and Feussner, J. (1992). Measurement of motor recovery after stroke. Outcome assessment and sample size requirements. Stroke 23, 1084–1089.

Exner, G. (2004). Der Arbeitskreis “Querschnittlähmungen” des Hauptverbandes der gewerblichen Berufsgenossenschaften in Deutschland. Fakten-ZahlenPrognosen. Trauma Berufskrankheit 6, 147–150.

Farwell, L. A., and Donchin, E. (1988). Talking off the top of your head: toward a mental prosthesis utilizing event related brain potentials. Clin. Neurophysiol. 70, 510–523.

Feltz, D. L., and Landers, D. M. (1983). The effects of mental practice on motor skill learning and performance: a meta-analysis.J. Sport Psychol. 5, 25–57.

Ferrez, P. W., and Millán, J. d. R. (2005). “You are wrong! – automaticdetection of interaction errors from brain waves,” in Proceedings of the 19th International Joint Conference on Artificial Intelligence, Edinburgh.

Ferrez, P. W. and Millán, J. d. R. (2008a). Error-related EEG potentials generated during simulated brain–computer interaction. IEEE Trans. Biomed. Eng. 55, 923–929.

Ferrez, P. W., and Millán, J. d. R. (2008b). “Simultaneous real-time detection of motor imagery and error-related

potentials for improved BCI accuracy,” in Proceedings of the 4th International Brain–Computer Interface Workshop and Training Course, Graz, Austria. Feydy, A., Carlier, R., Roby-Brami, A., Bussel, B., Cazalis, F., Pierot, L., Burnod, Y., and Maier, M. A. (2002). Longitudinal study of motor recovery after stroke: recruitment and focusing of brain activation. Stroke 33, 1610–1617.

Finke, A., Lenhardt, A., and Ritter, H. (2009). The MindGame: a P300based brain–computer interface game. Neural Netw. 22, 1329–1333.

Flemisch, O., Adams, A., Conway, S. R., Goodrich, K. H., Palmer, M. T., and Schutte. P.C. (2003).The H-Metaphor as a Guideline for Vehicle Automation and Interaction. Technical Report NASA/TM–2003-212672. Hampton, VA: NASA.

Frohlich, D., Kuchinsky, A., Pering, C., Don, A., and Ariss, S. (2002). “Requirements for photoware,” in Proceedings of the 2002 ACM conference on Computer Supported Cooperative Work (CSCW02), New Orleans, LA, USA, 166–175.

Galán, F., Ferrez, P. W., Oliva, F., Guardia, J., and Millán, J. d. R. (2007). “Feature extraction for multiclass BCI using canonical variates analysis,” in Proceedings of the 2007 IEEE International Symposium on Intelligent Signal Processing. Alcalá de Henares.

Galán, F., Nuttin, M., Lew, E., Ferrez, P. W., Vanacker, G., Philips, J., and Millán, J. d. R. (2008). A brain-actuated wheelchair: asynchronous and noninvasive brain–computer interfaces for continuous control of robots.Clin. Neurophysiol. 119, 2159–2169.

Gangadhar, G., Chavarriaga, R., and Millán, J. d. R. (2009). Fast recognition of anticipation related potentials.IEEE Trans. Biomed. Eng. 56, 1257–1260.

Gao, X., Dingfeng, X., Cheng, M., and Gao, S. (2003). A BCI-based environmental controller for the motion-disabled. IEEE Trans. Neural Syst. Rehabil. Eng. 11, 137–140.

Gerloff, C., Braun, C., Staudt, M., Hegner, Y. L., Dichgans, J., and Krägeloh-Mann, I. (2006). Coherent corticomuscular oscillations originate from primary motor cortex: evidence from patients with early brain lesions. Hum. Brain Mapp. 27, 789–798.

Gerson, A. D., Parra, L. C., and Sajda, P. (2006). Cortically-coupled computer vision for rapid image search. IEEE Trans. Neural Syst. Rehabil. Eng. 14, 174–179.

Goldfarb, M., and Durfee, W. K. (1996). Design of a controlled-brake orthosis for FES-aided gait.IEEE Trans. Neural Syst. Rehabil. Eng. 4, 13–24.

Guger, C., Edlinger, G., Harkam, W., Niedermayer, I., and Pfurtscheller, G. (2003). How many people are able to operate an EEG-based brain–computer interface (BCI)? IEEE Trans. Neural Syst. Rehabil. Eng. 11, 145–147.

Guillot, A., Collet, C., Nguyen, V. A., Malouin, F., Richards, C., and Doyon, J. (2008). Brain activity during visual versus kinesthetic imagery: an fMRI study. Hum. Brain Mapp. 30, 2157–2172.

Gu, Y., Dremstrup, K., and Farina, D. (2009). Single-trial discrimination of type and speed of wrist movements from EEG recordings. Clin. Neurophysiol. 120, 1596–1600.

Halder, S., Furdea, A., Leeb, R., MüllerPutz, G., Hösle, A., and Kübler, A. (2009). “Implementation of SMR based brain painting,” in Poster at COST Neuromath Workshop. Leuven, Belgium.

Hamadicharef, B., Zhang, H. H., Guan, C. T., Wang, C. C., Phua, K. S., Tee, K. P., and Ang, K.K. (2009). “Learning EEG-based spectral-spatial patterns for attention level measurement,” in Proceedings of the 2009 IEEE International Symposium on Circuits and Systems (ISCAS2009), Taipei. Hara, Y. (2008). Neurorehabilitation with new functional electrical stimulation for hemiparetic upper extremity in stroke patients. J. Nippon Med. Sch. 75, 4–14.

Hara, Y., Ogawa, S., Tsujiuchi, K., and Muraoka, Y. (2008). A home-based rehabilitation program for the hemiplegic upper extremity by power-assisted functional electrical stimulation. Disabil. Rehabil. 30, 296–304.

Hentz, V., and Le Clercq, C. (eds). (2002). Surgical Rehabilitation of the Upper Limb in Tetraplegia. Philadelphia, PA: W. B. Saunders Ltd.

Hochberg, L. R., Serruya, M. D., Friehs, G. M., Mukand, J. A., Saleh, M., Caplan, A. H., Branner, A., Chen, D., Penn, R. D., and Donoghue, J. P. (2006). Neuronal ensemble control of prosthetic devices by a human with tetraplegia. Nature 442, 164–171.

Holden, M. K., Dyar, T. A., Schwamm, L., and Bizzi, E. (2005). Virtualenvironment-based telerehabilitation in patients with stroke. Presence Teleoper. Virtual Environ. 14, 214–233.

Hoyer, H. (1995). The OMNI wheelchair. Serv. Robot. Int. J. 1, 26–29.

IJsselsteijn, W., van den Hoogen, W., Klimmt, C., de Kort, Y., Lindley, C., Mathiak, K., Poels, K., Ravaja, N., Turpeinen, M., and Vorderer, P. (2008). “Measuring the experience of digital game enjoyment,” in Proceedings of Measuring Behavior, Maastricht, The Netherlands, 88–89.

Ijzermann, M. J., Stoffers, T. S., Klatte, M. A., Snoeck, G., Vorsteveld, J. H., and Nathan, R. H. (1996). The NESS handmaster orthosis: restoration of hand function in C5 and stroke patients by means of electrical stimulation. J. Rehabil. Sci. 9, 86–89.

Iturrate, I., Antelis, J., and Minguez, J. (2009). “Synchronous EEG brainactuated wheelchair with automated navigation,” in Proceedings of the 2009 IEEE International Conference on Robotics and Automation, Kobe.

Jack, D., Boian, R., Merians, A. S., Tremaine, M., Burdea, G. C., Adamovich, S. V., Recce, M., and Poizner, H. (2001). Virtual reality-enhanced stroke rehabilitation. IEEE Trans. Neural Syst. Rehabil. Eng. 9, 308–318.

Jeannerod, M., and Frak, V. (1999). Mental imaging of motor activity in humans. Curr. Opin. Neurobiol. 9, 735–739. Junker, A. M., Wegner, J. R., and Sudkamp, T. (2002). “Cyberlink brainfingers for people with no means of access, NIH study results,” inProceedings of the 17th Annual International Conference on Technology & Persons with Disabilities, Los Angeles, CA, USA.

Kameyama, J., Handa, Y., Hoshimiya, N., and Sakurai, M. (1999). Restoration of shoulder movement in quadriplegic and hemiplegic patients by functional electrical stimulation using percutaneous multiple electrodes.Tohoku J. Exp. Med. 187, 329–337.

Karim, A. A., Hinterberger, T., Richter, J., Mellinger, J., Neumann, N., Flor, H., Kübler, A., and Birbaumer, N. (2006). Neural internet: web surfing with brain potentials for the completely paralyzed.Neurorehabil. Neural Repair 20, 508–515.

Katevas, N. I., Sgouros, N. M., Tzafestas, S. G., Papakonstantinou, G., Beattie, P., Bishop, J. M., Tsanakas, P., and Koutsouris, D. (1997). The autonomous mobile robot SENARIO: a sensor aided intelligent navigation system for powered wheelchairs.IEEE Robot. Autom. Mag. 4, 60–70.

Kauhanen, L., Nykopp, T., and Sams, M. (2006). Classification of single MEG trials related to left and right index finger movements.Clin. Neurophysiol. 117, 430–439.

Kawanabe, M., Vidaurre, C., Schöller, S., Blankertz, B., and Müller, K.-R. (2009). “Robust common spatial filters with a maxmin approach,” in Proceedings of the 31st Annual International Conference of the IEEE Engineering in Medicine and Biology Society, Minneapolis, MN, 2470–2473.

Keith, M. W., and Hoyen, H. (2002). Indications and future directions for upper limb neuroprostheses in tetraplegic patients: a review. Hand Clin. 18, 519–528.

Kirk, D., Sellen, A., Rother, C., and Wood, K. (2006). “Understanding photowork,” in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI ’06), Montréal, 761–770.

Kobetic, R., Marsolais, E. B., Triolo, R. J., Davy, D. T., Gaudio, R., and Tashman, S. (2003). Development of a hybrid gait orthosis: a case report. J. Spinal Cord Med. 26, 254–258.

Kohlmorgen, J., Dornhege, G., Braun, M., Blankertz, B., Müller, K.-R., Curio, G., Hagemann, K., Bruns, A., Schrauf, M., and Kincses, W. (2007). “Improving human performance in a real operating environment through realtime mental workload detection,” in Toward Brain–Computer Interfacing, eds G. Dornhege, J. d. R. Millán, T. Hinterberger, D. McFarland, and K.-R. Müller (Cambridge, MA: MIT press), 409–422.

Krepki, R., Blankertz, B., Curio, G., and Müller, K.-R. (2007). The Berlin brain–computer interface (BBCI): towards a new communication channel for online control in gaming applications. J. Multimedia Tools Appl. 33, 73–90.

Kübler, A., Furdea, A., Halder, S., and Hösle, A. (2008). “Brain paintingBCI meets art,” inProceedings of the 4th International Brain-Computer Interface Workshop and Training Course, Graz, Austria, 361–366.

Kübler, A., Nijboer, F., Mellinger, J., Vaughan, T. M., Pawelzik, H., Schalk, G., McFarland, D. J., Birbaumer, N., and Wolpaw, J. R. (2005). Patients with ALS can use sensorimotor rhythms to operate a brain–computer interface. Neurology 64, 1775–1777.

Kwakkel, G., Kollen, B. J., and Wagenaar, R. C. (1999). Therapy impact on functional recovery in stroke rehabilitation: a critical review of the literature. Physiotherapy 85, 377–391.

Lai, S.-M., Studenski, S., Duncan, P. W., and Perera, S. (2002). Persisting consequences of stroke measured by the Stroke Impact Scale. Stroke 33, 1840–1844.

Lalor, E. C., Kelly, S. P., Finucane, C., Burke, R., Smith, R., Reilly, R. B., and McDarby, G. (2005). Steady-state VEP-based brain computer interface control in an immersive 3-D gaming environment.EURASIP J. Appl. Signal Process. 19, 3156–3164.

Langhorne, P., Coupar, F., and Pollock, A. (2009). Motor recovery after stroke: a systematic review. Lancet Neurol. 8, 741–54.

Lecuyer, A., Lotte, F., Reilly, R. B., Leeb, R., Hirose, M., and Slater, M. (2008). Brain–computer interfaces, virtual reality, and videogames. Computer 41, 66–72.

Leeb, R., Friedman, D., Müller-Putz, G. R., Scherer, R., Slater, M., and Pfurtscheller, G. (2007a). Self-paced (asynchronous) BCI control of a wheelchair in virtual environments: a case study with a tetraplegics.Comput. Intell. Neurosci, 2007, 8, Article ID 79642. doi:10.1155/2007/79642.

Leeb, R., Gubler, M., Tavella, M., Miller, H., and Millán, J. d. R. (2010a). “On the road to a neuroprosthetic hand: a novel hand grasp orthosis based on functional electrical stimulation,” in Proceedings of the 32nd Annual International Conference of the IEEE Engineering in Medicine and Biology Society, Buenos Aires.

Leeb, R., Sagha, H., Chavarriaga, R., and Millán, J. d. R. (2010b). “Multimodal fusion of muscle and brain signals for a hybrid-BCI,” inProceedings of the 32nd Annual International Conference of the IEEE Engineering in Medicine and Biology Society.

Leeb, R., Keinrath, C., Friedman, D., Guger, C., Scherer, R., Neuper, C., Garau, M., Antley, A., Steed, A., Slater, M., and Pfurtscheller, G. (2006). Walking by thinking: the brainwaves are crucial, not the muscles! Presence Teleoper. Virtual Environ. 15, 500–514.

Leeb, R., Lee, F., Keinrath, C., Scherer, R., Bischof, H., and Pfurtscheller, G. (2007b). Brain–computer communication: motivation, aim and impact of exploring a virtual apartment. IEEE Trans. Neural Syst. Rehabil. Eng. 15, 473–482.

Leeb, R., Settgast, V., Fellner, D. W., and Pfurtscheller, G. (2007c). Self-paced exploring of the Austrian National Library through thoughts. Int. J. Bioelectromagn. 9, 237–244.

Leuthardt, E. C., Schalk, G., Wolpaw, J. R., Jemann, J. G., and Oran, D. W. (2004). A brain–computer interface using electrocorticographic signals in humans. J. Neural Eng. 1, 63–71.

Levine, S. P., Bell, D. A., Jaros, L. A., Simpson, R. C., Koren, Y., and Borenstein, J. (1999). The navchair assistive wheelchair navigation system. IEEE Trans. Neural Syst. Rehabil. Eng. 7, 443–451.

Liepert, J., Bauder, H., Wolfgang, H. R., Miltner, W. H., Taub, E., and Weiller, C. (2000). Treatment-induced cortical reorganization after stroke in humans. Stroke 31, 1210–1216.

Lotze, M., and Halsband, U. (2006). Motor imagery. J. Physiol. 99, 386–395.

Lu, S., Guan, C., and Zhang, H. (2009). Unsupervised brain computer interface based on intersubject information and online adaptation. IEEE Trans. Neural Syst. Rehabil. Eng. 17, 135–145.

Mahlke, S. (2005). “Understanding users’ experience of interaction,”

in Proceedings of the 2005 Annual Conference on European Association of Cognitive Ergonomics, Athens.

Mak, J., and Wolpaw, J. (2010). Clinical applications of brain–computer interfaces: current state and future prospects. IEEE Rev. Biomed. Eng. 2, 187–199.

Malouin, F., Richards, C. L., Durand, A., and Doyon, J. (2008). Clinical assessment of motor imagery after stroke. Neurorehabil. Neural Repair 22, 330–340.

Mangold, T., Keller, S., Curt, A., and Dietz, V. (2005). Transcutaneous functional electrical stimulation for grasping in subjects with cervical spinal cord injury. Spinal Cord 43, 1–13.

Mellinger, J., Schalk, G., Braun, C., Preissl, H., Rosenstiel, W., Birbaumer, N., and Kübler, A. (2007). An MEG-based brain–computer interface (BCI). Neuroimage 36, 581–593.

Memberg, W. D., Crago, P. E., and Keith, M. W. (2003). Restoration of elbow extension via functional electrical stimulation in individuals with tetraplegia. J. Rehabil. Res. Dev. 40, 477–486.

Merians, A. S., Poizner, H., Boian, R., Burdea, G., and Adamovich, S. (2006). Sensorimotor training in a virtual reality environment: does it improve functional recovery poststroke? Neurorehabil. Neural Repair 20, 252–267.

- Millán, J. d. R. (2002). “Brain–computer interfaces,” in Handbook of Brain Theory and Neural Networks, 2nd Edn, ed. M. A. Arbib (Cambridge, MA: The MIT Press), 178–181.
- Millán, J. d. R. (2003). Adaptive brain interfaces. Commun. ACM 46, 74–80.
- Millán, J. d. R. (2004). “On the need for on-line learning in brain–computer interfaces,” in Proceedings of 2004 International Joint Conference on Neural Networks, Budapest.

Millán, J. d. R., Buttfield, A., Vidaurre, C., Krauledat, M., Schögl, A., Shenoy, P., Blankertz, B., Rao, R. P. N., Cabeza, R., Pfurtscheller, G., and Müller, K.-R. (2007). “Adaptation in brain–computer interfaces,” inToward Brain–Computer Interfacing, eds G. Dornhege, J. d. R. Millán, T. Hinterberger, D. McFarland, and K.-R. Müller (Cambridge, MA: MIT press), 303–325.

Millán, J. d. R., Galán, F., Vanhooydonck, D., Lew, E., Philips, J., and Nuttin, M. (2009). “Asynchronous non-invasive brain-actuated control of an intelligent wheelchair,” in Proceedings of the 31st Annual International Conference of the IEEE Engineering in Medicine and Biology Society, Minneapolis, MN: IEEE.

Millán, J. d. R., Mouriño, J., Franzé, M., Cincotti, F., Varsta, M., Heikkonen, J.,

and Babiloni, F. (2002). A local neural classifier for the recognition of EEG patterns associated to mental tasks. IEEE Trans. Neural Netw. 13, 678–686.

Millán, J. d. R., Renkens, F., Mouriño, J., and Gerstner, W. (2004a). Brainactuated interaction. Artif. Intell. 159, 241–259.

Millán, J. d. R., Renkens, F., Mouriño, J., and Gerstner, W. (2004b). Noninvasive brain-actuated control of a mobile robot by human EEG. IEEE Trans. Biomed. Eng. 51, 1026–1033.

Miranda, E. R. (2006). Brain–computer music interface for composition and performance.Int. J. Disabil. Hum. Dev. 5, 119–125.

Moritz, C. T., Perlmutter, S. I., and Fetz, E. E. (2008). Direct control of paralysed muscles by cortical neurons. Nature 456, 639–642.

Mugler, E., Bensch, M., Halder, S., Rosenstiel, W., Bogdan, M., Birbaumer, N., and Kübler, A. (2008). Control of an internet browser using the P300 event-related potential. Int. J. Bioelectromagn. 10, 56–63.

Müller, K.-R., and Blankertz, B. (2006). Toward noninvasive brain–computer interfaces. IEEE Signal Process. Mag. 23, 125–128.

Müller-Putz, G. R., Scherer, R., Pfurtscheller, G., and Rupp, R. (2005). EEG-based neuroprosthesis control: a step towards clinical practice.Neurosci. Lett. 382, 169–174.

Müller-Putz, G. R., Scherer, R., Pfurtscheller, G., and Rupp, R. (2006). Brain–computer interfaces for control of neuroprostheses: from synchronous to asynchronous mode of operation. Biomed. Tech. 51, 57–63.

Müller-Putz, G. R., Scherer, R., Pfurtscheller, G., and Rupp, R. (2007). “Control of a two-axis artificial limb by means of a pulse width modulated,” in Proceedings of the 9th European Conference on Advancement of Assistive Technology, San Sebastian.

Murphy, T. H., and Corbett, D. (2009). Plasticity during stroke recovery: from synapse to behaviour. Nat. Rev. Neurosci. 10, 861–872.

Netz, J., Lammers, T., and Hömberg, V. (1997). Reorganization of motor output in the non-affected hemisphere after stroke. Brain 120, 1579–1586. Neumann, N., and Kübler, A. (2003). Training locked-in patients: a challenge for the use of brain–computer interfaces. IEEE Trans. Neural Syst. Rehabil. Eng. 11, 169–172.

Neuper, C., Müller-Putz, G. R., Scherer, R., and Pfurtscheller, G. (2006). Motor imagery and EEG-based control of spelling devices and neuroprostheses. Prog. Brain Res. 159, 393–409.

Neuper, C., Scherer, R., Reiner, M., and Pfurtscheller, G. (2005). Imagery of

motor actions: differential effects of kinesthetic and visual-motor mode of imagery in single-trial EEG. Cogn. Brain Res. 25, 668–677.

Neuper, C., Schlögl, A., and Pfurtscheller, G. (1999). Enhancement of left-right sensorimotor EEG differences during feedback-regulated motor imagery. Clin. Neurophysiol. 16, 373–382.

Nicolelis, M. A. L. (2001). Actions from thoughts. Nature 409, 403–407.

Nijboer, F., Furdea, A., Gunst, I., Mellinger, J., McFarland, D. J., Birbaumer, N., and Kübler, A. (2007). An auditory brain– computer interface (BCI).J. Neurosci. Methods 167, 43–50.

Nijboer, F., Sellers, E. W., Mellinger, J., Jordan, M. A., Matuz, T., Furdea, A., Halder, S., Mochty, U., Krusienski, D. J., Vaughan, T. M., Wolpaw, J. R., Birbaumer, N., and Kübler, A. (2008). A P300-based brain–computer interface for people with amyotrophic lateral sclerosis. Clin. Neurophysiol. 119, 1909–1916.

Nijholt, A. (2009). “BCI for games: a ‘state of the art’ survey,” in Proceedings of the 8th International Conference on Entertainment Computing, Paris, 225–228.

Nijholt, A., Erp, J., and van Heylen, D. K. J. (2008a). “BrainGain: BCI for HCI and games,” in Proceedings of the AISB Symposium on Brain Computer Interfaces and Human Computer Interaction: A Convergence of Ideas, Aberdeen, 32–35.

Nijholt, A., Tan, D., Allison, B., Millán, J. d. R., Graimann, B., and Jackson, M. M. (2008b). “Brain–computer interfaces for HCI and games,” in Proceedings of ACM CHI 2008, Florence.

Nudo, R. J. (2006). Mechanisms for recovery of motor function following cortical damage.Curr. Opin. Neurobiol. 16, 638–644.

Obermaier, B., Müller, G. R., and Pfurtscheller, G. (2003). “Virtual keyboard” controlled by spontaneous EEG activity. IEEE Trans. Neural Syst. Rehabil. Eng. 11, 422–426.

Page, S. J., Levine, P., and Leonard, A. (2007). Mental practice in chronic stroke: results of a randomized, placebo-controlled trial. Stroke 38, 1293–1297.

Page, S. J., Maslyn, S., Hermann, V. H., Wu, A., Dunning, K., and Levine, P. G. (2009). Activity-based electrical stimulation training in a stroke patient with minimal movement in the paretic upper extremity.Neurorehabil. Neural Repair 23, 595–599.

Parikh, S. P., Grassi, V., Kumar, V., and Okamoto, J. (2004). “Incorporating user inputs in motion planning for a smart wheelchair,” in Proceedings of the 2004 IEEE International Conference on Robotics and

Automation (ICRA’04), New Orleans, LA, USA.

Pfurtscheller, G., Allison, B. Z., Bauernfeind, G., Brunner, C., Solis Escalante, T., Scherer, R., Zander, T. O., Müller-Putz, G., Neuper, C., and Birbaumer, N. (2010). The hybrid BCI. Front. Neurosci. 4:42. doi:10.3389/ fnpro.2010.00003.

Pfurtscheller, G., Guger, C., Müller, G., Krausz, G., and Neuper, C. (2000). Brain oscillations control hand orthosis in a tetraplegic.Neurosci. Lett. 292, 211–214.

Pfurtscheller, G., Müller, G. R., Pfurtscheller, J., Gerner, H. J., and Rupp, R. (2003). Thought-control of functional electrical stimulation to restore hand grasp in a patient with tetraplegia.Neurosci. Lett. 351, 33–36.

Pfurtscheller, G., and Neuper, C. (2001). Motor imagery and direct brain–computer communication. Proc. IEEE 89, 1123–1134.

Pfurtscheller, G., Neuper, C., Flotzinger, D., and Pregenzer, M. (1997). EEG-based discrimination between imagination of right and left hand movement. Electroencephalogr. Clin. Neurophysiol. 103, 642–651.

Pistohl, T., Ball, T., Schulze-Bonhage, A., Aertsen, A., and Mehring, C. (2008). Prediction of arm movement trajectories from ECoG-recordings in humans. J. Neurosci. Methods 167, 105–114.

Platz, T., Kim, I. H., Pintschovius, H., Winter, T., Kieselbach, A., Villringer, K., Kurth, R., and Mauritz, K. H. (2000). Multimodal EEG analysis in man suggests impairment-specific changes in movement-related electric brain activity after stroke. Brain 123, 2475–2490.

Popescu, F., Fazli, Y., Badower, S., Blankertz, B., and Müller, K.-R. (2007). Single trial classification of motor imagination using 6 dry EEG electrodes.PLoS ONE 2:e637. doi:10.1371/journal. pone.0000637.

Prasad, G., Herman, P., Coyle, D., McDonough, S., and Crosbie, J. (2009). “Using motor imagery based brain–computer interface for poststroke rehabilitation,” in Proceedings of the 4th IEEE/EMBS International Conference on Neural Engineering, Antalya.

Prassler, E., Scholz, J., and Fiorini, P. (2001). A robotics wheelchair for crowded public environment. IEEE Robot. Autom. Mag. 8, 38–45.

Rebsamen, B., Burdet, E., Guan, C., Zhang, H., Teo, C. L., Zeng, Q., Laugier, C., and Ang, M. H. (2007). Controlling a wheelchair indoors using thought. IEEE Intell. Syst. 22, 18–24.

Rodden, K., and Wood, K. R. (2003). “How do people manage their dig-

ital photographs?” in Proceedings of SIGCHI Conference Human factors in Computing Systems (CHI ’03), Fort Lauderdale, FL, USA, 409–416.

Röfer, T., and Lankenau, A. (2000). Architecture and applications of the Bremen autonomous wheelchair. Inf. Sci. 126, 1–20.

Ron-Angevin, R., Diaz-Estrella, A., and Velasco-Alvarez, F. (2009). A two-class brain computer interface to freely navigate through virtual worlds. Biomed. Tech. 54, 126–133.

Ruffini, G., Dunne, S., Farrés, E., Cester, I., Watts, P. C. P., Silva, S. R. P., Grau, C., Fuentemilla, L., Marco-Pallarés, J., and Vandecasteele, B. (2007). “ENOBIO dry electrophysiology electrode; first human trial plus wireless electrode system,” in Proceedings of the 29th Annual International Conference of the IEEE Engineering Medicine and Biology Society, Lyon, France.

Schaechter, J. D. (2004). Motor rehabilitation and brain plasticity after hemiparetic stroke. Prog. Neurobiol. 73, 61–72.

Scherer, R., Lee, F., Schlögl, A., Leeb, R., Bischof, H., and Pfurtscheller, G. (2008). Toward self-paced brain– computer communication: navigation through virtual worlds. IEEE Trans. Biomed. Eng. 55, 675–682.

Scherer, R., Mohapp, A., Grieshofer, P., Pfurtscheller, G., and Neuper, C. (2007a). Sensorimotor EEG patterns during motor imagery in hemiparetic stroke patients.Int. J. Bioelectromagn. 9, 155–162.

Scherer, R., Müller-Putz, G. R., and Pfurtscheller, G. (2007b). Selfinitiation of EEG-based brain– computer communication using the heart rate response. J. Neural Eng. 4, L23–L29.

Scherer, R., Müller, G. R., Neuper, C., Grainmann, B., and Pfurtscheller, G. (2004). An asynchronous controlled EEG-based virtual keyboard: improvement of the spelling rate. IEEE Trans. Biomed. Eng. 51, 979–984.

Schlögl, A. (2000).The Electroencephalogram and the Adaptive Autoregressive Model: Theory and Applications. Aachen, Germany: Shaker Verlag.

Sellers, E. W., Krusienski, D. J., McFarland, D. J., Vaughan, T. M., and Wolpaw, J. R. (2006). A P300 event-related potential brain–computer interface (BCI): the effects of matrix size and inter stimulus interval on performance. Biol. Psychol. 73, 242–252.

Sellers, E. W., Turner, P., Sarnacki, W. A., Mcmanus, T., Vaughan, T. M., and Matthews, B. (2009). “A novel dry electrode for brain–computer interface,” inProceedings of the 13th International Conference on Human–Computer Interaction, San Diego, CA, USA.

Sharma, N., Baron, J.-C., and Rowe, J. B. (2009a). Motor imagery after stroke: relating outcome to motor network connectivity. Ann. Neurol. 66, 604–616.

Sharma, N., Pomeroy, V. M., and Baron, J.-C. (2006). Motor imagery: a backdoor to the motor system after stroke? Stroke 37, 1941–1952.

Sharma, N., Simmons, L. H., Jones, P. S., Day, D. J., Carpenter, T. A., Pomeroy, V. M., Warburton, E. A., and Baron, J.-C. (2009b). Motor imagery after subcortical stroke: a functional magnetic resonance imaging study.Stroke 40, 1315–1324.

Shenoy, P., Krauledat, M., Blankertz, B., Rao, R. P. N., and Müller, K.-R. (2006). Towards adaptive classification for BCI. J. Neural Eng. 3, 13–23.

Silvoni, S., Volpato, C., Cavinato, M., Marchetti, M., Priftis, K., Merico, A., Tonin, P., Koutsikos, K., Beverina, F., and Piccione, F. (2009). P300-based brain–computer interface communication: evaluation and follow-up in amyotrophic lateral sclerosis. Front. Neurosci. 3:60. doi:10.3389/ neuro.20.001.2009.

Simmons, L., Sharma, N., Baron, J.-C., and Pomeroy, V. M. (2008). Motor imagery to enhance recovery after subcortical stroke: who might benefit, daily dose, and potential effects. Neurorehabil. Neural Repair 22, 458–467.

Simpson, R. C. (2005). Smart wheelchairs: a literature review.J. Rehabil. Res. Dev. 42, 423–436.

Simpson, R. C., and Levine, S. P. (1999). Automatic adaptation in the navchair assistive wheelchair navigation system. IEEE Trans. Neural Syst. Rehabil. Eng. 7, 452–463.

Sitaram, R., Zhang, H., Guan, C., Thulasidas, M., Hoshi, Y., Ishikawa, A., Shimizu, K., and Birbaumer, N. (2007). Temporal classification of multichannel near-infrared spectroscopy signals of motor imagery for developing a brain–computer interface. Neuroimage 34, 1416–1427.

Subramanian, S. K., Massie, C. L., Malcolm, M. P., and Levin, M. F. (2010). Does provision of extrinsic feedback result in improved motor learning in the upper limb poststroke? A systematic review of the evidence. Neurorehabil. Neural Repair 24, 113–124.

Sugiyama, M., Krauledat, M., and Müller, K.-R. (2007). Adaptation by importance weighted cross validation. J. Mach. Learn. Res. 8, 985–1005.

Sullivan, T. J., Deiss, S. R., Jung, T. P., and Cauwenberghs, G. (2008). A brain– machine interface using dry-contact, low-noise EEG sensors. InProceedings of the 2008 IEEE International Symposium on Circuits and Systems (ISCAS 2008), Seattle, WA.

Sutter, E. E. (1992). The brain response interface: communication through visually-induced electrical brain response. J. Microcomput. Appl. 15, 31–45.

Takahashi, C. D., Der-Yeghiaian, L., Le, V., Motiwala, R. R., and Cramer, S. C. (2008). Robot-based hand motor therapy after stroke. Brain 131, 425–437.

Tangermann, M. W., Krauledat, M., Grzeska, K., Sagebaum, M., Vidaurre, C., Blankertz, B., and Müller, K.-R. (2008). “Playing pinball with non-invasive BCI,” in22nd Annual Conference on Neural Information Processing Systems, Vancouver.

Tavella, M., Leeb, R., Rupp, R., and Millán, J. d. R. (2010). “Towards natural noninvasive hand neuroprostheses for daily living,” inProceedings of the 32nd Annual International Conference of the IEEE Engineering in Medicine and Biology Society, Buenos Aires.

Thorsen, R., Spadone, R., and Ferrarin, M. (2001). A pilot study of myoelectrically controlled FES of upper extremity. IEEE Trans. Neural Syst. Rehabil. Eng. 9, 161–168.

Tonin, L., Leeb, R., Tavella, M., Perdikis, S., and Millán, J. d. R. (2010). “The role of shared-control in BCI-based telepresence,” in 2010 IEEE International Conference on Systems, Man, and Cybernetics, Istanbul.

Touyama, H. (2008). Photo data retrieval via P300 evoked potentials. IEICE Trans. Inf. Syst. 91, 2212–2213.

Tractinsky, N., Katz, A., and Ikar, D.

(2000). What is beautiful is usable. Interact. Comput. 13, 127–145.

Trejo, L. J., Kochavi, R., Kubitz, K., Montgomery, L. D., Rosipal, R., and Matthews, B. (2005). “EEG-based estimation of cognitive fatigue,” in Proceedings of the SPIE, Vol. 5797, Orlando, FL.

Vanacker, G., Millán, J. d. R., Lew, E., Ferrez, P. W., Galán, F., Philips, H., Van Brussel, J., and Nuttin, M. (2007). Contextbased filtering for assisted brainactuated wheelchair driving.Comput. Intell. Neurosci. 2007, 12, Article ID 25130 doi:10.1155/2007/25130.

Verbunt, J. A., Seelen, H. A. M., Ramos, F. P., Michielsen, B. H. M., Wetzelaer, W. L., and Moennekens, M. (2008). Mental practice-based rehabilitation training to improve arm function and daily activity performance in stroke patients: a randomized clinical trial. BMC Neurol. 8, 7.

Vidaurre, C., and Blankertz, B. (2010). Towards a cure for BCI illiteracy.Brain Topogr. 23, 194–198.

Vidaurre, C., Krämer, N., Blankertz, B., and Schlögl, A. (2009). Time domain parameters as a feature for EEG-based brain computer interfaces. Neural Netw. 22, 1313–1319.

Vidaurre, C., Schlögl, A., Blankertz, B., Kawanabe, M., and Müller, K.-R. (2008). “Unsupervised adaptation of the LDA classifier for brain–computer interfaces,” in Proceedings of the 4th International Brain–Computer Interface Workshop and Training Course, Graz, Austria, 122–127.

Vidaurre, C., Schlögl, A., Cabeza, R., Scherer, R., and Pfurtscheller, G. (2006). A fully on-line adaptive BCI. IEEE Trans. Biomed. Eng. 53, 1214–1219.

Volpe, B. T., Huerta, P. T., Zipse, J. L., Rykman, A., Edwards, D., Dipietro, L., Hogan, N., and Krebs, H. I. (2009). Robotic devices as therapeutic and diagnostic tools for stroke recovery. Arch. Neurol. 66, 1086–1090.

von Bünau, P., Meinecke, F. C., Kiraly, F., and Müller, K.-R. (2009). Finding stationary subspaces in multivariate time series. Phys. Rev. Lett. 103, 214101.

Wang, W., Collinger, J. L., Perez, M. A., Tyler-Kabara, E. C., Cohen, L. G., Birbaumer, N., Brose, S. W., Schwartz, A. B., Boninger, M. L., and Weber, D. J. (2010). Neural interface technology for rehabilitation: exploiting and promoting neuroplasticity. Phys. Med. Rehabil. Clin. N. Am. 21, 157–178.

Ward, N. S., and Cohen, L. G. (2004). Mechanisms underlying recovery of motor function after stroke. Arch. Neurol. 61, 1844–1848.

Weiskopf, N., Mathiak, K., Bock, S. W., Scharnowski, F., Veit, R., Grodd, W., Goebel, R., and Birbaumer, N. (2004). Principles of a brain–computer interface (BCI) based on real-time functional magnetic resonance imaging (fMRI). IEEE Trans. Biomed. Eng. 51, 966–970.

Wickelgren, I. (2003). Tapping the mind. Science 299, 496–499.

Williamson, J. (2006). Continuous Uncertain Interaction. Ph.D. thesis, Department of Computing Science, University of Glasgow.

Williamson, J., Murray-Smith, R., Blankertz, B., Krauledat, M., and Müller, K.-R. (2009). Designing for uncertain, asymmetric control: interaction design for brain–computer interfaces. Int. J. Hum. Comput. Stud. 67, 827–841.

Wills, S., and MacKay, D. (2006). DASHER—an efficient writing system for brain–computer interfaces? IEEE Trans. Neural Syst. Rehabil. Eng. 14, 244–246.

Wolf, S. L., Winstein, C. J., Miller, J. P., Taub, E., Uswatte, G., Morris, D., Giuliani, C., Light, K. E., and Nichols-Larsen, D. (2006). Effect of constraint-induced movement therapy on upper extremity function 3 to 9 months after stroke: the EXCITE randomized clinical trial. JAMA 296, 2095–2104.

Wolpaw, J. R., Birbaumer, N., McFarland, D. J., Pfurtscheller, G., and Vaughan, T. M. (2002). Brain–computer interfaces for communication and control.Clin. Neurophysiol. 113, 767–791.

Wolpaw, J. R., McFarland, D. J., and Vaughan, T. M. (2000). Brain– computer interface research at the Wadsworth center.IEEE Trans. Neural Syst. Rehabil. Eng. 8, 222–226.

Wyndaele, M., and Wyndaele, J. J. (2006). Incidence, prevalence and epidemiology of spinal cord injury: what learns a worldwide literature survey? Spinal Cord 44, 523–529.

Yanco, H. A. (1998). “Wheelesley, a robotic wheelchair system: indoor navigation and user interface,” in Assistive Technology and Artificial Intelligence,

Lecture Notes in Artificial Intelligence, eds V. O. Mittal, H. A. Yanco, J. Aronis, and R. Simspon (New York: SpringerVerlag), 256–268.

Yoo, S. S., Fairneny, T., Chen, N. K., Choo, S. E., Panych, L. P., Park, H., Lee, S. Y., and Jolesz, F. A. (2004). Brain– computer interface using fMRI: spatial navigation by thoughts. Neuroreport 15, 1591–1595.

Zhang, H., Wang, C., and Cuan, C. (2007). “Time-variant spatial filtering for motor imagery classification,” in Proceedings of the 29th Annual International Conference of the IEEE Engineering Medicine and Biology Society, Lyon, France.

Conflict of Interest Statement: C. Giugliemma discloses that he has financial relationships with QualiLife. The remaining authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

Received: 09 March 2010; paper pending published: 28 March 2010; accepted: 01 August 2010; published online: 07 September 2010. Citation: Millán JdR, Rupp R, MüllerPutz GR, Murray-Smith R, Giugliemma C, Tangermann M, Vidaurre C, Cincotti F, Kübler A, Leeb R, Neuper C, Müller K-R and Mattia D (2010) Combining brain–computer interfaces and assistive technologies: state-of-the-art and challenges. Front. Neurosci.4:161. doi:10.3389/ fnins.2010.00161 This article was submitted to Frontiers in Neuroprosthetic, a specialty of Frontiers in Neuroscience. Copyright © 2010 Millán, Rupp, MüllerPutz, Murray-Smith, Giugliemma, Tangermann, Vidaurre, Cincotti, Kübler, Leeb, Neuper, Müller and Mattia. This is an open-access article subject to an exclusive license agreement between the authors and the Frontiers Research Foundation, which permits unrestricted use, distribution, and reproduction in any medium, provided the original authors and source are credited.

