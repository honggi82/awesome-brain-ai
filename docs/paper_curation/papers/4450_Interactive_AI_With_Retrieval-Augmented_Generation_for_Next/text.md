# Interactive AI with Retrieval-Augmented Generation for Next Generation Networking

Ruichen Zhang*, Hongyang Du*, Yinqiu Liu*, Dusit Niyato, Fellow, IEEE, Jiawen Kang, Sumei Sun, Fellow, IEEE, Xuemin (Sherman) Shen, Fellow, IEEE, and H. Vincent Poor, Life Fellow, IEEE

## arXiv:2401.11391v1[cs.NI]21Jan2024

Abstract—With the advance of artificial intelligence (AI), the emergence of Google Gemini and OpenAI Q* marks the direction towards artificial general intelligence (AGI). To implement AGI, the concept of interactive AI (IAI) has been introduced, which can interactively understand and respond not only to human user input but also to dynamic system and network conditions. In this article, we explore an integration and enhancement of IAI in networking. We first comprehensively review recent developments and future perspectives of AI and then introduce the technology and components of IAI. We then explore the integration of IAI into the next-generation networks, focusing on how implicit and explicit interactions can enhance network functionality, improve user experience, and promote efficient network management. Subsequently, we propose an IAI-enabled network management and optimization framework, which consists of environment, perception, action, and brain units. We also design the pluggable large language model (LLM) module and retrieval augmented generation (RAG) module to build the knowledge base and contextual memory for decision-making in the brain unit. We demonstrate the effectiveness of the framework through case studies. Finally, we discuss potential research directions for IAIbased networks.

Index Terms—IAI, networking, pluggable LLM module, AGI, RAG, problem formulation.

I. INTRODUCTION

With the current development trajectory, artificial intelligence (AI) is moving towards an important stage of realizing artificial general intelligence (AGI). The evolution of AI from its original rule-based algorithms to the adoption of advanced learning models marks a significant shift in the field of computing technology. This process is driven by the increasing growth and complexity of data, requiring more sophisticated AI solutions. While early AI models provided the foundation for modern data-driven environments, their limitations in handling dynamic and large-scale data have prompted the development of more advanced and novel methods. Among these

R. Zhang, H. Du, Y. Liu, and D. Niyato are with the School of Computer Science and Engineering, Nanyang Technological University, Singapore (e-mail: ruichen.zhang@ntu.edu.sg, hongyang001@e.ntu.edu.sg, yinqiu001@e.ntu.edu.sg, dniyato@ntu.edu.sg).

J. Kang is with the School of Automation, Guangdong University of Technology, China (e-mail: kavinkang@gdut.edu.cn).

S. Sun is with the Institute for Infocomm Research, Agency for Science, Technology and Research, Singapore (e-mail: sunsm@i2r.a-star.edu.sg).

X. Shen is with the Department of Electrical and Computer Engineering, University of Waterloo, Canada (e-mail: sshen@uwaterloo.ca).

H. V. Poor is with the Department of Electrical and Computer Engineering, Princeton University, Princeton, NJ08544, USA (e-mail: poor@princeton.edu).

* means equal contribution.

advancements, such as Google Gemini1 and OpenAI Q*2, human-in-the-loop (HITL) systems highlight the importance of integrating human insights into AI decision-making [1]. These systems combine human feedback with the AI’s learning process, improving the accuracy and contextual understanding of AI results. For example, a 2018 Stanford study showed that AI combined with HITL outperformed human or AI analysis alone in healthcare3. However, HITL systems have limitations in adaptability and real-time responsiveness because they rely on human input, which can be limited, unpredictable, and erroneous.

To address these challenges and effectively develop AGI, interactive AI (IAI) has been proposed. The primary difference between IAI and HITL lies in their interaction modes, i.e., IAI emphasizes immediate and direct interaction between AI and users, whereas HITL focuses on human participation and supervision in the AI decision-making process [1]. IAI systems are capable of instantaneously understanding user inputs, such as voice commands, text messages, or other interactive commands, and intelligently responding or executing tasks based on these inputs. This ability not only enhances user experience but also increases flexibility and effectiveness of AI applications in dynamic environments. Integrating IAI with technologies such as retrieval-augmented generation (RAG) and LangChain can further personalize network operations [2]. For example, RAG enables IAI systems to extract information from vast databases to enrich their responses and decisions. Combined with LangChain, which extends AI reasoning capabilities, IAI can provide more context-aware solutions based on the existing databases. The main advantages of IAI over the limitations of HITL systems, especially when augmented with RAG and LangChain, include:

- • Customizabilty and Personalizability: IAI, enhanced by RAG and LangChain, offers tailored solutions by aligning AI responses closely with user preferences and needs, resulting in more personalized and user-centric AI applications.
- • Better Flexibility: IAI’s direct user interaction, supported by LangChain’s extended reasoning, can offer more flexibility to adapt to different network scenarios and users’ requirements, enhancing the system’s versatility and satisfaction.

- 1https://deepmind.google/technologies/gemini/#introduction
- 2https://community.openai.com/t/what-is-q-and-when-we-will-hear-

more/521343

- 3https://scopeblog.stanford.edu/2018/05/08/artificial-intelligence-in-

medicine-predicting-patient-outcomes-and-beyond/

• Less Bias: The combination of IAI with RAG and LangChain minimizes the reliance on human intervention, thus reducing the potential for human bias in AI decisions and leading to more objective outcomes.

TABLE I SUMMARY OF ABBREVIATIONS.

|Abbreviation|Full name|Description|
|---|---|---|
|AGI|Artificial General Intelligence|AI capable of understanding, learning, and applying intelligence across a broad range of tasks at human-level proficiency|
|GAI|Generative Artificial Intelligence|AI systems that focus on creating novel data and patterns, often used for tasks involving innovation and design|
|IAI|Interactive Artificial Intelligence|AI that emphasizes immediate, direct interaction with users for decision-making and learning|
|MOE|Mixture of Experts|An approach in AI using multiple expert models, each specialized in different aspects of a dataset or problem|
|RAG|Retrieval Augmented Generation|An approach that enhances generative models by retrieving relevant information from database to improve the generation|
|LLM|Large Language Model|AI models designed to process and interact using human language, capable of handling extensive text data|
|HITL|Human-in-the-Loop|A system where human participation and oversight are integrated into the AI decision-making process|
|PAI|Predictive Artificial Intelligence|AI systems that focus on forecasting future events or trends based on historical data and predictive algorithms|
|TAI|Traditional Artificial Intelligence|Early AI models based on rule-based algorithms and structured data analysis|
|GAN|Generative Adversarial Network|AI models where two neural networks compete, often used for generating new data that mimics real data|
|DRL|Deep Reinforcement Learning|AI models learn to make decisions by trial and error, using deep learning to process complex inputs|
|CNN|Convolutional Neural Network|AI models effective for analyzing visual imagery, known for pattern recognition in structured data|
|GDM|Generative Diffusion Model|AI models that generate data through a process of iterative refinement, often used for precise outputs|

It is particularly important to integrate IAI into wireless networks, given its dynamic nature and requirement to continuously adapt the dynamic changes. Fortunately, the capabilities of IAI are particularly promising in addressing these challenges. Its interactive adaptive resource management can optimize the utilization of network resources and improve network performance. For example, in a network with changing user requirements, IAI can dynamically allocate bandwidth to maintain high performance given instantaneous user experience feedback. Although the integration of IAI into networking has several potential advantages, the following issues need to be addressed:

- • Q1: Why is IAI suitable for networking?
- • Q2: Which networking challenges can IAI address?
- • Q3: How can IAI with RAG be applied in networking? Therefore, in this article, we attempt to provide forward-

neural networks (CNNs), PAI and DAI are good at learning special paradigms from large data sets [4]. PAI/DAI, with their enhanced learning algorithms, advances beyond the capabilities of TAI. However, their reliance on extensively annotated datasets, primarily for classification and prediction, has practical limitations, leading to the emergence of GAI.

looking research to answer the above “Why, Which, and How" questions. To the best of the authors’ knowledge, the synergy between IAI and networking is still an open issue. The contributions of this article are summarized as follows.

- • A1: We first review some aspects of the development of AI, then introduce the features, technologies, and composition of IAI, and finally overview the IAI on networking.
- • A2: We explore the integration of IAI in networking, focusing on how both implicit and explicit interactions enhance network functionalities, improve user experience, and facilitate efficient network management.
- • A3: We construct an IAI-enabled network management and optimization framework. It consists of environment, action, brain, and perception. More importantly, we design pluggable LLM and RAG modules to build the knowledge base and contextual memory for decisionmaking. Simulation results based on a real network optimization case study verify the effectiveness of the proposed framework.

##### Phase 3: Generative Artificial Intelligence (GAI) GAI

marks a new era where AI systems can create new data and patterns, showcasing a degree of creativity [5]. With the advent of generative diffusion models (GDMs) and generative adversarial networks (GANs), AI’s role expands from analysis to creation, which can produce innovative outputs and simulations. However, GAI’s reliance on pre-existing data patterns has limitations such as generating inaccurate results, leading to the emergence of IAI.

##### Phase 4: Interactive Artificial Intelligence (IAI) IAI goes

beyond traditional data interaction paradigms by engaging human users in dynamic and reciprocal information exchanges. This stage allows the AI system to contextualize interactions and learn from user input, thus facilitating adaptive feedback mechanisms [6]. As a result, AI systems can bridge the gap between AI and human interaction and then move towards AGI.

II. OVERVIEW OF IAI AND NETWORKING

This section provides an overview of IAI, where some abbreviations are summarized in Table I.

For clarity, the evolution of AI development is illustrated in Fig. 1. B. Overview of IAI

A. The development of AI

##### Phase 1: Traditional Artificial Intelligence (TAI) TAI

IAI is based on the principle of dynamic information exchange to meet the needs of administrators and human endusers, where the foundation of IAI lies in the following AI technologies:

consists of rule-based systems designed for specific tasks within well-defined parameters [3]. It leverages algorithms such as support vector machines (SVMs) and other fundamental methods to excel at pattern recognition and basic prediction tasks. Although TAI systems are effective at processing structured data, their limited flexibility highlights the need for more dynamic AI approaches, leading to the development of discriminative AI/predictive AI.

Retrieval-Augmented Generation (RAG): RAG plays a pivotal role in IAI framework by merging retrieval-based and generative AI techniques. RAG allows IAI systems to access a vast external knowledge base, retrieving relevant information to augment the generation process [2].

Large Language Models (LLMs): LLMs are a cornerstone of IAI, particularly due to their capacity to process and

##### Phase 2: Predictive AI (PAI) /Discriminative AI (DAI)

With the use of deep neural networks such as convolutional

[Figure 1]

[Figure 2]

###### Traditional Reinforcement ArtificialIntelligence

[Figure 3]

[Figure 4]

[Figure 5]

Learning

[Figure 6]

[Figure 7]

[Figure 8]

###### GENERATIVE

The algorithms that

[Figure 9]

Reinforcement learning (RL) is an interdisciplinary area of machine learning and optimal control concerned with how an intelligent agent ought to take actions in a dynamic environment to maximize the cumulative reward. Supportive

predict or classify by learning rules and patterns from data.

Artificial Intelligence

Enables

[Figure 10]

[Figure 11]

GAN-2014

Supplements

[Figure 12]

SVM-1995 Random forest-2001

GAN can generate realistic synthetic data by a generator and a discriminator.

• Features

and

extensions

[Figure 13]

Evolutionary branch

[Figure 14]

Creativity Learn data distribution Diversity Fidelity

| |
|---|

and

[Figure 15]

[Figure 16]

###### DISCRIMIMATIVE

Intertwined

[Figure 17]

[Figure 18]

###### DBM-2015

Artificial Intelligence

DBM can generate realistic data samples by starting with noise.

[Figure 19]

[Figure 20]

Data augmentation

Discriminative AI mainly focuses on distinguishing or distinguishing different categories in the data set.

Incorporates

CNN-1989 LSTM-1997

[Figure 21]

[Figure 22]

[Figure 23]

Integrate the characteristics of AI technology and RL technology

[Figure 24]

[Figure 25]

[Figure 26]

###### INTERACTIVE

Artificial Intelligence

[Figure 27]

Potential applications:

[Figure 28]

[Figure 29]

###### Techniques

[Figure 30]

[Figure 31]

[Figure 32]

[Figure 33]

[Figure 34]

[Figure 35]

[Figure 36]

###### Components:

[Figure 37]

[Figure 38]

[Figure 39]

###### User interfaces

###### Evaluation feedback

###### GAI optimization

Dynamic traffic management

Enhanced user interaction

Facilitate communication between the IAI system and users, respond to specific user queries and provide

The evaluation assesses the validity of outputs, with feedback driving iterative improvements in problem-solving accuracy.

Deploy GAI methods to design solutions and enhancements for interaction scenarios.

[Figure 40]

[Figure 41]

Generative adversarial network

Retrieval-augmented generation

[Figure 42]

[Figure 43]

personalized feedback

Intelligent

Human-machine interfaces

resource allocation

Interactive AI is designed for user engagement. It responds to user inputs

[Figure 44]

###### Advantages:

[Figure 45]

[Figure 46]

[Figure 47]

[Figure 48]

Multi-modal interaction

Generative diffusion

###### Innovation ability

###### Strong adaptability

###### High efficiency

[Figure 49]

[Figure 50]

and queries, making it

Efficient execution capabilities can be achieved on various tasks.

Ability to adapt to a wide

Have the potential to innovate in many fields such as science and art

Advanced network security Data analysis and feature extraction

suitable for applications like customer support, virtual assistants, and recommendation systems.

range of work environments and needs

[Figure 51]

[Figure 52]

Large language model

Mixture of experts

Channel estimation and optimization

Anomaly signal identification

- Fig. 1. The evolution of AI. For IAI, we highlight the role of the mixture of experts, large language models, deep reinforcement learning, retrieval-augmented generation, and generative AI in promoting adaptability and interaction with users. Additionally, the components and advantages of IAI are also presented, emphasizing its efficiency and adaptability in different applications such as optimization and traffic management.

generate human-like text, which facilitates complex interactive dialogues. This ability is central to IAI’s focus on enhancing user interaction, as LLMs enable AI systems to comprehend and respond to natural language inputs in a conversational manner, thereby significantly improving the interactive and intuitive nature of AI systems [7].

Multi-modal Interaction: IAI systems are not limited to a single modal; they are adept at understanding and responding to various input types, such as text, voice, and images [8]. This multi-modal interaction capability is fundamental to IAI, embodying the principle of versatility and adaptability in interactions. It ensures that AI systems can engage with users in the most natural and intuitive ways possible, adapting to different interaction modes seamlessly.

Mixture of Experts (MOE): The MOE framework is an integral component of IAI that embodies its responsiveness to specialized situation-awareness. MOE models are composed of multiple expert sub-models, each trained to handle different aspects or subsets of the data [7]. This specialization enables IAI systems to leverage the collective expertise of these individual models to solve complex problems. The gating mechanism is the core feature of MOE, which dynamically determines the relevance of each expert to a given input, thereby directing the input to the most appropriate expert.

Deep Reinforcement Learning (DRL): DRL embodies the interactivity and adaptability of IAI. It revolves around learning from interactions with the environment and making

decisions based on feedback, such as rewards and penalties [9]. This principle aligns well with the idea that IAI learns and develops through continuous interaction with the user or environment.

Generative Diffusion Models (GDMs): GDMs improve iteratively through interactions, consistent with the principles of IAI. These models generate data by learning to reverse a diffusion process, which essentially involves a series of interacting steps [5]. Each iteration in the process presents an opportunity for the model to adapt and refine its output, emphasizing the IAI principle of continuous evolution and response to new information.

Generative Adversarial Networks (GANs): GANs, with their dueling network structure, inherently align with IAI’s principles of interactive learning. The continuous learning process within GANs, where each network learns from the other, enables the system to adaptively refine its outputs [8].

C. Features of IAI

In the networking domain, IAI systems are characterized by three main components, each of which is an integral part of its functionality as follows:

User Interfaces: Modern IAI systems have revolutionized user interfaces (UIs), extending beyond conventional text and graphical interfaces. These systems incorporate LLMs and multi-modal techniques, allowing users to interact with network management systems through conversational language.

TABLE II SUMMARY OF POTENTIAL ISSUES OF IAI.

|Tech Issues|Differences| |Layers|
|---|---|---|---|
| |Traditional methods|Interactive methods|IAI advantages|
|Channel Estimation and Optimization|-Available methods: Fourier-based techniques, CNNs<br>-Description: Relies on static models for signal estimation<br>-Cons: Not suited for dynamic environments, high overhead, prone to model mismatch<br>|-Available methods: MOE, GANs<br>-Description: Utilizes user feedback and algorithms for channel optimization<br>-Pros: Resilient to changes, efficient, higher accuracy<br>|Potential Advantages for Physical layer:<br><br>-Enhanced Accuracy: GANs provide refined channel models improving signal clarity and reducing interference.<br>-Predictive Modeling: GDMs enable precise channel predictions, aligning real-world conditions.<br>-Real-Time Adaptation: DRL optimizes beamforming in real-time for changing network environments.<br>-Reduced Complexity: Automated processes through GANs and GDMs simplify the management of physical layer operations.<br>|
|Anomaly Signal Identification|-Available methods: Statistical analysis<br>-Description: Detects deviations using predefined criteria<br>-Cons: Poor adaptability, high false-positive rates, misses subtle anomalies<br>|-Available methods: Multi-modal, LLMs<br>-Description: Uses LLMs for real-time anomaly detection from diverse data<br>-Pros: Accurate, dynamic detection, reduced false alarms<br>| |
|Adaptive Beamforming|-Available methods: CVX, ZF/MRT/MMSE.<br>-Description: Uses mathematical modeling and fixed antenna patterns; lacks change adaptability<br>-Cons: Inflexible to fast user movement and fast channel changes<br>|-Available methods: RL, GANs<br>-Description: Adapts beamforming in real-time environments, GANs for training scenarios.<br>-Pros: Adaptable, improves spectral efficiency<br>| |
|Dynamic Traffic Management|-Available methods: Static routing algorithms<br>-Description: Uses preset routes; ignores live network status<br>-Cons: Unresponsive to real-time conditions, may cause congestion<br>|-Available methods: RL, GDMs<br>-Description: RL for traffic flow adaptively, GDMs for traffic prediction<br>-Pros: Better traffic handling, enhances network performance<br>|Potential Advantages for Network layer:<br><br>-Optimized Traffic Flow: DRL and GDMs enable dynamic management of data traffic, reducing congestion.<br>-Efficient Utilization: Intelligent allocation strategies via DRL and MOE maximize network resource usage.<br>-Enhanced Security: GANs provide advanced threat simulation for robust network security measures.<br>-Self-Improving Systems: DRL algorithms continuously learn and improve network performance.<br>|
|Intelligent Resource Allocation|-Available methods: Static resource partitioning, heuristic algorithms<br>-Description: Allocates based on predictions; no real-time adjustments<br>-Cons: Inefficient under variable loads, risk of resource misallocation<br>|-Available methods: RL, MOE<br>-Description: Allocates resources smartly, MOE for traffic pattern analysis<br>-Pros: More efficient use of network resources, better service quality<br>| |
|Advanced Network Security|-Available methods: Signature-based detection systems<br>-Description: Identifies threats using known signatures<br>-Cons: May not identify new or variant forms of attacks quickly, leading to a window of vulnerability<br>|-Available methods: GANs, LLMs<br>-Description: GANs for attack simulation, LLMs for threat detection<br>-Pros: Detects new threats, adapts security protocols<br>| |
|Enhanced User Interaction|-Available methods: Rule-based command interfaces, GUIs<br>-Description: Command interfaces need exact syntax; GUIs offer visuals<br>-Cons: Steep learning curve for commands; GUIs may lack depth in interaction<br>|-Available methods: RL, RAG<br>-Description: Personalizes interactions, RAG for natural responses<br>-Pros: Customized experiences, higher user interaction<br>|Potential Advantages for Application layer:<br><br>-Intuitive Interactions: LLMs and multi-modal technologies enhance user interface responsiveness.<br>-Personalized Experiences: Multi-modal capability allows for services based on user inputs and behaviors.<br>-In-Depth Analytics: LLMs process vast amounts of data for analysis and extraction, improving decisionmaking.<br>-User-Centric Design: The LLMs and multi-modal technologies ensure interfaces cater to diverse user needs.<br>|
|Human-Machine Interface|-Available methods: Physical controls, voice commands<br>-Description: Tactile and auditory interaction options<br>-Cons: Accessibility issues for some users; voice commands fail in noise<br>|-Available methods: LLMs, multi-modal<br>-Description: Integrates language and sensory data for interaction.<br>-Pros: Intuitive interfaces, complex data handling<br>| |
|Data Analysis and Feature Extraction|-Available methods: Batch processing, rule-based analytics<br>-Description: Processes large data volumes, uses set rules for analysis.<br>-Cons: Slow and intensive processing, might overlook new patterns<br>|-Available methods: RAG, MOE<br>-Description: RAG for unstructured data analysis, MOE for sequential data<br>-Pros: Deep analysis, enhanced machine learning inputs<br>| |

A notable example is Agent GPT4, which employs LLMs and multi-modal capability for interactive user interfaces in a dynamic plan-execute pattern. Unlike standard UIs, Agent GPT engages proactively with users, providing clarity for ambiguous instructions and continually modifying its approach based on user feedback.

Intelligent Evaluation and Adaptability: Network environments benefit from IAI systems that not only assess performance using real-time analytics and simulation-based testing but also adapt and evolve over time. These systems integrate cognitive network operations to create a feedback loop, continuously refining network configurations based on user inputs and environmental data. This enables AI models to develop their understanding strategies and enhance their decision-making processes. Google’s VirusTotal Code Insight5 is one such system that employs an LLM and MOE for script analysis, thus enabling human users to identify potential threats through responsive feedback during use.

Advanced Generative AI and Network Optimization: The core of IAI systems is the deployment of state-of-theart GAI. These systems utilize algorithms like GDM and TBM for network design optimization. They facilitate the automated generation of network topologies, simulate traffic for congestion forecasting, and provide routing optimization solutions. For instance, Google’s B4 network6 employs a combination of MOE and GAN techniques for capacity planning and traffic engineering, ensuring optimal data flow and resource

- 4https://agentgpt.reworkd.ai/de
- 5https://blog.virustotal.com/2023/04/introducing-virustotal-code-

insight.html

- 6https://www.b4networks.ca/

utilization. The generative process in these systems is iterative, leveraging both historical and real-time data to proactively adapt to evolving network conditions and user behavior trends.

D. IAI for Networking

IAI significantly benefits networking by integrating intelligence across multiple operational layers. It enhances networks from the physical layer to the application layer.

Physical Layer: In the physical layer, IAI can be used to improve network efficiency and reliability. A typical example is the application of channel estimation and optimization. IAI, particularly DRL approaches, leverage feedback-oriented neural network interaction to iteratively optimize beamforming patterns based on real-time environmental feedback, improving modulation techniques for robust communication [9]. This leads to more efficient use of the spectrum, reduced interference, and enhanced signal quality, particularly in dynamic environments where channel conditions frequently change.

Network Layer: In the network layer, IAI can be used to streamline network operations and enhance performance. A typical example is the application of dynamic network traffic management. IAI, particularly DRL and GDM, can dynamically manage and optimize network traffic flows by continuously learning and adapting to traffic conditions [5]. This includes predictive traffic modeling, real-time congestion management, and intelligent routing strategies, resulting in reduced latency, optimized bandwidth usage, and improved overall network resilience.

Application Layer: In the application layer, IAI can be used to enhance user interaction and experience. A typical example is the application of human-machine interfaces. IAI, partic-

TABLE III SUMMARY OF IMPLICIT AND EXPLICIT INTERACTION IN NETWORKING.

[Figure 53]

[Figure 54]

[Figure 55]

[Figure 56]

[Figure 57]

[Figure 58]

[Figure 59]

[Figure 60]

Implicit Interaction in Networking

#### Explicit Interaction in Networking

[Figure 61]

[Figure 62]

[Figure 63]

[Figure 64]

Implicit Interaction with Algorithm

Explicit Interaction with User Information

- 1) Adaptive Signal Processing: Utilizing IAI can significantly enhance this process by enabling the system to learn and adapt its signal processing strategies based on real-time data and interactions.
- 2) Predictive Resource Allocation: Referring to the allocation of network resources like bandwidth and power based on predicted future demands and usage patterns. Implementing IAI in this domain can result in more efficient and responsive resource management.

1) User Feedback Interaction: involving users providing direct input to influence the AI’s decision-making or output adjustments.

- 3) Anomaly Detection: Involving identifying unusual patterns or behaviors that may indicate a problem such as a security breach or network failure. IAI can significantly improve anomaly detection by learning complex patterns and detecting anomalies in real-time.

[Figure 65]

[Figure 66]

[Figure 67]

[Figure 68]

- 01

[Figure 69]

[Figure 70]

[Figure 71]

- 02

[Figure 72]

[Figure 73]

[Figure 74]

- 03

- 04

[Figure 75]

[Figure 76]

[Figure 77]

- 05

[Figure 78]

[Figure 79]

[Figure 80]

- 06

Interaction Feature

Interaction Feature

[Figure 81]

[Figure 82]

[Figure 83]

[Figure 84]

[Figure 85]

[Figure 86]

[Figure 87]

[Figure 88]

[Figure 89]

[Figure 90]

[Figure 91]

[Figure 92]

[Figure 93]

[Figure 94]

[Figure 95]

[Figure 96]

[Figure 97]

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

[Figure 108]

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

[Figure 133]

[Figure 134]

[Figure 135]

[Figure 136]

Interaction Frequency

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

[Figure 152]

[Figure 153]

[Figure 154]

[Figure 155]

[Figure 156]

Interaction Frequency

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

- 2) Network Configuration and Management: Referring to the process of setting up and maintaining network parameters and policies. The integration of explicit IAI in this domain simplifies complex tasks and enhances the accuracy of configurations.
- 3) Human-Computer Interfaces in Networks: Encompassing the ways users interact with networked computer systems. Explicit IAI can revolutionize HCI by facilitating more interactive and integrated user experiences.

[Figure 250]

[Figure 251]

[Figure 252]

[Figure 253]

[Figure 254]

VS

Periodic Interaction

[Figure 255]

[Figure 256]

[Figure 257]

[Figure 258]

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

Random Interaction

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

[Figure 325]

[Figure 326]

[Figure 327]

[Figure 328]

[Figure 329]

[Figure 330]

[Figure 331]

[Figure 332]

[Figure 333]

[Figure 334]

[Figure 335]

[Figure 336]

[Figure 337]

[Figure 338]

[Figure 339]

[Figure 340]

[Figure 341]

[Figure 342]

[Figure 343]

[Figure 344]

[Figure 345]

[Figure 346]

[Figure 347]

[Figure 348]

[Figure 349]

[Figure 350]

[Figure 351]

[Figure 352]

[Figure 353]

[Figure 354]

[Figure 355]

[Figure 356]

[Figure 357]

[Figure 358]

[Figure 359]

[Figure 360]

[Figure 361]

[Figure 362]

[Figure 363]

[Figure 364]

[Figure 365]

[Figure 366]

[Figure 367]

[Figure 368]

[Figure 369]

[Figure 370]

[Figure 371]

[Figure 372]

[Figure 373]

[Figure 374]

[Figure 375]

[Figure 376]

[Figure 377]

[Figure 378]

[Figure 379]

[Figure 380]

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

[Figure 445]

[Figure 446]

[Figure 447]

[Figure 448]

[Figure 449]

[Figure 450]

[Figure 451]

[Figure 452]

[Figure 453]

[Figure 454]

[Figure 455]

[Figure 456]

[Figure 457]

[Figure 458]

[Figure 459]

[Figure 460]

[Figure 461]

[Figure 462]

[Figure 463]

[Figure 464]

[Figure 465]

[Figure 466]

[Figure 467]

[Figure 468]

[Figure 469]

[Figure 470]

[Figure 471]

[Figure 472]

[Figure 473]

[Figure 474]

[Figure 475]

[Figure 476]

[Figure 477]

[Figure 478]

[Figure 479]

[Figure 480]

[Figure 481]

[Figure 482]

[Figure 483]

[Figure 484]

[Figure 485]

[Figure 486]

[Figure 487]

[Figure 488]

[Figure 489]

[Figure 490]

[Figure 491]

[Figure 492]

[Figure 493]

[Figure 494]

[Figure 495]

[Figure 496]

[Figure 497]

[Figure 498]

[Figure 499]

[Figure 500]

Interaction Benefits

Interaction Benefits

Accurate Information Flow Real-time Update

Accurate Information Flow Pre-Designed Process

ularly LLMs, can process and generate natural language for user interaction, while multi-modal methods integrate visual, auditory, and other data forms to enrich the interface [10]. This leads to more personalized and engaging user interactions, better accessibility for diverse user groups, and an overall more responsive and intelligent application environment.

For clarity, the potential issues of IAI in different layers are summarized in Table II.

III. INTERACTIVE APPLICATIONS IN NETWORKING

In this section, we explore the integration of IAI in networking, focusing on how both implicit and explicit interactions. For clarity, the summary of implicit and explicit interaction is shown in Table III.

- A. Implicit Interaction in Networking

Implicit interaction in networking refers to the process where AI systems engage and adapt to their environment, including network conditions and user behaviors, without direct external inputs or commands. The benefits of such interactions include increased system autonomy, improved adaptability to changing conditions, and enhanced overall network efficiency

- [9], [11], [12]. Some major applications of implicit interaction in networking are as follows:

Adaptive Signal Processing: Adaptive Signal Processing in wireless communications involves dynamically adjusting signal processing algorithms in response to changing network

conditions. Utilizing IAI can significantly enhance this process by enabling the system to learn and adapt its signalprocessing strategies based on real-time data and interactions. For example, in [11], the authors proposed an IAI framework for steganographic distortion learning framework. This framework employs a GAN composing two subnetworks, i.e., a steganographic generator and a steganalytic discriminator, which through adversarial training, learns the probabilities of embedding changes in pixels to minimize detectability. In this framework, implicit interactions in the form of adaptive learning allow the model to evolve from simple random embedding to advanced content-adaptive embedding, significantly improving its security performance with each iteration. Simulation results showed after 180,000 training iterations, the IAI model’s system performance steadily improved, achieving an average embedding rate close to the targeted capacity.

Predictive Resource Allocation: Predictive Resource Allocation refers to the allocation of network resources like bandwidth and power based on predicted future demands and usage patterns. Implementing IAI in this domain can result in more efficient and responsive resource management. For example, in [9], the authors proposed a DRL-based IAI method to optimize system energy efficiency (EE) by adjusting beamforming vectors, power splitting ratios, and phase shifts, considering users’ quality of service (QoS) and the transmitter’s power constraints. The proposed IAI method implicitly interacted with the whole network environment, learning to fine-tune these parameters without direct human input to satisfy energy harvesting and communication QoS requirements.

Simulation results reveal that this approach yields EE close to an upper bound scheme (i.e., about 2% performance gap) while significantly reducing computation time (i.e., five orders of magnitude), particularly in dynamic wireless conditions.

Anomaly Detection: Anomaly Detection in networking involves identifying unusual patterns or behaviors that may indicate a problem, such as a security breach or network failure. IAI can significantly improve anomaly detection by learning complex patterns and detecting anomalies in realtime. For example, in [12], the authors proposed an IAI framework to automatically identify dependencies between sensors for anomaly detection in multivariate time series data. The IAI framework employed a Gumbel-Softmax Samplingbased connection learning policy to automatically learn graph structures depicting sensor dependencies, and integrates this with graph convolutions and an IAI architecture for efficient anomaly detection. The framework’s implicit interaction involved determining bi-directional connections among sensors, where high probability values imply strong connections, enhancing the system’s ability to predict and identify anomalies. This method is effective as it incorporates user feedback and network interactions to refine its anomaly detection capability continually. Simulation results prove that the TBM-based IAI framework improves precision, recall, and F1-score by at least 6%, 16%, and 11%, respectively, compared with traditional methods in anomaly detection.

Lesson learned: The exploration of implicit IAI in networking underscores the integral role of automated adaptability and self-learning in enhancing network efficiency and security. A major benefit of implementing implicit IAI is its proficiency in navigating the complexities of dynamic network environments. Implicit IAI, through mechanisms like machine learning algorithms and predictive analytics, excels in discerning and adjusting to these changes autonomously. For instance, in adaptive signal processing, IAI has shown a notable improvement in efficiency, with performance enhancements measurable at approximately 10-15% in complex scenarios. In resource allocation, IAI has not only achieved near-optimal energy efficiency but also accelerated convergence speed by up to five times compared to traditional methods. Additionally, in anomaly detection, IAI’s continuous learning from network interactions has led to a substantial increase in accuracy, outperforming traditional methods by at least 6% to 16% in key metrics. These improvements highlight IAI’s real-time adaptability, faster processing, and reduced reliance on large data sets.

- B. Explicit Interaction in Networking

Explicit interaction in networking involves deliberate and direct engagement between users or network administrators and the AI system. This type of interaction facilitates precise control over network functionalities and enhances user involvement in decision-making processes, leading to more accurate and user-centric outcomes [13]–[15]. Some major applications of explicit interaction in networking are as follows:

User Feedback Interaction: User feedback interaction involves users providing direct input to influence the AI’s

decision-making or output adjustments. IAI enhances this process by enabling more intuitive and responsive interactions, where user feedback can dynamically shape AI responses or network adjustments. For example, in [13], the authors introduced the Query Generation Assistant, a search interface that uses the LLM-based IAI method to facilitate interactive and automatic query generation in challenging search scenarios such as cross-lingual retrieval. This system allows users to actively interact in refining queries generated by LLMs, providing feedback and edits throughout the process. It significantly improves qualitative analysis in complex search tasks and is a valuable tool for conducting human-in-the-loop simulations.

Network Configuration and Management: Network configuration and management refers to the process of setting up and maintaining network parameters and policies. The integration of explicit IAI in this domain simplifies complex tasks and enhances the accuracy of configurations. For example, in [14], the authors explored the use of the LLM-based IAI method to manage network configuration tasks. They introduce NETBUDDY, a system that translates high-level natural language requirements into low-level network configurations. This method involves explicit interactions where NETBUDDY decomposes the translation process into multiple steps, ensuring more accurate and efficient configurations, and demonstrating considerable improvement in simplifying and automating network management tasks. The simulation results showed that the method adopted not only ensures network accuracy but also increases efficiency by approximately 6 times compared with traditional ones.

Human-Computer Interfaces: Human-computer interfaces (HCI) in networking encompasses the ways users interact with networked computer systems. Explicit IAI can revolutionize HCI by facilitating more interactive and integrated user experiences. For example, in [15], the authors investigated machinein-the-loop creative writing using a multi-modal based IAI method that suggested improvements through sight, sound, and language, marking an innovative approach in AI-assisted creativity. This method engaged human users in explicit interactions, where they incorporated AI-generated suggestions into their writing, a process involving adaptability and cognitive integration. Simulations effectively demonstrated the potential of IAI method to enhance the creativity of human-machine collaboration.

Lesson learned: Explicit IAI interactions in networking emphasize the critical role of user involvement in shaping AIdriven functionalities. This approach highlights the integration of user feedback into AI systems, resulting in more precise and customized network solutions. Unlike conventional AI, which relies on predefined algorithms, explicit IAI uses user input to refine its decision-making. This direct engagement aligns AI outputs with user-specific needs and preferences. For instance, digital twins and semantic communications can use explicit IAI to interpret and prioritize data based on its meaning and relevance to user requirements. This not only ensures accuracy but also personalizes network operations to individual contexts. Furthermore, explicit IAI is able to create a collaborative environment, merging human expertise with AI

Perception

Environment

[Figure 501]

Brain

Prompt engineering

Database RAG

Multi-modal inputs

I want to maximize EE by jointly optimizing the transmit beamforming vectors, the PS ratios of SWIPT, the common message rates of RSMA, and the phase shifts of RIS. The information and EH QoS requirements, as well as the power budget at the transmitter are considered as constraints.

Hi, please help me formulate an optimization problem. I have show you the scenario latter. Based on your knowledge and do it step-bystep. If clear, reply me ok and wait for the following instruction.

Text Embeddings

[Figure 502]

[Figure 503]

[Figure 504]

[Figure 505]

Knowledge base

[Figure 506]

[Figure 507]

[Figure 508]

[Figure 509]

…

[Figure 510]

[Figure 511]

[Figure 512]

[Figure 513]

[Figure 514]

…

Sure, I can help you formulate an optimization problem. Please provide me with the scenario or problem you would like to optimize.

UAV RIS Multi-cell

Knowledge

The optimization problem is formulated as: Maximize: EE({{w_k},{α_i}, c_i},{Φ}) Subject to:

[Figure 515]

[Figure 516]

[Figure 517]

[Figure 518]

[Figure 519]

IAI

Embeddings

- • ∑c_i ≤ min_i R_i^{(C)}({{w_k}},{Φ},{α_i}) (Constraint 1)
- • c_i + R_i^{(P)}({{w_k}},{Φ},{α_i}) ≥ ξ_i (Constraint 2)
- • Γ_i^{(EH)}({{w_k}},{Φ},{α_i}) ≥ μ_i (Constraint 3)
- • P_T({{w_k}}) ≤ P_max (Constraint 4)
- • Φ_n ∈ Θ (Constraint 5)
- • α_i ∈ (0,1) (Constraint 6)
- • c_i ≥ 0 (Constraint 7)

IAI Agent

Agent

[Figure 520]

CF WPT MIMO

The scenario is about optimize the energy efficiency in RIS-assisted SWIPT networks with RSMA. What information do you need from me? Based on your knowledge and do it step-by-step.

Decision making

Retrieve Learn

[Figure 521]

[Figure 522]

Knowledge

Interaction

LLMs

### IAI

Planning Reasoning

[Figure 523]

[Figure 524]

###### Plug-in Part

[Figure 525]

[Figure 526]

[Figure 527]

[Figure 528]

Great, help me explain the above factors based on your knowledge.

[Figure 529]

[Figure 530]

[Figure 531]

To formulate an optimization problem for optimizing energy efficiency in RIS-assisted SWIPT networks with RSMA, I would need some specific

Certainly! 1. System Energy Efficiency: The objective of the optimization problem is to maximize the system energy efficiency.

[Figure 532]

###### Action

- 2. Decision Variables: The decision variables in the optimization problem are {{w_k},{α_i}, c_i}, which represent the transmit power, phase shifts, and time allocation, respectively.
- 3. Power Budget Constraint:

- Constraint 4 states that the total transmit power should not exceed the maximum power budget.

- 4. Quality of Service (QoS) Constraints: Constraints 1, 2, and 3 are related to the QoS requirements of the system.
- 5. Phase Shifts and Feasible Range:

- Constraint 5 states that the phase shifts of the reconfigurable intelligent surface (RIS) elements.
- 6. Power Splitting Ratio: Constraint

- 6 specifies that the power splitting ratio,
- 7. Non-Negative Time Allocation: Constraint 7 ensures that the time allocation is non-negative.

information about the system

###### IAI Agent IAI

and the objectives you want to achieve. Here are some key details that would be helpful:

Analysis Extraction

Summary Recall

Storage

[Figure 533]

[Figure 534]

- 1. System Model: Please provide a description of the RISassisted SWIPT network with RSMA.
- 2. Objective Function: Specify the objective you want to optimize.
- 3. Variables: Identify the decision variables that can be adjusted to optimize the system.
- 4. Constraints: Define any constraints that need to be satisfied in the optimization problem.

Agent

[Figure 535]

[Figure 536]

[Figure 537]

[Figure 538]

Formulation Model

[Figure 539]

[Figure 540]

History Context

Memory

…

- Fig. 2. In the IAI-enabled problem formulation framework, three key components are presented: brain, perception, and action. The brain units with LLM and RAG modules as the central processor, handling essential tasks such as memory retention, retrieval processing, and making decisions. Meanwhile, the perception module is responsible for acquiring and interpreting diverse data from the environment. Lastly, the action module implements responses and interacts with the environment, utilizing various tools for execution.

capabilities (i.e., MOE), thereby boosting the overall efficiency and effectiveness of network management.

aspect of complex network resource allocation. While this innovation offers distinct advantages to new network designers by making it easier to get involved, its main strengths are in making the optimization process more straightforward, efficiently managing network resources, and improving the accuracy and trustworthiness of network models.

IV. CASE STUDY: IAI-ENABLED PROBLEM FORMULATION FRAMEWORK

In this section, we propose a framework that utilizes an IAI agent with RAG to help network users and designers formulate optimization problems in the network domain.

B. Proposed Framework

Accordingly, to effectively generate problem modeling, as shown in Fig. 2, we propose an IAI-enabled problem formulation framework, which consists of the following units.

A. Motivations

Perception: The Perception component of the IAI-enabled problem formulation framework is akin to human sensory reception, drawing from diverse sources and modalities. This multi-modal approach enables the IAI to assimilate information from text, visuals, and numerical data. Upon receiving this data, the system employs prompt engineering to transform raw information into structured embeddings. These embeddings are designed to encapsulate the complexity of the input data in a format that is readily interpretable by the IAI agents. Consequently, the Perception component prepares the IAI to comprehend the nuances of the environment and facilitates informed decision-making. In our framework, the Perception component thus serves as the foundational interface between multifaceted data inputs and the IAI’s cognitive mechanisms, ensuring that the system’s responses are grounded in a comprehensive understanding of the environmental context.

In wireless network resource allocation, modeling complex real-world scenarios as mathematical optimization problems have traditionally required a deep understanding of complex equations and methods. This task can be challenging, particularly for newcomers or those with interdisciplinary backgrounds.

Fortunately, the IAI framework offers a transformative solution to these challenges. By interpreting the network environment and goals as defined by designers, the IAI system automatically formulates the appropriate optimization problem. This advancement speeds up the problem formulation process and importantly ensures that the optimization models accurately reflect the intricate details of network scenarios. Acting as a cognitive intermediary, the IAI framework enhances human capabilities with AI-driven insights, markedly reducing the complexity and manpower usually needed for such tasks. Furthermore, by automating the problem formulation phase

Brain: The Brain is the central component of the IAI system, functioning in a three-unit structure: database, storage,

- [10], IAI significantly lowers the risk of human error, a crucial

and decision-making. The RAG database contains a wealth of searchable academic texts, such as those pertaining to unmanned aerial vehicles (UAVs), reconfigurable intelligent surfaces (RISs), wireless power transfer (WPT), and more, as its training dataset. This corpus of knowledge is transformed into text embeddings that are stored within the IAI’s knowledge base. For the decision-making, the system adopts a plug-in architecture for selecting the appropriate LLM, such as GPT 4, LLAMA 2, Gemini, and Bloom. When the database unit and the decision-making unit are combined, they form the RAG module. RAG allows the brain to infer, learn, retrieve, and reason, combining its capabilities with database resources to plan and execute actions to provide appropriate strategies for generating problems. For the storage, it is a repository of the agent’s historical observations, thoughts, and actions. It enables the agent to effectively recall and apply previous strategies when tackling complex reasoning tasks, similar to how humans draw on memory to navigate unfamiliar situations. The Brain’s architecture is integral to the IAI’s learning process, providing a contextual understanding and the ability to utilize historical insights for informed decisionmaking, thereby enhancing the academic rigor of the system’s cognitive process.

Action: Within the IAI framework, the Action component responds to the Brain’s directions and performs tasks in the network environment. This unit of the system follows a clear four-step method. It starts by analyzing network designer inputs, guided by the Brain’s insights. Then, it pulls useful information from its knowledge base. Next, the module shapes the network problem into a clear mathematical form. The final step is to present the formulated optimization model. The Action module turns plans into real results, making sure that the IAI’s decisions have a direct and practical impact on the network.

Environment: The Environment component of the IAI framework is pivotal in encapsulating the application domain for the IAI agent’s operation. It represents the real-world network scenarios as described by the network designer, forming the foundation for the IAI’s problem formulation process. For instance, in a scenario where a network designer wants to formulate an optimization problem for a RIS-assisted SWIPT network with RSMA, the interaction begins with the network designer’s initial request for assistance. The IAI agent then prompts the network designer for specific details, such as the system model, the optimization objective, the decision variables, and any necessary constraints. Through this iterative dialogue, the network designer provides the required information step-by-step. Then, the network designer might describe the network’s configuration for optimizing EE, and the IAI agent will use its information to develop an appropriate optimization problem. This interactive process allows the IAI system to thoroughly understand the network designer-defined environment and generate an optimized problem model that aligns with the specific characteristics and requirements of the network scenario. It showcases how the Environment component acts as a collaborative stage, integrating network designer inputs with IAI functionality to create tailored problem-solving approaches for complex network environments.

Fig. 3. The chunk size versus the number of interaction rounds required to solve the network optimization task, where k represents the number of chunks that the LLM puts into context in each round of interaction.

C. Experiments

Experimental Settings: To explore the effectiveness of the proposed IAI agent, we apply it to solve a real-world network optimization problem. In our experiments, the pluggable LLM module is implemented by OpenAI APIs for calling the GPT4 model. The network-oriented knowledge base and context memory are built on LangChain.

Effectiveness of IAI Agent: As shown in Fig. 2, the user intends to optimize the energy efficiency in RIS-assisted simultaneous wireless information and power transfer (SWIPT) networks with rate splitting multiple access (RSMA) [9]. Traditionally, the network designer needs to search numerous articles, select an appropriate model, and apply it to the problem. With the help of an IAI agent, such a process can be realized automatically through four rounds of user-agent interactions. To be specific, the user first states the requirements, i.e., formulating a network optimization problem. Here, the chainof-thought prompting is applied to enhance the reasoning ability of the IAI agent. Then, the user further illustrates the specific scenario to the IAI agent, which then returns the stepby-step guidance of the entire optimization process. Afterward, the users clarify the optimization objective. Empowered by information retrieval techniques, the IAI agent will jointly search the local knowledge base and perform the inference. The resulting problem formulation perfectly aligns with the ground truth (i.e., the standard problem formulation from academic journals). Moreover, the user can acquire detailed explanations of all the factors.

Knowledge Base Settings: With the effectiveness of the IAI agent being verified, we further evaluate the influence of knowledge base settings on the interaction quality. Specifically, we adjust the chunk size for organizing knowledge embeddings in RAG module and test the number of interaction rounds required for solving the aforementioned task. As shown in Fig. 3, when k=1 and 3, setting chunk size as 2000 or 3000 can lead to the best interaction quality since the knowledge chunks can be effectively fetched. In contrast, if the chunk size decreases to 1000, the problem cannot be completely formulated within 10 rounds of interactions because the knowledge

[Figure 541]

[Figure 542]

[Figure 543]

[Figure 544]

System Description

[Figure 545]

I want to create an IAI model with powerful algorithm to formualte problem

I want to maximize EE by jointly optimizing the transmit beamforming vectors, the PS ratios of SWIPT, the common

How can a network designer create a model with only basic descriptions

message rates of RSMA, and the phase shifts of RIS. The information and EH QoS requirements, as well as the power budget at the transmitter are considered as constraints.

[Figure 546]

[Figure 547]

withmodel

Interactive

Doing alone

I miss essential components

My model is feasible

[Figure 548]

[Figure 549]

[Figure 550]

[Figure 551]

[Figure 552]

[Figure 553]

IAI modeling

Manual modeling

|[Figure 554]<br><br>The optimization problem is formulated as: Maximize: 𝐸𝐸({𝑤𝑘, 𝛼𝑖, 𝑐𝑖}, Φ) Subject to:<br><br>• ∑𝑐_𝑖 ≤ min<br><br>i<br><br>𝑅𝑖(𝐶)({𝑤𝑘}, Φ, 𝛼𝑖)<br><br>• 𝑐𝑖 + 𝑅𝑖(𝑃)({𝑤𝑘}, Φ, 𝛼𝑖) ≥ 𝜉𝑖 (Wrong constraint)<br>• Γ𝑖(𝐸𝐻)({𝑤𝑘}, Φ, 𝛼𝑖) ≥ 𝜇𝑖<br>• 𝑃𝑇({𝑤𝑘}) ≤ 𝑃𝑚𝑎𝑥<br>• Φ𝑛 ∈ Θ<br>• 𝛼𝑖 ∈ (0,1)<br>• 𝑐𝑖 ≥ 0<br>|
|---|

|[Figure 555]<br><br>The optimization problem is formulated as: Maximize: 𝐸𝐸({𝑤𝑘, 𝛼𝑖, 𝑐𝑖}, Φ) Subject to:<br><br>• ∑𝑐_𝑖 ≤ min<br><br>i<br><br>𝑅𝑖(𝐶)({𝑤𝑘}, Φ, 𝛼𝑖)<br><br>• 𝑐𝑖 + 𝑅𝑖(𝑃)({𝑤𝑘}, Φ, 𝛼𝑖) ≥ 𝜉𝑖<br>• Γ𝑖(𝐸𝐻)({𝑤𝑘}, Φ, 𝛼𝑖) ≥ 𝜇𝑖<br>• 𝑃𝑇({𝑤𝑘}) ≤ 𝑃𝑚𝑎𝑥<br>• Φ𝑛 ∈ Θ<br>• 𝛼𝑖 ∈ (0,1)<br>• 𝑐𝑖 ≥ 0<br>|
|---|

[Figure 556]

[Figure 557]

Real modeling

|[Figure 558]<br><br>The optimization problem is formulated as: Maximize: 𝐸𝐸({𝑤𝑘, 𝛼𝑖, 𝑐𝑖}, Φ) Subject to:<br><br>• ∑𝑐_𝑖 ≤ min<br><br>i<br><br>𝑅𝑖(𝐶)({𝑤𝑘}, Φ, 𝛼𝑖)<br><br>• 𝑐𝑖 + 𝑅𝑖(𝑃)({𝑤𝑘}, Φ, 𝛼𝑖) ≥ 𝜉𝑖<br>• Γ𝑖(𝐸𝐻)({𝑤𝑘}, Φ, 𝛼𝑖) ≥ 𝜇𝑖<br>• 𝑃𝑇({𝑤𝑘}) ≤ 𝑃𝑚𝑎𝑥<br>• Φ𝑛 ∈ Θ<br>• 𝛼𝑖 ∈ (0,1)<br>• 𝑐𝑖 ≥ 0<br>• ∀𝑖 ∈ 𝑁, ∀𝑘 ∈ 𝐾<br>|
|---|

Ideasfrom

Personal idea

model

[Figure 559]

[Figure 560]

System Solution

[Figure 561]

Using the same PPO-based DRL method to solve the above modeling problems

[Figure 562]

[Figure 563]

[Figure 564]

[Figure 565]

Action

[Figure 566]

Agent Net Critic Net

Value

[Figure 567]

[Figure 568]

[Figure 569]

[Figure 570]

Reward

[Figure 571]

State

Environment

RL framework

[Figure 572]

[Figure 573]

Experiment Result

The proposed IAI model

[Figure 574]

can help network designers by capturing essential

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

information and generate creative ideas

[Figure 575]

Fig. 4. Comparison of system performance under various optimization problem generation methods. The figure displays the effectiveness of the proposed IAI framework modeling against traditional real modeling (upper bound) and manual modeling approaches, where the PPO-based DRL method is set as the solution method to demonstrate the performance results.

that can be referred to is too limited. Note that extremely large chunk size is also undesirable. For instance, when the chunk size equals 4000, the problem formulation also fails since the LLM can hardly extract useful knowledge from large chunks. When the chunk size reaches 5000, the IAI agent cannot even perform inference due to the limited context size. If increasing k to 10, i.e., allowing the IAI agent to retrieve more chunks in each round, the interaction quality gets improved when chunk size equals 1000. However, the context oversize error happens in all other settings.

be prone to errors, especially when designers are novices or unfamiliar with certain aspects, such as overlooking or incorrectly defining constraints (e.g., decoding RSMA constraints in our example). Such oversights can lead to flawed optimization problems. Upon applying the same PPO-based optimization method for solving, it is observed that the performance of algorithms under our framework closely matches that of the original real problem formulation (i.e., in [9]), whereas manually designed optimization problems yield the lowest results. This difference is attributed to the strength of the IAI framework, which leverages LLM capabilities and features within LangChain to generate precise optimization problems through an interactive process. Therefore, the IAI framework ensures a more accurate and efficient problem formulation compared to traditional manual methods.

Performance Comparison: To demonstrate the efficacy of our proposed IAI framework, Fig. 4 shows an example to present a comparison of different ways for generating optimization problems. It is evident that the first step in creating an optimization problem involves providing a detailed problem description. Our IAI framework then interacts with this description, as illustrated in Fig. 2, to automatically derive the corresponding optimization problem. In contrast, network designers often rely on their experience to manually create optimization problems. However, this manual approach can

Lesson learned: Through the above experiments, we can observe that the IAI goes beyond GAI, which only considers the quality of generated content. Instead, the IAI agent is designed to help users accomplish specific tasks. Therefore, not only the core LLM but also the settings for other modules

that guarantee the smoothness and quality of interaction (e.g., the knowledge base and memory) should be well crafted.

V. FUTURE DIRECTIONS

In this section, we outline three main future directions for the improvement of IAI-enabled networking.

Integration with Emerging Technologies: IAI can enhance B5G/6G networks, particularly in real-time data processing, adapting to bandwidth and latency needs. Edge computing boosts IoT and smart city operations. Blockchain integration uses IAI for more secure, decentralized networks. IAI also makes semantic communications more context-sensitive and improves ISAC systems’ accuracy. These enhancements show IAI’s pivotal role in modern network technologies.

Security Aspects of IAI-Enabled Networks: Improving security in IAI networks is crucial. Future research should focus on IAI-driven protocols for early threat detection and adaptive response, automating security management, and evolving with emerging threats.

Evaluation of IAI systems: It is important to design a model that can evaluate IAI. In the future, AI evaluation criteria should be given to evaluate models generated by IAI instead of human user evaluation.

- [10] Z. Xi, W. Chen, X. Guo, W. He, Y. Ding, B. Hong, M. Zhang, J. Wang, S. Jin, E. Zhou et al., “The rise and potential of large language model based agents: A survey,” 2023, arXiv preprint arXiv:2309.07864.
- [11] W. Tang, S. Tan, B. Li, and J. Huang, “Automatic steganographic distortion learning using a generative adversarial network,” IEEE Signal Proces. Lett., vol. 24, no. 10, pp. 1547–1551, 2017.
- [12] Z. Chen, D. Chen, X. Zhang, Z. Yuan, and X. Cheng, “Learning graph structures with transformer for multivariate time-series anomaly detection in IoT,” IEEE Internet Things J., vol. 9, no. 12, pp. 9179–9189, 2021.
- [13] K. D. Dhole, R. Chandradevan, and E. Agichtein, “An interactive query generation assistant using LLM-based prompt modification and user feedback,” 2023, arXiv preprint arXiv:2311.11226.
- [14] C. Wang, M. Scazzariello, A. Farshin, D. Kostic, and M. Chiesa, “Making network configuration human friendly,” 2023, arXiv preprint arXiv:2309.06342.
- [15] N. Singh, G. Bernal, D. Savchenko, and E. L. Glassman, “Where to hide a stolen elephant: Leaps in creative writing with multimodal machine intelligence,” ACM Trans. Comput. Hum. Interact., vol. 30, no. 5, pp. 1–57, 2023.

VI. CONCLUSION

In this article, we have explored the integration and enhancement of IAI in networking. We have proposed a problem formulation framework by using IAI with RAG, where the effectiveness of the framework was verified through simulation results. Finally, some potential research directions for IAIbased networks were outlined.

REFERENCES

- [1] W. Xu, M. J. Dainoff, L. Ge, and Z. Gao, “Transitioning to human interaction with ai systems: New challenges and opportunities for HCI professionals to enable human-centered AI,” Int. J. Hum-Comput. Int., vol. 39, no. 3, pp. 494–518, 2023.
- [2] P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal, H. Küttler, M. Lewis, W.-T. Yih, T. Rocktäschel et al., “Retrievalaugmented generation for knowledge-intensive nlp tasks,” NIPS, vol. 33, pp. 9459–9474, 2020.
- [3] Y. Lu, “Artificial intelligence: a survey on evolution, models, applications and future trends,” J. Manag. Anal., vol. 6, no. 1, pp. 1–29, 2019.
- [4] Z. Li, F. Liu, W. Yang, S. Peng, and J. Zhou, “A survey of convolutional neural networks: analysis, applications, and prospects,” IEEE Trans. Neural. Netw. Learn. Syst., 2021.
- [5] H. Du, R. Zhang, Y. Liu, J. Wang, Y. Lin, Z. Li, D. Niyato, J. Kang, Z. Xiong, S. Cui et al., “Beyond deep reinforcement learning: A tutorial on generative diffusion models in network optimization,” 2023, arXiv preprint arXiv:2308.05384.
- [6] S. Teso, Ö. Alkan, W. Stammer, and E. Daly, “Leveraging explanations in interactive machine learning: An overview,” Front. Robot. AI, vol. 6, p. 1066049, 2023.
- [7] Z. Chen, Z. Wang, Z. Wang, H. Liu, Z. Yin, S. Liu, L. Sheng, W. Ouyang, Y. Qiao, and J. Shao, “Octavius: Mitigating task interference in MLLMs via MoE,” 2023, arXiv preprint arXiv:2311.02684.
- [8] R. Zhang, K. Xiong, H. Du, D. Niyato, J. Kang, X. Shen, and H. V. Poor, “Generative AI-enabled vehicular networks: Fundamentals, framework, and case study,” 2023, arXiv preprint arXiv:2304.11098.
- [9] R. Zhang, K. Xiong, Y. Lu, P. Fan, D. W. K. Ng, and K. B. Letaief, “Energy efficiency maximization in RIS-assisted SWIPT networks with RSMA: A PPO-based approach,” IEEE J. Sel. Areas Commun., vol. 41, no. 5, pp. 1413–1430, 2023.

