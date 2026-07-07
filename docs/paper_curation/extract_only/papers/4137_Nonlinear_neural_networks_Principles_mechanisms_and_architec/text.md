[Figure 1]

NeuralNetworks.Vol. I, pp. 17-61, 1988 Printed in theUSA. All rightsreserved. Copyright @ 19880893-6080/88Pergamon Journals$3.00 +Ltd..00

[Figure 2]

[Figure 3]

ORIGINAL CONTRIBUTION

###### Nonlinear Neural Networks: Principles, Mechanisms, and Architectures

[Figure 4]

[Figure 5]

###### STEPHEN GROSSBERG

[Figure 6]

BostonUniversity

[Figure 7]

(Received and accepted 1September 1987)

Abstract-An historicaldiscussionisprovided oftheintellectualtrendsthatcausednineteenthcenturyinterdisciplinary studies ofphysicsand psychobiologyby leading scientistssuchas Helmholtz,Maxwell, and Mach to splinter into separatetwentieth-centuryscientific movements.The nonlinear,nonstationary,and nonlocalnature ofbehavioral andbrain data are emphasized.Threesourcesofcontemporaryneural network research-the binary, linear,and continuous-nonlinearmodels-are noted.Theremainder ofthearticle describesresultsaboutcontinuous-nonlinear models: Manymodelsofcontent-addressablememoryare shownto be specialcasesoftheCohen-Grossbergmodel and global Liapunovfunction, including the additive, brain-state-in-a-box,McCulloch-Pitts,Boltzmann machine, Hartline-Ratliff-Millet; shunting,maskingfield,bidirectionalassociativememory,Volterra-Lotka,Gilpin-Ayala,and Eigen-Schustermodels.A Liapunovfunctional methodisdescribedfor provingglobal limit or oscillation theorems for nonlinear competitivesystemswhentheir decisionschemesare globallyconsistentor inconsistent,respectively. Theformer caseis illustrated bya model ofa globallystableeconomicmarket,andthelatter caseis illustrated by a model ofthevotingparadox.Keypropertiesofshuntingcompetitivefeedbacknetworksare summarized,including therole ofsigmoid signalling,automaticgain control,competitivechoiceand quantization,tunablefiltering, total activitynormalization,andnoisesuppressionin patterntransformationandmemorystorageapplications.Connections to models ofcompetitivelearning, vectorquantization,and categoricalperceptionare noted.Adaptiveresonance theory(ART)modelsfor selJstabilizingadaptivepatternrecognitionin responseto complexreal-time nonstationary input environmentsare comparedwith off-line modelssuchas autoassociators,theBoltzmann machine,and back propagation.Special attention is paid to the stability and capacity ofthesemodels,and to the role oftop-down expectationsand attentional processingin the activeregulation ofboth learningandfast information processing. Models whoseperformanceand learning are regulated by internal gating and matching signals,or by external environmentallygeneratederror signals,arecontrastedwith modelswhoselearningisregulatedbyexternalteacher signalsthat haveno analogin natural real-timeenvironments.Examplesfrom sensory-motorcontrol ofadaptive vectorencoders,adaptivecoordinatetransformations.adaptivegain control by visualerror signals.and automatic generation ofsynchronousmultijoint movementtrajectoriesillustrate theformer model types.Internal matching processesare showncapable of discoveringseveraldifferent types of inyariant environmentalproperties. These includeART mechanismswhichdiscoverrecognitioninvariants.adaptivevectorencodermechanismswhichdiscover movementinvariants.and autoreceptiveassociativemechanismswhichdiscoverinvariants ofselJregulatingtarget position maps.

###### TABLE OF CONTENTS

[Figure 8]

[Figure 9]

- 1. Introduction
- 2. Interdisciplinary StudiesDuring the NineteenthCentury: Helmholtz, Maxwell,and Mach
- 3. The SchismbetweenPhysicsand Psychology
- 4. The Nonlinear,Nonlocal,and NonstationaryPhenomenaof Mind and Brain

- A. Color Theory
- B. Top-DownLearning,Expectation,and Matching

[Figure 10]

- 18
- 19 19 19

- 19
- 20

[Figure 11]

[Figure 12]

BaseduponalecturegivenonOctober7, 1986attheNSFmeeting on Neural Networksand Neuromorphic Systems,Woburn, Massachusetts.

Supportedin part by the Air ForceOffice of ScientificResearch (AFOSR F49620-86-C-OO37and AFOSR F49620-87-C-OO18)and the National ScienceFoundation(NSFIRI-84-17756).

[Figure 13]

The author thanksCynthia Suchtaand CarolYanakakisfor their valuableassistancein the preparationof themanuscriptand illustrations.

Requestsfor reprintsshouldbesentto StephenGrossberg,Center for AdaptiveSystems,BostonUniversity, III Cummington Street, Boston,MA 02215.

18 S. Grossberg

[Figure 14]

[Figure 15]

[Figure 16]

- 5. The Nature of anEnduring Synthesis
- 6. Sourcesof Neural NetworkResearch:Binary, Linear,and Continuous-Nonlinear

- A. Binary
- B. Linear
- C. Continuous-Nonlinear

- 7. Nonlinear FeedbackBetweenFastDistributed STM Processingand SlowAssociativeLTM Processing
- 8. Principles,Mechanisms,and Architectures
- 9. Content-AddressableMemory Storage:A GeneralSTM Modeland ~iapunov Method

- A. Additive STM Equation
- B. Brain-State-in-a-BoxModel: S ~ Exchange
- C. The McCulloch-Pitts Model I
- D. The BoltzmannMachine f
- E. The Hartline-Ratliff-Miller Model
- F. ShuntingCooperative-CompetitiveFeedbackNetwork
- G. MaskingField Model
- H. BidirectionalAssociativeMemories:Symmetrizing anAsymmetric Interaction Matrix
- I. Volterra-Lotka,Gilpin-Ayala,and Eigen-SchusterModels

- 10. Other LiapunovMethods II. Testingthe Global Consistencyof Decisionsin CompetitiveSystemsI

- 12. StableProductionStrategiesfor a Competitive Market
- 13. SensitiveVariable-LoadParallelProcessingby ShuntingCooperative.CompetitiveNetworks:Automatic Gain Control and Total Activity Normalization
- 14. PhysiologicalInterpretation of ShuntingMechanismsasa Membrane Equation
- 15. Sigmoid Feedback,ContrastEnhancement,and Short Term Memory Storageby Shunting FeedbackNetworks

- A. Linear Signal:PerfectPatternStorageand Noise Amplification
- B. Slower-than-LinearSignal:PatternCompressionand Noise Amplification
- C. Faster-than-LinearSignal:Winner-Take-All,Noise Suppression,and Total Activity Quantization in an EmergentFinite StateMachine
- D. SigmoidSignal:TunableFilter,QuenchingThreshold,Noise Suppression,and Normalization

- 16. CompetitiveLearning Models
- 17. StableSelf-Organizationof PatternRecognitionCodes

- A. Real-Time (On-Line)Learning versusLab-Time (Off-Line)Learning
- B. NonstationaryUnexpectedWorld VersusStationaryControlled World
- C. Self-OrganizationVersusTeacherasa Sourceof ExpectedOutput
- D. Self-StabilizationVersusCapacityCatastrophe
- E. Maintain Plasticityon anUnexpectedWorld versusExternally Shut Off Plasticity
- F. Self-ScalingComputationalUnits
- G. Learn Internal ExpectationsVersusImpose ExternalCosts
- H. Active Attentional Focusingand Priming VersusPassiveWeightChange
- I. ClosingVersusOpeningthe Fast-SlowFeedbackLoop
- J. ExpectantPriming VersusGrinding All Memory Cycles
- K. Learning in the Approximate Match PhaseVersusin the Mismatch Phase:HypothesisTestingAvoidsthe NoiseCatastrophe
- L. Fastor SlowLearning:The OscillationCatastrophe
- M. Self-AdjustingParallelMemory SearchTreesand Global EnergyLandscapeUpheavalVersusSearchTrees and Local Minima
- N. Rapid Direct AccessVersusIncreaseof RecognitionTime with Code Complexity
- O. AsynchronousVersusSynchronousLearning
- P. Discriminative Tuning via Attentional Vigilance
- Q. Towardsa General-PurposeMachine for CognitiveHypothesisTesting,Data Search,and Classification

- 18. Internally RegulatedLearning andPerformancein Neural Modelsof Sensory-MotorControl: Adaptive Vector EncodersandCoordinateTransformations
- 19. ExternalError Signalsfor Learning Adaptive MovementGains: Push-PullOpponentProcessing
- 20. Match-Invariants:Internally RegulatedLearning of an Invariant Self-RegulatingTargetPositionMap
- 21. PresynapticCompetition for Long TermMemory: Self-RegulatingCompetitiveLearning References

[Figure 17]

- 20
- 21

- 21
- 22

- 22 24

- 24

- 24
- 25

25 26

- 26
- 27

- 27 27

- 29

- 29
- 30

- 30

- 32

[Figure 18]

- 33 35

- 35
- 36
- 37 37

[Figure 19]

- 37
- 38
- 39
- 40 40 40

- 40

- 40
- 41

- 41
- 42
- 43

- 43

[Figure 20]

- 43
- 44

[Figure 21]

44 44 45 45

- 45 45

[Figure 22]

- 50
- 51 54 56

"The foundationsof scienceasa whole,and of physicsin 1. INTRODUcnON particular, await their next greatelucidations from the side of biology,and especiallyfrom the analysisof the sensations

[Figure 23]

[Figure 24]

[Figure 25]

The physicaland mathematical theory of neural networks hasbeendevelopingrapidly during the past25 years.It is a theory whose diversity and complexity reflectthe multifaceted organizationof the brain processesthat it setsout to explain. In this article, I will summarize some of the unifying principles, mechanisms, and mathematicalmethods that arise in this

...psychological observationon the onesideand physical observationon the other maymake suchprogressthat they will ultimately comeinto contact,and that in this way new factsmaybe broughtto light. The resultof this investigation will not bea dualismbut rathera sciencewhich, embracing both the organicand the inorganic,shall interpret the facts that are commonto thetwo departments." (Mach, 1914)

[Figure 26]

Nonlinear NeuralNetworks 19

[Figure 27]

[Figure 28]

theory,aswellassomeof the specializedneuralarchitectureswhichare important both in physicalanalyses of behavioraland brain data and in the development of noveltechnologies.

I will beginthis article with somehistoricalremarks that may clarify the complexand oftenconfusingsociological milieu in which theseexciting intellectual developmentshavebeentaking place.

###### 2. INTERDISCIPLINARYSTUDIES DURING THE NINETEENTH CENTURY: HELMHOLTZ, MAXWELL, AND MACH

[Figure 29]

[Figure 30]

Interdisciplinary studiesflourishedduring the nineteenthcentury.In additionto pursuingtheir greatwork in physics,scientistssuchasHelmholtz, Maxwell,and Machalsomade seminalcontributions to psychology and neurobiology(Boring, 1950;Campbell& Garnett, 1882;Glazebrook, 1905;Koenigsberger,1906;Ratliff, 1965).Theirinterestsin thestructureof physicalspacetime werebalancedbya fascinationwith psychological space-time.Thus their contributions to understanding theobservedworld developedside-by-sidetheiranalysis of the observer.

Forexample,everyphysicistknowsaboutthe Mach numbersand abouttheinfluenceof Mach'sideasupon Einstein'sthinking during the developmentof relativity theory. Mach is alsofamous, however,for his investigationsof the Mach bandsin vision. Surprisingly few scientistshavestudied both types of contributions in school. In a similar way,everyphysicistknows about Maxwell's fundamental contributions to electromagnetic theoryandto the moleculartheoryofgases.Maxwell is equally well known, however,for his work on developingtrichromatic colortheory.

Helmholtz's life is an inspiration to usall. Trained asanM.D., hisexperimentsonthe velocityof electrical signals in nerve axonsled him to help discoverthe principle of conservationof energy,whichisoneofthe cornerstonesof nineteenth-centuryphysics.He made fundamentalcontributions to optics,which servedas a foundation for his classicalcontributions to vision. His work in acousticslikewise supported his major contributions to hearing.

Thus during the lasthalf ofthe nineteenthcentury, a number of greatscientistsfunctioned successfullyin an interdisciplinary researchmode and made lasting contributionsto boththe physicaland psychobiological sciences.

###### 3. THE SCHISM BETWEEN PHYSICS AND PSYCHOLOGY

[Figure 31]

It is often acceptedasa truism that successbreeds success,just asmoneymakesmoney.Likewise,thegreat interdisciplinarysuccessesof Helmholtz,Maxwell,and

[Figure 32]

Mach might have beenexpectedto breed droves of dedicated interdisciplinary disciples. This did not, however,occur. In the next generationof physicists, Einstein himself, in a letter to his friend QueenElizabethof Belgium in 1933,wrote: "Most of us prefer to look outsiderather than insideourselves;for in the lattercaseweseebuta darkhole,whichmeans:nothing at all" (Nathan& Norden, 1960,p. 567).

Thus a schismof major scientific importance occurred towardsthe emdof the nineteenthcentury.Scientistswhoseworkwaspreviouslygreatlyenergizedby interdisciplinary investigations of physics and psychologywererapidly replacedby scientistswho rarely had evena rudimentary knowledgeof the otherfield. Although the explosionof scientificknowledgeduring the twentieth century, with its attendantrequirement to specialize,surelycontributed to this schism,deeper

intellectualfactorse~acerbatedthis schism.An understandingof thesefactorsis useful for appreciatingthe scientificclimate in which neuralnetworkresearchhas beencarried out during the pastfewdecades.

[Figure 33]

4. THE NONLINEAR, NONLOCAL, AND NONSTATIONARY PHENOMENA OF MIND AND BRAIN

Basiccausesof this schismemergedfrom the scientific work of the very pioneers,suchas Helmholtz, Maxwell, and Mach, whose interdisciplinary careers wehavebeenconsidering.Two examplesfrom Helmholtz's work on visual perceptionareillustrative.

[Figure 34]

A. Color Theory

In the classical Newtonian approach to color theory, white light is defined by an energy spectrum that is locally measurable at each point in space. In contrast, Helmholtz realized that, during visual perception, the averagecolor of awhole scenetends to look white (Beck, 1972; Helmholtz, 1962). Thus, instead of being reduceable to local measurements at each location, the analysis of how humans perceive white light at each location necessitates an investigation of long-range (or nonlocal) interactions across a network of locations. Such investigations disclosed the role of these interactions in "discounting the illuminant," or enabling humans and other speciesto detect the actual reflectances of visible surfaces under a wide variety of illumination conditions. In addition to being nonlocal, the network interactions which discount the illuminant, being sensitive to image reflectances, are also nonlinear. The neural processes whereby illuminants are discounted are still the subject of intensive experimental and theoretical investigation (Arend, Buehler, & Lockhead, 1971; Com sweet, 1970; Hurvich, 1981; Land, 1977; Mollon & Sharpe, 1983)and only recently have a large number of paradoxical brightness and color phenomena

INPUTS

[Figure 35]

20 S. Grossberg

[Figure 36]

[Figure 37]

beenanalysedin a unifiedwayusingareal-time neural networkmodel(Cohen& Grossberg,1984;Grossberg, 1987a,1987b;Grossberg& Mingolla, 1985a,1985b; Grossberg& Todorovic,in press).

[Figure 38]

B. Top-DownLearning,Expectation,andMatching

Helmholtzfacedanotherbarrier whenheattempted to conceptualizetheprocessof visualperceptionitself. His conceptionis knownasthedoctrine of unconscious inference(Boring, 1950).This doctrine held thata raw sensorydatum, or perzeption,is modified by previous experiencevia a learned imaginal increment, or vorstellung,before it becomesa true perception, or anschauung.Thus Helmholtz realized that we perceive, in part, what we expectto perceivebasedupon past learning.

Helmholtz's doctrine canbe recastin modernterminology as follows (Figure I). Bottom-up environmentally-activatedinput signalstriggerthe read-outof learnedtop-downexpectations.Thesebottom-up and top-down data cooperate and compete through a matchingprocessuntil theygenerateanemergentconsensuswhich is the final percept.Sucha cooperativecompetitivenetworkinteractionalsorequiresnonlinear and nonlocalinteractions.In addition, the learning of top-downexpectationsrequiresa nonstationaryprocess. ThusHelmholtz'sexperimentaldiscoveriesaboutvisual perceptionled to the realization that theoretical understandingofthesephenomenawould requirethediscoveryofappropriatenonlinear,nonlocal,andnonstationary mathematics,which are nowbeing developed on multiple fronts.

In contrast, muchof the mathematicsavailablefor physicaltheorizingduring the nineteenthcenturywas linear, local,and stationarymathematics.Thus theexperimentaldiscoveriesaboutmind and brain by workerslike Helmholtz, Maxwell,and Mach clarified that

[Figure 39]

-

[Figure 40]

[Figure 41]

TOP-DOWN LEARNING

[Figure 42]

BOTTOM-UP LEARNING

-

(EXPECT AT ION)

[Figure 43]

[Figure 44]

COOPERATIONCOMPETITION

|[Figure 45]<br><br>T| |
|---|---|
| |[Figure 46]|
| | |

[Figure 47]

FIGURE 1. Bottom-up inputs and learned top-down expectations interact via a co-operative-competitive matching process until they generate an emer!~ent consensus w'hich represents the final, or resonant, percE'pt.

[Figure 48]

the availablemathematicswere not sufficient for supportinga sustainedtheoreticalpenetrationofmind and brainmechanisms.Sincetheoreticalscientistsrelyupon appropriatemathematicalbread-and-buttertechniques to expressand developtheir deepestintuitive ideas,the mismatch between psychological phenomena and nineteenth-centurymathematicscreatedan intellectual crisis for all theoristswho might havewishedto study mind and brain.

This schismwas exacerbatedby the fact that the major revolutions of twentieth-centuryphysicscould besupportedby nineteenth-centurymathematics.For example,whenEinsteinfinally realizedthat heneeded a certain type of mathematicsto expressthe general relativity theory,his burdenwassignificantlylightened by the fact that nineteenth-century Riemannian geometryprovided a perfecttool. As the early quantum mechaniciansstruggledtowardsexpressingtheir intuitive insightsusing matrix theory and linear operator theory,theytoo weregreatlyaidedbystrongnineteenthcentury mathematicaltraditions.

A major approach-avoidanceparadigmwashereby establishedin the practiceof theoreticalscience.Theoretical physicistsabandoned psychologyand neurobiologyto rapidly fashiontheories aboutthe external world that could bequantitativelysupported by availablemathematicalconceptsandmethods.Psychologists and neurobiologistsreturned the favor by abandoning physicalconceptsand mathematicsthat seemedirrelevantto their data and, overtime; by also eschewing and even denegrating theoretical and mathematical trainihg in general.This bifurcation was alreadyapparentduring the unfolding of Helmholtz's scientific life. Beginning his careeras an M.D., he ended it as the first Presidentofthe newPhysico-technicalInstitute in Berlin (Koenigsberger,1906).

###### 5. THE NATURE OF AN ENDURING SYNTHESIS

[Figure 49]

Left without anappropriate framework of concepts and mathematicaltechniquesfor interpretingandunifying their experiments,psychologistsand neurobiologistsnonethelesswent aboutaccumulatingoneof the largestand mostsophisticatedsetsof data basesin the history ofscience.Remarkably,theyaccomplishedthis featduring a century of controversythat wasspawned by the unavailability of a unifying theoretical and mathematicalframeworkfor explaining their data.As HilgardandBower(1975)havenotedin their important textbookabouttheoriesofleaming "Psychologyseems to be constantly in a state of ferment and change,if not of turmoil and revolution" (p. 2).

While mostmind andbrainexperimentalistsignored theory and mosttheoristslooked for more hospitable frontiers, there arosethe widespreadtendencyto interpretbrain function in terms of whatevertechnolog-

[Figure 50]

Nonlinear Neural Nel~'orks 21

[Figure 51]

[Figure 52]

ical developmenthappenedto be current. The everexpandinglist of technologicalmetaphorsto whichthe brain has beencomparedincludes telegraphcircuits, hydraulic systems,information processingchannels, digitalcomputers,linearcontrolsystems,catastrophies, holograms,andspinglasses.All ofthesemetaphorshave beenunable to explain a substantialdata baseabout brain and behavior,as well they might, sincenone of them arosefrom a sustainedanalysisof behavioralor brain data.

The schism betweenphysics and psychologyencouragedtheoriststrained in the physicstradition to believethatno theoriesof behaviorandbrainexist.An inquiry aboutavailabletheoriesby aninterestedphysicist more often than not would confirm this impression,becausethe schismhaspreventedmostpsychologists and neurobiologists from getting the training necessaryto understandthe theoriesthat havebegun to copewith the nonlinear,nonlocal,andnonstationary nature of behavioraland brain data.Thusthe theories which hold the greatestpromise have beenthe ones that havebeenmost difficult to evaluatein the social climate spawnedby the greatschism.

Wecanrecognizein this sociologicalmilieu touches of irony whenweacknowledgethatakeyscientificissue in understandingbehaviorand brain isto explain how humansrapidly and spontaneouslyadaptto noisyand complex environmentswhoserules may changeunexpectedly,or in William Jame$'engagingphrase:How do wecopewith the "blooming buzzingconfusion" of everyday? It remainsto be seenhow the severalscientific communities nowconvergingwith enthusiasm but vastlydifferenttraining and goalsupon the interdisciplinary studyofmind andbrain will assimilatethe noisy and unexpectedconstraints imposed by each others' existence,notably by the fact that, despitethe extra burden of difficult sociologicalconditions,relevanttheoriesof mind and brain havebeendeveloping rapidly during the pastfewdecades.

6. SOURCESOF NEURAL NETWORK RESEARCH:BINARY, LINEAR,

[Figure 53]

CONTINUOUS-NONLINEAR

###### A. Binary

[Figure 54]

At leastthree sourcesof neural network research canbeidentifiedwhichhavehada substantialinfluence on contemporary research.The streamsof research

[Figure 55]

generatedby the sourceshaveintersectedin complex waysthrough the yearsand havetendedto converge during the pastseveralyears.The presentbrief review merelysetsthe stagefor the article's laterdiscussions. Dueto the sheersizeand complexity ofthe neuralnetworkliterature,thisreviewmustnecessarilybeselective. Otherrecentcollectionsof classicaland current neural network results include both articles (Carpenter &

Grossberg,1987b;Grossberg,1987e;Hecht-Nielsen, 1986;Hestenes,1987; Levine, 1983;Szu, 1986)and books(Amari & Arbib, 1982;Denker,1986;Grossberg,

1982, 1987c, 1987d,1988;Grossberg& Kuperstein, 1986;Hinton & Anderson,1981;Kohonen, 1977,1984; McClelland & Rumelhart, 1986; Rumelhart & Mc-

Clelland, 1986).

Table 1 indicates severalof the contributions that initiated orillustrate significantresearchdevelopments. The streamof binaryneuralnetworkswasinitiated by the classicalarticle of McCullochandPitts(1943).This article investigatedthresholdlogicsystemsofthe form

Xj(t + I) = sgn[2:; Ajjxj(t) -BJ, (I)

wheresgn(w) = + 1 if w> 0,0 if w = 0, and -1 if w < O.Suchbinarysystemswereinspired in part byneu-

[Figure 56]

rophysiologicalobservationsshowingthat neuralsignals betweenmany cellsare carried by all-or-none spikes. The variablesXi in Equation (I) are oftencalled short term memory (STM) traces,or activations.Caianiello

- (1961)useda binary STM equationof the form

n ~m)

Xi(t+ r) = 1[~ ~ A~1)Xj(t-kr) -BiJ (2)

i-i k-O

where I(w} = 1 if w > 0 and 0 if w ~ O. Rosenblatt

- (1962)usedan STM equationof the form

-dd Xi= lAx/+ ~n 4>(Bj+ Xj)Cij (3)

t i-i

where <t>(w)= 1 if w ~ 8 and 0 if w < 8. Mueller, Martin, and Putzrath (1962)designedcircuits which usedthe McCulloch-Pitts logical operationsand also extendedtheir analysisto analogcircuits for applications to acousticpatternrecognition.

[Figure 57]

The binary,discrete-timeapproachto neuralmodelingwasencouragedbythe technicalliberation which the use of oscilloscopesbrought to neurophysiology. After yearsof heroic effortsto measurethe tiny electrical signalsin nerves,eachspikecould at lastbeeasily

[Figure 58]

TABLE 1

[Figure 59]

[Figure 60]

[Figure 61]

[Figure 62]

Hartline-Ratliff-Miller (1963) Grossberg (1967. 1968) Sperling-Sondhi (1968) Wilson-Cowan (1972)

McCulloch-Pitts (1943) Caianiello (1961) Rosenblatt (1962)

[Figure 63]

22 S, Grossberg'

[Figure 64]

[Figure 65]

[Figure 66]

amplified until it filled the whole oscilloscope screen. The all-or-none property of the individual spike was

celebrated by making eachspike much bigger than life. Although the oscilloscope provided a way for people to look at spikes, this representation did not necessarily correspond to what the cells which received the spikes were measuring. Cell body potentials may vary slowly and continuously relative to the time scale of a single spike. Thus neurons may process the frequencies or other statistical properties of spike sequencesthrough time. If, for example, the spiking activity of a visual cortical feature detector is amplified by a microphone instead of by an oscilloscope, and if an object to which the detector is sensitive is brought in and out of its receptive field, one hears a continuous waxing and waning of the sound of the cell's spike discharges through time. If the potentials of the cells receiving thesespike sequencesfluctuate slowly enough to average across clusters of spikes, then such cells will be better modeled by continuous than binary dynamics.

Both Caianiello (1961) and Rosenblatt (1962) also introduced equations to change the weights A~;)in (2) and C;jin (3) through learning. Such adaptive weights are often called long term memory (L TM) traces. Both workers decoupled the interactions between STM traces and LTM traces in order to partially analyze their nonlinear equations. These LTM equations also had a digital aspect.The equations of Caianiello (1961)increased or decreased at constant rates until they hit finite upper or lower bounds. Those of Rosenblatt (1962) were used to classify patterns into two distinct classes,as in the Perceptron Learning Theorem.

The historical importance of the binary McCullochPitts (1943) model cannot be overestimated. For example, in addition to its seminal influence on. neural modelling per se,it also was very much in the thoughts ofvon Neumann ashe developed his ideas for the modern digital computer. In fact, a number ofbrain-inspired developments have found spin-offs over the years into other technologies.

B. Linear

[Figure 67]

Conceptsfrom linear systemtheory haveprovided a classicalsourceof modelsfor representingsomeof the continuous aspectsof neural dynamics.Solutions of simultaneouslinearequationsY = AX usingmatrix

theoryandconceptsaboutcross-correlationhavebeen amongthe usefultools.

Inspired by an interestin brain modeling, Widrow (1962)developedhis classicalgradientdescentAdeline adaptivepatternrecognitionmachinebeforeusingthis background to make his major contributions to the theory of adaptiveantennas.Anderson(1968)initially describedhis intuitions about neural patternrecognition usingthe spatialcross-correlationfunction

" "

cPI2(X,y)= L LJi(i,j)}2(i+x,j+y). (4)

;-1i-i

[Figure 68]

Kohonen(1971)madehistransitionfrom linearalgebra conceptssuchasthe Moore-Penrosepseudoinverseto more biologicallymotivatedstudieswhichhehassummarized in his influential books (Kohonen, 1977, 1984).Theseworkersthus beganto developtheir intuitions within a mathematicallyfamiliar engineering framework which was progressivelydevelopedto include more biologically motivated nonlinear interactions.

###### C. Continuous-Nonlinear

[Figure 69]

Continuous-nonlinearnetworklawstypically arose froma directanalysisof behavioralor neuraldata.One distinguishedmodelingtradition canbetraceddirectly to the influenceof Mach (Ratliff, 1965).This tradition setout to modeldatataken from the lateraleyeof the Limulus, or horseshoecrab, and led to the award of a Nobelprize to H. K. Hartline.

The basic model from this tradition is the steady stateHartline-Ratliff model

n rj = e; -L k;j[rj -r;j]+ (5)

i-i where [w]+ = max(w,0). This model describeshow cellularexcitationse;aretransformedinto netresponses rjdueto inhibitory feedbackinteractionsgovernedby threshold-linearsignals -kjj[rj -rjj]+. Thus,the Hartline-Ratliff model is a type of continuous thresholdlogic system..Ratliff, Hartline, and Miller (1963)extendedthis steady-statemodelto a dynamical model of the form

[Figure 70]

whichalsobehaveslinearlyin thesuprathresholdrange. This modelis a precursorof the additive model that is describedbelow.

[Figure 71]

Another classicaltradition arosefrom the analysis of howthe excitablemembraneof a singleneuron can generateelectricalspikescapableof rapidly and nondecrementallytraversingthe axon, or pathway,of the cell.The original experimentaland modelingwork on the squid giant axon by Hodgkin and Huxley (1952) alsoled to the award of a Nobelprize. Sincethis work focusedonindividual cellsratherthannetworksof cells, it will not be further discussedherein exceptto note that it providesthe foundation for the shuntingmodel that is describedbelow.The Hodgkin-Huxley model andsomeofits variationsarereviewedelsewhere(Carpenter, 1981; Hodgkin, 1964; Hodgson, 1983;Katz, 1966; Plonsey& Fleming, 1969; Ricciardi & Scott, 1982;Scott, 1977).

Another source of continuous-nonlinear network models arose through a study of adaptive behavior, ratherthan of neuralmechanismsperse,in Grossberg (1964, 1967, 1968a,1968b).Its primary concernwas

[Figure 72]

Nonlinear Neural Networks 23

[Figure 73]

[Figure 74]

to understandhow the behaviorof individuals adapts stablyin real-time to complexand changingenvironmentalcontingencies.In orderto analyzeadaptivebehavior, it is necessaryto characterizethe functional levelon whicha system'sbehavioralsuccessis defined and achieved,as well asthe computationalunits that aremanipulated by this level.This behavioralanalysis led to the derivation of continuous neural networks definedby nonlinearlycoupled STM and LTM traces, andto the mathematicalproof thatthe computational units of thesenetworks are not individual STM and LTM variables,but are ratherdistributed spatialpatterns of STM and LTM variables(Grossberg,1968b,

1969a,1969b,1970a).Thus, neuralnetworksdescribe a proper levelfor ananalysisof adaptivebehaviorbecausethe functional units which govern behavioral successare emergentpropertiesdueto interactionson the networklevel.

As in thetradition ofbinarymodels,thiscontinuousnonlinear approachdefined laws for STM tracesand LTM traces(Figure 2). The two primary versionsof the STM equationwhichwereintroduced throughthis approachhavebeenused in many applicationssince the 1960sand havereceivedincreasingexperimental support.

###### AdditiveSTMEquation

[Figure 75]

d n n -

d Xi = -Aixi + L Jj(Xj)BjiZlt>-L gj(Xj)CjiZli>+ Ii- (7)

t j-l j-l

[Figure 76]

Equation (7) includes a term for passivedecay (- Aixi), positive feedback (2::J=I.fj(Xj)BjiZ)7»,negative feedback (-2::7-1 gfixj)Cjiz)i), and input (Ii). Each feedback term includes a state-dependent nonlinear signal (.fj(Xj), gfiXj», a connection, or path, strength (Bji, Cji), and an LTM trace (z)7), z)i). If the positive and negative feedbackterms are lumped together and the connection strengths are lumped with the LTM traces, then the additive model may be written in the simpler form

- d "
- di Xi = -Aixi + .L Jj(XJZji+ 1/. (8) i-I

[Figure 77]

Early applications of the additive model included computational analysesin vision, associativepattern learning,patternrecognition,classicalandinstrumental conditioning, andthe learningof temporalorderin ap-

# J.

x.

[Figure 78]

[Figure 79]

###### e..

###### v.

[Figure 80]

[Figure 81]

J

I

###### IJ

[Figure 82]

FIGLIRE 2. Short-term memory traces (or potentials) Xi at c:ell populations Vi emit signals along the directed pathways (or axons) eii which are gated by long-term memory traces Ziibefore they can perturb their target cells Vj'

[Figure 83]

plications to speechand languagebehavior and to planned sensory-motor control (Grossberg, I969a, I969b, I969c, 1970a, I970b, 1971a, 1972a, 1972b, 1974; Grossberg& Pepe,1971). The additive model hascontinued to bea cornerstoneof neural network researchto the presentday; see,for example, Amari and Arbib (1982)and Grossberg(1982). Somephysicistsunfamiliar with the classicalstatusofthe additive model in neural network theory erroneouslycalled it the Hopfield modelaftertheybecameacquaintedwith Hopfield's first application of the additive model in Hopfield (1984); see Section 9A. The classicalMcCulloch-Pitts (1943) model in Equation (1) has also erroneouslybeencalled the Hopfield model by some physicistswhobecameacquaintedwith theMcCullochPitts model in Hopfield(1982).Thesehistorical errors canultimately betracedto the schismbetweenphysics and psychologythat wasdescribedin Section3.

A related behaviorallyderived STM equationwas foundto moreadequatelymodeltheshuntingdynamics of individual neurons (Hodgkin, 1964; Kandel &

Schwartz,1981;Katz, 1966;Plonsey& Heming,1969). In sucha shunting equation, each STM trace is restrictedto aboundedinterval [-D;, B;] andautomatic gain control, instantiated by multiplicative shunting terms, interacts with balancedpositive and negative feedbacksignalsandinputs to maintain the sensitivity of eachSTM tracewithin its interval (seeSection15)~

ShuntingSTMEquation

d-d Xi = -Aixi + (Bi -Xi)[ ~ Jj(Xj)Cjiz}7>+ Ii]

t i-i

n

[Figure 84]

[Figure 85]

-! (X; + D;)[2:: gAXj)Ej;z}i) + J;].

(9)

, j-1

[Figure 86]

SeveralLTM equationshavebeenuseful in applications.Two particularly usefulvariationshavebeen:

###### PassiveDecayLTM Equation

[Figure 87]

###### and GatedDecayLTM Equation

[Figure 88]

did Zjj = hj(xJ[-Fjjzjj + Gjj};(x;)]. (11)

In bothequations,a nonlinearlearningtermJj(xj)hj(Xj), oftencalleda Hebbianterm after Hebb(1949),is balancedbya memorydecayterm. In (10),memorydecays passivelyata constantrate -Fjj. In (11),memorydecay is gatedon and off by one of the nonlinear signals.A key proPertyof both equationsis that the size of an LTM trace Zjj can either increaseor decreasedue to learning. Neurophysiological support for an LTM

equation of the form (11)has recentlybeenreported (Levy, 1985;Levy, Brassel,& Moore, 1983; Levy &

v.

[Figure 89]

24

[Figure 90]

Desmond, 1985;Rauschecker& Singer,1979;Singer, 1983).ExtensivecomputationalanalysesoftheseSTM and LTM equationsin a numberofspecializedcircuits led graduallyto the identification of a generalclassof networksfor whichonecouldproveinvariantproperties of associativespatio-temporal pattern learning and recognition(Grossberg,1969a,1971b, 1972c,1982).

Sperlingand Sondhi(1968)utilized a shuntingSTM equation in an important contribution to visual psychophysics.Wilson and Cowan (1972) introduced a modified shunting STM equationof the form

d n diXj = -AjXj + (Bj -Xj)fi(.L XjCji) (12)

)8\

[Figure 91]

which replacesthe sum 2:j=l jj(xftCj;z~t) of nonlinear signals in (9) with a nonlinear function of the sum. Equation (12) possessesone automatic gain control term (B;-x;), whereas(9)possessestwo. Consequently, thedynamicsof (12)saturatein manysituationswhere the dynamics of (9) remain sensitiveto input fluctuations (seeSection15).

[Figure 92]

7. NONLINEAR FEEDBACK BETWEEN FAST DISTRIBUTED STM PROCESSING AND SLOW ASSOCIATIVE LTM PROCESSING

Thesedynamicalequationsincorporatetwo general typesof nonlinear processeswhich explicatesomeof the themesthat were alreadytouched upon in Helmholtz's work. On the onehand,therearethe cooperative-competitive nonlinear feedbackprocesseswhich operateona relativelyfasttime scale.Theseprocesses instantiatethe distributed information processingand STM storagecapabilitiesofthe network. Theycan,for example, carry out matching.of bottom-up data with top-downexpectations(Figure I) to generatethe perceptualconsensusdiscussedby Helmholtz.

Interacting with these fast STM interactions via nonlinear feedbackarethe more slowlyvarying LTM processeswhich instantiate associativelearning. Such a learning processcan, for example, adaptivelytune the bottom-up filtersandencodethe learnedtop-down expectations (Figure I) that were adumbrated in Helmholtz's conceptof unconsciousinference.

###### 8. PRINCIPLES, MECHANISMS, AND ARCHITECfURES

[Figure 93]

Such STM and LTM equations were discovered through the analysisof two mutually supportive, but complementary,typesof results.

On the onehand,a small numberof generaldesign principles and their mechanistic instantiations were discoveredthrough a comparativeanalysisof several interdisciplinary data bases.For example, the functional importance of the shunting STM equation (9)

[Figure 94]

S. Grossberg

[Figure 95]

becameclearthroughanalysesof dataaboutperception, conditioning, and cognitive information processing. Suchanalysesled to the realization that a singletype of network wasneededthat wascapableof ratio processing,conservationor normalization of total activation (limited capacity), Weberlaw modulation, adaptation levelprocessing,noisesuppression,contrastenhancement, short term memory storage, energetic amplification of matchedinput patterns,andenergetic suppressionof mismatched input patterns. The discoverythat thesemultiple constraintsare all satisfied byaubiquitoustype of on-centeroff-surround network of cells which obeythe membraneequations of neurophysiologycreated an irresistable intellectual pressure to study them exhaustively (see Sections 9F and 13-15).

In addition to suchgenerallaws,a growing number of specializedarchitectureshavealso beendeveloped. Eacharchitectureisasynthesisof severaltypesof design principlesandmechanismsin a carefullycraftedcircuit. The organization of the brain into functionally distinctive regions-such as cerebellum, hippocampus, retina,visualcortex, parietalcortex, frontal cortex,hypothalamus,septum, amygdala,and reticular formation-illustrates why a considerablenumber of specializedarchitecturesneedto bedeveloped.

.Due to the highly interactive nature of brain dynamics, the development of general organizational principles,mechanisms,and specializedarchitectures haveproceededhand-in-hand, eachbootstrappingthe scientificunderstandingoftheothers.Hereisa research areawhere it is essentialto keepthe forest,the trees, andthe individual branchessimultaneouslyin view.In the remainderof the article, I will summarize several of theprinciples,mechanisms,andarchitectureswhose furtherdevelopmentis still engagingthe effortsof many scientists.

[Figure 96]

9. CONTENT-ADDRESSABLE MEMORY STORAGE: A GENERAL STM MODEL AND LIAPUNOV METHOD

[Figure 97]

From a mathematicalperspective,the question of content-addressablememory (CAM) in a neural network canbe formulated as follows: Under what conditions does a neural network always approach an equilibrium point in responseto anarbitrary, but sustained,input pattern?The equilibrium point represents the storedpattern in responseto the input pattern. In a satisfactoryanalysisof this problem, the behaviorof the network in responseto arbitrary initial data, an arbitrary sustained input pattern, and an arbitrary choiceof network parametersis provided.Also anaccount of how many equilibrium points exist and of how they are approachedthrough time is desirable. Sucha mathematicalanalysisiscalleda globalanalysis,

[Figure 98]

Nonlinear NeuralNetworks

[Figure 99]

to distinguish it from a local stability analysisaround individual equilibrium points.

Amari and Arbib (1982)and Levine (1983)include a numberof contributionsto the localanalysisof neural networks.Our concernhereinis with globalmethods. A globalanalysisof equilibrium behavioris of importance for an understandingboth of CAM and of the types of nonequilibrium behavior-such as traveling waves,bursts, standingwaves,and chaos-which can be obtained by perturbing off systemswhich always approachequilibrium (Carpenter,1977a,1977b,1979, 1981;Cohen& Grossberg,1983;Ellias & Grossberg, 1975; Ermentrout & Cowan, 1979, 1980; Hastings, 1976,1982;Hodgson,1983;Kaczmarek& Babloyantz, 1977).A globalmathematicalanalysisof nonlinearassociativelearning networks was begun in Grossberg (1967,1968b).A globalmathematicalanalysisof nonlinear shuntingcooperative-competitivefeedbacknetworkswasbegunin Grossberg(1973).Someofthe main articlesin theseseriesarebroughttogetherin Grossberg

(1982).

One approachto the globalapproachto equilibrium which has attracted widespreadinterestis the useof global Liapunov, or energy,methods. Such global methodswereintroduced fortheanalysisof neuralnetworks in the I970s. Herein I summarize a general model of a nonlinear cooperative-competitiveneural networkfor whicha globalLiapunovfunctionhasbeen explicitly constructed. I then showthat a number of popularmodelsare specialcasesof the generalmodel, andthus arecapableofCAM.

Cohen and Grossberg(1983) describeda general principle fordesigningCAM networksbyproving that modelsthat canbe written in the form

d n

diXj = Qj(Xj)[bj(Xj) -.L Cjjdj(Xj)]' (13)

j-1

|[Figure 100]<br><br>admit the global Liapunov function<br><br>n Ixi 1 n<br><br>V = -L bj(~i)dj(~;)d~j + 2 L cjkdj(xj)dk(Xk) (14) i-I j.k~1<br><br>if the coefficient matrix C,: II CjjII and the functions ai, bi, and djobey mild technical conditions, including<br><br>Symmetry:| |
|---|---|
|[Figure 101]<br><br>Cjj= Cji,|[Figure 102]<br><br>(15)|

[Figure 103]

###### Positivity:

[Figure 104]

[Figure 105]

a/(x/) ~ 0, (16)

[Figure 106]

###### Monotonicity:

|[Figure 107]<br><br>dj(Xj) ~ O. (17)<br><br>Integrating V alongtrajectoriesimplies that<br><br>d n n<br><br>-V = -L aidi[bi -L cijdjf. (18)<br><br>dt i-I j-1<br><br>If(16) and(17)hold,then (d/dt)V ~ 0 alongtrajectories. Oncethis basicproperty of a Liapunov function is in place,it is a technical matterto rigorouslyprove that|
|---|

25

[Figure 108]

[Figure 109]

every trajectory approachesone of a possibly large number of equilibrium points.

Forexpositoryvividness,thefunctionsin theCohenGrossberg model (13) are called the amplification function ai, the selfsignal function hi, and the othersignalfunctions dj. Specializedmodelsare characterized by particular choicesof thesefunctions.

[Figure 110]

A. Additive STM Equation

CohenandGrossberg(1983,p. 819)notedthat"the simpleradditiveneuralnetworks. ..are alsoincluded in ouranalysis."The additiveequation(8)canbewrittenusingthe coefficientsof the standardelectricalcircuit interpretation (Plonsey& Heming, 1969)as

dxi 1 n

CiT = 1 RXi + 2::fJ(Xj)Zji+ Ii. (19)

t, j-t

I

Substitutioninto (13)showsthat

o;(xJ= t (constant!)

[Figure 111]

b;(xJ= -k x;+ Ii (linear!)

[Figure 112]

(20)

[Figure 113]

(21)

Cij= -T/j (22)

[Figure 114]

[Figure 115]

[Figure 116]

and

|[Figure 117]<br><br>dj(Xfl = Jj(Xfl. (23)<br><br>Thus in the additive case,the amplification function (20) is a positiveconstant,hencesatisfying (16), and the self-signalterm (21)is linear. Substitutionof (20)(23)into (14)leadsdirectly to the equation<br><br>n 1 Ixi n<br><br>V = L -: ~;/;(~i)dti -L /ifi(Xi)<br><br>i-I R, i-I|
|---|

n

[Figure 118]

-! L ~k}j(xflfi(Xk). (24) J.k-1

This Liapu~ov function for the additive modelwas

laterpublishedby Hopfield(1984).In Hopfield'streatment, ~iis written as an inverseIi I(Vi), Cohenand

Grossberg(1983)showed,however,that althoughfi(x;) mustbenondecreasing,asin (17),it neednot havean inversein order for (24)to be valid.

[Figure 119]

B. Brain-State-in-a-BoxModel: S ~ Exchange

The BSB model wasintroduced in Anderson,Silverstein,Ritz, and Jones(1977). It is often described in discretetime by the equation

"

[Figure 120]

Xj(t + 1) = S(X;(t) + a L AijXj(t»

[Figure 121]

(25)

i-i

[Figure 122]

usingsymmetric coefficients

Ajj = Aft (26)

[Figure 123]

and a specialtype of nonlinear signal function S(w)

26 S. Grossberg that characterizesthe model. The signalfunction is a symmetric ramp function:

[Figure 124]

[Figure 125]

[Figure 126]

[Figure 127]

of modelswhich havebeentreated as distinct are, in reality,mathematicallyidentical. In contrast,this type of transformation cannot be carried out on shunting modelssuchas (9)and (12).

|[Figure 128]<br><br>F ifw;?:.F<br><br>w if-F<w<F.<br><br>-F ifw.s-F|
|---|

[Figure 129]

S(w) =

[Figure 130]

[Figure 131]

(27)

The Liapunov function for (33)is found by directly substitutinginto model(13)expressedin terms of the variablesYi:

[Figure 132]

Thus eachSTM trace Xiobeysa linear equationuntil its argumentreachesthe hard saturationlimit F.

[Figure 133]

[Figure 134]

The BSBmodelhasbeenusedto discusscategorical perceptionin termsof its formal contrastenhancement propertythat eachXitendsto approacha limiting value :tF, and thus that the vector(Xl, X2,..., xn)tendsto approacha corner of the box (:tF, :tF, ..., :tF) as time goeson. An alternative explanationof contrast enhancementby a nonlinear feedbacknetwork was provided in Grossberg(1973)using a sigmoid signal function, ratherthan a function linear nearzero,coupledto the soft saturationdynamicsof a shuntingnetwork, rather than the hard saturation of a symmetric ramp (seeSectionIS). This is still a topic undergoing theoretical discussion(Anderson,Silverstein,Ritz, & Jones,1977;Grossberg,1978b,1987d).

(34) Since a;(y;) = 1, b;(y;) = -y;, C;j= -B;j, and dj(Yfl

[Figure 135]

= S(Yj), substitution into (14) yields

n fYI n

V = L EiS'(Ei)dEi-! L BjkS(Yj)S(Yk). (35)

i-I k-1

Using the definitions in (27), (29), and (32), Equation (35) can be rewritten in terms of the original variables X;as follows:

a n

[Figure 136]

V = -"2 L AjkXjXk. (36) j,k-t

Golden(1986)hasderived (36) from a direct analysis of the BSBmodel.

The BSB model can be rewritten as an additive modelwith no input anda specialsignalfunction that satisfies(17). Henceit is a specialcaseof model(13). To seethis, rewrite (25) in the form

###### C. TheMcCulloch-PittsModel

[Figure 137]

This classicalmodeltakesthe form

n

n

[Figure 138]

Xi(t + 1) = S( ~ Bijxj(t» (28) j-1

x;(t + I) = sgn(2::Aijxj(t) -B;). i-i

[Figure 139]

(I)

|[Figure 140]<br><br>Letting| |
|---|---|
|[Figure 141]<br><br>M(w) = sgn(w -Bi),<br><br>( I ) can be rewritten as| |

[Figure 142]

usingthe coefficient

[Figure 143]

(37) B.IJ = fJ.IJ + ~~AIJ (29)

[Figure 144]

where Ojj = if i = j and 0 if i + j. By (26), it follows

[Figure 145]

|[Figure 146]<br><br>n<br><br>x;(t + I) = M( L Aijxj(t». (38)<br><br>j~1<br><br>As in theanalysisof (31),(38) canbe rewritten in continuous time in terms of the variablesy; via S }; Ex-<br><br>change: d /I| | |
|---|---|---|
| |[Figure 147]<br><br>diY; = -Y; + L AijM(y)<br><br>i-i|[Figure 148]<br><br>(39)|

that

|[Figure 149]<br><br>Bjj = Bjjo (30)<br><br>Although (28) is written in discretetime for computational convenience,it needsto be expressedin continuous time in orderto representa physicalmodel,as<br><br>in|
|---|

[Figure 150]

[Figure 151]

(31)

[Figure 152]

andis thusalsoa symmetric additive modelwith zero inputs. In addition, its signalfunction M(Yj) hasazero derivative(M'(Yj) = 0) exceptat Yj= o. Substitution of this additionalpropertyinto (35)showsthattheLiapunov function for the continuous time McCullochPitts modelis

[Figure 153]

Define the new variables Yi by

n

Yi = L Bijxj

[Figure 154]

(32)

i-I

###### Then

[Figure 155]

|[Figure 156]<br><br>d "<br>di Yi = -Yi + L BijS(Yj). (33) j-1<br><br><br>Comparisonof(33) with (19)showsthattheBSBmodel is anadditive modelsuchthat eachIi = O.Becausethis simplechangeofcoordinatesis so important in neural modeling, I give it a name:S 2;Exchange.<br><br>The observationthat, viaS 2;Exchange,a nonlinear signalof a sum,as in (31), canbe rewritten asa sum of nonlinear signals,as in (33),showsthat a number|
|---|

n

[Figure 157]

V = -! L AjkM(YvM(Yk), (40)

j,k-l

which is the continuous time version of the discrete time Liapunov function describedby Hopfield (1982).

[Figure 158]

D. The BoltzmannMachine

The STM equation of the Boltzmann machine (Ackley,Hinton, & Sejnowski,1985)hasthesameform

[Figure 159]

Nonlinear Neural Networks 27

[Figure 160]

as(31)and (38),and is thus also anadditive equation with symmetric coefficients.Its signal function is the sigmoidlogistic function

[Figure 161]

###### andthat

[Figure 162]

|[Figure 163]<br><br>gj(Xj) ~ O. (46)<br><br>In orderto write (44) in Cohen-Grossbergform, it is convenientto introduce the variables<br><br>Yi = Xi+ Ci. (47)<br><br>In applications, C; is typically nonnegative.Since X; canvarywithin the interval[-C;, B;],Y;canvarywithin the interval [0, B; + C;] of nonnegativenumbers. In termsofthesevariables,(44)canbewritten in the form|
|---|

I

[Figure 164]

[Figure 165]

(41)

f(w)=~,

which satisfies(17)andis thus a specialcaseof model (13).Thusthe Boltzmannmachineis a specializedadditive modelregulatedby simulatedannealingasdevelopedby Geman(1983, 1984),Gemanand Geman (1984), and Kirkpatrick, Gelatt, and Yecchi (1982, 1983).

[Figure 166]

[Figure 167]

where

[Figure 168]

###### E. TheHartline-Ratliff-MillerModel

[Figure 169]

a;(yu = Y; (nonconstant!),

[Figure 170]

[Figure 171]

(48)

TheS}; Exchangeis notthe onlychangeofvariables

bj(y;) = -[A;C;J -(A; + l;)x; + (B; + C; -x;) x;

[Figure 172]

wherebyCAM modelscanbetransformedinto anadditive modelformat. For example,the STM equation (6) of the classical Hartline-Ratliff-Miller model is transformed into an additive model under an exponential changeof variables

[Figure 173]

x (II + jj(x; -C;»] (nonlinearl), (49) C;j= Vij, (50)

[Figure 174]

and

|[Figure 175]<br><br>dj(Yj) = gj(Yj -q) (noninvertible!). (51)<br><br>Unlike the additive model, the amplification function aim) in (48) is not a constant. In addition, the selfsignal function b;(y;) in (49) is not necessarily linear, notably becausethe feedback signal jj(x; -C;} is often nonlinear in applications of the shunting model; in particular it is often a sigmoid or multiple sigmoid signal function (Ellias & Grossberg, 1975; Grossberg, 1973, 1977, 1978c; Grossberg& Levine, 1975; Sperling, 1981). Sigmoid signal functions, and approximations thereto, also appear in applications of the additive model and its variants (Ackney, Hinton, & Sejnowski, 1985; Amari & Arbib, 1982; Freeman, 1975, 1979; Grossberg, 1969a,1982; Grossberg& Kuperstein, 1986; Hinton & Anderson, 1981; Hopfield, 1984; Rumelhart & McClelland, 1986). Such applications do not require the full generality of the Liapunov function (13) because the nonlinear signal function can then beabsorbed into the terms dj(xj).<br><br>Property (16) follows from the fact that ai(Y;} = Yi ~ O. Property (17) follows from the assumption that the negative feedback signal function gjis monotone non-decreasing. Cohen and Grossberg (1983) proved that gj need not be invertible. A signal threshold may exist below which gj = 0 and above which gj may grow in a nonlinear way. The inclusion of nonlinear signals with thresholds better enables the model to deal with fluctuations due to subthreshold noise. On the other hand, thresholds are not the only mechanisms which can suppress noise in a cooperative-competitive feedback network (see Section 15D).|
|---|

x;(t)=i' e-(I-sJ/Trj(s)ds. (42)

[Figure 176]

Then (6)becomes

-dIn [I ]+

dt XI = --XI -:L -Xj -'Ij klj + el'

[Figure 177]

T )-1 T (43)

[Figure 178]

###### F. ShuntingCooperative-CompetitiveFeedback Network

All additive modelslead to constantamplification functionsai(xJ and linearself-feedbackfunctionsbi(xJ. The need for the more generalmodel (13) becomes apparentwhenthe shunting STM equation(9) is analyzed.Consider,forexample,aclassof shuntingmodels in which eachnode canreceiveexcitatoryand inhibitory inputs Ii and Ji, respectively,and eachnode canexcite itself and can inhibit other nodesvia nonlinear feedback.Suchnetworks model on-centeroffsurround interactions amongcells which obeymembrane equations (Grossberg, 1973; Hodgkin, 1964; Kandel & Schwartz, 1981; Katz, 1966; Plonsey& Fleming, 1969).In particular, let

did X; = -A;x; + (B; -x;)[!; + .fi(x;)]

[Figure 179]

n

[Figure 180]

[Figure 181]

-(Xi + Ci)[Ji + L Dijgj(xj)].

(44)

j-1

[Figure 182]

In (44),eachXi canfluctuate within the finite interval [-C/, B;] in responseto the constantinputs 1;and Ji, the state-dependentpositivefeedbacksignalfi(xu, and the negativefeedbacksignalsD;jgAXj). It is assumed that

###### G. MaskingFieldModel

[Figure 183]

In many applications of the shuntingand additive Dij = Djj ~ 0 models,the coefficientsCijin (13)maybeasymmetric,

|[Figure 184]<br><br>(45)|
|---|

[Figure 185]

[Figure 186]

28 S. G'rossberg

[Figure 187]

[Figure 188]

therebyrenderingthe Liapunov function ( 14)inapplicable.Asymmetric coefficientstypically occurin problems relating to the learning and recognition of temporal order in behavior. Consequently,a number of mathematicalmethodsweredevelopedfromthe earliest daysof the continuous-nonlinearapproachto analyse modelswith asymmetric interactioncoefficients.

Onthe otherhand,certainnetworkmodelsmayhave asymmetric interaction coefficients,yet bereduceable to the form (13)with symmetricinteractioncoefficients through a suitable changeof variables.The masking field model is a shunting network of this type. The masking field model was introduced in Grossberg (1978a;reprinted in Grossberg,1982)to explaindata about speech learning, word recognition, and the learning of adaptivesensory-motorplans. It has been further developedthrough computer simulations in Cohenand Grossberg(1986, 1987).A maskingfield isamultiple-scale,self-similar,automaticallygaincontrolled, cooperative-competitivenonlinear feedback network (Figure 3) which cangeneratea compressed but distributed STM representationof aninput pattern asa whole,of its most salientparts,and of predictive codeswhich representlargerinput patternsof which it forms a part. The maskingfield modelis thus a specialized type of vector quantization scheme (Gray, 1984).Its multiple-scale self-similarpropertiesimply its asymmetric interactioncoefficients.

The STM equationof a typical maskingfield is defined by

[Figure 189]

-dtd x~J) = -AX~J) + (B -xY1[}:: Ejp}() + DIJlf(x~J»]

.jEJ

-(I) C )~m.Kg(x<:1IKI(1+IK n JI) (Xi + ~m.KIKI(1+IKnJI) .

[Figure 190]

(52)

[Figure 191]

In (52),x~J)is the STM trace of the ith maskingfield node that receivesexcitatory input LjEJEjpyf) from the unorderedsetJ of input items.Notation IJI counts the number of items in setJ and therebykeepstrack ofthe numberof spatialscalesthatgointo eachversion of the model.

The inhibitory interaction coefficient

IKI(1 +IKn JI)

[Figure 192]

2:m,KIKI(1 +IK n JI) I (53)

[Figure 193]

in (52)is anasymmetric function of J and K. Despite this fact, (52)canbe written in Cohen-Grossbergform

as

[Figure 194]

[Figure 195]

(54)

[Figure 196]

with symmetric coefficients

[Figure 197]

CJK= CKJ= 1 +IK n JI

[Figure 198]

(55)

in termsofthevariables

y\J) = Fvl(x~J) + C) (56)

[Figure 199]

[Figure 200]

[Figure 201]

###### TEM FIELD

[Figure 202]

(8)

|[Figure 203]<br><br>..:.r---= ~ +---A. E<br><br>~=:...|
|---|

## .;;;;-a.2

[Figure 204]

t

[Figure 205]

[Figure 206]

F1

[Figure 207]

(b)

FIGURE 3. Masking field interi~ctions: (a) I:ells from an item field F, grow randomly to a masking field F2 along positionally sensitive gradients. The nodes in the masking field grow so that larger item groupings, up to, some optimal size, can activate nodes with broader and stron~,er inhibitory interactions. Thus the F, -.F2 connections and fhe F2 +-+F2 interactions exhibit properties of self-similarity; (b) The interactions within a masking field F2 include positive feedback from a node to itself and negative feedback from a nocje to its neighbors. Long term memory (LTM) traces at the ends of F, -.F2 pathways (designated by hemidisks) adaptively tune the filter defined by these pathways to amplify the F2 reaction to item groupings which have previously succeeded in activating their target F2nodes. (Reprinted with permission from Cohen & Grossberg, 1987, p. 1868.)

[Figure 208]

where

FIJI = L IKI(1 +IKn JI). (57)

[Figure 209]

m,K

This is seenasfollows. SinceFIJIis the denominator of (53), it canbe usedto divide term x~J)+ C in (52). Thentheasymmetricterm IKI in the numeratorof (53) canbeabsorbedinto the definition of gin (54). Then by redefining and rearrangingterms as in (47)-(51), equation(54)holds with

[Figure 210]

a\J)(y~J» = Fjjly~J)

(58)

[Figure 211]

[Figure 212]

+ DIJIFIJlf(FIJiY~J) -C»] (59)

[Figure 213]

Nonlinear Neural Networks 29

[Figure 214]

[Figure 215]

where

[ (J)i -IJI- F ""~ E:iPji(J) ,

[Figure 216]

[Figure 217]

(60)

jEJ

and

[Figure 218]

|[Figure 219]<br><br>d(K>(yC:» = IKlg(FIKIYC:> -C). (61)<br><br>Thus the maskingfield modelis a specializedCohen-<br><br>Grossbergmodel.|
|---|

[Figure 220]

H. BidirectionalAssociativeMemories: SymmetrizinganAsymmetric Interaction Matrix

Otherprocedureshavealsobeendevisedfordealing with systemshaving asymmetric coefficients.For example, givenan arbitrary n X m coefficientmatrix Z

= Ilzijll from a network levelFI to a network levelF2 with STM traces Xi and Yj, respectively.Kosko and Guest (in press)and Kosko (1987)have shownthat (13)and (14) canbe usedto construct feedbackpathwaysfrom F2to FI so that the two-levelfeedbacknetwork FI -F2 hasconvergenttrajectories.

Forexample,if the bottom-up interactionF1 -F2 obeysanadditive equation

[Figure 221]

[Figure 222]

then the top-down interaction F2-FI is definedto obeyanadditive equation

d-d Xj = -Bjx/ + ~ g/(y/)z//+ Ji, (63)

l /

[Figure 223]

where IjandJi are input terms.This definition creates asymmetricinteractionmatrix byclosingthe top-down feedbackloop, since if fi(Xi) influences Yjwith coefficient Zijin (62),then gj(Yj)influencesXi with the same coefficientzij. Thus, by defining anaugmentedvector (XI, X2,..., Xn,YI, Y2,..., Ym)of STM activities, system(62)-(63) asa whole define anadditive model (19) with an(n + m) X (n + m)symmetric coefficient

###### matrix.

The sameprocedure can be usedto symmetrize many other neural networkmodels.Kosko and Guest (in press)havedescribedoptical implementations for this procedure,and Kosko (1987)hasusedthe symmetrized additive model to discussminimization of fuzzyentropy.

[Figure 224]

I. Volterra-Lotka, Gilpin-Ayala, andEigen-Schuster Models

The Cohen-Grossbergmodelwasdesignedto also include models which arosein other areasof biology than neural networktheory. For example, it includes the classical

###### Volterra-LotkaModel

- d n
- di Xj = AjXj(l -2:: BijXj) (64) )-1

of population biology(Lotka, 1956),the

[Figure 225]

###### Gilpin-AyalaModel

-x. = A.x. 1 ---"" )"" C:.(-1x. )]

d

[ (XI

(65

dt'" B ,,",IJB.' )

I J-I J

also from population biology (Gilpin & Ayala, 1973), andthe

###### Eigen-SchusterModel

d n

[Figure 226]

###### -x-dt I = XI(A-X~lI I - q '"L., A-xl?j j ) (66)

j-1

from the theory of macromolecularevolution (Eigen & Schuster,1978). In all of thesemodels, either the amplificationfunction a;(x;)isnon-constant,ortheselfsignalfunction b;(x;)is nonlinear,or both.

Thespecializedmodelssummarizedin Sections9A91 illustrate that model (13) and Liapunov function (14) embody a generalprinciple for designingCAM devicesfrom cooperative-competitivefeedbackmodels. Thesemodelsare saidto be absolutelystablebecause the CAM property is not destroyedby changingthe parameters,inputs, or initial valuesof the model.The persistenceof the CAM property under arbitrary parameterchanges-enableslearningto changesystemparametersin responseto unpredictable input environments without destroyingCAM. The STM transformation executedby a network with adaptivelyaltered parameterscan differ significantly from its original STM transformation. A finer analysis is neededto choosemodels,as in Sections9A-91, which are optimallydesignedto carryoutspecializedprocessingtasks.

The Cohen-Grossberganalysisemphasizesthe critical role of mathematicalanalysis in classifyingand understandingvery largesystemsof nonlinear neural networks (VLSN). Without such an integrative approach, it is difficult to tell whetheror not a modelis really newcomputationally, or whetherit is a special caseof a known modelin slightlydifferentcoordinates or notation. Forexample,manyscientistshavenot realized that models (31) and (33) are mathematically equivalent.Table2 describestherelationshipsbetween modelsdisclosedby such an analysis.Thus the BSB modelenjoysaCAM propertyforthesamereasonthat

[Figure 227]

TABLE 2 C:AM Models in Decreasing Generality

[Figure 228]

[Figure 229]

[Figure 230]

MP (1943) BSB (1977) BM (1985) BAM (1987) MF (1978. 1986)

[Figure 231]

ADDITIVE (1967) CG (1983)

[Figure 232]

[Figure 233]

SHUNTING (1973)

[Figure 234]

[Figure 235]

Organization in terms of decreasing generality of the models described in Section 9. Abbreviations: CG = Cohen-Grossberg; MP = McCu!loch-Pitts; BSB = Brain-State-in-a-Box; BM = Boltzmann Machine; BAM = Bidirectional Associative Memory; MF

= Masking F'ield.

[Figure 236]

30 S.Grossberg'

[Figure 237]

[Figure 238]

anyadditiveor CG modeldoes.Onthe otherhand,the BSBmodelmayhavespecialpropertiesthat maymake it ideal for certain tasks,or it maybe too specialized to accomplishcertaintaskswhichare betterdealtwith usinga shuntingmodel.

###### 10. OTHER LIAPUNOV METHODS

[Figure 239]

A considerableamount of workwasdoneonfinding Liapunov functions for specialcasesof(13) beforethe appearanceof Cohenand Grossberg(1983). A global Liapunov methodwasalsodevelopedwhichis in some respectsmoregeneralthanthat of CohenandGrossberg

(1983).

Inthe formercategory,MacArthur (1970)described a quadratic Liapunov function for proving local asymptotic stability of isolated equilibrium points of Volterra-Lotka systemswith symmetric coefficients. Goh and Agnew (1977)describeda global Liapunov function for Volterra-Lotka andGilpin-Ayala systems in caseswhere only one equilibrium point exists.LiapunovfunctionswerealsodescribedforVolterra-Lotka systemswhoseoff-diagonalterms are relatively small (Kilmer, 1972;Takeuchi,Adachi,& Tokumaru, 1978). Suchconstraintsare,however,too limiting for the designofCAM systemsaimedattransformingandstoring a largevariety of patterns.

11. TESTING THE GLOBAL CONSISTENCY OF DECISIONS IN COMPETITIVE

[Figure 240]

SYSTEMS

An alternativeapproachbeganwith the globalanalysis in Grossberg(1973)of the nonlineardynamics of shunting cooperative-competitivefeedbacknetworks. The goalof this analysiswasto designCAM networks capableof transformingandstablystoringin STMlarge numbersofpatterns(seeSectionIS).The firstanalyses carried out direct proofs of the STM transformation andstoragepropertiesfor smallclassesof shuntingnetworks which arosein specializedapplications. Later articles(Ellias& Grossberg,1975;Grossberg& Levine, 1975;Levine, 1979;Levine & Grossberg,1976)classified the global CAM behavior of increasinglylarge setsof networks.

Theseresultsled to the progressivedevelopmentin Grossberg(1977, 1978c,1978d,1980a)ofa globalLiapunovmethod for classifyingthe dynamicalbehaviors of a wider variety of competitive dynamical systems. A competitive dynamical systemis, for presentpurposes,definedbya systemof differentialequationssuch that

d

[Figure 241]

[Figure 242]

[Figure 243]

, Xn) (67)

dix;=./i(Xt,X2,.

###### where

[Figure 244]

[Figure 245]

[Figure 246]

(68)

[Figure 247]

andthe.li are chosento generateboundedtrajectories. By (68),increasingthe activity Xjof a givenpopulation canonlydecreasethe growthratesdldt Xiof otherpopulations,i "" j, or may not influence them at all. No constraintis placeduponthe signof a.lilaxi.Typically, cooperativebehavioroccurs within a population and competitive behavioroccurs betweenpopulations, as in the on-centeroff-surroundnetworks(44). Sincethis Liapunovmethodledto resultswhicharestill ofcurrent interestand which seemamenableto further development,someof its most salientpoints will be sum-

###### marizedhere.

Themethodmakesmathematicallyprecisethesimpleintuitive idea that a competitive systemcanbeunderstoodby keepingtrack of who is winning the competition. To do this, write (67) in the form

diX;d = a;(x;)M;(x) X=(Xl,X2,...,X,,), (69)

[Figure 248]

which factors out the amplification function a;(x;) ~ O.ThendefJne

M+(x) = max{ M;(x): i = 1, 2, ..., n} (70)

and

[Figure 249]

|[Figure 250]<br><br>M-(x) = min{M;(x): i = 1,2,..., n}. (71)<br><br>Thesevariablestrack the largestand smallestratesof change,andareusedto keeptrack of who is winning. Usingthesefunctions, it is easyto seethat thereexists a propertyof ignition: Oncea trajectory entersthepositive ignition region<br><br>R+ = {x: M+(x)~ O} (72)|
|---|

|[Figure 251]<br><br>or the negativeignition region<br><br>R- = {x: M-(x) .s OJ, (73)<br><br>it can neverleaveit. If .x"(t)neverentersthe set<br><br>R* = R+ n R-, (74)<br><br>then eachvariable Xi(t) convergesmonotonically to a limit. The interestingbehaviorin a competitivesystem occursinR*. In particular, if.x"(t)neverentersR+,each Xi(t)decreasesto a limit; then the competition never getsstarted.The set<br><br>S+ = {x: M+(x) = O} (75)<br><br>actslike a competition threshold, which is called the positiveignition hypersurface.<br><br>Wethereforeconsidera trajectoryafterit hasentered<br><br>R*. For simplicity, redefinethe time scaleso that the trajectoryis in R* at time t = O.The Liapunov func-<br><br>tional for anycompetitive systemis thendefinedas<br><br>L(xJ = il M+(~v»dv. (76)<br><br>The Liapunov propertyis a directconsequenceof positive ignition:| | |
|---|---|---|
| |[Figure 252]| |

[Figure 253]

Nonlinear Neural Networks 31

[Figure 254]

[Figure 255]

This functional providesthe "energy" that forcestrajectories through a series of competitive decisions, which are alsocalledjumps. Jumps keeptrack of the statewhich is undergoingthe maximal rate of change at anytime ("who's winning"). If M+(x(r» = Mi(x(t» for times S ~ t < T but M+(x(t» = Mj(x(t» for times T ~ t < U, then we saythat the systemjumps from node Vito node vi at time t = T. A jump from Vito Vi canonly occur onthejump set

[Figure 256]

J;j = {x E R*: M+(x) = M;(x) = Mj(x)}. (78)

The Liapunov functional L(xJ moves the system throughthesedecisionhypersurfacesthroughtime. The geometryof S+,S-, andthejump setsJij,togetherwith the energydefined by L(xJ, can be usedto globally analyzethe dynamics of the system.In particular,due to the positive ignition property (77),the limit

LooM+(x(v»dv (79)

Jim L(x,) =

1-00 0

alwaysexists,and is possiblyinfinite.

The following resultsillustrate the useof theseconcepts(Grossberg,1978d):

[Figure 257]

TheoremI: Givenanyinitial data.x(O),supposethat

1'" M+(x(v»dv < 00. (80)

Then the limit x(oo) = lim,-+oox(t) exists.

[Figure 258]

[Figure 259]

Corollary I: If in responseto initial data x(0), all jumps ceaseaftersometime T < 00,thenx(oo)exists.

Speakingintuitively, this resultmeansthat after all localdecisions,orjumps, havebeenmadein response to an initial statex(O),thenthe systemcansettledown to a globaldecision,orCAM x(00).In particular,if x(0) leadsto only finitely manyjumps becausethereexists ajump tree, or partial orderingofdecisions,thenx(00) exists.This fact led to the analysisof circumstances under which no jump cycle, or repetitive series of jumps, occursin responseto x(0),andhencethatjump treesexist.

Furtherinformation followsreadilyfrom(80).Since

M+(.x(t» ~ 0 for all t ~ 0, it alsofollows that lim,-oo M+(.x(t» = O.This tells usto look for the equilibrium

points .x(00)on the positive ignition hypersurfaceS+ in (75):

[Figure 260]

Corollaryl: If f'if M+(.x(t»dt< 00,then.x(oo)ES+. Thus the positiveignition surfaceistheplacewhere

the competition both ignitesand is storedif no jump cycleexists.Usingthis result, ananalysiswasmadeof conditionsunderwhichnojump cycleexistsin response to anyinitial vector.x(O),andhenceall trajectoriesapproachan equilibrium or CAM state.

The same method was also usedto prove that a competitive systemcangeneratesustainedoscillations

[Figure 261]

if it contains globallyinconsistentdecisions.Theseresultsare important for understandingthe role of symmetric coefficientsin the designofCAM systems.They identified circumstancesunder which, in responseto initial data .x(O),

[Figure 262]

La) M+(x(v»dv = 00, (81)

thus that infinitely many jumps occur, hence a jump cycle occurs, and finally that the trajectory undergoes undamped oscillations.

This method was used to provide a global analysis of the oscillations taking place in the May-Leonard

(1975) model of the voting paradox. In this specialized Volterra-Lotka model,

- d
- di Xl = Xt(1 -XI -aX2 -fJX3)

- d
- di X2= x2(1 -fJXI -X2 -ax3)

did X3= x3(1 -ax, . -fJX2 -X3) (82)

[Figure 263]

and the parameters are chosen to satisfy fJ> 1> (Xand (X+ fJ> 2. System (82) representsthe following intuitive

situation. Three "candidates" are run against eachother in pairwise e1ec~ions.If VI wins over V2, V2wins over V3,and V3wins over VI, what happens when all three candidates run against each other? If the winning relationship were transitive, then VI could win over himself! Thus the voting paradox illustrates how a globally inconsistent decision scheme can arise.

In (82) the relationship "Vi wins over Vj" is represented by "Vi inhibits Vjmore than Vjinhibits Vi." In particular, VI> V2> V3> VI. May and Leonard (1975) did computer simulations which showed that the trajectories of(82) oscillate. Grossberg (1978d) proved that the trajectories oscillate because system (82) generates a globally inconsistent decision scheme, characterized by a jump cycle VI -V2 -V3 -VI with L(xoo) = 00, for almost all trajectories.

The interaction matrix

[Figure 264]

[Figure 265]

1 a fJ\

[Figure 266]

[Figure 267]

(83)

fJ 1 a

,a fJ 1

of system(82)canbechosenarbitrarily closeto asymmetric matrix by letting a and fJapproach I without violatingthe constraintfJ> I > a anda + fJ> 2.Thus thereexistcompetitivesystemswhosematricesarearbitrarily close to symmetric matrices almost all of whosetrajectories oscillate, albeit slowly. There also existcompetitivesystemswithout jump cycleswhose coefficientsare not symmetric, yet approachequilibrium points,becausetheysatisfyTheoremI. Although symmetry may be sufficientto generateCAM, as in model(13),the conceptsof jump cycleandjump tree

32 S. Grossberg

[Figure 268]

[Figure 269]

[Figure 270]

illustrate that one needsto analyzemore globalgeometrical conceptsto understandthe relationshipbetween a system's symmetry and its emergentCAM

valleyacts,in somerespects,like a classicalpotential. Correspondingly,it wasproved that after all the Xiget trapped in suchvalleys,the function

[Figure 271]

properties.

B[.x(t)]= max{bi(.x(t»: i = 1,2, ..., n} (87)

The Liapunov functional method led to the Cohen andGrossberg(1983)analysisin thefollowingway.The Liapunov functional methodwasusedto proveatheorem aboutthe globalCAM behaviorof thecompetitive adaptationlevelsystems

is a Liapunov function. This Liapunov property was usedto completethe proof of the theorem.

The adaptation level model (84) is in some ways more generaland in somewayslessgeneralthan model (13).Cohenand I beganour studyof(13) with thehope thatwecould usethe symmetric coefficientsin (13)to provethat no jump cyclesexist, and thus that all trajectoriesapproachequilibrium asaconsequenceofthe generalTheorem1. Sucha proofis greatlyto bedesired becauseit would be part of a more generaltheory and, by using geometricalconceptssuchas jump setand ignition surface,it would clarify howto perturb off the symmetriccasewithout generatingoscillationssuchas thevoting paradox(82).As it is,the Liapunov function ( 14)doesnot necessarilyrequire that the system(13) becompetitivebecause,by (18), (d/dt) Vi:s;0 whether or not the coefficients Cijare all nonnegative.

did Xj = aj(x)[bj(Xj) -c(x)] (84)

[Figure 272]

whichwereidentified through ananalysisof manyspecializednetworks.In system(84),eachstate-dependent

amplification function ai(X) and self-signalfunction bi(xJ canbe chosenwith greatgeneralitywithout destroying the system'sability to reachequilibrium becausethere exists a state-dependentadaptation level c(x) againstwhich each bi(Xi)is compared. Such an adaptationlevelc(x)definesastrongtype oflong-range symmetry within the system.

The exampleswhich motivatedthe analysisof (84) wereadditive networks

Hirsch (1982, 1985)has proved powerful global theoremsaboutthe classof cooperativesystems

[Figure 273]

[Figure 274]

(85)

did Xi = .fi(Xi. X2. Xn) and shunting networks where

[Figure 275]

[Figure 276]

(88)

[Figure 277]

[Figure 278]

|[Figure 279]<br><br>¥ ~ 0, i 10j. (89)<br><br>uXJ<br><br>One of the outstanding mathematical problems in neuralnetworktheoryisto find more generalmethods thanthe CohenandGrossberg,Grossberg,and Hirsch results for designing mixed cooperative-competitive feedbacksystemswith desiredglobalbehavior.|
|---|

[Figure 280]

-d Xj = -Ajxj + (Bj -x;)[Ij + L f~Xk)Ckj]

t k

[Figure 281]

-(Xj + D;)[Jj + L g~xk)Ekj]

(86)

k

[Figure 282]

in which the symmetric coefficientsBki, Cki,and Eki took on different valueswhen k = i and whenk + i.

Examplesin which the symmetric coefficientsvaried with Ik -il in a graded fashion were also studied through computer simulations (Ellias & Grossberg, 1975; Levine & Grossberg, 1976),but an adequate global mathematicalconvergenceproof wasnot availablebefore Cohenand Grossberg(1983).

[Figure 283]

12. STABLE PRODUCTION STRATEGIES FOR A COMPETITIVE MARKET

Thepropertiesof adaptationlevelsystemsmayprove usefulin areasfar removedfrom neural networks.To illustrate this possiblerange,considerthe problem of how to designa competitive market such that every competingfirm canchooseoneof infinitely manyproductionstrategies,eachchoiceis unknownto the other competitors,yetthe marketgeneratesa stablepriceand eachfirm balancesits books.

[Figure 284]

In the proof of the global convergencetheorem (Grossberg,1978c,1980a)forsystemsofthe form (84), it was shownthat eachXi(t)getstrapped within a sequence of decision boundaries that get laid down throughtime attheabscissavaluesofthe highestpeaks in thegraphsofthe functionshi. The sizeand location of thesepeaksreflectthe statisticalrules,which canbe chosenextremelycomplex,that giveriseto the output signalsfrom the totality of cooperatingsubpopulations within eachnode Vi. In particular, a hi with multiple peaks canbe generatedwhen a population's positive feedbacksignalfunctionis a multiple-sigmoidfunction which addsup output signalsfrom multiple randomly definedsubpopulationswithin Vi.

Let Xidenotethe amount producedby firm i ofthe commodity; p(x) denotethe market price per item of the commodity, whereX = (Xl' X2,..., Xn);Ci(Xi)de-

notethe costperitem of firm i; and Ai(x) (~ 0)denote a multiplier chosenby firm i. Let the firms agreeto governtheir individual production plans accordingto the adaptationlevelsystem

[Figure 285]

After allthe decisionboundariesgetlaid down,each Xi is trapped within a singlevalleyof its higraph.This

[Figure 286]

Nonlinear Neural Networks 33

[Figure 287]

Thecompetitivepropertyofthe marketisexpressedby the conditions

[Figure 288]

[Figure 289]

ap

[Figure 290]

[Figure 291]

<0, i=I,2,...,n. (91)

aXI

In order to play this market, eachfirm comparesits private costfunction with the publicly known market price. If A;(x) dependsonly on X;, thenthis is all that the firm needsto know to determine its production rate d.x;/dt.If A;(x) dependson amount xi produced by other firms, then eachfirm needsalsoto know how muchthe otherfirms areproducing. In eithercase,no firm knows the internal strategiesA;(x) and C;(x;) of the other firms, which canbe verycomplex. Nor does any firm needto know the function P(x), which can alsobeverycomplex.All it needsto knowarethevalues of P(x(t)) through time, which it can read in a trade newspaper.

[Figure 292]

Bythe adaptationlevelconvergencetheorem,limits limt-oo P(x(t)) andlimt-oo C;(x;(t))existandareequal. Thus the marketprice is stableand everyfirm breaks even.If the definition of C;(Xj)alsoincludesa savings factor,thenthesavingsfunctions of allthe firms would also besatisfied.

In this generality,the theorem does not saywhat firms will getrich. It only saysthat if firms arewilling to play the game, then they can attain some muchvaluedpropertiesof marketstabilityandpredictability. JustastheexistenceofstableCAM in neuralnetworks must besupplementedbya mathematicalclassification theory which determines who, if anyone, will win a speciallydesignedcompetition,theexistenceofastable market must be supplementedby an analysisof how firms shouldchoosetheir strategiesto maximize their gainsdespiteignoranceof theircompetitors'strategies.

Beforeturning to a discussionof somerecentspecializedarchitectures,I shallfurtherdiscusstwo issues that naturally arise from the precedingtext:

- 1. Why bother studying shunting interactions?Why aren't the simpler additive interactionsalwayssufficient?
- 2. Are symmetriccoefficientsnecessaryto achievestable learningand memorystorage?In Section11,it wasnoted thatthe answeris "no" for CAM systems whosestorageis in shortterm memory(STM). The answerisalsowell-knownto be"no" forassociative learningsystemswhosestorageis in long term memory(LTM). This is true for networksdesigned to accomplishassociativepatternlearningaswellas for networks designedfor spatiotemporalpattern recognition and planned sensory-motor performance. Some asymmetric associative networks which arise in adaptive pattern recognition and adaptive sensory-motor control are discussedin Sections16-20.

[Figure 293]

13. SENSITIVE VARIABLE-LOAD PARALLEL PROCESSING BY SHUNTING COOPERATIVE-COMPETITIVE NETWORKS: AUTOMATIC GAIN CONTROL AND TOTAL ACTIVITY NORMALIZATION

[Figure 294]

The value of shunting networks is clarified by their ability to help overcome one of the problems which hasconfronted recent investigatorswho have been using additive networks. Amit, Gutfreund, and Sompolinsky (1987, p. 2294) found spurious memory states in the additive model that they studied. Their analysis led

- them to conclude that "there must be some global control on the dynamics of the network, which prevents too high or too low activity." In other words, it is important to carefully regulate the network's total activation through time. The importance of this property, called total activity normalization, has beenrecognized in the neural network literature for the pasttwo decades, and is one of the basic properties of shunting cooperative-competitive networks (Grossberg, I970b, 1972a,

1973, 1982).

More generally, shunting networks provide a design for sensitive variable-load parallel processors. Suppose that the STM traces or activations Xl, X2, ..., Xnat a network level fluctuate within fixed finite limits at their respective network nodes. Setting a bounded operating range for each Xi has the advantage that fixed decision criteria, suchas output thresholds, can also be defined. On the other hand, if a large number of intermit~ent input sourcesconverge on the nodesthrough time, then a serious design problem arises, due to the fact that the total input converging on each node can vary wildly through time. I have called this problem the noise-saturation dilemma: If the Xi are sensitive to large inputs,

- then why do not small inputs get lost in internal system noise? If the Xi are sensitive to small inputs, then why do they not all saturate at their maximum values in response to large inputs?

Shunting cooperative-competitive networks possess automatic gain control properties capable of generating an infinite dynamic range within which input patterns can be effectively processed, thereby solving the noisesaturation dilemma. Specialized shunting networks have been classified in terms of their specific pattern processing and memory storage properties, thereby providing a storehouse of networks which serves as a

resource for solving particular computational problems. Sincf; the design and properties both of feedforward

and feedback shunting networks have been reviewed in a number of places (Grossberg, 1981, 1982, 1987d), the present summary considersbriefly only the simplest feedforward and feedback networks to convey some of the main ideas. First the simplest feedforward network will bedescribed to illustrate how it solvesthe sensitivity problem raised by the noise-saturation dilemma.

Let a spatial pattern Ii = (}iI of inputs be processed

,

[Figure 295]

34 S. Grossberg return to an equilibrium point (arbitrarily setequalto

[Figure 296]

by the cells Vi,i = 1,2, ..., n. EachOiis the constant relativesize,or reflectance,of its input Ij and I is the variable total input size.In otherwords, I = LZ=I Ik, so that LZ-l Ok= 1. How can eachcell Vimaintain its sensitivityto OiwhenI is parametricallyincreased?How is saturationavoided?

[Figure 297]

[Figure 298]

0) after all inputs cease.Theserules saythat

-dd Xj = -AXj + (B -x;}Ij -Xj L Ik' (92)

l k+j

If a fixed spatialpattern, Ii = OjIis presentedand the backgroundinput I is held constantfor awhile, eachXi approachesan equilibrium value.This value is easily found by settingdXi/dt = 0 in (92). It is

[Figure 299]

TocomputeOi= Ii(LZ=1Ik)-I, eachcellVimusthave information about all the inputs Ik, k = 1,2, ..., n. Moreover,since OJ= Ii(Ij + Lk+i Ik)-l, increasingIi increasesOiwhereasincreasingany Ik, k + i, decreases OJ.Whenthis observationistranslatedinto ananatomy for deliveringfeedforwardinputs to the cells Vi,it suggeststhat Ij excitesViand that all Ik, k + i, inhibit Vi. This rule representsthe simplestfeedforwardon-center off-surround anatomy(Figure 4a).

|Xj = 8j|[Figure 300]<br><br>AHI+ I|
|---|---|
|[Figure 301]| |

[Figure 302]

(93)

Note thatthe relativeactivity Xi = Xi(LZ=l Xk)-1equals 8ino matterhowlargeI ischosen;thereisno saturation. This isdueto automatic gain control bythe inhibitory inputs. In other words, Lk+i Ik multiplies Xi in (92). The total gain in (92)is found by writing

[Figure 303]

How doesthe on-centeroff-surround anatomyactivateand inhibit the cellsVivia massaction?Let each VjpossessB excitablesitesof which Xj(t) are excited and B -Xj(t) areunexcitedat eachtime t. Then at Vi, Ij excitesB -Xi unexcited sitesby massaction, and the total inhibitory input Lk+i Ik inhibits Xjexcited sitesby massaction. Moreover,excitation Xjcanspontaneouslydecayat a fixed rate A, so that the cell can

[Figure 304]

[Figure 305]

(94)

The gainisthe coefficientofXi, namely-(A + I), since if Xi(O)= 0,

[Figure 306]

[Figure 307]

[Figure 308]

(95)

[Figure 309]

Boththe steadystateandthe gain of Xidependonthe input strengths.This is characteristicof massaction, or shunting networks but not of additive networks. Many alternativemodelscannotretune themselvesin responseto parametric shifts in backgroundintensity.

[Figure 310]

The simple law (93) combinestwo types of information: information aboutpattern8j,or"reflectances," and information about background activity, or "luminance." In visual psychophysics,the tendencytowardsreflectanceprocessinghelpsto explainbrightness constancy,andthe rule /(A + /)-1 helpsto explainthe Weber-Fechnerlaw(Cornsweet,1970).

[Figure 311]

(a)

Another property of (93)is that the total activity

[Figure 312]

[Figure 313]

[Figure 314]

[Figure 315]

(b) ,

FIGURE 4. Two types of on-center off-surround networks: (a) A feedforward network in which the input pathways define the on-center off-surround interactions; (b) A feedback network in which interneurons define the on-center off-surround interac-

tions.

n

[Figure 316]

[Figure 317]

BI

X= LXk= k-1

A+I

[Figure 318]

(96)

is independentof the number of activecells.This normalization rule is a conservationlaw which says,for example,that a network that receivesa fixed totalluminance, making one part of the field brighter tends to makeanotherpart ofthe field darker.This property helpsto explainbrightnesscontrast(Cornsweet,1970; Grossberg& Todorovic,in press).Brightnessconstancy and contrastare two sidesof a coin: on one side is Weber-lawmodulatedreflectanceprocessing,asin (93), andonthe othersideisa normalizationrule, asin (96).

[Figure 319]

Equation (93) canbe written in another form that expressesa different physicalintuition. If we plot the intensity of an on-centerinput in logarithmic coordinatesKi, then Ki = In(Ii) and Ii = exp(Ki). Also write

[Figure 320]

Nonlinear Neural Networks 35

[Figure 321]

|[Figure 322]<br><br>the total off-surround input asJ; = Lk+;IkoThen (93) canbe written in logarithmic coordinatesas<br><br>xJK, .1,)= BeKt|
|---|
|[Figure 323]<br><br>--"--,, -" A+ K<br><br>How doesthe responseXjat Vichangeif we parametrically changethe off-surround inputJi? The answeris thatXi'Sentire responsecurveto Kjisshifted,andthus its dynamic rangeis not compressed.Sucha shift occurs,for example,in bipolarcellsoftheNecturusretina (Werblin, 1971)and in a modified form in thepsychoacousticdata of Iversonand Pavel(1981). The shift property saysthat<br><br>x;(Ki + S,J.i;1»= x;(K;,J.i;2» (98)<br><br>for all Ki ~ 0, wherethe amount of shift S causedby changingthe total off-surround input from ~I> to ~2> is predictedto be|

s =In(~ )

[Figure 324]

[Figure 325]

(99)

A +f2)i

[Figure 326]

14. PHYSIOLOGICAL INTERPRETATION OF SHUNTING MECHANISMS AS A MEMBRANE EQUATION

Equation (92) is a specialcaseof a law that occurs in vivo; namely,the membrane equation on which cellular neurophysiology is based. The membrane equation is the voltage equation that appearsin the Hodgkin-Huxley equationsmentioned in Section6C. This equationembodiesthe classicalelectricalcircuit interpretation (Hodgkin, 1964;Katz, 1966;Plonsey& Fleming, 1969)which is usedto physically interpret the additive and shunting neuralnetworks.

The membraneequationdescribesthe voltage V(t) of a cell by the law

###### av

[Figure 327]

Cai"=(V+- V)g++(V-- V)g-+(VP- V)gP. (100)

In (100), C is a capacitance;V+, V-, and V Pareconstant excitatory, inhibitory, and passive saturation points, respectively;and g+, g-, andgPareexcitatory, inhibitory, and passiveconductances,respectively.We will scaleV+and V- sothat V+> V-. Then in vivo V+ ~ V(t)~ V- and V+ > VP~ V-. Often V+ represents the saturationpoint ofa Na+channeland V- represents the saturation point of a K+ channel. There is also symmetry-breakingin (100)becauseV+ -VP is usually much largerthan VP-V-. This symmetry-breaking operation, which is usually mentioned in the experimental literature without comment, achievesan important noisesuppressionpropertywhenit is coupled to an on-centeroff-surround anatomy.

To seewhy (92) is a specialcaseof (100),suppose that (100)holds at eachcellVi' Then at Vi, V= Xi. Set C = 1(rescaletime), V+ = B, V- = VP= 0, g+ = Ii, g- = Lk+i Ik, and gP= A.

[Figure 328]

Thereflectanceprocessingand Weberlawproperties

(93),the total activity normalization property(96),and the shift property (98) setthe stagefor the designand classificationof more complexfeedforwardand feedback on-centeroff-surround shuntingnetworks.Some resultsclassifyingfeedforwardon-centeroff-surround networksare reviewedin Grossberg(1981, 1987d).

[Figure 329]

15. SIGMOID FEEDBACK, CONTRAST ENHANCEMENT, AND SHORT TERM

MEMORY STORAGE BY SHUNTING FEEDBACK NETWORKS

Feedback additive and shunting networks possess useful CAM properties that eventually led to the CohenGrossberg model reviewed in Section 9. During the last few years, many investigators have realized the importance of sigmoid feedbacksignals for generatingeffective pattern processing and CAM properties; (e.g., Ackley, Hinton, & Sejnowski, 1985; Hopfield, 1984; McClelland & Rumelhart, 1986). The first complete global analysis which rigorously demonstrated theseproperties was provided in Grossberg (1973). There the importance of sigmoid feedback was clarified by classifying the manner in which different types of feedback signal functions-linear, slower-than-linear, faster-than-linear, and sigmoid-transform input patterns and store th~ transformed patterns in STM. The simplest shunting on-center off-surround feedback network was chosen for this demonstration because it possessedthe key properties of: (a) solving the noise-saturation dilemma by using the interaction betweenautomatic gain control and on-center off-surround interactions, (b) normalizing or conserving its total activity, and (c) being capable of absolutely stable STM.

This simplest such network is defined by the equations

-dd Xi = -AXi + (B -xJ[li + [(XV] -Xi[Ji + l'[(Xk)],

[Figure 330]

t k+i

[Figure 331]

(101)

i = 1,2, ..., n (Figure 3b).Supposethat the inputs Ii and J; actingbeforet = 0 establishan arbitrary initial activity pattern (XI(O),X2(O),..., xn(O»before being shut off at t = O.How doesthe choiceof the feedback

[Figure 332]

signalfunctionf(w) control the transformation of this pattern at t -oo? The answeris schematizedin

###### Table3.

Table3displayschoicesofthe feedbacksignalfunction f(w) and the corresponding function g(w)

= w-lf(w) which measureshow much f(w) deviates from linearity at prescribedactivity levelsw.The network'sresponsesto thesechoicesaresummarizedusing the functionsXi = Xi(L~=1Xk)-1and x = L~=I Xk.The relative activity Xi of the ith node computeshowthe network transforms the input pattern through time.

###### 36

[Figure 333]

[Figure 334]

The functions X; play the role for feedbacknetworks thatthe reflectances8;in (93)playforfeedforwardnetworks.The total activity x measureshow wellthe network normalizesthe total networkactivityand whether the patternis stored(x( CX)= lim/_a) x(t) > 0) or not (x( CX)= 0). Variablex playsthe role ofthe total input I in (93).

Usingthesefunctions, (101)canbe rewrittenasthe

###### system

[Figure 335]

[Figure 336]

- (102)

[Figure 337]

and

[Figure 338]

- (103)

[Figure 339]

[Figure 340]

Usingsystem(102)-(103),the followingtypesofresults wereproved.

[Figure 341]

A. Linear Signal: PerfectPatternStorageandNoise Amplification

Iff(w) is chosenlinear,as inf(w) = Cw, then g(w)

= C = constant. Hence by (102), all dldt Xj = 0, so that Xj(t) = constantin responseto anarbitrary initial patternXj(O).This systemthus possessesa continuum of nondistortingCAM states.Why,therefore,is not a

[Figure 342]

S. Grossberg

[Figure 343]

linear feedbacksignala perfectchoicefor sensorypattern processing?

The answerbecomesclearthrough considerationof the total activity variablex(t). In the linearcase,(103) reducesto

[Figure 344]

[Figure 345]

(104)

[Figure 346]

Hence sucha systemeither cannot store any pattern (x( 00) = 0 if B -AC-1 < 0), or it amplifies noiseas

vigorouslyasit amplifiessignalsif it iscapableof CAM (x(oo) = B -AC-I ifB -AC-I > 0, no matter how small x(O)> 0 is chosen).This amplification property generalizesto othermodels,andchallengesthosemodels,suchastheBSBmodel(Section9B),whosefeedback signalsare linear at small activity values.

Equation(102)suggestshowto defineslower-thanlinear,faster-than-linear,and sigmoid feedbacksignals forpurposesof patternprocessing.Justasa linearf(w)

= Cw generatesa constant g(w) = C, a slower-thanlinearf(w), suchasCw(D+ W)-l,generatesa decreasing g(w), suchas C(D + W)-I; a faster-than-linearf(w), suchas Cwnwith n > I, generatesanincreasingg( w), suchas Cwn-l; and a sigmoid f(w), suchas Cwn(Dn + wn)-l with n > I, generatesa hill-shapedg(w), such asCwn-l(Dn + Wn)-l.

[Figure 347]

TABLE 3

[Figure 348]

|[Figure 349]<br><br>-XjlOQI -|
|---|
|f(w) g(w) Xj(oo)-ik Xk«x» X(oo)= ~kXk(oo<br><br>[Figure 350]<br><br>AMPLIFIES'liaiSE<br><br>[Figure 351]<br><br>AMPLIFIESfllOISE<br><br>|[Figure 352]|L|
|---|---|
| |[Figure 353]|
<br><br>[Figure 354]<br><br>QUENCHES INOISE<br><br>[Figure 355]<br><br>Ii'JOISE<br><br>[Figure 356]<br><br>[Figure 357]<br><br>[Figure 358]<br><br>|[Figure 359]|
|---|
<br><br>|[Figure 360]|
|---|
<br><br>[Figure 361]<br><br>[Figure 362]<br><br>|[Figure 363]|
|---|
<br><br>[Figure 364]<br><br>[Figure 365]<br><br>[Figure 366]<br><br>[Figure 367]|

QUENCHES

[Figure 368]

Nonlinear Neural Networks 37

[Figure 369]

- B. Slower-than-LinearSignal: PatternCompression andNoise Amplification

Slower-than-linearsignalfunctionsf(w) alsoamplify

noise.Analysisof(102) and (103)showsthat a slowerthan-linear feedbacksignalexertsa compressiveeffect onthe reverberatingactivity pattern which obliterates all differencesbetweeninitially active nodes(X;(CX)

= ~)if the networkis capableof CAM (x( CX)> 0).

[Figure 370]

- C. Faster-than-LinearSignal: Winner-Take-AIl, Noise Suppression,andTotal Activity Quantization in anEmergentFinite State Machine

[Figure 371]

A faster-than-linearsignalfunction cantell the differencebetweensmalland largeinitial valuesby amplifying and storing only sufficiently large activities. Analysis of (102) and (103) showsthat a faster-thanlinear signalfunction amplifiesthe largestinitial activities so much more than smaller initial activities that it makesachoice:Only the nodewith the largestinitial activity getsstoredin STM. This isa remarkableproperty from severalperspectives.

It shows how a very large network of nodes can quickly choosea winner in a single processingstep without anysearch,simplyby lettingits nodescompete. Choicenetworkswereoriginally designedforusein the many applications whereinthe computational taskis to choosea winner from noisydata. FeldmanandBallard (1982) havecalled this choice property winnertake-all. Platt and Hopfield (1986)have,for example, mentioned this property in their discussionof errorcorrectingcodes.

A faster-than-linearsignal function also generates remarkablenormalizationand quantizationproperties in thetotal activitydomain.Combinedwiththewinnertake-allproperty,the quantizationpropertyshowsthat a faster-than-linearsignalfunction generatesemergent propertiesofafinite-statemachine,eventhoughsystem (10I) is defined by continuous laws. In particular, at largetimes, (103)is approximatedby the equation

- d
- di x -x(-A + (B -x)g(x)]. (105)

[Figure 372]

[Figure 373]

Thus the stored total activity x( 00)is a root of the equation

[Figure 374]

A

[Figure 375]

[Figure 376]

g(w)=B-=-;

(106)

[Figure 377]

whereboth g(w) and A(B -W)-I are increasingfunctions of w. The storedtotal activity is normalized becausetheroots of(106) are independentofthe number n of competingnodes.

Total activity quantization and noise suppression

supplementthe normalization propertyif thefollowing hypothesesare satisfied.Supposethat A > Bg(O)and that there are m roots E1 < E2< ...< Em< B of equation(106).ThentherootsE1,E3,... areunstable

[Figure 378]

equilibrium points of x(t), whereasthe roots E2< E4 < ...are stableequilibrium points of x(t). RootE1 definesthe level below which x(t) is treated as noise and suppressed.Roots E2, E4, ...are stable,quantized, normalized limit valuesofx( CX).Functiong( w) canalsobe chosento equalA(B -w) alonganinterval of values,thereby leadingto a continuum of stable equilibrium values.Thus, one can use system(101) with a faster-than-linearfeedbacksignal function to designinfinitely manyfinite-statemachinesorcontinuous energy spectrum machines capable of rapidly making choicesin noiseand possessingas many normalizedasymptotic activity levelsasonepleases.

[Figure 379]

D. Sigmoid Signal: Tunable Filter, Quenching Threshold, Noise Suppression, and Normalization

Although a faster-than-linear signal function suppressesnoise, it does so with such vigor that only the node with maximal initial activity survives in CAM. In many applications, one needsa spatially distributed CAM code, albeit one that contrast-enhances and thereby compresses an input pattern before the transformed pattern is stored in CAM. A sigmoid signal function generates these properties. Indeed, the classification of signal function properties in (A)-(C) shows that a signal functionf( w)which suppressesnoise must be faster-than-linear at small activity values w. In addition, every physical signal function is bounded at large activity values w, thereby suggestingthe use of a hybrid signal function which is faster-than-linear at small activities, slower-than-linear at large activities, and thus, by continuity, approximately linear in between; viz., a sigmoid signal function (Table 3).

Grossberg (1973) proved that a sigmoid signal function generates a quenching threshold (QT): Activities less than the QT are suppressed, whereas the pattern of activities that exceedsthe QT is contrast-enhanced before being stored in STM. Speaking heuristically, the QT property is a consequence of pattern processing properties of faster-than-linear and linear signal functions combined with normalization properties in the total energydomain: The faster-than-linear property at small activity levels begins to contrast-enhance the input pattern as the total activity shifts due to normalization. As the partially contrast-enhanced activity pattern is normalized, it is influenced by the (approximately) linear range of the sigmoid signal function, which stores whatever pattern it detects (Table 3), including the partially contrast-enhanced pattern. Thus a sigmoid signal function can be usedto designa noisesuppressing network with infinitely many stable equilibri~m points, representing partially contrast-enhanced, or compressed, input patterns.

Any network that possessesa QT can be adaptively tuned. By increasing or decreasingthe QT, the criterion of which activities represent functional signals-and

[Figure 380]

38 S. Grossberg

[Figure 381]

[Figure 382]

henceshouldbeprocessedandstoredin STM-and of whichactivitiesrepresentfunctionalnoise-and hence

should be suppressed-can be flexibly modified throughtime. An increasein the QT cancauseall but the largestactivitiesto bequenched.Thenthe network behaveslike a choicemachine. A suddendecreasein the QT cancauseall recentlypresentedinput signals to be stored. If a novelor unexpectedeventsuddenly decreasesthe QT, then all recentlypresenteddata can be stored in CAM until the causeof the unexpected eventcanbedeterminedandlearned.This propertyis important in activelyregulatingthe focusof attention of a neural network sensory processor(Grossberg,

###### 1982).

It cannot be overemphasizedthat the existenceof the QT and its desirabletuning and CAM properties follow from theuseofa nonlinearsigmoidsignalfunction. When thesepropertieswere first proved in the early 1970s,the popularity of linear control models and of digital serialmodelsin applicationsto intelligent systemspreventedtheir acceptance,or ofteneventheir toleration. The recent popularity of connectionist modelsand of Liapunov methodshaveturned the obscureinto the obvious, which is a sure sign of major progress.

The QT has beenexplicitly computed in a special case(Grossberg,1973,pp. 355-359). In system(101) with Ii = Ji = 0, let

|[Figure 383]<br><br>f(w) = Cwg(w) (107)<br><br>whereC ~ 0, g(w) is increasingfor 0 ~ w ~ X(I),and g(w) = 1 forx(l) ~ w~ B. Then<br><br>nr = x(I) (lOR)|
|---|
|[Figure 384]<br><br>=- B-AC-1. ,---,<br><br>Thus all the parametersof the network influencethe QT. An important openproblemisto computethe QT of more generalcooperative-competitivenetworksthat arise in computationalapplications.<br><br>In summary, severalfactors work togetherto generatedesirablepatterntransformationand STM-CAM properties:the dynamics of massaction, the geometry of competition, and the statisticsof competitivefeedbacksignalswork togetherto definea unified network module whoseseveralparts are designedin a coordinated fashionthrough development.How sucha network module is self-organizedin vivo is a profound openproblemwhosesolutionis worthy ofa majorscientific effort. A great deal more mathematicalwork will alsobe neededto fully understandeventhe properties of those shuntingand additive networkswhich havealreadyarisenin applications.Forexample,mixed cooperative-competitivenonlinear feedbacknetworks havebeendesignedto analyzeand predict properties of emergentv.isualsegmentation(Grossberg,1987a, 1987b;Grossberg& Mingolla, 1985a, 1985b,1987). Although the computersimulations of thesenetworks|

[Figure 385]

wereguided by previoustheorems about competitive andcooperativenonlinearfeedbacknetworks,no global theoremshaveyet beenproved aboutthesemixed cooperative-competitivefeedbacknetworks. The additional insightsthat suchtheoremsare bound to bring are much to be desired if only becauseof the great practicalimportance of emergentvisual segmentation in a numberof applications.

[Figure 386]

16. COMPETITIVE LEARNING MODELS Another application of a choice network occursin

competitivelearning models. In the simplestcompetitive learning model, normalized input patterns pass

throughanadaptivefilterbeforethe maximal filteroutputischosenbya winner-take-allnetwork.Thewinning population then triggers associativepattern learning within the vectorof LTM traceswhich sentits inputs throughtheadaptivefilter. Suchacompetitivelearning model is a particular type of adaptive vectorquantizationscheme(Gray, 1984)which possessesBayesian processingproperties(Duda& Hart, 1973).In cognitive psychology,competitivelearningpropertiesareusedto model categorical perception (Anderson, Silverstein, Ritz,& Jones,1977;Elman, Diehl, & Buchwald, 1977; Hary& Massaro,1982;Miller & Liberman, 1979;Pastore, 1981; Sawusch& Nusbaum, 1979; Sawusch, Nusbaum,& Schwab,1980;Schwab,Sawusch,& Nusbaum, 1981;Studdert-Kennedy,1980).During categorical perception, input patterns are classifiedinto mutually exclusive recognition categorieswhich are separatedby sharpcategoricalboundaries. A sudden switch in pattern classificationcan occur if an input patternisdeformedsomuchthat it crossesoneofthese boundaries.

The developmentofcompetitivelearningmodelswas achieved through an interaction betweenresults of Grossberg(1970b, 1972b, 1973) and of Malsburg (1973), leading in Grossberg(1976a, 1976b)to the model in severalforms which havesubsequentlybeen further analyzedand applied by a number of authors (e.g.,Amari & Takeuchi, 1978;Bienenstock,Cooper, & Munro, 1982;Carpenter& Grossberg,1985,1987a; Grossberg, 1982; Grossberg & Kuperstein, 1986; Rumelhart& Zipser,1985).Kohonen(1984)hasmade particularly stronguseof competitive learningmodels in his work on self-organizingmaps. His important theorem on the statistical distribution of such maps extendsto the stochasticcasethe Grossberg(1976a) theorem on the stability of map learning in response to sparselydistributed input patterns.Kohonen'sanalysis of the distribution properties of a self-organizing map in the stochasticcasereflectsthe property in the deterministic casethat LTM vectors in the adaptive filter area time averageof their learned input vectors, and thus track the distribution of theseinput vectors within their convexhull undersuitableconditions.Such

[Figure 387]

Nonlinear Neural Networks

[Figure 388]

deterministicanalysesincludestochasticanalysesin the sensethat they predict the time courseof learning in responseto arbitrary sequencesof input patterns,including stochasticallycontrolled input patterns.A historical discussionof the developmentof competitive learningmodelsis givenin Grossberg(1987e).

Although competitivelearningmodelsare usefulin manysituations,theirlearningbecomesunstablein responseto a variety of input environments,aswasfirst shownin Grossberg(1976a).An effort to understand howto designanadaptivepatternrecognitionand map learning systemthat could self-stabilizeits learning in responseto arbitrary input environments led to the introduction ofadaptiveresonancetheoryin Grossberg (1976b). In this theory, competitive learning mechanismsareembeddedin a largernetworkwhichincludes learnedtop-downexpectationsand other modulatory mechanismsthat wereidentified through an analysis of data concerningperception, cognition, conditioning, attention, event-related potentials, and neurophysiology.

In addition to suggestingmechanisticexplanations of manyinterdisciplinary data from thesesubjects,the theoryalsomadea number of predictions which have sincebeenpartially supportedbyexperiments.Forexample,Grossberg(1976b)predictedthat both norepinephrine (NE) mechanismsand attentional mechanisms modulate the adaptive developmentof thalamocortical visual feature detectors. Kasamatsuand Pettigrew(1976)and Pettigrewand Kasamatsu(1978) describedNE modulation of featuredetectordevelopment and Singer(1982)reported attentional modulation. Grossberg(1978a)predicteda word lengtheffect in word recognition paradigms.Samuel,van Santen, andJohnston(1982,1983)reportedaword lengtheffect in word superiority experiments. Grossberg(1978a, 1980b)predicteda hippocampalgeneratoroftheP300

event-relatedpotential. Halgren etal. (1980)reported the existenceof a hippocampalP300 generatorin humans. The existenceand correlations betweenother event-relatedpotentials, suchas processingnegativity (PN), earlypositivewave(PI20), and N200 werealso predicted in thesetheoretical articles (seeBanquet& Grossberg,in press,for further discussion).

The next sectiondescribesa number of the key propertieswhichemergedfrom suchdataanalysesand subsequentmathematical developmentsand computational analysesof Carpenterand Grossberg(1985, 1987a).

###### 17. STABLE SELF-ORGANIZATIONOF PATTERNRECOGNITION CODES

[Figure 389]

[Figure 390]

A number of basic computational distinctions can be usedto differentiate neural network architectures andto clarify the applicationsfor which theyare best

39

[Figure 391]

[Figure 392]

suited. Sincea givencomputational property maybe advantageousfor one applicationanddisadvantageous for a differentapplication, sucha classificationis well worth keepingin mind.

In this section,I compareand contrastpropertiesof theadaptiveresonancetheory(ART) forthestableselforganizationof pattern recognition codeswith propertiesof alternativemodels for the learning of pattern recognition codes. Since ART was introduced in Grossberg(1976b), it hasundergonesubstantialdevelopmentandanalysis.A number of articleswhich contributed to the theory are brought togetherin several books(Grossberg,1982,1987c,1987d,1988).Thediscussionhereinwill bebaseduponpropertiesof anART architecture,called ART I, whosekeypropertieswere developed, proved mathematically, and illustrated through extensivecomputersimulations in Carpenter andGrossberg(1987a).Thearchitectureandprocessing cycleof ART 1 are summarized in Figures 5 and 6. The main computationaldistinctions to be discussed areoutlined underseparateheadings:

[Figure 393]

[Figure 394]

INPUT

PATTERN

FIGURE 5. Anatomy of the ART 1 architecture: Two successive stages, F, and F2' of the attentional subsystem encode pattems of activation in short term mel11ory (STM). Bottom-up and topdown pathways between F, and F2contain adaptive long term memory (L TM) traces which rrlultiply the signals in these pathways. The remainder of the circuit modulates these STM and LTM processes. Modulation by gain c:ontrol enables F, to distinguish between bottom-up input patterns and top-down priming, or template, patterns, as well as, to match these bottomup and top-down patterns. GElincontrol signals also enable F2 to react supraliminally to sign,als frorrl F, while an input pllttern is on. The orienting subsystem generates a reset wave to F2 when mismatches between bottom-up and top-down patterns occur at F,. This reset wave selectively and enduringly inhibits active F2 cells until the input is shut off. (Reprinted with permission from Carpenter & Gn)ssberg, 1987a, p. 56.)

40

[Figure 395]

[Figure 396]

- A. Real-Time (On-Line) Learning Versus Lab-Time (Off.;Line) Learning

An ART architecture is designedto run in real-time, or on-line, when it is implemented in hardware. Various other architectures can only be run in lab-time, or offline. This is perhaps the most important distinction that separates neural network architectures. Although some problems, suchasthe traveling salesmanproblem (Hopfield & Tank, 1985, 1986), can be run off-line, other problems, such as learning to recognize novel objects in a rapidly changing environment, must be solved on-line. Many of the computational properties which set apart ART architectures from other currently available learning algorithms are imposed to enable them to learn and recognize well in real-time.

[Figure 397]

- B. NonstationaryUnexpectedWorld Versus StationaryControlled World

Real-time environments ar~ often nonstationary; their statistical properties can change unexpectedly through time. In addition, the world doesnot stopin a real-timeenvironment. A ceaselessflowof input patterns of variable complexity canoccur.ART architectures are designedto copewith nonstationaryworlds of unlimited complexity. In contrast,manyalternative learning and recognition schemesare off-line models that work well only in a stationaryworld whoseinputs are carefullycontrolled both in numberand statistical properties.The followingdiscussionsharpensthis basic difference.

[Figure 398]

D. Self-Stabilization Versus Capacity Catastrophe

An ART architecture can self-stabilize its learning in responseto arbitrarily many inputs. New inputs may either refine the criteria for accessingalready established recognition codes, or may initiate the learning of a new recognition code, until the full capacity of the architecture is utilized. Input patterns which cannot refine prior knowledge, or which are first experienced after full capacity is utilized, are rejecte~ by the architecture's self-stabilizing mechanisms.

In architectures which cannot self-stabilize their learning, later input patterns can wash awaythe learning of prior input patterns, leading to an unstable cycle of learning and forgetting. These architectures include essentially all the classical versions of autoassociators, competitive learning mechanisms, and steepestdescent algorithms such as back propagation.

Effective use of a non-self-stabilizing architecture depends upon results which estimate the architecture's capacity. The capacity estimates the maximum number of input patterns which the architecture can learn, recognize, or remember. Typically, an autoassociator's capacity is -.15n, where the autoassociator's memory is defined by an n X n matrix (Anderson, 1983; Hopfield, 1984; Kohonen, 1984; McEliece, Posner, Rodemich, & Venkatesh, 1980; Psaltis & Park, 1986; Venkatesh, 1986). Thus an autoassociator cannot effectively use its full capacity. Moreover, if the number of input patterns exceedsthis capacity, a capacity catastrophe occurs which rendersthe architecture's output unreliable. Such non-self-stabilizing architectures are thus inherently off-line machines whose lab-time world of inputs is under strict control. In an ART architecture, estimates of capacity playa different role than in an autoassociator or steepest-descentalgorithm, since no catastrophe occurs when the input world contains more patterns than the architecture can encode.

[Figure 399]

- C. Self-OrganizationVersusTeacherasa Sourceof ExpectedOutput

[Figure 400]

An ART architecture self-organizes its recognition code, without a teacher, through a direct interaction with its input environment. Self-organizing networks contrast sharply with learning networks which require an external teacher who presents an explicit correct answer, in the code of the network, for comparison with every output generated by the network, as in back propagation. Back propagation usesthe Adeline learning rule of Widrow (1962). It is a steepest descent algorithm which was discovered by Werbos (1974), rediscovered and further developed by Parker (1982, 1985, 1986) under the name learning-logic, and popularized and applied to cognitive science applications by Rumelhart, Hinton, and Williams (1986) under the name back propagation.

The off-line nature of back-propagation, at least as it is used in many applications, is illustrated by the fact that its teaching signals often haveno analog with analogous learning experiences in vivo. For example, the popular NETtaik back-propagation simulation of Sejnowski and Rosenberg (1986) uses a phoneme-by-

[Figure 401]

S. Grossberg

[Figure 402]

phonemematchingschemethat hasno analogduring human real-time learningto read. The use of sucha pre-codedteacheralsohas major implications for the structure of the learned code-notably the invariants of this code(seeitems F and G below)-and the way in whichmatchingoccurswithin the network(seeitem H below).

[Figure 403]

E. Maintain Plasticity in an Unexpected World Versus Externally Shut Off Plasticity

An ART architecture retains its plasticity, or ability to learn, for all time; that is, the parameters which enable its adaptive weights, or long-term memory (LTM) traces, to learn are not switched off as time goes on. The self-stabilization property is due to a dynamic buffering schemewhich protects these LTM traces from changing except during appropriate circumstances.

[Figure 404]

Nonlinear Neural Networks 41

[Figure 405]

[Figure 406]

I

[Figure 407]

[Figure 408]

[Figure 409]

[Figure 410]

###### I I

[Figure 411]

FIGURE 6. Search for a correct F2 code: (a) The input pattern I generates the specific STM activity pattern X at F, as it nonspecifically activates A. Pattern X both inhibits A and generates the output signal pattern S. Signal pattern S is transformed into the input pattern T, which activates the STM pattern Y across

F.; (b) Pattern Y generates the top-down signal pattern U which is transformed into the template pattern V. If V mismatches I at F" then a new STM activity pattern X' is generated at F,. The reduction in total STM activity which occurs when X is transformed into X' causes a decrease in the total inhibition from j~,toA; (c) Then the input-driven activation of A can release a nonspecific arousal wave to F2, which resets the STM pattern Y at F.; (d) After Y is inhibited, its top-dow1n template is eliminated, and X can be reinstated at F,. Now X once again generates input pattern T to F., but since Y remains inhibited T can activate a different STM pattern Y' at F.. If the top-down template due to Y* also mismatches I at F" then the rapid search for an appropriate F. code continues. (Reprinted with permission from Carpenter & Grossberg, 1987a, p. 61.)

[Figure 412]

Thus, if an unfamiliar eventoccursat anytime in the future, anART architecturecanlearnaboutit, without destabilizingits prior knowledge,just so longas it has not alreadycommittedits full capacityto priorlearning.

In contrast, if a non-self-stabilizingarchitectureis exposedto a never-endingtime-seriesof input patterns, as in vivo, then it will experiencea fatal capacitycatastropheunlessits plasticity is shutoff; that is, unless the parameters of its individual LTM traces are switchedto a no-learningmode by an external or internalizedteacher.

Sucha switching-offof plasticitydoesnot work well in nonstationary environments whosepropertiesare not predictable in advance.If learningis switchedoff too soon,thenimportant latereventscannotbelearned. Iflearning isswitchedofftoo late,thenimportant earlier learning maybewashedawaydueto a capacitycatastrophe. An omniscientteacheris neededto switchoff

[Figure 413]

learning atjust the right time in responseto an arbitrary input environment. If an effective model of an omniscient teacher is available, however, then a potentially unstable learning device will not be needed.

[Figure 414]

F. Self-ScalingComputationalUnits

An ART architecture can learnto distinguisharbitrary pairsof input patterns.In contrast,a number of alternative recognitionarchitecturesdependupon orthogonality, linear predictability, or other statistical constraintson input patternsin orderto function well. In orderto achievethis property,an ART architecture self-scalestheprocessingofits inputpatterns.Individual input featuresareautomaticallygivenlessweightwhen theyoccurwithin more complexinput patterns.A side benefitofthis type offeaturenormalizationis thatsufficientlysmallnoisychangesin a complexinput pattern may not forcerecodingof the pattern.

Asa resultofthe self-scalingproperty,an input feature maybeencodedin LTM whenit occurswithin a simple input pattern, yetbe rejectedfrom LTM when it occurswithin a complexinput pattern. In the former case,the input feature becomesa critical feature by beinglearnedbythe LTM codethathelpsto recognize thepattern.In the lattercase,the input featurebecomes a noiseelementby beingdeletedfrom the LTM code that helpsto recognizethe pattern. This decisiondependsupontheentire history of learning that hasprecededthe presentationof an input pattern which contains the feature.Thus, the conceptof critical feature is an emergentproperty of the network rather than a property which canbe defined solelyby choice of an input filter.

[Figure 415]

G. Learn Internal ExpectationsVersusImpose ExternalCosts

An ART architecture learnsits own top-downexpectationsasa function of the unique input environment to which it is exposed.Theseexpectationsare emergentinternal representationswhich capture invariant statisticalproperties of the entire input environment. Suchlearned top-down expectationsare a keyingredientof ART architectures.They function as prototypes for anentire recognitioncategory,and apstractly encode the similarity properties which are sharedby all exemplarsof the category.On the other hand, the manner in which these expectationsare learnedandmanipulatedsetsthem apartfrom classical prototypeideas.Theymayalsobeinterpretedas"costs" which the architecturelearns for itself, suchthat differentcostsare learned in responseto different input environments(Figure 7). In order to avoid misinterpretations of theseexpectationsdue to suchanalogies with previousideas,Carpenterand Grossberg(1987a) havecalled them criticalfeature patterns.

[Figure 416]

[Figure 417]

In contrast,architectureswhich usean external teacheroften representthis teacheras a set of target patterns,or externallyimposedcosts.In NETtalk, for example,the mismatchbetweena targetphonemeoutput codeand the actualphonemeoutput codeis used to drive learning at all the model's stages,from the visual representationof input letters to the auditory representationof output phonemes.Thus, anauditory mismatchis usedto determinethe learnedproperties ofa visualcode.In vivo, bycontrast,manyobjectscan be visually recognizedbasedupon visual invariants, evenif the objectshaveno names;for example,the familiar faceofa check-outpersonatthe supermarket. The verbalphrase"check-outperson"doesnot determine howwe visually recognizesucha person'sface,

[Figure 418]

S. Grossberg

[Figure 419]

any more than wewould visually recognizethe same facedifferentlyif the samejob wererenamed"cashier attendant."

In ART, self-organizationof invariantcritical feature

patternscan occur within eachmodality beforeintermodality transformations betweenthese invariants, suchas betweena visual representationof a faceand an auditory representationof a name,are learnedvia associativemechanisms(Grossberg,1978a,1982).

[Figure 420]

H. Active Attentional FocusingandPriming Versus PassiveWeightChange

A top-downlearnedexpectationin ART is actively matched against bottom-up information (Figure 6).

|[Figure 421]<br><br>(8) TOP-DOWNTEMPLATES<br><br>1 ABU A1 2 3 4 5<br><br>RES<br><br>2 e Fc<br><br>RES<br><br>3 C i P = .5<br><br>RES<br><br>4 D i<br><br><br>RES<br><br>sE iE<br><br>1 RES|
|---|

|[Figure 422]<br><br>(b) TOP-DOWN TEMPLATES<br><br>1 Rau R1 2 3 4 S 6 7 B 9 10<br><br>RES<br><br>2 B Fc RES<br>3 t: Fct: P = .8<br><br><br>1 RES<br><br>40 Fct:O<br><br>2 1 RES<br><br><br>sE Fc[:OE<br><br>:5 1 2 RES|
|---|

[Figure 423]

|[Figure 424]<br><br>6<br>7 a<br><br><br>9<br>10<br><br><br>[Figure 425]<br><br>F<br>G<br>H :I<br><br><br>r|[Figure 426]<br><br>[Figure 427]|[Figure 428]<br><br>sF F[:DE<br><br>RES<br><br>7~ F[:DE<br><br>1 RES<br><br>8H F[:DEH<br><br>1 4 J 2 RES<br><br>9:[ F[:DZH<br><br>1 RES<br><br>10J' F [: D ~ H<br><br>RES| |
|---|---|---|---|
|[Figure 429]<br><br>11K r I.: I'<br><br>RES<br><br>12L rl.I'RES<br>13M r I .I' M<br><br><br>2 1 RES 14N rl.I'M, RES 15crl.I'MRES| | |[Figure 430]<br><br>11K F [: D ~ to:<br><br>RES<br><br>12L. F L. D ~ to:<br><br>RES<br><br>13M F L D ~ to:M<br><br>4 2;5 1 RES<br><br>14NFL. D ~ to:H<br><br>RES<br><br>15C F L. D~ to:H<br><br>RES|

[Figure 431]

###### 16P r I , J' tol 16P F L. D ~ ..: N P

[Figure 432]

RES 1 ,6 5 3 2 "RES

###### 17m r I , J' H 17m F L. D ~ ..: N P m

1 2 RES 7 2 1 3 5 " 6 RES

###### 18R r I , J' 1'1 18R F L. D ~ ..: tolP m

RES RES

###### 195 r I ,~ 1,1 195 F L. D ~ ..: N P 5

1 2 RES 2 3 5 1" 6 RES

###### 20T r I , T H 20T F L. D ~ ..: N P 5 T

RES 3 5 1 " 2 RES

FIGURE 7. Alphabet learning: Code learning in response to the first presentation of the first 20 letters of tlhe alphabet is shown. Two differel1lt vigilance levels were used, (a) p = .5 and (b) p = .8. Each row represents the total code that is learned after the letter at the left-hl~nd column of the row is presented at F,. Each column represents the critical feature pattern that is learned through time by the F2 node listed at the top of the column. The critical feature patterns do not, in general, equal the pattern exemplars which change them through learning. Instead, each critical feature pattern acts likE!a prototype for the entire siet of these exemplars, as well as for unfamiliar exemplars which share invariant properties with familiar exemplars. The simulation illustrates the "fast learning" calse, in which the altered LTM traces reach a new equilibrium in response to each new stimulus. Slow learning is more gradual than this. (Reprinted with permission from Carpenter & Grossberg, 1987a, p. 72.)

[Figure 433]

Nonlinear Neural Netl1'orks 43

[Figure 434]

[Figure 435]

This matchingprocesstakesplacewithin a processing stage,or level,and can rapidly reorganizethe activations, or short-term memory (STM) traces, that are computed at the nodesof this stage.In particular, a toP-downcritical featurepatterncanprime a lowerlevel to getreadyfor an exemplarfrom anexpectedclassof input patterns. It can amplify and therebyspeedup processingof an input pattern that belongsto an expected class,while it actively reorganizesthe information processingof this input. A top-downexpectation canalsoattenuateprocessingof unexpectedinputs througha mismatchbetweenthe bottom-up input and the top-downexpectation.

In this way,a top-downexpectationenablesanART architecture to function like an intentional machine that generatesanactivefocusof attention. In contrast, the top-down mechanismsof a teacher-drivenarchitecture such as back propagationdoes not" directly prime the system,or focusits attention, or reorganize its fastinformation processing.Insteadback propagation merely causesslow changesin the bottom-up adaptiveweightsof the network(Figure 8).

- I. ClosingVersusOpeningthe Fast-SlowFeedback Loop

The botto~-up and top-down interactions in an ART architectureclosethe feedbackloop betweenfast activationsat networklevelsand slowerlearnedchanges in the pathwaysbetweenlevels(Figure 6). This fundamentalpropertyis whatenablestheARTarchitecture to learn stably in real-time. In contrast, back propagationopensthis feedbackloop(Figure8),whichmakes this network easierto understandbut computationally lessrobust.

[Figure 436]

- J. ExpectantPriming VersusGrinding All Memory Cycles

Dueto theclosedfeedbackcyclein ART,a top-down prime that is lockedinto STM by a largegain control signalcanpreventanyinput that is not in theexpected recognition categoryfrom activating higher levels of the architecture,muchasthe verbalcommandto look for orangesenablesone to avoid beingtoo distracted by otherobjects.

In contrast,anarchitecturewithout a top-downexpectationcapableof activelysuppressingmismatched exemplarswill becomefully engagedby any input patternsthat mayhappento occur.Its memorycyclesmay thus be so fully engagedby irrelevant inputs whena crucial eventoccursthat it cannotrespondin time.

[Figure 437]

terns while prototypically deforming and amplifying matchedinput patterns,anART architecturelearnsin the approximate match phase.In other words,if an input patterncausesthe read-outofa learnedtoP-down expectationwhich matchesit well enoughto preventa resetevent,then the matching processselectsthe information that is consistentbetweenthe input andthe expectation.If thesematcheddata include novelelements,theyareusedto refinethe learnedcodeof that recognitioncategory.In otherwords,if thecompressed recognitioncode,orhypothesis,generatedbythe input patterndoesnot causeresetdueto read-outof its topdownexpectation,thenthearchitecturedeemsthis input patternto beconsistentenoughwith thathypothesis to refine or updatethe hypothesisbasedupon anyadditional information that the pattern maycontain. If resetdoesoccur and leadsto selectionof an uncommitted code, then this codelearnsa completerepresentationofthe input pattern, whichis intuitively reasonablebecausethe pattern could not be assimilated into any previouslylearnedcode.

Becausean ART architecturelearnsin the approximate match stage,it is not degradedby noise fluctuating at its input level.If a noisepatternis verydifferentfrom its learnedcodes,the architecturedynam-

[Figure 438]

- K. Learning in the Approximate Match Phase Versusin the Mismatch Phase:HypothesisTesting Avoidsthe Noise Catastrophe

[Figure 439]

Due to its possessionof learnedtop-downexpectations which actively suppressmismatched input pat-

[Figure 440]

[Figure 441]

FIGURE 8. Circuit diagram of the back propagation model: In addition to the processing levels F" F2' F3' there are also I,evels F., Fs, F6' and F7 to carry out the computations which control the learning process. The transport of learned weights from the F2 -+ F3 pathways to the F. -+ Fs pathways show that this algorithm cannot represent a learning process in the brain. All feedback within the levels F, -+ F2 -+ F3is expressed through learning signals which slowly change bottom-up adaptive weights but do not quickly reorganize the network's fast information processing.

[Figure 442]

[Figure 443]

ically buffcrsthesecodesagainstrelearningandselects an uncommitted codeto learn the noise. If the noise

doesnot repeatitself often enoughand learning proceedsslowly,thenoisewill notcausesignificantlearning within the uncommitted code.It will not, in anycase, interferewith thecodesof sufficientlydifferentpatterns evenif learning proceedsquickly.

Architectureswithouta fast-slowfeedbackloop,such asback propagati<;Jn,aredesignedso that learningoccurs in the mismatchmode.Thus if noisecanactivate theteacher,or expectedoutput stage,thenall the LTM traces of the architecture can eventuallybe recoded. This noisecatastrophecanbepreventedonlyif thenoise is infrequentandlearningisslow.InART, evenfrequent noiseis simply treatedasa newsourceof input that doesnot endangerthe corpusof previouslylearnedinformation.

Althoughlearning in the mismatchphasecancause a noisecatastrophein anarchitecturewhichisdesigned to learn a recognitioncode in real-time, it is a useful type of learning in a numberof alternativesituations, notably during adaptive sensory-motorcontrol (see Sections18-21).

[Figure 444]

L. Fastor SlowLearning:The Oscillation Catastrophe

Anotherconsequenceoflearningin theapproximate match phaseis that ART can learn at eithera fastor slowrate. Fastlearning occurs wheneachLTM trace canreacha newequilibrium valueona singlelearning trial. Successivelearning trials mayor may not cause the LTM traceto assumedifferentequilibrium values. Slowlearning mayrequire manytrials beforethe LTM tracesreachany equilibrium point of the system.

When learningoccursin the mismatchphase,asin back propagation, fastlearning cancausewild oscillations to occur in the network's LTM traces,since eachmismatch can dragthe LTM tracesto a totally differentregionofphasespace.Thus sucharchitectures must learn slowly, which emphasizestheir off-line character.Contrastthevivid recollectionof anexciting movie after one-trialon-line learning in vivo.

[Figure 445]

M. Self-AdjustingParallel Memory Searchand Global EnergyLandscapeUpheavalVersusSearch Treesand Local Minima

Learning in theapproximate matchphasecouldbe disastrouswere it not for the existencein ART of a self-adjustingparallel memory searchthat maintains its efficiencyasthe learnedcodebecomesmore complex. When an input patterncausesread-outof a topdown expectationwith which it cannot form an approximate match,the attenuationof activitydueto the mismatch event resetsthe compressedcode, or hypothesis,that causedthe mismatch(Figure6c). A par-

[Figure 446]

S. Grossberg

[Figure 447]

allel memory searchis herebytriggered that rapidly testsa seriesof suchhypotheses.This hypothesistesting schemeactively and globally reorganizesthe energy landscapeofthe architecture.In this way,the architecture circumventsthe problem of localminima thathas plaguedalternativearchitectures~uchasautoassociators,simulatedannealing,andthe Boltzmannmachine.

The needto escapelocalminima hasinfluencedthe designof all content-addressablememoryandlearning architectures.Architectures which do not possessselfadjustinghypothesistestingschemestypically usetwo alternativeapproaches.In autoassociators,simulated annealing,and the Boltzmann machine, noiseis used to helpthe classificationto jump out of a local minimum. Sucha schemedoesnot globallyreorganizethe energylandscapebaseduponthe outcome ofactiveinformationprocessing.Insteadthe nonspecificactionof noisetries to exploit the fact that the localminima of a fixed energylandscapemaybe easierto escapethan a global minimum, and that a nonspecific external temperatureparametermaybeusedto control therate of approachto equilibrium.

Steepest-descentmethods,suchasbackpropagation, usea mismatchto drag the system'sLTM tracesout of local minima, and do so slowly enoughto reduce the potentiallydestabilizingeffectsofthe oscillationcatastrophe.

Traditional AI architectures often include search

trees to escapeerroneousclassifications.Although a searchtree maybe efficientat onestageof learning, it cannotremain efficientat anarbitrary stageoflearning unlessit hasa self-adjustingcapability, as in ART.

N. Rapid Direct AccessVersusIncreaseof Recognitionlime with CodeComplexity

[Figure 448]

In ART, aslearning self-stabilizesin responseto a set of input patterns,the searchmechanismis automaticallydisengaged.Thereafterrapid direct accessto the recognitioncodeoccursin responseto familiar input exemplarsaswellasto novelexemplarsthat share invariantpropertieswith familiar input exemplars.Direct accessoccurs becauseread-out of the top-down expectationof a familiar input patternalwaysleadsto anapproximatematch(Carpenter& Grossberg,1987a). Thenthe initial bottom-up eventthat led to top-down readout(Figure 6) cangeneratea resonantrecognition eventwithout causingreset.Thus anART architecture reconcilesthe ostensiblyconflictingdemandsof direct accessandsearch.It usesresetand self-regulatingsearch to build globallyself-consistentrecognitioncodeswhich avoid localminima in responseto arbitrarily complex time-seriesof input patterns. It usesdirect accessto recognizefamiliar eventswith a speedas fastasone's hardwarecanrun.

In contrast, an AI architecture with a searchtree takeslongerandlongerto recognizeaneventasit needs

[Figure 449]

Nonlinear Neural Networks 45

[Figure 450]

[Figure 451]

to searchmore and more codes.If this werethe case in vivo, it could take orders of magnitudemore time to recognizeour parents whenwe were 30 yearsold than it did whenwewere5 yearsold. Fortunately,this is false.

[Figure 452]

- O. AsynchronousVersusSynchronousLearning

In ART 1, eachLTM trace oscillatesat mostonce through time in responseto an arbitrary time-seriesof binary input patterns(Carpenter& Grossberg,1987a). Wereit not for the architecture'sactivereorganization ofthe energylandscapethroughhypothesistesting,this remarkable monotonicity property could easilycause the architecture to learn a local minimum. As it is, .learningisallowedto occuronly whenthe energylandscapereachesa configuration that leadsto anapproximate match. Due to theseproperties, an ART I architecturecanlearnasynchronouslyorsynchronously: If input patternscome in too quickly to generatean approximate match or to terminate a search,then no learning occurs. If the input pattern stays on long enough for somelearning to occur, then it does not mattertoo much how long it stayson because,due to the monotonicity property, the LTM traces will tend to changein the samedirection no matter howlong it stayson.

In contrast, if mismatchdrives learning in sucha way that eachLTM trace canoscillate persistentlyas it approachesequilibrium, then variable durations of the input patternsmaydestabilizethelearningprocess.. The limiting caseof this propertyis the oscillationcatastrophe,which occursif sufficientlymany input patternsstayonlongenoughfor LTM tracesto reachequilibrium on eachsuchlearningtrial.

[Figure 453]

Q. Towardsa General-PurposeMachine for CognitiveHypothesisTesting,Data Search,and Classification

.In ART, adaptive pattern recognition is a form of hypothesisdiscovery,testing,learning,and recognition in responseto a nonstationaryinput environment.This propertywould seemto be essentialfor any cognitive theory which hopesto understand how ever-morecomplexknowledgeinvariants are discovered,tested, and recognized,at any levelof abstraction.

In particular,future ART machinesmaybedesigned to learn,search,andclassifycomplexhierarchicallyorganizeddatafiles.The propertiesofautomaticself-stabilization and self-scalingwill be essentialfor suchan architectureto work reliablyandquickly onenormous data bases.The advantagesof such a self-organizing systembecomegreaterasthe datasetsarechosenlarger, becausethe decisiontaskfor hand-sortingsomuchdata or the discoveryof rules for automatically sorting all thedata, especiallywhen newdataareaddedlateron, rapidly becomeunmanageablydifficult as a function of scale.

The postulatesof ART thusdefineaclassof models for a broad range of cognitive scienceapplications, whichincludeexamplesthat mayor maynot evenpossessan orienting subsystemand search mechanism (Figure 5), as discussedby Carpenterand Grossberg (in press).McCl.elland(1987)hasproposedthatmodels of this classbe renamed the "interactive activation framework" afterthe interactiveactivation modelthat wasintroduced by McClelland and Rumelhart (1981) and RumelhartandMcClelland(1982).Thepostulates of theinteractiveactivationmodelare,however,inconsistentwith thoseof an ART model.The postulatesof the interactiveactivation modelhavebeenabandoned in favorofARTpostulatesbecausetheyareinconsistent with keycognitivedata and possesssomeundesirable computationalproperties,asnoted in Grossberg(1984, 1986,1987e).SinceART wasanestablishedcognitive theory(Grossberg,1978a,1980b)beforethe interactive activation model waspublished, it seemshistorically and scientificallyjustified to retainthe nameAdaptive ResonanceTheory for suchmodels.

[Figure 454]

- P. Discriminative Tuningvia Attentional Vigilance

Although an ART architecture self-organizesits learning, it can betuned by environmental feedback to learn coarseror finerdiscriminations; that is, it can learn to categorizethe samesetof input patternsinto largeror smallergroupingsdependinguponhowstrictly

arethe performanceimposed. demandsofthe external.environment

Suchenvironmentalfeedbackactsto changea single parameter of the network that is called the vigilance parameter(Carpenter& Grossberg,1987a).This parameter determines how fine the mismatch between bottom-up input and top-downexpectationmustbe in orderto resetthe codewhich reads-outtheexpectation. A largevigilance parameterdemandsa highdegreeof matchto preventreset,hencefinelycategorizesthe input patterns. A small vigilance parametertolerates larger mismatchesbefore forcing reset, hence more coarselycategorizesthe input patterns.

This tuning parameterdependsforitsexistenceupon the fact that bottom-up and top-downmatchesoccur as part ofthe real-time feedbackcyclethat determines

[Figure 455]

the classificationof input patterns.In particular, it can changedramatically the global reorganizationof the energylandscapethat regulatesself-regulatingsearch andlearningby modifyingthe overallattentiveness,or sensitivity,of the circuit.

[Figure 456]

18. INTERNALLY REGULATED LEARNING AND PERFORMANCE IN NEURAL MODELS OF SENSORY-MOTOR CONTROL: ADAPTIVE VECTOR ENCODERS AND COORDINATE TRANSFORMATIONS

In manyre~l-time nonlinear neural networkarchitecturesotherthanART architectures,learningis reg-

+

[Figure 457]

[Figure 458]

[Figure 459]

(a)

[Figure 460]

[Figure 461]

###### ..

[Figure 462]

[Figure 463]

[Figure 464]

(b)

[Figure 465]

FIGURE 9. (a) Learning in sensory-motor pathways is gated by a difference vector (DV) process which matches target position command (TPC) with present position command (PPC) to prevent incorrect associations from forming between eye-head TPCs and hand-arm TPCs; (b) A GO signal gates execution of

[Figure 466]

S. Grossberg

[Figure 467]

ulated by pattern matchesand mismatches. For example, learning of intermodality associativemapsbetween the target position commands of different sensory-motorsystems(Figure 9a)is gatedon and off by intramodality patternmatchesand mismatches,respectively.Thesesamematching processestransform automatically sucha target position command into a synchronousmultijoint trajectory which automatically compensatesfor variable initial positions in a manner that quantitativelyexplainsa largebody of data about human and monkey arm movements (Bullock & Grossberg,in press-a).Thus just as in an ART model, modelneuralarchitectureswhich havebeenidentified for the learning and performance of arm movements use internal matching processesto regulate both the fastinformation processingandthe slowerlearning of the system.

The circuit depicted in Figure 9 schematizeskey processingstagesin a VectorIntegrationto Endpoint, or VITE, circuit. In its simplestform, the VITE circuit obeysthe equations:

DijJerence Vector

did Vi = a(-Vi + Ti -P;) (109)

[Figure 468]

and

PresentPositionCommand

[Figure 469]

|[Figure 470]<br><br>(110)|
|---|

where[V;]+ = max(V;, 0). Equations (109)and (110) describeagenericcomponentofa targetpositioncommand (TI, Tz, ..., Tn),a difference vector (VI, Vz, ..., Vn),anda presentpositioncommand(PI, Pz,..., Pn)in responseto a time-varying velocity command, or GO signalG(t);seeFigure9b. The differencevector computes a mismatch between target position and presentposition,andisusedto updatepresentposition at a variablerate determined by G(t)until the present positionmatchesthe targetposition.

[Figure 471]

Sucha schemepermits multiple muscles,or other motor effectors,to contractsynchronouslyeventhough the total amountofcontraction,scaledby T;(O)-P;(O), may be different for eacheffector(Figure 10). Unlike many alternative schemesfor motor control, present position in (110)is not computed usinginflow signals fromthe muscles.Rather,it isdeterminedby nonlinear integration of vectorscomputed by matching an outflowing target position command with feedbackfroin outflowing presentpositionsignals.

The VITE circuit is not sufficientin itselfto accom-

[Figure 472]

[Figure 473]

a primed movement vector and regulates the rate at which the movement vector updates the present position command. (Re-

printed with permission from Bullock & Grossberg, 1987a).

[Figure 474]

Nonlinear Neural Networks 47

[Figure 475]

[Figure 476]

plishall thetasksrequiredofavariable-speedvariableload arm movementsystem. In concert with several

parallelcircuits, however,it cangenerateflexible and adaptivetrajectories without suffering from the combinatorial explosionsandrigid performanceof control systemswhich preplan an entire trajectory. Herein I outline someof the adaptivecontrol issueswhicharise in the designof suchneuralarchitecturesfor movement controland mentionwhereinternalmatchingprocesses regulatetheir processesof learning and performance. Quantitativeneuralnetworksolutionsto suchproblems aresuggestedby Bullock and Grossberg(in press-a,in press-b)and Grossbergand Kuperstein(1986).

The computationofahandorarm's presentposition illustratesthe complexityoftheproblem.Asmentioned above,two generaltypesof presentpositionsignalshave beenidentified in discussionsof motorcontrol: outflow signalsand inflow signals.Figure II schematizesthe differencebetweenthesesignalsources.An outflowsignalcarriesa movementcommand from the brain to a muscle(Figure I Ia). Signalsthat branchoff from the efferentbrain-to-muscle pathway in order to register presentpositionsignalsarecalled corollary discharges (Helmholtz, 1962;vonHolst& Mittelstaedt, 1950).An inflow signalcarriespresentposition information from a muscleto the brain(Figure II b). A primary difference

[Figure 477]

betweenoutflowand inflow is that a changein outflow signalsis triggeredonly whenanobserver'sbrain generatesa newmovementcommand.A newinflow signal can, in contrast,begeneratedbypassivemovementsof the limb. Both outflow and inflow signalsare usedin multiple waysto providedifferenttypesof information about presentposition. The following summaryitemizessomeof the waysin which thesesignalsare used in our theory.

Althoughonerole of an outflow signalis to movea limb by contractingits targetmuscles,or motor plant, the operatingcharacteristicsofthe motor plantare not known a priori to the outflow source.It is not known a priori eitherhow muchthe musclewill actuallycontract in responseto anoutflow signalofprescribedsize, or how muchthe limb will movein responseto a prescribed muscle contraction. In addition, evenif the outflow systemsomehowpossessedthis information at onetime, it might turn outto bethewronginformation ata latertime, becausemuscleplantcharacteristicscan changethrough time due to development,aging,exercise,changesin blood supply,or minor tears.(Statedependentand history-dependentplant changesmay occuronthe factoryassemblyline or in afreely-moving robot, no lessthan in a living muscle.)Thus the relationship betweenthe size of an outflow movement

[Figure 478]

[Figure 479]

(.? ~

[Figure 480]

[Figure 481]

###### TIME

[Figure 482]

'"

[Figure 483]

[Figure 484]

w NU)a

[Figure 485]

[Figure 486]

###### f\

[Figure 487]

[Figure 488]

on on

00 00

- -+-'
- -0 ...

[Figure 489]

### "

- -+-' ...
- -0 ~

D--0 ...m

G- '"

-0 U)

;

[Figure 490]

[Figure 491]

0

0.95 1.19

[Figure 492]

[Figure 493]

0.48 0.71

0.00 0.00 0.24 0.48 0.71 0.95 1.19

[Figure 494]

[Figure 495]

###### TIME

###### ..TIME

(8)

(b)

FIGURE 10. With equal GO signals, movements of different size have equal durations and perfectly superimposable velocity profiles after velocity axis rescaling. (a, b): GO signals and velocity profiles for 20 and 60 unit movements lasting 560 ms. (Reprinted with permission from Bullock & Grossberg, 1987a).

0.24

48 S. Grossberg

[Figure 496]

[Figure 497]

[Figure 498]

[Figure 499]

- (a)

[Figure 500]

control processgeneratesadaptively a linear correspondencebetweenan outflow movementcommand andthe amount of musclecontraction evenif themuscle plant is nonlinear.The processwhich matchesoutflow and inflow signalsto linearize the muscle plant responsethrough learning is called adaptivelinearization of the muscleplant.

The cerebellumis implicated by both the theoreticallyderivedcircuit and experimentalevidenceasthe siteof learning. Early cerebellarlearningmodelswere proposedbyAlbus (1971),Brindley (1964),Grossberg (1964, 1969d,1972b),and Marr (1969). Later models and experimental support were provided by Fujita (1982a, 1982b),Ito (1974, 1982, 1984),McCormick and Thompson(1984), Opticanand Robinson(1980), Ronand Robinson(1973),Vilis and Hore (1986),and Vilis, Snow,and Hore (1983). The presentmodelintroduces newfeatureswhich are critical to its success in correcting behaviorallywell-characterizedtypes of movementserrors.

For example, an adaptive gain (AG) stagein our theory-which is interpretedasa modelcerebellumis usedby multiple circuits that contribute to botheye movementand arm movementaccuracyand postural stability. Eachofthesecircuits involvesdifferent-and specific-input, output, anderror signalpathways,but

[Figure 501]

MUSCLE

[Figure 502]

- (b)

[Figure 503]

[Figure 504]

[Figure 505]

FIGURE 11. Both outflow (a) and inflow (b) signals contribute to the brain's estimate of the limb's present position, but in

different ways.

[Figure 506]

commandandthe amount of musclecontractionis,in principle, undeterminable without additional information which characterizesthe muscleplant's actual responseto outflow signals.

To establisha satisfactorycorrespondencebetween outflow movementsignalsand actualmusclecontractions, the motor systemneedsto compute reliable presentpositionsignalswhich representwheretheoutflow commandtells the muscleto move,aswell asreliable presentpositionsignalswhich representthestate of contraction of the muscle.Corollary dischargesand inflow signalscanprovide thesedifferent types of information. Grossbergand Kuperstein (1986) have shownhowa match betweencorollary dischargesand inflow signalscanbe usedto modify, through an automatic learningprocess,the total outflow movement signalto the musclein a way that effectivelycompensatesfor changesin the muscleplant (Figure 12).Mismatchesact as error signalswhich changethe gain of the total outflow movementsignal.This automaticgain

[Figure 507]

[Figure 508]

FIGURE 12. ~;ome main features of the! muscle linearization network, or r.~LN: The outflow-inflow in11erface (011) registers matches and mismatches between outflow signals and inflow signals. Mismatches generate error signalls to the adaptive gain (AG) stage. '.hese error signals changE~ the gain of the conditioned movement signal to the moton,eurons (MN). Such an MLN adaptively linearizes the responses of a nonlinear muscle plant to outflow signals. The outflow sigrlals can therefore also be used as a :source of accurate corollary discharges of present eye position. (Reprinted with permission from Grossberg & Kuperstein, 1986, p. 136.)

[Figure 509]

Nonlinear Neural Networks 49

[Figure 510]

[Figure 511]

all ofthesepathwaysaremediatedby thesameinternal AG stagearchitecture. TheseAG stageresultssignificantly extend recentdata and modelsconcerningthe cerebellum'srole in the conditioning of movements

(Fujita, 1982a, 1982b; Ito, 1984; McCormick & Thompson, 1984;Optican& Robinson,1980).Forexample, push-pull opponentprocessingof the error signalswhichgovernadaptivegainchangesattheAG stage is a novel, and computationally critical, part of this model. Suchan arrangementenablesthe AG stageto correctundershoot,overshoot,or directionally skewed eyemovementerrors,aswellaserrorsdueto sustained wearingof curvature-distorting contactlens.

Although adaptive linearization is,like back-propagation,a form of error-drivenlearningin the mismatch mode, it is not susceptibleto the instabilities of back-

propagationbecauseit merelychangesthe gainsof internalcommand pathwaysvia internal mismatches.It does not put at risk the spatial encodingof the commandsthat activatethe pathwaysand is not subjected to noisefluctuations from the externalenvironment.

Given that corollary dischargesare matched with inflow signals to linearize the relationship between muscleplant contraction and outflow signalsize,outflow signalscanalsobe usedin otherwaysto provide important information about presentposition.As Figure 9 illustrates, outflow presentposition signalscan then be matched with target position commandsto generatea trajectorywith synchronousproperties.Thus outflow signalsare usedin at leastthree ways,and all of thesewaysare automatically registered:They send movementsignalsto targetmuscles;theygeneratecorollarydischargeswhicharematchedwith inflowsignals to guarantee linear muscle contractions evenif the muscleplant is nonlinear; and theygeneratecorollary dischargeswhich are matchedwith targetpositionsignalsto generatesynchronoustrajectories.

Inflow signalsarealsousedin severalways.Oneway hasalreadybeenitemized. A seconduseof inflow signals is suggestedby the following gedankenexample. When you are sitting in an armchair, let your hands drop passivelytowards your sides.Dependingupon a multitude of accidentalfactors, your handsand arms canend up in any of infinitely many final positions.If youare thencalled uponto makea precisemovement with yourarm-handsystem,this canbedonewith great accuracy.Thus the factthat your handsandarms start out this movementfrom an initial position which was not reachedunderactive control by an outflow signal doesnot impair the accuracyof the movement.

Much evidencesuggests,however,that comparison

betweentargetposition and presentposition information is usedto movethe arms andthat, asin Figure 9, this present position information is computed from outflow signals.In contrast, during the passivefall of an arm underthe influence of gravity,changesin outflow signal commands are not responsible for the

[Figure 512]

changesin positionofthelimb. Sincethe final position of a passivelyfalling limb cannot be predicted in advance, it is clear that inflow signalsmust be usedto updatepresentpositionwhenanarmismovedpassively by an externalforce, eventhough outflow signalsare usedto update presentposition whenthe arm moves activelyunder neuralcontrol.

This conclusioncalls attention to a closelyrelated issuethat mustbe dealtwith to understandthe neural basesofskilledmovement:Howdoesthe motor system know that the arm is beingmovedpassivelydue to an externalforce,and not activelydueto a changingoutflowcommand?Sucha distinction isneededto prevent inflow information from contaminating outflow commandswhenthe arm isbeingactivelymoved.The motor systemusesinternallygeneratedsignalsto makethe distinction between active movement and passive movement, or postural, conditions. Computational gatesare openedand shut basedupon whetherthese internally generatedsignalsare on or off.

Bullock and Grossberg(in press-a)havesuggested that the GO signalschematizedin Figure 9b helpsto computationallydefinethe posturalstate.Offsetofthe GO signalis hypothesizedto openalearninggate:which enablesinflowsignalsto beadaptivelyrecalibrateduntil theyarecomputed in the samemeasurementscaleas outflowsignals(Figure 13).This typeoflearningoccurs

[Figure 513]

[Figure 514]

FIGURE 13. A passive update of position (PUP) circuit. An adaptive path PPC DVpcalibr,ates PPC-outfiow signals in the same scale as inflow signals dul'ing intervals of posture. Dulring passive movements, output from DV equals zero. Hence the passive difference vector DVpllpdates the PPC until it equals the new position caused by any passive movements that rnay occur due to the application of external forces.

[Figure 515]

50 S. Grossberg

[Figure 516]

[Figure 517]

in the mismatch mode, rather than the approximate match mode, using the mismatch betweenthe coordinate systemsas an error signalto drive the learning process.OffsetoftheGO signalisalsohypothesizedto openagatewhichenablesanoutflow-inflow mismatch dueto a passivemovementto updatethe outflowpresent positioncommand(Figure 13).

[Figure 518]

###### AdaptiveGainControl

~ Zj;= P{ -Bzji + Sj[X;]+},

###### and

[Figure 519]

Vector

v = ([xJ+, [X2]+, ., [Xn]+)

[Figure 520]

[Figure 521]

|[Figure 522]<br><br>where<br><br>Match Gate|
|---|

The circuit whichaccomplishesboth oftheselearning and updatefunctions is calledthe PassiveUpdate of Position,or PUP,circuit. The equationsofa typical PUP circuit are:

11 if Ln Sj> 0

[Figure 523]

###### PresentPositionCommand

G(~Sfl= j=1 (117)

###### i-i 0 If.n L ~ = 0

[Figure 524]

[Figure 525]

(Ill)

j=1

and [Xj]+ = max(Xj,0). In (114),Ii is the corollarydischarge signal that representsthe position of the ith muscle, Sjis the light-activated representationof the jth targetposition, zjiis the LTM trace that adaptively adjuststhe gain betweenSjand Ii, P is a gatingsignal that switcheson in the postural mode, and V is the outputvector.VariableXiin (114)playstheroleofvariableMi in (112).

[Figure 526]

Outflow-InflowMatch

[Figure 527]

[Figure 528]

(112)

[Figure 529]

Adaptive Gain Control

did Zj= OGP(-EZj+ [MJ+). (113)

[Figure 530]

Due to the generalimportance of schemessuchas the PUP circuit of(III)-(113) andthe HMI circuit of (114)-( 117) for adaptively recalibrating coordinate systemsusing vector computations, I havecalled all schemesof this typeAdaptive VectorEncoders.

[Figure 531]

Equation (Ill) supplementsequation (110) with an updatesignalGp[MJ+that is turned on only whenthe passivegatingfunction, or"pauser" signal,Gpbecomes positive in the passive,or postural, state. Function Zj in (113)is an LTM trace, or associativeweight,which adaptivelyrecalibratesthe gain of outflow signals Pj until they are in the samescaleas outflow signals'Ylj in (112).

A third role for inflow signalsis neededdue to the fact that arms canmove at variable velocities while carryingvariableloads.Becausean armisa mechanical systemembeddedin a Newtonian world, an arm can generateunexpectedamounts of inertia and acceleration whenit triesto movenovelloadsat novelvelocities. During sucha novelmotion, the commandedoutflow position of the arm and its actualposition maysignificantly diverge.Inflow signalsare neededto compute mismatchesleadingto partial compensationfor this uncontrolled componentof the movement.

In summary,offsetoftheGO signalwithin the VITE circuit enablesa pausersignalwithin the PUP circuit to drive its learning and resetfunctions. Suchpausermodulated learning of mismatchesseemsto occur in severaladaptivesensory-motorcontrolcircuits. Forexample,GrossbergandKuperstein(1986)havesuggested that a pausersignalwhich definesthe posturalstateof the ballistic eyemovementsystemenablesa mismatch signalanalogousto Mj in (112)to adaptivelyrecode the representationof a light-activated target position command into motor coordinates.This adaptiverecoding scheme,which is called the Head-MuscleInterface,or HMI, permitstherecodedtargetpositionto be matched againstthe presentposition of the eye, which is also coded in motor coordinates. Such a matchingprocessgeneratesa movementcommand in the form ofadifferencevectorwhichmeasuresthemismatch betweentarget position and presentposition, much asin the VITE circuit of Figure 9.

Suchnovelmovementsarequite different from our movementswhenwe pick up a familiar fountain pen or briefcase.Whenthe objectis familiar, we canpredictivelyadjustthegainofthe movementto compensate for the expectedmassof the object. This type of automatic gaincontrolcan,moreover,be flexiblyswitched onand off usingsignalpathwaysthat can beactivated byvisual recognitionofa familiar object.Inflow signals are used in the learning processwhich enablessuch automatic gain control signalsto be activated in an anticipatory fashion in responseto familiar objects (Bullock & Grossberg,in press-b).

Typicalequationsfor anHMI circuit are: Head-MuscleMatch

[Figure 532]

19. EXTERNAL ERROR SIGNALS FOR LEARNING ADAPTIVE MOVEMENT GAINS: PUSH-PULL OPPONENT PROCESSING

[Figure 533]

Thepreviousdiscussionoutlined severalofthetypes (114) of learningwherebyinternalmismatchesgenerateerror

[Figure 534]

[Figure 535]

Nonlinear Neural Networks 51

[Figure 536]

[Figure 537]

[Figure 538]

[Figure 539]

CHOICE

[Figure 540]

[Figure 541]

ERROR

MOVEMENT COMMAND

SIGNAL

~:~+.--

[Figure 542]

[Figure 543]

SSTM

[Figure 544]

~SIGNAL

[Figure 545]

UNCONDITIONED PATHWAY

.

[Figure 546]

PATHWAY

|[Figure 547]<br><br>.~|
|---|

+

[Figure 548]

[Figure 549]

[Figure 550]

[Figure 551]

FIGURE 14. The representation of the chosen first light gives rise 1:0an unconditioned movE~ment signal and a conditioned movement signal. The unconditioned signal causes movements that are corrected by the conditioned movement signal via learning. The conditioned pathway carries sampling signals whose strength can be altered by second-light mediated error signals. These sampling signals give rise to the conditioned movement signal. The representation of tht~ first light must be stored until after the end of the saccade, so that the secondlight Imediated error signal can act. (Reprinted with permission from Grossberg & Kuperstein, 1986, p. 38.)

[Figure 552]

signalscapableof adaptivelyrecalibratingacoordinate systemor adaptivelychangingthe gainof a movement command.External errorsignalsarealsousedto alter the gain of a movementcommand. Sucherror signals function like an external"teacher." Unlike the hypotheticalteachersemployedin manyexamplesof backpropagation,theseerror signalscorrespondto events which actually occurin the externalenvironmentduring real-time learning.

Grossbergand Kuperstein(1986)have,forexample, demonstrated how the accuracy of eye movements which do not successfullyfoveatea light can be improvedby usingthe position of the light on the retina afterthe movementterminatesasanerrorsignal(Figure 14). Suchan error signaladaptivelychangesthe gain of the movementcommand. Mathematicaland computeranalysesdemonstratehowto designsucha system so that externalerror signalsdueto nonfoveatedlights cooperatewith internal error signalsdue to outflowinflow mismatchesto generatemovementscapableof adaptivelymaintaining their accuracywithout the intervention of a human teacher(Figure 15).

--t

SAMF'LlNG

|[Figure 553]<br><br>The successofthis learningmodeldependscritically uponthehypothesisthat errorsarecorrectedin apushpull, oropponent,fashion(Figure 16).Theeyemuscles, or other effectors,are assumedto be organizedin reciprocal push-pull pairs, suchasa pair for pulling to the right (R) andthe left (L). Typicallearningrules for suchpairs are (expressedfor conveniencein discrete time (n):<br><br>HemifzeldGradientLearningRule<br><br>ZRi(n + I) = OZRi(n)+ [L(En)]+ (118) zLi(n + I) = ozLi(n) + [-L(En)]+ (119)|
|---|
|[Figure 554]<br><br>and the<br><br>Fractured Somatotopy Learning Rule<br><br>ZRi(n + I) = [OZRi(n) + L(En)]+ (120) zLi(n + I) = [ozLi(n) -L(En)]+ (121)<br><br>where in both casesEn representsthe position of the light error onthe nth trial, and L(E,,)isthe error signal by which it drivesthe learningofadaptivegains.Function L( ",) is assumedto be anincreasingfunction of w ~ 0, and to be an odd function of w; viz., L(w) = -L(-w). VariablesZRiand ZLiare the LTM traces controlled bythe ith commandsourceto the right and left motor effectors.<br><br>Due to the push-pull organizationof the learning process,the output signal °R(n) to the right muscle dependsupon the differencesZRi(n)-zLi(n) of these LTM traces,whereasthe output signalOL(n)to the left muscledependsupon the differencesZLi(n)-zRi(n). Suchpush-pullterms suggesta physicalwayto instantiate the types of formal comparisonsbetweenincrementsandbaselineterms that havebeenhypothesized in a number of learning models(Rescorla& Wagner, 1972;Sutton& Barto, 1981).Opponentprocessinghas also beenassumedto regulatelearning in real-time neural network modelsof classicaland instrumental ~onditioning (Grossberg,1972a;Grossberg& Schmajuk, 1987).|

20. MATCH-INVARIANTS:INTERNALLY REGULATEDLEARNING OF AN INVARIANT SELF-REGULATING

[Figure 555]

TARGET POsmON MAP

Among the most important types of problems in neural network theory are those which concernthe adaptiveemergenceof recognition invariants. Many differenttypes of invariants canbe identified; for example,the emergentinvariantsencodedbythe critical featurepatternsin an ART architectureenablethe architecture to group all exemplarsthat share certain similarity propertiesinto a singlerecognitioncategory. As in ART, a number of othertypesof invariants are learnedthroughamatch-regulatedprocesswhichgates

[Figure 556]

[Figure 557]

52

[Figure 558]

###### ~tI

[Figure 559]

- 0

[Figure 560]

~

4:3 7

~~

~o

- 1

###### ~

LJoo

[Figure 561]

g;

0

[Figure 562]

###### Lt:~

[Figure 563]

Rt'INA,L~

OSIIION

###### ""~IGH"

[Figure 564]

(a)

[Figure 565]

S. Grossberg"

[Figure 566]

[Figure 567]

~l ERRORS BEFORE/AFTER

[Figure 568]

[Figure 569]

[Figure 570]

MUSCLE INPUT BEFORE AFTER

(b)

FIGURE 15. Computer simulation of saccadic error correction model with sampling from a non-invariant target position map using a siower-than-linear muscle function and a linear learning function. (a) Topographic distribution of LTM trace, values after learning; (b) Muscle response function used in the simulation; (c) Errors in 100 trials before learning begins and 100 trials after learning ends. Negative values correspond to undershoots and positive values correspond to overshoots. (Reprinted with permission from Grossberg & Kuperstein, 1986, p. 89.)

[Figure 571]

on and off the learningmechanismsthat enableindividual eventsto begroupedtogetheradaptively.I call suchinvariants match invariantsto distinguish them from invariantsthatarise(say)dueto apassivefiltering process,suchas Fourier-Mellin filtering.

Another model of a match invariant processwas

developedby Grossbergand Kuperstein(1986).This modelshowshowamatchingprocesswhichdefinesthe postural statecanregulatethe learningof an invariant self-regulatingtarget position map in egocentric, or head-centered,coordinates.This problemariseswhen

[Figure 572]

one considershow a visual signalto a moveableeye, or camerasystem,canbeefficientlyconvertedinto an eye-trackingmovementcommand.

To solvethis problem, the positions of lights registered onthe retina of aneyeneedto beconvertedinto ahead-coordinateframesotheycanbecomparedwith presenteye positions which are also computed in a head-coordinateframe. In orderto convertthe position of a light on the retina into a target position in head coordinates,one needsto join together information aboutthelight's retinalpositionwith information about

[Figure 573]

Nonlinea; NeuralNetworks

[Figure 574]

53 ANTAGONIST

[Figure 575]

[Figure 576]

[Figure 577]

is learnedarisesfrom its many-to-oneproperty. The many-to-onepropertyimplies thateachretinal position andeacheyepositioncanactivatemanytargetpositions in headcoordinates(Figure 18b).Evenafter learning takesplace,eachpair of retinal and eyepositions can activatemanytargetpositionsin headcoordinates,but onlythe correcttargetpositionshouldreceivethemaximal total activation.

AGONIST MUSCLE STRIP

MUSCLE STRIP

[Figure 578]

[Figure 579]

SAMPLING SIGNAL

-~L:.::t..T

[Figure 580]

ERROR

What preventslearningdue to one pair of retinal andeyepositionsfrom contradictinglearningdueto a different pair of positions?In particular, if pairing retinal position R( with eye position £( strengthensthe pathwaysfrom thesepositions to target position T(, thenwhy doesnot future pairing ofR( with a different eyeposition£2continueto maximallyexciteT, instead

SIGNAL

[Figure 581]

(a)

[Figure 582]

[Figure 583]

ANTAGONIST AGONIST

[Figure 584]

[Figure 585]

SAMPLING SIGNAL

###### EYE

[Figure 586]

[Figure 587]

ERROR POSITION

SIGNAL

[Figure 588]

[Figure 589]

TARGET

"",~.:\1\

[Figure 590]

+~TITION + ~

[Figure 591]

[Figure 592]

##### (b) :>-<

[Figure 593]

[Figure 594]

RETINAL L~'~

FIGURE 16. Two ways to achieve opponent conditioning of agonist-antagonist muscles: (a) An error si~lnal increases the conditioned gain at the agonist muscle strip and decreases the conditioned gain at the antagonist muscle strip; (b) An error signal increases the conditioned gain at tlhe agonist muscle strip. Competition between agonist and antagonist muscle strip outputs causes the decrease in the net antagonist output. (Reprinted with permission from Grossberg & Kuperstein, 1986, p.70.)

[Figure 595]

POSITION

RETINA

[Figure 596]

presentposition of the eye in the head (Figure 17). Kupersteinand I suggestedthat this type of transformation is learned. Otherwise,the retinal systemand the eye position system-which are widely separated inthe brainanddesignedaccordingto differentinternal constraints-would haveto bepre-wiredwith perfectly chosenparametersfor their mutual interaction. We haveshownhowsucha transformation canbelearned evenif parametersare coarselychoseninitially and if significant portions of either systemare damagedor evendestroyed.This typeoflearningexhibitsproperties whichare of generalinterestin otherbiologicalmovementsystems,in cognitivepsychology,andin thedesign of freely moving robots. I will thereforedescribeits majorelementshere.

The most important propertiesof this transformation are that it is many-to-one,invariant, and self-regulating. As Figure 17illustrates, many combinations of retinal position and eye position correspondto a singletargetposition with respectto the head.Whena singletargetposition representationis activatedby all of thesepossiblecombinations,the transformation is saidto be invariant (Figure 18a).The keydifficulty in understandinghow such an invariant transformation

[Figure 597]

[Figure 598]

""-..

/)"-:;"/11

[Figure 599]

~,

[Figure 600]

FIGURE 17. Many combinations of retinal position and eye position can encode the same target position.

54 S. Grossberg

[Figure 601]

[Figure 602]

[Figure 603]

TARGET POSITIONS

IN HEAD

COORDINATES

[Figure 604]

[Figure 605]

RETINAL

POSITIONS

[Figure 606]

PRESENT EYE

POSITIONS

[Figure 607]

(a)

[Figure 608]

TARGET

POSITIONS

[Figure 609]

[Figure 610]

RETINAL

POSITIONS

[Figure 611]

EYE POSITIONS

[Figure 612]

(b)

[Figure 613]

FIGURE 1B. (a) When the many combinations of retinal position and eye position that correspond to each fixed target position all activate the same internal representation of that target position in head coordinates, the ensemble of such head coordinate representations is said to form an invariant map; (b) Every eye position and retinal position can send signals to many target position representations.

[Figure 614]

of the correct targetposition correspondingto Rt and £2? Howisa globallyconsistentrule learnedby a network, despitethe fact that allcomputationsin the network arelocal?How cana targetposition mapbe implicitly defined,suchthat eacheyepositionand retinal position, takenseparately,activatesa largenumber of

targetpositions,yet in combination alwaysmaximally activatethe correct targetposition?

[Figure 615]

Finally, the property of self-regulationmeansthat the mapcancorrectitself evenif a largefraction ofthe retinal positionsand/oreyepositionsaredestroyed,or if their parametersareotherwisealteredthroughtime. Destruction of a single retinal position eliminates all the combinations which that position made with all eyepositionsto activate targetpositions. In a similar fashion,destroyinga singleeyeposition candisrupt all targetpositions with which it waslinked. A self-regulating map must thus be able to reorganizeall of its learnedchangesto maintain its global self-consistency after removalof any of its components.

The self-regulation property is illustrated by the computer simulation from Grossbergand Kuperstein (1986)that is summarized in Figure 19. Eachrow in Figure 19depicts learning of target positions correspondingto a different number of retinal and eyepositions.Morecombinationsofpositionsarerepresented in eachsuccessiverow. The first column in eachrow depictsanintermediatelearning stage,andthe second columndepictsa latelearningstage.The abscissaplots topographicpositionsacrossthe retinal and eyepositions maps,whereasthe ordinate plots the sizesof the adaptivepathstrengths,or learnedlong term memory (LTM) traces,in the pathwaysfrom thesemapsto the targetposition map. Sucha schemeclarifies how the eye-headtarget position map that is schematizedin Figure9 mayself-organiz~.

The LTM tracesin Figure 19wererandomlychosen beforelearningbegan.A comparisonofpanels(b), (d), and (f) shows that the LTM traces can reorganize themselveswhenmore combinations of positions are associatedin suchawayasto (approximately)preserve that part of the map which was learned when fewer combinations of positions were associated.This selfregulationpropertyalsoholdswhenmorecombinations are replaced by fewercombinations, or if the initial LTM tracesare not randomly chosen(Figure 20).

[Figure 616]

21. PRESYNAPTIC COMPETmON FOR

###### LONG TERM MEMORY: SELF-REGULATING

COMPETITIVE LEARNING A completemodelof howaninvariantself-regulating

targetposition map canbelearned,aswell asvariants of this model, aredescribedin Grossbergand Kuperstein(1986). Herein I emphasizeone key point about the model.

The invarianceand self-regulationpropertiesof the TPM aredueto the factthat allthe LTM traceswhose pathwaysproject to a singleTPM cell readjustthemselvesin a compensatoryfashionwhenanyone ofthese LTM traceschangesdue to learning (Figure 18). We suggestedthatthesynapticendingsin whichtheseLTM tracesarecomputed contain autoreceptors(Cubeddu,

[Figure 617]

Nonlinear Neural-Networks 55

[Figure 618]

[Figure 619]

[Figure 620]

[Figure 621]

::>ILl

-I

###### ~

###### ~~

[Figure 622]

(b)

[Figure 623]

[Figure 624]

[Figure 625]

[Figure 626]

Z (1) Z (2)

Z (1) Z (2)

[Figure 627]

###### -

[Figure 628]

;I .II

12 .i2

[Figure 629]

.,0,;

w

###### -' ..

~ 0

001: 0

>

~ ",.

0

###### -'

t- 0

N.0 0

~~160I -120...I-80 -40 0 40 80 120 160

###### LEFT RIGHT

[Figure 630]

(e) (f)

FIGURE 19. Expansion of L TM spatial maps due to increase of the number of light positions and I~ye positions being correlated. The learned LTM values in corresponding positions agree, thereby illustrating map self-regulation. Initial values of LTM traces Viere randomly chosen. (Reprinted with permission from Grossberg & Kuperstein, 1986, p. 246.)

[Figure 631]

Hoffmann, & James, 1983; Dubocovich & Weiner, 1982;Groves& Tepper,1983;Groves,Fenster,Tepper, Nakamura,& Young, 1981;Niedzwiecki,Mailman, & Cubeddu,1984;Siever& Sulser,1984;Tepper,Young, & Groves,1984).In a networkwhosecellscontainautoreceptivesynapses,whena transmitteris releasedby onesynapticending,a portion of it canundergoreuptake via the autoreceptorsof other activeand nearby synapticendings.Reuptakehasan inhibitory effecton the LTM trace of eachactive synaptic ending. Thus autoreceptorsrealizeatype ofpresynapticcompetition among all the LTM traceswhosepathwaysconverge upon the same cell within the TPM. Autoreceptors

[Figure 632]

herebymediatea noveltype of self-regulatingcompetitive learning.

Suchan LTM traceobeysan equationof the form:

AutoreceptiveAssociator

d-d Z;j = ES;[-Fzij + GXj -H Ln SkZIIj]. (122)

t k-1

[Figure 633]

In (122), Zjjis the LTM trace in the pathwayfrom the ith cell in the retinotopic map or eyeposition mapto thejth cell in the TPM; Sjis the signalemitted by the ith cell into this pathway;and Xjis the activity of the jth TPM cell. The termsE,F, G, and H areconstants.

[Figure 634]

###### 56 S. GTossberg

[Figure 635]

[Figure 636]

[Figure 637]

[Figure 638]

, ,

###### .,,

LU

:>-J.c

< '

..,>~ .,,

-J

, ,

,

[Figure 639]

(b)

|[Figure 640]<br><br>0<br><br>~ .,0<br><br>w ,,;<br><br>~-J .,0 .( ,,;<br><br>><br><br>~ ~0<br><br>t- 0<br><br>-J<br><br>0<br><br>'"<br><br>(|[Figure 641]<br><br>Z (1) Z (Z)<br><br>IZ .IZ<br><br>[Figure 642]<br><br>1), Z11(2)<br><br>[Figure 643]| |
|---|---|---|
|,,;<br><br>'"<br><br>-160 -1|[Figure 644]<br><br>20 -80 -~ 0<br><br>LEFT<br><br>4|[Figure 645]<br><br>0 80 120 160<br><br>RIGHT|

[Figure 646]

[Figure 647]

[Figure 648]

(c) (d)

[Figure 649]

[Figure 650]

[Figure 651]

[Figure 652]

[Figure 653]

Z (1) Z (2)

Z"(1)..'Z (2) Z12(1)tZi1(1)

Z (I) Z (2)

|[Figure 654]<br><br>~<br><br>.,0<br><br>0<br><br>!oJ ~ 0<br><br>>-I< G0<br><br>[Figure 655]| |
|---|---|
|~~|0<br><br>0<br><br>N,.<br><br>0<br><br>[Figure 656]<br><br>0<br><br>-160|

c c

, 11 .11

#### .

12 .i2

[Figure 657]

c

c W

###### ~-J.c

>< c

~ ..c

t- C

###### I

-J

!

~

C

-

0-160 -120 -80 -40 0

[Figure 658]

[Figure 659]

[Figure 660]

40 80 120 160

40 80 120 160

-120 -80 -40 0

RIGHT

LEFT

###### RIGHT

LEFT

[Figure 661]

(e) (f)

FIGURE 20. Same as in Figure 19, except initial values of LTM traces were chosen equal to zero. Note that Ilearned spatial maps in Figures 19 and 20 agree, thereby illustrating the ability of map learning to overcome noise. (Reprinted 1Nith permission from Grossberg & Kuperstein, 1986, p. 239.)

[Figure 662]

Equation (122)saysthat reuptakevia autoreceptorsof a fraction of releasedtransmitter, as in term -H X LZ=I SkZkj,inhibits the growthof the corresponding LTM trace.

Match-regulated learning processesalso occur in applicationsto suchspatio-temporallearningproblems asspeechandlanguagelearning,andplannedsensorymotor control (Grossberg,1982, 1987b;Grossberg& Kuperstein, 1986).The totality of suchknown examplesillustrate howcombinations of internal matching processesand external error signalsderived from natural real-time environments can regulatestableself-

[Figure 663]

organizedlearning,recognition,and actionin response to noisyand unpredictableenvironments.

REFERENCES

[Figure 664]

[Figure 665]

Ackley, D. H., Hinton, G. E., & Sejnowski, T. J. (1985). A learning algorithm for Boltzmann machines. Cognitive Science, 9, 147169.

Albus, J. S. (1971). A theory of cerebellar function. Mathematical Biosciences, 10,25-61. Amari, S.,& Arbib, M. A. (Eds.). (1982). Competition and cooperation in neural networks. New York: Springer-Verlag. Amari, S., & Takeuchi, A. (1978). Mathematiical theory on formation

[Figure 666]

Nonlinear Neural Networks 57

[Figure 667]

[Figure 668]

of category detecting nerve cells. Biological Cybernetics, 29, 127136.

Amit, D. J., Gutfreund, H., & Sompolinsky, H. (1987). Information storage in neural networks with low levels of activity. Physical Review A. 35, 2293-2303.

Anderson, J. A. (1968). A memory model utilizing spatial correlation functions. Kybernetik. 5, 113-119. Anderson, J. A. (1983). Cognitive and psychological computation with neural models. IEEE Transactions SMC-13, 5, 799-815.

Anderson, J. A., Silverstein, J. W., Ritz, S. R., & Jones,R. S. (1977). Distinctive features, categorical perception, and probability learning: Some applications of a neural model. PsJ'chological Re-

view,84, 413-451.

Arend, L. E., Buehler, J. N., & Lockhead, G. R. (1971). Difference information in brightness perception. Perception and Psychophysics. 9, 367-370.

Banquet, J.-P., & Grossberg, S. (in press). Probing cognitive processes through the structure of event-related potentials during learning: An experimental and theoretical analysis. Applied Optics.

Beck, J. (1972). Surface color perception. Ithaca, NY: Cornell University Press.

Bienenstock, E. L., Cooper, L. N., & Munro, P. W. (1982). Theory for the development of neuron selectivity: Orientation specificity and binocular interaction in visual cortex. Journal ofNeuroscience. 2, 32-48.

Boring, E. G. (1950). A history ofexperimental psychology (2nd ed.). New York: Appleton-Century-Crofts.

Brindley, G. S. (1964). The usemade by the cerebellum of the information that it receives from sense organs. International Brain Research Organization Bulletin, 3, 80.

- Bullock, D., & Grossberg, S. (in press-a). Neural dynamics of planned arm movements: Emergent invariants and speed-accuracy properties during trajectory formation. Psychological Review.
- Bullock, D., & Grossberg, S. (in press-b). Neuromuscular realization of planned trajectories: Adaptive and automatic mechanisms.

Caianiello, E. R. (1961). Outline of a theory of thought and thinking machines. Journal ofTheoretical Biology, 1,204-235. Campbell, L., & Garnett, W. (1882). The life ofJames Clerk Maxwell. London: Macmillan.

- Carpenter, G. A. (1977a). A geometric approach to singular perturbation problems with applications to nerve impulse equations. Journal ofDifferential Equations. 23, 335-367.
- Carpenter, G. A. (1977b). Periodic solutions of nerve impulse equations. Journal ofMathematical Analysis andApplications. 58, 152173.

Carpenter, G. A. (1979). Bursting phenomena in excitable membranes. SIAM Journal on Applied Mathematics, 36, 334-372.

Carpenter, G. A. (1981). Normal and abnormal signal patterns in nerve cells. In S. Grossberg (Ed.), Mathematical psychology and psychophysiology (pp. 49-90). Providence, RI: American Mathematical Society.

Carpenter, G. A., & Grossberg, S. (1985). Category learning and adaptive pattern recognition: A neural network model. Proceedings

ofthe Third Army Conference on Applied Mathematics and Computing, 37-56.

- Carpenter, G. A., & Grossberg, S. (1987a). A massively parallel architecture for a self-organizing neural pattern recognition machine. Computer Vision, Graphics. and Image Processing. 37, 54-115.
- Carpenter, G. A., & Grossberg, S. (1987b). Associative learning, adaptive pattern recognition, and cooperative-competitive decision making by neural networks. In H. Szu (Ed.), Optical and hybrid computing (218-247). Bellingham, WA: Society of Photo-Optical Instrumentation Engineers.

Carpenter, G. A., & Grossberg, S. (in press). ART 2: Self-organization of stable category recognition codes for analog input patterns. Applied Optics.

Cohen, M. A., & Grossberg, S. (1983). Absolute stability of global

[Figure 669]

pattern formation and parallel memory storage by competitive neural networks. IEEE Transactions SMC-13, 815-826.

Cohen, M. A., & Grossberg, S.(1984). Neural dynamics of brightness perception: Features, boundaries, diffusion, and resonance. Perception and Psychophysics. 36, 428-456.

Cohen, M., & Grossberg, S. (1986). Neural dynamics of speechand

language coding: Developmental programs, perceptual grouping, and competition for short term memory. Human Neurobiolog).:

5,1-22.

Cohen, M., & Grossberg,S.(1987). Masking fields: A massively parallel neural architecture for learning, recognizing, and predicting multiple groupings of patterned data. Applied Optics. 26, 1866-1891.

Cornsweet, T. N. (1970). Visual perception. New York: Academic Press. Cubeddu, L. X., Hoffmann, I. S., & James, M. K. (1983). Frequency-

dependent effects of neuronal uptake inhibitors on the autoreceptor-mediated modulation of dopamine and acetylcholine release from the rabbit striatum. Journal ofPharmacology and Experimental Therapeutics. 226, 88-94.

Denker, J. S.(Ed.). (1986). Neural net»'orksforcomputing. New York: American Institute of Physics.

Dubocovich, M. L., & Weiner, N. (1982). Modulation of the stimulation-evoked release of 3H-dopamine through activation of dopamine autoreceptors of the D-2 subtype in the isolated rabbit retina. In M. Kohsaka et al. (Eds.), Advances in the biosciences. Volume 37: Advancesin dopamine research. New York: Pergamon

Press.

Duda, R. 0., & Hart, P. E. (1973). Pattern classification and scene analysis. New York: Wiley.

Eigen, M., & Schuster,P.(1978). The hypercycle: A principle of natural self-organization, B: The abstract hypercycle. Naturwissenschaflen. 65, 7-41.

Ellias, S. A., & Grossberg, S. (1975). Pattern formation, contrast control, and oscillations in the short term memory of shunting oncenter off-surround networks. Biological Cybernetics. 20, 69-98.

Elman, J. H., Diehl, R. L., & Buchwald, S. E. (1977). Perceptual switching in bilinguals. Journal ofthe Acoustical Society ofAmerica. 62,971-974.

- Ermentrout, G. B., & Cowan, J. D. (1979). Temporal oscillations in neuronal nets. Journal ofMathematical Biolog).: 7,265-286.
- Ermentrout, G. B., & Cowan, J. D. (1980). Large scale spatially organized activity in neural nets. SIAM Journal on Applied Mathematics.38, 1-21.

Feldman, J. A., & Ballard, D. H. (1982). Connectionist models and their properties. Cognitive Science. 6, 205-254. Freeman, W.J. (1975). Mass action in thenervous system. New York: Academic Press.

Freeman, W. J. (1979). EEG analysisgivesmodel of neuronal templatematching mechanism for sensory search with olfactory bulb. Biological Cybernetics. 35, 221-234.

- Fujita, M. (1982a). Simulation of adaptive modification of the vestibulo-ocular reflex with an adaptive filter model of the cerebellum. Biological Cybernetics. 45, 207-214.
- Fujita, M. (1982b). Adaptive filter model of the cerebellum. Biological Cybernetics. 45, 195-206.

- Geman, S. (1983, April). Stochastic relaxation methods for image restoration and expert systems. Proceedings of ARO worksh,:>pon unsupervised image analysis. Brown University, Providence, RI.
- Geman, S. (1984). Stochastic relaxation methods for image restoration and expert systems. In D. B. Cooper, R. L. Launer, & D. E. McClure (Eds.), Automated image analysis: Theory and experiments. New York: Academic Press.

Geman, S., & Geman, D. (1984). Stochastic relaxation, Gibbs distributions, and the Bayesian restoration of images. IEEE Transactions on Pattern Analysis and Machine Intelligence. 6, 721-

741.

Gilpin, M. E., & Ayala, F. J. (1973). Global models of growth and competition. Proceedings ofthe National Academy ofSciences. 70, 3590-3593.

[Figure 670]

58 S. Grossberg

[Figure 671]

[Figure 672]

Glazebrook, R. T. (1905). James Clerk Maxwell and modern physics. New York: Macmillan.

Goh, B. S., & Agnew, T. T. (1977). Stability in Gilpin and Ayala's models of competition. Journal ofMathematical Biology, 4, 275279.

Golden, R. M. (1986). The "Brain-state-in-a-box" neural model is a gradient descent algorithm. Journal ofMathematical Psychology, 30, 73-80.

Gray, R. M. (1984, April). Vectorquantization. IEEE ASSPMagazine.

4-29.

Grossbe~ S. (1964). The theory ofembeddingfields with applications to psychology and neurophysiology. New York: Rockefeller Institute for Medical Research.

- Grossberg, S. (1967). Nonlinear difference-differential equations in prediction and learning theory. Proceedings ofthe National AcademyofSciences, 58,1329-1334.
- Grossberg, S. (1968a). Some physiological and biochemical consequences of psychological postulates. Proceedings ofthe National Academy ofSciences,60, 758-765.

- Grossberg, S. (1968b). Some nonlinear networks capable of learning a spatial pattern of arbitrary complexity. Proceedings ofthe National Academy ofSciences, 59, 368-372.

Grossberg, S. (1969a). On learning and energy-entropy dependence in recurrent and nonrecurrent signed networks. Journal ofStatistical Physics, 1, 319-350.

- Grossberg, S. (1969b). Some networks that can learn, remember, and reproduce any number of complicated space-time patterns, I. Journal ofMathematics and Mechanics. 19,53-91.

- Grossberg, S. (1969c). On the serial learning of lists. Mathematical Biosciences, 4, 201-253.
- Grossberg, S. (1969d). On learning of spatiotemporal patterns by networks with ordered sensory and motor components, I: Excitatory components of the cerebellum. Studies in Applied Mathematics.48, 105-132.

- Grossberg, S. (1970a). Some networks that can learn, remember, and reproduce any number of complicated space-time patterns, II. Studies in Applied Mathematics. 49,135-166.

- Grossberg, S. (1970b). Neural pattern discrimination. Journal of Theoretical Biology, 27,291-337.

Grossberg, S. (197Ia). On the dynamics of operant conditioning. Journal of Theoretical Biology, 33, 225-255.

Grossberg, S. (197Ib). Pavlovian pattern learning by nonlinear neural networks. Proceedings ofthe National Academy of Sciences, 68,

828-831.

- Grossberg, S. (1972a). A neural theory of punishment and avoidance, II: Quantitative theory. Mathematical Biosciences. 15, 253-285.
- Grossberg, S. (1972b). Neural expectation: Cerebellar and retinal analogs of cells fired by learnable or unlearned pattern classes. Ky-

bernetik, 10, 49-57.

- Grossberg, S. (1972c). Pattern learning by functional-differential neural networks with arbitrary path weights. In K. Schmitt (Ed.), Delay andfunctional-dijferential equations and their applications (pp. 121-160). New York: Academic Press.

- Grossberg, S. (1973). Contour enhancement, short term memory, and constancies in reverberating neural networks. Studies in Applied Mathematics. 52,217-257.
- Grossberg, S. (1974). Classical and instrumental learning by neural networks. In R. Rosen and F. Snell (Eds.), Progress in theoretical biology. New York: Academic Press.

- Grossberg, S. (1976a). Adaptive pattern classification and universal recoding, I: Parallel development and coding of neural feature detectors. Biological Cybernetics. 23, 121-134.
- Grossberg, S. (1976b). Adaptive pattern classification and universal recoding, II: Feedback, expectation, olfaction, and illusions. Biological Cybernetics. 23, 187-202.

- Grossberg, S. (1977). Pattern formation by the global limits of a nonlinear competitive interaction in n dimensions. Journal ofMathematical Biology. 4, 237-256.
- Grossberg, S. (1978a). A theory of human memory: Self-organization

[Figure 673]

and performance of sensory-motor codes, maps, and plans. In R. Rosen & F. Snell (Eds.), Progress in theoretical biology (Vol. 5, pp. 233-374). New York: Academic Press.

- Grossberg, S. (1978b). Do all neural models really look alike? Psychological Revie~ 85, 592-596.
- Grossberg, S. (1978c). Competition, decision, and consensus.Journal ofMathematical Analysis and Applications, 66, 470-493.
- Grossberg, S. (1978d). Decisions, patterns, and oscillations in nonlinear competitive systems with applications to Volterra-Latka systems. Journal ofTheoretical Biology, 73, 101-130.

- Grossberg, S. (1980a). Biological competition: Decision rules, pattern formation, and oscillations. Proceedings ofthe National Academy

ofSciences,77,2338-2342.

- Grossberg, S. (1980b). How does a brain build a cognitive code? PsychologicalRevie~ 87, I-51.

Grossberg, S. (Ed.). (1981), Adaptive resonance in development, perception, and cognition. In Mathematical psychology and psychophysiology (pp. 107-156). Providence, RI: American Mathematical Society.

Grossberg, S. (1982). Studies ofmind and brain: Neural principles of learning, perception, development, cognition, and motor control. Boston: Reidel Press.

Grossberg, S. (1984). Unitization, automaticity, temporal order, and word recognition. Cognition and Brain Theo').',7, 263-283.

- Grossberg, S. (1986). The adaptive self-organization of serial order in behavior: Speech, language,and motor control. In E. C. Schwab & H. C. Nusbaum (Eds.), Pattern recognition by humans and machines, Vol. I: Speech perception (pp. 187-294). New York: Academic Press.
- Grossberg, S. (1987a). Cortical dynamics of three-dimensional form, color, and brightness perception, I: Monocular theory. Perception and Psychophysics, 41, 87-116.

Grossberg, S. (1987b). Cortical dynamics of three-dimensional form, color, apd brightness perception, II: Binocular theory. Perception and Psychophysics, 41, 117-158.

Grossberg,S.(Ed.). (1987c). The adaptive brain, I: Cognition. learning, reinforcement, and rhythm. Amsterdam: Elsevier/North-Holland.

- Grossberg, S. (Ed.). (1987d). The adaptive brain, II: Vision, speech, lang/lage, and motor control. Amsterdam: ElsevierjNorth-Holland.

Grossberg, S. (1987e). Competitive learning: From interactive activation to adaptive resonance. Cognitive Science, 11,23-63.

- Grossberg, S. (Ed.). (1988). Neural net~'orks and natural intelligence. Cambridge, MA: MIT Press.

Grossberg, S., & Kuperstein, M. (1986). Neural dynamics ofadaptive sensory-motor control: Ballistic eye movements. Amsterdam: Elsevier/North-Holland.

Grossberg, S., & Levine, D. (1975). Some developmental and attentional biasesin the contrast enhancement and short term memory of recurrent neural networks. Journal ofTheoretical Biology, 53,

341-380.

- Grossberg, S., & Mingolla, E. (1985a). Neural dynamics ofform perception: Boundary completion, illusory figures, and neon color spreading. Psychological Review, 92, 173-211.
- Grossberg, S., & Mingolla, E. (1985b). Neural dynamics of perceptual grouping: Textures, boundaries, and emergent segmentations. Perception and Psychophysics, 38, 141-171.

Grossberg, S., & Mingolla, E. (1987). Neural dynamics of surface

perception: Boundary webs, illuminants, and shape-from-shading. Computer Vision, Graphics, and Image Processing, 37, 116-165.

Grossberg, S., & Pepe, J. (1971). Spiking threshold and overarousal effects in serial learning. Journal ofStatistical Physics, 3, 95-125.

Grossberg, S., & Schmajuk, N. A. (1987). Neural dynamics ofPavlovian conditioning: Conditioned reinforcement, habituation, and opponent processing. Psychobiology, 15, 195-240.

Grossberg, S., & Todorovic, D. (in press). Neural dynamics of I-D and 2-D brightness perception: A unified model of classical and recent phenomena. Perception and Psychophysics.

[Figure 674]

Nonlinear Neural Networks 59

[Figure 675]

[Figure 676]

Groves, P. M., Fenster,G. A., Tepper,J. M., Nakamura, S., & Young, S.J. (1981). Changes in d~aminergic terminal excitability induced by amphetamine and hatoperidol. Brain Research. 221,425-431.

Groves,P. M., & Tepper,J. M. (1983). Neuronal mechanisms of action of amphetamine. In I. Creese (Ed.), Stimulants: Neurochemical, behavioral and clinical perspectives(pp. 81-129). New York: Raven Press.

Halgren; E., Squires, N. K., Wilson, C. L., Rohrbaugh, J. W., Babb, T. L., & Crandall, P. H. (1980). Endogenous potentials generated in the human hippocampal formation and amygdala by infrequent events. Science, 210, 803-805.

Hary, J. M., & Massaro, D. W. (1982). Categorical results do not imply categorical perception. Perception and Psychophysics. 32, 409-418.

Hastings, S. P.(1976). The existence of periodic solutions to Nagumo's equation. Qllarterly Journal ofMathematics, 27, 123-134.

Hastings, S. P. (1982). Single and multiple pulse waves for the FitzHugh-Nagumo equations. SIAM Journal ofApplied Mathematics. 42,247-260.

Hebb, D. O. (1949). The organization ofbehavior. New York: Wiley. Hecht-Nielsen, R. (1986). Performance limits of optical, electro-op-

tical, and electronic neurocomputers. In H. Szu (Ed.), Hybrid and optical computing (pp. 277-306). Bellingham, WA: Society of Photo-Optical Instrumentation Engineers.

Helmholtz, H. von (1962). Treatise on physiological optics (J. P. C. Southall, Trans.). New York: Dover. (Original work published in 1866)

Hestenes, D. (1987). How the brain works: The next great scientific revolution. In C. R. Smith (Ed.), Maximum entropy in Bayesian spectral analysis and estimation problems. Boston: Reidel Press.

Hilgard, E. R., & Bower, G. H. (1975). Theories oflearning (4th ed.). Englewood Cliffs, NJ: Prentice-Hall. Hinton, G. E., & Anderson, J. A. (Eds.). (1981). Parallel mod.el.~ of associative memor}( Hillsdale, NJ: Erlbaum.

Hirsch, M. W. (1982). Systems of differential equations that are competitive or cooperative, I: Limit sets. SIAM Journal of Mathematical Analysis. 13, 167-179.

Hirsch, M. W. (1985 )..Systems of differential equations that are competitive or cooperative, II: Convergence almost everywhere. SIAM Journal ofMathematical Analysis. 16,423-439.

Hodgkin, A. L. (1964). The conduction ofthe nervous impulse. Liverpool: Liverpool University.

Hodgkin, A. L., & Huxley, A. F. (1952). A quantitative description of membrane current and its application to conduction and excitation in nerve. Journal ofPhysiolog): 117,500-544.

Hodgson, J. E. P.(Ed.). (1983). Oscillations in mathematical biology. New York: Springer-Verlag.

Holst, E. von, & Mittelstaedt, H. (1950). The reafference principle: Interaction between the central nervous system and the periphery. Naturwissenschafien. 37,464-476.

Hopfield, J. J. (1982). Neuronal networks and physical systems with emergent collective computational abilities. Proceedings of the National Academy ofSciences. 79, 2554-2558.

Hopfield, J. J. (1984). Neurons with graded response have collective computational properties like those of two-state neurons. Proceedings ofthe National Academy ofSciences. 81, 3058-3092. H~field, J. E., & Tank, D. W. (1985). "Neural" computation of de-

cisions in ~timization problems. Biological Cybernetics. 52, 141152. Hopfield, J. J., & Tank, D. W. (1986). Computing with neural circuits: A model. Science. 233, 625-633. Hurvich, L. M. (1981). Colour vision. Sunderland, MA: Sinauer Associates.

Ito, M. (1974). The control mechanisms of cerebellar motor systems. In F. O. Schmitt & F. G. Worden (Eds.), The neurosciences third studyprogram (pp. 293-303). Cambridge, MA: MIT Press.

Ito, M. (1982). Cerebellar control of the vestibulo-ocular reflexAround the flocculus hypothesis. Annual Review ofNeuroscience. 5, 275~296.

[Figure 677]

Ito, M. (1984). The cerebellum and neural control. New York: Raven Press. Iverson, G. J., & Pavel, M. (1981). Invariant properties of masking

phenomena in psychoacoustics and their theoreticai consequences. In S. Grossberg (Ed.), Mathematical psychology and psychophysiology. Providence, RI: American Mathematical Society.

Kaczmarek, L. K., & Babloyantz, A. (1977). Spatiotemporal patterns in epileptic seizures. Biological Cybernetics, 26, 199-208. Kandel, E. R., & Schwartz, J. H. (1981). Principles ofneural science. New York: Elsevier/North-Holland.

Kasamatsu, T., & Pettigrew, J. D. (1976). Depletion of brain catecholamines: Failure of ocular dominance shift after monocular occlusion in kittens. Science, 194,206-209.

Katz, B. (1966). Nerve, muscle, and synapse. New York: McGraw-

Hill.

Kilmer, W. L. (1972). On some realistic constraints in prey-predator mathematics. Journal of Theoretical Biology, 36, 9-22. Kirkpatrick, S., Gelatt, C. D., & Vecchi, M. P. (1982). Optimization

bysimulated annealing. IBM Thomas J. Watson Research Center, Yorktown Heights, NY.

Kirkpatrick, S., Gelatt, D. D., & Vecchi, M. P.(1983). Optimization by simulated annealing. Science, 220,671-680. Koenigsberger, L. (1906). Hermann von Helmholtz (F. A. Welby, Trans.). Oxford: Clarendon Press. Kohonen, T. (1971). A classof randomly organized associative memories. Acta Polytechnica Scandinavica, El. 25. Kohonen, T. (1977). Associative memory-A system-theoretical approach. New York: Springer-Verlag. Kohonen, T. (1984). Self-organization and associative memory. New York: Springer-Verlag. Kosko, B. (1987). Bidirectional associative memories. Manuscript submitted for publication.

Kosko, B., & Guest, C. (in press). Optical bidrectional associative memories. Societyfor Photo-optical and Instrumentation Engineering (SPIE) Proceedings: Image Understanding, 758.

Land, E. H. (1977). The retinex theory of color vision. Scientific American, 237, 108-128.

Levine, D. S. (1979). Existence of a limiting pattern for a system of nonlinear equations describing inter-population competition. Bulletin ofMathematical Biolog}\ 41, 617-628.

Levine, D. S. (1983). Neural population modeling and psychology:

-A review. Mathematical Biosciences, 66, 1-86.

Levine, D. S., & Grossberg, S. (1976). Visual illusions in neural networks: Line neutralization, tilt aftereffects, and angle expansion. Journal ofTheoretical Biolog}\ 61,477-504.

Levy, W. B. (1985). Associative changes at the synapse: LTP in the hippocampus. In W. B. Levy, J. Anderson, & S. Lehmkuhle (Eds.), Synaptic modification, neuron selectivity, and nervous system organization (pp. 5-33). Hillsdale, NJ: Erlbaum.

Levy, W. B., Brassel,S. E., & Moore, S.D. (1983). Partial quantification of the associative synaptic learning rule of the dentate gyrus. Neuroscience, 8, 799-808.

Levy, W. B., & Desmond, N. L. (1985). The rules of elemental synaptic plasticity. In W. B. Levy, J. Anderson, & S. Lehmkuhle (Eds.), Synaptic modification, neuron selectivity, and nervous system organization (pp. 105-121). Hillsdale, NJ: Erlbaum.

Lotka, A. J. (1956). Elements of mathematical biology. New York: Dover. MacArthur, R. H. (1970). Speciespacking and competitive equilibrium for many species. Theoretical Population Biology, 1, I-II.

Mach, E. (1914). The analysis ofsensation and the relation of the physicgl to the psychical (C. M. Williams, Trans., revised by S. Waterlow). London: Open Court Publishing.

MalsbUJi, C. von der (1973). Self-organization of orientation sensitive cells in the striate cortex. Kybernetik, 14,85-100. Marr, D. (1969). A theory of cerebellar cortex. Journal ofPhysiology (London), 202,437-470. May,R. M., & Leonard, W.J. (1975). Nonlinear aspectsof competition

[Figure 678]

60 S. Grossberg

[Figure 679]

[Figure 680]

between three species. SIAM Journal on Applied Mathematics. 29, 243-253.

McClelland, J. L. (1987). The case for interactionism in language processing. Preprint.

McClelland, J. L., & Rumelhart, D. E. (1981). An interactive activation model of context effects in letter perception, Part I: An account of basic findings. Psychological Review. 88, 375-407.

McClelland, J. L., & Rumelhart, D. E. (Eds.). (1986). Parallel distributed processing (Vol. II). Cambridge, MA: MIT Press.

McCormick, D. A., & Thompson, R. F. (1984). Cerebellum: Essential involvement in the classically conditioned eyelid response.Science. 223, 296-299.

McCulloch, W. S., & Pitts, W. (1943). A logical calculus of the ideas immanent in nervous activity. Bulletin ofMathematical Biophysics.5,115-133.

McEliece, R. J., Posner, E. C. Rodemich, E. R., & Venkatesh, S. S.

(1986). The capacity of the Hopfield associative memory. IEEE Transactions in Information Theory.

Miller, J. L., & Liberman, A. M. (1979). Some effectsof later-occurring information on the perception of stop consonant and semivowel. Perception and Ps)'Chophysics.25,457-465.

Mollon, J. D., & Sharpe, L. T. (Eds.). (1983). Colour vision. New York: Academic Press.

Mueller, P., Martin, T., & Putzrath, F. (1962). General principles of operations in neuron nets with application to acoustical pattern recognition. In E. E. Bernard & M. R. Kare (Eds.), Biological prototypes and synthetic systems(Vol. I, pp. 192-212). New York:

Plenum Press. Nathan, 0., & Norden, H. (Eds.). (1960). Einstein on peace. New York: Schocken Books.

Niedzwiecki, D. M., Mailman, R. B., & Cubeddu, L. X. (1984). Greater potency of mesoridazine and sulforidazine compared with the parent compound, thioridazine, on striatal dopamine autoreceptors. Journal ofPharmacology and Experimental Therapeutics. 228,636-639.

Optican, L. M., & Robinson, D. A. (1980). Cerebellar-dependent adaptive control of primate saccadic system. Journal ofNeurophysiology. 44, 1058-1076.

Parker, D. B. (1982, October). Learning-logic (Invention Report 58164, File I). Office of Technology Licensing, Stanford University.

- Parker, D. B. (1985, April). Learning-Logic. TR-47. Center for Computational Research in Economics and Management Science,MIT.
- Parker, D. B. (1986). A comparison of algorithms for neuron-like cells. In J. S. Denker (Ed.), Neural networks for computing (pp. 327-332). New York: American Institute of Physics.

Pastore, R. E. (1981). Possible psychoacoustic factors in speech perception. In P. D. Eimas & J. L. Miller (Eds.), Perspectives'in the

study ofspeech(pp. 165-205). Hillsdale, NJ: Erlbaum.

Pettigrew, J. D., & Kasamatsu, T. (1978). Local perfusion of noradrenaline maintains visual cortical plasticity. Nature. 271,761763.

Platt, J. C., & Hopfield, J. J. (1986). Analog decoding using neural networks. In J. S. Denker (Ed.), Neural networks for computing (pp. 364-369). New York: American Institute of Physics.

Plonsey, R., & Fleming, D. G. (1969). Bioelectric phenomena. New York: McGraw-Hili. Poggio, T., & Koch, C. (1987). Synapses that compute motion. Scientific American. 256, 46-52.

Psaltis, D., & Park, C. H. (1986). Nonlinear discriminative functions and associative memories. In J. S. Denker (Ed.), Neural networks for computing. New York: American Institute of Physics.

Ratliff, F. (1965). Mach bands: Quantitative studies on neural net~rks in the retina. New York: Holden-Day.

Ratliff, F., Hartline, H. K., & Miller, W. H. (1963). Spatial and temporal aspects of retinal inhibitory interactions. Journal ofthe Optical Society ofAmerica. 53, 110-120.

Rauschecker, J. P., & Singer, W. (1979). Changes in the circuitry of the kitten's visual cortex are gated by postsynaptic activity. Nature. 280, 58-60.

[Figure 681]

Rescorla, R. A., & Wagner, A. R. (1972). A theory of Pavlovian conditioning: Variations in the effectiveness of reinforcement and nonreinforcement. In A. H. Black & W. F. Prokasy (Eds.), Classical condilioning. II: Currem research and theory New York: Appleton-

Century-Crofts. Ricciardi, L., & Scott, A. (Eds.). (1982). Biomathematics in 1980. Amsterdam: North-Holland.

Ron, S., & Robinson, D. A. (1973). Eye movements evoked by cerebellar stimulation in the alert monkey. Journal ofNeurophysiology, 36, 1004-1021.

Rosenblatt, F. (1962). Principles ofneurodynamics. Washington, DC: Spartan Books.

Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). Learning internal representations by error pr~agation. In D. E. Rumelhart & J. L. McClelland (Eds.), Parallel distribuled processing. Cambridge, MA: MIT Press.

Rumelhart, D. E., & McClelland,J. L. (1982). An interactive activation model of context effects in letter perception, Part 2: The contextual enhancement effect and some tests and extensions of the model. Psychological Reviell; 89, 60-94.

Rumelhart, D. E., & McClelland, J. L. (Eds.). (1986). Parallel dislributed processing (Vol. I). Cambridge, MA: MIT Press. Rumelhart, D. E., & Zipser, D. (1985). Feature discovery by competitive learning. Cognilive Science, 9, 75-112.

Samuel, A. G., van Santen, J. P. H., & Johnston, J. C. (1982). Length effects in word perception: We is better than I but worse than you or them. Journal ofExperimental Psychology: Human Percepi ion and Performance, 8, 91-105.

Samuel, A. G., van Santen,J. P. H., & Johnston, J. C. (1983). Reply to Matthei: We really is worse than you or them, and so are ma and pa. Journal ofExperimemal Psychology: Human Perceplion and Performance. 9, 321-322.

Sawusch,J. R., & Nusbaum, H. C. (1979). Contextual effects in vowel perception, I: Anchor-induced contrast effects. Perceplion and Psychophysics, 25, 292-302.

Sawusch,J. R., Nusbaum, H. C., & Schwab,E. C. (1980). Contextual effects in vowel perception, II: Evidence for two processing mechanisms. Perception and Psychophysics. 27, 421-434.

Schwab, E. C., Sawusch, J. R., & Nusbaum, H. C. (1981). The role of second formant transitions in the stop-semivowel distinction. Perception and Psychophysics, 29,121-128.

Scott, A. C. (1977). Neurophysics. New York: Wiley-Interscience. Sejnowski, T. J., & Rosenberg, C. R. (1986, January). NETtalk: A

parallel network thai learns 10 read aloud. Johns Hopkins University, MD.

Siever,L., & Sulser,F. (1984). Regulations of amine neurotransmitter systems: Implication for the major psychiatric syndromes and their treatment. Psychopharmacology Bulletin, 20, 500-504.

Singer, W. (1982). The role of attention in developmental plasticity. Human Neurobiology, 1,41-43.

Singer,W. (1983). Neuronal activity as a shaping factor in the selforganization of neuron assemblies. In E. Basar,H. flohr, H. Haken, &A. J. Mandell (Eds.), Synergetics oflhebrain(pp. 89-101). New York: Springer-Verlag.

Sperling, G. (1981). Mathematical models of binocular vision. In S. Grossberg (Ed.), Malhematical psychology and psychophysiology (pp. 281-300). Providence, RI: American Mathematical Society.

Sperling, G., & Sondhi, M. M. (1968). Model for visual luminance discrimination and flicker detection. Joumal ofthe Optical Society ofAmerica, 58, 1133-1145. Studdert-Kennedy, M. (1980). Speech perception. Language and Speech, 23, 45-66.

Sutton, R. S., & Barto, A. G. (1981). Toward a modern theory of adaptive networks: Expectation and prediction. Psychological Re-

view,88, 135-170.

Szu, H. (1986). Three layers of vector outer product neural networks for ~tical pattern recognition. In H. Szu (Ed.), OPlical and hybrid computing (pp. 312-330). Bellingham, WA: Society ofPhoto-Optical Instrumentation Engineers.

[Figure 682]

Nonlinear Neural Networks 61

[Figure 683]

[Figure 684]

Takeuchi, Y., Adachi, N., & Tokumaru, H. (1978). The stability of generalized Volterra equations. Journal q( Mathematical Analysis and Applications. 62,453-473.

Tepper, J. M., Young, S. J., & Groves, P. M. (1984). Autoreceptormediated changes in dopaminergic terminal excitability: Effects of increases in impulse flow. Brain Research. 309, 309-316.

Venkatesh, S. S. (1986). Epsilon capacity of neural networks. In J. S. Denker (Ed.), Neural networksfor computing. New York: American Institute of Physics.

Vilis, T., & Hore, J. (1986). A comparison of disorders in saccades

and in fast and accurate elbow flexions during cerebellar dysfunction. In H. J. Freund, U. Buttner, B. Cohen, &J. Noth (Eds.), The oculomotor and skeletal motor systems: Differences and similarities. N~ York: Elsevier.

Vilis, T., Snow, R., & Hore, J. (1983). Cerebellar saccadic dysmetria is not equal in the two eyes. Experimental Brain Research. 51,

343-350.

[Figure 685]

Werblin, F. S. (1971). Adaptation in a vertebrate retina: Intracellular recordings in Necturus. Journal ofNeurophysiology, 34,228-241.

Werbos, P. (1974). Beyond regression: New tools for prediction and analysis in the behavioral sciences. Unpublished doctoral thesis, Harvard University, Cambridge, MA.

Werbos, P. (1982). Applications of advances in nonlinear sensitivity analysis. In A. V. Balakrishnan, M. Thoma, R. F. Drenick, & F. Kozin (Eds.), Lecture notes in control and information sciences. Vol. 38: System modeling and optimization. Proceedings of the 10th IFIP Conference. New York: Springer-Verlag.

Widrow, B. (1962). Generalization and information storage in networks of Adaline neurons. In M. C. Yovits, G. T. Jacobi, & G. D. Goldstein (Eds.), Selforganizing systems. Washington, DC: Spartan Books.

Wilson, H. R., & Cowan, J. D. (1972). Excitatory and inhibitory interactions in localized populations of model neurons. Biophysical Journal. 12, 1-24.

