import csv
import html
import json
import math
import re
import shutil
import time
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import requests

try:
    from docx import Document
except ImportError:  # pragma: no cover - validation reports this if missing.
    Document = None


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DOCS_DIR = ROOT / "docs"
PAPER_DIR = ROOT / "paper"
CACHE_DIR = DATA_DIR / "cache"

START_YEAR = 1900
END_YEAR = 2026
YEARS = list(range(START_YEAR, END_YEAR + 1))
YEAR_RANGE_TEXT = f"{START_YEAR}-{END_YEAR}"
YEAR_FILE_STEM = f"{START_YEAR}_{END_YEAR}"

TARGET_PER_YEAR = 100
CANDIDATES_PER_YEAR = 1000
GENERATED_DATE = date.today().isoformat()

S2_BULK_URL = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"
S2_FIELDS = ",".join(
    [
        "paperId",
        "title",
        "year",
        "authors",
        "venue",
        "publicationVenue",
        "publicationDate",
        "citationCount",
        "influentialCitationCount",
        "abstract",
        "url",
        "externalIds",
        "openAccessPdf",
        "s2FieldsOfStudy",
        "publicationTypes",
    ]
)
S2_QUERIES = [
    "brain artificial intelligence",
    "brain machine learning",
    "brain deep learning",
    "brain neural network model",
    "brain inspired artificial intelligence",
    "computational neuroscience artificial intelligence",
    "cerebral cortex machine learning",
    "brain structure machine learning",
    "structural MRI machine learning brain",
    "functional connectivity machine learning brain",
    "connectome graph neural network",
    "brain network graph model",
    "neuroimaging artificial intelligence",
    "neuroimaging deep learning",
    "brain decoding machine learning",
    "neural decoding artificial intelligence",
    "brain computer interface deep learning",
    "BCI machine learning brain",
    "neuromorphic computing brain",
    "cognitive architecture brain",
    "reinforcement learning neuroscience",
    "predictive coding artificial intelligence",
    "representation learning neuroscience",
]
S2_MAX_PAGES_PER_QUERY = 1

PAPERS_JSON = f"papers_{YEAR_FILE_STEM}.json"
PAPERS_CSV = f"papers_{YEAR_FILE_STEM}.csv"
CANDIDATES_JSON = f"candidates_top{CANDIDATES_PER_YEAR}_{YEAR_FILE_STEM}.json"
CANDIDATES_CSV = f"candidates_top{CANDIDATES_PER_YEAR}_{YEAR_FILE_STEM}.csv"
TAXONOMY_CSV = f"papers_taxonomy_{YEAR_FILE_STEM}.csv"
PERIOD_ANALYSIS_JSON = f"period_analysis_{YEAR_FILE_STEM}.json"
OVERALL_ANALYSIS_JSON = f"overall_analysis_{YEAR_FILE_STEM}.json"
GITHUB_LINKS_JSON = f"github_links_{YEAR_FILE_STEM}.json"
LINK_AUDIT_JSON = f"link_audit_{YEAR_FILE_STEM}.json"
SKILL2_PROVENANCE_JSON = "paper_curation_skill2_provenance.json"

LANGUAGES = {
    "en": "English",
    "ko": "한국어",
    "zh": "中文",
    "ja": "日本語",
}

UI_LABELS = {
    "en": {
        "papers": "papers",
        "years": "active years",
        "citations": "citations",
        "categories": "categories",
        "keyIdea": "Key idea",
        "strengths": "Strengths",
        "limitations": "Limitations",
        "noKeyword": "No keyword selected.",
        "overview": "Category Overview",
        "researchLimitations": "Research Limitations",
        "allTaxonomies": "All Taxonomies",
        "topPaper": "Top paper",
        "showing": "Showing",
        "of": "of",
        "matchingPapers": "matching papers",
        "completeSet": "The complete set is in the data files.",
        "selected": "selected",
        "allTaxonomiesDescription": "All papers matching the current period and keyword filters, sorted by citation count across every taxonomy.",
        "categorySpecificLimitations": "Use the individual taxonomy rows below for category-specific context and limitations.",
        "paperLink": "paper",
        "influentialCitations": "influential citations",
        "score": "score",
        "noPapers": "No papers match the current filters.",
    },
    "ko": {
        "papers": "논문",
        "years": "활성 연도",
        "citations": "인용",
        "categories": "분류",
        "keyIdea": "핵심 아이디어",
        "strengths": "강점",
        "limitations": "한계",
        "noKeyword": "선택된 키워드가 없습니다.",
        "overview": "분류 개요",
        "researchLimitations": "연구상 한계",
        "allTaxonomies": "전체 분류",
        "topPaper": "대표 상위 논문",
        "showing": "표시 중",
        "of": "/",
        "matchingPapers": "일치 논문",
        "completeSet": "전체 목록은 데이터 파일에 있습니다.",
        "selected": "선택됨",
        "allTaxonomiesDescription": "현재 기간과 키워드 필터에 맞는 모든 논문을 분류 전체에서 인용 수 순으로 정렬했습니다.",
        "categorySpecificLimitations": "아래 개별 분류 행에서 분류별 맥락과 한계를 확인하세요.",
        "paperLink": "논문",
        "influentialCitations": "영향력 인용",
        "score": "점수",
        "noPapers": "현재 필터와 일치하는 논문이 없습니다.",
    },
    "zh": {
        "papers": "论文",
        "years": "活跃年份",
        "citations": "引用",
        "categories": "分类",
        "keyIdea": "核心思想",
        "strengths": "优势",
        "limitations": "局限",
        "noKeyword": "未选择关键词。",
        "overview": "分类概览",
        "researchLimitations": "研究局限",
        "allTaxonomies": "全部分类",
        "topPaper": "代表论文",
        "showing": "正在显示",
        "of": "/",
        "matchingPapers": "篇匹配论文",
        "completeSet": "完整集合见数据文件。",
        "selected": "已选择",
        "allTaxonomiesDescription": "按引用次数排序，显示当前年份和关键词筛选下跨全部分类的论文。",
        "categorySpecificLimitations": "请查看下方各分类行，了解分类特定的背景与局限。",
        "paperLink": "论文",
        "influentialCitations": "高影响引用",
        "score": "得分",
        "noPapers": "当前筛选条件下没有匹配论文。",
    },
    "ja": {
        "papers": "論文",
        "years": "対象年",
        "citations": "引用",
        "categories": "分類",
        "keyIdea": "主要アイデア",
        "strengths": "強み",
        "limitations": "限界",
        "noKeyword": "キーワードは選択されていません。",
        "overview": "分類概要",
        "researchLimitations": "研究上の限界",
        "allTaxonomies": "全分類",
        "topPaper": "代表論文",
        "showing": "表示中",
        "of": "/",
        "matchingPapers": "件の該当論文",
        "completeSet": "完全な一覧はデータファイルにあります。",
        "selected": "選択中",
        "allTaxonomiesDescription": "現在の期間とキーワード条件に合う全分類の論文を、引用数順に並べています。",
        "categorySpecificLimitations": "下の各分類行で、分類ごとの文脈と限界を確認してください。",
        "paperLink": "論文",
        "influentialCitations": "影響力のある引用",
        "score": "スコア",
        "noPapers": "現在の条件に一致する論文はありません。",
    },
}

RELEVANCE_TERMS = [
    "brain",
    "cerebral",
    "cerebrum",
    "cortex",
    "cortical",
    "neuron",
    "neurone",
    "neural",
    "neuroscience",
    "neurology",
    "neuroglia",
    "neuroimaging",
    "hippocampus",
    "amygdala",
    "cerebellum",
    "medulla oblongata",
    "brain stem",
    "brainstem",
    "forebrain",
    "midbrain",
    "hindbrain",
    "diencephalon",
    "thalamus",
    "hypothalamus",
    "basal ganglia",
    "central nervous system",
    "cerebrospinal",
    "encephalon",
    "encephalitis",
    "prefrontal",
    "connectome",
    "synapse",
    "glia",
    "microglia",
    "eeg",
    "meg",
    "ecog",
    "fmri",
    "mri",
]

STRUCTURE_TERMS = [
    "brain",
    "cerebral",
    "cerebrum",
    "cortex",
    "cortical",
    "hippocampus",
    "amygdala",
    "thalamus",
    "hypothalamus",
    "basal ganglia",
    "cerebellum",
    "brainstem",
    "connectome",
    "connectivity",
    "tractography",
    "structural mri",
    "diffusion mri",
    "diffusion tensor",
    "fmri",
    "mri",
    "eeg",
    "meg",
    "ecog",
    "neuron",
    "neural",
    "synapse",
]

AI_RELATION_TERMS = [
    "artificial intelligence",
    "machine learning",
    "deep learning",
    "neural network",
    "support vector",
    "random forest",
    "classification",
    "prediction",
    "predictive",
    "decoding",
    "encoding model",
    "representation learning",
    "reinforcement learning",
    "graph neural",
    "transformer",
    "bayesian",
    "computational model",
    "computational neuroscience",
    "brain-inspired",
    "brain inspired",
    "neuromorphic",
    "brain-computer",
    "brain computer",
    "bci",
    "cognitive architecture",
]

CATEGORIES = [
    {
        "name": "Neuroimaging and Brain Mapping",
        "slug": "neuroimaging-and-brain-mapping",
        "patterns": [
            "mri",
            "fmri",
            "magnetic resonance",
            "neuroimaging",
            "brain mapping",
            "diffusion tensor",
            "tractography",
            "pet",
            "connectome",
            "functional connectivity",
        ],
        "accent": "#2563eb",
        "secondary": "#14b8a6",
        "overview": [
            "High-citation brain imaging work maps structure, function, connectivity, and disease signatures across MRI, fMRI, PET, DTI, and multimodal cohorts.",
            "The strongest recent trend is large-scale population neuroimaging with harmonized preprocessing, shared atlases, and open datasets.",
            "Imaging biomarkers increasingly connect anatomy and physiology to cognition, development, degeneration, and psychiatric phenotypes.",
        ],
        "limitations": [
            "Scanner, protocol, site, and preprocessing variation can limit reproducibility across cohorts.",
            "Associational imaging biomarkers often need stronger longitudinal or intervention evidence before causal claims are made.",
            "Citation-ranked imaging lists can favor widely reused atlases and datasets over newer mechanistic studies.",
        ],
    },
    {
        "name": "EEG, MEG, and Electrophysiology",
        "slug": "eeg-meg-and-electrophysiology",
        "patterns": [
            "eeg",
            "meg",
            "electroencephal",
            "magnetoencephal",
            "erp",
            "evoked potential",
            "oscillation",
            "spectral",
            "electrophysiology",
            "ecog",
        ],
        "accent": "#0f766e",
        "secondary": "#60a5fa",
        "overview": [
            "Electrophysiology papers organize brain research around fast neural dynamics, oscillations, event-related responses, and disease-related rhythms.",
            "The field is moving toward source localization, multimodal fusion, mobile recordings, and machine-learning assisted decoding.",
            "EEG and MEG remain central where temporal precision, clinical accessibility, or non-invasive monitoring are more important than spatial detail.",
        ],
        "limitations": [
            "Low signal-to-noise ratio, artifacts, and source-localization uncertainty complicate interpretation.",
            "Many studies rely on controlled tasks and may not generalize to everyday behavior or clinical monitoring.",
            "Hardware, montage, preprocessing, and reference choices can make direct comparison difficult.",
        ],
    },
    {
        "name": "Cellular, Molecular, and Synaptic Neuroscience",
        "slug": "cellular-molecular-and-synaptic-neuroscience",
        "patterns": [
            "single cell",
            "single-cell",
            "single unit",
            "neuron",
            "neuronal",
            "synapse",
            "synaptic",
            "glia",
            "microglia",
            "astrocyte",
            "molecular",
            "transcriptomic",
            "calcium imaging",
        ],
        "accent": "#7c3aed",
        "secondary": "#f59e0b",
        "overview": [
            "This area captures cell types, circuits, synaptic plasticity, molecular pathways, and single-cell atlases that explain brain function from the microscopic level.",
            "High-throughput transcriptomics and large-scale cell atlases increasingly bridge molecular identity with anatomy and circuit function.",
            "Classic synaptic and plasticity papers remain prominent because they define mechanisms reused across learning, development, and disease research.",
        ],
        "limitations": [
            "Cellular mechanisms can be difficult to connect directly to whole-brain dynamics or human behavior.",
            "Single-cell sampling, dissociation, alignment, and batch effects can bias inferred cell populations.",
            "Animal and ex vivo findings need careful translation to human disease and cognition.",
        ],
    },
    {
        "name": "Cognitive and Systems Neuroscience",
        "slug": "cognitive-and-systems-neuroscience",
        "patterns": [
            "cognition",
            "memory",
            "attention",
            "perception",
            "decision",
            "learning",
            "behavior",
            "systems neuroscience",
            "hippocampus",
            "prefrontal",
            "visual cortex",
            "auditory cortex",
        ],
        "accent": "#dc2626",
        "secondary": "#f97316",
        "overview": [
            "Cognitive and systems work links brain networks, circuits, and dynamics to perception, action, memory, attention, learning, and decision making.",
            "The literature increasingly combines behavior, neural recording, imaging, computational models, and causal perturbation.",
            "Highly cited papers often become conceptual anchors for how brain systems implement cognition.",
        ],
        "limitations": [
            "Task designs can simplify cognition enough that ecological validity becomes uncertain.",
            "Cross-species alignment between circuits, behavior, and subjective experience remains imperfect.",
            "Correlational neural signatures need causal tests before they are treated as mechanisms.",
        ],
    },
    {
        "name": "Clinical Neurology and Neurodegeneration",
        "slug": "clinical-neurology-and-neurodegeneration",
        "patterns": [
            "alzheimer",
            "parkinson",
            "dementia",
            "stroke",
            "epilepsy",
            "multiple sclerosis",
            "neurology",
            "neurodegeneration",
            "brain tumor",
            "traumatic brain",
            "clinical",
            "patient",
        ],
        "accent": "#be123c",
        "secondary": "#06b6d4",
        "overview": [
            "Clinical brain research concentrates on diagnosis, mechanisms, biomarkers, treatment, and prognosis for neurological and neurodegenerative disorders.",
            "Large cohorts and biomarker frameworks have made dementia, stroke, epilepsy, Parkinson disease, and brain injury especially visible in citation-ranked views.",
            "Translation depends on connecting biological signatures to outcomes that matter to patients and care systems.",
        ],
        "limitations": [
            "Clinical cohorts often differ in disease stage, comorbidity, treatment history, and follow-up duration.",
            "Biomarkers may not transfer cleanly across populations, scanners, care settings, or diagnostic criteria.",
            "High citation counts can favor broad disease frameworks over smaller mechanistic or interventional studies.",
        ],
    },
    {
        "name": "Brain Development, Plasticity, and Connectomics",
        "slug": "brain-development-plasticity-and-connectomics",
        "patterns": [
            "development",
            "developmental",
            "plasticity",
            "connectome",
            "connectivity",
            "network",
            "child",
            "adolescent",
            "aging",
            "lifespan",
            "critical period",
        ],
        "accent": "#0891b2",
        "secondary": "#22c55e",
        "overview": [
            "This category follows how brain structure, networks, and function change across development, learning, aging, and recovery.",
            "Connectomics has shifted the field from isolated regions toward network-level organization and lifespan trajectories.",
            "Plasticity research links cellular mechanisms, experience, rehabilitation, and large-scale brain reorganization.",
        ],
        "limitations": [
            "Developmental and aging studies are sensitive to cohort composition, attrition, and longitudinal sampling intervals.",
            "Network measures can depend heavily on parcellation, thresholding, and acquisition choices.",
            "Plasticity claims need stronger evidence separating transient compensation from durable functional improvement.",
        ],
    },
    {
        "name": "Brain Stimulation, Neurotechnology, and BCI",
        "slug": "brain-stimulation-neurotechnology-and-bci",
        "patterns": [
            "brain stimulation",
            "deep brain stimulation",
            "tms",
            "tdcs",
            "bci",
            "brain-computer",
            "brain machine",
            "neurotechnology",
            "closed-loop",
            "implant",
            "prosthetic",
            "neuromodulation",
        ],
        "accent": "#16a34a",
        "secondary": "#8b5cf6",
        "overview": [
            "Neurotechnology work uses stimulation, implants, decoding, and closed-loop systems to probe or restore brain function.",
            "The field is moving from proof-of-concept control and stimulation toward durable devices, adaptive therapy, and user-centered deployment.",
            "BCI and neuromodulation papers connect engineering performance with clinical function, safety, and usability.",
        ],
        "limitations": [
            "Small cohorts, invasive risk, device maintenance, and long-term stability remain major translation barriers.",
            "Closed-loop effects are hard to separate from placebo, training, medication, and disease fluctuation.",
            "Performance in controlled sessions may not reflect daily-life reliability or user burden.",
        ],
    },
    {
        "name": "Computational Neuroscience and AI",
        "slug": "computational-neuroscience-and-ai",
        "patterns": [
            "computational",
            "model",
            "neural network",
            "machine learning",
            "deep learning",
            "artificial intelligence",
            "bayesian",
            "reinforcement learning",
            "encoding model",
            "decoding",
            "simulation",
        ],
        "accent": "#9333ea",
        "secondary": "#14b8a6",
        "overview": [
            "Computational brain research formalizes neural coding, inference, learning, dynamics, and decoding with statistical and machine-learning models.",
            "AI methods are increasingly used both as analysis tools and as hypotheses for brain computation.",
            "High-impact work often clarifies which computations could plausibly be implemented by neural circuits.",
        ],
        "limitations": [
            "Predictive performance does not necessarily identify causal neural mechanisms.",
            "Models can inherit dataset bias, preprocessing artifacts, and task constraints.",
            "Interpretability and biological plausibility remain central challenges for large AI-based models.",
        ],
    },
    {
        "name": "Cerebrovascular, Metabolism, and Brain Injury",
        "slug": "cerebrovascular-metabolism-and-brain-injury",
        "patterns": [
            "stroke",
            "ischemia",
            "ischaemia",
            "cerebrovascular",
            "blood brain barrier",
            "metabolism",
            "traumatic brain",
            "brain injury",
            "hypoxia",
            "edema",
            "haemorrhage",
            "hemorrhage",
        ],
        "accent": "#ea580c",
        "secondary": "#0284c7",
        "overview": [
            "This category covers vascular, metabolic, inflammatory, and injury pathways that shape brain damage and recovery.",
            "Highly cited studies often define mechanisms, acute care evidence, or biomarkers for stroke, trauma, and barrier dysfunction.",
            "The area is clinically important because small changes in timing, physiology, and treatment windows can alter outcomes.",
        ],
        "limitations": [
            "Acute injury studies can be sensitive to timing, severity, comorbidity, and treatment heterogeneity.",
            "Animal models may not capture human vascular risk, injury complexity, or rehabilitation context.",
            "Translational failures remain common when mechanistic signals are not tied to functional outcomes.",
        ],
    },
    {
        "name": "General Brain Science and Reviews",
        "slug": "general-brain-science-and-reviews",
        "patterns": [
            "review",
            "meta-analysis",
            "systematic review",
            "brain",
            "neuroscience",
            "atlas",
            "framework",
            "consensus",
        ],
        "accent": "#334155",
        "secondary": "#0f766e",
        "overview": [
            "General brain science papers synthesize methods, concepts, atlases, datasets, and cross-domain frameworks.",
            "Reviews and consensus papers are useful entry points because they connect specialized subfields and standardize terminology.",
            "This category also catches broad brain papers that do not fit cleanly into one methodological or disease-focused area.",
        ],
        "limitations": [
            "Broad reviews can dominate citation-ranked lists while obscuring narrower empirical advances.",
            "Taxonomy boundaries are imperfect because many brain papers combine methods, scales, and diseases.",
            "Metadata-level curation cannot replace full-text expert appraisal of claims and evidence quality.",
        ],
    },
]

CATEGORIES = [
    {
        "name": "Structural Neuroimaging and AI",
        "slug": "neuroimaging-and-brain-mapping",
        "patterns": ["mri", "fmri", "neuroimaging", "brain mapping", "segmentation", "registration", "classification", "deep learning", "machine learning"],
        "accent": "#2563eb",
        "secondary": "#14b8a6",
        "overview": [
            "This category links structural and functional brain imaging to AI-assisted segmentation, prediction, registration, diagnosis, and representation learning.",
            "Highly cited work often becomes reusable infrastructure for brain atlases, image preprocessing, statistical maps, and machine-learning pipelines.",
            "The central relation is practical: AI turns brain structure measurements into scalable features for inference, discovery, and clinical decision support.",
        ],
        "limitations": [
            "Scanner, site, protocol, and preprocessing differences can be learned as shortcuts by AI models.",
            "High predictive accuracy does not guarantee anatomical validity or causal interpretation.",
            "External validation is essential before imaging AI claims transfer across cohorts or clinics.",
        ],
    },
    {
        "name": "Connectomics, Graph Models, and Brain Networks",
        "slug": "brain-development-plasticity-and-connectomics",
        "patterns": ["connectome", "connectivity", "network", "graph", "tractography", "parcellation", "community", "functional connectivity"],
        "accent": "#0891b2",
        "secondary": "#22c55e",
        "overview": [
            "Connectomics organizes brain structure as graphs, making it a natural meeting point between neuroscience and graph-based AI.",
            "Citation-ranked papers emphasize atlases, network measures, functional connectivity, tractography, and graph abstractions for cognition and disease.",
            "The area bridges biological wiring diagrams with machine-learning representations of nodes, edges, communities, and dynamic networks.",
        ],
        "limitations": [
            "Graph results can depend strongly on parcellation, thresholding, acquisition, and preprocessing choices.",
            "Correlation networks are often interpreted more causally than the evidence supports.",
            "Brain graph benchmarks need clearer train/test leakage controls and external validation.",
        ],
    },
    {
        "name": "Brain Decoding, Representation Learning, and BCI",
        "slug": "brain-stimulation-neurotechnology-and-bci",
        "patterns": ["decoding", "encoding", "representation", "brain-computer", "brain computer", "bci", "prosthetic", "closed-loop", "classifier", "neural decoding"],
        "accent": "#16a34a",
        "secondary": "#8b5cf6",
        "overview": [
            "Brain decoding and BCI papers use AI models to map neural activity to perception, movement, language, intention, or control signals.",
            "The field moves from handcrafted signal features toward representation learning, deep decoders, adaptive interfaces, and closed-loop systems.",
            "These papers make the brain-AI relationship bidirectional: AI reads neural structure and dynamics, while neural data constrains AI models.",
        ],
        "limitations": [
            "Small cohorts, session drift, invasive risk, and nonstationary signals limit generalization.",
            "Offline decoding accuracy may not reflect real-time user burden or long-term deployment reliability.",
            "Ethical, privacy, and consent issues intensify when neural signals become actionable model inputs.",
        ],
    },
    {
        "name": "Computational Neuroscience and Brain-Inspired AI",
        "slug": "computational-neuroscience-and-ai",
        "patterns": ["computational", "model", "neural network", "artificial intelligence", "reinforcement learning", "predictive coding", "bayesian", "learning rule", "brain-inspired", "neuromorphic"],
        "accent": "#9333ea",
        "secondary": "#14b8a6",
        "overview": [
            "Computational neuroscience translates brain structure and dynamics into formal models of learning, inference, control, and representation.",
            "Brain-inspired AI uses neural circuits, cortical computation, reinforcement learning, predictive coding, and neuromorphic ideas as design constraints.",
            "Highly cited papers often define concepts that later become shared language for both neuroscience and machine learning.",
        ],
        "limitations": [
            "Model fit does not by itself prove biological mechanism.",
            "Brain-inspired analogies can become too loose unless tied to measurable neural evidence.",
            "Large AI models need stronger interpretability before they can serve as precise brain theories.",
        ],
    },
    {
        "name": "Cellular, Synaptic, and Neuromorphic Foundations",
        "slug": "cellular-molecular-and-synaptic-neuroscience",
        "patterns": ["neuron", "synapse", "synaptic", "plasticity", "spike", "spiking", "cell", "microcircuit", "neuromorphic", "learning rule"],
        "accent": "#7c3aed",
        "secondary": "#f59e0b",
        "overview": [
            "Cellular and synaptic work supplies the biological substrate for neural computation, plasticity, spiking models, and neuromorphic AI.",
            "The category connects local circuit mechanisms to learning rules, memory, adaptation, and efficient hardware-inspired computation.",
            "Historical papers are especially important because many modern AI metaphors inherit vocabulary from neurons, synapses, and plasticity.",
        ],
        "limitations": [
            "Cellular mechanisms rarely scale directly into whole-brain behavior or modern AI architectures.",
            "Animal and ex vivo findings require careful translation to human cognition and deployed systems.",
            "Metadata-level curation can miss whether a paper truly shaped AI rather than only sharing terminology.",
        ],
    },
    {
        "name": "Cognitive Architectures, Learning, and Systems Neuroscience",
        "slug": "cognitive-and-systems-neuroscience",
        "patterns": ["cognition", "memory", "attention", "perception", "decision", "learning", "behavior", "systems neuroscience", "prefrontal", "visual cortex"],
        "accent": "#dc2626",
        "secondary": "#f97316",
        "overview": [
            "Systems neuroscience links brain structure and dynamics to cognitive functions that AI also tries to model: perception, attention, memory, decision making, and learning.",
            "The category captures papers that use computational accounts to connect circuits, behavior, and algorithmic hypotheses.",
            "It is a conceptual bridge between biological intelligence and artificial cognitive architectures.",
        ],
        "limitations": [
            "Task designs can oversimplify cognition and limit ecological validity.",
            "Circuit-behavior correlations need causal perturbation or strong model comparison before mechanistic claims are secure.",
            "AI comparisons can overstate similarity when objectives, embodiment, or data regimes differ.",
        ],
    },
    {
        "name": "Clinical NeuroAI and Brain Disorders",
        "slug": "clinical-neurology-and-neurodegeneration",
        "patterns": ["alzheimer", "parkinson", "dementia", "stroke", "epilepsy", "tumor", "clinical", "patient", "diagnosis", "prognosis", "biomarker"],
        "accent": "#be123c",
        "secondary": "#06b6d4",
        "overview": [
            "Clinical NeuroAI uses structural, functional, molecular, and behavioral brain data to support diagnosis, prognosis, stratification, and treatment planning.",
            "Highly cited work often provides disease cohorts, biomarkers, clinical scales, or modeling frameworks reused by AI studies.",
            "The brain-AI relationship here is translational: models must improve patient-facing interpretation, not only benchmark performance.",
        ],
        "limitations": [
            "Clinical cohorts vary by disease stage, comorbidity, treatment history, and follow-up.",
            "Models can learn site or demographic artifacts instead of disease mechanisms.",
            "Clinical usefulness requires prospective validation, calibration, fairness checks, and workflow integration.",
        ],
    },
    {
        "name": "Electrophysiology, Neural Signals, and AI Decoding",
        "slug": "eeg-meg-and-electrophysiology",
        "patterns": ["eeg", "meg", "ecog", "electrophysiology", "oscillation", "erp", "spike", "spectral", "source localization", "signal processing"],
        "accent": "#0f766e",
        "secondary": "#60a5fa",
        "overview": [
            "Electrophysiology supplies high-temporal-resolution signals for AI decoding, state estimation, seizure detection, and cognitive modeling.",
            "The category includes EEG, MEG, ECoG, spikes, oscillations, and signal-processing work that later feeds machine-learning pipelines.",
            "It highlights how AI can extract structure from noisy neural time series.",
        ],
        "limitations": [
            "Signal artifacts, montage choices, source localization, and session drift can dominate apparent model performance.",
            "Temporal precision does not automatically imply anatomical specificity.",
            "Deployment claims need real-time, out-of-distribution, and user-centered validation.",
        ],
    },
    {
        "name": "General Brain-AI Structure Reviews and Methods",
        "slug": "general-brain-science-and-reviews",
        "patterns": ["review", "meta-analysis", "atlas", "framework", "method", "survey", "brain", "neuroscience", "artificial intelligence"],
        "accent": "#334155",
        "secondary": "#0f766e",
        "overview": [
            "General reviews and methods connect brain structure, neuroscience evidence, and AI concepts across scales and subfields.",
            "These papers often define shared terminology, benchmark assumptions, and methodological standards for later brain-AI work.",
            "The category also catches broad bridge papers that do not fit neatly into one modality or disease domain.",
        ],
        "limitations": [
            "Reviews and methods can dominate citations while obscuring smaller empirical advances.",
            "Bridge terminology can be ambiguous, especially around neural networks, intelligence, and biological plausibility.",
            "Full-text expert review is needed before treating a metadata relation as a substantive brain-AI contribution.",
        ],
    },
]

CATEGORY_BY_NAME = {category["name"]: category for category in CATEGORIES}

KEYWORD_CONVENTION = [
    ("brain-structure", "Cortex, hippocampus, cerebellum, brainstem, structural MRI, diffusion MRI, atlas, parcellation, or anatomical organization.", "2563eb"),
    ("connectome", "Brain connectivity, connectomics, graph structure, tractography, functional networks, or atlas-based network mapping.", "16a34a"),
    ("machine-learning", "Machine learning, classification, prediction, support vector machines, random forests, deep learning, or data-driven modeling.", "475569"),
    ("deep-learning", "Deep neural networks, representation learning, convolutional networks, transformers, graph neural networks, or learned embeddings.", "7c3aed"),
    ("decoding", "Brain decoding, encoding models, neural representation analysis, BCI classifiers, or signal-to-behavior prediction.", "0f766e"),
    ("brain-inspired-ai", "Brain-inspired AI, computational neuroscience, cognitive architectures, predictive coding, reinforcement learning, or neural computation.", "9333ea"),
    ("neuroimaging", "MRI, fMRI, PET, DTI, image registration, segmentation, neuroimaging biomarkers, or imaging-derived model features.", "0891b2"),
    ("neural-signals", "EEG, MEG, ECoG, spikes, oscillations, electrophysiology, and temporal neural signal processing.", "dc2626"),
    ("clinical-neuroai", "Clinical diagnosis, prognosis, brain disorders, disease biomarkers, treatment response, or patient-facing NeuroAI.", "be123c"),
    ("neuromorphic-bci", "Neuromorphic computing, spiking systems, implants, stimulation, closed-loop control, neurotechnology, or BCI.", "ea580c"),
    ("github", "Papers with an official GitHub or code repository link identified in the metadata audit.", "24292f"),
]
KEYWORD_COLORS = {keyword: color for keyword, _, color in KEYWORD_CONVENTION}

KEYWORD_DESCRIPTION_I18N = {
    "brain-structure": {
        "ko": "피질, 해마, 소뇌, 뇌간, 구조 MRI, 확산 MRI, atlas, parcellation 등 뇌 해부학적 구조를 다루는 논문.",
        "zh": "涉及皮层、海马、小脑、脑干、结构 MRI、扩散 MRI、图谱或脑区分区等脑解剖结构的论文。",
        "ja": "皮質、海馬、小脳、脳幹、構造 MRI、拡散 MRI、アトラス、区画化など脳構造を扱う論文。",
    },
    "connectome": {
        "ko": "뇌 연결성, connectome, graph 구조, tractography, 기능적 네트워크를 다루는 논문.",
        "zh": "涉及脑连接组、连接性、图结构、纤维束追踪或功能网络的论文。",
        "ja": "脳コネクトーム、結合性、グラフ構造、トラクトグラフィ、機能ネットワークを扱う論文。",
    },
    "machine-learning": {
        "ko": "머신러닝, 분류, 예측, SVM, 랜덤 포레스트, 데이터 기반 모델링을 사용하는 논문.",
        "zh": "使用机器学习、分类、预测、支持向量机、随机森林或数据驱动建模的论文。",
        "ja": "機械学習、分類、予測、SVM、ランダムフォレスト、データ駆動モデルを用いる論文。",
    },
    "deep-learning": {
        "ko": "딥러닝, 표현학습, CNN, Transformer, GNN, embedding을 사용하는 논문.",
        "zh": "使用深度学习、表示学习、卷积网络、Transformer、图神经网络或嵌入表示的论文。",
        "ja": "深層学習、表現学習、CNN、Transformer、GNN、埋め込み表現を用いる論文。",
    },
    "decoding": {
        "ko": "뇌 decoding, encoding model, neural representation, BCI classifier, 신호-행동 예측을 다루는 논문.",
        "zh": "涉及脑解码、编码模型、神经表征、BCI 分类器或神经信号到行为预测的论文。",
        "ja": "脳デコーディング、符号化モデル、神経表現、BCI 分類器、信号から行動への予測を扱う論文。",
    },
    "brain-inspired-ai": {
        "ko": "brain-inspired AI, 계산신경과학, 인지 아키텍처, predictive coding, 강화학습, 신경계산을 연결하는 논문.",
        "zh": "连接脑启发 AI、计算神经科学、认知架构、预测编码、强化学习或神经计算的论文。",
        "ja": "脳型 AI、計算神経科学、認知アーキテクチャ、予測符号化、強化学習、神経計算を結ぶ論文。",
    },
    "neuroimaging": {
        "ko": "MRI, fMRI, PET, DTI, 영상 registration/segmentation, neuroimaging biomarker를 다루는 논문.",
        "zh": "涉及 MRI、fMRI、PET、DTI、影像配准/分割或神经影像生物标志物的论文。",
        "ja": "MRI、fMRI、PET、DTI、画像レジストレーション/セグメンテーション、神経画像バイオマーカーを扱う論文。",
    },
    "neural-signals": {
        "ko": "EEG, MEG, ECoG, spike, oscillation, electrophysiology, 시간 신경신호 처리를 다루는 논문.",
        "zh": "涉及 EEG、MEG、ECoG、脉冲、振荡、电生理或时间神经信号处理的论文。",
        "ja": "EEG、MEG、ECoG、スパイク、振動、電気生理、時間的神経信号処理を扱う論文。",
    },
    "clinical-neuroai": {
        "ko": "진단, 예후, 뇌질환, biomarker, 치료 반응 등 임상 NeuroAI와 관련된 논문.",
        "zh": "与诊断、预后、脑疾病、生物标志物、治疗反应等临床 NeuroAI 相关的论文。",
        "ja": "診断、予後、脳疾患、バイオマーカー、治療反応など臨床 NeuroAI に関わる論文。",
    },
    "neuromorphic-bci": {
        "ko": "neuromorphic computing, spiking system, implant, stimulation, closed-loop, neurotechnology, BCI를 다루는 논문.",
        "zh": "涉及类脑计算、脉冲系统、植入、刺激、闭环控制、神经技术或 BCI 的论文。",
        "ja": "ニューロモルフィック計算、スパイキングシステム、インプラント、刺激、閉ループ、神経技術、BCI を扱う論文。",
    },
    "github": {
        "ko": "메타데이터 감사에서 공식 GitHub 또는 code repository 링크가 확인된 논문.",
        "zh": "在元数据审计中识别出官方 GitHub 或代码仓库链接的论文。",
        "ja": "メタデータ監査で公式 GitHub またはコードリポジトリが確認された論文。",
    },
}

CATEGORY_TEXT_I18N = {
    "Structural Neuroimaging and AI": {
        "ko": {
            "overview": [
                "구조 및 기능적 뇌영상은 segmentation, prediction, registration, diagnosis를 위한 AI feature space가 됩니다.",
                "이 분류의 고인용 논문은 atlas, preprocessing, statistical map, machine-learning pipeline 같은 재사용 가능한 기반을 제공합니다.",
            ],
            "limitations": [
                "Scanner, site, protocol, preprocessing 차이가 AI 모델의 shortcut으로 학습될 수 있습니다.",
                "높은 예측 성능이 곧 해부학적 타당성이나 인과적 해석을 보장하지는 않습니다.",
            ],
        },
        "zh": {
            "overview": [
                "结构和功能脑影像为 AI 分割、预测、配准和诊断提供可建模的特征空间。",
                "该分类中的高引用论文常成为脑图谱、预处理、统计图和机器学习流程的可复用基础设施。",
            ],
            "limitations": [
                "扫描仪、站点、协议和预处理差异可能被 AI 模型学成捷径。",
                "高预测性能并不等同于解剖学有效性或因果解释。",
            ],
        },
        "ja": {
            "overview": [
                "構造・機能脳画像は、AI によるセグメンテーション、予測、位置合わせ、診断の特徴空間になります。",
                "この分類の高被引用論文は、アトラス、前処理、統計地図、機械学習パイプラインの再利用基盤になります。",
            ],
            "limitations": [
                "スキャナ、施設、プロトコル、前処理の差が AI モデルのショートカットとして学習される可能性があります。",
                "高い予測性能は、解剖学的妥当性や因果解釈を保証しません。",
            ],
        },
    },
    "Connectomics, Graph Models, and Brain Networks": {
        "ko": {
            "overview": ["Connectomics는 뇌 구조를 graph로 표현해 graph AI와 자연스럽게 만나는 축입니다.", "논문들은 node, edge, community, dynamic network 관점으로 뇌 연결성과 AI 표현학습을 연결합니다."],
            "limitations": ["Graph 결과는 parcellation, threshold, acquisition, preprocessing 선택에 민감합니다.", "상관 기반 네트워크를 인과 구조로 과해석하지 않도록 주의해야 합니다."],
        },
        "zh": {
            "overview": ["连接组学把脑结构表示为图，因此自然连接到图 AI。", "这些论文用节点、边、社区和动态网络来连接脑连接性与 AI 表征学习。"],
            "limitations": ["图结果对脑区分区、阈值、采集和预处理选择很敏感。", "相关网络不应被过度解释为因果结构。"],
        },
        "ja": {
            "overview": ["コネクトミクスは脳構造をグラフとして表現し、グラフ AI と自然に接続します。", "ノード、エッジ、コミュニティ、動的ネットワークの観点から脳結合性と AI 表現学習を結びます。"],
            "limitations": ["グラフ結果は区画化、閾値、取得条件、前処理に強く依存します。", "相関ネットワークを因果構造として過度に解釈しない注意が必要です。"],
        },
    },
    "Brain Decoding, Representation Learning, and BCI": {
        "ko": {
            "overview": ["뇌 decoding과 BCI는 neural activity를 지각, 운동, 언어, 의도, 제어 신호로 매핑합니다.", "수작업 feature에서 representation learning, adaptive interface, closed-loop system으로 이동하고 있습니다."],
            "limitations": ["소규모 cohort, session drift, invasive risk, nonstationary signal이 일반화를 제한합니다.", "오프라인 decoding 정확도는 실시간 사용성과 장기 안정성을 보장하지 않습니다."],
        },
        "zh": {
            "overview": ["脑解码和 BCI 将神经活动映射到知觉、运动、语言、意图或控制信号。", "该领域正从手工特征转向表示学习、自适应接口和闭环系统。"],
            "limitations": ["小样本、会话漂移、侵入风险和非平稳信号限制泛化。", "离线解码准确率不能保证实时可用性或长期稳定性。"],
        },
        "ja": {
            "overview": ["脳デコーディングと BCI は神経活動を知覚、運動、言語、意図、制御信号へ写像します。", "手作り特徴から表現学習、適応インターフェース、閉ループシステムへ移行しています。"],
            "limitations": ["小規模コホート、セッションドリフト、侵襲リスク、非定常信号が汎化を制限します。", "オフライン精度はリアルタイム使用性や長期安定性を保証しません。"],
        },
    },
    "Computational Neuroscience and Brain-Inspired AI": {
        "ko": {
            "overview": ["계산신경과학은 학습, 추론, 제어, representation을 형식 모델로 바꿉니다.", "Brain-inspired AI는 neural circuit, predictive coding, reinforcement learning, neuromorphic idea를 설계 제약으로 사용합니다."],
            "limitations": ["모델 적합도가 곧 생물학적 메커니즘의 증거는 아닙니다.", "Brain-inspired 주장은 측정 가능한 신경 증거와 연결되어야 합니다."],
        },
        "zh": {
            "overview": ["计算神经科学把学习、推理、控制和表征转化为形式模型。", "脑启发 AI 将神经回路、预测编码、强化学习和类脑思想作为设计约束。"],
            "limitations": ["模型拟合本身不能证明生物机制。", "脑启发主张需要连接到可测量的神经证据。"],
        },
        "ja": {
            "overview": ["計算神経科学は学習、推論、制御、表現を形式モデルへ変換します。", "脳型 AI は神経回路、予測符号化、強化学習、ニューロモルフィックな考えを設計制約として使います。"],
            "limitations": ["モデル適合だけでは生物学的機構の証拠になりません。", "脳型 AI の主張は測定可能な神経証拠と結びつける必要があります。"],
        },
    },
    "Cellular, Synaptic, and Neuromorphic Foundations": {
        "ko": {"overview": ["세포와 synapse 연구는 neural computation, plasticity, spiking model, neuromorphic AI의 생물학적 기반을 제공합니다."], "limitations": ["세포 수준 메커니즘은 현대 AI architecture나 whole-brain behavior로 직접 확장되기 어렵습니다."]},
        "zh": {"overview": ["细胞和突触研究为神经计算、可塑性、脉冲模型和类脑 AI 提供生物基础。"], "limitations": ["细胞层面的机制不容易直接扩展到现代 AI 架构或全脑行为。"]},
        "ja": {"overview": ["細胞・シナプス研究は神経計算、可塑性、スパイキングモデル、脳型 AI の生物学的基盤を与えます。"], "limitations": ["細胞レベルの機構は現代 AI アーキテクチャや全脳行動へ直接拡張しにくいです。"]},
    },
    "Cognitive Architectures, Learning, and Systems Neuroscience": {
        "ko": {"overview": ["시스템 신경과학은 지각, 주의, 기억, 의사결정, 학습처럼 AI도 모델링하려는 기능을 뇌 회로와 연결합니다."], "limitations": ["과제 설계가 cognition을 단순화하면 실제 행동으로의 일반화가 제한됩니다."]},
        "zh": {"overview": ["系统神经科学把知觉、注意、记忆、决策和学习等 AI 也试图建模的功能连接到脑回路。"], "limitations": ["任务设计若过度简化认知，会限制对真实行为的泛化。"]},
        "ja": {"overview": ["システム神経科学は知覚、注意、記憶、意思決定、学習など AI もモデル化する機能を脳回路と結びます。"], "limitations": ["課題設計が認知を単純化しすぎると、実世界行動への汎化が制限されます。"]},
    },
    "Clinical NeuroAI and Brain Disorders": {
        "ko": {"overview": ["Clinical NeuroAI는 뇌 데이터로 진단, 예후, 환자 stratification, 치료 계획을 지원합니다."], "limitations": ["임상 모델은 prospective validation, calibration, fairness check, workflow integration이 필요합니다."]},
        "zh": {"overview": ["临床 NeuroAI 使用脑数据支持诊断、预后、患者分层和治疗规划。"], "limitations": ["临床模型需要前瞻性验证、校准、公平性检查和工作流整合。"]},
        "ja": {"overview": ["臨床 NeuroAI は脳データで診断、予後、患者層別化、治療計画を支援します。"], "limitations": ["臨床モデルには前向き検証、較正、公平性確認、ワークフロー統合が必要です。"]},
    },
    "Electrophysiology, Neural Signals, and AI Decoding": {
        "ko": {"overview": ["Electrophysiology는 AI decoding, 상태 추정, seizure detection, cognitive modeling을 위한 고시간해상도 신호를 제공합니다."], "limitations": ["Artifact, montage, source localization, session drift가 model performance를 좌우할 수 있습니다."]},
        "zh": {"overview": ["电生理为 AI 解码、状态估计、癫痫检测和认知建模提供高时间分辨率信号。"], "limitations": ["伪迹、导联、源定位和会话漂移可能主导模型表现。"]},
        "ja": {"overview": ["電気生理は AI デコーディング、状態推定、発作検出、認知モデリングに高時間分解能信号を提供します。"], "limitations": ["アーティファクト、モンタージュ、信号源推定、セッションドリフトが性能を左右します。"]},
    },
    "General Brain-AI Structure Reviews and Methods": {
        "ko": {"overview": ["리뷰와 방법론 논문은 뇌 구조, 신경과학 증거, AI 개념을 여러 scale에서 연결합니다."], "limitations": ["Bridge 용어는 neural network, intelligence, biological plausibility 주변에서 모호할 수 있습니다."]},
        "zh": {"overview": ["综述和方法论文在多个尺度上连接脑结构、神经科学证据和 AI 概念。"], "limitations": ["围绕神经网络、智能和生物合理性的桥接术语可能存在歧义。"]},
        "ja": {"overview": ["レビューと方法論論文は、脳構造、神経科学的証拠、AI 概念を複数スケールで結びます。"], "limitations": ["神経ネットワーク、知能、生物学的妥当性に関する橋渡し用語は曖昧になり得ます。"]},
    },
}

RECOGNIZED_VENUES = [
    "Nature",
    "Science",
    "Cell",
    "Neuron",
    "The Lancet",
    "Nature Neuroscience",
    "Nature Reviews Neuroscience",
    "Nature Reviews Neurology",
    "PNAS",
    "Proceedings of the National Academy of Sciences",
    "Brain",
    "Cerebral Cortex",
    "NeuroImage",
    "Journal of Neuroscience",
    "Annals of Neurology",
    "Neurology",
    "eLife",
]

CSV_FIELDS = [
    "rank",
    "year",
    "title",
    "authors",
    "venue",
    "publicationDate",
    "citationCount",
    "influentialCitationCount",
    "importanceScore",
    "category",
    "keywordTags",
    "keyIdea",
    "strengths",
    "limitations",
    "doi",
    "sourceId",
    "url",
    "semanticScholarUrl",
    "openAccessPdf",
    "githubUrl",
    "workType",
    "language",
    "relevanceReason",
]

CANDIDATE_FIELDS = [
    "year",
    "title",
    "authors",
    "venue",
    "publicationDate",
    "citationCount",
    "category",
    "keywordTags",
    "doi",
    "sourceId",
    "url",
    "workType",
    "language",
    "relevanceScore",
    "relevanceReason",
    "abstractSnippet",
]


def ensure_dirs():
    for path in [DATA_DIR, DOCS_DIR, PAPER_DIR, CACHE_DIR, DOCS_DIR / "data", DOCS_DIR / "assets", DOCS_DIR / "assets" / "taxonomy", DOCS_DIR / "paper"]:
        path.mkdir(parents=True, exist_ok=True)


def clean_text(value):
    if value is None:
        return ""
    text = str(value)
    text = text.replace("\u2010", "-").replace("\u2011", "-").replace("\u2012", "-").replace("\u2013", "-").replace("\u2014", "-")
    text = text.replace("\u2018", "'").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"\s+", " ", text).strip()


def title_key(value):
    text = clean_text(value).lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def clean_github_url(value):
    text = clean_text(value)
    match = re.search(r"https?://github\.com/[^\s<>\"')]+", text, flags=re.I)
    if not match:
        return ""
    path = match.group(0).split("github.com/", 1)[1].rstrip(".,;")
    return f"https://github.com/{path}"


def semantic_scholar_url(row):
    paper_id = clean_text(row.get("paperId") or row.get("sourceId"))
    if re.fullmatch(r"[0-9a-f]{40}", paper_id, flags=re.I):
        return f"https://www.semanticscholar.org/paper/{paper_id}"
    return clean_text(row.get("semanticScholarUrl"))


def is_official_github_entry(value):
    return isinstance(value, dict) and bool(value.get("githubOfficial")) and bool(value.get("mentionedInPaper"))


def official_github_url_from_paper_text(row):
    official_context = re.compile(
        r"\b(code|codes|source|implementation|repo|repository|software|toolbox|package|model|models|weights|data|dataset|project|available|released|open-source|publicly)\b",
        flags=re.I,
    )
    for field in ("abstract", "abstractSnippet"):
        text = clean_text(row.get(field))
        for match in re.finditer(r"https?://github\.com/[^\s<>\"')]+", text, flags=re.I):
            window = text[max(0, match.start() - 160): match.end() + 80]
            if official_context.search(window):
                return clean_github_url(match.group(0))
    return ""


def load_github_links():
    path = DATA_DIR / GITHUB_LINKS_JSON
    if not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    links = {}
    for key, value in payload.get("links", {}).items():
        if not is_official_github_entry(value):
            continue
        github_url = clean_github_url(value.get("githubUrl") if isinstance(value, dict) else value)
        if github_url:
            links[key] = {**value, "githubUrl": github_url} if isinstance(value, dict) else {"githubUrl": github_url}
    return links


def sync_github_keyword_tag(row):
    raw = str(row.get("keywordTags") or "")
    separator = "; " if "; " in raw else ";"
    tags = [tag.strip() for tag in raw.split(";") if tag.strip() and tag.strip() != "github"]
    if row.get("githubUrl"):
        tags.append("github")
    row["keywordTags"] = separator.join(tags)


def apply_github_links(rows):
    links = load_github_links()
    for row in rows:
        match = links.get(title_key(row.get("title")))
        if match and is_official_github_entry(match):
            row["githubUrl"] = clean_github_url(match.get("githubUrl", ""))
        else:
            row["githubUrl"] = ""
        sync_github_keyword_tag(row)
    return rows


def strip_doi(doi):
    doi = clean_text(doi)
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi, flags=re.I)
    return doi


def slugify(text):
    text = clean_text(text).lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "item"


def abstract_from_inverted_index(index):
    if not index:
        return ""
    positions = []
    for word, offsets in index.items():
        for offset in offsets:
            positions.append((offset, word))
    positions.sort()
    return clean_text(" ".join(word for _, word in positions))


def first_sentence(text):
    text = clean_text(text)
    if not text:
        return ""
    match = re.search(r"(.{40,420}?[.!?])\s", text + " ")
    if match:
        return match.group(1).strip()
    return text[:360].strip()


def authors_from_work(work, limit=6):
    authors = []
    for authorship in work.get("authorships") or []:
        author = authorship.get("author") or {}
        name = clean_text(author.get("display_name") or authorship.get("raw_author_name"))
        if name:
            authors.append(name)
    if not authors:
        return "Unknown authors"
    if len(authors) > limit:
        return ", ".join(authors[:limit]) + ", et al."
    return ", ".join(authors)


def venue_from_work(work):
    primary = work.get("primary_location") or {}
    source = primary.get("source") or {}
    venue = clean_text(source.get("display_name") or primary.get("raw_source_name"))
    return venue or "Unknown venue"


def link_from_work(work):
    doi = strip_doi(work.get("doi"))
    if doi:
        return f"https://doi.org/{doi}"
    primary = work.get("primary_location") or {}
    if primary.get("landing_page_url"):
        return clean_text(primary["landing_page_url"])
    ids = work.get("ids") or {}
    for key in ["pmid", "pmcid"]:
        if ids.get(key):
            return clean_text(ids[key])
    return clean_text(work.get("id"))


def pdf_from_work(work):
    best = work.get("best_oa_location") or {}
    primary = work.get("primary_location") or {}
    open_access = work.get("open_access") or {}
    return clean_text(best.get("pdf_url") or primary.get("pdf_url") or open_access.get("oa_url"))


def concept_terms(work):
    terms = []
    for concept in work.get("concepts") or []:
        name = clean_text(concept.get("display_name"))
        score = concept.get("score") or 0
        if name:
            terms.append((name, score))
    for keyword in work.get("keywords") or []:
        name = clean_text(keyword.get("display_name"))
        score = keyword.get("score") or 0
        if name:
            terms.append((name, score))
    return terms


def relevant_text(work, abstract=""):
    title = clean_text(work.get("title") or work.get("display_name"))
    concepts = " ".join(name for name, score in concept_terms(work) if score >= 0.12)
    return f"{title} {abstract} {concepts}".lower()


def relevance_score(work, abstract):
    text = relevant_text(work, abstract)
    score = 0
    reasons = []
    for term in RELEVANCE_TERMS:
        if term in text:
            score += 1
            if len(reasons) < 8:
                reasons.append(term)
    for concept, concept_score in concept_terms(work):
        if concept.lower() == "neuroscience" and concept_score >= 0.2:
            score += 3
            reasons.append("neuroscience concept")
        elif concept_score >= 0.35 and any(term in concept.lower() for term in ["brain", "neuro", "cortex", "neuron", "synapse", "connect"]):
            score += 2
            reasons.append(concept)
    if "brain" in clean_text(work.get("title") or "").lower():
        score += 3
        reasons.append("brain in title")
    return score, "; ".join(dict.fromkeys(reasons)) or "brain-structure and AI query"


def assign_category(text):
    text = text.lower()
    best_name = "General Brain-AI Structure Reviews and Methods"
    best_score = 0
    for category in CATEGORIES:
        score = sum(1 for pattern in category["patterns"] if pattern in text)
        if category["name"] == "General Brain-AI Structure Reviews and Methods":
            score -= 1
        if score > best_score:
            best_name = category["name"]
            best_score = score
    return best_name


def assign_keywords(text):
    lower = text.lower()
    tags = []
    checks = {
        "brain-structure": ["brain", "cortex", "cortical", "cerebral", "hippocampus", "cerebellum", "brainstem", "structural mri", "diffusion tensor", "parcellation", "atlas"],
        "connectome": ["connectome", "connectivity", "network", "tractography", "graph", "functional connectivity", "structural connectivity"],
        "machine-learning": ["machine learning", "classification", "prediction", "predictive", "support vector", "random forest", "classifier", "regression", "data mining"],
        "deep-learning": ["deep learning", "neural network", "convolutional", "transformer", "graph neural", "representation learning", "embedding"],
        "decoding": ["decoding", "encoding model", "brain decoding", "neural decoding", "representation", "brain-computer", "brain computer", "bci"],
        "brain-inspired-ai": ["brain-inspired", "brain inspired", "computational neuroscience", "predictive coding", "reinforcement learning", "cognitive architecture", "neural computation"],
        "neuroimaging": [" mri", "fmri", "magnetic resonance", "neuroimaging", "pet", "diffusion tensor", "segmentation", "registration"],
        "neural-signals": ["eeg", "meg", "ecog", "electroencephal", "magnetoencephal", "electrophysiology", "oscillation", "spike"],
        "clinical-neuroai": ["clinical", "patient", "diagnosis", "prognosis", "biomarker", "alzheimer", "parkinson", "stroke", "epilepsy", "dementia"],
        "neuromorphic-bci": ["neuromorphic", "spiking", "brain-computer", "brain computer", "bci", "deep brain stimulation", "dbs", "tms", "tdcs", "closed-loop", "implant"],
    }
    padded = " " + lower
    for keyword, needles in checks.items():
        if any(needle in padded for needle in needles):
            tags.append(keyword)
    return tags


def recognized_venue(venue):
    venue_lower = venue.lower()
    return any(candidate.lower() in venue_lower for candidate in RECOGNIZED_VENUES)


def work_type_label(work_type):
    return clean_text(work_type).replace("-", " ") or "work"


def importance_score(row):
    score = math.log1p(row["citationCount"]) * 18
    score += min(row.get("relevanceScore", 0), 20) * 2
    if recognized_venue(row["venue"]):
        score += 12
    if row["workType"] in {"review", "meta-analysis"} or "review" in row["title"].lower():
        score += 8
    if row.get("openAccessPdf"):
        score += 3
    if row["keywordTags"]:
        score += len(row["keywordTags"].split(";")) * 1.2
    return round(score, 2)


def strengths_for(row):
    strengths = [f"high citation signal ({row['citationCount']:,})"]
    tags = {tag for tag in row["keywordTags"].split(";") if tag}
    if recognized_venue(row["venue"]):
        strengths.append("recognized venue")
    if row.get("openAccessPdf"):
        strengths.append("open-access PDF metadata")
    if "review" in row["workType"] or "review" in row["title"].lower():
        strengths.append("synthesis or review value")
    if "machine-learning" in tags or "deep-learning" in tags:
        strengths.append("explicit AI/modeling signal")
    if "brain-structure" in tags or "connectome" in tags:
        strengths.append("brain-structure signal")
    if "decoding" in tags or "neuromorphic-bci" in tags:
        strengths.append("brain-to-model interface signal")
    if not strengths:
        strengths.append("selected by citation count from the audited brain-AI candidate pool")
    return "; ".join(dict.fromkeys(strengths[:4]))


def limitations_for(row):
    category = CATEGORY_BY_NAME[row["category"]]
    limitations = list(category["limitations"][:2])
    tags = set(row["keywordTags"].split(";")) if row["keywordTags"] else set()
    if "machine-learning" in tags or "deep-learning" in tags:
        limitations.append("Model performance should be checked for leakage, confounding, calibration, and external validity.")
    elif "neuroimaging" in tags or "brain-structure" in tags:
        limitations.append("Imaging conclusions can depend on acquisition, preprocessing, and model specification.")
    elif "decoding" in tags or "neural-signals" in tags:
        limitations.append("Signal drift, artifacts, and session effects can limit real-world decoding reliability.")
    else:
        limitations.append("Metadata-level ranking should be complemented with full-text expert review before strong claims are made.")
    return "; ".join(dict.fromkeys(limitations[:3]))


def localized_category_sentence(row, lang):
    category = CATEGORY_BY_NAME.get(row["category"], {})
    localized_block = CATEGORY_TEXT_I18N.get(row["category"], {}).get(lang) or {}
    overview = localized_block.get("overview") or category.get("overview") or []
    return overview[0] if overview else row["category"]


def localized_strengths_for(row, lang):
    if lang == "en":
        return row["strengths"]
    tags = {tag for tag in row["keywordTags"].split(";") if tag}
    citation = row["citationCount"]
    parts_by_lang = {
        "ko": [f"인용 신호가 높음({citation:,}회)"],
        "zh": [f"引用信号高（{citation:,} 次）"],
        "ja": [f"引用シグナルが高い（{citation:,}件）"],
    }
    parts = parts_by_lang.get(lang, parts_by_lang["ko"])
    if recognized_venue(row["venue"]):
        parts.append({"ko": "인정받는 학술지/학회", "zh": "发表渠道具有认可度", "ja": "認知度の高い掲載先"}[lang])
    if row.get("openAccessPdf"):
        parts.append({"ko": "공개 PDF 메타데이터 있음", "zh": "包含开放 PDF 元数据", "ja": "公開 PDF メタデータあり"}[lang])
    if "review" in row["workType"] or "review" in row["title"].lower():
        parts.append({"ko": "종합/리뷰 가치", "zh": "具有综述或综合价值", "ja": "レビュー/総合整理として有用"}[lang])
    if "machine-learning" in tags or "deep-learning" in tags:
        parts.append({"ko": "명시적 AI/모델링 신호", "zh": "具有明确的 AI/建模信号", "ja": "明示的な AI/モデリング信号"}[lang])
    if "brain-structure" in tags or "connectome" in tags:
        parts.append({"ko": "뇌 구조 신호", "zh": "包含脑结构信号", "ja": "脳構造シグナル"}[lang])
    if "decoding" in tags or "neuromorphic-bci" in tags:
        parts.append({"ko": "뇌-모델 인터페이스 신호", "zh": "体现脑到模型的接口信号", "ja": "脳とモデルをつなぐ信号"}[lang])
    return "; ".join(dict.fromkeys(parts[:4]))


def localized_limitations_for(row, lang):
    if lang == "en":
        return row["limitations"]
    category = CATEGORY_BY_NAME[row["category"]]
    localized_block = CATEGORY_TEXT_I18N.get(row["category"], {}).get(lang) or {}
    limitations = list((localized_block.get("limitations") or category["limitations"])[:2])
    tags = set(row["keywordTags"].split(";")) if row["keywordTags"] else set()
    extras = {
        "machine": {
            "ko": "모델 성능은 leakage, confounding, calibration, 외부 타당성까지 점검해야 합니다.",
            "zh": "模型表现仍需检查数据泄漏、混杂、校准和外部有效性。",
            "ja": "モデル性能はリーケージ、交絡、較正、外部妥当性まで確認が必要です。",
        },
        "imaging": {
            "ko": "영상 결론은 acquisition, preprocessing, model specification에 따라 달라질 수 있습니다.",
            "zh": "影像结论可能受采集、预处理和模型设定影响。",
            "ja": "画像解析の結論は取得条件、前処理、モデル仕様に左右されます。",
        },
        "signals": {
            "ko": "신호 drift, artifact, session effect가 실제 decoding 신뢰도를 제한할 수 있습니다.",
            "zh": "信号漂移、伪迹和会话效应会限制真实解码可靠性。",
            "ja": "信号ドリフト、アーティファクト、セッション効果が実運用での信頼性を制限します。",
        },
        "metadata": {
            "ko": "메타데이터 순위는 강한 주장 전에 전문 PDF 검토로 보완해야 합니다.",
            "zh": "元数据排序在形成强主张前应由全文 PDF 审阅补充。",
            "ja": "メタデータ順位は強い主張の前に全文 PDF レビューで補完する必要があります。",
        },
    }
    if "machine-learning" in tags or "deep-learning" in tags:
        limitations.append(extras["machine"][lang])
    elif "neuroimaging" in tags or "brain-structure" in tags:
        limitations.append(extras["imaging"][lang])
    elif "decoding" in tags or "neural-signals" in tags:
        limitations.append(extras["signals"][lang])
    else:
        limitations.append(extras["metadata"][lang])
    return "; ".join(dict.fromkeys(limitations[:3]))


def localized_paper_text(row):
    texts = {
        "en": {
            "keyIdea": row["keyIdea"],
            "strengths": row["strengths"],
            "limitations": row["limitations"],
        }
    }
    title = row["title"]
    year = row["year"]
    category = row["category"]
    templates = {
        "ko": "'{title}'는 {year}년에 발표된 {category} 분야의 인용 상위 논문입니다. {category_sentence}",
        "zh": "《{title}》是 {year} 年发表的 {category} 方向高引用论文。{category_sentence}",
        "ja": "「{title}」は {year} 年に発表された {category} 分野の高引用論文です。{category_sentence}",
    }
    for lang, template in templates.items():
        texts[lang] = {
            "keyIdea": template.format(
                title=title,
                year=year,
                category=category,
                category_sentence=localized_category_sentence(row, lang),
            ),
            "strengths": localized_strengths_for(row, lang),
            "limitations": localized_limitations_for(row, lang),
        }
    return texts


def normalize_work(work):
    abstract = abstract_from_inverted_index(work.get("abstract_inverted_index"))
    score, reason = relevance_score(work, abstract)
    title = clean_text(work.get("title") or work.get("display_name"))
    venue = venue_from_work(work)
    concept_text_value = " ".join(name for name, _ in concept_terms(work))
    aggregate_text = f"{title} {abstract} {venue} {concept_text_value}"
    category = assign_category(aggregate_text)
    tags = assign_keywords(aggregate_text)
    doi = strip_doi(work.get("doi"))
    row = {
        "rank": "",
        "year": int(work.get("publication_year") or 0),
        "title": title,
        "authors": authors_from_work(work),
        "venue": venue,
        "publicationDate": clean_text(work.get("publication_date")) or str(work.get("publication_year") or ""),
        "citationCount": int(work.get("cited_by_count") or 0),
        "influentialCitationCount": 0,
        "category": category,
        "keywordTags": ";".join(tags),
        "doi": doi,
        "sourceId": clean_text(work.get("id")),
        "url": link_from_work(work),
        "openAccessPdf": pdf_from_work(work),
        "workType": work_type_label(work.get("type")),
        "language": clean_text(work.get("language")) or "unknown",
        "relevanceScore": score,
        "relevanceReason": reason,
        "abstract": abstract,
        "abstractSnippet": first_sentence(abstract) or "",
    }
    row["keyIdea"] = first_sentence(abstract) or f"Positions {title} within {category}."
    row["strengths"] = strengths_for(row)
    row["limitations"] = limitations_for(row)
    row["importanceScore"] = importance_score(row)
    return row


def cache_path_for_year(year):
    return CACHE_DIR / f"s2_brain_candidates_{year}.json"


def s2_paper_key(paper):
    ext = paper.get("externalIds") or {}
    for key in ["DOI", "ArXiv", "PubMed", "CorpusId"]:
        if ext.get(key):
            return f"{key}:{ext[key]}".lower()
    return (paper.get("paperId") or paper.get("url") or paper.get("title") or "").lower()


def s2_authors(paper, limit=6):
    names = [clean_text(author.get("name")) for author in paper.get("authors") or [] if author.get("name")]
    if not names:
        return "Unknown authors"
    if len(names) > limit:
        return ", ".join(names[:limit]) + ", et al."
    return ", ".join(names)


def s2_venue(paper):
    venue = clean_text(paper.get("venue"))
    publication_venue = paper.get("publicationVenue") or {}
    return venue or clean_text(publication_venue.get("name")) or "Unknown venue"


def s2_fields_text(paper):
    fields = paper.get("s2FieldsOfStudy") or []
    categories = [clean_text(field.get("category")) for field in fields if field.get("category")]
    types = [clean_text(item) for item in paper.get("publicationTypes") or []]
    return " ".join(categories + types)


def s2_relevance_score(paper):
    title = clean_text(paper.get("title"))
    abstract = clean_text(paper.get("abstract"))
    text = f"{title} {abstract} {s2_fields_text(paper)}".lower()
    if ("brain natriuretic peptide" in text or "nt-probnp" in text or "b-type natriuretic" in text) and not any(
        term in text for term in ["neuron", "cortex", "cerebral", "neuro", "mri", "fmri", "eeg", "stroke", "dementia"]
    ):
        return 0, "excluded natriuretic-peptide usage"
    score = 0
    reasons = []
    structure_hits = []
    ai_hits = []
    for term in STRUCTURE_TERMS:
        if term in text:
            structure_hits.append(term)
    for term in AI_RELATION_TERMS:
        if term in text:
            ai_hits.append(term)
    if structure_hits:
        score += min(len(structure_hits), 8)
        reasons.extend(structure_hits[:6])
    if ai_hits:
        score += 4 * min(len(ai_hits), 5)
        reasons.extend(ai_hits[:6])
    if "brain" in title.lower() or "cortex" in title.lower() or "neural" in title.lower():
        score += 3
        reasons.append("brain/neural structure in title")
    if structure_hits and ai_hits:
        score += 8
        reasons.append("explicit brain-structure/AI bridge")
    elif structure_hits and any(term in text for term in ["model", "learning", "intelligence", "computation", "algorithm"]):
        score += 4
        reasons.append("historical computation/learning bridge")
    if not structure_hits and not ai_hits and "Medicine" in s2_fields_text(paper):
        return 0, "weak brain-AI relevance"
    return score, "; ".join(dict.fromkeys(reasons)) or "Semantic Scholar brain-AI query"


def normalize_s2_paper(paper):
    abstract = clean_text(paper.get("abstract"))
    score, reason = s2_relevance_score(paper)
    title = clean_text(paper.get("title"))
    venue = s2_venue(paper)
    aggregate_text = f"{title} {abstract} {venue} {s2_fields_text(paper)}"
    category = assign_category(aggregate_text)
    tags = assign_keywords(aggregate_text)
    ext = paper.get("externalIds") or {}
    oa = paper.get("openAccessPdf") or {}
    doi = strip_doi(ext.get("DOI", ""))
    url = f"https://doi.org/{doi}" if doi else clean_text(paper.get("url"))
    row = {
        "rank": "",
        "year": int(paper.get("year") or 0),
        "title": title,
        "authors": s2_authors(paper),
        "venue": venue,
        "publicationDate": clean_text(paper.get("publicationDate")) or str(paper.get("year") or ""),
        "citationCount": int(paper.get("citationCount") or 0),
        "influentialCitationCount": int(paper.get("influentialCitationCount") or 0),
        "category": category,
        "keywordTags": ";".join(tags),
        "doi": doi,
        "sourceId": clean_text(paper.get("paperId")),
        "url": url,
        "semanticScholarUrl": semantic_scholar_url({"sourceId": paper.get("paperId", "")}),
        "openAccessPdf": clean_text(oa.get("url")) if isinstance(oa, dict) else "",
        "workType": "; ".join(clean_text(item) for item in paper.get("publicationTypes") or []) or "paper",
        "language": "unknown",
        "relevanceScore": score,
        "relevanceReason": reason,
        "abstract": abstract,
        "abstractSnippet": first_sentence(abstract) or "",
    }
    row["keyIdea"] = first_sentence(abstract) or f"Positions {title} within {category}."
    row["strengths"] = strengths_for(row)
    row["limitations"] = limitations_for(row)
    row["importanceScore"] = importance_score(row)
    return row


def refresh_row_enrichment(row):
    row = dict(row)
    row["year"] = int(row.get("year") or 0)
    row["citationCount"] = int(row.get("citationCount") or 0)
    row["influentialCitationCount"] = int(row.get("influentialCitationCount") or 0)
    aggregate_text = " ".join(
        clean_text(row.get(field))
        for field in ["title", "abstract", "abstractSnippet", "venue", "workType", "relevanceReason"]
    )
    pseudo_paper = {
        "title": row.get("title", ""),
        "abstract": row.get("abstract") or row.get("abstractSnippet") or "",
        "s2FieldsOfStudy": [{"category": value} for value in str(row.get("category", "")).split(";") if value],
        "publicationTypes": [row.get("workType", "")],
    }
    score, reason = s2_relevance_score(pseudo_paper)
    row["relevanceScore"] = score
    row["relevanceReason"] = reason
    row["category"] = assign_category(aggregate_text)
    row["keywordTags"] = ";".join(assign_keywords(aggregate_text))
    row["importanceScore"] = importance_score(row)
    row["strengths"] = strengths_for(row)
    row["limitations"] = limitations_for(row)
    if not row.get("keyIdea"):
        row["keyIdea"] = f"Positions {row.get('title', 'this paper')} within {row.get('category', 'brain-AI relation research')}."
    return row


def fetch_s2_year_query(session, year, query, max_pages=S2_MAX_PAGES_PER_QUERY):
    params = {
        "query": query,
        "year": str(year),
        "fields": S2_FIELDS,
        "sort": "citationCount:desc",
    }
    papers = []
    token = None
    for _ in range(max_pages):
        if token:
            params["token"] = token
        for attempt in range(1, 6):
            response = session.get(S2_BULK_URL, params=params, timeout=90)
            if response.status_code == 429:
                wait = 12 * attempt
                print(f"[s2] 429 for {year} {query}; retrying in {wait}s", flush=True)
                time.sleep(wait)
                continue
            if response.status_code in {500, 502, 503, 504}:
                wait = min(45, 2 ** attempt)
                print(f"[s2] {response.status_code} for {year} {query}; retrying in {wait}s", flush=True)
                time.sleep(wait)
                continue
            response.raise_for_status()
            data = response.json()
            papers.extend(data.get("data") or [])
            token = data.get("token")
            break
        else:
            break
        if not token:
            break
        time.sleep(1.0)
    return papers


def collect_year(session, year, refresh=False):
    cache_path = cache_path_for_year(year)
    if cache_path.exists() and not refresh:
        rows = [refresh_row_enrichment(row) for row in json.loads(cache_path.read_text(encoding="utf-8"))]
        rows = sorted(rows, key=lambda item: (-item["citationCount"], -item["relevanceScore"], item["title"].lower()))
        cache_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
        return rows
    merged = {}
    for query in S2_QUERIES:
        print(f"[collect] {year} :: {query}", flush=True)
        try:
            for paper in fetch_s2_year_query(session, year, query):
                if paper.get("year") != year or not paper.get("title"):
                    continue
                row = normalize_s2_paper(paper)
                if row["relevanceScore"] <= 0:
                    continue
                merged[s2_paper_key(paper)] = row
        except Exception as exc:
            print(f"[warn] {year} {query}: {exc}", flush=True)
        if len(merged) >= CANDIDATES_PER_YEAR:
            break
        time.sleep(1.0)
    rows = sorted(merged.values(), key=lambda item: (-item["citationCount"], -item["relevanceScore"], item["title"].lower()))
    rows = rows[:CANDIDATES_PER_YEAR]
    cache_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    return rows


def collect_papers(refresh=False):
    session = requests.Session()
    session.headers.update({"User-Agent": "awesome-brain-ai-curation/1.0"})
    all_candidates = []
    selected = []
    for year in YEARS:
        rows = collect_year(session, year, refresh=refresh)
        for row in rows:
            all_candidates.append(row)
        eligible = [row for row in rows if row.get("relevanceScore", 0) >= 6]
        if len(eligible) < TARGET_PER_YEAR:
            seen = {row["title"].lower() for row in eligible}
            eligible.extend(row for row in rows if row["title"].lower() not in seen)
        year_selected = sorted(eligible, key=lambda item: (-item["citationCount"], -item["relevanceScore"], item["title"].lower()))[:TARGET_PER_YEAR]
        for rank, row in enumerate(year_selected, start=1):
            row = dict(row)
            row["rank"] = rank
            selected.append(row)
        print(f"[year {year}] candidates={len(rows)} selected={len(year_selected)}", flush=True)
    selected.sort(key=lambda item: (item["year"], item["rank"]))
    all_candidates.sort(key=lambda item: (item["year"], -item["citationCount"], item["title"].lower()))
    return selected, all_candidates


def selected_csv_row(row):
    return {field: row.get(field, "") for field in CSV_FIELDS}


def candidate_csv_row(row):
    return {field: row.get(field, "") for field in CANDIDATE_FIELDS}


def write_csv(path, rows, fields):
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def write_json_csv(selected, candidates):
    DATA_DIR.mkdir(exist_ok=True)
    apply_github_links(selected)
    selected_export = [selected_csv_row(row) | {"abstract": row.get("abstract", "")} for row in selected]
    candidate_export = [candidate_csv_row(row) for row in candidates]
    (DATA_DIR / PAPERS_JSON).write_text(json.dumps(selected_export, ensure_ascii=False, indent=2), encoding="utf-8")
    (DATA_DIR / CANDIDATES_JSON).write_text(json.dumps(candidate_export, ensure_ascii=False, indent=2), encoding="utf-8")
    write_csv(DATA_DIR / PAPERS_CSV, selected_export, CSV_FIELDS + ["abstract"])
    write_csv(DATA_DIR / CANDIDATES_CSV, candidate_export, CANDIDATE_FIELDS)
    for year in YEARS:
        year_selected = [selected_csv_row(row) | {"abstract": row.get("abstract", "")} for row in selected if row["year"] == year]
        year_candidates = [candidate_csv_row(row) for row in candidates if row["year"] == year]
        write_csv(DATA_DIR / f"papers_{year}.csv", year_selected, CSV_FIELDS + ["abstract"])
        write_csv(DATA_DIR / f"candidates_top{CANDIDATES_PER_YEAR}_{year}.csv", year_candidates, CANDIDATE_FIELDS)


def write_taxonomy_dataset(selected):
    fields = [
        "rank",
        "year",
        "category",
        "keywordTags",
        "title",
        "authors",
        "venue",
        "citationCount",
        "importanceScore",
        "keyIdea",
        "strengths",
        "limitations",
        "url",
        "doi",
        "sourceId",
    ]
    write_csv(DATA_DIR / TAXONOMY_CSV, selected, fields)


def year_stats(rows):
    stats = {}
    for year in YEARS:
        subset = [row for row in rows if row["year"] == year]
        if not subset:
            continue
        top = max(subset, key=lambda item: item["citationCount"])
        stats[year] = {
            "count": len(subset),
            "citations": sum(row["citationCount"] for row in subset),
            "top": {"title": top["title"], "url": top["url"], "citations": top["citationCount"]},
        }
    return stats


def category_stats(rows):
    counts = Counter(row["category"] for row in rows)
    citations = defaultdict(int)
    for row in rows:
        citations[row["category"]] += row["citationCount"]
    return counts, citations


def keyword_stats(rows):
    counts = Counter()
    for row in rows:
        for tag in row["keywordTags"].split(";"):
            if tag:
                counts[tag] += 1
    return counts


def research_overview_html():
    return """
    <section class="research-brief" id="researchBrief" aria-labelledby="research-timeline-title">
      <h2 id="research-timeline-title">Research Timeline</h2>
      <div class="timeline-copy">
        <p>1900-2026??brain ?곌뎄 肄뷀띁?ㅻ뒗 ?대??? 蹂묐━?? ?앸━??以묒떖??珥덇린 ?뚭낵?숈뿉??異쒕컻???꾩긽 ?좉꼍?? ?명룷쨌遺꾩옄 ?좉꼍怨쇳븰, ?좉꼍?곸긽, ?꾧린?앸━, connectomics, 怨꾩궛?좉꼍怨쇳븰怨?neurotechnology濡??뺤옣???κ린 吏?뺣룄?? ?몄슜 湲곕컲?쇰줈 ?좊퀎??12,700?몄? ?뱀젙 ?곕룄蹂??좏뻾蹂대떎, ?꾩냽 ?곌뎄??怨듯넻 ?몄뼱媛 ??atlas, 痢≪젙踰? ?꾩긽 湲곗?, 由щ럭, 吏덊솚 肄뷀샇?? 遺꾩꽍 ?꾧뎄??異뺤쟻??媛뺥븯寃??쒕윭?몃떎.</p>
        <p>媛?????먮쫫? ?쇰컲 ?뚭낵?숆낵 由щ럭, ?꾩긽 ?좉꼍?쇑룹떊寃쏀눜?? ?명룷쨌遺꾩옄쨌?쒕깄???곌뎄媛 ?볦? 湲곕컲???뺤꽦?섍퀬, 洹??꾩뿉 ?몄?쨌?쒖뒪???좉꼍怨쇳븰, 諛쒕떖쨌媛?뚯꽦쨌connectomics, EEG/MEG, ?좉꼍?곸긽, ?뚰삁愿쨌?먯긽, 怨꾩궛?좉꼍怨쇳븰怨?BCI媛 ?묒냽?섎뒗 援ъ“?? 理쒓렐 援ш컙?쇰줈 ?ъ닔濡??⑥씪 諛⑸쾿濡좊낫???ㅼ쨷紐⑤떖 ?곗씠?? ?κ린 異붿쟻, ?ㅽ듃?뚰겕 ?섏? ?댁꽍, AI 湲곕컲 遺꾩꽍, ?먭레쨌?먮（???쒖뒪?쒖쓣 寃고빀?섎뒗 ?곌뎄媛 ??以묒슂?댁쭊??</p>
      </div>
      <h2>Research Insights</h2>
      <div class="research-insights">
        <article class="insight-box">
          <div class="insight-label">Infrastructure</div>
          <h3>怨듭쑀 ?명봽?쇨? ?곌뎄 諛⑺뼢???ы렪?쒕떎</h3>
          <p>?믪? ?몄슜 ?좏샇???⑥씪 諛쒓껄肉??꾨땲??atlas, 醫뚰몴怨? ?곸긽쨌?꾧린?앸━ ?꾨줈?좎퐳, ?꾩긽 泥숇룄泥섎읆 ?щ윭 ?섏쐞 遺꾩빞媛 ?④퍡 ?곕뒗 湲곕컲 ?쇰Ц??吏묒쨷?쒕떎.</p>
          <p class="insight-implication">?쒖궗?? ???곌뎄???낅┰ 寃곌낵蹂대떎 ?ъ궗??媛?ν븳 ?곗씠?? ?쒖?, ?꾧뎄瑜??숇컲?????κ린 ?곹뼢?μ씠 而ㅼ쭊??</p>
        </article>
        <article class="insight-box">
          <div class="insight-label">Clinical Translation</div>
          <h3>吏덈퀝 ?곌뎄???뚮줈쨌遺꾩옄쨌?곸긽??寃고빀?쇰줈 ?대룞?쒕떎</h3>
          <p>?좉꼍?댄뻾, ?뚯넀?? 醫낆뼇, ?뚰삁愿 ?곌뎄??蹂묐━ 遺꾨쪟?먯꽌 諛붿씠?ㅻ쭏而? ?곸긽, ?명룷 湲곗쟾, 移섎즺 諛섏쓳???④퍡 ?쎈뒗 諛⑺뼢?쇰줈 ?볦뼱吏怨??덈떎.</p>
          <p class="insight-implication">?쒖궗?? ?꾩긽???좎슜?깆? 湲곗쟾 ?ㅻ챸怨??섏옄援??ы쁽?깆쓣 ?숈떆???붽뎄?쒕떎.</p>
        </article>
        <article class="insight-box">
          <div class="insight-label">Multi-scale Models</div>
          <h3>諛쒕떖쨌媛?뚯꽦쨌connectomics媛 ?ㅼ??쇱쓣 ?곌껐?쒕떎</h3>
          <p>?명룷? ?쒕깄?? 援?냼 ?뚮줈, ?꾨뇤 ?ㅽ듃?뚰겕, ?됰룞 蹂?붾? ?댁뼱 蹂대젮???곌뎄媛 利앷??섎ŉ ?앹븷二쇨린? 吏덊솚 吏꾪뻾???④퍡 ?ㅻ챸?섎뒗 異뺤씠 ?쒕떎.</p>
          <p class="insight-implication">?쒖궗?? ?〓떒硫?寃곌낵留뚯쑝濡쒕뒗 遺議깊븯硫??κ린 異붿쟻怨??ㅽ듃?뚰겕 寃利앹씠 ?듭떖 蹂묐ぉ?대떎.</p>
        </article>
        <article class="insight-box">
          <div class="insight-label">AI And Computation</div>
          <h3>怨꾩궛 紐⑤뜽? 愿李곗쓣 ?덉륫 臾몄젣濡?諛붽씔??/h3>
          <p>怨꾩궛?좉꼍怨쇳븰怨?AI?????좏샇瑜??댁꽍?섎뒗 蹂댁“ ?꾧뎄?먯꽌 representation, decoding, disease trajectory ?덉륫???ㅻ（???곌뎄 ?몄뼱濡??뺤옣?쒕떎.</p>
          <p class="insight-implication">?쒖궗?? 紐⑤뜽 ?깅뒫蹂대떎 ?댁꽍 媛?μ꽦, ?몃? 寃利? ?곗씠???명뼢 ?듭젣媛 以묒슂?댁쭊??</p>
        </article>
        <article class="insight-box">
          <div class="insight-label">Neurotechnology</div>
          <h3>?먭레쨌BCI???꾩긽 ?꾪솚??愿臾몄씠 ?쒕떎</h3>
          <p>?뚯옄洹? neurotechnology, BCI ?곌뎄???좏샇 痢≪젙?먯꽌 媛쒖엯怨??먮（???쒖뼱濡??대룞?섎ŉ ?덉쟾?? ?κ린 ?덉젙?? 媛쒖씤?붽? ?듭떖 湲곗????쒕떎.</p>
          <p class="insight-implication">?쒖궗?? ?ㅼ젣 ?곸슜???꾪빐?쒕뒗 ?뺥솗?꾩? ?④퍡 ?ъ슜?? ?꾪뿕 愿由? ?섏옄蹂??곸쓳 ?꾨왂???꾩슂?섎떎.</p>
        </article>
        <article class="insight-box">
          <div class="insight-label">Open Gaps</div>
          <h3>?쒖??붋룹씤怨쇱꽦쨌?ㅼ뼇?깆씠 ?⑥? 蹂묐ぉ?대떎</h3>
          <p>?몄슜 湲곕컲 吏?꾨뒗 媛뺥븳 異뺤쓣 蹂댁뿬二쇱?留? ?멸뎄吏묐떒 ?ㅼ뼇?? ?λ퉬쨌遺꾩꽍 ?쒖??? ?멸낵 寃利? 理쒖떊 ?곌뎄???몄슜 吏?곗? ?ъ쟾???댁꽍?곸쓽 二쇱쓽?먯씠??</p>
          <p class="insight-implication">?쒖궗?? ?ㅼ쓬 ?④퀎??brain research map? citation rank? ?④퍡 reproducibility? clinical utility瑜??④퍡 ?됯??댁빞 ?쒕떎.</p>
        </article>
      </div>
    </section>
"""


def research_copy():
    return {
        "en": """
          <h2 id="research-timeline-title">Research Timeline</h2>
          <div class="timeline-copy">
            <p>The 1900-2026 brain-AI corpus follows a long arc from neuroanatomy, physiology, and early neural computation toward neuroimaging, connectomics, neural decoding, brain-computer interfaces, neuromorphic ideas, and machine-learning models of brain structure and function.</p>
            <p>The map is citation-ranked but taxonomy-first: it treats AI as a set of modeling, prediction, decoding, graph, representation, and brain-inspired methods that interact with structural and functional evidence about the brain.</p>
          </div>
          <h2>Research Insights</h2>
          <div class="research-insights">
            <article class="insight-box"><div class="insight-label">Bridge</div><h3>Brain structure becomes model input</h3><p>Structural MRI, functional connectivity, electrophysiology, and connectome papers increasingly become reusable feature spaces for AI systems.</p><p class="insight-implication">Implication: model validation should test whether learned features correspond to stable neurobiological structure.</p></article>
            <article class="insight-box"><div class="insight-label">Computation</div><h3>Neuroscience also shapes AI concepts</h3><p>Learning rules, neural coding, predictive coding, reinforcement learning, and cognitive architectures create conceptual traffic from brain science into AI.</p><p class="insight-implication">Implication: brain-inspired claims should be tied to measurable mechanisms, not only analogy.</p></article>
            <article class="insight-box"><div class="insight-label">Translation</div><h3>Clinical NeuroAI raises the evidence bar</h3><p>Disease prediction, diagnosis, prognosis, and treatment-response models need cohort diversity, calibration, and prospective validation.</p><p class="insight-implication">Implication: citation rank is a navigation signal, not a substitute for clinical evidence.</p></article>
          </div>
        """,
        "ko": """
          <h2 id="research-timeline-title">연구 타임라인</h2>
          <div class="timeline-copy">
            <p>1900-2026년 brain-AI corpus는 신경해부학, 생리학, 초기 신경계산에서 출발해 neuroimaging, connectomics, neural decoding, BCI, neuromorphic idea, 뇌 구조와 기능을 모델링하는 machine-learning 연구로 확장됩니다.</p>
            <p>이 지도는 인용 순위 기반이지만 taxonomy-first 방식입니다. AI를 modeling, prediction, decoding, graph, representation, brain-inspired method의 묶음으로 보고, 이를 뇌의 구조적·기능적 증거와 연결합니다.</p>
          </div>
          <h2>연구 인사이트</h2>
          <div class="research-insights">
            <article class="insight-box"><div class="insight-label">연결</div><h3>뇌 구조가 모델 입력이 됩니다</h3><p>구조 MRI, 기능적 연결성, 전기생리, connectome 논문은 점점 AI 시스템이 재사용할 수 있는 feature space가 됩니다.</p><p class="insight-implication">시사점: 모델 검증은 학습된 특징이 안정적인 신경생물학적 구조와 대응하는지 확인해야 합니다.</p></article>
            <article class="insight-box"><div class="insight-label">계산</div><h3>신경과학은 AI 개념도 형성합니다</h3><p>학습 규칙, neural coding, predictive coding, reinforcement learning, cognitive architecture는 뇌과학에서 AI로 이어지는 개념적 통로를 만듭니다.</p><p class="insight-implication">시사점: brain-inspired 주장은 단순 비유가 아니라 측정 가능한 메커니즘과 연결되어야 합니다.</p></article>
            <article class="insight-box"><div class="insight-label">임상 전환</div><h3>Clinical NeuroAI는 더 높은 증거 기준을 요구합니다</h3><p>질병 예측, 진단, 예후, 치료 반응 모델은 cohort 다양성, calibration, prospective validation이 필요합니다.</p><p class="insight-implication">시사점: 인용 순위는 탐색 신호이지 임상 근거를 대신하지 않습니다.</p></article>
          </div>
        """,
        "zh": """
          <h2 id="research-timeline-title">研究时间线</h2>
          <div class="timeline-copy">
            <p>1900-2026 年的 brain-AI 语料从神经解剖、生理学和早期神经计算，延伸到神经影像、连接组学、神经解码、脑机接口、类脑思想，以及脑结构和功能的机器学习模型。</p>
            <p>这张地图按引用排序，但以分类体系为先：它把 AI 视为建模、预测、解码、图、表示和脑启发方法的集合，并将这些方法与脑的结构和功能证据连接起来。</p>
          </div>
          <h2>研究洞察</h2>
          <div class="research-insights">
            <article class="insight-box"><div class="insight-label">桥接</div><h3>脑结构成为模型输入</h3><p>结构 MRI、功能连接、电生理和连接组论文越来越成为 AI 系统可复用的特征空间。</p><p class="insight-implication">启示：模型验证应检验学习到的特征是否对应稳定的神经生物结构。</p></article>
            <article class="insight-box"><div class="insight-label">计算</div><h3>神经科学也塑造 AI 概念</h3><p>学习规则、神经编码、预测编码、强化学习和认知架构构成了从脑科学通向 AI 的概念通道。</p><p class="insight-implication">启示：脑启发主张应连接到可测量机制，而不仅是类比。</p></article>
            <article class="insight-box"><div class="insight-label">转化</div><h3>临床 NeuroAI 提高了证据门槛</h3><p>疾病预测、诊断、预后和治疗反应模型需要队列多样性、校准和前瞻性验证。</p><p class="insight-implication">启示：引用排名是导航信号，不能替代临床证据。</p></article>
          </div>
        """,
        "ja": """
          <h2 id="research-timeline-title">研究タイムライン</h2>
          <div class="timeline-copy">
            <p>1900-2026 年の brain-AI コーパスは、神経解剖学、生理学、初期の神経計算から、神経画像、コネクトミクス、神経デコーディング、BCI、ニューロモルフィックな発想、脳構造と機能の機械学習モデルへ広がっています。</p>
            <p>この地図は引用順位に基づきますが、分類体系を優先します。AI をモデリング、予測、デコーディング、グラフ、表現、脳型手法の集合として扱い、脳の構造的・機能的証拠と接続します。</p>
          </div>
          <h2>研究インサイト</h2>
          <div class="research-insights">
            <article class="insight-box"><div class="insight-label">橋渡し</div><h3>脳構造がモデル入力になります</h3><p>構造 MRI、機能的結合、電気生理、コネクトームの論文は、AI システムが再利用できる特徴空間になりつつあります。</p><p class="insight-implication">示唆：モデル検証では、学習特徴が安定した神経生物学的構造に対応するか確認すべきです。</p></article>
            <article class="insight-box"><div class="insight-label">計算</div><h3>神経科学は AI 概念も形作ります</h3><p>学習則、神経符号化、予測符号化、強化学習、認知アーキテクチャは、脳科学から AI への概念的な流れを作ります。</p><p class="insight-implication">示唆：脳型 AI の主張は単なる比喩ではなく、測定可能な機構に結びつける必要があります。</p></article>
            <article class="insight-box"><div class="insight-label">臨床応用</div><h3>臨床 NeuroAI は証拠水準を引き上げます</h3><p>疾患予測、診断、予後、治療反応モデルには、コホート多様性、較正、前向き検証が必要です。</p><p class="insight-implication">示唆：引用順位はナビゲーション信号であり、臨床証拠の代替ではありません。</p></article>
          </div>
        """,
    }


def overall_research_templates():
    return {
        "en": {
            "timelineTitle": "Research Timeline",
            "summary": [
                "For {range}, this brain-AI corpus contains {papers} selected papers across {activeYears} active years, with {citations} citations. The strongest taxonomy signals are {topCategories}, and the most active year is {peakYear} ({peakYearCount} papers).",
                "The leading citation-ranked paper is \"{topPaper}\" ({topPaperYear}, {topPaperCitations} citations) in {topPaperCategory}. Keywords such as {topKeywords} show how the period connects brain structure, neural signals, computation, and AI modeling.",
            ],
            "insightsTitle": "Research Insights",
            "insights": [
                {"label": "Period Shape", "title": "The selected range changes the brain-AI map", "body": "{topCategory} accounts for {topCategoryCount} papers, so the visible corpus is anchored by the taxonomies that were strongest in {range}.", "implication": "Implication: compare adjacent periods before treating one taxonomy as the field's long-term center."},
                {"label": "Citation Mass", "title": "Citation concentration identifies shared infrastructure", "body": "The range carries {citations} citations, with the citation peak around {peakCitationYear}. Highly cited papers often define reusable atlases, protocols, cohorts, models, or analysis tools.", "implication": "Implication: durable brain-AI impact often comes from resources that other subfields can reuse."},
                {"label": "Methods", "title": "Keywords expose the period's methodological spine", "body": "Frequent tags such as {topKeywords} indicate which instruments, models, or research settings organize the selected years.", "implication": "Implication: keyword shifts are useful early signals before citation counts fully mature."},
                {"label": "Review Priority", "title": "What deserves full-text review next", "body": "This metadata-adapter insight flags {topCategories} and {topKeywords} as the period's highest-priority reading lanes.", "implication": "Implication: full PDF review remains the next step for causal claims, reproducibility, and experimental detail."},
            ],
        },
        "ko": {
            "timelineTitle": "연구 타임라인",
            "summary": [
                "{range} 기간의 brain-AI corpus는 {activeYears}개 활성 연도에서 선별된 논문 {papers}편과 인용 {citations}회를 포함합니다. 가장 강한 분류 신호는 {topCategories}이며, 논문 수가 가장 많은 해는 {peakYear}년({peakYearCount}편)입니다.",
                "인용 순위 최상위 논문은 \"{topPaper}\"({topPaperYear}, {topPaperCitations}회 인용)이며 분류는 {topPaperCategory}입니다. {topKeywords} 같은 키워드는 이 기간이 뇌 구조, 신경 신호, 계산, AI 모델링을 어떻게 연결하는지 보여줍니다.",
            ],
            "insightsTitle": "연구 인사이트",
            "insights": [
                {"label": "기간 구조", "title": "선택한 기간이 brain-AI 지도를 바꿉니다", "body": "{topCategory}가 {topCategoryCount}편을 차지하므로, 현재 보이는 corpus는 {range}에서 강했던 분류 축에 의해 고정됩니다.", "implication": "시사점: 한 분류를 장기 중심으로 보기 전에 인접 기간과 비교해야 합니다."},
                {"label": "인용 밀도", "title": "인용 집중은 공유 인프라를 드러냅니다", "body": "이 기간은 인용 {citations}회를 포함하며 인용 피크는 {peakCitationYear}년 부근입니다. 고인용 논문은 atlas, protocol, cohort, model, analysis tool처럼 재사용 가능한 자원을 정의하는 경우가 많습니다.", "implication": "시사점: 지속적인 brain-AI 영향력은 여러 하위 분야가 재사용할 수 있는 자원에서 자주 나옵니다."},
                {"label": "방법", "title": "키워드는 기간의 방법론적 척추를 보여줍니다", "body": "{topKeywords} 같은 빈번한 태그는 선택 연도를 조직하는 도구, 모델, 연구 환경을 보여줍니다.", "implication": "시사점: 키워드 변화는 인용이 충분히 쌓이기 전에도 유용한 초기 신호입니다."},
                {"label": "검토 우선순위", "title": "다음으로 전문 검토가 필요한 곳", "body": "이 metadata-adapter 인사이트는 {topCategories}와 {topKeywords}를 이 기간의 우선 읽기 경로로 표시합니다.", "implication": "시사점: 인과 주장, 재현성, 실험 세부사항에는 여전히 PDF 전문 검토가 필요합니다."},
            ],
        },
        "zh": {
            "timelineTitle": "研究时间线",
            "summary": [
                "在 {range} 期间，brain-AI 语料包含 {activeYears} 个活跃年份中的 {papers} 篇精选论文和 {citations} 次引用。最强的分类信号是 {topCategories}，论文数量最多的年份是 {peakYear}（{peakYearCount} 篇）。",
                "引用排名最高的论文是 \"{topPaper}\"（{topPaperYear}，{topPaperCitations} 次引用），分类为 {topPaperCategory}。{topKeywords} 等关键词显示这一时期如何连接脑结构、神经信号、计算和 AI 建模。",
            ],
            "insightsTitle": "研究洞察",
            "insights": [
                {"label": "时期形态", "title": "所选年份范围会改变 brain-AI 地图", "body": "{topCategory} 占 {topCategoryCount} 篇，因此可见语料由 {range} 期间最强的分类轴支撑。", "implication": "启示：在把某一分类视为长期中心之前，应先比较相邻时期。"},
                {"label": "引用集中", "title": "引用集中度识别共享基础设施", "body": "该范围包含 {citations} 次引用，引用峰值约在 {peakCitationYear}。高引用论文常定义可复用的图谱、协议、队列、模型或分析工具。", "implication": "启示：持久的 brain-AI 影响力往往来自其他子领域可以复用的资源。"},
                {"label": "方法", "title": "关键词揭示时期的方法主干", "body": "{topKeywords} 等高频标签显示哪些工具、模型或研究场景组织了所选年份。", "implication": "启示：在引用数充分成熟前，关键词变化就是有用的早期信号。"},
                {"label": "阅读优先级", "title": "下一步值得全文审读的内容", "body": "这个 metadata-adapter 洞察将 {topCategories} 和 {topKeywords} 标为该时期最高优先级的阅读路径。", "implication": "启示：因果主张、可复现性和实验细节仍需要 PDF 全文审读。"},
            ],
        },
        "ja": {
            "timelineTitle": "研究タイムライン",
            "summary": [
                "{range} の brain-AI コーパスには、{activeYears} の対象年から選ばれた {papers} 本の論文と {citations} 件の引用が含まれます。最も強い分類シグナルは {topCategories} で、論文数が最も多い年は {peakYear} 年（{peakYearCount} 本）です。",
                "引用順位トップの論文は \"{topPaper}\"（{topPaperYear}、{topPaperCitations} 件の引用）で、分類は {topPaperCategory} です。{topKeywords} などのキーワードは、この時期が脳構造、神経信号、計算、AI モデリングをどう結びつけるかを示します。",
            ],
            "insightsTitle": "研究インサイト",
            "insights": [
                {"label": "期間の形", "title": "選択範囲が brain-AI 地図を変えます", "body": "{topCategory} が {topCategoryCount} 本を占めるため、表示中のコーパスは {range} で強かった分類軸に支えられています。", "implication": "示唆：一つの分類を長期的中心とみなす前に、隣接期間と比較してください。"},
                {"label": "引用集中", "title": "引用の集中は共有インフラを示します", "body": "この範囲は {citations} 件の引用を持ち、引用ピークは {peakCitationYear} 年付近です。高被引用論文は、再利用可能なアトラス、プロトコル、コホート、モデル、分析ツールを定義することがよくあります。", "implication": "示唆：持続的な brain-AI の影響は、他分野が再利用できる資源から生まれることが多いです。"},
                {"label": "方法", "title": "キーワードは時期の方法論的な骨格を示します", "body": "{topKeywords} などの頻出タグは、選択年を組織する装置、モデル、研究環境を示します。", "implication": "示唆：キーワードの変化は、引用数が成熟する前の早期シグナルとして有用です。"},
                {"label": "レビュー優先度", "title": "次に全文レビューすべきもの", "body": "この metadata-adapter インサイトは、{topCategories} と {topKeywords} をこの期間の最優先の読解ルートとして示します。", "implication": "示唆：因果主張、再現性、実験詳細には、なお PDF 全文レビューが必要です。"},
            ],
        },
    }


def overall_period_summary(rows, start, end, by_year):
    counts, citations = category_stats(rows)
    keywords = keyword_stats(rows)
    year_counts = Counter(row["year"] for row in rows)
    year_citations = defaultdict(int)
    for row in rows:
        year_citations[row["year"]] += row["citationCount"]
    peak_year, peak_count = year_counts.most_common(1)[0] if year_counts else (None, 0)
    peak_citation_year = max(year_citations, key=year_citations.get) if year_citations else None
    top = max(rows, key=lambda item: item["citationCount"]) if rows else None
    summary = {
        "startYear": start,
        "endYear": end,
        "rangeLabel": str(start) if start == end else f"{start}-{end}",
        "totalPapers": len(rows),
        "activeYears": sum(1 for year in range(start, end + 1) if by_year[year]),
        "citationCount": sum(row["citationCount"] for row in rows),
        "categoryCount": len(counts),
        "topCategories": [
            {"name": category, "count": count, "citations": citations[category]}
            for category, count in counts.most_common(6)
        ],
        "topKeywords": [
            {"name": keyword.strip(), "count": count}
            for keyword, count in keywords.most_common(6)
        ],
        "peakYear": peak_year,
        "peakYearCount": peak_count,
        "peakCitationYear": peak_citation_year,
        "peakCitationCount": year_citations.get(peak_citation_year, 0) if peak_citation_year else 0,
        "topPaper": {
            "title": top["title"],
            "year": top["year"],
            "category": top["category"],
            "url": top["url"],
            "citations": top["citationCount"],
        } if top else None,
    }
    summary["periodInsights"] = paper_curation_period_insights(summary, "brain-AI")
    return summary


def _insight_number(value):
    return f"{int(value or 0):,}"


def _insight_names(items, key="name", limit=3, fallback="metadata-ranked signals"):
    values = [
        str(item.get(key, "")).strip()
        for item in (items or [])[:limit]
        if str(item.get(key, "")).strip()
    ]
    return ", ".join(values) if values else fallback


def paper_curation_period_insights(summary, corpus_label):
    return {
        code: template["insights"]
        for code, template in overall_research_templates().items()
    }


def write_overall_analysis(selected):
    by_year = {year: [row for row in selected if row["year"] == year] for year in YEARS}
    analysis = {}
    for start in YEARS:
        period_rows = []
        for end in range(start, END_YEAR + 1):
            period_rows.extend(by_year[end])
            analysis[f"{start}-{end}"] = overall_period_summary(period_rows, start, end, by_year)
    payload = {
        "generated": GENERATED_DATE,
        "yearRange": YEAR_RANGE_TEXT,
        "languages": LANGUAGES,
        "uiLabels": UI_LABELS,
        "analysis": analysis,
    }
    (DATA_DIR / OVERALL_ANALYSIS_JSON).write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")


def write_period_analysis(selected):
    by_year = {year: [row for row in selected if row["year"] == year] for year in YEARS}
    analysis = {}
    for start in YEARS:
        period_rows = []
        for end in range(start, END_YEAR + 1):
            period_rows.extend(by_year[end])
            counts, citations = category_stats(period_rows)
            keywords = keyword_stats(period_rows)
            top = max(period_rows, key=lambda item: item["citationCount"]) if period_rows else None
            analysis[f"{start}_{end}"] = {
                "startYear": start,
                "endYear": end,
                "totalPapers": len(period_rows),
                "activeYears": sum(1 for year in range(start, end + 1) if by_year[year]),
                "citationCount": sum(row["citationCount"] for row in period_rows),
                "categoryCounts": dict(counts),
                "categoryCitations": dict(citations),
                "keywordCounts": dict(keywords),
                "topPaper": {"title": top["title"], "year": top["year"], "url": top["url"], "citations": top["citationCount"]} if top else None,
            }
    (DATA_DIR / PERIOD_ANALYSIS_JSON).write_text(json.dumps(analysis, ensure_ascii=False, indent=2), encoding="utf-8")


def badge(keyword):
    color = KEYWORD_COLORS.get(keyword, "64748b")
    label = keyword.replace("-", "--")
    return f"![{keyword}](https://img.shields.io/badge/keyword-{label}-{color})"


def html_badge(keyword):
    color = KEYWORD_COLORS.get(keyword, "64748b")
    return f'<span class="badge" style="--badge-color: #{html.escape(color)}">{html.escape(keyword)}</span>'


def markdown_link(title, url):
    if url:
        return f"[{title}]({url})"
    return title


def html_escape(value):
    return html.escape(clean_text(value), quote=True)


def paper_table(rows, limit=20):
    out = [
        '<table width="100%">',
        "<thead><tr><th align=\"right\">Rank</th><th>Paper</th><th>Meta</th><th>Keywords</th><th>Key idea</th><th>Strengths</th><th>Limitations</th></tr></thead>",
        "<tbody>",
    ]
    for index, row in enumerate(rows[:limit], start=1):
        link = markdown_link(html_escape(row["title"]), html_escape(row["url"]))
        keywords = " ".join(badge(tag) for tag in row["keywordTags"].split(";") if tag) or "-"
        out.append(
            "<tr>"
            f"<td align=\"right\">{index}</td>"
            f"<td>{link}<br><sub>{html_escape(row['authors'])}</sub></td>"
            f"<td>{row['year']}<br>{html_escape(row['venue'])}<br>{row['citationCount']:,} citations</td>"
            f"<td>{keywords}</td>"
            f"<td>{html_escape(row['keyIdea'])}</td>"
            f"<td>{html_escape(row['strengths'])}</td>"
            f"<td>{html_escape(row['limitations'])}</td>"
            "</tr>"
        )
    if len(rows) > limit:
        out.append(f"<tr><td colspan=\"7\">See the website and taxonomy CSV for all {len(rows):,} papers in this category.</td></tr>")
    out.extend(["</tbody>", "</table>"])
    return "\n".join(out)


def markdown_to_html_doc(title, markdown):
    body_lines = []
    in_table = False
    for line in markdown.splitlines():
        if line.startswith("# "):
            body_lines.append(f"<h1>{html_escape(line[2:])}</h1>")
        elif line.startswith("## "):
            body_lines.append(f"<h2>{html_escape(line[3:])}</h2>")
        elif line.startswith("### "):
            body_lines.append(f"<h3>{html_escape(line[4:])}</h3>")
        elif line.startswith("|"):
            if not in_table:
                body_lines.append("<pre class=\"table-block\">")
                in_table = True
            body_lines.append(html_escape(line))
        else:
            if in_table:
                body_lines.append("</pre>")
                in_table = False
            if not line.strip():
                body_lines.append("")
            elif line.startswith("- "):
                body_lines.append(f"<p>{html_escape(line)}</p>")
            else:
                body_lines.append(f"<p>{html_escape(line)}</p>")
    if in_table:
        body_lines.append("</pre>")
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html_escape(title)}</title>
  <style>
    body {{ font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; max-width: 980px; margin: 40px auto; padding: 0 24px; color: #172033; line-height: 1.65; }}
    h1, h2, h3 {{ line-height: 1.2; }}
    .table-block {{ white-space: pre-wrap; background: #f6f8fb; border: 1px solid #d9dee8; padding: 14px; overflow: auto; }}
  </style>
</head>
<body>
{chr(10).join(body_lines)}
</body>
</html>
"""


def readme_language_selector_lines(owner, repo):
    return [
        '<div align="center">',
        '  <a href="README.md"><strong>English</strong></a> |',
        '  <a href="README.de.md">Deutsch</a> |',
        '  <a href="README.es.md">Espanol</a> |',
        '  <a href="README.fr.md">Francais</a> |',
        '  <a href="README.ja.md">Japanese</a> |',
        '  <a href="README.ko.md">Korean</a> |',
        '  <a href="README.pt.md">Portugues</a> |',
        '  <a href="README.ru.md">Russian</a> |',
        '  <a href="README.zh.md">Chinese</a>',
        "</div>",
        "",
    ]


def write_readme(selected, candidates):
    counts, citations = category_stats(selected)
    stats = year_stats(selected)
    lines = [
        "# Awesome Brain AI",
        "",
        "[![Awesome](https://awesome.re/badge-flat.png)](https://awesome.re)",
        "",
        "A taxonomy-first, citation-ranked map of brain-structure and AI-relation research from 1900 through 2026.",
        "",
        '<p align="center">',
        '  <a href="https://honggi82.github.io/awesome-brain-ai/">',
        '    <img src="https://img.shields.io/badge/Open_Interactive_Website-honggi82.github.io%2Fawesome--brain--ai-0f766e?style=for-the-badge" alt="Open Interactive Website">',
        "  </a>",
        "</p>",
        "",
        *readme_language_selector_lines("honggi82", "awesome-brain-ai"),
        "> Browse the full interactive taxonomy site with period, keyword, chart, and paper-card filters: https://honggi82.github.io/awesome-brain-ai/",
        "",
        f"Generated on {GENERATED_DATE} from free public Semantic Scholar metadata. The current edition starts from an audited brain-structure candidate pool, re-scores each record for AI/modeling/decoding/brain-inspired relevance, selects the top {TARGET_PER_YEAR} papers per year by citation count from the eligible pool for {YEAR_RANGE_TEXT}, and reorganizes the selected {len(selected):,} papers by brain-AI relation taxonomy.",
        "",
        "## Project Links",
        "",
        "- Website: https://honggi82.github.io/awesome-brain-ai/",
        f"- Selected dataset: `data/{PAPERS_CSV}`",
        f"- Taxonomy dataset with paper-level ideas, strengths, and limitations: `data/{TAXONOMY_CSV}`",
        f"- Precomputed period and keyword analysis: `data/{PERIOD_ANALYSIS_JSON}`",
        f"- Candidate pool: `data/{CANDIDATES_CSV}`",
        "- English review draft: `paper/review_en.html`, `paper/review_en.docx`",
        "- Korean review draft: `paper/review_ko.html`",
        "- Curation method: `paper/curation_method.md`, `paper/curation_method.html`",
        "",
        "## Keywords Convention",
        "",
        "These badges define the brain-structure and AI-relation keyword tags used to read and extend this collection.",
        "",
    ]
    for keyword, description, _ in KEYWORD_CONVENTION:
        lines.append(f"- {badge(keyword)} **{keyword}**: {description}")
    lines.extend(["", "## Taxonomy Overview", ""])
    lines.append(f"- **Total selected papers**: {len(selected):,} papers")
    for category, count in counts.most_common():
        lines.append(f"- **{category}**: {count:,} papers")
    lines.extend(["", "## Taxonomy Collections", ""])
    by_category = defaultdict(list)
    for row in selected:
        by_category[row["category"]].append(row)
    for category in CATEGORIES:
        name = category["name"]
        rows = sorted(by_category[name], key=lambda item: (-item["citationCount"], item["year"], item["title"].lower()))
        if not rows:
            continue
        years = [row["year"] for row in rows]
        lines.extend(
            [
                f"### {name}",
                "",
                f"- Papers selected: **{len(rows):,}**",
                f"- Years covered: **{min(years)}-{max(years)}**",
                f"- Citation count in selected set: **{sum(row['citationCount'] for row in rows):,}**",
                "- Category Overview (main research trends):",
            ]
        )
        lines.extend([f"  - {item}" for item in category["overview"]])
        lines.append("- Limitations:")
        lines.extend([f"  - {item}" for item in category["limitations"]])
        lines.extend(
            [
                "",
                f"<details>",
                f"<summary><strong>Show representative papers for {name}</strong></summary>",
                "",
                paper_table(rows),
                "",
                "</details>",
                "",
            ]
        )
    lines.extend(["## Yearly Coverage", ""])
    lines.append("| Year | Candidate papers | Selected papers | Citation count | Top paper |")
    lines.append("| ---: | ---: | ---: | ---: | --- |")
    candidate_counts = Counter(row["year"] for row in candidates)
    for year in YEARS:
        info = stats.get(year)
        if not info:
            lines.append(f"| {year} | {candidate_counts.get(year, 0):,} | 0 | 0 | - |")
            continue
        top = info["top"]
        lines.append(
            f"| {year} | {candidate_counts.get(year, 0):,} | {info['count']:,} | {info['citations']:,} | {markdown_link(top['title'], top['url'])} |"
        )
    lines.extend(
        [
            "",
            "## Method",
            "",
            f"The collection uses the Semantic Scholar Academic Graph bulk paper search and cached public metadata from the companion brain map. For each publication year from {START_YEAR} through {END_YEAR}, the pipeline re-evaluates title, abstract, venue, and field metadata for explicit brain-structure signals plus AI, machine-learning, computational, decoding, graph, neuromorphic, BCI, or brain-inspired modeling signals. It keeps up to {CANDIDATES_PER_YEAR:,} audited candidates per year, then selects the top {TARGET_PER_YEAR} eligible papers per year by citation count. Taxonomy, keyword tags, key ideas, strengths, limitations, and audit scores are deterministic rule-based enrichments so the repository can be regenerated without paid APIs.",
            "",
            "## Caveats",
            "",
            "- Citation counts favor older papers and can under-rank very recent 2026 work.",
            "- Some early years have fewer than 1,000 discoverable candidates because the public metadata pool is sparse before large-scale journal indexing; every year still contributes 100 selected papers.",
            "- Semantic Scholar metadata is broad scholarly metadata; this is not a full systematic review of every PDF.",
            "- Influential citation counts use Semantic Scholar metadata when available.",
            "- Brain-AI relation research spans neuroscience, neurology, psychology, engineering, computation, clinical medicine, and machine learning, so taxonomy boundaries are necessarily approximate.",
            "",
            "## Acknowledgements",
            "",
            "This repository and interactive site were created with appreciation for [jehyunlee/paper-curation](https://github.com/jehyunlee/paper-curation). Its paper-curation workflow and repository organization informed the approach used here for a taxonomy-first, citation-ranked research map.",
        ]
    )
    readme = "\n".join(lines) + "\n"
    (ROOT / "README.md").write_text(readme, encoding="utf-8")
    (ROOT / "README.html").write_text(markdown_to_html_doc("Awesome Brain AI", readme), encoding="utf-8")


def write_taxonomy_assets():
    target = DOCS_DIR / "assets" / "taxonomy"
    missing = []
    for category in CATEGORIES:
        image_path = target / f"{category['slug']}.png"
        if not image_path.exists():
            missing.append(image_path.as_posix())
    if missing:
        raise FileNotFoundError("Missing taxonomy PNG assets: " + ", ".join(missing))


def site_rows(selected):
    rows = []
    for row in selected:
        rows.append(
            {
                "rank": row["rank"],
                "year": row["year"],
                "title": row["title"],
                "authors": row["authors"],
                "venue": row["venue"],
                "citationCount": row["citationCount"],
                "influentialCitationCount": row["influentialCitationCount"],
                "importanceScore": row["importanceScore"],
                "category": row["category"],
                "keywordTags": [tag for tag in row["keywordTags"].split(";") if tag],
                "keyIdea": row["keyIdea"],
                "strengths": row["strengths"],
                "limitations": row["limitations"],
                "localized": localized_paper_text(row),
                "url": row["url"],
                "semanticScholarUrl": semantic_scholar_url(row),
                "openAccessPdf": row["openAccessPdf"],
                "githubUrl": row.get("githubUrl", ""),
                "workType": row["workType"],
            }
        )
    return rows


def write_site(selected):
    apply_github_links(selected)
    categories = [
        {
            "name": item["name"],
            "slug": item["slug"],
            "accent": item["accent"],
            "overview": item["overview"],
            "limitations": item["limitations"],
            "localized": CATEGORY_TEXT_I18N.get(item["name"], {}),
            "icon": f"assets/taxonomy/{item['slug']}.png",
        }
        for item in CATEGORIES
    ]
    keyword_info = [
        {
            "name": keyword,
            "description": {"en": desc, **KEYWORD_DESCRIPTION_I18N.get(keyword, {})},
            "color": color,
        }
        for keyword, desc, color in KEYWORD_CONVENTION
    ]
    payload = json.dumps(site_rows(selected), ensure_ascii=False)
    category_payload = json.dumps(categories, ensure_ascii=False)
    keyword_payload = json.dumps(keyword_info, ensure_ascii=False)
    research_overview = f'<section class="research-brief" id="researchBrief" aria-labelledby="research-timeline-title">{research_copy()["en"]}</section>'
    research_copy_payload = json.dumps(research_copy(), ensure_ascii=False)
    overall_research_templates_payload = json.dumps(overall_research_templates(), ensure_ascii=False)
    ui_labels_payload = json.dumps(UI_LABELS, ensure_ascii=False)
    language_options = "\n".join(
        f'<option value="{code}"{" selected" if code == "en" else ""}>{html.escape(label)}</option>'
        for code, label in LANGUAGES.items()
    )
    index = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Awesome Brain AI</title>
  <style>
    :root {{
      color-scheme: light;
      --ink: #142033;
      --muted: #5b6678;
      --line: #dbe3ee;
      --soft: #f6f8fb;
      --panel: #ffffff;
      --accent: #2563eb;
      --focus: #0f766e;
    }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; color: var(--ink); background: #ffffff; }}
    header {{ padding: 26px 28px 18px; border-bottom: 1px solid var(--line); background: linear-gradient(180deg, #f8fafc 0%, #ffffff 100%); }}
    h1 {{ margin: 0 0 8px; font-size: 34px; letter-spacing: 0; }}
    h2 {{ margin: 0 0 12px; font-size: 22px; }}
    h3 {{ margin: 0; font-size: 18px; }}
    p {{ color: var(--muted); line-height: 1.55; }}
    a {{ color: #1d4ed8; }}
    .topline {{ display: flex; flex-wrap: wrap; gap: 12px; align-items: center; justify-content: space-between; }}
    .links {{ display: flex; flex-wrap: wrap; gap: 10px; }}
    .links a, button, select {{ min-height: 38px; border: 1px solid var(--line); background: var(--panel); color: var(--ink); border-radius: 6px; padding: 8px 11px; font: inherit; }}
    button {{ cursor: pointer; }}
    button:hover, select:hover {{ border-color: #94a3b8; }}
    main {{ padding: 24px 28px 48px; max-width: 1440px; margin: 0 auto; }}
    .controls {{ display: grid; grid-template-columns: repeat(6, minmax(130px, 1fr)); gap: 12px; align-items: end; padding: 14px 0 18px; border-bottom: 1px solid var(--line); }}
    label {{ display: grid; gap: 6px; font-size: 12px; color: var(--muted); font-weight: 700; text-transform: uppercase; }}
    .stats {{ display: grid; grid-template-columns: repeat(4, minmax(160px, 1fr)); gap: 12px; margin: 18px 0; }}
    .stat {{ border: 1px solid var(--line); border-radius: 8px; padding: 14px; background: var(--soft); }}
    .stat strong {{ display: block; font-size: 26px; color: var(--ink); }}
    .research-brief {{ margin: 28px 0; padding: 24px 0; border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); }}
    .timeline-copy {{ max-width: 1080px; }}
    .research-insights {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 12px; margin-top: 12px; }}
    .insight-box {{ border: 1px solid var(--line); border-radius: 8px; padding: 14px; background: #fff; }}
    .insight-label {{ color: var(--focus); font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 0; }}
    .insight-box h3 {{ margin: 6px 0 8px; font-size: 17px; }}
    .insight-box p {{ margin: 8px 0 0; }}
    .insight-implication {{ color: var(--ink); font-weight: 700; }}
    .keyword-panel {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 10px; margin: 12px 0 8px; }}
    .keyword-button {{ display: grid; gap: 8px; align-items: start; min-height: 112px; border-radius: 8px; text-align: left; line-height: 1.45; }}
    .keyword-button[aria-pressed="true"] {{ border-color: var(--focus); box-shadow: 0 0 0 2px rgba(15, 118, 110, 0.16); }}
    .keyword-chip {{ justify-self: start; display: inline-flex; gap: 7px; align-items: center; border-radius: 999px; padding: 4px 9px; background: var(--keyword-color); color: white; font-size: 13px; font-weight: 800; }}
    .keyword-dot {{ width: 8px; height: 8px; border-radius: 50%; background: currentColor; display: inline-block; opacity: 0.88; }}
    .keyword-description {{ display: block; width: 100%; color: var(--muted); }}
    .keyword-count {{ color: var(--focus); font-size: 12px; font-weight: 800; }}
    .keyword-status {{ min-height: 24px; color: var(--muted); margin: 4px 0 18px; }}
    .charts {{ display: grid; grid-template-columns: minmax(260px, 1fr) minmax(260px, 1fr); gap: 18px; margin: 18px 0 24px; }}
    .chart-wrap {{ border: 1px solid var(--line); border-radius: 8px; padding: 14px; min-height: 280px; }}
    canvas {{ width: 100%; height: 230px; display: block; }}
    .taxonomy {{ display: grid; gap: 12px; }}
    details {{ border: 1px solid var(--line); border-radius: 8px; background: var(--panel); overflow: hidden; }}
    summary {{ list-style: none; cursor: pointer; padding: 0; }}
    summary::-webkit-details-marker {{ display: none; }}
    .summary-row {{ display: grid; grid-template-columns: 98px minmax(220px, 1fr) repeat(3, minmax(110px, 150px)); gap: 14px; align-items: center; padding: 12px 14px; }}
    .summary-row img, .summary-all-icon {{ width: 98px; height: 56px; object-fit: cover; border-radius: 6px; border: 1px solid var(--line); }}
    .summary-all-icon {{ display: inline-flex; align-items: center; justify-content: center; background: #eef6ff; color: #1d4ed8; font-weight: 800; }}
    .summary-metric {{ color: var(--muted); font-size: 13px; }}
    .summary-metric strong {{ display: block; color: var(--ink); font-size: 18px; }}
    .section-body {{ padding: 16px; border-top: 1px solid var(--line); }}
    .section-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 18px; margin-bottom: 16px; }}
    .section-grid ul {{ margin-top: 8px; color: var(--muted); line-height: 1.55; }}
    .paper-list {{ display: grid; gap: 10px; }}
    .paper-card {{ border: 1px solid var(--line); border-radius: 8px; padding: 13px; background: #fff; }}
    .paper-head {{ display: flex; gap: 10px; justify-content: space-between; align-items: start; }}
    .paper-title {{ font-weight: 800; line-height: 1.35; }}
    .meta {{ color: var(--muted); font-size: 13px; margin-top: 4px; }}
    .badges {{ display: flex; flex-wrap: wrap; gap: 6px; margin: 10px 0; }}
    .badge {{ display: inline-flex; align-items: center; border: 1px solid color-mix(in srgb, var(--badge-color), #ffffff 35%); background: color-mix(in srgb, var(--badge-color), #ffffff 88%); color: #172033; border-radius: 999px; padding: 3px 8px; font-size: 12px; }}
    .paper-card dl {{ display: grid; grid-template-columns: 110px 1fr; gap: 7px 12px; margin: 10px 0 0; }}
    .paper-card dt {{ font-weight: 800; color: var(--ink); }}
    .paper-card dd {{ margin: 0; color: var(--muted); }}
    .empty {{ padding: 22px; border: 1px dashed var(--line); border-radius: 8px; color: var(--muted); }}
    @media (max-width: 920px) {{
      .controls, .stats, .charts, .section-grid {{ grid-template-columns: 1fr; }}
      .summary-row {{ grid-template-columns: 74px 1fr; }}
      .summary-metric {{ grid-column: 2; }}
      .summary-row img, .summary-all-icon {{ width: 74px; height: 52px; }}
      .paper-head, .paper-card dl {{ display: block; }}
      .paper-card dt {{ margin-top: 8px; }}
    }}
  </style>
</head>
<body>
  <header>
    <div class="topline">
      <div>
        <h1>Awesome Brain AI</h1>
        <p>Taxonomy-first, citation-ranked brain-structure and AI-relation map for {YEAR_RANGE_TEXT}. Generated {GENERATED_DATE} from free Semantic Scholar metadata.</p>
      </div>
      <nav class="links" aria-label="Project links">
        <a href="../README.md">README</a>
        <a href="../data/{PAPERS_CSV}">Selected CSV</a>
        <a href="../data/{CANDIDATES_CSV}">Candidate CSV</a>
        <a href="../paper/review_en.html">Review</a>
      </nav>
    </div>
  </header>
  <main>
    <section class="controls" aria-label="Filters">
      <label>Preset
        <select id="preset">
          <option value="{START_YEAR}-{END_YEAR}">All years</option>
          <option value="1900-1949">1900-1949</option>
          <option value="1950-1979">1950-1979</option>
          <option value="1980-1999">1980-1999</option>
          <option value="2000-2009">2000-2009</option>
          <option value="2010-2019">2010-2019</option>
          <option value="2020-2026">2020-2026</option>
        </select>
      </label>
      <label>Start year<select id="startYear"></select></label>
      <label>End year<select id="endYear"></select></label>
      <label>Language
        <select id="language">
          {language_options}
        </select>
      </label>
      <button id="reset" type="button">Reset</button>
    </section>
    <section class="stats" id="stats" aria-live="polite"></section>
    {research_overview}
    <h2>Keywords Convention</h2>
    <div class="keyword-panel" id="keywordPanel"></div>
    <div class="keyword-status" id="keywordStatus">No keyword selected.</div>
    <section class="charts">
      <div class="chart-wrap"><h2>Category Distribution</h2><canvas id="categoryChart" width="720" height="300"></canvas></div>
      <div class="chart-wrap"><h2>Yearly Citation Mass</h2><canvas id="yearChart" width="720" height="300"></canvas></div>
    </section>
    <section class="taxonomy" id="taxonomy"></section>
  </main>
  <script>
    const PAPERS = {payload};
    const CATEGORIES = {category_payload};
    const KEYWORDS = {keyword_payload};
    const RESEARCH_COPY = {research_copy_payload};
    const OVERALL_RESEARCH_TEMPLATES = {overall_research_templates_payload};
    const OVERALL_ANALYSIS_URL = 'data/{OVERALL_ANALYSIS_JSON}';
    const START_YEAR = {START_YEAR};
    const END_YEAR = {END_YEAR};
    const labels = {ui_labels_payload};
    const state = {{ start: START_YEAR, end: END_YEAR, keyword: null, lang: 'en' }};
    let overallAnalysis = null;
    const startSelect = document.getElementById('startYear');
    const endSelect = document.getElementById('endYear');
    const presetSelect = document.getElementById('preset');
    const languageSelect = document.getElementById('language');
    const keywordPanel = document.getElementById('keywordPanel');
    const keywordStatus = document.getElementById('keywordStatus');
    const taxonomy = document.getElementById('taxonomy');

    function fmt(value) {{ return Number(value || 0).toLocaleString(); }}
    function filtered() {{
      return PAPERS.filter(p => p.year >= state.start && p.year <= state.end && (!state.keyword || p.keywordTags.includes(state.keyword)));
    }}
    function fillYears() {{
      for (let year = START_YEAR; year <= END_YEAR; year++) {{
        startSelect.append(new Option(year, year));
        endSelect.append(new Option(year, year));
      }}
      startSelect.value = state.start;
      endSelect.value = state.end;
    }}
    function renderStats(rows) {{
      const activeYears = new Set(rows.map(p => p.year)).size;
      const citations = rows.reduce((sum, p) => sum + p.citationCount, 0);
      const cats = new Set(rows.map(p => p.category)).size;
      const l = labels[state.lang] || labels.en;
      document.getElementById('stats').innerHTML = `
        <div class="stat"><strong>${{fmt(rows.length)}}</strong>${{l.papers}}</div>
        <div class="stat"><strong>${{fmt(activeYears)}}</strong>${{l.years}}</div>
        <div class="stat"><strong>${{fmt(citations)}}</strong>${{l.citations}}</div>
        <div class="stat"><strong>${{fmt(cats)}}</strong>${{l.categories}}</div>`;
    }}
    function escapeHtml(value) {{
      const escapeMap = {{ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }};
      return String(value ?? '').replace(/[&<>"']/g, ch => escapeMap[ch]);
    }}
    function t(name) {{
      const current = labels[state.lang] || labels.en || {{}};
      const english = labels.en || {{}};
      return current[name] || english[name] || name;
    }}
    function localized(value) {{
      if (!value || typeof value !== 'object' || Array.isArray(value)) return value;
      return value[state.lang] || value.en || Object.values(value)[0] || '';
    }}
    function localizedCategoryList(category, field) {{
      const languageBlock = category.localized?.[state.lang] || category.localized?.en || null;
      return (languageBlock && languageBlock[field]) || category[field] || [];
    }}
    function localizedPaperField(paper, field) {{
      const languageBlock = paper.localized?.[state.lang] || paper.localized?.en || null;
      return (languageBlock && languageBlock[field]) || paper[field] || '';
    }}
    function listItems(items) {{
      return (items || []).map(item => `<li>${{escapeHtml(item)}}</li>`).join('');
    }}
    function names(items, key = 'name') {{
      return (items || []).slice(0, 3).map(item => item[key]).filter(Boolean).join(', ') || 'n/a';
    }}
    function researchTemplateData(metric) {{
      const topCategories = metric.topCategories || [];
      const topKeywords = metric.topKeywords || [];
      const topCategory = topCategories[0] || {{}};
      const topPaper = metric.topPaper || {{}};
      return {{
        range: metric.rangeLabel || `${{metric.startYear}}-${{metric.endYear}}`,
        papers: fmt(metric.totalPapers),
        activeYears: fmt(metric.activeYears),
        citations: fmt(metric.citationCount),
        topCategories: names(topCategories),
        topCategory: topCategory.name || 'n/a',
        topCategoryCount: fmt(topCategory.count || 0),
        topKeywords: names(topKeywords),
        peakYear: metric.peakYear || 'n/a',
        peakYearCount: fmt(metric.peakYearCount || 0),
        peakCitationYear: metric.peakCitationYear || 'n/a',
        topPaper: topPaper.title || 'n/a',
        topPaperYear: topPaper.year || 'n/a',
        topPaperCategory: topPaper.category || 'n/a',
        topPaperCitations: fmt(topPaper.citations || 0)
      }};
    }}
    function applyTemplate(template, data) {{
      let output = template || '';
      Object.keys(data).forEach(key => {{
        output = output.split('{{' + key + '}}').join(escapeHtml(data[key]));
      }});
      return output;
    }}
    function renderOverallResearch(metric) {{
      const copy = OVERALL_RESEARCH_TEMPLATES[state.lang] || OVERALL_RESEARCH_TEMPLATES.en;
      const data = researchTemplateData(metric);
      const summaryHtml = (copy.summary || []).map(text => `<p>${{applyTemplate(text, data)}}</p>`).join('');
      const insightItems = metric?.periodInsights?.[state.lang] || copy.insights || metric?.periodInsights?.en || [];
      const insightHtml = insightItems.map(item => `
        <article class="insight-box">
          <div class="insight-label">${{escapeHtml(item.label)}}</div>
          <h3>${{applyTemplate(item.title, data)}}</h3>
          <p>${{applyTemplate(item.body, data)}}</p>
          <p class="insight-implication">${{applyTemplate(item.implication, data)}}</p>
        </article>`).join('');
      return `
        <h2 id="research-timeline-title">${{escapeHtml(copy.timelineTitle)}}</h2>
        <div class="timeline-copy">${{summaryHtml}}</div>
        <h2>${{escapeHtml(copy.insightsTitle)}}</h2>
        <div class="research-insights">${{insightHtml}}</div>`;
    }}
    function renderResearchCopy() {{
      const brief = document.getElementById('researchBrief');
      if (!brief) return;
      const key = `${{state.start}}-${{state.end}}`;
      const metric = overallAnalysis?.analysis?.[key];
      brief.innerHTML = metric ? renderOverallResearch(metric) : (RESEARCH_COPY[state.lang] || RESEARCH_COPY.en);
    }}
    function renderKeywords(rows) {{
      keywordPanel.innerHTML = KEYWORDS.map(k => {{
        const matchCount = PAPERS.filter(p => p.year >= state.start && p.year <= state.end && p.keywordTags.includes(k.name)).length;
        const pressed = state.keyword === k.name ? 'true' : 'false';
        return `<button class="keyword-button" type="button" data-keyword="${{escapeHtml(k.name)}}" aria-pressed="${{pressed}}" style="--keyword-color:#${{k.color}}">
          <span class="keyword-chip"><span class="keyword-dot"></span><span>${{escapeHtml(k.name)}}</span></span>
          <span class="keyword-description">${{escapeHtml(localized(k.description))}}</span>
          <span class="keyword-count">${{fmt(matchCount)}} ${{t('papers')}}</span>
        </button>`;
      }}).join('');
      if (state.keyword) {{
        keywordStatus.textContent = `${{state.keyword}} ${{t('selected')}} - ${{fmt(rows.length)}} ${{t('matchingPapers')}}.`;
      }} else {{
        keywordStatus.textContent = t('noKeyword');
      }}
    }}
    keywordPanel.addEventListener('click', event => {{
      const button = event.target.closest('[data-keyword]');
      if (!button) return;
      const keyword = button.dataset.keyword;
      state.keyword = state.keyword === keyword ? null : keyword;
      render();
    }});
    function countsBy(rows, key) {{
      const counts = new Map();
      for (const row of rows) counts.set(row[key], (counts.get(row[key]) || 0) + 1);
      return counts;
    }}
    function citationsByYear(rows) {{
      const counts = new Map();
      for (const row of rows) counts.set(row.year, (counts.get(row.year) || 0) + row.citationCount);
      return counts;
    }}
    function drawBarChart(canvas, entries, color) {{
      const ctx = canvas.getContext('2d');
      const width = canvas.width;
      const height = canvas.height;
      ctx.clearRect(0, 0, width, height);
      ctx.fillStyle = '#ffffff';
      ctx.fillRect(0, 0, width, height);
      const max = Math.max(1, ...entries.map(e => e.value));
      const left = 150, right = 20, top = 16, bottom = 30;
      const plotWidth = width - left - right;
      const rowHeight = Math.max(14, (height - top - bottom) / Math.max(entries.length, 1));
      ctx.font = '12px system-ui';
      entries.forEach((entry, index) => {{
        const y = top + index * rowHeight;
        const barWidth = Math.max(1, (entry.value / max) * plotWidth);
        ctx.fillStyle = '#5b6678';
        ctx.fillText(entry.label.slice(0, 22), 8, y + rowHeight * 0.62);
        ctx.fillStyle = color;
        ctx.fillRect(left, y + 3, barWidth, Math.max(7, rowHeight - 7));
        ctx.fillStyle = '#172033';
        ctx.fillText(fmt(entry.value), left + barWidth + 5, y + rowHeight * 0.62);
      }});
    }}
    function renderCharts(rows) {{
      const catEntries = Array.from(countsBy(rows, 'category'), ([label, value]) => ({{ label, value }})).sort((a, b) => b.value - a.value).slice(0, 10);
      drawBarChart(document.getElementById('categoryChart'), catEntries, '#2563eb');
      const yearCounts = citationsByYear(rows);
      const yearEntries = [];
      for (let year = state.start; year <= state.end; year++) {{
        if (yearCounts.has(year)) yearEntries.push({{ label: String(year), value: yearCounts.get(year) }});
      }}
      const sampled = yearEntries.length > 28 ? yearEntries.filter((_, i) => i % Math.ceil(yearEntries.length / 28) === 0) : yearEntries;
      drawBarChart(document.getElementById('yearChart'), sampled, '#0f766e');
    }}
    function badges(tags) {{
      return tags.map(tag => {{
        const meta = KEYWORDS.find(k => k.name === tag);
        const color = meta ? meta.color : '64748b';
        return `<span class="badge" style="--badge-color:#${{color}}">${{tag}}</span>`;
      }}).join('');
    }}
    function paperCard(p) {{
      const l = labels[state.lang] || labels.en;
      const linkParts = [`<a href="${{p.url}}">${{escapeHtml(l.paperLink)}}</a>`];
      if (p.semanticScholarUrl) linkParts.push(`<a href="${{p.semanticScholarUrl}}">Semantic Scholar</a>`);
      if (p.openAccessPdf) linkParts.push(`<a href="${{p.openAccessPdf}}">PDF</a>`);
      if (p.githubUrl) linkParts.push(`<a href="${{p.githubUrl}}">GitHub</a>`);
      const links = linkParts.join(' &middot; ');
      return `<article class="paper-card" data-year="${{p.year}}" data-keywords="${{p.keywordTags.join(' ')}}">
        <div class="paper-head"><div><a class="paper-title" href="${{p.url}}">${{p.title}}</a><div class="meta">${{p.authors}}</div></div><div class="meta">#${{p.rank}} in ${{p.year}}</div></div>
        <div class="meta">${{p.year}} &middot; ${{p.venue}} &middot; ${{fmt(p.citationCount)}} ${{l.citations}} &middot; ${{l.influentialCitations}} ${{fmt(p.influentialCitationCount)}} &middot; ${{l.score}} ${{p.importanceScore}} &middot; ${{links}}</div>
        <div class="badges">${{badges(p.keywordTags)}}</div>
        <dl><dt>${{l.keyIdea}}</dt><dd>${{escapeHtml(localizedPaperField(p, 'keyIdea'))}}</dd><dt>${{l.strengths}}</dt><dd>${{escapeHtml(localizedPaperField(p, 'strengths'))}}</dd><dt>${{l.limitations}}</dt><dd>${{escapeHtml(localizedPaperField(p, 'limitations'))}}</dd></dl>
      </article>`;
    }}
    function allTaxonomiesDetails(rows) {{
      const l = labels[state.lang] || labels.en;
      const allRows = [...rows].sort((a, b) => b.citationCount - a.citationCount);
      const years = allRows.map(p => p.year);
      const citations = allRows.reduce((sum, p) => sum + p.citationCount, 0);
      const top = allRows[0];
      const visibleCards = allRows.slice(0, 120).map(paperCard).join('');
      const extra = allRows.length > 120 ? `<p class="meta">${{l.showing}} 120 ${{l.of}} ${{fmt(allRows.length)}} ${{l.matchingPapers}}. ${{l.completeSet}}</p>` : '';
      return `<details>
        <summary><div class="summary-row">
          <div class="summary-all-icon" aria-hidden="true">All</div>
          <div><h3>${{l.allTaxonomies}}</h3><div class="meta">${{l.topPaper}}: <a href="${{top.url}}">${{top.title}}</a></div></div>
          <div class="summary-metric"><strong>${{fmt(allRows.length)}}</strong>${{l.papers}}</div>
          <div class="summary-metric"><strong>${{Math.min(...years)}}-${{Math.max(...years)}}</strong>${{l.years}}</div>
          <div class="summary-metric"><strong>${{fmt(citations)}}</strong>${{l.citations}}</div>
        </div></summary>
        <div class="section-body">
          <div class="section-grid">
            <div><h3>${{l.overview}}</h3><p>${{l.allTaxonomiesDescription}}</p></div>
            <div><h3>${{l.researchLimitations}}</h3><p>${{l.categorySpecificLimitations}}</p></div>
          </div>
          <div class="paper-list">${{visibleCards}}</div>${{extra}}
        </div>
      </details>`;
    }}
    function renderTaxonomy(rows) {{
      if (!rows.length) {{
        taxonomy.innerHTML = `<div class="empty">${{t('noPapers')}}</div>`;
        return;
      }}
      const l = labels[state.lang] || labels.en;
      const byCategory = new Map();
      for (const category of CATEGORIES) byCategory.set(category.name, []);
      for (const row of rows) byCategory.get(row.category)?.push(row);
      const categoryDetails = CATEGORIES.map(category => {{
        const catRows = (byCategory.get(category.name) || []).sort((a, b) => b.citationCount - a.citationCount);
        if (!catRows.length) return '';
        const years = catRows.map(p => p.year);
        const citations = catRows.reduce((sum, p) => sum + p.citationCount, 0);
        const top = catRows[0];
        const visibleCards = catRows.slice(0, 120).map(paperCard).join('');
        const extra = catRows.length > 120 ? `<p class="meta">${{l.showing}} 120 ${{l.of}} ${{fmt(catRows.length)}} ${{l.matchingPapers}}. ${{l.completeSet}}</p>` : '';
        return `<details>
          <summary><div class="summary-row">
            <img src="${{category.icon}}" alt="">
            <div><h3>${{category.name}}</h3><div class="meta">${{l.topPaper}}: <a href="${{top.url}}">${{top.title}}</a></div></div>
            <div class="summary-metric"><strong>${{fmt(catRows.length)}}</strong>${{l.papers}}</div>
            <div class="summary-metric"><strong>${{Math.min(...years)}}-${{Math.max(...years)}}</strong>${{l.years}}</div>
            <div class="summary-metric"><strong>${{fmt(citations)}}</strong>${{l.citations}}</div>
          </div></summary>
          <div class="section-body">
            <div class="section-grid">
              <div><h3>${{l.overview}}</h3><ul>${{listItems(localizedCategoryList(category, 'overview'))}}</ul></div>
              <div><h3>${{l.researchLimitations}}</h3><ul>${{listItems(localizedCategoryList(category, 'limitations'))}}</ul></div>
            </div>
            <div class="paper-list">${{visibleCards}}</div>${{extra}}
          </div>
        </details>`;
      }}).join('');
      taxonomy.innerHTML = allTaxonomiesDetails(rows) + categoryDetails;
    }}
    function render() {{
      if (state.start > state.end) [state.start, state.end] = [state.end, state.start];
      startSelect.value = state.start;
      endSelect.value = state.end;
      const rows = filtered();
      renderStats(rows);
      renderResearchCopy();
      renderKeywords(rows);
      renderCharts(rows);
      renderTaxonomy(rows);
    }}
    presetSelect.addEventListener('change', () => {{
      const [start, end] = presetSelect.value.split('-').map(Number);
      state.start = start; state.end = end; render();
    }});
    startSelect.addEventListener('change', () => {{ state.start = Number(startSelect.value); render(); }});
    endSelect.addEventListener('change', () => {{ state.end = Number(endSelect.value); render(); }});
    languageSelect.addEventListener('change', () => {{ state.lang = languageSelect.value; render(); }});
    document.getElementById('reset').addEventListener('click', () => {{
      state.start = START_YEAR; state.end = END_YEAR; state.keyword = null; state.lang = 'en';
      presetSelect.value = `${{START_YEAR}}-${{END_YEAR}}`;
      languageSelect.value = 'en';
      render();
    }});
    fillYears();
    render();
    fetch(OVERALL_ANALYSIS_URL)
      .then(response => response.json())
      .then(data => {{ overallAnalysis = data; render(); }})
      .catch(() => {{}});
  </script>
</body>
</html>
"""
    (DOCS_DIR / "index.html").write_text(index, encoding="utf-8")


def reference_line(row):
    return f"{row['authors']}. ({row['year']}). {row['title']}. {row['venue']}. {row['url']}"


def review_sections(selected, korean=False):
    counts, _ = category_stats(selected)
    stats = year_stats(selected)
    total_citations = sum(row["citationCount"] for row in selected)
    leading_category, leading_count = counts.most_common(1)[0]
    peak_year = max(stats, key=lambda year: stats[year]["citations"]) if stats else START_YEAR
    top_cited = sorted(selected, key=lambda row: row["citationCount"], reverse=True)[:15]
    if korean:
        title = f"{YEAR_RANGE_TEXT} brain ?곌뎄 ?숉뼢: 怨듦컻 硫뷀??곗씠??湲곕컲 ?몄슜???먮젅?댁뀡"
        abstract = f"??由щ럭 珥덉븞? Semantic Scholar 怨듦컻 硫뷀??곗씠?곗뿉??{START_YEAR}?꾨???{END_YEAR}?꾧퉴吏 brain 愿???꾨낫 ?쇰Ц???곕룄蹂?理쒕? {CANDIDATES_PER_YEAR:,}??議곗궗?섍퀬, 媛??곕룄 ?몄슜 ?곸쐞 {TARGET_PER_YEAR}?몄쓣 ?좎젙??寃곌낵瑜??붿빟?쒕떎. 理쒖쥌 紐⑸줉? {len(selected):,}?몄씠硫? ?좉꼍?곸긽, ?꾧린?앸━, ?명룷/遺꾩옄 ?좉꼍怨쇳븰, ?몄?/?쒖뒪???좉꼍怨쇳븰, ?꾩긽 ?좉꼍?? 諛쒕떖/?곌껐泥? ?좉꼍湲곗닠, 怨꾩궛 ?좉꼍怨쇳븰, ?뚰삁愿/?먯긽, ?쇰컲 由щ럭 遺꾨쪟濡??뺣━?덈떎."
        findings = [
            f"?좎젙 ?쇰Ц? 珥?{total_citations:,}?뚯쓽 ?몄슜???ы븿?섎ŉ, ?좏깮 吏묓빀?먯꽌 ?몄슜?됱씠 媛?????곕룄??{peak_year}?꾩씠??",
            f"媛????遺꾨쪟??{leading_category}({leading_count:,}???대떎.",
            "MRI, fMRI, EEG, MEG, ECoG, single-cell, human, non-human ?깆쓽 ?ㅼ썙???쒓렇??諛⑸쾿怨????異뺤쓣 鍮좊Ⅴ寃??꾪꽣留곹븯湲??꾪빐 遺?ы뻽??",
            "??寃곌낵??PDF ?꾨Ц ?ъ궗??泥닿퀎??臾명뿄怨좎같???꾨땲??硫뷀??곗씠??湲곕컲 吏?꾩씠誘濡? ?댁꽍?먮뒗 ?꾩냽 ?꾨Ц媛 寃?좉? ?꾩슂?섎떎.",
        ]
        future = [
            "?좎젙 ?쇰Ц???꾨Ц???쎄퀬 ?곌뎄 ?ㅺ퀎, ?쒕낯 ?? ?ы쁽?? 怨듦컻 ?곗씠???щ?瑜?蹂꾨룄 肄붾뵫?쒕떎.",
            "?꾩긽 以묎컻, ?κ린 ?덉젙?? ?덉쟾?? ?ㅻ━, 媛쒖씤?뺣낫 蹂댄샇 ??ぉ???뺤옣 taxonomy濡?異붽??쒕떎.",
            "理쒓렐 ?곕룄 ?쇰Ц? ?몄슜 異뺤쟻 ?쒓컙??吏㏃쑝誘濡??꾨Ц媛 異붿쿇?대굹 理쒖떊??蹂댁젙 ?먯닔瑜?蹂묓뻾?쒕떎.",
        ]
        labels = {
            "abstract": "珥덈줉",
            "findings": "?듭떖 諛쒓껄",
            "taxonomy": "遺꾨쪟蹂??댁꽍",
            "future": "?ν썑 ?곌뎄 怨쇱젣",
            "refs": "?좎젙 李멸퀬臾명뿄",
            "top": "?몄슜 ?곸쐞 ?쇰Ц",
        }
    else:
        title = f"Brain Research from {START_YEAR} to {END_YEAR}: A Metadata-Driven Review"
        abstract = f"This draft review maps research on the relationship between brain structure and AI from {START_YEAR} through {END_YEAR}, re-scoring up to {CANDIDATES_PER_YEAR:,} public Semantic Scholar candidate papers per year for structural brain signals and AI/modeling relevance before selecting {TARGET_PER_YEAR} papers per year by citation count. The final {len(selected):,} selected papers are organized into neuroimaging AI, connectomics and graph models, decoding and BCI, computational neuroscience and brain-inspired AI, cellular and neuromorphic foundations, cognitive architectures, clinical NeuroAI, electrophysiology decoding, and broad reviews."
        findings = [
            f"The selected papers account for {total_citations:,} citations in the selected set, with the largest citation mass in {peak_year}.",
            f"The largest taxonomy category is {leading_category} ({leading_count:,} papers).",
            "Keyword filters expose method and population axes such as MRI, fMRI, EEG, MEG, ECoG, single-cell, human, and non-human.",
            "The result is a metadata-driven map rather than a PDF-level systematic review, so expert appraisal remains necessary before strong field-level claims.",
        ]
        future = [
            "Add full-text appraisal for study design, sample size, reproducibility, data availability, and code release.",
            "Extend the taxonomy with clinical translation, long-term stability, safety, neuroethics, and privacy criteria.",
            "Use expert review or recency-aware scoring to compensate for structurally low citation counts in recent years.",
        ]
        labels = {
            "abstract": "Abstract",
            "findings": "Key Findings",
            "taxonomy": "Category-Level Interpretation",
            "future": "Future Research Agenda",
            "refs": "Selected References",
            "top": "Top Papers by Citation Count",
        }
    category_lines = [f"{cat}: {count:,} papers ({count / len(selected):.1%})" for cat, count in counts.most_common()]
    refs = [reference_line(row) for row in top_cited]
    return title, abstract, findings, category_lines, future, refs, labels, top_cited


def html_ranked_table(rows):
    out = ["<table>", "<thead><tr><th>Year</th><th>Rank</th><th>Paper</th><th>Citations</th><th>Category</th></tr></thead>", "<tbody>"]
    for row in rows:
        out.append(
            f"<tr><td>{row['year']}</td><td>{row['rank']}</td><td><a href=\"{html_escape(row['url'])}\">{html_escape(row['title'])}</a></td><td>{row['citationCount']:,}</td><td>{html_escape(row['category'])}</td></tr>"
        )
    out.extend(["</tbody>", "</table>"])
    return "\n".join(out)


def write_review_html(selected, korean=False):
    title, abstract, findings, category_lines, future, refs, labels, top_cited = review_sections(selected, korean=korean)
    lang = "ko" if korean else "en"
    doc = f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html_escape(title)}</title>
  <style>
    body {{ font-family: Georgia, "Noto Serif KR", serif; max-width: 920px; margin: 40px auto; padding: 0 22px; line-height: 1.72; color:#172033; }}
    h1 {{ line-height:1.15; }}
    h2 {{ margin-top: 34px; }}
    li {{ margin: 6px 0; }}
    .abstract {{ background:#f5f7fb; border-left:4px solid #2563eb; padding:14px 18px; }}
    table {{ width:100%; border-collapse:collapse; margin:16px 0; }}
    th,td {{ border-bottom:1px solid #d9dee8; padding:8px; vertical-align:top; text-align:left; }}
    th {{ background:#f4f6fa; }}
  </style>
</head>
<body>
  <h1>{html_escape(title)}</h1>
  <p><strong>Generated:</strong> {GENERATED_DATE} &middot; <strong>Dataset:</strong> {len(selected):,} papers</p>
  <h2>{labels['abstract']}</h2>
  <p class="abstract">{html_escape(abstract)}</p>
  <h2>{labels['findings']}</h2>
  <ul>{''.join(f'<li>{html_escape(item)}</li>' for item in findings)}</ul>
  <h2>{labels['taxonomy']}</h2>
  <ul>{''.join(f'<li>{html_escape(item)}</li>' for item in category_lines)}</ul>
  <h2>{labels['top']}</h2>
  {html_ranked_table(top_cited)}
  <h2>{labels['future']}</h2>
  <ul>{''.join(f'<li>{html_escape(item)}</li>' for item in future)}</ul>
  <h2>{labels['refs']}</h2>
  <ol>{''.join(f'<li>{html_escape(ref)}</li>' for ref in refs)}</ol>
</body>
</html>
"""
    filename = "review_ko.html" if korean else "review_en.html"
    (PAPER_DIR / filename).write_text(doc, encoding="utf-8")


def write_review_docx(selected):
    if Document is None:
        (PAPER_DIR / "review_en.docx.txt").write_text("python-docx is not installed; review_en.docx was not generated.\n", encoding="utf-8")
        return
    title, abstract, findings, category_lines, future, refs, labels, top_cited = review_sections(selected, korean=False)
    document = Document()
    document.add_heading(title, level=0)
    document.add_paragraph(f"Generated: {GENERATED_DATE} | Dataset: {len(selected):,} papers")
    document.add_heading(labels["abstract"], level=1)
    document.add_paragraph(abstract)
    document.add_heading(labels["findings"], level=1)
    for item in findings:
        document.add_paragraph(item, style="List Bullet")
    document.add_heading(labels["taxonomy"], level=1)
    for item in category_lines:
        document.add_paragraph(item, style="List Bullet")
    document.add_heading(labels["top"], level=1)
    for row in top_cited:
        document.add_paragraph(f"{row['year']} #{row['rank']}: {row['title']} ({row['citationCount']:,} citations)", style="List Number")
    document.add_heading(labels["future"], level=1)
    for item in future:
        document.add_paragraph(item, style="List Bullet")
    document.add_heading(labels["refs"], level=1)
    for ref in refs:
        document.add_paragraph(ref, style="List Number")
    document.save(PAPER_DIR / "review_en.docx")


def write_curation_method():
    markdown = f"""# Awesome Brain AI Curation Method

Generated: {GENERATED_DATE}

## Scope

- Topic: relationship between brain structure and AI
- Years: {START_YEAR}-{END_YEAR}
- Candidate target: up to {CANDIDATES_PER_YEAR:,} papers per year
- Selection target: {TARGET_PER_YEAR} papers per year
- Ranking: citation count descending, using Semantic Scholar `citationCount`
- Metadata source: Semantic Scholar Academic Graph bulk search, free public metadata

## Query

For each year, the pipeline starts from broad brain/neuroscience Semantic Scholar candidate metadata, then re-scores records for both brain-structure evidence and AI, machine-learning, computational modeling, graph, decoding, neuromorphic, BCI, or brain-inspired signals. Final yearly selections are citation-ranked within the eligible brain-AI relation pool.

For early years where public metadata contains fewer than the requested target, the generated datasets keep the full audited pool and select all available citation-ranked records rather than fabricating missing entries.

## Enrichment

The script deterministically assigns taxonomy categories, keyword convention tags, key ideas, strengths, and research-focused limitations. No paid API, paid LLM, paid translation service, or paid compute is used.

## GitHub-Awesome Skill2 and Paper-Curation Provenance

This regeneration follows `github-awesome-skill2` in metadata-adapter mode for a large citation-ranked awesome repository while preserving the selected paper set in `data/{PAPERS_CSV}`. The workflow inspected the local `jehyunlee/paper-curation` checkout and is configured for Zotero-free folder-source PDF staging under `E:\\議곗꽑?\\?곌뎄\\paper-curation\\paper\\awesome-brain-ai`. Full PDF LLM review stages from paper-curation were not run because they require explicit approval for paid or metered APIs.

## Verification Targets

The repository should contain selected and candidate CSV/JSON data, `README.md`, `README.html`, `docs/index.html`, period analysis JSON, taxonomy SVG assets, and English/Korean review HTML files.
"""
    (PAPER_DIR / "curation_method.md").write_text(markdown, encoding="utf-8")
    (PAPER_DIR / "curation_method.html").write_text(markdown_to_html_doc("Awesome Brain AI Curation Method", markdown), encoding="utf-8")


def write_skill2_provenance(selected, candidates):
    folder_source_pdf_dir = Path(r"E:\議곗꽑?\?곌뎄\paper-curation\paper\awesome-brain-ai")
    manifest_path = folder_source_pdf_dir / "_folder_source_manifest.json"
    failures_path = folder_source_pdf_dir / "_folder_source_failures.json"
    manifest_count = 0
    failure_count = 0
    if manifest_path.exists():
        manifest_count = len(json.loads(manifest_path.read_text(encoding="utf-8")))
    if failures_path.exists():
        failure_count = len(json.loads(failures_path.read_text(encoding="utf-8")))
    payload = {
        "skill": "github-awesome-skill2",
        "mode": "metadata-adapter",
        "paper_curation_source": "E:\\議곗꽑?\\?곌뎄\\paper-curation",
        "zotero_used": False,
        "paid_or_metered_api_used": False,
        "folder_source_pdf_dir": str(folder_source_pdf_dir),
        "folder_source_manifest": str(manifest_path),
        "folder_source_manifest_pdfs": manifest_count,
        "folder_source_failed_records": failure_count,
        "selected_dataset": f"data/{PAPERS_CSV}",
        "candidate_dataset": f"data/{CANDIDATES_CSV}",
        "selected_papers": len(selected),
        "candidate_records": len(candidates),
        "period": YEAR_RANGE_TEXT,
        "candidate_target_per_year": CANDIDATES_PER_YEAR,
        "selection_target_per_year": TARGET_PER_YEAR,
        "ranking": "citationCount descending with influentialCitationCount and metadata importance score retained as audit signals",
        "note": "The repository/site outputs are deterministic metadata curation artifacts; full PDF LLM reviews require separate explicit approval.",
    }
    (DATA_DIR / SKILL2_PROVENANCE_JSON).write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def write_citation_and_license():
    citation = f"""cff-version: 1.2.0
title: Awesome Brain AI
message: If you use this metadata curation, please cite the repository and the original papers.
type: dataset
authors:
  - family-names: Hong
    given-names: Gi
repository-code: https://github.com/honggi82/awesome-brain-ai
url: https://honggi82.github.io/awesome-brain-ai/
date-released: "{GENERATED_DATE}"
license: CC-BY-4.0
"""
    (ROOT / "CITATION.cff").write_text(citation, encoding="utf-8")
    (ROOT / "LICENSE").write_text("CC-BY-4.0 for text and metadata curation; upstream paper metadata belongs to original sources.\n", encoding="utf-8")
    (ROOT / ".gitignore").write_text("__pycache__/\n*.pyc\n.DS_Store\ndata/cache/\n", encoding="utf-8")
    publish = """@echo off
echo This repository is generated locally. Create https://github.com/honggi82/awesome-brain-ai, then run:
echo git remote add origin https://github.com/honggi82/awesome-brain-ai.git
echo git push -u origin main
"""
    (ROOT / "publish_to_github.bat").write_text(publish, encoding="utf-8")


def copy_docs_data():
    for filename in [PAPERS_CSV, PAPERS_JSON, CANDIDATES_CSV, CANDIDATES_JSON, TAXONOMY_CSV, PERIOD_ANALYSIS_JSON, OVERALL_ANALYSIS_JSON, SKILL2_PROVENANCE_JSON]:
        shutil.copyfile(DATA_DIR / filename, DOCS_DIR / "data" / filename)
    if (DATA_DIR / GITHUB_LINKS_JSON).exists():
        shutil.copyfile(DATA_DIR / GITHUB_LINKS_JSON, DOCS_DIR / "data" / GITHUB_LINKS_JSON)
    if (DATA_DIR / LINK_AUDIT_JSON).exists():
        shutil.copyfile(DATA_DIR / LINK_AUDIT_JSON, DOCS_DIR / "data" / LINK_AUDIT_JSON)
    shutil.copyfile(PAPER_DIR / "review_en.html", DOCS_DIR / "paper" / "review_en.html")
    shutil.copyfile(PAPER_DIR / "review_ko.html", DOCS_DIR / "paper" / "review_ko.html")
    shutil.copyfile(PAPER_DIR / "curation_method.html", DOCS_DIR / "paper" / "curation_method.html")


def main():
    refresh = "--refresh" in __import__("sys").argv
    ensure_dirs()
    selected, candidates = collect_papers(refresh=refresh)
    write_json_csv(selected, candidates)
    write_taxonomy_dataset(selected)
    write_period_analysis(selected)
    write_overall_analysis(selected)
    write_taxonomy_assets()
    write_readme(selected, candidates)
    write_site(selected)
    write_review_html(selected, korean=False)
    write_review_html(selected, korean=True)
    write_review_docx(selected)
    write_curation_method()
    write_skill2_provenance(selected, candidates)
    write_citation_and_license()
    copy_docs_data()
    print(f"[done] generated {len(selected):,} selected papers from {len(candidates):,} candidates", flush=True)


if __name__ == "__main__":
    main()


