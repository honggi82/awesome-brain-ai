### REVIEW ARTICLE

published: 12 March 2013 doi: 10.3389/fnins.2013.00031

# A hitchhiker’s guide to diffusion tensor imaging

## José M. Soares1,2*, Paulo Marques1,2,3, Victor Alves3 and Nuno Sousa1,2

- 1 Life and Health Science Research Institute (ICVS), School of Health Sciences, University of Minho, Braga, Portugal
- 2 ICVS/3B’s - PT Government Associate Laboratory, Braga/Guimarães, Portugal
- 3 Department of Informatics, University of Minho, Braga, Portugal

Edited by: Arno Klein, Cornell Medical School, USA

Reviewed by: Arno Klein, Cornell Medical School, USA Eleftherios Garyfallidis, University of Cambridge, UK Mahshid Farzinfar, University of North Carolina at Chapel Hill, USA

*Correspondence: José M. Soares, Life and Health Science Research Institute (ICVS), School of Health Sciences, University of Minho, Campus Gualtar, 4710-057 Braga, Portugal. e-mail: josesoares@ecsaude. uminho.pt

Diffusion Tensor Imaging (DTI) studies are increasingly popular among clinicians and researchers as they provide unique insights into brain network connectivity. However, in order to optimize the use of DTI, several technical and methodological aspects must be factored in. These include decisions on: acquisition protocol, artifact handling, data quality control, reconstruction algorithm, and visualization approaches, and quantitative analysis methodology. Furthermore, the researcher and/or clinician also needs to take into account and decide on the most suited software tool(s) for each stage of the DTI analysis pipeline. Herein, we provide a straightforward hitchhiker’s guide, covering all of the workﬂow’s major stages. Ultimately, this guide will help newcomers navigate the most critical roadblocks in the analysis and further encourage the use of DTI.

Keywords: diffusion tensor imaging, hitchhiker’s guide, acquisition, analysis, processing

## INTRODUCTION

Diffusion-Weighted Imaging (DWI) (Le Bihan and Breton, 1985; Merboldt et al., 1985; Taylor and Bushell, 1985; Le Bihan et al., 1986) is a variant of conventional Magnetic Resonance Imaging based on the tissue water diffusion rate. It is a non-invasive method, with unparalleled sensitivity to water movements within the architecture of the tissues that uses existing MRI technology and requires no new equipment, contrast agents, or chemical tracers. The introduction of the diffusion tensor model enabled the indirect measurement of the degree of anisotropy and structural orientation that characterizes diffusion tensor imaging (DTI) (Basser et al., 1994a,b; Pierpaoli et al., 1996). While DWI refers to the contrast of the acquired images, DTI is a speciﬁc type of modeling of the DWI datasets. DTI principles and basic concepts have been extensively described and reviewed in the literature (Mori and Barker, 1999; Le Bihan et al., 2001; Hagmann et al., 2006; Mori and Zhang, 2006; Mori,

- 2007; Nucifora et al., 2007; Assaf and Pasternak, 2008; Jones, 2008, 2010b; Mukherjee et al., 2008a; Johansen-Berg and Behrens, 2009; Figueiredo et al., 2011; Thomason and Thompson, 2011; Tournier et al., 2011; Yang et al., 2011). Summarily, the basic concept behind DTI is that water molecules diffuse differently along the tissues depending on its type, integrity, architecture, and presence of barriers, giving information about its orientation and quantitative anisotropy (Chenevert et al., 1990; Moseley

- et al., 1990; Douek et al., 1991; Beaulieu, 2002). With DTI analysis it is possible to infer, in each voxel, properties such as the molecular diffusion rate [Mean Diffusivity (MD) or Apparent Diffusion Coefﬁcient (ADC)], the directional preference of diffusion [Fractional Anisotropy (FA)], the axial (diffusion rate along the main axis of diffusion), and radial (rate of diffusion in the transverse direction) diffusivity. Diffusion in White Matter (WM)

is less restricted along the axon and tends to be anisotropic (directionally-dependent) whereas in Gray Matter (GM) is usually less anisotropic and in the Cerebrospinal ﬂuid (CSF) is unrestricted in all directions (isotropic) (Pierpaoli et al., 1996; Song et al., 2002; Hagmann et al., 2006). Based on this assumption, Basser and colleagues (1994a,b) modeled the diffusion process by an ellipsoid, which can mathematically be represented by a 3 × 3 symmetric matrix, also known as tensor (hence DTI’s name origin).

Gaining increased popularity among clinicians and researchers, DTI is presently a promising tool for studying WM architecture in living humans, both in healthy conditions and in disease. However, it has a complex workﬂow (summarized in Figure 1) that implicates knowledge of imaging artifacts, complex MRI protocol deﬁnition, neuroanatomical complexity, and intrinsic technique limitations. These factors are compounded by a multitude of preprocessing and analysis methods in several software packages. Several papers and books describing the main technical issues and pitfalls related to DTI studies have been published (Basser and Jones, 2002; Moritani et al., 2005; Le Bihan et al., 2006; Mukherjee et al., 2008b; Bammer et al., 2009; Jones, 2010a,b,c; Jones and Cercignani, 2010; Chung et al., 2011; Hasan et al., 2011) which are complemented by available neuroanatomical WM atlas (Jellison et al., 2004; Wakana et al., 2004; Catani and Thiebaut De Schotten, 2008; Lawes et al., 2008; Oishi et al., 2008, 2010; Zhang et al., 2010; Bazin et al., 2011; Nowinski et al., 2012). However, given the constant methodological advances and the increase in DTI applicability across clinical and research domains, we have here compiled a practical hitchhiker’s guide of critical information and main references to consider in setting up DTI studies, optimizing data quality, and interpreting results.

[Figure 1]

[Figure 2]

[Figure 3]

[Figure 4]

resulting data can be visualized as glyphs (G), scalar indices such as colored FA (H), FA (I), and MD (J) or as tractography (K). ROI (L), histogram (M), VBA (N), or TBSS (O) analyses may be performed and the results can be incorporated with fMRI (P) or structural MRI (Q) in multimodal analysis. Finally, results interpretation should be made with extreme caution.

FIGURE 1 | Typical DTI workﬂow. In order to perform a DTI study, researchers need to understand its main application ﬁelds, recognize the main artifacts (A) and what acquisition protocols can be used (B). The data should undergo quality control, preprocessing, including format conversion (C), distortions and motion correction (D), and skull stripping (E). Before further analysis, tensors need to be estimated (F) and the

[Figure 5]

## APPLICATION FIELDS

DTI is sensitive to microstructural tissue properties and, thus, it can be used in WM research and clinical work to explore WM anatomy and structure in vivo. In fact, this sensitivity, providing diffusion summary measures and tissue ﬁber orientation, has made DTI widely used as a clinical tool, especially in conditions where abnormalities in WM are expected (Sundgren et al., 2004; Mori and Zhang, 2006). For example, it has been successfully implemented to study patients with acute stroke or brain tumors; neurodegenerative disorders including multiple sclerosis, epilepsy, and Alzheimer’s; neuropsychiatric disorders such as schizophrenia; mild cognitive impairment; development disorders like dyslexia, autism, and attention deﬁcit hyperactivity disorder; movement disorders (mainly Parkinson’s and Huntington’s); neurogenetic developmental disorders such as Williams syndrome and fragile X syndrome; and changes in WM microstructure during neurodevelopment and in aging (Le Bihan et al., 2001; Moseley et al., 2002; Sundgren et al., 2004; Vilanova et al., 2006; Nucifora et al., 2007; Ciccarelli et al., 2008; Imfeld et al., 2009; Johansen-Berg and Behrens, 2009; Madden et al., 2009; Yamada et al., 2009; Chanraud et al., 2010; Carvalho Rangel et al., 2011; Fung et al., 2011; Hygino da Cruz Jr et al., 2011; Thomason and Thompson, 2011; Voineskos et al., 2012). DTI variables (e.g., FA, axial diffusivity) are usually related with alterations in structure (possibly due to particular conditions/disease) pointing to speciﬁc myelination levels and axonal injury (Song et al., 2002; White et al.,

- 2008; Budde et al., 2009; Gupta et al., 2012). With the progressive increase in the range of applications, consistency of results and robustness of the technique, DTI is expected to be valuable in the future in disease treatment planning, detection of preclinical markers, and microstructural abnormalities; it is also anticipated that the structural-functional correlates provided by DTI studies will become part of the clinic’s imaging routine.

## ARTIFACTS AND DATA ACQUISITION TECHNIQUES

Implementing DTI studies involves the understanding of speciﬁc MRI acquisition techniques and artifacts, and how to deal with them (Figures 1A,B). The artifacts in DWI datasets are mainly related with the gradient system hardware, pulse sequence, acquisition strategy used and motion. DWI data are generally collected to cover the entire brain by repeating the acquisition while varying the orientation or magnitude of the diffusion gradients. DWI has low Signal-to-Noise Ratio (SNR) and resolution and is very susceptible to motion (Farrell et al., 2007; Choi et al., 2011; Polders et al., 2011). To reduce the inﬂuence of motion artifacts, the scan time can be reduced. This makes the use of Singleshot Echo Planar Imaging (EPI) (Mansﬁeld, 1977; Stehling et al., 1991; Turner et al., 1991; Nana et al., 2008) the typical strategy employed to reduce this sensitivity (Stehling et al., 1991; Turner

- et al., 1991; Nana et al., 2008); however, alternative sequences, such as Fast Spin Echo (FSE) (Seifert et al., 2000; Pipe et al., 2002), Line Scan Diffusion Imaging (LSDI), (Gudbjartsson et al., 1996) and Stimulated Echo Acquisition Mode (STEAM) (Nolte et al.,

2000) may also be of interest to reduce artifacts (Xu et al., 2004; Mukherjee et al., 2008b; Bammer et al., 2009).

Besides being the most common approach, EPI images are very sensitive to other artifacts related with EPI characteristics such as ﬁeld inhomogeneities at B0 (especially at higher ﬁelds), image blurring [also called Point-Spread Function (PSF) artifact], limited resolution from T2 and T2∗ signal decay during the signal readout; with diffusion MRI properties such as eddy current-induced distortions and general MRI issues like sensitivity to motion and B0-susceptibility artifacts (Farzaneh et al., 1990; Basser and Jones, 2002; Le Bihan et al., 2006; Kaur et al., 2007; Bammer et al., 2009; Jones and Cercignani, 2010). Shorter readout times can reduce the echo train and increase SNR, resulting in a lower sensitivity to motion and reduced susceptibility to geometric artifacts and blurring (Mukherjee et al.,

- 2008b). This decrease in the readout times can be achieved with the use of phased-array head coils, enabling parallel imaging such as Sensitivity Encoding (SENSE), Array Spatial Sensitivity Encoding Technique (ASSET), and Generalized Autocalibrating Partially Parallel Acquisition (GRAPPA) (Pruessmann et al., 1999; Bammer et al., 2002; Griswold et al., 2002; Jaermann et al., 2006; Brau et al., 2008; Nana et al., 2008; Holdsworth et al.,
- 2009). Parallel imaging is important at 3T, and essential at 7T (Mukherjee et al., 2008c).

Importantly, the two main artifacts intrinsic to DTI acquisitions that may destroy the voxel-wise correspondence across all the DWIs are eddy current distortions and head motion (Rohde et al., 2004; Le Bihan et al., 2006; Mohammadi et al., 2010). In DTI, contrary to most imaging acquisitions, the gradients are much longer (rising and falling edges of the gradient are separated in time); there might be perturbations of the local magnetic ﬁeld that result in current inductions in the diverse conducting surfaces of the MRI scanner causing image distortions (contraction and/or overall shift and shear) that are usually easy to detect visually. Eddy currents vary with the diffusion gradient applied and, consequently, there will be misregistration between successive images, which are worse with stronger and longer gradient pulses. Some strategies have been used to prevent and correct eddy current distortions, based on a twice-refocused spin echo pulse, bipolar gradients, ﬁeld maps, and preprocessing approaches(described later); it is important to note, however,that there are pitfalls associated with these strategies (Reese et al.,2003; Chen et al., 2006; Zhuang et al., 2006; Huang et al., 2008; Truong et al., 2008, 2011; Jones and Cercignani, 2010).

Diffusion MRI is very sensitive to motion, due to phase shifts induced microscopically by diffusion-driven water molecular displacements, and macroscopically by head motion, cardiac pulsation and breathing. This sensitivity increases with the intensity and duration of gradient pulses, which are characterized by the b-value, the scalar that deﬁnes the amount of diffusion weighting in the experiment (Le Bihan et al., 2001). It can be reduced by synchronizing the acquisition with the source of motion, monitoring using “navigator echoes,” using speciﬁc protocols, applying realtime prospective motion and outlier detection methods; however, all of these may raise other problems such as increased acquisition times (Ordidge et al., 1994; Pipe, 1999; Kennedy and Zhong, 2004; Zwiers, 2010; Zhou et al., 2011b; Kober et al., 2012; Ling et al., 2012). Even though it is also possible, and even advisable, to correct subject motion using preprocessing techniques

(see in preprocessing steps below), the best approach is still to use comfortable padding to adjust the participant’s head, and to inform the subject in advance about the noise and the vibration of the bed. This vibration was recently reported as the cause of another artifact, known as vibration artifact. During the acquisition, strong gradients are applied causing low-frequency mechanical resonances of the MR system that lead to small brain tissue movements. When these movements occur in the direction of the diffusion-encoding gradient, phase offsets will occur inducing signal dropouts in DWI images. This kind of artifacts can be reduced increasing TR (with the drawback of reducing SNR) or using full k-space coverage combined with parallel imaging (e.g., GRAPPA) (Gallichan et al., 2010). It can also be compensated using methods such as phase-encoding reversal (COVIPER) (Mohammadi et al., 2012), implemented in Artifact Correction in Diffusion MRI (ACID) toolbox.

Whenever artifacts can’t be corrected, such as severe movement, signal dropouts, or slice-wise intensity disruption, researchers adopt different strategies depending on the type and extent of the artifact. The exclusion of the affected subject, volume (gradient) or single slice is a common approach. An alternative is to limit the analysis to regions without artifacts if the artifact is localized (Liu et al., 2010b).

Artifacts in DWI acquisitions lead to errors in tensor estimation and, consequently, in diffusion maps (FA and MD) that give rise to ﬁber reconstructions with erroneous orientation or length. Optimizing diffusion-imaging sequences is, thus, crucial to obtain more precise data. Protocols should be oriented to the question under study, and speciﬁc parameters should be used to optimize a particular analysis. There is no consensus on the optimal acquisition parameters because they vary according to MRI hardware conﬁguration, ﬁeld strength, vendor, scanning time available, speciﬁc anatomic structure and brain anatomic coverage needed. Thus, herein we only provide a suggestion for parameters in a typical DTI acquisition mostly based on a previous technical review (Mukherjee et al., 2008b). Usually, DWI data are acquired covering the entire brain through axial slices with no gap between slices (crucial for tractography). On modern scanners, 5min scanning time is enough to perform an acceptable acquisition; however, the acquisition time may be much longer (15min) depending on the scanner and the acquisition parameters deﬁned. Diffusion tensor estimation requires high b-values (e.g., 1000s/mm2) along at least six non-collinear diffusion encoding directions in addition to one minimally T2 weighted low b-image (b = 0s/mm2). Several sampling schemes have been suggested and it is argued that the sampling vectors should be uniformly distributed in space so that the SNR is also uniform in respect to the tensor orientation. The usage of 30 diffusion-encoded images (orientations) was found to be a good compromise between image quality and scanning time, since increasing the number of orientations didn’t result in improved tensor orientation and MD estimates (Jones, 2004). Ideally, 1 low-b image for each 5–10 high-b images should be acquired. Another approach is to repeat acquisition of the same DWIs [increasing the Number of Excitations (NEX)] instead of raising the number of DWIs (Wang et al., 2011). Most DTI studies use high b-values in the range of 700–1000s/mm2, and the

actual standard for clinical DWI is 1000s/mm2 (Mukherjee et al., 2008b). The magnitude of b-values is also dependent upon SNR, echo time, eddy currents, and motion artifacts and should, in speciﬁc cases, be adjusted to the population and speciﬁc structure. The rule is that the optimal b-value multiplied by the ADC value should be close to 1 (Xing et al., 1997; Jones et al., 1999a). The spatial resolution is also important for DTI quality and when using isotropic voxels (in-plane resolution and thickness with equal dimensions, e.g., 2 × 2 × 2); typically, 2–2.5mm are recommended for ﬁber tracking, using interleaved acquisitions to minimize crosstalk between contiguous sections. Anisotropic voxels also introduce bias in the quantitative assessment of ﬁber orientation and anisotropy and larger voxels are more likely to have more than one ﬁber tract orientation (Mukherjee et al., 2008b). Other characteristic parameters of DTI acquisitions are Field Of View (FOV) usually ranging from 240 to 256mm, acquisition matrix 96 × 96–128 × 128, Echo Time (TE) 50–70ms and Repetition Time (TR) 8.5–12s. Optimization of DTI protocols has been the focus of diverse studies that specify metrics for detailed protocol deﬁnition, including its relation with the DTI metrics and multi-center approaches (Xing et al., 1997; Jones et al., 1999a; Pfefferbaum et al., 2003; Hagmann et al., 2006; Farrell et al., 2007; Wakana et al., 2007; Mukherjee et al., 2008b; Abe et al., 2010; Jones, 2010c; Lagana et al., 2010; Choi et al., 2011; Hasan et al., 2011; Zhu et al., 2011; Lebel et al., 2012).

## QUALITY CONTROL AND PREPROCESSING

Quality control and preprocessing procedures are key steps to detect andcorrect artifacts in DWI andto exclude those that could not be corrected, providing consistency to reliable tensor estimation. Although it is already possible to ﬁnd automated preprocessing pipelines (Liu et al., 2010b) (ColbyImaging, http://www. colbyimaging.com/wiki/neuroimaging/dti-preprocessing), there is no consensus over which workﬂow is ideal for DTI quality control or preprocessing. Herein we provide a guided approach, comprising standard methodology easy to perform and not extremely time consuming.

The ﬁrst step consists in, when importing the data, checking if all images have been imported and sorted correctly and if the different subjects, under the same study, have the same parameters. This can be performed with general-purpose image viewers such as Osirix, syngo FastView, MRIcro, or ImageJ (Rosset et al., 2004; Liao et al., 2008). After this initial examination, a visual inspection of the DWI data is recommended to detect potential artifacts. Looping through the raw images in different “orthogonal” views allows the identiﬁcation of geometric distortions, signal dropouts, subtle system drifts, and missing slices (Tournier et al., 2011). On the other hand, outlier detection methods provide automated approaches to identify corrupted images. Methods based on testing for ADC consistency (Jiang et al., 2009) and detection of spike noise (Chavez et al., 2009) have also been suggested. RESTORE is a commonly used tool to estimate tensors robustly, excluding potential outliers prior to tensor estimation (Chang et al., 2005). Monte Carlo simulated data have been used to study the effects of different sources/magnitudes of noise on DTI derived

measures (Pierpaoli et al., 1996; Basu et al., 2006) and also to validate methods such as RESTORE.

The acquired data may at this point need several preprocessing steps depending on the MRI scanner, acquisition parameters, image quality, software package used and study focus. In preprocessing, it is common to start by converting raw data into speciﬁc and adequate image formats (Figure 1C). With poor interoperability between DTI analysis tools and the lack of a standard DTI format (Patel et al., 2010), many software packages deﬁne their own data formats; for example, Neuroimaging Informatics Technology Initiative (NIfTI) and Analyze and Nearly Raw Raster Data (NRRD) are common data formats. File format converters such as MRIcro, dcm2nii, MRIConvert, NiBabel, and software package converters (e.g., AFNI, Freesurfer, SPM, Slicer) are commonly used to convert from the original DICOM format (Smith et al., 2004; Pieper et al., 2006; Friston et al., 2007; Fischl, 2012).

In DWI images, distortions caused by eddy currents and head motion are the most common artifacts (Figure 1D); therefore, a common and recommended preprocessing step is to correct for such artifacts. Eddy currents can be corrected with an afﬁne registration to the b0 image and motion correction with a rigid body registration to b0. Since both corrections consist in registration procedures, they can be implemented as one single step. To do this, FMRIB’s Diffusion Toolbox (FDT), Automated Image Registration (AIR), and DT_Recon, are popular software tools, although tools like DTIC (b0 and eddy current correction for DTI) DTIPrep (Liu et al., 2010b), DIFF_PREP, and ExploreDTI (Leemans et al., 2009) can also be used for this purpose. It is important to note that since this procedure deals with changes in the orientation of the images, the encoding vectors should be reoriented (Leemans and Jones, 2009); fortunately, the DTIPrep, DIFF_PREP, and ExploreDTI tools take this into account.

After this, one optional step is to perform skull stripping (Figure 1E), removing non-brain areas from analysis, improving co-registration/normalization results and reducing data size. This step can be accomplished with several tools, such as BET from FSL, Freesurfer, Atropos, and Bioimage Suite. Accurate tensor estimation and tractography analysis are also dependent on precise gradient tables. Gradient information can usually be retrieved directly from the MRI console or it can be calculated with speciﬁc tools such as DTI gradient table creator. In some cases, the orientation of the gradient directions may be inaccurate and minor corrections may be required (ColbyImaging, http://www.colbyimaging.com/wiki/ neuroimaging/bvecs). After tensor estimation (described in the following sections), visual examination of tensor orientations in some speciﬁc regions (e.g., corpus callosum, cingulate and uncinate fasciculus) is also an assessment that can be performed with any tensor visualization tool (e.g., Slicer, TrackVis, DTIStudio, MedINRIA, BrainVoyager QX, FSL View, Camino, BioImage Suite, ExploreDTI). If tensor orientation errors are noticed it is necessary to modify the gradient table and repeat the tensor reconstruction (using tools such as DTI-TK). The presence of bias in DTI datasets is also common (Farrell et al., 2007) and it can originate from multiple sources (e.g., noise, ﬁeld inhomogeneities, quality control procedures that might

modify/exclude problematic gradients, and experimental and biological parameters); at this stage, it can be estimated with the SIMulation and EXtrapolation (SIMEX) statistical approach (Lauzon et al., 2011).

On a ﬁnal practical note, researchers or clinicians can search and compare existing software in listings such as the source for neuroimaging tools and resources (NITRC, http://www.nitrc. org/) or I Do Imaging (http://www.idoimaging.com/), particularly when searching for a tool for a speciﬁc task.

## PROCESSING AND VISUALIZATION

After data preprocessing, the next stage in DTI analysis comprises tensor estimation at each voxel (Figure 1F); for this purpose, images with diffusion-encoding gradients applied at least along six non-collinear directions are required. Three main methods are used to estimate the tensors: Ordinary Least Squares (OLS), the most popular, and Weighted Linear Least Squares (WLLS) and Non-linear Least Squares(NLLS). Different estimation methods may yield different results, therefore it is important to assure that the same package is used to estimate the tensors in an entire dataset (Koay et al., 2006; Jones and Cercignani, 2010). Since the diffusion tensor is a symmetric 3 × 3 matrix, it can be described by its eigenvalues (λ1, λ2, λ3) and eigenvectors (e1, e2, e3). The eigenvalues and eigenvectors are then used to process scalar indices and, in some studies, tractography analysis. At each voxel, the eigenvalues represent the magnitude of diffusion and the corresponding eigenvectors reﬂect the directions of maximal and minimal diffusion.

Nowadays, a wide range of free or commercial DTI software tools with different purposes and speciﬁcations are available. Choosing one among the others can be a difﬁcult and timeconsuming task for newcomers. In Table 1 we present a list of the most commonly used software tools and their main applicability.

Mainly used for clinical purposes, commercial applications although intuitive, friendly and automated, are also more rigid and limited. Examples of these are syngo DTI, Elite Neuro clinical solutions, or Functool and FiberTrak and others such as nordicICE Diffusion/DTI Module, iPlan® Fibertracking, Prism Clinical Imaging®, DynaSuite Neuro. On the other hand, Python based tools, especially the Nipy project (including tools such as Dipy, NiBabel, and Nipype) are more ﬂexible and customizable, but less intuitive and user friendly (Millman and Brett, 2007).

One of the biggest challenges in DTI is to visualize and present the tensor information in an intuitive and easily understandable way. In fact, the high dimensionality of the data and the complex associations in diffusion tensors domain make this step quite problematic. Typical approaches consist of using tensor glyphs or reducing the dimensionality to one scalar (scalar indices) and to three dimensions (tractography). Tools such as Explore DTI, MedINRIA, and Slicer, among many others, enable all the before mentioned visualization schemes, as summarized in Table 2.

2D visualization of scalar maps, the most common DTI visualization approach used by clinicians, is used due to its simplicity and instant visualization; however, this approach has limitations in the quantity of information presented. The two main diffusion indices, MDandFA, are based onthe eigenvalues, which represent the magnitude of the diffusion process.

- Table 1 | Software tools for DTI processing used in published studies.

[Figure 6]

DTI software/tools URL Main purpose

[Figure 7]

3D Slicer (Pieper et al., 2006) http://www.slicer.org/ Tensor estimation, ROI analysis, and tractography AFNI (Cox, 2012) http://afni.nimh.nih.gov/afni Preprocessing and tensor estimation BioImage Suite (Papademetris et al., 2005)

http://www.bioimagesuite.org/ Tensor estimation, ROI analysis, and tractography

BrainVoyager QX (Goebel, 2012) http://www.brainvoyager.com/ Tensor estimation and tractography Camino (Cook et al., 2006) http://web4.cs.ucl.ac.uk/research/medic/camino/pmwiki/

Tensor estimation and tractography

pmwiki.php?

Dipy (Garyfallidis et al., 2011) http://dipy.org Tensor estimation and tractography DoDTI (Park et al., 2004) http://neuroimage.yonsei.ac.kr/dodti/ Preprocessing, tensor estimation, and tractography DTI-Query (Akers et al., 2004) http://graphics.stanford.edu/projects/dti/software/ Tractography DTI-TK (Zhang et al., 2009) http://dti-tk.sourceforge.net/pmwiki/pmwiki.php Registration DTIStudio (Jiang et al., 2006) https://www.mristudio.org/wiki/DtiStudioV2 Tensor estimation, ROI analysis, and tractography ExploreDTI (Leemans et al., 2009) http://www.exploredti.com/ Preprocessing, tensor estimation, and tractography Freesurfer (Fischl, 2012) http://surfer.nmr.mgh.harvard.edu/ Preprocessing and tensor estimation FSL-FDT (Smith et al., 2004) http://www.fmrib.ox.ac.uk/fsl/fdt/index.html Preprocessing, tensor estimation, and tractography FSL-TBSS (Smith et al., 2006) http://www.fmrib.ox.ac.uk/fsl/tbss/index.html TBSS analysis JIST (Lucas et al., 2010) http://www.nitrc.org/projects/jist/ Preprocessing and tensor estimation MedINRIA (Toussaint et al., 2007) http://wwwsop.inria.fr/asclepios/software/MedINRIA/ Tensor estimation, tractography, and ROI analysis MrDiffusion http://white.stanford.edu/mrdiff Tensor estimation and tractography MRtrix (Tournier et al., 2012) http://www.brain.org.au/software/mrtrix/ Tensor estimation and tractography SATURN (Cardenes et al., 2010) http://www.lpi.tel.uva.es/saturn/ Tensor estimation and tractography SPM and toolboxes (e.g., Diffusion II, DTI Toolboxes)

http://www.ﬁl.ion.ucl.ac.uk/spm/ext/ Preprocessing and tensor estimation

TrackVis (Wang et al., 2007) http://trackvis.org/ Tensor estimation, tractography, and ROI analysis TORTOISE (Pierpaoli et al., 2010) https://science.nichd.nih.gov/conﬂuence/display/nihpd/

Preprocessing, tensor estimation, and ROI analysis

TORTOISE

[Figure 8]

MD, ADC, or trace, can be calculated by the mean of the three eigenvalues and correspond to the molecular diffusion rate (lower values mean low diffusivity) (Figure 1J):

Dxx + Dyy + Dzz 3 =

λ1 + λ2 + λ3 3 =

Trace 3

MD =

[Figure 9]

[Figure 10]

[Figure 11]

where Dxx, Dyy, Dzz are the diagonal terms of the diffusion tensor.

Fractional Anisotropy is a normalized measure of the fraction of the tensor’s magnitude due to anisotropic diffusion, corresponding to the degree of anisotropic diffusion or directionality and ranges from 0 (isotropic diffusion) to 1 (anisotropic diffusion):

FA =

[Figure 12]

3 2

[Figure 13]

[Figure 14]

(λ1 − D)2 + (λ2 − D)2 + (λ3 − D)2 λ21 + λ22 + λ23

[Figure 15]

where D = (λ1 + λ2 + λ3)/3. FA has no information about the orientation (Figure 1I), its rotationally invariant. This can be deciphered by color-coded FA maps in which the color of each voxel demonstrates its main diffusion direction (Figure 1H). In these maps, red color represents left-to-right orientation, green posterior-to-anterior and blue inferior-to-superior diffusion.

Other relevant DTI indices reported are trace (magnitude of diffusion in a voxel), Lattice Anisotropy Index (LAI—an intervoxel anisotropy measure with reduced sensitivity to noise), axial (derived from the largest eigenvalues and measures the rate of diffusion in the direction of fastest diffusion detecting longitudinal diffusion along axons), and radial diffusivity (derived from the second and third eigenvalues and measures the transverse direction of diffusion) (Basser and Pierpaoli, 1996; Vilanova et al., 2006; Jones, 2008; Abe et al., 2010; Chanraud et al., 2010). Typically, MD is higher in damaged tissues as a result of increased free diffusion; in contrast, FA decreases due to the loss of coherence in the main preferred diffusion direction. Importantly, software tools presented in Table 1 that can be used for tensor estimation also enable the calculation of some of the most commonly used scalar maps.

Contrasting with the dimensionality reduction of the tensor represented by scalar indices, glyphs are parameterized graphical objects that describe a diffusion tensor through its size, shape, location, and color (Figure 1G). Glyphs are used for visualization and quality control and not for analysis procedures. The most typical representation is the 3D ellipsoidal shape elongated along the fastest diffusion axis and squashed along restricted

diffusion directions. These objects map the tensor eigenvectors and eigenvalues, which express the water molecules diffusion proﬁle (Pierpaoli and Basser, 1996; Kindlmann and Westin, 2006). Other shapes can also be used, such as box glyphs which are better for linear anisotropy proﬁles but, as ellipsoids, they overlook important information and it is difﬁcult to clearly understand 3D shapes when viewed in planes (Vilanova et al., 2006). To overcome this problem, another class of glyphs, known as superquadrics were introduced and combine spherical, cylindrical and box shapes to distinguish between isotropic, planar and linear anisotropy and intermediate states (Kindlmann, 2006). The main disadvantage of glyph visualization is that it only allows intrinsic individual proﬁles rather than global characterization of the tensor data. Most DTI viewers enable glyphs representation as lines, tubes or ellipsoids and allow its combination with scalar maps visualization. From the tools presented in Table 2, MedINRIA and SATURN also support box and superquadrics glyphs.

The last family of parameters that can be extrapolated from DTI is based on the primary eigenvector of diffusion to obtain three-dimensional representations of WM pathways or ﬁber bundles, the so-called, WM tractography (Figure 1K). This method projects 3D trajectories of ﬁber pathways and connection patterns between different brain systems in vivo (Jones et al., 1999b; Mori et al., 1999; Basser et al., 2000; Mori and van Zijl, 2002; Wedeen et al., 2012). Tractography processing can be divided in three main stages, namely seeding, propagation, and termination. Seeding consists of deﬁning the points from

which the ﬁber bundles will be drawn; one of the most common methodologies is based on deﬁning Regions Of Interest (ROIs) and placing one or more seeds in each voxel of the ROI (Figure 1L). The ROIs can be manually drawn or extracted from other MRI modalities. The main issues at this stage are related with the location of the seeding points among different subjects and the ﬁber tracking tool used, causing variability in the results (Burgel et al., 2009; Hattingen et al., 2009). A second popular approach consists of using automatic seeding for the whole brain, enabling a fully exploratory visualization of the tensor data.

During the propagation process the ﬁbers are gradually generated. Fiber tracking can be performed with different algorithms divided in two main categories: deterministic and probabilistic (Jones, 2008, 2010a; Descoteaux et al., 2009; Chung et al., 2011; Fillard et al., 2011; Tensaouti et al., 2011; Tournier et al., 2011). Deterministic tractography aims to model the data and, in practical terms, can be thought of as generating/reconstructing one ﬁber from each seed. On the other hand, probabilistic approaches take into account the uncertainty of the estimation, which results in probability maps representing the likelihood of a voxel being part of a ﬁber and provides the multiple possible ﬁber directions emanating from each seed. A common deterministic algorithm used and implemented in the main DTI processing packages is Fiber Assignment by Continuous Tracking (FACT) deﬁning speciﬁc anatomic tracts based on ROIs assuming that ﬁber orientation is uniform within a voxel and changes abruptly in the boundaries of it (Mori et al., 1999).

[Figure 16]

- Table 2 | A list of the main workﬂow steps implemented by the common DTI tools∗.

[Figure 17]

Software Steps Quality control and preprocessing Processing and visualization Quantitative analysis

[Figure 18]

[Figure 19]

[Figure 20]

Outlier detection

Motion and eddy current correction/ B-matrix rotation

Skull stripping

Tensor estimation

Scalar maps

Glyphs Tractography (deterministic/ probabilistic)

ROI Histogram VBA TBSS

[Figure 21]

- 3D Slicer ✗ ✓/✓ ✓ ✓ ✓ ✓ ✓/✓ ✓ ✗ ✗ ✗ AFNI ✗ ✓/✗ ✓ ✓ ✓ ✓ ✓/✓ ✓ ✓ ✓ ✗ BioImage Suite ✗ ✗/✗ ✓ ✓ ✓ ✓ ✓/✗ ✓ ✗ ✗ ✗ BrainVoyager QX ✗ ✗/✗ ✗ ✓ ✓ ✓ ✓/✗ ✗ ✗ ✓ ✗ Camino ✓ ✗/✗ ✗ ✓ ✓ ✓ ✓/✓ ✗ ✗ ✗ ✗ Dipy ✗ ✗ ✗ ✓ ✓ ✗ ✓/✗ ✗ ✗ ✗ ✗ DoDTI ✗ ✓/✗ ✗ ✓ ✓ ✓ ✓/✗ ✗ ✗ ✗ ✗ DTIStudio ✓ ✗/✗ ✗ ✓ ✓ ✓ ✓/✗ ✓ ✗ ✗ ✗ ExploreDTI ✓ ✓/✓ ✗ ✓ ✓ ✓ ✓/✓ ✓ ✗ ✗ ✗ Freesurfer ✗ ✓/✓ ✓ ✓ ✓ ✗ ✗/✓ ✓ ✗ ✓ ✗ FSL ✗ ✓/✗ ✓ ✓ ✓ ✓ ✗/✓ ✓ ✓ ✓ ✓ JIST ✓ ✓/✓ ✗ ✓ ✓ ✗ ✓/✗ ✗ ✗ ✗ ✗ MedINRIA ✗ ✗/✗ ✗ ✓ ✓ ✓ ✓/✗ ✓ ✓ ✗ ✗ MRtrix ✗ ✗ ✓ ✓ ✓ ✗ ✓/✗ ✗ ✗ ✗ ✗ SATURN ✗ ✗/✗ ✗ ✓ ✓ ✓ ✓/✗ ✓ ✗ ✗ ✗ SPM and toolboxes ✗ ✓/✓ ✓ ✓ ✓ ✗ ✗/✗ ✗ ✗ ✓ ✓ TrackVis ✗ ✗/✗ ✗ ✓ ✓ ✗ ✓/✗ ✓ ✓ ✗ ✗ TORTOISE ✓ ✓/✓ ✗ ✓ ✓ ✗ ✗/✗ ✓ ✗ ✗ ✗

[Figure 22]

*To the best of our knowledge at the date of submission, based on information gathered from the software manuals, main webpages, and published papers.

Other deterministic algorithms are streamlining with different interpolation methods (tri-linear, second, or fourth order RungeKutta), tensor deﬂection, or tensorline (Weinstein et al., 1999; Basser et al., 2000; Lazar et al., 2003). Tools like Diffusion Toolkit implement all these algorithms, whereas Slicer implements second order Runge-Kutta. Regularly used probabilistic algorithms are PICo (Parker et al., 2003), used by Camino, multi-ﬁber ﬁeld model (Behrens et al., 2007), implemented in FSL, and the Bayesian approach (Friman et al., 2006) used in Slicer and Camino.

The last tractography step is termination of the ﬁber tracking procedure based on some well-deﬁned criteria, also known as the termination criteria. These criteria aim to avoid propagating the ﬁbers in voxels where robustness of the vectorial ﬁeld is not assured. The common termination criteria are minimum FA thresholds (typically 0.1–0.3 in adult brain and 0.1 in infant) and turning angle threshold (typically 40–70◦, depending on the pathway).

Interpreting tractography maps can be problematic due to the intrinsic unrealistic assumption of a homogeneous unidirectional population inside the voxels. Speciﬁc regions of the brain containing two or even more differently oriented ﬁber bundles within the same voxel (crossing, diverging, or kissing ﬁbers) lead to incorrect estimations of ﬁber directions and pathways and abrupt terminations of tracts (Wiegell et al., 2000; Alexander et al., 2001; Barrick and Clark, 2004; Descoteaux et al., 2009). This limitation can be minimized by adopting more sophisticated approaches including multi tensor models, High Angular Resolution Diffusion Imaging (HARDI), Hybrid Diffusion Imaging (HYDI), Diffusion Spectrum Imaging (DSI), Q-Ball Imaging (QBI), Q-Space Imaging (QSI), Spherical Deconvolution Model, and Persistent Angular Structure MRI (PAS-MRI) (Tuch et al., 2002; Jansons and Alexander, 2003; Tuch, 2004; Alexander et al., 2006; Wedeen et al., 2008; Assemlal et al., 2011; Tournier et al., 2011; Landman et al., 2012; Vos et al., 2012). Recently, these methods have gained increasing popularity, replacing the traditional tensor model for tractography (Wedeen et al., 2012). For instance, DSI and QBI use probability density functions instead of single tensors, which can describe the diffusion process in many different directions at each voxel. This comes with the limitation of requiring longer acquisition times as it needs more encoding directions (Tournier et al., 2011). HARDI, DSI and QBI approaches can be implemented with TrackVis and Diffusion Toolkit,and Camino has been used in HYDI analysis and PAS-MRI.

## QUANTITATIVE ANALYSIS

After parametric maps (e.g., MD, FA) computation and in order to perform individual or group statistical analysis, the next common step is to extract summary measures from either speciﬁc anatomical regions or whole brain. For this purpose, ROIs, histogram, voxel-based analysis and Tract-Based Spatial Statistics (TBSS) are typically applied. It is important to note that usually researchers/clinicians are interested in group comparisons and the methods to extract summary measures differ mainly in the way the correspondence across subjects is achieved.

ROI analysis is based on manual delineation of a priori speciﬁc regions of the brain or on automated parcellations. ROI analyses are time-consuming, require anatomical knowledge and are applied to quantify diffusion parameters (mainly MD and FA) within those areas. The main problems of ROI analyses include: the inﬂuence of the image intensity on ROI boundaries by direct segmentations on the map of interest (typically FA or MD); the difﬁculty to co-register diffusion with typical anatomical images (T1 or T2 weighted) when using anatomical ROIs; performing analysis in smaller/thinner tracts; and difﬁcult application in longitudinal studies (Snook et al., 2007; Mukherjee et al., 2008b; Astrakas and Argyropoulou, 2010; Chanraud et al., 2010; Jones and Cercignani, 2010). Of note, ROI analysis can be performed with the main tensor estimation and visualization software, such as Slicer, TrackVis, MedINRIA, and ExploreDTI.

Another possibility for quantitative analysis is the use of frequencies of distributions to screen the voxels within a speciﬁc range of parameters of interest (usually MD or FA). The histogram of each diffusion parameter presents the mean, the peak height and location, values that can be used to compare groups through statistical tests (Figure 1M). Histograms allow analysis of whole brain in an automated way, without any a priori speciﬁed ROI; however, such an approach requires the removal of the tissue of no interest (typically CSF), does not retain any information about the location of abnormalities and is sensitive to partial volume effect from atrophy (Della Nave et al., 2007; Jones and Cercignani, 2010; Zhou et al., 2011a). For such approach, tools such as TrackVis or MedINRIA can be used.

Analyses on a voxel-by-voxel basis are becoming popular in DTI given that they are automated, require minimum intervention and are not inﬂuenced by users. Voxel Based Analysis (VBA) involves registration of diffusion maps into a standard space (a process known as normalization) to achieve correspondences between subjects across voxels and consequently anatomical structures (Figure 1N). This enables the comparison of diffusion parameters between groups and correlations with covariates of interest (e.g., age). This approach allows spatially speciﬁc (as ROIs) and unbiased (as histogram) analysis and does not require previous ROI deﬁnition. The main problem is the accuracy of registration algorithms using tensor datasets (Mukherjee et al., 2008b; Abe et al., 2010; Astrakas and Argyropoulou, 2010; Jones and Cercignani, 2010; Van Hecke et al., 2010). VBA can be carried out with SPM or BrainVoyager QX, with SPM as the most widely used software tool for this kind of analysis.

A recent method designed to overcome the problems with registration algorithms and arbitrariness of spatial smoothing is TBSS. TBSS is an automated method for detecting group voxel-wise changes in whole brain, based on the skeletonization of group registered FA maps (Figure 1O). TBSS removes the need to perform spatial smoothing, increases the statistical power (reducing number of total voxels tested). On the other hand, the skeletonization of FA images may be inaccurate in images with large anatomical shifts or WM lesions and registration errors are difﬁcult to identify visually in the skeleton (Jones and Cercignani, 2010). Back projection to native space is also an issue since the skeletonization process aligns local maxima, which

may not necessarily correspond to the same anatomical location across all subjects (Zalesky, 2011). This method is part of the FSL distribution (Smith et al., 2006).

One of the big issues in group studies is that to compare a condition among a group, the individual images need to be normalized to a standard space (Evans et al., 2012). After this, each structure should be in the same position across all the group subjects. The normalization procedure is crucial for VBA analysis and the result of a misalignment can be unpredictable. This is particularly challenging in DTI due to its highly directional and topographical nature. This challenge led to a variety of procedures for the normalization of DTI images (Jones et al., 2002; Park et al., 2003; Xu et al., 2003). The most straightforward method consists in using the b0 images to calculate a rigid alignment with a high-resolution T1 image and then an afﬁne alignment from the T1 space to standard the space. Note that the transformation matrixes generated should only be applied to the scalar images. Alternatively, some researchers opt to drive the registration directly from b0 image to an EPI template in standard space. The differences among these approaches were already addressed in previous studies (Liu et al., 2010a). Another normalization approach consists in the normalization of the tensors using complex multi-channel algorithms (Park et al., 2003). The tools that are most commonly used in data normalization are AIR, FLIRT, and SPM. Also here, to solve the normalization problems with DTI images, TBSS provides a new and revolutionary method for inter-subject registration of FA maps.

To perform statistical parametric analysis, the data can be smoothed using a three-dimensional ﬁlter. This increases the SNR, reduces imperfections due to spatial normalization procedures, improves the statistical power and enables the assumption of random ﬁeld theory (Westin et al., 2002). Care must be taken since the chosen spatial width of the ﬁlter will determine the size of the differences than can be detected, and smoothing also increases the amount of partial volume effect (Jones and Cercignani, 2010). This step can be performed with tools like fslmaths (a command line tool from FSL library) or SPM.

For a global guidance about the possible software solutions for the main steps of the DTI workﬂow consult Table 2.

## MULTIMODAL STUDIES

Collecting multimodal brain data from the same individual using different neuroimaging methods has become recently a standard in the ﬁeld and is certainly a trend for the future. Combining different modalities allows a global and complementary overview of living brain structure and function. Brain connectivity studies have become popular nowadays with the combination of microstructural organization (DTI) and functional activation patterns using resting state or task related functional MRI (fMRI) (Le Bihan, 2012) (Figure 1P). Changes in diffusion measures can point to alterations in functional patterns and behavior. A general problem using this approach is the common need to expand GM clusters to WM areas, in order to reach the WM ﬁber tracts (Li et al., 2012). In practice this is achieved by dilating the activation clusters using tools such as fslmaths (from FSL package)

or MarsBaR (SPM toolbox). Several studies have demonstrated neuroanatomical connections between functionally linked brain regions in resting state networks (Van Den Heuvel et al., 2008,

- 2009; Greicius et al., 2009) and task related patters (Propper et al.,
- 2010; Ethofer et al., 2011). Another popular multimodal approach is to use conven-

tional MRI or T1 weighted derived masks, segmentations or parcellations (ROIs) in DTI data to extract combined structural and diffusion data (Figure 1Q). Moreover, WM volumetric ROIs have been used to assess microstructure integrity (Fjell et al., 2008; Moriya et al., 2010; Kochunov et al., 2011). In addition, combining DTI parameters with electroencephalography (EEG) records (Bangera et al., 2010; Gullmar et al.,

- 2010), cortico-cortical evoked potentials (CCEPs) (Conner et al.,
- 2011), Magnetoencephalography (MEG) (Fernandez et al., 2011), Positron Emission Tomography (PET) (Yakushev et al., 2011), Magnetic Resonance Spectroscopy (MRS) (Tang et al., 2007; Wang et al., 2009) and Transcranial Magnetic Stimulation (TMS) (Hubers et al., 2012), have revealed new insights on the complementary complexity of the human brain. Importantly, in order to combine DTI with other neuroimaging modality data, the ROIs should be in the same reference space as the DTI data.

RESULTS INTERPRETATION

In DTI data interpretation the most common misconception is related with the scalar results. Usually higher MD and lower FA values indicate damaged or impaired ﬁber integrity due to increased diffusion and loss of coherence on preferred movement direction. However, this is not always true. In fact, depending on the brain region, cellular basis, and sample studied (speciﬁc disease processes, developmental conditions), unusually high or low indices may indicate dysfunction or not (Hoeft et al., 2007; Thomason et al., 2010).

Other pitfalls in DTI interpretation are also observed. The interpretation of color-oriented maps is also far from trivial because two different tracts may have the same color (if they have the same in-plane ﬁber orientations) and the same tract can change color-coding when orientation changes, making it difﬁcult to localize across 2D images. Crossing ﬁbers are also problematic in DTIresults interpretation, affecting more FA, axial and radial diffusivity than MD, and having a huge impact on tractography methods (Tournier et al., 2011).

As a ﬁnal take-home message, WM integrity assumptions must always be made with extreme caution (Beaulieu, 2002; Jones et al.,

- 2012).

## CONCLUSIONS AND FUTURE DIRECTIONS

DTI is currently a promising tool to study WM microstructure in vivo. It has, nevertheless, difﬁculties associated with each speciﬁc analysis stage that must be taken into account from the initial steps of the experimental design to the ﬁnal interpretation of results. This article has highlighted the common problems faced when performing DTI studies and some possible ways to overcome them, giving practical guidelines and references, including for the most used tools for each step of the common DTI pipeline. The description of the most commonly used solutions and tools

in the DTI workﬂow is something that we believe to be underestimated so far. It is, thus, our belief that this hitchhicker’s guide will be of help for newcomers to the ﬁeld, but also for those who want to update their knowledge on the topic.

## ACKNOWLEDGMENTS

The work was supported by SwitchBox-FP7-HEALTH-2010grant 259772-2. The authors acknowledge Nadine Santos for her help in editing the manuscript.

## REFERENCES

Abe, O., Takao, H., Gonoi, W., Sasaki, H., Murakami, M., Kabasawa, H., et al. (2010). Voxel-based analysis of the diffusion tensor. Neuroradiology 52, 699–710.

Akers, D., Sherbondy, A., MacKenzie, R., Dougherty, R., and Wandell, B. (2004). “Exploration of the brain’s white matter pathways with dynamic queries,” in Proceedings of the Conference on Visualization ‘04 (Austin, TX: IEEE Computer Society).

Alexander, A. L., Hasan, K. M., Lazar, M., Tsuruda, J. S., and Parker, D. L. (2001). Analysis of partial volume effects in diffusion-tensor MRI. Magn. Reson. Med. 45, 770–780. Alexander, A. L., Wu, Y. C., and Venkat, P. C. (2006). Hybrid diffusion imaging (HYDI). Conf. Proc. IEEE Eng. Med. Biol. Soc. 1, 2245–2248.

Assaf, Y., and Pasternak, O. (2008). Diffusion tensor imaging (DTI)based white matter mapping in brain research: a review. J. Mol. Neurosci. 34, 51–61.

Assemlal, H. E., Tschumperle, D., Brun, L., and Siddiqi, K. (2011). Recent advances in diffusion MRI modeling: angular and radial reconstruction. Med. Image Anal. 15, 369–396.

Astrakas, L. G., and Argyropoulou, M. I. (2010). Shifting from region of interest (ROI) to voxel-based analysis in human brain mapping. Pediatr. Radiol. 40, 1857–1867.

Bammer, R., Auer, M., Keeling, S. L., Augustin, M., Stables, L. A., Prokesch, R. W., et al. (2002). Diffusion tensor imaging using single-shot SENSE-EPI. Magn. Reson. Med. 48, 128–136.

Bammer, R., Holdsworth, S. J., Veldhuis, W. B., and Skare, S. T. (2009). New methods in diffusionweighted and diffusion tensor imaging. Magn. Reson. Imaging Clin. N. Am. 17, 175–204.

Bangera, N. B., Schomer, D. L., Dehghani, N., Ulbert, I., Cash, S., Papavasiliou, S., et al. (2010). Experimental validation of the inﬂuence of white matter anisotropy on the intracranial EEG forward solution. J. Comput. Neurosci. 29, 371–387.

Barrick, T. R., and Clark, C. A. (2004). Singularities in diffusion tensor ﬁelds and their relevance

in white matter ﬁber tractography. Neuroimage 22, 481–491.

Basser, P. J., and Jones, D. K. (2002). Diffusion-tensor MRI: theory, experimental design and data analysis– a technical review. NMR Biomed. 15, 456–467.

Basser, P. J., Mattiello, J., and Lebihan, D. (1994a). Estimation of the effective self-diffusion tensor from the NMR spin echo. J. Magn. Reson. B 103, 247–254.

Basser, P. J., Mattiello, J., and Lebihan, D. (1994b). MR diffusion tensor spectroscopy and imaging. Biophys. J. 66, 259–267.

Basser, P. J., Pajevic, S., Pierpaoli, C., Duda, J., and Aldroubi, A. (2000). In vivo ﬁber tractography using DTMRI data. Magn. Reson. Med. 44, 625–632.

Basser, P. J., and Pierpaoli, C. (1996). Microstructural and physiological features of tissues elucidated by quantitative-diffusion-tensor MRI. J. Magn. Reson. B 111, 209–219. Basu, S., Fletcher, T., and Whitaker, R. (2006). Rician noise removal in diffusion tensor MRI. Med. Image Comput. Comput. Assist. Interv. 9, 117–125.

Bazin, P. L., Ye, C., Bogovic, J. A., Shiee, N., Reich, D. S., Prince, J. L., et al. (2011). Direct segmentation of the major white matter tracts in diffusion tensor images. Neuroimage 58, 458–468.

Beaulieu, C. (2002). The basis of anisotropic water diffusion in the nervous system– a technical review. NMR Biomed. 15, 435–455.

Behrens, T. E., Berg, H. J., Jbabdi, S., Rushworth, M. F., and Woolrich, M. W. (2007). Probabilistic diffusion tractography with multiple ﬁbre orientations: what can we gain? Neuroimage 34, 144–155.

Brau, A. C., Beatty, P. J., Skare, S., and Bammer, R. (2008). Comparison of reconstruction accuracy and efﬁciency among autocalibrating datadriven parallel imaging methods. Magn. Reson. Med. 59, 382–395. Budde, M. D., Xie, M., Cross, A. H., and Song, S. K. (2009). Axial diffusivity is the primary correlate of axonal injury in the experimental autoimmune encephalomyelitis spinal cord: a quantitative pixelwise analysis. J. Neurosci. 29, 2805–2813.

Burgel, U., Madler, B., Honey, C. R., Thron, A., Gilsbach, J., and Coenen,

V. A. (2009). Fiber trackingwith distinct software tools results in a clear diversity in anatomical ﬁber tract portrayal. Cent. Eur. Neurosurg. 70, 27–35.

Cardenes, R., Munoz-Moreno, E., Tristan-Vega, A., and MartinFernandez, M. (2010). Saturn: a software application of tensor utilities for research in neuroimaging. Comput. Methods Programs Biomed. 97, 264–279.

Carvalho Rangel, C., Hygino Cruz, L. C. Jr., Takayassu, T. C., Gasparetto, E. L., and Domingues, R. C. (2011). Diffusion MR imaging in central nervous system. Magn. Reson. Imaging Clin. N. Am. 19, 23–53.

Catani, M., and Thiebaut De Schotten, M. (2008). A diffusion tensor imaging tractography atlas for virtual in vivo dissections. Cortex 44, 1105–1132.

Chang, L. C., Jones, D. K., and Pierpaoli, C. (2005). RESTORE: robust estimation of tensors by outlier rejection. Magn. Reson. Med. 53, 1088–1095.

Chanraud, S., Zahr, N., Sullivan, E. V., and Pfefferbaum, A. (2010). MR diffusion tensor imaging: a window into white matter integrity of the working brain. Neuropsychol. Rev. 20, 209–225.

Chavez, S., Storey, P., and Graham, S. J. (2009). Robust correction of spike noise: application to diffusion tensor imaging. Magn. Reson. Med. 62, 510–519.

Chen, B., Guo, H., and Song, A. W. (2006). Correction for directiondependent distortions in diffusion tensor imaging using matched magnetic ﬁeld maps. Neuroimage 30, 121–129.

Chenevert, T. L., Brunberg, J. A., and Pipe, J. G. (1990). Anisotropic diffusion in human white matter: demonstration with MR techniques in vivo. Radiology 177, 401–405.

Choi, S., Cunningham, D. T., Aguila, F., Corrigan, J. D., Bogner, J., Mysiw, W. J., et al. (2011). DTI at 7 and 3 T: systematic comparison of SNR and its inﬂuence on quantitative metrics. Magn. Reson. Imaging 29, 739–751.

Chung, H. W., Chou, M. C., and Chen, C. Y. (2011). Principles and limitations of computational algorithms

in clinical diffusion tensor MR tractography. AJNR. Am. J. Neuroradiol. 32, 3–13.

Ciccarelli, O., Catani, M., JohansenBerg, H., Clark, C., and Thompson, A. (2008). Diffusion-based tractography in neurological disorders: concepts, applications, and future developments. Lancet Neurol. 7, 715–727.

Conner, C. R., Ellmore, T. M., Disano, M. A., Pieters, T. A., Potter, A. W., and Tandon, N. (2011). Anatomic and electro-physiologic connectivity of the language system: a combined DTI-CCEP study. Comput. Biol. Med. 41, 1100–1109.

Cook, P. A., Bai, Y., Gilani, N., Seunarine, K. K., Hall, M. G., Parker, G. J., et al. (2006). “Camino: open-source diffusion-MRI reconstruction and processing,” in 14th Scientiﬁc Meeting of the International Society for Magnetic Resonance in Medicine (Seattle, WA), 2759.

Cox, R. W. (2012). AFNI: what a long strange trip it’s been. Neuroimage 62, 743–747.

Della Nave, R., Foresti, S., Pratesi, A., Ginestroni, A., Inzitari, M., Salvadori, E., et al. (2007). Whole-brain histogram and voxel-based analyses of diffusion tensor imaging in patients with leukoaraiosis: correlation with motor and cognitive impairment. AJNR. Am. J. Neuroradiol. 28, 1313–1319.

Descoteaux, M., Deriche, R., Knosche, T. R., and Anwander, A. (2009). Deterministic and probabilistic tractography based on complex ﬁbre orientation distributions. IEEE Trans. Med. Imaging 28, 269–286. Douek, P., Turner, R., Pekar, J., Patronas, N., and Le Bihan, D. (1991). MR color mapping of myelin ﬁber orientation. J. Comput. Assist. Tomogr. 15, 923–929.

Ethofer, T., Gschwind, M., and Vuilleumier, P. (2011). Processing social aspects of human gaze: a combined fMRI-DTI study. Neuroimage 55, 411–419.

Evans, A. C., Janke, A. L., Collins, D. L., and Baillet, S. (2012). Brain templates and atlases. Neuroimage 62, 911–922.

Farrell, J. A., Landman, B. A., Jones, C. K., Smith, S. A., Prince, J. L., van Zijl, P. C., et al. (2007). Effects of

signal-to-noise ratio on the accuracy and reproducibility of diffusion tensor imaging-derived fractional anisotropy, mean diffusivity, and principal eigenvector measurements at 1.5 T. J. Magn. Reson. Imaging 26, 756–767.

Farzaneh, F., Riederer, S. J., and Pelc, N. J. (1990). Analysis of T2 limitations and off-resonance effects on spatial resolution and artifacts in echo-planar imaging. Magn. Reson. Med. 14, 123–139.

Fernandez, A., Rios-Lago, M., Abasolo, D., Hornero, R., Alvarez-Linera, J., Paul, N., et al. (2011). The correlation between white-matter microstructure and the complexity of spontaneous brain activity: a difussion tensor imaging-MEG study. Neuroimage 57, 1300–1307.

Figueiredo, E. H., Borgonovi, A. F., and Doring, T. M. (2011). Basic concepts of MR imaging, diffusion MR imaging, and diffusion tensor imaging. Magn. Reson. Imaging Clin. N. Am. 19, 1–22.

Fillard, P., Descoteaux, M., Goh, A., Gouttard, S., Jeurissen, B., Malcolm, J., et al. (2011). Quantitative evaluation of 10 tractography algorithms on a realistic diffusion MR phantom. Neuroimage 56, 220–234.

Fischl, B. (2012). FreeSurfer. Neuroimage 62, 774–781.

Fjell, A. M., Westlye, L. T., Greve, D. N., Fischl, B., Benner, T., van der Kouwe, A. J., et al. (2008). The relationship between diffusion tensor imaging and volumetry as measures of white matter properties. Neuroimage 42, 1654–1668.

Friman, O., Farneback, G., and Westin, C. F. (2006). A Bayesian approach for stochastic white matter tractography. IEEE Trans. Med. Imaging 25, 965–978.

Friston, K. J., Ashburner, J. T., Kiebel, S. J., Nichols, T. E., and Penny, W. D. (2007). Statistical Parametric Mapping: The Analysis of Functional Brain Images. London: Academic Press.

Fung, S. H., Roccatagliata, L., Gonzalez, R. G., and Schaefer, P. W. (2011). MR diffusion imaging in ischemic stroke. Neuroimaging Clin. N. Am. 21, 345–377.

Gallichan, D., Scholz, J., Bartsch, A., Behrens, T. E., Robson, M. D., and Miller, K. L. (2010). Addressing a systematic vibration artifact in diffusion-weighted MRI. Hum. Brain Mapp. 31, 193–202.

Garyfallidis, E., Brett, M., Amirbekian, B., Nguyen, C., Yeh, F.-C., Olivetti, E., et al. (2011). “Dipy – a novel software library for diffusion MR and tractography,”

in 17th Annual Meeting of the Organization for Human Brain Mapping (Québec, QC).

Goebel, R. (2012). BrainVoyager– past, present, future. Neuroimage 62, 748–756.

Greicius, M. D., Supekar, K., Menon, V., and Dougherty, R. F. (2009). Resting-state functional connectivity reﬂects structural connectivity in the default mode network. Cereb. Cortex 19, 72–78.

Griswold, M. A., Jakob, P. M., Heidemann, R. M., Nittka, M., Jellus, V., Wang, J., et al. (2002). Generalized autocalibrating partially parallel acquisitions (GRAPPA). Magn. Reson. Med. 47, 1202–1210.

Gudbjartsson, H., Maier, S. E., Mulkern, R. V., Morocz, I. A., Patz, S., and Jolesz, F. A. (1996). Line scan diffusion imaging. Magn. Reson. Med. 36, 509–519.

Gullmar, D., Haueisen, J., and Reichenbach, J. R. (2010). Inﬂuence of anisotropic electrical conductivity in white matter tissue on the EEG/MEG forward and inverse solution. A high-resolution whole head simulation study. Neuroimage 51, 145–163.

Gupta, R. K., Trivedi, R., Awasthi, R., Paliwal, V. K., Prasad, K. N., and Rathore, R. K. (2012). Understanding changes in DTI metrics in patients with different stages of neurocysticercosis. Magn. Reson. Imaging 30, 104–111.

Hagmann, P., Jonasson, L., Maeder, P., Thiran, J. P., Wedeen, V. J., and Meuli, R. (2006). Understanding diffusion MR imaging techniques: from scalar diffusion-weighted imaging to diffusion tensor imaging and beyond. Radiographics 26(Suppl. 1), S205–S223.

Hasan, K. M., Walimuni, I. S., Abid, H., and Hahn, K. R. (2011). A review of diffusion tensor magnetic resonance imaging computational methods and software tools. Comput. Biol. Med. 41, 1062–1072.

Hattingen, E., Rathert, J., Jurcoane, A., Weidauer, S., Szelenyi, A., Ogrezeanu, G., et al. (2009). A standardised evaluation of pre-surgical imaging of the corticospinal tract: where to place the seed ROI. Neurosurg. Rev. 32, 445–456.

Hoeft, F., Barnea-Goraly, N., Haas, B. W., Golarai, G., Ng, D., Mills, D., et al. (2007). More is not always better: increased fractional anisotropy of superior longitudinal fasciculus associated with poor visuospatial abilities in Williams syndrome. J. Neurosci. 27, 11960–11965.

Holdsworth, S. J., Skare, S., Newbould, R. D., and Bammer, R. (2009). Robust GRAPPAaccelerated diffusion-weighted readout-segmented (RS)-EPI. Magn. Reson. Med. 62, 1629–1640.

Huang, H., Ceritoglu, C., Li, X., Qiu, A., Miller, M. I., Van Zijl, P. C., et al. (2008). Correction of B0 susceptibility induced distortion in diffusion-weighted images using large-deformation diffeomorphic metric mapping. Magn. Reson. Imaging 26, 1294–1302.

Hubers, A., Klein, J. C., Kang, J. S., Hilker, R., and Ziemann, U. (2012). The relationship between TMS measures of functional properties and DTI measures of microstructure of the corticospinal tract. Brain Stimul. 5, 297–304.

Hygino Da Cruz, L. C. Jr., Vieira, I. G., and Domingues, R. C. (2011). Diffusion MR imaging: an important tool in the assessment of brain tumors. Neuroimaging Clin. N. Am. 21, 27–49.

Imfeld, A., Oechslin, M. S., Meyer, M., Loenneker, T., and Jancke, L. (2009). White matter plasticity in the corticospinal tract of musicians: a diffusion tensor imaging study. Neuroimage 46, 600–607.

Jaermann, T., Pruessmann, K. P., Valavanis, A., Kollias, S., and Boesiger, P. (2006). Inﬂuence of SENSE on image properties in high-resolution single-shot echoplanar DTI. Magn. Reson. Med. 55, 335–342.

Jansons, K. M., and Alexander, D. C. (2003). Persistent Angular Structure: new insights from diffusion MRI data. Dummy version. Inf. Process. Med. Imaging 18, 672–683.

Jellison, B. J., Field, A. S., Medow, J., Lazar, M., Salamat, M. S., and Alexander, A. L. (2004). Diffusion tensor imaging of cerebral white matter: a pictorial review of physics, ﬁber tract anatomy, and tumor imaging patterns. AJNR. Am. J. Neuroradiol. 25, 356–369.

Jiang, H., Chou, M.-C., Van Zijl, P., and Mori, S. (2009). “Outlier detection for diffusion tensor imaging by testing for ADC consistency,” in Proceedings of the International Society for Magnetic Resonance in Medicine (Honolulu, HI), 17.

Jiang, H., Van Zijl, P. C., Kim, J., Pearlson, G. D., and Mori, S. (2006). DtiStudio: resource program for diffusion tensor computation and ﬁber bundle tracking. Comput. Methods Programs Biomed. 81, 106–116.

Johansen-Berg, H., and Behrens, T. E. J. (2009). Diffusion MRI:

From Quantitative Measurement to In-Vivo Neuroanatomy. London: Academic Press.

Jones, D. K. (2004). The effect of gradient sampling schemes on measures derived from diffusion tensor MRI: a Monte Carlo study. Magn. Reson. Med. 51, 807–815.

Jones, D. K. (2008). Studying connections in the living human brain with diffusion MRI. Cortex 44, 936–952.

- Jones, D. K. (2010a). Challenges and limitations of quantifying brain connectivity in vivo with diffusion MRI. Imaging Med. 2, 341–355.
- Jones, D. K. (2010b). Diffusion MRI: Theory, Methods, and Applications. New York, NY: Oxford University Press.
- Jones, D. K. (2010c). Precision and accuracy in diffusion tensor magnetic resonance imaging. Top. Magn. Reson. Imaging 21, 87–99.

Jones, D. K., and Cercignani, M. (2010). Twenty-ﬁve pitfalls in the analysis of diffusion MRI data. NMR Biomed. 23, 803–820.

Jones, D. K., Grifﬁn, L. D., Alexander, D. C., Catani, M., Horsﬁeld, M. A., Howard, R., et al. (2002). Spatial normalization and averaging of diffusion tensor MRI data sets. Neuroimage 17, 592–617.

Jones, D. K., Horsﬁeld, M. A., and Simmons, A. (1999a). Optimal strategies for measuring diffusion in anisotropic systems by magnetic resonance imaging. Magn. Reson. Med. 42, 515–525.

Jones, D. K., Knosche, T. R., and Turner, R. (2012). White matter integrity, ﬁber count, and other fallacies: the do’s and don’ts of diffusion MRI. Neuroimage. doi: 10.1016/j.neuroimage.2012.06.081. [Epub ahead of print].

Jones, D. K., Simmons, A., Williams, S. C., and Horsﬁeld, M. A. (1999b). Non-invasive assessment of axonal ﬁber connectivity in the human brain via diffusion tensor MRI. Magn. Reson. Med. 42, 37–41.

Kaur, P., Senthil Kumaran, S., Tripathi, R. P., Khushu, S., and Kaushik, S. (2007). Protocol error artifacts in MRI: sources and remedies revisited. Radiography 13, 291–306.

Kennedy, S. D., and Zhong, J. (2004). Diffusion measurements free of motion artifacts using intermolecular dipole-dipole interactions. Magn. Reson. Med. 52, 1–6.

Kindlmann, G. (2006). “Superquadric tensor glyphs,” in Proceeding of The Joint Eurographics – IEEE TCVG Symposium on Visualization (Konstanz), 147–154.

Kindlmann, G., and Westin, C. F. (2006). Diffusion tensor

visualization with glyph packing. IEEE. Trans. Vis. Comput. Graph. 12, 1329–1335.

Koay, C. G., Carew, J. D., Alexander, A. L., Basser, P. J., and Meyerand, M. E. (2006). Investigation of anomalous estimates of tensor-derived quantities in diffusion tensor imaging. Magn. Reson. Med. 55, 930–936. Kober, T., Gruetter, R., and Krueger, G. (2012). Prospective and retrospective motion correction in diffusion magnetic resonance imaging of the human brain. Neuroimage 59, 389–398.

Kochunov, P., Glahn, D. C., Lancaster, J., Thompson, P. M., Kochunov, V., Rogers, B., et al. (2011). Fractional anisotropy of cerebral white matter and thickness of cortical gray matter across the lifespan. Neuroimage 58, 41–49.

Lagana, M., Rovaris, M., Ceccarelli, A., Venturelli, C., Marini, S., and Baselli, G. (2010). DTI parameter optimisation for acquisition at 1.5T: SNR analysis and clinical application. Comput. Intell. Neurosci. 2010:254032. doi: 10.1155/2010/ 254032

Landman, B. A., Bogovic, J. A., Wan, H., Elshahaby Fel, Z., Bazin, P. L., and Prince, J. L. (2012). Resolution of crossing ﬁbers with constrained compressed sensing using diffusion tensor MRI. Neuroimage 59, 2175–2186.

Lauzon, C. B., Asman, A. J., Crainiceanu, C., Caffo, B. C., and Landman, B. A. (2011). Assessment of bias for MRI diffusion tensor imaging using SIMEX. Med. Image Comput. Comput. Assist. Interv. 14, 107–115.

Lawes, I. N., Barrick, T. R., Murugam, V., Spierings, N., Evans, D. R., Song, M., et al. (2008). Atlas-based segmentation of white matter tracts of the human brain using diffusion tensor tractography and comparison with classical dissection. Neuroimage 39, 62–79.

Lazar, M., Weinstein, D. M., Tsuruda, J. S., Hasan, K. M., Arfanakis, K., Meyerand, M. E., et al. (2003). White matter tractography using diffusion tensor deﬂection. Hum. Brain Mapp. 18, 306–321.

Le Bihan, B., and Breton, E. (1985). Imagerie de diffusion in vivo par résonance magnétique nucléaire. C. R. Acad. Sci. 301, 1109–1112.

Le Bihan, D. (2012). Diffusion, confusion and functional MRI. Neuroimage 62, 1131–1136.

Le Bihan, D., Breton, E., Lallemand, D., Grenier, P., Cabanis, E., and LavalJeantet, M. (1986). MR imaging of intravoxel incoherent motions:

application to diffusion and perfusion in neurologic disorders. Radiology 161, 401–407.

Le Bihan, D., Mangin, J. F., Poupon, C., Clark, C. A., Pappata, S., Molko, N., et al. (2001). Diffusion tensor imaging: concepts and applications. J. Magn. Reson. Imaging 13, 534–546.

Le Bihan, D., Poupon, C., Amadon, A., and Lethimonnier, F. (2006). Artifacts and pitfalls in diffusion MRI. J. Magn. Reson. Imaging 24, 478–488.

Lebel, C., Benner, T., and Beaulieu, C. (2012). Six is enough? Comparison of diffusion parameters measured using six or more diffusionencoding gradient directions with deterministic tractography. Magn. Reson. Med. 68, 474–483.

Leemans, A., Jeurissen, B., Sijbers, J., and Jones, D. K. (2009). “ExploreDTI: a graphical toolbox for processing, analyzing, and visualizing diffusion MR data,” in 17th Annual Meeting of Intl. Soc. Mag. Reson. Med. (Hawaii), 3537. Leemans, A., and Jones, D. K. (2009). The B-matrix must be rotated when correcting for subject motion in DTI data. Magn. Reson. Med. 61, 1336–1349.

Li, K., Guo, L., Zhu, D., Hu, X., Han, J., and Liu, T. (2012). Individual functional ROI optimization via maximization of group-wise consistency of structural and functional proﬁles. Neuroinformatics 10, 225–242.

Liao, W., Deserno, T., and Spitzer, K. (2008). Evaluation of free nondiagnostic DICOM software tools. Proc. SPIE 6919, 691903.

Ling, J., Merideth, F., Caprihan, A., Pena, A., Teshiba, T., and Mayer, A. R. (2012). Head injury or head motion? Assessment and quantiﬁcation of motion artifacts in diffusion tensor imaging studies. Hum. Brain Mapp. 33, 50–62.

Liu, G., Yao, L., and Zhao, X. (2010a). “Optimization of image preprocessing for diffusion tensor magnetic resonance imaging,” in Sixth International Conference on Natural Computation (ICNC) (Yantai).

Liu, Z., Wang, Y., Gerig, G., Gouttard, S., Tao, R., Fletcher, T., et al. (2010b). Quality control of diffusion weighted images. Proc. SPIE 7628:76280J. doi: 10.1117/ 12.844748

Lucas, B. C., Bogovic, J. A., Carass, A., Bazin, P. L., Prince, J. L., Pham, D. L., et al. (2010). The Java Image Science Toolkit (JIST) for rapid prototyping

and publishing of neuroimaging software. Neuroinformatics 8, 5–17.

Madden, D. J., Bennett, I. J., and Song, A. W. (2009). Cerebral white matter integrity and cognitive aging: contributions from diffusion tensor imaging. Neuropsychol. Rev. 19, 415–435.

Mansﬁeld, P. (1977). Multi-planar image formation using NMR spin echoes. J. Phys. C 10, L55–L58.

Merboldt, K.-D., Hanicke, W., and Frahm, J. (1985). Self-diffusion NMR imaging using stimulated echoes. J. Magn. Reson. 64, 479–486.

Millman, K. J., and Brett, M. (2007). Analysis of functional magnetic resonance imaging in python. Comp. Sci. Eng. 9, 52–55.

Mohammadi, S., Moller, H. E., Kugel, H., Muller, D. K., and Deppe, M. (2010). Correcting eddy current and motion effects by afﬁne whole-brain registrations: evaluation of threedimensional distortions and comparison with slicewise correction. Magn. Reson. Med. 64, 1047–1056.

Mohammadi, S., Nagy, Z., Hutton, C., Josephs, O., and Weiskopf, N. (2012). Correction of vibration artifacts in DTI using phase-encoding reversal (COVIPER). Magn. Reson. Med. 68, 882–889.

Mori, S. (2007). Introduction to Diffusion Tensor Imaging. Amsterdam: Elsevier Science.

Mori, S., and Barker, P. B. (1999). Diffusion magnetic resonance imaging: its principle and applications. Anat. Rec. 257, 102–109.

Mori, S., Crain, B. J., Chacko, V. P., and van Zijl, P. C. (1999). Threedimensional tracking of axonal projections in the brain by magnetic resonance imaging. Ann. Neurol. 45, 265–269.

Mori, S., and van Zijl, P. C. (2002). Fiber tracking: principles and strategies– a technical review. NMR Biomed. 15, 468–480.

Mori, S., and Zhang, J. (2006). Principles of diffusion tensor imaging and its applications to basic neuroscience research. Neuron 51, 527–539.

Moritani, T., Ekholm, S., and Westesson, P. (2005). DiffusionWeighted MR Imaging of the Brain. Berlin, Heidelberg: Springer.

Moriya, J., Kakeda, S., Abe, O., Goto, N., Yoshimura, R., Hori, H., et al. (2010). Gray and white matter volumetric and diffusion tensor imaging (DTI) analyses in the early stage of ﬁrst-episode schizophrenia. Schizophr. Res. 116, 196–203.

Moseley, M., Bammer, R., and Illes, J. (2002). Diffusion-tensor imaging of cognitive performance. Brain Cogn. 50, 396–413.

Moseley, M. E., Cohen, Y., Mintorovitch, J., Chileuitt, L., Shimizu, H., Kucharczyk, J., et al. (1990). Early detection of regional cerebral ischemia in cats: comparison of diffusion- and T2-weighted MRI and spectroscopy. Magn. Reson. Med. 14, 330–346.

Mukherjee, P., Berman, J. I., Chung, S. W., Hess, C. P., and Henry, R. G. (2008a). Diffusion tensor MR imaging and ﬁber tractography: theoretic underpinnings. AJNR. Am. J. Neuroradiol. 29, 632–641.

Mukherjee, P., Chung, S. W., Berman, J. I., Hess, C. P., and Henry, R. G. (2008b). Diffusion tensor MR imaging and ﬁber tractography: technical considerations. AJNR. Am. J. Neuroradiol. 29, 843–852.

Mukherjee, P., Hess, C. P., Xu, D., Han, E. T., Kelley, D. A., and Vigneron, D. B. (2008c). Development and initial evaluation of 7-T q-ball imaging of the human brain. Magn. Reson. Imaging 26, 171–180.

Nana, R., Zhao, T., and Hu, X. (2008). Single-shot multiecho parallel echo-planar imaging (EPI) for diffusion tensor imaging (DTI) with improved signal-to-noise ratio (SNR) and reduced distortion. Magn. Reson. Med. 60, 1512–1517.

Nolte, U. G., Finsterbusch, J., and Frahm, J. (2000). Rapid isotropic diffusion mapping without susceptibility artifacts: whole brain studies using diffusion-weighted singleshot STEAM MR imaging. Magn. Reson. Med. 44, 731–736.

Nowinski, W. L., Chua, B. C., Yang, G. L., and Qian, G. Y. (2012). Threedimensional interactive and stereotactic human brain atlas of white matter tracts. Neuroinformatics 10, 33–55.

Nucifora, P. G., Verma, R., Lee, S. K., and Melhem, E. R. (2007). Diffusion-tensor MR imaging and tractography: exploring brain microstructure and connectivity. Radiology 245, 367–384.

Oishi, K., Faria, A. V., Zijl, P. C. M., and Mori, S. (2010). MRI Atlas of Human White Matter. London: Academic Press.

Oishi, K., Zilles, K., Amunts, K., Faria, A., Jiang, H., Li, X., et al. (2008). Human brain white matter atlas: identiﬁcation and assignment of common anatomical structures in superﬁcial white matter. Neuroimage 43, 447–457.

Ordidge, R. J., Helpern, J. A., Qing, Z. X., Knight, R. A., and Nagesh,

V. (1994). Correction of motional artifacts in diffusion-weighted MR images using navigator echoes. Magn. Reson. Imaging 12, 455–460.

Papademetris, X., Jackowski, M., Rajeevan, N., Constable, R. T., and Staib, L. (2005). “Bioimage Suite: an integrated medical image analysis suite,” in The Insight Journal – 2005 MICCAI Open-Source Workshop (Palm Springs, CA).

Park, H. J., Kubicki, M., Shenton, M. E., Guimond, A., McCarley, R. W., Maier, S. E., et al. (2003). Spatial normalization of diffusion tensor MRI usingmultiple channels. Neuroimage 20, 1995–2009.

Park, H. J., Shenton, M. E., and Westin, C. F. (2004). “An analysis tool for quantiﬁcation of diffusion tensor imaging,” in Seventh International Conference on Medical Image Computing and ComputerAssisted Intervention (MICCAI’04) (Saint-Malo), 1040–1041.

Parker, G. J., Haroon, H. A., and Wheeler-Kingshott, C. A. (2003). A framework for a streamline-based probabilistic index of connectivity (PICo) using a structural interpretation of MRI diffusion measurements. J. Magn. Reson. Imaging 18, 242–254.

Patel, V., Dinov, I. D., Van Horn, J. D., Thompson, P. M., and Toga, A. W. (2010). LONI MiND: metadata in NIfTI for DWI. Neuroimage 51, 665–676.

Pfefferbaum, A., Adalsteinsson, E., and Sullivan, E. V. (2003). Replicability of diffusion tensor imaging measurements of fractional anisotropy and trace in brain. J. Magn. Reson. Imaging 18, 427–433.

Pieper, S., Lorensen, B., Schroeder, W., and Kikinis, R. (2006). “The NAMIC kit: ITK, VTK, pipelines, grids and 3D slicer as an open platform for the medical image computing community,” in Proceedings of the IEEE International Symposium on Biomedical ImagingISBI (Arlington, TX), 698–701.

Pierpaoli, C., and Basser, P. J. (1996). Toward a quantitative assessment of diffusion anisotropy. Magn. Reson. Med. 36, 893–906.

Pierpaoli, C., Jezzard, P., Basser, P. J., Barnett, A., and Di Chiro, G. (1996). Diffusion tensor MR imaging of the human brain. Radiology 201, 637–648.

Pierpaoli, C., Walker, L., Irfanoglu, M. O., Barnett, A., Basser, P., Chang, L. C., et al. (2010). “TORTOISE: an integrated software package for processing of diffusion MRI data,” in ISMRM 18th Annual Meeting (Stockholm).

Pipe, J. G. (1999). Motion correction with PROPELLER MRI: application to head motion and free-breathing cardiac imaging. Magn. Reson. Med. 42, 963–969.

Pipe, J. G., Farthing, V. G., and Forbes, K. P. (2002). Multishot diffusionweighted FSE using PROPELLER MRI. Magn. Reson. Med. 47, 42–52.

Polders, D. L., Leemans, A., Hendrikse, J., Donahue, M. J., Luijten, P. R., and Hoogduin, J. M. (2011). Signal to noise ratio and uncertainty in diffusion tensor imaging at 1.5, 3.0, and 7.0 Tesla. J. Magn. Reson. Imaging 33, 1456–1463.

Propper, R. E., O’Donnell, L. J., Whalen, S., Tie, Y., Norton, I. H., Suarez, R. O., et al. (2010). A combined fMRI and DTI examination of functional language lateralization and arcuate fasciculus structure: effects of degree versus direction of hand preference. Brain Cogn. 73, 85–92.

Pruessmann, K. P., Weiger, M., Scheidegger, M. B., and Boesiger, P. (1999). SENSE: sensitivity encoding for fast MRI. Magn. Reson. Med. 42, 952–962.

Reese, T. G., Heid, O., Weisskoff, R. M., and Wedeen, V. J. (2003). Reduction of eddy-current-induced distortion in diffusion MRI using a twicerefocused spin echo. Magn. Reson. Med. 49, 177–182.

Rohde, G. K., Barnett, A. S., Basser, P. J., Marenco, S., and Pierpaoli, C. (2004). Comprehensive approach for correction of motion and distortion in diffusion-weighted MRI. Magn. Reson. Med. 51, 103–114.

Rosset, A., Spadola, L., and Ratib, O. (2004). OsiriX: an open-source software for navigating in multidimensional DICOM images. J. Digit. Imaging 17, 205–216.

Seifert, M. H., Jakob, P. M., Jellus, V., Haase, A., and Hillenbrand, C. (2000). High-resolution diffusion imaging using a radial turbospin-echo sequence: implementation, eddy current compensation, and self-navigation. J. Magn. Reson. 144, 243–254.

Smith, S. M., Jenkinson, M., JohansenBerg, H., Rueckert, D., Nichols, T. E., MacKay, C. E., et al. (2006). Tract-based spatial statistics: voxelwise analysis of multi-subject diffusion data. Neuroimage 31, 1487–1505.

Smith, S. M., Jenkinson, M., Woolrich, M. W., Beckmann, C. F., Behrens, T. E., Johansen-Berg, H., et al. (2004). Advances in functional and structural MR image analysis and

implementation as FSL. Neuroimage 23(Suppl. 1), S208–S219.

Snook, L., Plewes, C., and Beaulieu, C. (2007). Voxel based versus region of interest analysis in diffusion tensor imaging of neurodevelopment. Neuroimage 34, 243–252.

Song, S. K., Sun, S. W., Ramsbottom, M. J., Chang, C., Russell, J., and Cross, A. H. (2002). Dysmyelination revealed through MRI as increased radial (but unchanged axial) diffusion of water. Neuroimage 17, 1429–1436.

Stehling, M. K., Turner, R., and Mansﬁeld, P. (1991). Echo-planar imaging: magnetic resonance imaging in a fraction of a second. Science 254, 43–50.

Sundgren, P. C., Dong, Q., GomezHassan, D., Mukherji, S. K., Maly, P., and Welsh, R. (2004). Diffusion tensor imaging of the brain: review of clinical applications. Neuroradiology 46, 339–350.

Tang, C. Y., Friedman, J., Shungu, D., Chang, L., Ernst, T., Stewart, D., et al. (2007). Correlations between Diffusion Tensor Imaging (DTI) and Magnetic Resonance Spectroscopy (1H MRS) in schizophrenic patients and normal controls. BMC Psychiatry 7:25. doi: 10.1186/1471-244X-7-25

Taylor, D. G., and Bushell, M. C. (1985). The spatial mapping of translational diffusion coefﬁcients by the NMR imaging technique. Phys. Med. Biol. 30, 345–349.

Tensaouti, F., Lahlou, I., Clarisse, P., Lotterie, J. A., and Berry, I. (2011). Quantitative and reproducibility study of four tractography algorithms used in clinical routine. J. Magn. Reson. Imaging 34, 165–172.

Thomason, M. E., Dougherty, R. F., Colich, N. L., Perry, L. M., Rykhlevskaia, E. I., Louro, H. M., et al. (2010). COMT genotype affects prefrontal white matter pathways in children and adolescents. Neuroimage 53, 926–934.

Thomason, M. E., and Thompson, P. M. (2011). Diffusion imaging, white matter, and psychopathology. Annu. Rev. Clin. Psychol. 7, 63–85.

Tournier, J. D., Calamante, F., and Connelly, A. (2012). MRtrix: diffusion tractography in crossing ﬁber regions. Int. J. Imaging Syst. Technol. 22, 53–66.

Tournier, J. D., Mori, S., and Leemans, A. (2011). Diffusion tensor imaging and beyond. Magn. Reson. Med. 65, 1532–1556.

Toussaint, N., Souplet, J. C., and Fillard, P. (2007). “MedINRIA:

medical image navigation and research tool by INRIA,” in Workshop on Interaction in Medical Image Analysis and Visualization (Brisbane, QLD).

Truong, T. K., Chen, B., and Song, A. W. (2008). Integrated SENSE DTI with correction of susceptibilityand eddy current-induced geometric distortions. Neuroimage 40, 53–58.

Truong, T.-K., Chen, N.-K., and Song, A. W. (2011). Dynamic correction of artifacts due to susceptibility effects and time-varying eddy currents in diffusion tensor imaging. Neuroimage 57, 1343–1347.

Tuch, D. S. (2004). Q-ball imaging. Magn. Reson. Med. 52, 1358–1372.

Tuch, D. S., Reese, T. G., Wiegell, M. R., Makris, N., Belliveau, J. W., and Wedeen, V. J. (2002). High angular resolution diffusion imaging reveals intravoxel white matter ﬁber heterogeneity. Magn. Reson. Med. 48, 577–582.

Turner, R., Le Bihan, D., and Chesnick, A. S. (1991). Echo-planar imaging of diffusion and perfusion. Magn. Reson. Med. 19, 247–253.

Van Den Heuvel, M., Mandl, R., Luigjes, J., and Hulshoff Pol, H. (2008). Microstructural organization of the cingulum tract and the level of default mode functional connectivity. J. Neurosci. 28, 10844–10851.

Van Den Heuvel, M. P., Mandl, R. C., Kahn, R. S., and Hulshoff Pol, H. E. (2009). Functionally linked restingstate networks reﬂect the underlying structural connectivity architecture of the human brain. Hum. Brain Mapp. 30, 3127–3141.

Van Hecke, W., Leemans, A., De Backer, S., Jeurissen, B., Parizel, P. M., and Sijbers, J. (2010). Comparing isotropic and anisotropic smoothing for voxel-based DTI analyses: a simulation study. Hum. Brain Mapp. 31, 98–114.

Vilanova, A., Zhang, S., Kindlmann, G., and Laidlaw, D. (2006). “An introduction to visualization of diffusion tensor imaging and its applications,” in Visualization and Processing of Tensor Fields, eds J. Weickert and H. Hagen (Berlin, Heidelberg: Springer), 121–153. Voineskos, A. N., Rajji, T. K., Lobaugh, N. J., Miranda, D., Shenton, M. E., Kennedy, J. L., et al. (2012). Age-related decline in white matter tract integrity and cognitive performance: a DTI tractography and structural equation modeling study. Neurobiol. Aging 33, 21–34.

Vos, S. B., Jones, D. K., Jeurissen, B., Viergever, M. A., and Leemans,

A. (2012). The inﬂuence of complex white matter architecture on the mean diffusivity in diffusion tensor MRI of the human brain. Neuroimage 59, 2208–2216.

Wakana, S., Caprihan, A., Panzenboeck, M. M., Fallon, J. H., Perry, M., Gollub, R. L., et al. (2007). Reproducibility of quantitative tractography methods applied to cerebral white matter. Neuroimage 36, 630–644.

Wakana, S., Jiang, H., Nagae-Poetscher, L. M., van Zijl, P. C., and Mori, S. (2004). Fiber tract-based atlas of human white matter anatomy. Radiology 230, 77–87.

Wang, J. J., Durazzo, T. C., Gazdzinski, S., Yeh, P. H., Mon, A., and Meyerhoff, D. J. (2009). MRSI and DTI: a multimodal approach for improved detection of white matter abnormalities in alcohol and nicotine dependence. NMR Biomed. 22, 516–522.

Wang, J. Y., Abdi, H., Bakhadirov, K., Diaz-Arrastia, R., and Devous, M. D. Sr. (2011). A comprehensive reliability assessment of quantitative diffusion tensor tractography. Neuroimage 60, 1127–1138.

Wang, R., Benner, T., Sorensen, A. G., and Wedeen, V. J. (2007). “Diffusion toolkit: a software package for diffusion imaging data processing and tractography,” in Proceedings of the International Society for Magnetic Resonance in Medicine (Berlin), 3720.

Wedeen, V. J., Rosene, D. L., Wang, R., Dai, G., Mortazavi, F., Hagmann, P., et al. (2012). The geometric structure of the brain ﬁber pathways. Science 335, 1628–1634.

Wedeen, V. J., Wang, R. P., Schmahmann, J. D., Benner, T., Tseng, W. Y., Dai, G., et al. (2008). Diffusion spectrum magnetic resonance imaging (DSI) tractography

of crossing ﬁbers. Neuroimage 41, 1267–1277.

Weinstein, D. M., Kindlmann, G. L., and Lundberg, E. C. (1999). “Tensorlines: advection-diffusion based propagation through diffusion tensor ﬁelds,” in Proceedings of the 10th IEEE Visualization 1999 Conference (VIS’99) (San Francisco, CA: IEEE Computer Society).

Westin, C. F., Maier, S. E., Mamata, H., Nabavi, A., Jolesz, F. A., and Kikinis, R. (2002). Processing and visualization for diffusion tensor MRI. Med. Image Anal. 6, 93–108.

White, T., Nelson, M., and Lim, K. O. (2008). Diffusion tensor imaging in psychiatric disorders. Top. Magn. Reson. Imaging 19, 97–109.

Wiegell, M. R., Larsson, H. B., and Wedeen, V. J. (2000). Fiber crossing in human brain depicted with diffusion tensor MR imaging. Radiology 217, 897–903.

Xing, D., Papadakis, N. G., Huang, C. L., Lee, V. M., Carpenter, T. A., and Hall, L. D. (1997). Optimised diffusion-weighting for measurement of apparent diffusion coefﬁcient (ADC) in human brain. Magn. Reson. Imaging 15, 771–784.

Xu, D., Henry, R. G., Mukherjee, P., Carvajal, L., Miller, S. P., Barkovich, A. J., et al. (2004). Single-shot fast spin-echo diffusion tensor imaging of the brain and spine with head and phased array coils at 1.5 T and 3.0 T. Magn. Reson. Imaging 22, 751–759.

Xu, D., Mori, S., Shen, D., Van Zijl, P. C., and Davatzikos, C. (2003). Spatial normalization of diffusion tensor ﬁelds. Magn. Reson. Med. 50, 175–182.

Yakushev, I., Schreckenberger, M., Muller, M. J., Schermuly, I., Cumming, P., Stoeter, P., et al. (2011). Functional implications of

hippocampal degeneration in early Alzheimer’s disease: a combined DTI and PET study. Eur. J. Nucl. Med. Mol. Imaging 38, 2219–2227.

Yamada, K., Sakai, K., Akazawa, K., Yuen, S., and Nishimura, T. (2009). MR tractography: a review of its clinical applications. Magn. Reson. Med. Sci. 8, 165–174.

Yang, E., Nucifora, P. G., and Melhem, E. R. (2011). Diffusion MR imaging: basic principles. Neuroimaging Clin. N. Am. 21, 1–25.

Zalesky, A. (2011). Moderating registration misalignment in voxelwise comparisons of DTI data: a performance evaluation of skeleton projection. Magn. Reson. Imaging 29, 111–125.

Zhang, H., Yushkevich, P. A., and Gee, J. C. (2009). “DTI toolkit: a spatial normalization and atlas construction toolkit optimized for examining white matter morphometry using DTI data,” in International Society for Magnetic Resonance in Medicine (Honolulu, HI).

Zhang, Y., Zhang, J., Oishi, K., Faria, A. V., Jiang, H., Li, X., et al. (2010). Atlas-guided tract reconstruction for automated and comprehensive examination of the white matter anatomy. Neuroimage 52, 1289–1301.

- Zhou, Y., Qun, X., Qin, L. D., Qian, L. J., Cao, W. W., and Xu, J. R. (2011a). A primary study of diffusion tensor imaging-based histogram analysis in vascular cognitive impairment with no dementia. Clin. Neurol. Neurosurg. 113, 92–97.
- Zhou, Z., Liu, W., Cui, J., Wang, X., Arias, D., Wen, Y., et al. (2011b). Automated artifact detection and removal for improved tensor estimation in motion-corrupted DTI data sets using the combination of local binary patterns and 2D partial least squares. Magn. Reson. Imaging 29, 230–242.

Zhu, T., Hu, R., Qiu, X., Taylor, M., Tso, Y., Yiannoutsos, C., et al. (2011). Quantiﬁcation of accuracy and precision of multi-center DTI measurements: a diffusion phantom and human brain study. Neuroimage 56, 1398–1411.

Zhuang, J., Hrabe, J., Kangarlu, A., Xu, D., Bansal, R., Branch, C. A., et al. (2006). Correction of eddycurrent distortions in diffusion tensor images using the known directions and strengths of diffusion gradients. J. Magn. Reson. Imaging 24, 1188–1193.

Zwiers, M. P. (2010). Patching cardiac and head motion artefacts in diffusion-weighted images. Neuroimage 53, 565–575.

Conﬂict of Interest Statement: The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

Received: 09 November 2012; paper pending published: 22 December 2012; accepted: 23 February 2013; published online: 12 March 2013. Citation: Soares JM, Marques P, Alves V and Sousa N (2013) A hitchhiker’s guide to diffusion tensor imaging. Front. Neurosci. 7:31. doi: 10.3389/fnins. 2013.00031 This article was submitted to Frontiers in Brain Imaging Methods, a specialty of Frontiers in Neuroscience. Copyright © 2013 Soares, Marques, Alves and Sousa. This is an openaccess article distributed under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in other forums, provided the original authors and source are credited and subject to any copyright notices concerning any third-party graphics etc.

