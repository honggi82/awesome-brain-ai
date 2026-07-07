# Digital Twin of Wireless Systems: Overview, Taxonomy, Challenges, and Opportunities

Latif U. Khan, Zhu Han, Fellow, IEEE, Walid Saad, Fellow, IEEE, Ekram Hossain, Fellow, IEEE, Mohsen Guizani, Fellow, IEEE, Choong Seon Hong, Senior Member, IEEE

## arXiv:2202.02559v1[cs.NI]5Feb2022

Abstract—Future wireless services must be focused on improving the quality of life by enabling various applications, such as extended reality, brain-computer interaction, and healthcare. These applications have diverse performance requirements (e.g., user-deﬁned quality of experience metrics, latency, and reliability) that are challenging to be fulﬁlled by existing wireless systems. To meet the diverse requirements of the emerging applications, the concept of a digital twin has been recently proposed. A digital twin uses a virtual representation along with security-related technologies (e.g., blockchain), communication technologies (e.g., 6G), computing technologies (e.g., edge computing), and machine learning, so as to enable the smart applications. In this tutorial, we present a comprehensive overview on digital twins for wireless systems. First, we present an overview of fundamental concepts (i.e., design aspects, high-level architecture, and frameworks) of digital twin of wireless systems. Second, a comprehensive taxonomy is devised for both different aspects. These aspects are twins for wireless and wireless for twins. For the twins for wireless aspect, we consider parameters, such as twin objects design, prototyping, deployment trends, physical devices design, interface design, incentive mechanism, twins isolation, and decoupling. On the other hand, for wireless for twins, parameters such as, twin objects access aspects, security and privacy, and air interface design are considered. Finally, open research challenges and opportunities are presented along with causes and possible solutions.

Index Terms—Digital twin, wireless system, machine learning, federated learning, virtual modeling.

I. INTRODUCTION Emerging Internet of Everythings (IoE) applications, such

- as haptics, brain-computer interaction, ﬂying vehicles, and extended reality (XR), among others, will enable a merger of digital and physical worlds [1]–[4]. These IoE applications have widely diverse requirements (e.g., user experience, reliability, and latency). To meet these diverse requirements, there

L. U. Khan and C. S. Hong are with the Department of Computer Science & Engineering, Kyung Hee University, Yongin-si 17104, South Korea.

Zhu Han is with the Electrical and Computer Engineering Department, University of Houston, Houston, TX 77004 USA, and also with the Computer Science Department, University of Houston, Houston, TX 77004 USA, and the Department of Computer Science and Engineering, Kyung Hee University, South Korea.

Walid Saad is with the Wireless@VT, Bradley Department of Electrical and Computer Engineering, Virginia Tech, Blacksburg, VA 24061 USA.

M. Guizani is with the Department of Computer Science and Engineering

- at Qatar University, Doha, Qatar.

E. Hossain is with Department of Electrical and Computer Engineering at University of Manitoba, Winnipeg, Canada.

is a need to assist the wireless systems by novel technologies. These new technologies will enable the wireless systems to meet the diverse requirements via enabling the two main trends: self-sustaining wireless systems and proactive-onlinelearning-enabled systems [5]. Generally, wireless systems rely on intelligent, seamless, and ubiquitous connectivity for meeting the diverse requirements of end-users. To enable wireless systems with these features, there is a need for self-sustaining wireless systems. Self-sustaining wireless systems will offer efﬁcient management of wireless systems with minimum possible intervention from the network operators/end-users. Such self-sustaining wireless systems can use optimization theory, game theory, and graph theory, among others to enable IoE services. On the other hand, IoE services have highly dynamic requirements in terms of user-deﬁned metrics, latency, data rate, and reliability, among others. To meet these highly dynamic and extreme requirements, there is a need to efﬁciently enable interaction between various players of wireless systems. These players are security-related technologies (e.g., blockchain), computing technologies (e.g., edge computing), and wireless channel resources (e.g., terahertz band, millimeter wave). Therefore, upon request from the end-users, there is a need to provide them instant services especially for strict latency applications (e.g., extended reality). To enable such kinds of instant services to end-users, we must perform intelligent analytics (i.e., proactive learning) prior to service request for efﬁcient resource management. Therefore, it is necessary to propose proactive-online learning-based wireless systems.

To design a wireless system by following the aforementioned trends of self-sustaining wireless systems and proactiveonline-learning-enabled systems, we can create a digital twin to represent the wireless system [5]. A digital twin will use a virtual representation of the physical system to enable IoE applications [5]–[7]. In detail, a digital twin-based wireless system will use optimization theory, game theory, and machine learning in addition to the virtual representation of a wireless system. Additionally, to enable transparent and immutable handling of data, a digital twin-based system will use blockchain. An overview of digital twin-based wireless systems is given in Fig. 1. We can divide the twin-based wireless systems architecture into physical interaction layer and twins layer. The physical interaction layer covers all the physical objects necessary for a given wireless system application, such as end-devices, edge/cloud servers, base stations, and core network elements, among others. On the other hand, the twin layer is a logical layer that contains logical

Physicalinteractionlayer

|[Figure 1]<br><br>[Figure 2]<br><br>|[Figure 3]<br><br>[Figure 4]<br><br>|
|---|
<br><br>[Figure 5]<br><br>[Figure 6]<br><br>|[Figure 7]<br><br>[Figure 8]<br><br>|
|---|
<br><br>[Figure 9]<br><br>[Figure 10]<br><br>|[Figure 11]<br><br>[Figure 12]<br><br>|
|---|
<br><br>[Figure 13]<br><br>[Figure 14]<br><br>|[Figure 15]<br><br>[Figure 16]<br><br>|
|---|
<br><br>[Figure 17]<br><br>[Figure 18]<br><br>|[Figure 19]<br><br>[Figure 20]<br><br>|
|---|
<br><br>[Figure 21]<br><br>[Figure 22]<br><br>|[Figure 23]<br><br>[Figure 24]<br><br>|
|---|
<br><br>[Figure 25]<br><br>[Figure 26]<br><br>|[Figure 27]<br><br>[Figure 28]<br><br>|
|---|
<br><br>||Blockchain<br><br>network|
|---|
<br><br>Blockchain<br><br>network|
|---|
<br><br>Blockchain<br><br>network<br><br>Digital twin<br><br>[Figure 29]<br><br>[Figure 30]<br><br>[Figure 31]<br><br>[Figure 32]<br><br>[Figure 33]<br><br>[Figure 34]<br><br>[Figure 35]<br><br>[Figure 36]<br><br>|[Figure 37]<br><br>Instructions|
|---|
<br><br>||[Figure 38]<br><br>Machine learning<br><br>models|
|---|
|
|---|
|[Figure 39]<br><br>Optimization schemes|
|[Figure 40]<br><br>|[Figure 41]<br><br>Game-theoretic<br><br>schemes|
|---|
|
<br><br>Virtual model|
|---|

Twinlayer

Blockchain

network

End-devices data/

Control instructions/

learning model updates

learning model updates

|[Figure 42]<br><br>[Figure 43]<br><br>[Figure 44]<br><br>[Figure 45]<br><br>[Figure 46]<br><br>[Figure 47]<br><br>[Figure 48]<br><br>[Figure 49]<br><br>[Figure 50]<br><br>[Figure 51]<br><br>[Figure 52]<br><br>[Figure 53]<br><br>[Figure 54]<br><br>[Figure 55]<br><br>[Figure 56]<br><br>[Figure 57]<br><br>[Figure 58]<br><br>[Figure 59]<br><br>[Figure 60]<br><br>[Figure 61]<br><br>[Figure 62]<br><br>[Figure 63]<br><br>[Figure 64]<br><br>[Figure 65]<br><br>[Figure 66]<br><br>[Figure 67]<br><br>[Figure 68]<br><br>[Figure 69]<br><br>[Figure 70]<br><br>[Figure 71]<br><br>[Figure 72]<br><br>[Figure 73]<br><br>[Figure 74]<br><br>[Figure 75]<br><br>[Figure 76]<br><br>GPS satellite<br><br>[Figure 77]<br><br>[Figure 78]<br><br>[Figure 79]<br><br>[Figure 80]<br><br>[Figure 81]<br><br>Edge computing enabled road<br><br>side unit<br><br>6G base station<br><br>[Figure 82]<br><br>[Figure 83]<br><br>[Figure 84]<br><br>[Figure 85]<br><br>[Figure 86]<br><br>[Figure 87]<br><br>[Figure 88]<br><br>[Figure 89]<br><br>SDN/NFV based core network Millimeter<br><br>[Figure 90]<br><br>[Figure 91]<br><br>[Figure 92]<br><br>[Figure 93]<br><br>[Figure 94]<br><br>wave BS<br><br>[Figure 95]<br><br>[Figure 96]<br><br>[Figure 97]<br><br>[Figure 98]<br><br>[Figure 99]<br><br>[Figure 100]<br><br>[Figure 101]<br><br>[Figure 102]<br><br>[Figure 103]<br><br>[Figure 104]<br><br>[Figure 105]<br><br>[Figure 106]<br><br>[Figure 107]<br><br>[Figure 108]<br><br>[Figure 109]<br><br>Smart<br><br>healthcare<br><br>[Figure 110]<br><br>[Figure 111]<br><br>[Figure 112]<br><br>Waste recycling<br><br>plant<br><br>[Figure 113]<br><br>[Figure 114]<br><br>hospit<br><br>al<br><br>[Figure 115]<br><br>[Figure 116]<br><br>hospital<br><br>AR glasses<br><br>[Figure 117]<br><br>[Figure 118]<br><br>[Figure 119]<br><br>[Figure 120]<br><br>[Figure 121]<br><br>[Figure 122]<br><br>[Figure 123]<br><br>[Figure 124]<br><br>[Figure 125]<br><br>[Figure 126]<br><br>[Figure 127]<br><br>[Figure 128]<br><br>[Figure 129]<br><br>Big Data<br><br>[Figure 130]<br><br>[Figure 131]<br><br>[Figure 132]<br><br>[Figure 133]<br><br>[Figure 134]<br><br>[Figure 135]<br><br>cloud<br><br>[Figure 136]<br><br>[Figure 137]<br><br>[Figure 138]<br><br>[Figure 139]<br><br>[Figure 140]<br><br>[Figure 141]<br><br>Smart<br><br>airport<br><br>[Figure 142]<br><br>[Figure 143]<br><br>[Figure 144]<br><br>[Figure 145]<br><br>[Figure 146]<br><br>[Figure 147]<br><br>[Figure 148]<br><br>[Figure 149]<br><br>[Figure 150]<br><br>[Figure 151]<br><br>Road accident<br><br>[Figure 152]<br><br>[Figure 153]<br><br>[Figure 154]<br><br>[Figure 155]<br><br>[Figure 156]<br><br>[Figure 157]<br><br>[Figure 158]<br><br>[Figure 159]<br><br>[Figure 160]<br><br>[Figure 161]<br><br>[Figure 162]<br><br>|[Figure 163]<br><br>[Figure 164]<br><br>[Figure 165]<br><br>[Figure 166]<br><br>[Figure 167]<br><br>1 2 3 4 5|
|---|
<br><br>Smart parking<br><br>|
|---|

Fig. 1: Conceptual overview of a digital twin for wireless systems.

twin objects. More detailed discussion about the creation of twin objects will be provided in Sections II-C and III-G). Next, we discuss research trends and statistics for digital twins.

- A. Market Statistics and Research Trends

The IoT market will grow at a Compound Annual Growth Rate (CAGR) of 26.9% during the period of 2017 − 2022 [8]. The market share will grow from 170.6 Billion USD in 2017 to 561.0 Billion USD in 2022. The main causes of an increase in the IoT market are smart buildings, smart grids, smart industries, intelligent transportation. The key players of IoT markets are General Electric (US), Bosch Software Innovation GmbH (Stuttgart, Germany), Amazon Web Services Inc. (US), Hewlett-Packard Enterprise (US), Google Inc. (US), PTC Inc. (US), International Business Machine (IBM) Corporation (US), Oracle Corporation (US), Microsoft Corporation (US), Cisco Systems, Inc. (US), SAP SE (Walldorf, Germany), and

Intel Corporation (US). Among different regions, such as Latin America, MEA, APAC, Europe, and North America, it is expected that China will lead the IoT market in APAC region [9]. Globally, the US will have the highest share in IoT markets by 2029 [10] and will be followed by China, Japan, and Germany.

According to statistics, the market of digital twins will grow at a CAGR rate of 58% during the period of 2020−2026 [11]. The market value of digital twin in 2020 was 3.1 Billion USD and it will reach 48.2 Billion USD by 2026. The key factors in the rise of the digital twin market include the rise in the demand for manufacturing monitoring assets, intelligent analytics-based healthcare systems, smart warehouse, and intelligent transportation, among others [11], [12]. Due to the increasing importance of digital twin in the development of smart applications, various countries, such as Brazil, Norway, Mexico, China, Japan, South Korea, and Singapore, are trying

to implement twin based systems. The key market players of digital twin market are SWIM.AI (USA), Robert Bosch (Germany), ANSYS (USA), Siemens AG (USA), Oracle (USA), SAP (Germany), Microsoft Corporation (USA), PTC (USA), IBM (USA), and General Electric (USA). Additionally, system digital twin among all kinds, such as product digital twin, process digital twin, and system digital twin will have the highest market share by 2026. From the aforementioned discussion, it is clear that both digital twin and IoT will serve as one of the promising areas for future research.

- B. Existing Surveys and Tutorials Few surveys and tutorials have reviewed digital twins [5],

- [13]–[17]. The authors in [13] focused on digital twin in the context of IoT. They discussed the digital twin concept with architectural elements as well as key enablers. Another work
- [14] surveyed the key technologies along with the use case of digital twins towards enabling IoT applications. Barricelli et al. in [15] presented the key concepts, applications, and design implications. Furthermore, they presented few open research challenges. On the other hand, the works in [16] and [17] focused mainly on the role of blockchain in enabling digital twins. The authors in [16] presented the key beneﬁts of using blockchain for digital twins. Additionally, they devised taxonomy and presented a few open challenges. Suhail et al. in [17] systematically reviewed the role of blockchain in enabling digital twins. The work in [5] presented the role of digital twin towards enabling of 6G wireless system. Additionally, the authors provided architectural trends for twin-based wireless systems. Different from the existing surveys and tutorials on digital twins [5], [13]–[17], the goal of our survey is to comprehensively discuss the fellowship of digital twin and wireless systems, as given in Table I. We present the fundamentals of digital twins and derive a general deﬁnition in the context of wireless systems. A general architecture along with design aspects is presented. We also derive a comprehensive taxonomy of digital twins-based wireless systems and presented open research challenges.

- C. Our Tutorial

Our tutorial (see organization in Fig. 2) aims to answer the following questions:

- • What is a digital twin in the context of wireless systems? What are the main design aspects of digital twin of wireless systems?
- • How does one use digital twin for enabling wireless systems? What are the challenges for digital twin signaling over the wireless channel?
- • How can we classify the research areas for digital twin of wireless system?
- • What are the open research challenges and their preferable solutions in enabling the digital twins of wireless systems?

The main focus of our tutorial is to consider two main aspects: digital twins for wireless and wireless for twins. Twin for wireless deals with the role of the digital twin in enabling

|Digital twin and wireless systems| |
|---|---|
| | |

|Introduction<br><br>(SectionI) {<br><br>A. Market statistics and research trends<br>B. Existing surveys and tutorials<br>C. Our tutorial<br>| |
|---|---|
| | |

|Digital twinning: Concept, key design aspects and<br><br>frameworks<br><br>(Section II)<br><br>{<br><br>A. Concept<br>B. Design aspects<br>C. High-level architecture<br>D. Frameworks<br>E. Summary and lessons learned<br>|
|---|

|Taxonomy:<br><br>Twins for<br><br>wireless (Section III)<br><br>{<br><br>A. Twins isolation<br>B. Decoupling<br>C. Interfaces design<br>D. Twin objects design<br>E. Twin objects prototyping<br>F. Incentive mechanism<br>G. Twins deployment trends<br>H. Physical end-devices design<br>I. Summary and lessons learned<br>| |
|---|---|
| | |

|Taxonomy: Wireless for<br><br>twins<br><br>(Section IV)<br><br>{<br><br>A. Air interface design<br>B. Twin objects and end-devices communication<br>C. Security and privacy<br>D. Summary and lessons learned<br>| |
|---|---|
| | |

|Open research<br><br>challenges (Section V)<br><br>{<br><br>A. Dynamic twins<br>B. Interoperability for twin objects migration<br>C. True prototyping of twin objects<br>D. Incentive mechanism for twinning<br>E. Twinning forensics and security<br>F. Efficient twin objects chaining<br>| |
|---|---|
| | |

|Conclusions and future prospects (Section VI)|
|---|

Fig. 2: Organization of the tutorial.

wireless systems. Wireless for twins deals with the efﬁcient utilization of wireless resources for enabling effective twin signalings over a wireless link. Different from the existing works [5], [13]–[17], we present a detailed concept, key design aspects, and high-level architecture of digital twins for wireless systems. We also present a comprehensive taxonomy that covers both twins for wireless and wireless for twins aspects. Furthermore, novel open research challenges with their causes and solutions are provided. Our contributions are summarized as follows.

- • We present a concept, key design aspects, and high-level architecture for digital twin of wireless systems.
- • A comprehensive taxonomy considering both twins for wireless and wireless for twins, is provided. We consider twin objects design, twin objects prototyping, twin objects deployment trends, interface design, incentive mechanism, twin objects access aspects, twins isolation, decou-

TABLE I: Summary of existing surveys and tutorials with their primary focus.

Reference Wireless for twins

Twins for wireless

Taxonomy Remark

Minerva et al. [13]

This survey comprehensively presents technical features, scenarios and architectural models for digital twin in the context of IoT.

Wu et al. [14] This survey presents the twin fundamentals, as well

as key enabling technologies, and open challenges. Barricelli et

- al. [15]

This paper presents the fundamentals, implementation details, and applications of digital twin.

Yaqoob et

- al. [16]

The authors discussed the role of blockchain towards enabling digital twin. Additionally, taxonomy was also devised.

Suhail et al. [17] Blockchain-based twins are discussed. Furthermore, research trends and future directions were also presented.

Khan et al. [5] This tutorial presents the key design requirements, architectural trends, and future directions for digitaltwin-enabled 6G.

Our Tutorial N.A

pling, security and privacy, and AI-enabled air interface design, as parameters.

• Several open challenges are presented. Moreover, promis-

ing solutions are also provided.

II. DIGITAL TWINS: CONCEPT, KEY DESIGN ASPECTS, AND FRAMEWORKS

- A. Concept

A digital twin is a virtual representation of the physical system serving as a digital counterpart [18], [19]. The main purpose of a digital twin is to jointly optimize the cost and performance of the overall process using various emerging technologies (e.g., virtual modeling, simulation technologies, blockchain, edge computing, cloud computing) and optimization tools (e.g., machine learning, game theory, graph theory). Digital twin provides proactive analysis of the physical process using various simulation tools (e.g., AMEsim, SimScale, Simulink [20], [21]), artiﬁcial intelligence, mathematical optimization, game theory, and graph theory, among others [5]. Such analyses enable us to optimize the overall design. Digital twin technology has gained signiﬁcant interest since 2002 when the ﬁrm, namely, Challenge Advisory hosted a presentation at University of Michigan [22]. They discussed the fundamental elements of a digital twin, such as virtual space, real space, and the information ﬂow between them. Prior to the event at the University of Michigan, the US space agency NASA proposed the use of a digital twin around 1960’s for analyzing the space systems at the ground.

Digital twins are categorized by various sources in many ways, as given in Table II. According to Siemens, a digital twin can be divided into product digital twins, production digital twins, and performance digital twins [23]. Furthermore, the twins can be categorized into status twin, simulation twin, and operational twin [24]. The classiﬁcation of twins by different sources is based on their objective and coverage

Network planning

IoE

device

Edge server

Resource

End-to-end IoE service

management

Single entity

Cloud server

Digital twin

New

service

twins

Multiple IoE services

Resource

Network

slicing

planning

Isolated

service twins

Wireless system devices management/

Legends Twin entity

network functions

Fig. 3: Conceptual overview of a digital twin for wireless systems.

(i.e, single entity or whole system). From all the types of twins [23]–[26], we generalize the deﬁnition and types of a twins for a wireless system, as shown in Fig. 3. Digital twin for 6G can be intended for a single entity (i.e, edge server management and IoE end-devices management), an end-to-end service (i.e., resource management, new service design, and network planning), and multi-services (i.e., resource slicing for different twins, isolation of different service twins, and network planning). From the aforementioned discussion, one can say that digital twin for 6G can enable analysis, design, and real-time monitoring with control of devices to enable IoE services for cost-efﬁcient and resource optimized operation.

The implementation process of a digital twin starts with the analysis of a physical system, as shown in Fig. 4. Such

TABLE II: Digital twin categories: source, type, and explanation.

Reference Category (deﬁned by source) Description by the source Key objective Siemens [23]

Product digital twins To use a digital for enabling a new product. This twin will offers us with the ability to make various experiments by varying different system parameters to analyze the cost, efﬁciency, and performance for a new product before it is actually manufactured.

New product design

Production digital twins To use a digital twin in process of manufacturing. Digital twins of the various components are tested for performance and cost. This will lead efﬁcient selection/placement of manufacturing process component in real time deployment.

Efﬁcient deployment of system components

Performance digital twins To use a digital twin for capturing and acting on operational data. This twin will enable smart plants (e.g., smart grid, smart industry) to operate in an efﬁcient way to optimize the cost and performance by using the generated data. This data can be further used by machine learning models and other techniques to enhance the twin performance.

Data analysis for performance enhancement

Standalone digital twins This twin refers to the virtual models of individual entities (e.g., Heating, ventilation, and air conditioning system in a smart home) of a system.

Modeling of a single entity.

Vercator [25]

Duplicated digital twins This twin refers to twin for optimized use of multiple stand-alone twins (e.g., car twins and smart industry twins).

Performance optimization of a component that is made of many twins in a complex system.

Enhanced digital twins This twin deals with modeling of complex systems that have a broad scale than those of a duplicate twin and will consist of multiple duplicate twins.

To enhance the performance of a complete system (e.g., 6G-based smart surveillance in a city).

Component twins This twin represents a single component in an entire system.

Single speciﬁc component in a system.

Tributech [26]

Asset twins It refers to twin that can manage the system that is made up of multiple component twins (e.g., autonomous car engine).

System multiple components.

System twins This twin scales by covering a large system (e.g., entire autonomous car).

Single system Process twins This twin models the entire process facility (e.g.,

Entire plant

autonomous car plant).

Status twin This twin is used to monitor the system (e.g., dashboards and simple alerting systems).

To monitor the phenomenon. Simulation twin It enables us analyze the system performance via

XMPRO [24]

To analyze the system performance.

simulation and provide insights into future states.

Operational twin It enables us to interact with the system and control the system for efﬁcient and cost performance.

To efﬁciently control the system.

analysis gives us insights into the system speciﬁcations, inputs, outputs, and environment dynamics. Next to physical system analysis, one can design a virtual system that represents the physical system. Modeling a virtual system requires careful design and requires overcoming many challenges. The challenges are an accurate representation of a system using a mathematical equations or using machine learning models. Additionally, some of the real-time system parameters (e.g., IoE device operating frequency, wireless channel conditions) are very difﬁcult to model accurately due to their uncertain nature with the time. Therefore, one must try to accurately estimate these parameters while performing the simulation of the virtual model. After virtual modeling, there is a need to verify the virtual design by simulating the virtual model and comparing the performance with the physical system. One must modify the virtual model in this phase to make the virtual model closest possible to the physical system. The ﬁnal phase is the operation phase that involves controlling the real-time system using a digital twin.

- B. Design Aspects

In this tutorial, we consider both aspects of digital twins and wireless systems, such as (a) twins for wireless and

Verification of the physical

Simulation of the virtual

model

model

Virtual model

of the IoE service

Analysis of the physical IoE service

Modify the model if it does

not meet the design criteria

|Digital twin design trend|
|---|

Fig. 4: Digital twin design steps.

(b) wireless for twins, as shown in Fig. 5. The twin for wireless deals with the design of twins to enable various network functions/ applications. On the other hand, wireless for twins deals with efﬁcient communication modeling to enable signaling for twins implementation. Twin for wireless mainly deals with the efﬁcient implementation of wireless system services (e.g., extended reality) using a digital twin. A twins-enabled wireless network will have a variety of

players to enable the successful operation of IoE services. These players are blockchain networks, edge/cloud servers, data decoupling interfaces, function decoupling interfaces, and physical devices. Furthermore, the requirements of various IoE applications are signiﬁcantly diverse. Therefore, special care must be taken while designing twin-based wireless systems to meet the diverse requirements.

Wireless for twins mainly deals with the wireless resource optimization for twinning over wireless networks. Wireless resources can be used in twinning for two operations: (a) twin objects training and (b) twin operation signalling. Twin training will use wireless resources to transfer the data and learning updates. For centralized learning, wireless channel is used to migrate the end-devices data to the shared storage (i.e., servers installed at the edge/cloud. However, some practical scenarios (e.g., autonomous driving cars) generate signiﬁcant amount of data frequently. Transferring such an enormous amount of data to the shared storage will use signiﬁcant amount of communication resources. To address this issue, one can use distributed learning (e.g., federated learning) that is based on sending of only learning model update rather than the whole data, and thus consumes fewer communication resources. To train digital twin models using distributed learning over wireless networks, signiﬁcant amount of resources will be required. Meanwhile, the wireless channel will degrade the performance of distributed learning-based twin model during the transfer of learning model updates between end-devices and aggregation server [27]. Additionally, variable latencies will be induced for transferring of learning model updates between devices and twin model servers due to different signal-to-interference-plus noise ratio (SINR). The SINR of devices depends on many factors, such as resource block bandwidth, interference from other users using same resource blocks, and distance between the device and twin model server. For a twin model update of size 𝑢 and channel throughput Γ, the transmission latency can be given by 𝑑 = 𝑢Γ. The transmission latency can be minimized by many ways, such as (a) reducing the size of twin model updates, (b) enhancing the throughput, and (c) improving the SINR. SINR can be enhanced by optimally performing wireless resource allocation, association of devices with edge/cloud server, and transmit power allocation [28], [29].

- C. High-Level Architecture

A high-level architecture of a digital twin for wireless systems based on logical twin objects is shown in Fig. 6 [5], [14], [30]. The architecture can be divided into three layers, such as physical devices interaction layer, twin objects layers, and services layer. The services layer contains interfaces for applications. One can request a service from a twin-based wireless system. In response to the user request, semantic reasoning schemes are used to translate the request. Then, the translated requests are passed to the next layers. Next, there is a twin layer that contains logical twin objects. Twin objects use a virtual representation of the physical object/ phenomenon. Representing a physical object/phenomenon using a virtual model faces some challenges. It is difﬁcult to exactly model

How to efficiently perform signaling for twin operation over a wireless channel?

How to propose exact virtual model of a physical system ?

[Figure 168]

How to perform efficient computing

How to efficiently manage and store the training data and twin pre-trained model using distributed ledger?

Wireless for twin

Twin for

and communication resource for end-

wireless

users?

[Figure 169]

How to enable various

How to efficiently

heterogeneous wireless system

decouple the network function for efficient management by twin?

components for twin operation?

Fig. 5: Digital twin and wireless system: design aspects and challenges.

the physical objects/ phenomenon. One can various ways, such as mathematical model, 3D model, and data-driven model [31], [32]. Representing a physical object using a mathematical model needs several assumptions [33]. Another way can be to use 3D modeling. However, both mathematical and 3D models may not accurately model the physical model/ phenomenon. To address these limitations, one can use datadriven models-based machine learning to effectively model the physical objects [34]–[37]. The selection of an effective machine learning model is challenging and the right selection of machine learning model consumes a signiﬁcant amount of time. Note that the twin layer objects can be implemented using container/s or virtual machine/s [5], [38]. Also, one can deploy twin objects either at the network edge or remote cloud. Implementing a twin object at the remote cloud can offer more computing power but at the cost of high latency [39], [40]. To address this issue, one can use a twin object based on the network edge. However, twin objects deployed at the network edge can have low computing power [41], [42]. Therefore, one must make a tradeoff between computing power and latency. The last layer is the devices’ physical interaction layer. The physical devices layer contains all the physical devices, such as end-devices, edge/cloud servers, base stations, miners, and core network switches, among others. Note that there must effective interfaces between different layers of the twins-based wireless system. These interfaces can be twin to physical object interface, twin to twin interface, and twin to service interface.

Now we discuss the reliability of digital-twin-enabled wireless systems. There are two issues: twin reliability and twin-based service reliability [43]. Twin reliability refers to the operation of twin without minimum possible interruption due to failure of edge/cloud server running the twin object. An IoT service based on a single twin deployed at the cloud has lower reliability than an IoT service based on multiple twin objects deployed at edge servers. However, the management of multiple twins for a certain service will offer more complexity. Therefore, we must make a tradeoff between the twin reliability and complexity. Additionally, to ensure reliable twin signaling, there is a need to employ channel

|Services<br><br>layer|
|---|

Services

layer

|Twin layer|
|---|

Twin layer Physicalinteraction

|Physicalinteraction<br><br>layer|
|---|

layer

|Smart grid<br><br>Smart banking<br><br>Intelligent transportation<br><br>system<br><br>Extended reality<br><br>Industry 4.0<br><br>Healthcare<br><br>Smart buildings<br><br>Smart surveillance|
|---|

|Blockchain<br><br>network of miners<br><br>[Figure 170]<br><br>[Figure 171]<br><br>[Figure 172]<br><br>[Figure 173]<br><br>[Figure 174]<br><br>[Figure 175]<br><br>[Figure 176]<br><br>Miner<br><br>Pre-training of ML models|
|---|

||[Figure 177]<br><br>[Figure 178]<br><br>[Figure 179]<br><br>[Figure 180]<br><br>[Figure 181]<br><br>[Figure 182]<br><br>[Figure 183]<br><br>[Figure 184]<br><br>[Figure 185]<br><br>Edge/cloud based<br><br>twin|
|---|
<br><br>|[Figure 186]<br><br>[Figure 187]<br><br>[Figure 188]<br><br>[Figure 189]<br><br>[Figure 190]<br><br>[Figure 191]<br><br>[Figure 192]<br><br>[Figure 193]<br><br>[Figure 194]<br><br>Edge/cloud based<br><br>twin|
|---|
<br><br>||[Figure 195]<br><br>Digital model of the physical system|
|---|
<br><br>|[Figure 196]<br><br>Instructions|
|---|
<br><br>[Figure 197]<br><br>Machine<br><br>learning<br><br>models<br><br>|[Figure 198]<br><br>Optimizatio n schemes|
|---|
<br><br>[Figure 199]<br><br>Game<br><br>theoretic<br><br>schemes|
|---|
<br><br>Twin to twin<br><br>interface|
|---|

|Mathematical<br><br>modeling 3D modeling<br><br>Data-driven<br><br>modeling<br><br>Reusability<br><br>Decomposability<br><br>Efficient interfacing|
|---|

|Channel coding (e.g., Turbo codes,<br><br>URLLC codes) Transmission schemes (e.g., , multi-<br><br>connectivity, packet duplication)<br><br>Lightweight devices authentication Wireless security (e.g., homomorphic encryption) Hardware-software co-design Computing and wireless resource allocation|
|---|

|[Figure 200]<br><br>|Physical object to twin interface (e.g., gateway)|
|---|
<br><br>|Twin to physical object interface (e.g., gateway)|
|---|
| | |
|---|---|---|
| | | |

|Smart devices<br><br>[Figure 201]<br><br>[Figure 202]<br><br>[Figure 203]<br><br>[Figure 204]<br><br>[Figure 205]<br><br>[Figure 206]<br><br>[Figure 207]<br><br>[Figure 208]<br><br>[Figure 209]|
|---|

Fig. 6: High-level architecture of digital twin enabled wireless systems.

coding schemes (e.g., URLLC codes) and other techniques (e.g., multi-connectivity, packet duplication). On the other hand, twin service reliability mainly depends on wireless channel reliability and reliable edge/cloud computing. For service wireless channel reliability, similar to twin signaling we can use channel coding schemes and other techniques for communication [44]–[46]. Additionally, a digital twin can be used for predictive maintenance of 6G systems to avoid system malfunctions and cyber-attacks through artiﬁcial intelligence analytics and simulation. The summary of the steps for twinbased wireless system operation is as follows.

- • First of all, end-user will request a service. This request will be translated using semantic reasoning schemes to make it compatible with the twin object-based architecture.
- • Next, the twin object will be created to to serve the end-

user.

• Finally, the twin object uses mathematical optimization and machine learning schemes in addition to virtual representation to enable efﬁcient resource optimization for various services.

D. Frameworks

In this section, we discuss various frameworks designed for implementing digital twins. Moreover, we critically analyze them and discuss their advantages and limitations.

1) Eclipse Ditto: Eclipse Ditto is an open-source framework for creating digital IoT twins [47]. The framework consists of Ditto services (components), external dependencies (MongoDB and nginx), and application programming interfaces (APIs). Ditto consists of microservices, each with its own data store where reading and writing take place. Every

microservice has a set of APIs (events, command responses, commands). Moreover, a microservice can communicate with other microservices using deﬁned signals. Within a Ditto cluster, all microservices can communicate asynchronously using an open-source toolkit, namely, AKKA remoting. Therefore, each service can acts client, enabling a TCP endpoint, and a server. The messages between microservices are serializable (i.e., from Java objects to JavaScript Object Notation(JSON)) and deserializable (i.e., from JSON to Java objects).

- 2) Model Conductor-eXtended Framework: Model

Conductor-eXtended (MCX) is an open-source framework for digital twins experimentation [48], [49]. The framework enables us to co-execute the digital systems and physical systems as well as asynchronous communication. Furthermore, support for machine learning models, customized models, and running FMUs (simulation models packaged according to the FMI speciﬁcation) is also provided. The MCX uses standard data transmission protocol, time-synchronous implementation of time-consuming simulation models, and decoupling of the queue and the model computation module, for offering scalability which is one of the important design aspects of IoT applications.

- 3) Mago3D: Mago3D is an open-source digital twin plat-

form developed by a South Korean company, namely, Gaia3D inc. [50]. The purpose is to real-world objects, phenomenon, and process on web environment [51]. The platform consists of a geospatial data server, data conversion server, platform core server, and web server, for realizing the digital twin-based architecture. Mago3D has been applied in various sectors, such as Korean national defense, indoor data management, shipbuilding, and urban management, and have shown good results.

All of the aforementioned digital twin platforms (i.e., Eclipse Ditto,Model Conductor-eXtended Framework, and Mago3D) are promising towards the realization of digital twinbased systems. However, none of them effectively considered the effects of wireless channels on the performance of digital twins. In wireless systems, wireless channel uncertainties will signiﬁcantly affect the performance of IoT applications. Therefore, one must effectively model these wireless channel uncertainties while digital twinning for wireless system applications.

E. Summary and Lessons Learned

In this section, we presented the fundamentals of digital twins and derived the deﬁnition of twins in the context of wireless systems. We also presented the key design aspects, such as twins for wireless and wireless for twins. Several available frameworks for digital twins experimentation are also discussed. Some key lessons learned here include:

• A digital twin should be designed in a generalized way so that it can be easily reusable for future services. Designing a twin takes signiﬁcant effort and time. Twins based on machine learning should be trained using more data to make them generalized so as to use them for multiple scenarios. Such kinds of twins will minimize the design of the service based on twins. Furthermore, this twin will reduce the design cost.

- • Mostly, the current digital twin frameworks are designed without effectively taking into account the wireless channel impairments. There is a need to propose a novel framework for digital twinning over wireless networks. The digital twin framework should consist of multiple base stations/access points and devices. The wireless impairments degrade the SINR of the transmitted signal. The SINR can be improved using effective resource allocation, association, and transmit power allocation. Therefore, the framework allows us to enable effective resource allocation, association, and power allocation.
- • Digital twins bring together two main use cases for wireless systems: twin for wireless and wireless for twins. Twin for wireless is necessary for effective use of resources (e.g., computing, communication, transmit power). On the other hand, wireless for twins deal with resource-efﬁcient management for twins signaling. Therefore, it is necessary to effectively manage both aspects of digital twin and wireless systems.

III. TAXONOMY: TWINS FOR WIRELESS

Both aspects (i.e., wireless for twins and twin for wireless) of twin-based wireless system deal with a variety of players that act in a complex environment to enable digital twin-based wireless systems. To classify the areas for study in both aspects, we devise a taxonomy that covers both twins for wireless and wireless for twins, as shown in Fig. 7. Fig. 7 divides the taxonomy into layers, such as physical interaction later and twin later. The parameters are positioned according to their role at the layer. For instance, physical devices design is positioned at the physical interaction layer due to its role there. Additionally, the taxonomy related to twins for wireless and wireless for twins is shown by different colors in Fig. 7. Twin for wireless refers to the enabling of various wireless systems applications, such as extended reality, human-computer interaction, and digital healthcare, using twins. We categorize the twins for wireless aspect research into twin isolation, incentive design, twin object design, twin object prototyping, twin objects deployment trends, physical end-devices design, decoupling, and interfaces design. Twin isolation deals with the seamless operation of twin-based services without interrupting the performance of other twins. Incentive design enables attractive incentives for devices that participate in twinning. Twin objects design helps in the ondemand creation of twins using existing computing hardware for various applications, whereas twin objects prototyping helps in the creation of virtual models of the wireless systems. Twin object deployment trends guide us about the placement (e.g., cloud or edge) of twin objects. Decoupling allows the seamless operation of the twin-based services with minimum possible dependency on the underlying hardware. On the other hand, interfaces are used for various types of communications, such as among twin objects, and between twin objects and physical devices.

A. Twins Isolation

Twins isolation deals with the operation of a twin-based application (e.g., extended reality) without affecting the perfor-

|[Figure 210]<br><br>IoEApplicationslayer|
|---|

IoEApplicationslayer

|Haptics-based applications<br><br>Smart surveillance Smart banking<br><br>Autonomous connected vehicles<br><br>Brain-computer interaction<br><br>Extended reality Augmented reality Healthcare Industry 4.0 Smart homes<br><br>|
|---|

|[Figure 211]<br><br>Twinobjectslayer|
|---|

Twinobjectslayer

|[Figure 212]<br><br>Physicalinteractionspace|
|---|

Physicalinteractionspace

|||Clouds<br><br>running twin objects|
|---|
<br><br>[Figure 213]<br><br>Private<br><br>[Figure 214]<br><br>Public<br><br>[Figure 215]<br><br>Community<br><br>[Figure 216]<br><br>Hybrid|
|---|
<br><br>||Edge server<br><br>running twin<br><br>objects|
|---|
<br><br>[Figure 217]<br><br>MEC server<br><br>[Figure 218]<br><br>Fog server<br><br>[Figure 219]<br><br>Flying edge server|
|---|
|
|---|

|||Cloud server|
|---|
|
|---|
<br><br>||Edge server|
|---|
|
|---|
<br><br>||IoE devices|
|---|
|
|---|
<br><br>||Radio access<br><br>network devices|
|---|
|
|---|
<br><br>||Core network devices|
|---|
|
|---|
|
|---|

|[Figure 220]<br><br>Virtual machine-<br><br>based design Container-based design<br><br>[Figure 221]<br><br>|[Figure 222]<br><br>Twin objects design|
|---|
<br><br>[Figure 223]<br><br>[Figure 224]<br><br>Experimental<br><br>modeling Mathematical modeling<br><br>[Figure 225]<br><br>|[Figure 226]<br><br>Twin objects prototyping|
|---|
<br><br>[Figure 227]<br><br>[Figure 228]<br><br>Edge<br><br>[Figure 229]<br><br>|[Figure 230]<br><br>Twin objects deployment trends|
|---|
<br><br>[Figure 231]<br><br>Cloud<br><br>|[Figure 232]<br><br>Data driven modeling|
|---|
<br><br>|
|---|

|[Figure 233]<br><br>Functions decoupling<br><br>[Figure 234]<br><br>|[Figure 235]<br><br>Decoupling|
|---|
<br><br>[Figure 236]<br><br>Data decoupling<br><br>[Figure 237]<br><br>Twin objects isolation<br><br>[Figure 238]<br><br>|[Figure 239]<br><br>Twins isolation|
|---|
<br><br>[Figure 240]<br><br>Wireless<br><br>access network isolation<br><br>[Figure 241]<br><br>Game theoretic<br><br>scheme Contract Theory-based schemes<br><br>[Figure 242]<br><br>|[Figure 243]<br><br>Incentive<br><br>mechanism|
|---|
<br><br>[Figure 244]<br><br>[Figure 245]<br><br>Core network<br><br>resources isolation<br><br>[Figure 246]<br><br>Auction Theory-based schemes<br><br>[Figure 247]<br><br>Twin object to physical object<br><br>[Figure 248]<br><br>|[Figure 249]<br><br>Interface design|
|---|
<br><br>[Figure 250]<br><br>Twin object to twin object<br><br>|
|---|

|[Figure 251]<br><br>OFDMA<br><br>[Figure 252]<br><br>|[Figure 253]<br><br>Air Interface Design|
|---|
<br><br>[Figure 254]<br><br>NOMA<br><br>[Figure 255]<br><br>Wireless security<br><br>[Figure 256]<br><br>[Figure 257]<br><br>Security and privacy<br><br>[Figure 258]<br><br>Device access security<br><br>[Figure 259]<br><br>Twin objects and physical<br><br>objects<br><br>association<br><br>[Figure 260]<br><br>[Figure 261]<br><br>Twin objects<br><br>access aspects<br><br>[Figure 262]<br><br>Wireless<br><br>resource allocation<br><br>[Figure 263]<br><br>IRS based communication<br><br>|
|---|

|[Figure 264]<br><br>Software-based design<br><br>[Figure 265]<br><br>|[Figure 266]<br><br>Physical devices design|
|---|
<br><br>[Figure 267]<br><br>Software<br><br>hardware-<br><br>based design|
|---|

|Legends<br><br>| |
|---|
<br><br>DT for wireless<br><br>taxonomy<br><br>| |
|---|
<br><br>| |
|---|
<br><br>Other functionalities<br><br>Wireless for<br><br>DT taxonomy<br><br>| |
|---|
|
|---|

Fig. 7: Taxonomy of digital twin and wireless systems.

mance of other twin-based applications (e.g., brain-computer interaction). The operation of various twins for different

applications requires computing, storage, and communication resources. The computing resources are used for performing

blockchain mining as mentioned in architecture (for more details, please refer to Fig. 6) in Section II-C. Meanwhile, there is a need for storage to store pre-trained twin models for various applications. Additionally, sufﬁcient communication resources are required for the signaling of twin instructions. To do so, there can be mainly two ways of enabling twins, such as using dedicated hardware and shared hardware. Using dedicated hardware for twin-based applications can better perform but at the cost of high expenditure. Therefore, using dedicated hardware for the end-to-end implementation of twinbased applications is not feasible. To address these issues, one can use shared hardware for twin-based applications. However, sharing hardware for various twin-based applications may affect performance. Therefore, there is a need for isolated operation of twin-based applications.

Isolation in digital twin-enabled wireless systems can be divided into twin objects isolation, core network isolation, and access network isolation [57], [58]. Radio access network isolation refers to using the same access network for various twins without affecting the performance of other twins. Access network isolation can be performed effectively with better management using radio resource virtualization [59]–[61]. In resource virtualization, the third party, a mobile virtual network operator (MVNO) will buy radio resources from multiple network operators. For twins, using resources from different network operators is challenging and suffers from high management complexity. Therefore, one can easily use network virtualization that will enable MVNO to buy network operators’ resources and then sell the resources (i.e., resource partitioning) to various twins based on their requirements in such a way to fulﬁll the end users’ QoS. A twin can also buy resources from multiple MVNOs. In the virtualization approach, the twin does not require management of the resources of multiple network operators, and thus avoids high management complexity. However, this will increase the management complexity of the overall system. Numerous approaches that perform resource selling between the MVNOs and twins are heuristic schemes, deep reinforcement learning schemes, and game-theoretic schemes. Heuristic schemes will offer high implementation complexity [52]. Deep reinforcement learning schemes many also offer high training complexity [53]. Therefore, one can preferably use matching game-based schemes for resource selling between the MVNOs and twins [54]–[56].

Similar to radio access network isolation, one can perform core network isolation. However, the core network isolation will be different than the access network isolation. The core network can be constituted using various technologies, such as optical ﬁber, microwaves, and wired communication technologies. Therefore, performing resource partitioning at the core network for twins may be more challenging. There is a need to propose a hybrid scheme for core network isolation that has different criteria for each communication technology (e.g., optical ﬁber links, microwave links). On the other hand, twin objects isolation can be performed using shared computing hardware (e.g., cloud) for multiple virtual machines running twin objects. Isolation of such twin objects is necessary for improving performance and avoiding security attacks [62], [63]. For instance, if the twin objects are not well isolated, then

Typical network appliances NFV-based approach

[Figure 268]

[Figure 269]

| |
|---|

[Figure 270]

[Figure 271]

Virtual appliances

IPTV

Router

IMS

[Figure 272]

[Figure 273]

[Figure 274]

General purpose

servers

VPN CDN

DPI

[Figure 275]

[Figure 276]

[Figure 277]

Standard storage and switches Firewall

NAT

PGW

Fig. 8: Overview of network function virtualization.

the security attack instantiated within a twin object can easily affect other twin objects. One easy way is to assign dedicated hardware for running a twin object. However, this approach is not feasible due to the high implementation cost. Therefore, there is a need to share the same hardware for virtual machines running twin objects. Similar to radio access network resource sharing, one can use various schemes based on heuristic algorithms, matching game, and deep reinforcement learning.

B. Decoupling

Decoupling in digital twin-enabled wireless systems can be of two types, such as functions decoupling and data decoupling [5]. Data decoupling can be performed using data homogenization techniques. This will enable the twin-based system design independent of the underlying the smart devices network. The layered architecture of twin-based wireless system is discussed in Section II-C. Fig. 6 shows that there will be a variety of smart devices (e.g., temperature sensors, image sensors) at the physical interaction layers. To transform these data into homogenized data, there is a need to employ efﬁcient data homogenization techniques. On the other hand, functions decoupling enables the twin-based system to decouple the management functions from the physical interaction layer to the twin layer. Function decoupling can be implemented by network slicing that is based on NFV and SDN [64]–[69]. Network slicing offers the use of shared network resources for various applications (e.g., intelligent transportation system, healthcare). Network slicing uses NFV and SDN to separate the control plane from the physical interaction plane for easier and efﬁcient management. NFV is based on implementing various network functions using generic hardware as shown in Fig. 8. Implementing various network functions using generic hardware will offer us a cost-efﬁcient design. To implement the physical devices using the NFV-based approach, there may few limitations, such as throughput and latency deterioration [67]. The per-instance capacity of the NFV-based device may not be similar to the actual physical device. There is a need

TABLE III: Virtualization schemes for radio access networks.

Reference Network details Utility Solution approach

Ludwig et al. [52] A graph of nodes (i.e., cloud nodes and end-users nodes) as vertices with connectivity cost (e.g., latency) as vertices was considered..

Acceptance ratio that is given by dividing embedded (i.e., served) slices divided by total slices.

Heuristic approach

De Bast et al. [53] A set of Wi-Fi users with different, dynamic requirements was considered.

A reward function for optimizing throughput was used.

Double deep Q-network-based scheme.

Kim et al. [54] A set of infrastructure provides, users, and set of virtual network operators.

To jointly maximize the network throughput and proﬁt of the revenue of the infrastructure provides.

Match theory-based solution.

Manh ho et al. [55] A heterogeneous cellular network providers, users, and virtual network operators was considered.

To optimize overall energy and revenue of the virtual network operators.

Main problem is decomposed into two sub-problems that are solved using two-stage Stackelberg game, matching theory, and iterative schemes, respectively.

Kazmi et al. [56] A set of virtual network operators, set of infrastructure providers, and users were considered.

To jointly maximize the utilities of infrastructure providers (i.e., proﬁt) and virtual network providers (i.e., maximize the end-users throughput and minimize the cost).

Matching theory-based solution

Main controller manages communication between distributed controllers

Global controller

Communication between devices of various distributed controllers is challenging

Distributed controller 1

Distributed controller 2

Centralized controller

Local controller Local controller

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

Centralized control plane Distributed control plane Hybrid control plane

Fig. 9: Twins function decoupling using (a) centralized controller, (b) distributed controllers, and (c) hybrid controllers.

to keep such deterioration in performance lowest possible. Other challenges faced by NFV-based design are reliability and security issues. Multiple NFVs for various network functions running on the same hardware might result in failure due to a physical damage/ security attack [70]. To address this issue, one can migrate the NFV to a new device. However, migration may introduce a delay that is undesirable in many IoE/IoT applications [71]–[73]. Additionally, mobility of the enddevices also requires the migration of NFV-based functions to the new network edge. To enable such migration, we can use machine learning-based mobility prediction schemes to proactively determine the next location [38]. On the other hand, NFV-based implementation faces new security concerns. NFV-based functions running on remote cloud that is not

controlled by the network operators. Therefore, security must be ensured for the NFV-based functions running on the cloud. On the other hand, SDN separates the control plane from the data plane. In a typical SDN control plane, a single centralized controller is used to control multiple switches for performing various functions (e.g., routing) [74]–[77]. These switches intended to control wireless system devices can be installed on dedicated hardware for better performance. However, this approach will increase the implementation cost of the system. To address limitations, we can design SDN-based devices with built-in capabilities of SDN switches [77]. Controlling SDNbased devices using a single centralized controller may suffer from scalability and reliability issues which are one of the most important design considerations of wireless systems. An

TABLE IV: Comparison of twins function decoupling.

Twin function type

Management complexity

Latency Implementation cost

Centralized controllerbased function decoupling

Lowest High Lowest

Distributed controllersbased function decoupling

High Low High

Hybrid controllerbased function decoupling

Highest Low Highest

for communication between end-users and the system. The interface can be of various types, such as voice interface (e.g., Amazon Echo), touch interface (e.g., smart phone), and physical button interface [82]. These interfaces enables users to interact with the twin-based system. For instance, smart phones uses iOS, Samsung One UI, OxygenOS, Android One, and Indus OS, are the operating systems used by Apple, Samsung, OnePlus, Google’s Android One programme, and India, respectively [83]. For smart phone, one can use any of the aforementioned interfaces of operating systems. However, for applications based on digital twins, there may be a need to propose new interfaces because of their different architecture than the existing ones.

increase in the number of devices will increase the signaling between SDN-based devices and the centralized controller, and thus suffer from high latency issues. To address this limitation, one can use a distributed control plane that consists of multiple SDN controllers [78], [79]. Every controller among a set of controllers controls some end-devices, and thus minimizes the latency due to signaling. However, using multiple controllers will lead to an increase in control plane management complexity. Additionally, communication between the devices connected to different distributed SDN controllers may suffer from extra latency in communication. To reap the advantages of both centralized control and distributed control planes, one can use a hybrid control plan. A hybrid control plane will use both centralized and distributed controllers [80], [81]. In the hybrid control plane, the main controller controls the local controllers. The local controllers control its small set of devices. All the functions that are local to the devices are handled by the local controller, whereas the functions that require global network knowledge (e.g., wireless resource allocation) are controlled by the main controller in addition to local controllers. Overview of the centralized, distributed, and hybrid control planes are given in Fig. 9. Meanwhile, the tabular comparison is given in Table. IV. The management complexity of the centralized control plane is less than the distributed control plane and hybrid control plane. Additionally, the signaling latency of the centralized control plane will be higher than the distributed and hybrid control plane.

C. Interfaces Design

Interface in digital twin-based system can be many types, such as user to twin system interface, twin to object interface, twin object to twin object interface, and air interface. Detailed discussions about air interface will be given in Section IV-A. Here, we discuss twin to physical objects interface, user to twin system interface, and twin object to twin object interface. The twin to physical object interface will can be both wireless (e.g., industrial machine end-devices) and wired (e.g., smart phone running an application). Similarly, twin to twin interface can also be wired and wireless. For distributed twins deployed at multiple edge servers [5], there is a need to enable wireless communication among them. Another way of communication can be through the core network [38]. On the other hand, there is a need to propose efﬁcient and easy to use interface

D. Twin Objects Design

Twin objects are instantiated upon request from the endusers. There are two ways to instantiate the twin objects, such as virtual machine-based twin objects and container-based twin objects [38], [41]. A virtual machine can be deﬁned as the architecture that is independent of the underlying hardware. Virtual machines can be mainly of two types, such as system virtual machine and process virtual machine [84]. In the context of twin-based wireless system, the system virtual machine can be used to model a complete IoT service (e.g., AR-based healthcare system), whereas the process virtual machine can be used to model the particular portion (e.g., edge caching module for smart infotainment system) of digital twin-based system. Modeling of a complete system may be easier than modeling of a particular part. The reason for this can be decoupling only a part of a system from the hardware is challenging. Note that the virtual machine is different from the operating system. In an operating system, language independent extensions of hardware are created, whereas a virtual machine creates a machineindependent instruction set. Note that virtual machine-based virtualization can be seen as an infrastructure-as-a-service (IaaS) component that can enable the same hardware via virtualization for running multiple operating systems (e.g., twins). This operational approach has a main drawback of high management complexity. To address this issue, one can use container-based twin objects. Containers can help minimize management complexity by running multiple twins on the same operating system [85]. In fact, containers can be considered as operating systems-as-a-service. Therefore, one can easily implement twin objects using container based design due to its low management complexity and light weight nature compared to virtual machine based design [86]. However, container-based twin objects may face more security attacks than the virtual machine-based design. The reason for this is the same operating system running various twin objects, and thus more prone to security attacks. On the other hand, virtual machine based twin objects has less security attacks due to their IaaS nature (i.e., multiple operating systems are used to implement twins on the same hardware). Virtual machinebased twins achieve this at the cost of high management complexity. Therefore, a tradeoff must be made between the management complexity and security.

E. Twin Objects Prototyping

True prototyping of twin objects is one of the primary challenges in digital twinning over wireless networks. Physical objects are characterized by a set of attributes (e.g., shape, mass, energy). These attributes are difﬁcult to exactly model [87]. Additionally, these parameters will signiﬁcantly affect the performance of the system. Therefore, one must effectively model these parameters in digital twinning. In experimental modeling, a series of experiments are performed to ﬁnd out the various parameters of a physical wireless system [88]. Various entities of a wireless system can be modeled using experimental data. For instance, the work in [88] modeled the free space path loss for intelligent reﬂecting surfaces using a series of experiments. Their experimental setup was comprised of accessories (i.e., cables and blocking object (electromagnetic wave-absorbing materials), Rx horn antenna, RF signal analyzer (Agilent N9010A), Tx horn antenna, RF signal generator (Agilent E8267D), and metasurface. Although experimental modeling of a wireless system can provide many beneﬁts, it has a few issues [88]. These issues are high costs associated with the experimental setup and human experimental errors. Additionally, if want to design new service twins, there is a need to perform many experiments that will signiﬁcantly increase the cost, and thus may be undesirable [5]. To address this issue, one can use mathematical modeling that is based on a mathematical representation of the wireless phenomenon. Although mathematical models can be obtained in a cost-effective way, there is a need to pay special attention while modeling various parts. Typical mathematical models are based on various assumptions, therefore, we must make assumptions that are close to real time scenario for more practical results.

Mathematical models can be used to model a variety of scenarios, there are some scenarios where it seems difﬁcult to model using mathematical models [33]. To address this limitation, one can use data-driven modeling. All the wireless system applications (e.g., XR) generate a signiﬁcant amount of data that can be used in modeling their behavior [38]. One can use the data of wireless system applications to train machine learning models. Note that machine learning models can model the wireless system phenomenon that can not be modeled using mathematical techniques. However, such training will be at the cost of the training cost. There can be mainly two possible ways to train machine learning models, such as centralized machine learning and distributed machine learning. Centralized machine learning relies on centralized training at the remote cloud or edge server. Although centralized machine learning offers many advantages, it has a prominent issue of privacy leakage because of transferring end-devices data to the centralized cloud/edge server. To address this issue, one can use distributed machine learning. In distributed machine learning, end-devices iteratively train their local model using the local datasets. The local models are then sent to the edge/cloud server for aggregation to yield a global model. Although distributed machine learning can better preserve users’ privacy, it has its own challenges, such as data heterogeneity, system heterogeneity, and wireless channel uncertainties.

F. Incentive Mechanism

The nature of the twin-based wireless systems will be different compared to the existing wireless systems. Therefore, the design of incentive mechanisms for the digital twinbased system will be different. Here, we consider the highlevel architecture of digital twin-enabled wireless systems (Fig. 6) presented in Section II-C. The different types of incentives required in digital twin-enabled wireless systems are presented in Fig. 10. As described in Section II-C, digital twin-based wireless system can use distributed learning to train twin models. These pre-trained twin models are stored using blockchain network in an immutable, transparent manner and can be used in future to serve the requesting users. Upon request from end-users’, the twin-based system serves the end-users’ by controlling the network entities for efﬁcient management of resources. To do so, there must be incentives to various entities of the digital twin-based wireless system. Incentive mechanisms for the digital twin-based wireless system have three main aspects, such as incentive mechanism design for pre-training of twin models, incentive mechanism design for blockchain mining, and incentive mechanism design for control of physical objects, as shown in Fig. 10. During these three phases, the players involved are end-devices, aggregation servers, edge/cloud servers running twin objects, and blockchain miners used for storing pre-trained models and training data. Attractive incentives must be given to all the players of a digital twin-based wireless system for performing their tasks.

When using distributed learning for digital twins, enddevices participate in the learning model local models [93]. Moreover, edge/cloud servers run twin objects and also assist (i.e., aggregation of local models) distributed learning. Therefore, there is a need to give them reward for performing their jobs. However, the nature of the incentive mechanism will be different for end-devices and edge/cloud servers for two tasks (i.e., distributed learning and twinning control). For distributed learning-based twins, the edge/cloud servers will interact with the end-devices for learning a global model. End-devices perform local model learning and edge/cloud server performs aggregation of the end-devices local models to yield a global model. The global model is then shared with the end-devices to update their local models. Such an iterative process takes place until convergence is achieved. One can design an incentive mechanism for such a scenario by deﬁning a utility at the edge/cloud server. The utility of edge/cloud servers can be to maximize the global model accuracy. Meanwhile, the devices with high local accuracy can be given more monetary reward. This seems practical approach because generally, the enddevices need to consume more computing resources to obtain a better local model accuracy. Various works proposed incentive mechanism design for distributed learning using Stackelberg game, auction theory, and contract theory [89]. An overview of these incentive mechanisms is given in Table V. Additionally, details about the incentive model approach, motivation, device utilities, and aggregation server utilities are given.

On the other hand, for a twinning operation, incentives must be provided to the edge/cloud servers running twin

|Twinlayer|
|---|

Twinlayer

|Physicalinteractionlayer|
|---|

Physicalinteractionlayer

|||Blockchain network<br><br>of miners|
|---|
|
|---|
<br><br>[Figure 299]<br><br>[Figure 300]<br><br>[Figure 301]<br><br>[Figure 302]<br><br>[Figure 303]<br><br>[Figure 304]<br><br>[Figure 305]<br><br>Miner<br><br>Pre-training of ML models|
|---|

||[Figure 306]<br><br>[Figure 307]<br><br>[Figure 308]<br><br>[Figure 309]<br><br>[Figure 310]<br><br>[Figure 311]<br><br>[Figure 312]<br><br>[Figure 313]<br><br>[Figure 314]<br><br>Edge/cloud based twin|
|---|
<br><br>|[Figure 315]<br><br>[Figure 316]<br><br>[Figure 317]<br><br>[Figure 318]<br><br>[Figure 319]<br><br>[Figure 320]<br><br>[Figure 321]<br><br>[Figure 322]<br><br>[Figure 323]<br><br>Edge/cloud based<br><br>twin|
|---|
|
|---|

|[Figure 324]<br><br>|Physical object to twin Interface (e.g., gateway)|
|---|
<br><br>|Twin to physical object Interface (e.g., gateway)|
|---|
| | |
|---|---|---|
| | | |

|Smart devices<br><br>[Figure 325]<br><br>[Figure 326]<br><br>[Figure 327]<br><br>[Figure 328]<br><br>[Figure 329]<br><br>[Figure 330]<br><br>[Figure 331]<br><br>[Figure 332]<br><br>[Figure 333]|
|---|

| Miners must be given attractive incentives for mining. Additionally, miners/nodes used for storage must be given incentives<br> Edge/cloud server must be given incentives for running twin objects for services<br> Edge/cloud server must also be given incentives for assisting (i.e., global aggregation) pre-training of distributed learning models<br>|
|---|

| Gateways and SDN network operators<br><br>must also be given incentives|
|---|

| End-devices must be given incentives<br><br>for participation in distributed learning<br><br>model training|
|---|

Fig. 10: Overview of incentives in digital twin-based wireless systems.

objects. In digital twin-based architecture, pre-trained twin models must be stored using blockchain for future use [5]. Miners used for performing blockchain consensus algorithms and storage must be given attractive incentives [94]. In [94], a Fee and Waiting Tax scheme was proposed to provide miners with an incentives for mining and storage of the generated blockchain blocks. The Fee and Waiting Tax scheme was based on addressing the two kinds of issues associated with the existing blockchain protocols, such as selecting a transaction by a certain miner will impose storage cost on the other miners and users’ transactions generation may increase the waiting time for other users. The Fee and Waiting Tax has two main steps, such as fee choices and waiting tax. In fee choices, the proposed scheme offers a set of fee-per-byte choices for users while ensuring the miners to get sufﬁcient fees for their work. The second step is that the Fee and Waiting Tax scheme is waiting tax on users proportional to their negative impact on other users. This enables the users to become more conservative while generating transactions. On the other hand, the edge/cloud servers running the twin objects must be given incentives for their contributions. Meanwhile, the SDN

network operators must also be given attractive incentives for enabling efﬁcient twinning.

G. Twins Deployment Approaches

Twins can be mainly deployed either at the network edge or cloud depending on the requirement of the application. Every application has distinct requirements in terms of latency, quality of physical experience, computing resource requirement, and reliability, among others. Depending on the these requirements one can deploy twins at various locations (e.g., edge). Twins deployed at the network edge can enable services with low latency compared to twins at the cloud. Meanwhile, the twins at the edge can have more context awareness (e.g., end-devices location, mobility-awareness). Although edge-based twins can enable various applications with a variety of advantages, they have limitations in terms of low computing resources. Edge has lower computing resources than the cloud. Therefore, one can deploy twins at the cloud. Cloud has more computing resources but at the cost of high latency and low context-awareness.

TABLE V: Federated learning incentive mechanisms [89].

Reference Incentive model Motivation Device utility/ bid Utility of aggregation server Pandey et al., [90] Stackelberg game To enable accurate, com-

Difference between cost (i.e., communication and computation cost) and reward.

Concave function of log(1/𝑔𝑙𝑜𝑏𝑎𝑙 𝑎𝑐𝑐𝑢𝑟𝑎𝑐𝑦)

munication efﬁcient federated learning model.

Le et al., [91] Auction theory To reduce the social cost (i.e., devices bids cost).

Difference between cost and reward.

To reduce the bids cost.

Kang et al., [92] Contract theory Motivating reliable enddevices for participating in learning process.

Difference between energy consumption and reward.

To maximize the proﬁt (i.e., difference between reward given to end-devices and total time for global iteration).

TABLE VI: Comparison of various twin objects deployment [5].

Description Edge-based twin object

Cloudbased twin object

Edgecloudbased twin objects

Twins Robustness (reliability)

It refers to seamless operation during failure of one of twin objects. Highest (for multiple edgebased twins)

Lowest Medium

Geodistribution

This metric enable us with the information about the geographical distribution of twin objects.

Distributed Centralized Hybrid

Elasticity This metric shows the ability of a twin-based wireless system in providing highly dynamic

High Low High

requirements of various services via elastic resource allocation.

Mobility support

It refers to the ability of a twin-based wireless system to serve the mobile devices seamlessly. High Low Medium

Latency It deals with the overall delay in providing the service to end-users. Low High Medium Contextawareness

It deals with the ability of a twin-based wireless system to obtain network and devices information.

High Low Medium

Scalability It deals with fulﬁlling the requirements of a massive number of wireless devices. Addition-

High Lowest Low

ally, the addition of more devices should not degrade the latency performance.

||||interaction|
|---|
<br><br>Physical<br><br>interaction<br><br>layer|
|---|
<br><br>Physical<br><br>interaction<br><br>layer<br><br>[Figure 334]<br><br>[Figure 335]<br><br>[Figure 336]<br><br>[Figure 337]<br><br>[Figure 338]|
|---|
<br><br>Twinlayer<br><br>| | | |
|---|---|---|
<br><br>Network<br><br>edge<br><br>||Cloud|
|---|
<br><br>Cloud|
|---|
<br><br>Cloud<br><br>|Cloud-<br><br>based twin object|
|---|
<br><br>|Edgebased twin object|
|---|
<br><br>Twin-to-Things interface<br><br>Twin-to-twin interface<br><br>Collaborative twin<br><br>Twinsmanager<br><br>|Edgebased twin<br><br>object|
|---|
<br><br>|Cloud-<br><br>based twin object|
|---|
|
|---|

[Figure 339]

[Figure 340]

[Figure 341]

Cloude

IoE services

Twinsmanager

Twinlayer

[Figure 342]

[Figure 343]

[Figure 344]

ork

[Figure 345]

[Figure 346]

[Figure 347]

Protocol

design

[Figure 348]

[Figure 349]

[Figure 350]

Edge-based twin Cloud-based twin

3DCameras

Autonomous

Edge-cloud-based twin

Satellites

cars

Optimization

theory

Game

UAVs

theory

AI

Algorithmic dimension

Fig. 11: Twin objects deployment trends [5].

To beneﬁt from both edge-based twins and cloud-based twins, one can use a hybrid trend that simultaneously deploys twins at network edge and cloud for enabling a certain application. For instance, consider the digital-twin-enabled infotainment system for autonomous cars. One can use caching assisted by a hybrid twin that consists of two twins deployed at both network edge and the cloud. The edge twin will make

the caching decisions for infotainment users where latency is stringent. Meanwhile, due to limited storage capacity at the edge, one can use the cloud to cache the information that is less frequent compared to cached information at the edge. To control caching at the cloud, cloud twins can be used. Comparisons of various twins depending on the deployment trends are given in Table VI. Fig. 11 shows the different ways in which twins can be deployed. Table VI shows that edge-based twins (i.e., for multiple twin objects) have the highest robustness to failures compared to cloud-based twins and hybrid twins. The reason for this is due to the fact that even if any of the twin objects malfunction due to physical damage or a security attack, the other twin objects will serve the end-user. Similarly, the elasticity of edge-based twins is higher than a cloud-based twin. The reason for this is the remote location of cloud-based twin objects that results in high latency while serving the user. Considering latency as a metric, edge-based twins will have the lowest among the possible deployment trends. The reason for this is due to its nearby location to end-users. However, edge-based twins have low computing power than the cloud-based-twins. Therefore, one must make a tradeoff between the latency and available computing resources for performing a twinning task. Mobility support is also high for edge-based twins due to their nearby nature to end-devices and high context-awareness (i.e., devices

locations and edge network information).

- H. Physical End-Devices Design

To efﬁciently operate twin-based wireless systems, there is a need to effectively design the end-devices. These enddevices have two main uses, such as actions and training of local models for distributed learning [5]. For actions (e.g., optimal transmit power), the devices with the assistance of twins will perform decisions (e.g., optimal transmit power, association, and resource allocation) for optimal performance. For such scenarios, the devices may not require signiﬁcantly high computing power. However, for the distributed learning case, the devices will require high computing power to learn their local models. In the case of distributed learning-based twins training, the devices will learn local models using their local data. Other than local models training, the devices have to perform additional tasks as well. Training a twin model using a set of devices depends on local learning model architecture, local dataset, and local iterations [95]. For a ﬁxed local dataset and local model architecture, the computing time is determined by the device operating frequency. The device’s local model computing time decreases within an increase in operating frequency. However, this would cause an increase in energy consumption. Note that the energy consumption also depends on the devices design [96]. Therefore, there is a need to efﬁciently design the end-devices for twin-based wireless systems. End-devices design can be mainly based on either hardware-based design or software-based design [89].

One can design programmable hardware with high dimensionality for end-devices to enable its general use for various tasks in a digital twin-enabled wireless system [5]. Note that high dimensionality causes an increase in computing power because of more generated data. To efﬁciently enable the hardware design, one can use application-speciﬁc manycore processors [97]. To implement hardware using manycore processors there is a need to ﬁne-tuning for enabling efﬁcient run-time resource management. Also, the use case has a signiﬁcant impact on the hardware performance. To enable efﬁcient hardware, Kim et al. in [98] presented a machine learning-based design for manycore systems. On the other hand, using ﬁxed hardware design, one can propose multiple software designs that can efﬁciently use the given hardware for performing distributed learning tasks. To do so, we can exploit neural architecture search (NAS) [99]–[102]. In NAS, various possible neural architectures are searched among a search space for certain hardware and the efﬁcient one is selected.

- I. Lessons Learned and Recommendations

In this section, we devised a taxonomy for twins of wireless aspect. The devised taxonomy considered twin isolation, incentive design, twin object design, twin object prototyping, twin objects deployment trends, physical end-devices design, decoupling, and interfaces design. as parameters. The lessons learned and future recommendations are as follows.

• From [5], [95], [96], [99]–[102], we learned that there is a need to consider both hardware and software design

while designing end-devices. One can jointly consider both hardware designs and neural architectures and selected the one with optimal results. Such a joint design hardware-software co-design will offer more freedom of variations during searching of the optimal hardware and software designs.

- • There is a need to efﬁciently deploy the twin objects at the network edge/cloud. There can be situations, where one service (i.e., deep reinforcement learning-infotainment service) must be served by multiple twin objects (i.e., running agent for caching decision) at edge servers. For such scenarios, one must cost-efﬁciently deploy the twin objects. To deploy one can use a scheme based on matching theory and optimization theory.
- • From [5], [87], [88], we learned that considerable care must be taken while virtual modeling the physical system/entity. Mathematical models are based on assumptions that may not more accurately follow the real scenarios. On the other hand, one can use experimental modeling that is based on extensive experimentation. However, this approach has the drawback of long design time. Another way can be data driven modeling that is based on training a machine learning model. Again, training a machine learning model may have training time. From the aforementioned facts, there is a need to effectively model the twins while minimizing design time. For instance, one can train a machine learning for twin using efﬁcient architecture that have less training time.

IV. TAXONOMY: WIRELESS FOR TWINS

Wireless for twins deals with efﬁcient twins signaling for enabling various services. Various parameters of the wireless for twins aspects are air interface design, twin objects access aspects, and security and privacy, as shown in Fig. 7. Air interface will be used for twin signaling. Twin objects access aspects will enable efﬁcient association of twins and physical devices. Finally, there must be effective security and privacy mechanism for twins-based wireless systems.

A. Air Interface Design

Air interface will be used by digital twin for transfer of learning model updates, data, and control instructions. Meanwhile, there are signiﬁcant limitations on the availability of wireless resources. Therefore, we must employ efﬁcient communication schemes for wireless transfer. There can be two main aspects for the design of wireless interface for digital twinning, such as frequency band and access scheme. The access schemes can be orthogonal frequency division multiple access (OFDMA), time division multiple access (TDMA), non-orthogonal multiple access (NOMA), etc [103]. OFDMA uses orthogonal resource blocks for communication, and thus there will be no interference among them. OFDMA suffers from spectral efﬁciency and limited users issues. It might not be able to serve the massive number of users. To address this limitation, one can use NOMA. Comparison of NOMA and OFDMA is given in Table VII [104]. NOMA uses the whole bandwidth for all users and performs decoding

TABLE VII: Comparison of NOMA and OFDMA [104].

based compressed sensing broadband channel estimation. The focus of the authors was an intelligent reﬂecting surfacesassisted millimeter wave system and minimized training overhead.

Category Advantages Disadvantages OFDMA

• Low complexity receiver

- • Low spectral efﬁciency
- • Limited users

design

B. Twin Objects access aspects

NOMA

- • High spectral efﬁciency
- • High connection density
- • Enhanced user fairness

- • High complexity of receivers
- • Sensitivity to channel uncertainties

There are two main aspects associated with accessing the twin objects, such as (a) twin objects and physical devices association and (b) computing and wireless resource allocation. Twin objects can be deployed at either at cloud or edge server. For edge-based twins, one can apply twins at various network edges that have different access costs (e.g., transmit power, achievable throughput, packet error rate) for physical objects. Therefore, we must properly associate the physical objects with twins. The edge-based twins and physical objects association problem will be a combinatorial problem. Such kinds of problems can be solved using various techniques, such as relaxation-based schemes, heuristic schemes, and matching theory-based solutions [28], [111]–[117]. The relaxation-based solution ﬁrst transforms the binary association variable into a continuous variable which can be further solved using various schemes (e.g., convex optimization solver if the relaxed problem is convex). A relaxation-based solution can provide a low complexity solution but at the cost of approximation error (i.e., transforming the binary variables into continuous variables). To avoid the approximation error in relaxationbased schemes, one can use heuristic schemes [28]. However, heuristic schemes have high computational complexity. Therefore, to address the limitations of both heuristic and relaxationbased schemes, one can use matching theory-based solutions that can offer effectively association between twins and the physical objects with reasonable complexity [116], [117].

using power levels. NOMA can offer several advantages, such as high spectral density, high connection density, and enhanced user fairness but at the cost of high complexity associated with the receiver. Therefore, a tradeoff must be made between the receiver complexity and spectral efﬁciency.

On the other hand, one can use many frequency bands for twinning depending on the requirement of the wireless system applications. Lower frequency bands (e.g., medium frequency, high frequency) have been used for various applications (e.g., navigation beacons) that do not have very strict latency requirements. With the emergence of novel applications, such as intelligent transportation systems, human-computer interactions, and XR, among others, the requirement of strict latency becomes one of the most important key performance requirements. To enable low latency communication, there is a need for large bandwidth for communication. To enable such communication, one can use higher frequency bands (i.e., millimeter-wave and terahertz). Although sufﬁcient bandwidth is available at high-frequency bands, there will be sufﬁciently high attenuation. To address this issue, one can use intelligent reﬂecting surfaces [105]. Intelligent reﬂecting surfaces consist of an array of reﬂecting units with the ability to incur some change independently [106]. Such a change can be either polarization, frequency, amplitude or phase [105]. The main goal of intelligent reﬂecting surfaces is to enable efﬁcient communication between the transmitter and receiver that does not have a line of sight path. Although intelligent reﬂecting surfaces have many beneﬁts, it has a few challenges. These challenges are surface design, channel sensing, and estimation, and passive beamforming, among others [107]. For channel sensing and estimation in intelligent reﬂecting surfaces, many works [108]–[110] presented several proposals. In [108], the authors considered estimation for an intelligent reﬂecting surfacesenabled millimeter-wave communication system and proposed a compressed sensing-based estimation scheme. Additionally, the authors also extended their work to a multi-antenna system. The work of [108] performed well while minimizing the training overhead. Another work [109] studied modeling and channel estimation for intelligent reﬂecting surfaces-assisted wireless communication. The works in [108] and [109] may not very effectively perform in a change in SNR scenarios and require retraining. To address this issue, the work [110] proposed a hybrid passive/active intelligent reﬂecting surfaces architecture. They presented a deep denoising neural network-

Other than association, there is a need to efﬁciently allocate wireless resources to physical devices for communication with twin objects. Additionally, computing resources are required for twin processing. There are two main resources in digital twin-enabled wireless systems, such as wireless/wired resources for signaling and computing resources. The computing resources can be used for various tasks. These tasks are running machine learning models at edge/cloud in case of centralized learning or physical devices for distributed learning. Additionally, computing resources are required for blockchain consensus algorithms and analysis of the virtual twin model prior to applying for real-time applications. The computing resource for a machine learning task of size 𝑇𝑠 units within time 𝑇𝑐𝑜𝑚𝑝 for 𝐼 iterations can be given by.

𝑇𝑠 𝑇comp

. (1)

𝑓𝑛 = 𝐼

More computing resources are required for running the twin model within less time, and vice versa. Additionally, the size of the twin model along with learning model iterations proportionally affect the requirement of computing resources. Therefore, we must make a tradeoff between the task computing time and computing resource requirement. On the other hand, computing resource requirement for blockchain

consensus strictly depends on the type of consensus algorithm and network size.

Other than computing resources, communication resources are required for the signaling and training of distributed twin models. Communication resources can be wireless access network resources and core network resources. Generally, the core network delay is signiﬁcantly small due to high-speed optical backhaul links. Wireless access network resources are limited, therefore, there is a need to efﬁciently allocate these resources for twinning. The tasks, such as distributed twin models training, twin signaling, and wireless blockchain miners will use communication resources. The required communication resources are dependent on the twinning task. For distributed twin models training, wireless resources are required for sharing the learning model updates between the end-devices and the aggregation server. For twin signaling, wireless resources are required for the transfer of control signals (e.g., SDN controllers signaling). On the other hand, blockchain miners will use wireless resources for sharing of blocks during consensus algorithm. All of the aforementioned use of wireless resources require efﬁcient allocation of wireless resources. Generally, the wireless resource allocation problem is a combinatorial problem that can be solved using various ways, such as heuristic algorithms [28], relaxationbased schemes [118], matching theory-based schemes [119]– [121].

C. Security and Privacy

Security in digital twins and wireless systems can be mainly categorized into two types, such as devices physical security and interfaces security. Devices physical security is challenging due to their large number and distributed nature [38]. Therefore, one must employ effective authentication schemes to avoid the unauthorized access to devices, edge/cloud servers, and blockchain miners, among others. On the other hand, we must use effective security mechanisms for interfaces in digital twin-based wireless systems. Interfaces in digital twin-based wireless system can be wireless interface (e.g., radio access network), application interface (i.e., smart phone application access screen security), and wired interface (e.g., wired core network). Furthermore, the technologies, such as SDN and NFV used by the digital twin for efﬁcient control of the underlying physical devices arise new security challenges. Overview of various security attacks with their possible solutions for digital twin based wireless system is given in Fig. 12. In SDN control plane, the secruity threats are vulnerable network controllers, forged control packet injection, misconﬁgured policy enforcement, and weak network devices authentication [122]. Misconﬁgured interfaces (e.g., twin to twin interface) and protocols (twin packets routing protocols) results in various security vulnerability [123]. Weak or improper authentication schemes and plan text channels may lead to security attacks. Therefore, one must employ effective encryption/decryption schemes to avoid the security attacks.

On the other hand, there may a loss of privacy during training twin models. In the case of centralized training, all the end-devices data is transferred to a centralized server for

training and thus results in end-devices privacy leakage. To address this issue, one can train twin models in a distributed manner that is based on on-device training. The local models trained at devices are sent to the edge/cloud for aggregation to yield a global model. The global model is shared with the end-devices again for updating their local models. This process of learning distributed twin models takes place iteratively. Although end-devices do not send their data to the remote cloud/edge server for training, they still require privacy preservation techniques. A malicious aggregation server can infer the end-device sensitive information using their local learning model updates, and thus results in privacy leakage [89], [93], [124]. To address this issue, one can use various schemes, such as differential privacy and homomorphic encryptionbased schemes. In differential privacy, a noise is added to the local learning model updates prior to sending them to the aggregation server. Although differential privacy can enhance privacy preservation, it will be at the cost of slowing the global learning convergence [95]. To avoid this issue, one can use homomorphic encryption that is based on encrypting the local learning models prior to sending them to the aggregation server. Similar to differential privacy, homomorphic encryption works at the cost of communication overhead [93]. Therefore, a tradeoff must be made the overhead and privacy preservation. Other than differential privacy and homomorphic encryption, few works [125]–[127] proposed over-the-air computation. In over-the-air computation, the channel noise is considered a differential privacy noise for preserving the distributed learning privacy. On the other hand, the work in [93] proposed a dispersed federated learning scheme that is based on computing sub-global models within groups, as shown in Fig. 13. The computation of the sub-global model is performed iteratively. Then, the sub-global models are shared among each other and ﬁnally, the global model is computed. Note that dispersed federated learning offers enhanced privacy protection compared to traditional federated learning. In traditional federated learning, a malicious aggregation server can infer some of the devices’ sensitive information from their learning model updates. In contrast to traditional federated learning, a sub-global aggregation server can infer, but a global server can not infer. Therefore, one can say that dispersed federated learning can offer better privacy preservation than traditional federated learning. Another work [128] presented a collaborative federated learning scheme that is based on local aggregation at end-devices, as shown in Fig. 14. Such local aggregation is performed due to communication resources constraints. The global aggregation can infer the devices’ sensitive information from the learning model updates (excluding locally aggregated learning models). However, it is very difﬁcult for the aggregation server to infer the devices’ local information from the locally aggregated learning models. Therefore, one can say that collaborative federated learning can offer better privacy preservation compared to traditional federated learning [129].

D. Lessons Learned and Recommendations

In this section, a taxonomy of twins wireless for twins is devised. We considered three parameters, such as twin objects

|Twinlayer|
|---|

Twinlayer

|Physicalinteractionlayer|
|---|

Physicalinteractionlayer

||[Figure 351]<br><br>[Figure 352]<br><br>[Figure 353]<br><br>[Figure 354]<br><br>[Figure 355]<br><br>[Figure 356]<br><br>[Figure 357]<br><br>[Figure 358]<br><br>[Figure 359]<br><br>Edge/cloud based twin|
|---|
|
|---|

|[Figure 360]<br><br>[Figure 361]<br><br>[Figure 362]<br><br>[Figure 363]<br><br>[Figure 364]<br><br>[Figure 365]<br><br>[Figure 366]|
|---|

| Unauthorized modification of twinning information<br> Misconfigured Interfaces for twins communication<br> Forged twining control packet injection<br> Weak interfaces<br>|
|---|

| Devices physical security<br> Devices authentication schemes<br> Wireless security<br> Vulnerable physical devices<br>|
|---|

Possible

solutions

| On-demand virtualized security functions for twin layer<br> Encryption of twin control information<br> Continuous monitoring of twin control information<br>|
|---|

| Lightweight devices authentication protocols<br> Encryption for wireless security<br> Lightweight devices authentication protocol<br> Novel forensic techniques to analyze the attacks<br>|
|---|

Fig. 12: Security attacks in digital twin-based wireless systems.

Global aggregation

[Figure 367]

Sharing of subglobal models

6

Sub-global aggregation 5

[Figure 368]

[Figure 369]

Sub-global

[Figure 370]

[Figure 371]

3

server B

Sub-global server A

[Figure 372]

[Figure 373]

[Figure 374]

[Figure 375]

4 2

[Figure 376]

[Figure 377]

|[Figure 378]<br><br>| | |
|---|---|---|
| | | |
| | | |
| | | |

|[Figure 379]<br><br>| | |
|---|---|---|
| | | |
| | | |
| | | |

Device A

[Figure 380]

1

[Figure 381]

[Figure 382]

[Figure 383]

[Figure 384]

[Figure 385]

[Figure 386]

[Figure 387]

[Figure 388]

[Figure 389]

[Figure 390]

[Figure 391]

[Figure 392]

[Figure 393]

[Figure 394]

[Figure 395]

[Figure 396]

[Figure 397]

[Figure 398]

[Figure 399]

[Figure 400]

[Figure 401]

[Figure 402]

[Figure 403]

[Figure 404]

[Figure 405]

[Figure 406]

[Figure 407]

[Figure 408]

[Figure 409]

[Figure 410]

[Figure 411]

[Figure 412]

[Figure 413]

[Figure 414]

[Figure 415]

[Figure 416]

[Figure 417]

[Figure 418]

[Figure 419]

[Figure 420]

[Figure 421]

[Figure 422]

[Figure 423]

[Figure 424]

[Figure 425]

[Figure 426]

[Figure 427]

[Figure 428]

[Figure 429]

[Figure 430]

[Figure 431]

[Figure 432]

[Figure 433]

[Figure 434]

[Figure 435]

[Figure 436]

[Figure 437]

[Figure 438]

[Figure 439]

[Figure 440]

[Figure 441]

[Figure 442]

[Figure 443]

[Figure 444]

Local

Local dataset

Local model

Local model

Local model

Local

Local model

Local

dataset

dataset

dataset

Fig. 13: Dispersed federated learning overview.

access aspects, air interface design, security and privacy. The lessons learned and recommendations are as follows.

- • We learned from [38], [93], [122], [123] that effective security schemes must be applied to digital twin-based wireless systems. Digital twin-based wireless systems will offer many beneﬁts but will be prone to variety of security attacks as discussed in Section IV-C. Prior to applying to security schemes, one can propose effective forensic schemes to investigate the attacks in digital twinbased system. Next to investigation of security attacks, we can propose efﬁcient security attacks. For devices,

one must propose lightweight and effective authentication schemes. For wireless transfer of data and control signals, one can use efﬁcient and effective encryption schemes. Twin-based wireless systems have a layered architecture that communicate with each other using interfaces (e.g., twin object to twin object interface and twin object to physical object interface). There may be conﬁgured interfaces for twinning that will result in security attack. Additionally, forged twinning control instructions will signiﬁcantly degrade the performance of digital twinbased systems. Therefore, there is a need to propose novel

|[Figure 445]<br><br>Aggregation<br><br>server<br><br>Limited communication<br><br>resources<br><br>Local model<br><br>sharing with<br><br>nearby device<br><br>[Figure 446]<br><br>[Figure 447]<br><br>Local aggregation<br><br>Transfer of locally aggregated model<br><br>[Figure 448]<br><br>3<br><br>[Figure 449]<br><br>2<br><br>[Figure 450]<br><br>4 4<br><br>[Figure 451]<br><br>[Figure 452]<br><br>5<br><br>[Figure 453]<br><br>[Figure 454]<br><br>[Figure 455]<br><br>Local<br><br>dataset<br><br>Local<br><br>model<br><br>[Figure 456]<br><br>[Figure 457]<br><br>[Figure 458]<br><br>[Figure 459]<br><br>[Figure 460]<br><br>[Figure 461]<br><br>[Figure 462]<br><br>[Figure 463]<br><br>[Figure 464]<br><br>[Figure 465]<br><br>[Figure 466]<br><br>[Figure 467]<br><br>[Figure 468]<br><br>[Figure 469]<br><br>[Figure 470]<br><br>1<br><br>[Figure 471]<br><br>[Figure 472]<br><br>Local<br><br>dataset<br><br>Local<br><br>model<br><br>[Figure 473]<br><br>1<br><br>[Figure 474]<br><br>[Figure 475]<br><br>[Figure 476]<br><br>[Figure 477]<br><br>[Figure 478]<br><br>[Figure 479]<br><br>[Figure 480]<br><br>[Figure 481]<br><br>[Figure 482]<br><br>[Figure 483]<br><br>[Figure 484]<br><br>[Figure 485]<br><br>[Figure 486]<br><br>[Figure 487]<br><br>[Figure 488]<br><br>[Figure 489]<br><br>[Figure 490]<br><br>[Figure 491]<br><br>Local<br><br>dataset<br><br>Local<br><br>model<br><br>[Figure 492]<br><br>[Figure 493]<br><br>[Figure 494]<br><br>[Figure 495]<br><br>[Figure 496]<br><br>[Figure 497]<br><br>[Figure 498]<br><br>[Figure 499]<br><br>[Figure 500]<br><br>[Figure 501]<br><br>[Figure 502]<br><br>[Figure 503]<br><br>[Figure 504]<br><br>[Figure 505]<br><br>[Figure 506]<br><br>1|
|---|

Fig. 14: Collaborative federated learning.

security schemes for digital twinning control information transfer.

- • To deploy multiple twin objects for various services, there is a need to efﬁciently manage computing resource at the network edge/cloud. Different twins (e.g., XR twin, healthcare twin) have different computing resource requirements, therefore, deploying twins with heterogeneous requirements need careful design considerations. We must effectively allocate computing resource among various twins. Additionally, there may be different among twins deployment. For instance, healthcare twins might have more priority compared to infotainment twins. Therefore, computing resource allocation must also take int account the priority of various twins.
- • Digital-twin-based system have a wide variety of players (i.e., end-devices, edge/cloud servers, SDN switches). Mostly, the backup power of end-devices has limitations. Therefore, there is a need to propose energy efﬁcient algorithms. For instance, one can propose energy efﬁcient association of physical end-devices with the edge server running twin objects. The energy efﬁciency for association can be obtained by optimizing the transmit power allocation while performing association.

V. OPEN CHALLENGES

This section presents a few open challenges with their possible guidelines. Previous surveys and tutorials have discussed open challenges, such as standardization issues, security and privacy, government regulations for medical twins, accurate representation of digital twins, technical limitations, barriers to blockchain applications in digital twins, and data related issues. Our work lists novel challenges as given in Table VIII.

A. Dynamic Twins

How does one enable twins to be reused for controlling various physical devices? Re-usability of twin objects is one

TABLE VIII: Summary of existing surveys and tutorials open research challenges.

Reference Challenges Minerva et al., [13] Standardization, scalability, composability, and

business model.

Wu et al., [14] Security vulnerability, privacy leakage, costeffective solutions, and two-way real-time interaction.

Barricelli et al., [15]

Ethical issues, security and privacy, cost of development, equally distributed wealth, government regulations for medical twins, and technical limitations.

Yaqoob et al., [16] Accurately representing an object and affordability of digital twins, ethical, legal, and societal issues, cybersecurity, and barriers to Blockchain Adoption in digital twins.

Suhail et al., [17] Digital twin representation, data related issues, expenditure on infrastructure.

Khan et al., [5] Isolation between digital twin-based services, mobility management for edge-based twins, digital twin forensics.

Our Tutorial Dynamic twins, interoperability for twins migration, twins prototyping of physical objects, incentive mechanism for twinning, and efﬁcient twin objects chaining.

of the main features that can make digital twins promising for use in wireless systems. Designing twin objects require signiﬁcant efforts to make them an exact replication of physical object/ phenomenon with energy and computationally efﬁciency. Therefore, it will be highly desirable to make the twins reusable for future use. There is a need to make the twins general for their use for various services. The general twins can be designed using machine learning. One can train a twin machine learning model for a more general dataset to enable its applicability to different services. However, training a twin machine learning model for general data might not perform well [130], [131]. Additionally, the selection of the machine learning model must be made carefully. For small datasets, generally, machine learning models with low complexity are desirable than the models with high complexity. Therefore, there must effective selection of the twin machine learning models for making it more general. Such a general dynamic twin model can be based on either centralized machine learning or distributed machine learning (e.g., federated learning).

B. Interoperability for Twin Objects Migration

How does one enable a seamless operation of end-devices served by edge-based twin objects? Mostly, end-devices in wireless systems are mobile. For instance, one device connected to a small cell base station equipped with an edge server running twin objects may move to the coverage area of another base station. There can be two ways to serve the mobile device. One can be to connect to the existing edge server through the core network via a newly associated base station. However, this approach will suffer from inherent latency that might not be desirable due to strict latency constraints of most of the IoE

TABLE IX: Summary of the research challenges and their guidelines.

Challenges Taxonomy relevancy Causes Guidelines Dynamic twins Twin objects prototyping

- • Physical objects/system dynamic states
- • Long design time of new twin objects

- • Centralized machine learning-based twins
- • Distributed learning-based twins

Interoperability for twin objects migration

Twin objects deployment trends • End-devices mobility

- • Open cloud/edge computing interface based design
- • Similar architecture for edge servers running the twin objects.

• Strict latency constraints of the vari-

ous services

True Prototyping of Physical Objects

Twin objects prototyping

- • Accurate estimation of twin objects measure
- • Dynamic nature of the physical systems

- • Experimental modeling
- • 3D modeling
- • Data driven modeling

Incentive Mechanisms for Twinning

Incentive design

- • End-devices consume their resources for training a distributed twin model.
- • Miners also perform mining for managing twin object pretrained models.
- • Edge/cloud servers require incentives for running twin objects of various services.

- • Game theory-based incentive mechanism
- • Contract theory-based incentive mechanism
- • Auction-based incentive mechanism

Twinning forensics and security

Security and privacy

- • Wide variety of players are susceptible to security attacks
- • Different players (e.g., edge server, routers) have different architecture

- • Video-based forensics schemes
- • Blockchain-based forensics schemes
- • Mobility-aware forensics schemes

Efﬁcient Twin objects chaining

Twin objects access aspects

- • Design a new twin is computationally expensive
- • Long design time for training, testing, and validation for newly designed twins
- • High cost associated with new twins design

- • Mathematical optimization-based schemes
- • Game theoretic schemes
- • Machine learning-enabled schemes

applications. To address this issue, one can migrate the twin object to the newly associated small cell base station. Twin objects based on virtual machines can be migrated dynamically depending on the mobile device location [132]. One can use machine learning schemes to enable the efﬁcient migration of twin object-based virtual machines. However, it must be noted that transferring a virtual machine from one edge/cloud server to another may face interoperability issues. Two edge/cloud servers must be designed interoperable to ease migration of virtual machines running twin objects to tackle the mobility of end-devices. One can use a common architecture to enable easier migration, such as uniﬁed cloud interface/cloud broker, enterprise cloud Orchestration platform/orchestration layer, and open cloud computing interface [133].

C. True Prototyping of Physical Objects

How do we truly prototype the physical object attributes (e.g., features, data, actions, and events) into twin objects for various applications? It is necessary to estimate the measurable aspects of the physical objects for twin modeling. However, it is challenging to accurately measure the aspects

of a physical system. For instance, it is difﬁcult to measure the aspects of the human body using wearable for healthcare [13]. During modeling of a physical object, one can focus on a few parameters more, otherwise, the complexity will be very high. Meanwhile, there are various dynamic phenomena (e.g., wireless channels) in wireless systems that are possible to be exactly determined. Various modeling schemes are experimental modeling, three-dimensional modeling, and data-driven modeling [31]. Experimental modeling involves full-scale experimentation for understanding a physical phenomenon. Based on the experimentation, one can ﬁnd the parameters that are difﬁcult to ﬁnd directly using techniques (e.g., correlations). In three-dimensional modeling, the goal is to develop mathematical models of physical objects using various techniques (e.g., 3D scanning). However, exact representation using a mathematical model is challenging. On the other hand, data-driven modeling uses data for deriving the functional form of physical objects. Machine learning can be used to model physical objects using data. However, proper selection and training of a machine learning model is a challenge and needs careful considerations.

- D. Incentive Mechanisms for Twinning

How does one motivate various players of a twin-based wireless system for successful and effective operation? In digital twinning, a variety of players, such as edge/cloud servers, miners, end-devices, and network operators, interact with each other to enable wireless services. These players interact to perform various tasks, such as pretraining of twin models, twin operation, and mining for management of twin pre-trained models. For pretraining of twin models using distributed machine learning, there will be two main players, such as end-devices and edge/cloud servers. End-devices compute their local model and expect a monetary incentive for their contributions towards learning of a global model. To design an incentive for such a scenario, one can use the Stackelberg game that follows leader-follower fashion. The edge/cloud server will act as a leader and devices will follow it. The utility of the edge/cloud server can be a function of global accuracy and the end-devices utility can be the difference between cost (i.e., communication and computation) and reward (monetary incentive) [90]. Furthermore, one can also use contract theory and auction theory for design incentive for pretraining of twin models [91], [92]. On the other hand, one can also design incentives for network operators using game theory, contract theory, and auction theory. The network operator and users can be two players. The network operator will aim to maximize its proﬁt by serving more users while fulﬁlling their requirements. The end-users will try to improve their performance in terms of throughput.

- E. Twinning Forensics and Security

How do we investigate and take necessary steps to counter the security attacks in a digital twin-enabled wireless system? Digital twin-based wireless systems will involve a wide variety of players, such as edge/cloud computing servers, end-devices, various interfaces (e.g., twin to device and twin to twin), and twin objects, among others. The digital twin-based wireless system will have a different architecture than the existing wireless systems. Therefore, they are prone to various kinds of novel attacks (e.g., twin object attacks and twin to twin interface attacks) in addition to existing attacks (e.g., a man in the middle attack). Therefore, one must apply effective forensic schemes to enable the successful operation of twinbased wireless systems. Forensic techniques for a digital twinbased system can be blockchain-based forensics schemes [134] and video-based evidence analysis [135]. On the other hand, there may be challenges in implementing forensics schemes due to the mobility of nodes. To address this issue, one can propose mobility-aware forensics schemes for digital twinsbased wireless systems. As forensics enables to get information about the security attacks, therefore, there is a need to propose effective security mechanisms to meet the security demands of digital twin-based systems. The security scheme can be designed for a complex digital system depending on the point of interest. For instance, SDN and NFV used for decoupling in the digital twin-based wireless system needs different security mechanisms compared to the edge/cloud

servers running the twin objects. Similarly, for twin signaling, one can use encryption/decryption schemes.

F. Efﬁcient Twin Objects Chaining

How do we chain various twins to enable a service/ wireless system functions for efﬁcient operation? Generally, designing a twin object requires extensive efforts and time. Therefore, designing novel twin objects for new services will require signiﬁcant amount of time. For instance, twin-based AR service may requires multiple twin objects deployed at network edge. One way can be to design a novel twin objects for deployment at the network edge. However, this approach will cost in terms of time and efforts. More feasible way can be to reuse the existing twins to enable a complete twinbased AR service. However, combining multiple twins for enabling a service may suffer from high communication and computing cost. Selecting a number of twin objects among a set of available objects is challenging. Every twin object at the edge/cloud is characterized by a certain cost (e.g., latency). For instance, similar twin objects running at edge and cloud server has different latencies. Additionally, the available computing power can also be different depending on the location of twin objects. We must take into account all the factors while chaining twin objects for a certain service/function. Such chaining of twin objects can be based on optimization theory, game theory, heuristic algorithms, and deep reinforcement learning-based schemes. Typically, heuristic algorithms have high computing complexity, and thus may not be suitable for use. One can use optimization and game theory-based schemes. However, there may be a few twin object chaining problems that can not exactly be modeled via mathematical optimization. For such kinds of problems, one can use deep reinforcement learning-based schemes.

VI. CONCLUSIONS AND FUTURE PROSPECTS

We have presented a comprehensive tutorial on digital twins and wireless systems. We presented key design aspects and a high-level framework for a digital-twin-based wireless system. Also, we outlined currently available digital twinning frameworks. Additionally, a comprehensive taxonomy is devised using various parameters. Finally, we presented key open research challenges with causes and possible solutions. We concluded that the integration of digital twins and wireless systems is necessary for enabling IoE applications. Proactive analysis of digital twinning will enable wireless systems to proactively manage the network resources for strict latency applications (e.g., XR). Furthermore, the reusability of generalized digital twins will make them attractive for use in many new emerging applications.

As a future prospect, we believe that digital twins will be one of the most promising technology for 6G and beyond wireless systems. 6G services will have diverse requirements for novel applications (e.g., human-computer interaction, XR). To meet such kind of diverse requirements, we will redesign the existing wireless systems. These requirements are the userdeﬁned quality of physical experiences, extremely low latency, and ultra-reliability, among others. Enabling a wireless system

to meet the aforementioned requirements needs proactive analysis and machine learning-based schemes. The digital twin will enable us to proactively analyze the system and train effective machine learning models. The pre-trained twin machine learning models will enable the wireless system to make on-demand decisions related to the operation of wireless applications in response to demand from users. Furthermore, one can further train the pre-trained twin models to more effectively incorporate the newly generated data.

REFERENCES

- [1] A. Al-Fuqaha, M. Guizani, M. Mohammadi, M. Aledhari, and M. Ayyash, “Internet of things: A survey on enabling technologies, protocols, and applications,” IEEE communications surveys & tutorials, vol. 17, no. 4, pp. 2347–2376, Fourthquarter, 2015.
- [2] L. Atzori, A. Iera, and G. Morabito, “The internet of things: A survey,” Computer networks, vol. 54, no. 15, pp. 2787–2805, October 2010.
- [3] S. Li, L. Da Xu, and S. Zhao, “5g internet of things: A survey,” Journal of Industrial Information Integration, vol. 10, pp. 1–9, June 2018.
- [4] M. Ge, H. Bangui, and B. Buhnova, “Big data for internet of things: a survey,” Future generation computer systems, vol. 87, pp. 601–614, October 2018.
- [5] L. U. Khan, W. Saad, D. Niyato, Z. Han, and C. S. Hong, “Digitaltwin-enabled 6g: Vision, architectural trends, and future directions,” To appear, IEEE Communication Magazine, 2022.
- [6] F. Tao, H. Zhang, A. Liu, and A. Y. Nee, “Digital twin in industry: State-of-the-art,” IEEE Transactions on Industrial Informatics, vol. 15, no. 4, pp. 2405–2415, April 2018.
- [7] S. Haag and R. Anderl, “Digital twin–proof of concept,” Manufacturing Letters, vol. 15, pp. 64–66, January 2018.
- [8] Markets and Markets, “Internet of thigns market,” https://www.marketsandmarkets.com/Market-Reports/internet-ofthings-market-573.html, [Online; accessed Sept. 22, 2021].
- [9] Statistica, “Spending on internet of things (iot) in selected countries of the asia-paciﬁc region in 2019,” https://www.statista.com/statistics/1037118/apac-internet-of-thingsspending-by-country/, [Online; accessed Sept. 22, 2021].
- [10] ——, “Iot spending worldwide 2019, by country,” https://www.statista.com/statistics/1118256/iot-spending-worldwideby-country/, [Online; accessed Sept. 22, 2021].
- [11] Markets and Markets, “Digital twin market,” https://www.marketsandmarkets.com/Market-Reports/digital-twinmarket-225269522.html?, [Online; accessed Sept. 22, 2021].
- [12] B. Research, “Global digital twin market,” https://www.marketsandmarkets.com/Market-Reports/digital-twinmarket-225269522.html?, [Online; accessed Sept. 22, 2021].
- [13] R. Minerva, G. M. Lee, and N. Crespi, “Digital twin in the iot context: a survey on technical features, scenarios, and architectural models,” Proceedings of the IEEE, vol. 108, no. 10, pp. 1785–1824, October 2020.
- [14] Y. Wu, K. Zhang, and Y. Zhang, “Digital twin networks: a survey,” IEEE Internet of Things Journal, Early access, 2021.
- [15] B. R. Barricelli, E. Casiraghi, and D. Fogli, “A survey on digital twin: deﬁnitions, characteristics, applications, and design implications,” IEEE access, vol. 7, pp. 167653–167671, November 2019.
- [16] I. Yaqoob, K. Salah, M. Uddin, R. Jayaraman, M. Omar, and M. Imran, “Blockchain for digital twins: Recent advances and future research challenges,” IEEE Network, vol. 34, no. 5, pp. 290–298, September/October 2020.
- [17] S. Suhail, R. Hussain, R. Jurdak, A. Oracevic, K. Salah, and C. S. Hong, “Blockchain-based digital twins: Research trends, issues, and future challenges,” arXiv preprint arXiv:2103.11585, 2021.
- [18] “Digital twins are mission critical,” https://www.ge.com/digital/applications/digital-twin, [Online; accessed May. 16, 2021].
- [19] “What is digital twin?” https://www.twi-global.com/technicalknowledge/faqs/what-is-digital-twin, [Online; accessed May. 16, 2021].
- [20] “Compare simulation & cae software,” https://www.g2.com/categories/simulation-cae, [Online; accessed May. 16, 2021].
- [21] “Best digital twin software,” https://www.g2.com/categories/digitaltwin, [Online; accessed May. 16, 2021].

- [22] “The history and creation of the digital twin concept,” https://www.challenge.org/insights/digital-twin-history/, [Online; accessed May. 19, 2021].
- [23] Siemens, “Digital twin,” https://www.plm.automation.siemens.com/global/en/ourstory/glossary/digital-twin/24465, [Online; accessed May. 20, 2021].
- [24] XMPRO, “Digital twins: The ultimate guide,” https://xmpro.com/digital-twins-the-ultimate-guide//, [Online; accessed May. 21, 2021].
- [25] Vercator, “How to make a digital twin: the options, types and outputs,” https://info.vercator.com/blog/how-to-make-a-digital-twin-the-optionstypes-and-outputs, [Online; accessed May. 21, 2021].
- [26] “The digital twin – an introduction,” https://www.tributech.io/blog/thedigital-twin, [Online; accessed May. 21, 2021].
- [27] M. Chen, Z. Yang, W. Saad, C. Yin, H. V. Poor, and S. Cui, “A joint learning and communications framework for federated learning over wireless networks,” IEEE Transactions on Wireless Communications, vol. 20, no. 1, pp. 269–283, January 2020.
- [28] L. U. Khan, M. Alsenwi, Z. Han, and C. S. Hong, “Self organizing federated learning over wireless networks: A socially aware clustering approach,” in International Conference on Information Networking (ICOIN). IEEE, 2020, pp. 453–458.
- [29] Z. Han, D. Niyato, W. Saad, T. Ba¸sar, and A. Hjørungnes, Game theory in wireless and communication networks: theory, models, and applications. Cambridge university press, 2012.
- [30] F. Pires, A. Cachada, J. Barbosa, A. P. Moreira, and P. Leit˜ao, “Digital twin in industry 4.0: Technologies, applications and challenges,” in 2019 IEEE 17th International Conference on Industrial Informatics (INDIN), vol. 1. IEEE, January 2019, pp. 721–726.
- [31] A. Rasheed, O. San, and T. Kvamsdal, “Digital twin: Values, challenges and enablers,” arXiv preprint arXiv:1910.01719, 2019.
- [32] H. Elayan, M. Aloqaily, and M. Guizani, “Digital twin for intelligent context-aware iot healthcare systems,” IEEE Internet of Things Journal, Early access 2021.
- [33] S. Ali, W. Saad, N. Rajatheva, K. Chang, D. Steinbach, B. Sliwa, C. Wietfeld, K. Mei, H. Shiri, H.-J. Zepernick et al., “6G white paper on machine learning in wireless communication networks,” arXiv preprint arXiv:2004.13875, 2020.
- [34] D. P. Kumar, T. Amgoth, and C. S. R. Annavarapu, “Machine learning algorithms for wireless sensor networks: A survey,” Information Fusion, vol. 49, pp. 1–25, September 2019.
- [35] J. Jagannath, N. Polosky, A. Jagannath, F. Restuccia, and T. Melodia, “Machine learning for wireless communications in the internet of things: A comprehensive survey,” Ad Hoc Networks, vol. 93, p. 101913, October 2019.
- [36] M. S. Mahdavinejad, M. Rezvan, M. Barekatain, P. Adibi, P. Barnaghi, and A. P. Sheth, “Machine learning for internet of things data analysis: A survey,” Digital Communications and Networks, vol. 4, no. 3, pp. 161–175, August 2018.
- [37] B. Sudharsan and P. Patel, “Machine learning meets internet of things: From theory to practice,” 2021.
- [38] L. U. Khan, I. Yaqoob, N. H. Tran, S. A. Kazmi, T. N. Dang, and C. S. Hong, “Edge-computing-enabled smart cities: A comprehensive survey,” IEEE Internet of Things Journal, vol. 7, no. 10, pp. 10200– 10232, October 2020.
- [39] N. Fernando, S. W. Loke, and W. Rahayu, “Mobile cloud computing: A survey,” Future generation computer systems, vol. 29, no. 1, pp. 84–106, January 2013.
- [40] E. F. Coutinho, F. R. de Carvalho Sousa, P. A. L. Rego, D. G. Gomes, and J. N. de Souza, “Elasticity in cloud computing: a survey,” annals of telecommunications-annales des t´el´ecommunications, vol. 70, no. 7, pp. 289–309, 2015.
- [41] W. Z. Khan, E. Ahmed, S. Hakak, I. Yaqoob, and A. Ahmed, “Edge computing: A survey,” Future Generation Computer Systems, vol. 97, pp. 219–235, August 2019.
- [42] N. Abbas, Y. Zhang, A. Taherkordi, and T. Skeie, “Mobile edge computing: A survey,” IEEE Internet of Things Journal, vol. 5, no. 1, pp. 450–465, September 2017.
- [43] https://www.altoros.com/blog/digital-twins-for-aerospace-better-ﬂeetreliability-and-performance/, [Online; accessed Sept. 27, 2021].
- [44] D. S. Lun, M. M´edard, R. Koetter, and M. Effros, “On coding for reliable communication over packet networks,” Physical Communication, vol. 1, no. 1, pp. 3–20, 2008.
- [45] Z. Guo, J. Huang, B. Wang, S. Zhou, J.-H. Cui, and P. Willett, “A practical joint network-channel coding scheme for reliable communication in wireless networks,” Ieee transactions on wireless communications, vol. 11, no. 6, pp. 2084–2094, 2012.

- [46] C. Hausl, “Joint network-channel coding for the multiple-access relay channel based on turbo codes,” European Transactions on Telecommunications, vol. 20, no. 2, pp. 175–181, 2009.
- [47] “Eclipse ditto,” https://www.eclipse.org/ditto/, [Online; accessed Sept. 22, 2021].
- [48] https://github.com/COMEA-TUAS/mcx-public, [Online; accessed Sept. 24, 2021].
- [49] https://research.utu.ﬁ/converis/portal/detail/Publication/66484819?, [Online; accessed Sept. 22, 2021].
- [50] http://mago3d.com/en/index.html, [Online; accessed Sept. 27, 2021].
- [51] https://callforpapers.2021.foss4g.org/foss4g2021/talk/MJPNQC/, [Online; accessed Sept. 27, 2021].
- [52] K. Ludwig, A. Fendt, and B. Bauer, “An efﬁcient online heuristic for mobile network slice embedding,” in 2020 23rd Conference on Innovation in Clouds, Internet and Networks and Workshops (ICIN). IEEE, 2020, pp. 139–143.
- [53] S. De Bast, R. Torrea-Duran, A. Chiumento, S. Pollin, and H. Gacanin, “Deep reinforcement learning for dynamic network slicing in ieee 802.11 networks,” in IEEE INFOCOM 2019-IEEE Conference on Computer Communications Workshops (INFOCOM WKSHPS). IEEE, 2019, pp. 264–269.
- [54] S. A. Kazmi, A. Ndikumana, A. Manzoor, W. Saad, C. S. Hong et al., “Distributed radio slice allocation in wireless network virtualization: Matching theory meets auctions,” IEEE Access, vol. 8, pp. 73494– 73507, 2020.
- [55] T. M. Ho, N. H. Tran, L. B. Le, Z. Han, S. A. Kazmi, and C. S. Hong, “Network virtualization with energy efﬁciency optimization for wireless heterogeneous networks,” IEEE Transactions on Mobile Computing, vol. 18, no. 10, pp. 2386–2400, 2018.
- [56] S. M. A. Kazmi and C. S. Hong, “A matching game approach for resource allocation in wireless network virtualization,” in Proceedings of the 11th International Conference on ubiquitous information management and communication, 2017, pp. 1–6.
- [57] S. A. Kazmi, L. U. Khan, N. H. Tran, and C. S. Hong, Network slicing for 5G and beyond networks. Springer, 2019, vol. 1.
- [58] L. U. Khan, I. Yaqoob, N. H. Tran, Z. Han, and C. S. Hong, “Network slicing: Recent advances, taxonomy, requirements, and open research challenges,” IEEE Access, vol. 8, pp. 36009–36028, February 2020.
- [59] C.-Y. Chang, N. Nikaein, and T. Spyropoulos, “Radio access network resource slicing for ﬂexible service execution,” in IEEE INFOCOM 2018-IEEE Conference on Computer Communications Workshops (INFOCOM WKSHPS). IEEE, 2018, pp. 668–673.
- [60] E. Datsika, A. Antonopoulos, N. Zorba, and C. Verikoukis, “Matching game based virtualization in shared lte-a networks,” in 2016 IEEE Global Communications Conference (GLOBECOM). IEEE, 2016, pp. 1–6.
- [61] S. A. Kazmi, N. H. Tran, T. M. Ho, and C. S. Hong, “Hierarchical matching game for service selection and resource purchasing in wireless network virtualization,” IEEE Communications Letters, vol. 22, no. 1, pp. 121–124, 2017.
- [62] “How a vm is realy isolated?” https://vinfrastructure.it/2017/04/vmreally-isolated/, [Online; accessed Oct. 19, 2021].
- [63] https://docs.vmware.com/en/VMware-Cloud-Director/index.html, [Online; accessed Oct. 19, 2021].
- [64] S. Bera, S. Misra, and A. V. Vasilakos, “Software-deﬁned networking for internet of things: A survey,” IEEE Internet of Things Journal, vol. 4, no. 6, pp. 1994–2008, 2017.
- [65] A. H. Mohammed, R. M. KHALEEFAH, I. A. Abdulateef et al., “A review software deﬁned networking for internet of things,” in 2020 International Congress on Human-Computer Interaction, Optimization and Robotic Applications (HORA). IEEE, 2020, pp. 1–8.
- [66] K. Kalkan and S. Zeadally, “Securing internet of things with software deﬁned networking,” IEEE Communications Magazine, vol. 56, no. 9, pp. 186–192, 2017.
- [67] B. Han, V. Gopalakrishnan, L. Ji, and S. Lee, “Network function virtualization: Challenges and opportunities for innovations,” IEEE Communications Magazine, vol. 53, no. 2, pp. 90–97, 2015.
- [68] R. Mijumbi, J. Serrat, J.-L. Gorricho, N. Bouten, F. De Turck, and R. Boutaba, “Network function virtualization: State-of-the-art and research challenges,” IEEE Communications surveys & tutorials, vol. 18, no. 1, pp. 236–262, 2015.
- [69] K. Joshi and T. Benson, “Network function virtualization,” IEEE Internet Computing, vol. 20, no. 6, pp. 7–9, 2016.
- [70] S. Lal, T. Taleb, and A. Dutta, “Nfv: Security threats and best practices,” IEEE Communications Magazine, vol. 55, no. 8, pp. 211– 217, August 2017.

- [71] S. Wang, J. Xu, N. Zhang, and Y. Liu, “A survey on service migration in mobile edge computing,” IEEE Access, vol. 6, pp. 23511–23528, April 2018.
- [72] N. Hassan, K.-L. A. Yau, and C. Wu, “Edge computing in 5g: A review,” IEEE Access, vol. 7, pp. 127276–127289, August 2019.
- [73] Y. C. Hu, M. Patel, D. Sabella, N. Sprecher, and V. Young, “Mobile edge computing—a key technology towards 5G,” ETSI white paper, vol. 11, no. 11, pp. 1–16, 2015.
- [74] M. Karakus and A. Durresi, “A survey: Control plane scalability issues and approaches in software-deﬁned networking (sdn),” Computer Networks, vol. 112, pp. 279–293, January 2017.
- [75] E. Amiri, E. Alizadeh, and K. Raeisi, “An efﬁcient hierarchical distributed sdn controller model,” in 2019 5th Conference on Knowledge Based Engineering and Innovation (KBEI). IEEE, 2019, pp. 553–557.
- [76] D. E. Sarmiento, A. Lebre, L. Nussbaum, and A. Chari, “Decentralized sdn control plane for a distributed cloud-edge infrastructure: A survey,” IEEE Communications Surveys & Tutorials, Firstquarter 2021.
- [77] F. Bannour, S. Souihi, and A. Mellouk, “Distributed sdn control: Survey, taxonomy, and challenges,” IEEE Communications Surveys & Tutorials, vol. 20, no. 1, pp. 333–354, Firstquarter 2017.
- [78] M. A. Togou, D. A. Chekired, L. Khoukhi, and G.-M. Muntean, “A hierarchical distributed control plane for path computation scalability in large scale software-deﬁned networks,” IEEE Transactions on Network and Service Management, vol. 16, no. 3, pp. 1019–1031, September 2019.
- [79] S. Ahmad and A. H. Mir, “Scalability, consistency, reliability and security in sdn controllers: A survey of diverse sdn controllers,” Journal of Network and Systems Management, vol. 29, no. 1, pp. 1–59, November 2021.
- [80] S. Huang, J. Zhao, and X. Wang, “Hybridﬂow: A lightweight control plane for hybrid sdn in enterprise networks,” in 2016 IEEE/ACM 24th International Symposium on Quality of Service (IWQoS). IEEE, June 2016, pp. 1–2.
- [81] Y. Fu, J. Bi, Z. Chen, K. Gao, B. Zhang, G. Chen, and J. Wu, “A hybrid hierarchical control plane for ﬂow-based large-scale software-deﬁned networks,” IEEE Transactions on Network and Service Management, vol. 12, no. 2, pp. 117–131, June 2015.
- [82] https://trackinno.com/iot/how-iot-works-part-4-user-interface/, [Online; accessed Oct. 19, 2021].
- [83] https://www.business-standard.com/, [Online; accessed Oct. 19, 2021].
- [84] http://course.ece.cmu.edu/ ece600/fall17/lectures/lecture19.pdf, [Online; accessed Oct. 21, 2021].
- [85] NetApp, “Containers vs. virtual machines (vms): What’s the difference?” https://www.netapp.com/blog/containers-vs-vms/, [Online; accessed Oct. 19, 2021].
- [86] “To containerize or not to containerize, that is the question, or containers vs vms: the eternal debate,” https://www.mirantis.com/blog/containers-vs-vms-eternal-debate/, [Online; accessed Oct. 19, 2021].
- [87] A. S. Khan and F. U. Khan, “A survey of wearable energy harvesting systems,” International Journal of Energy Research, Early access, 2021.
- [88] W. Tang, M. Z. Chen, X. Chen, J. Y. Dai, Y. Han, M. Di Renzo, Y. Zeng, S. Jin, Q. Cheng, and T. J. Cui, “Wireless communications with reconﬁgurable intelligent surface: Path loss modeling and experimental measurement,” IEEE Transactions on Wireless Communications, vol. 20, no. 1, pp. 421–439, January 2020.
- [89] L. U. Khan, W. Saad, Z. Han, E. Hossain, and C. S. Hong, “Federated learning for internet of things: Recent advances, taxonomy, and open challenges,” IEEE Communications Surveys & Tutorials, vol. 23, no. 3, pp. 1759–1799, June 2021.
- [90] S. R. Pandey, N. H. Tran, M. Bennis, Y. K. Tun, A. Manzoor, and C. S. Hong, “A crowdsourcing framework for on-device federated learning,” IEEE Transactions on Wireless Communications, vol. 19, no. 5, pp. 3241–3256, May 2020.
- [91] T. H. T. Le, N. H. Tran, Y. K. Tun, Z. Han, and C. S. Hong, “Auction based incentive design for efﬁcient federated learning in cellular wireless networks,” in 2020 IEEE Wireless Communications and Networking Conference (WCNC), 2020, pp. 1–6.
- [92] J. Kang, Z. Xiong, D. Niyato, S. Xie, and J. Zhang, “Incentive mechanism for reliable federated learning: A joint optimization approach to combining reputation and contract theory,” IEEE Internet of Things Journal, vol. 6, no. 6, pp. 10700–10714, September 2019.
- [93] L. U. Khan, Y. K. Tun, M. Alsenwi, M. Imran, Z. Han, and C. S. Hong, “A dispersed federated learning framework for 6g-enabled autonomous driving cars,” arXiv preprint arXiv:2105.09641, 2021.

- [94] Y. Liu, Z. Fang, M. H. Cheung, W. Cai, and J. Huang, “An incentive mechanism for sustainable blockchain storage,” arXiv preprint arXiv:2103.05866v3, 2021.
- [95] L. U. Khan, S. R. Pandey, N. H. Tran, W. Saad, Z. Han, M. N. Nguyen, and C. S. Hong, “Federated learning for edge networks: Resource optimization and incentive mechanism,” IEEE Communications Magazine, vol. 58, no. 10, pp. 88–93, October 2020.
- [96] “Designing for extreme low power,” https://semiengineering.com/designing-for-extreme-low-power/, [Online; accessed Nov. 10, 2021].
- [97] L. Ceze, M. D. Hill, and T. F. Wenisch, “Arch2030: A vision of computer architecture research over the next 15 years,” arXiv preprint arXiv:1612.03182, 2016.
- [98] R. G. Kim, J. R. Doppa, and P. P. Pande, “Machine learning for design space exploration and optimization of manycore systems,” in IEEE/ACM International Conference on Computer-Aided Design (ICCAD). IEEE, 2018, pp. 1–6.
- [99] C. Liu, B. Zoph, M. Neumann, J. Shlens, W. Hua, L.-J. Li, L. Fei-Fei, A. Yuille, J. Huang, and K. Murphy, “Progressive neural architecture search,” in Proceedings of the European conference on computer vision (ECCV), 2018, pp. 19–34.
- [100] Y. Zhou, P. Wang, S. Arik, H. Yu, S. Zawad, F. Yan, and G. Diamos, “Epnas: Efﬁcient progressive neural architecture search,” arXiv preprint arXiv:1907.04648, 2019.
- [101] T. Elsken, J. H. Metzen, and F. Hutter, “Neural architecture search: A survey,” The Journal of Machine Learning Research, vol. 20, no. 1, pp. 1997–2017, March 2019.
- [102] H. Pham, M. Guan, B. Zoph, Q. Le, and J. Dean, “Efﬁcient neural architecture search via parameters sharing,” in International Conference on Machine Learning. PMLR, 2018, pp. 4095–4104.
- [103] L. U. Khan, Z. Sabir, S. A. Mahmud, and G. M. Khan, “Comparison of three interpolation techniques in comb-type pilot-assisted channel coded ofdm system,” in 27th International Conference on Advanced Information Networking and Applications Workshops, 2013, pp. 977– 981.
- [104] Z. Wei, J. Yuan, D. W. K. Ng, M. Elkashlan, and Z. Ding, “A survey of downlink non-orthogonal multiple access for 5g wireless communication networks,” arXiv preprint arXiv:1609.01856, 2016.
- [105] J. Zhao, “A survey of intelligent reﬂecting surfaces (irss): Towards 6g wireless communication networks with massive mimo 2.0,” arXiv preprint arXiv:1907.04789, 2019.
- [106] E. Basar, M. Di Renzo, J. De Rosny, M. Debbah, M.-S. Alouini, and R. Zhang, “Wireless communications through reconﬁgurable intelligent surfaces,” IEEE access, vol. 7, pp. 116753–116773, August 2019.
- [107] S. Gong, X. Lu, D. T. Hoang, D. Niyato, L. Shu, D. I. Kim, and Y.-C. Liang, “Toward smart wireless communications via intelligent reﬂecting surfaces: A contemporary survey,” IEEE Communications Surveys & Tutorials, vol. 22, no. 4, pp. 2283–2314, Fourth Quarter, 2020.
- [108] P. Wang, J. Fang, H. Duan, and H. Li, “Compressed channel estimation for intelligent reﬂecting surface-assisted millimeter wave systems,” IEEE Signal Processing Letters, vol. 27, pp. 905–909, May 2020.
- [109] Q.-U.-A. Nadeem, A. Kammoun, A. Chaaban, M. Debbah, and M.-S. Alouini, “Intelligent reﬂecting surface assisted wireless communication: Modeling and channel estimation,” arXiv preprint arXiv:1906.02360, 2019.
- [110] S. Liu, Z. Gao, J. Zhang, M. Di Renzo, and M.-S. Alouini, “Deep denoising neural network assisted compressive channel estimation for mmwave intelligent reﬂecting surfaces,” IEEE Transactions on Vehicular Technology, vol. 69, no. 8, pp. 9223–9228, August 2020.
- [111] Z. Zhou, K. Ota, M. Dong, and C. Xu, “Energy-efﬁcient matching for resource allocation in d2d enabled cellular networks,” IEEE Transactions on Vehicular Technology, vol. 66, no. 6, pp. 5256–5268, June 2016.
- [112] H. Zhang, Y. Xiao, S. Bu, D. Niyato, F. R. Yu, and Z. Han, “Computing resource allocation in three-tier iot fog networks: A joint optimization approach combining stackelberg game and matching,” IEEE Internet of Things Journal, vol. 4, no. 5, pp. 1204–1215, October 2017.
- [113] A. Ahmed, M. Awais, T. Akram, S. Kulac, M. Alhussein, and K. Aurangzeb, “Joint placement and device association of uav base stations in iot networks,” Sensors, vol. 19, no. 9, p. 2157, 2019.
- [114] H. Zhang, S. Huang, C. Jiang, K. Long, V. C. Leung, and H. V. Poor, “Energy efﬁcient user association and power allocation in millimeterwave-based ultra dense networks with energy harvesting base stations,” IEEE Journal on Selected Areas in Communications, vol. 35, no. 9, pp. 1936–1947, September 2017.

- [115] A. Azizi, N. Mokari, and M. R. Javan, “Joint radio resource allocation, 3d placement and user association of aerial base stations in iot networks,” arXiv preprint arXiv:1710.05315, 2017.
- [116] A. K. Bairagi, M. S. Munir, M. Alsenwi, N. H. Tran, and C. S. Hong, “A matching based coexistence mechanism between embb and urllc in 5g wireless networks,” in Proceedings of the 34th ACM/SIGAPP Symposium on Applied Computing, 2019, pp. 2377–2384.
- [117] K. Kim and C. S. Hong, “Optimal task-uav-edge matching for computation ofﬂoading in uav assisted mobile edge computing,” in 20th AsiaPaciﬁc Network Operations and Management Symposium (APNOMS). IEEE, 2019, pp. 1–4.
- [118] R. O. Afolabi, A. Dadlani, and K. Kim, “Multicast scheduling and resource allocation algorithms for ofdma-based systems: A survey,” IEEE Communications Surveys & Tutorials, vol. 15, no. 1, pp. 240– 254, First Quarter 2012.
- [119] B. Di, S. Bayat, L. Song, and Y. Li, “Radio resource allocation for downlink non-orthogonal multiple access (noma) networks using matching theory,” in IEEE global communications conference (GLOBECOM). IEEE, 2015, pp. 1–6.
- [120] T. LeAnh, N. H. Tran, W. Saad, L. B. Le, D. Niyato, T. M. Ho, and C. S. Hong, “Matching theory for distributed user association and resource allocation in cognitive femtocell networks,” IEEE Transactions on Vehicular Technology, vol. 66, no. 9, pp. 8413–8428, September 2017.
- [121] A. Zakeri, M. Moltafet, and N. Mokari, “Joint radio resource allocation and sic ordering in noma-based networks using submodularity and matching theory,” IEEE Transactions on Vehicular Technology, vol. 68, no. 10, pp. 9761–9773, October 2019.
- [122] J. C. C. Chica, J. C. Imbachi, and J. F. B. Vega, “Security in sdn: A comprehensive survey,” Journal of Network and Computer Applications, vol. 159, p. 102595, June 2020.
- [123] K. K. R. Kendall, “A database of computer attacks for the evaluation of intrusion detection systems,” Ph.D. dissertation, Massachusetts Institute of Technology, 1999.
- [124] L. U. Khan, Z. Han, D. Niyato, and C. S. Hong, “Socially-awareclustering-enabled federated learning for edge networks,” IEEE Transactions on Network and Service Management, vol. 18, no. 3, pp. 2641– 2658, September 2021.
- [125] K. Yang, T. Jiang, Y. Shi, and Z. Ding, “Federated learning via overthe-air computation,” IEEE Transactions on Wireless Communications, vol. 19, no. 3, pp. 2022–2035, March 2020.
- [126] W. Liu, X. Zang, Y. Li, and B. Vucetic, “Over-the-air computation systems: Optimization, analysis and scaling laws,” IEEE Transactions on Wireless Communications, vol. 19, no. 8, pp. 5488–5502, August 2020.
- [127] T. Jiang and Y. Shi, “Over-the-air computation via intelligent reﬂecting surfaces,” in 2019 IEEE Global Communications Conference (GLOBECOM). IEEE, 2019, pp. 1–6.
- [128] M. Chen, H. V. Poor, W. Saad, and S. Cui, “Wireless communications for collaborative federated learning,” IEEE Communications Magazine, vol. 58, no. 12, pp. 48–54, January 2020.
- [129] U. Majeed, L. U. Khan, and C. S. Hong, “Cross-silo horizontal federated learning for ﬂow-based time-related-features oriented trafﬁc classiﬁcation,” in 2020 21st Asia-Paciﬁc Network Operations and Management Symposium (APNOMS), 2020, pp. 389–392.
- [130] F. Emmert-Streib, Z. Yang, H. Feng, S. Tripathi, and M. Dehmer, “An introductory review of deep learning for prediction models with big data,” Frontiers in Artiﬁcial Intelligence, vol. 3, p. 4, February 2020.
- [131] S. Pouyanfar, S. Sadiq, Y. Yan, H. Tian, Y. Tao, M. P. Reyes, M.L. Shyu, S.-C. Chen, and S. S. Iyengar, “A survey on deep learning: Algorithms, techniques, and applications,” ACM Computing Surveys (CSUR), vol. 51, no. 5, pp. 1–36, September 2018.
- [132] M. Masdari, S. S. Nabavi, and V. Ahmadi, “An overview of virtual machine placement schemes in cloud computing,” Journal of Network and Computer Applications, vol. 66, pp. 106–127, May 2016.
- [133] P. Thakur and D. K. Shrivastava, “Interoperability issues and standard architecture for service delivery in federated cloud: a review,” in International Conference on Computational Intelligence and Communication Networks. IEEE, 2015, pp. 908–912.
- [134] H. F. Atlam, A. Alenezi, M. O. Alassaﬁ, and G. B. Wills, “Blockchain with internet of things: Beneﬁts, challenges, and future directions,” International Journal of Intelligent Systems & Applications, vol. 10, no. 6, 2018.
- [135] M. Stoyanova, Y. Nikoloudakis, S. Panagiotakis, E. Pallis, and E. K. Markakis, “A survey on the internet of things (iot) forensics: challenges, approaches, and open issues,” IEEE Communications Surveys & Tutorials, vol. 22, no. 2, pp. 1191–1221, Secondquarter 2020.

Latif U. Khan received his Ph.D. degree (Computer Engineering) and MS (Electrical Engineering) degree with distinction from Kyung Hee University (KHU), South Korea in 2021 and University of Engineering and Technology (UET), Peshawar, Pakistan, in 2017, respectively. He worked as a leading researcher in the intelligent Networking Laboratory under a project jointly funded by the prestigious Brain Korea 21st Century Plus and Ministry of Science and ICT, South Korea. Prior to joining the KHU, he has served as a faculty member and

[Figure 507]

research associate in the UET, Peshawar, Pakistan. He has published his works in highly reputable conferences and journals. He is the author/co-author of two conference best paper awards. He is also author of two books, such as ”Network Slicing for 5G and Beyond Networks” and ”Federated Learning for Wireless Networks”. His research interests include analytical techniques of optimization and game theory to edge computing, end-to-end network slicing, and federated learning for wireless networks.

Walid Saad (S’07, M’10, SM’15, F’19) received the Ph.D. degree from the University of Oslo, Oslo, Norway, in 2010.,He is currently a Professor with the Department of Electrical and Computer Engineering, Virginia Tech, Blacksburg, VA, USA, where he leads the Network sciEnce, Wireless, and Security (NEWS) Laboratory. His research interests include wireless networks, machine learning, game theory, security, unmanned aerial vehicles (UAV), cyberphysical systems, and network science.,Dr. Saad was named the Stephen O. Lane Junior Faculty Fellow

[Figure 508]

at Virginia Tech, from 2015 to 2017. In 2017, he was named as the College of Engineering Faculty Fellow. He was a recipient of the NSF CAREER Award in 2013, the Air Force Ofﬁce of Scientiﬁc Research (AFOSR) Summer Faculty Fellowship in 2014, and the Young Investigator Award from the Ofﬁce of Naval Research (ONR) in 2015. He was the author/coauthor of eight conference best paper awards at WiOpt in 2009, the International Conference on Internet Monitoring and Protection (ICIMP) in 2010, the IEEE Wireless Communications and Networking Conference (WCNC) in 2012, the IEEE International Symposium on Personal, Indoor and Mobile Radio Communications (PIMRC) in 2015, IEEE SmartGridComm in 2015, EuCNC in 2017, IEEE GLOBECOM in 2018, and the International Federation for Information Processing (IFIP) International Conference on New Technologies, Mobility and Security (NTMS) in 2019. He was also a recipient of the 2015 Fred W. Ellersick Prize from the IEEE Communications Society, the 2017 IEEE ComSoc Best Young Professional in Academia award, the 2018 IEEE ComSoc Radio Communications Committee Early Achievement Award, and the 2019 IEEE ComSoc Communication Theory Technical Committee. He received the Dean’s Award for Research Excellence from Virginia Tech in

- 2019. He also serves as an Editor for the IEEE Transactions on Wireless Communications, the IEEE Transactions on Mobile Computing, and the IEEE Transactions on Cognitive Communications and Networking. He is also an Editor-at-Large for the IEEE Transactions on Communications. He is also an IEEE Distinguished Lecturer. (Based on document published on 18 May
- 2020).

Zhu Han (S’01, M’04, SM’09, F’14) received the B.S. degree in electronic engineering from Tsinghua University, in 1997, and the M.S. and Ph.D. degrees in electrical and computer engineering from the University of Maryland, College Park, in 1999 and 2003, respectively.

[Figure 509]

From 2000 to 2002, he was an R&D Engineer of JDSU, Germantown, Maryland. From 2003 to 2006, he was a Research Associate at the University of Maryland. From 2006 to 2008, he was an assistant professor at Boise State University, Idaho. Currently,

he is a John and Rebecca Moores Professor in the Electrical and Computer Engineering Department as well as in the Computer Science Department at the University of Houston, Texas. His research interests include wireless resource allocation and management, wireless communications and networking, game theory, big data analysis, security, and smart grid. Dr. Han received an NSF Career Award in 2010, the Fred W. Ellersick Prize of the IEEE Communication Society in 2011, the EURASIP Best Paper Award for the Journal on Advances in Signal Processing in 2015, IEEE Leonard G. Abraham Prize in the ﬁeld of Communications Systems (best paper award in IEEE JSAC) in 2016, and several best paper awards in IEEE conferences. Dr. Han was an IEEE Communications Society Distinguished Lecturer from 2015-2018, AAAS fellow since 2019 and ACM distinguished Member since 2019. Dr. Han is 1% highly cited researcher since 2017 according to Web of Science. Dr. Han is also the winner of 2021 IEEE Kiyo Tomiyasu Award, for outstanding early to mid-career contributions to technologies holding the promise of innovative applications, with the following citation: “for contributions to game theory and distributed management of autonomous communication networks.”

Ekram Hossain (F’15) is a Professor in the Department of Electrical and Computer Engineering at University of Manitoba, Canada. He is a Member (Class of 2016) of the College of the Royal Society of Canada, a Fellow of the Canadian Academy of Engineering, and a Fellow of the Engineering Institute of Canada. He was elevated to an IEEE Fellow “for contributions to spectrum management and resource allocation in cognitive and cellular radio networks”. He was listed as a Clarivate Analytics Highly Cited Researcher in Computer Science in

[Figure 510]

2017, 2018, 2019, and 2020. Currently he serves as the Editor-in-Chief of IEEE Press. Previously he served as the Editor-in-Chief for the IEEE Communications Surveys and Tutorials (2012–2016).

Mohsen Guizani (S’85, M’89, SM’99, F’09) received his B.S. (with distinction) and M.S. degrees in electrical engineering, and M.S. and Ph.D. degrees in computer engineering from Syracuse University, New York, in 1984, 1986, 1987, and 1990, respectively. He is currently a professor in the Computer Science and Engineering Department at Qatar University. Previously, he served in different academic and administrative positions at the University of Idaho, Western Michigan University, the University of West Florida, the University of Missouri-Kansas

[Figure 511]

City, the University of Colorado-Boulder, and Syracuse University. His research interests include wireless communications and mobile computing, computer networks, mobile cloud computing, security, and smart grid. He is currently the Editor-in-Chief of IEEE Network, serves on the Editorial Boards of several international technical journals, and is the Founder and Editorin-Chief of the Wireless Communications and Mobile Computing journal (Wiley). He is the author of nine books and more than 500 publications in refereed journals and conferences. He has guest edited a number of Special Issues in IEEE journals and magazines. He has also served as a TPC member, Chair, and General Chair of a number of international conferences. Throughout his career, he received three teaching awards and four research awards. He also received the 2017 IEEE Communications Society WTC Recognition Award as well as the 2018 AdHoc Technical Committee Recognition Award for his contribution to outstanding research in wireless communications and ad hoc sensor networks. He was the Chair of the IEEE Communications Society Wireless Technical Committee and the Chair of the TAOS Technical Committee. He served as a IEEE Computer Society Distinguished Speaker and is currently an IEEE ComSoc Distinguished Lecturer. He is a Senior Member of ACM.

Choong Seon Hong (S’95-M’97-SM’11) received the B.S. and M.S. degrees in electronic engineering from Kyung Hee University, Seoul, South Korea, in 1983 and 1985, respectively, and the Ph.D. degree from Keio University, Tokyo, Japan, in 1997. In 1988, he joined KT, Gyeonggi-do, South Korea, where he was involved in broadband networks as a member of the Technical Staff. Since 1993, he has been with Keio University. He was with the Telecommunications Network Laboratory, KT, as a Senior Member of Technical Staff and as the

[Figure 512]

Director of the Networking Research Team until 1999. Since 1999, he has been a Professor with the Department of Computer Science and Engineering, Kyung Hee University. His research interests include future Internet, intelligent edge computing, network management, and network security. Dr. Hong is a member of the Association for Computing Machinery (ACM), the Institute of Electronics, Information and Communication Engineers (IEICE), the Information Processing Society of Japan (IPSJ), the Korean Institute of Information Scientists and Engineers (KIISE), the Korean Institute of Communications and Information Sciences (KICS), the Korean Information Processing Society (KIPS), and the Open Standards and ICT Association (OSIA). He has served as the General Chair, the TPC Chair/Member, or an Organizing Committee Member of international conferences, such as the Network Operations and Management Symposium (NOMS), International Symposium on Integrated Network Management (IM), Asia-Paciﬁc Network Operations and Management Symposium (APNOMS), End-to-End Monitoring Techniques and Services (E2EMON), IEEE Consumer Communications and Networking Conference (CCNC), Assurance in Distributed Systems and Networks (ADSN), International Conference on Parallel Processing (ICPP), Data Integration and Mining (DIM), World Conference on Information Security Applications (WISA), Broadband Convergence Network (BcN), Telecommunication Information Networking Architecture (TINA), International Symposium on Applications and the Internet (SAINT), and International Conference on Information Networking (ICOIN). He was an Associate Editor of the IEEE TRANSACTIONS ON NETWORK AND SERVICE MANAGEMENT and the IEEE JOURNAL OF COMMUNICATIONS AND NETWORKS. He currently serves as an Associate Editor for the International Journal of Network Management.

