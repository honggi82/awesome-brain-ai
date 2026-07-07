# BrainNet Viewer: A Network Visualization Tool for Human Brain Connectomics

Mingrui Xia*, Jinhui Wang, Yong He*

State Key Laboratory of Cognitive Neuroscience and Learning, Beijing Normal University, Beijing, China

|Abstract<br><br>The human brain is a complex system whose topological organization can be represented using connectomics. Recent studies have shown that human connectomes can be constructed using various neuroimaging technologies and further characterized using sophisticated analytic strategies, such as graph theory. These methods reveal the intriguing topological architectures of human brain networks in healthy populations and explore the changes throughout normal development and aging and under various pathological conditions. However, given the huge complexity of this methodology, toolboxes for graph-based network visualization are still lacking. Here, using MATLAB with a graphical user interface (GUI), we developed a graph-theoretical network visualization toolbox, called BrainNet Viewer, to illustrate human connectomes as ball-and-stick models. Within this toolbox, several combinations of defined files with connectome information can be loaded to display different combinations of brain surface, nodes and edges. In addition, display properties, such as the color and size of network elements or the layout of the figure, can be adjusted within a comprehensive but easy-to-use settings panel. Moreover, BrainNet Viewer draws the brain surface, nodes and edges in sequence and displays brain networks in multiple views, as required by the user. The figure can be manipulated with certain interaction functions to display more detailed information. Furthermore, the figures can be exported as commonly used image file formats or demonstration video for further use. BrainNet Viewer helps researchers to visualize brain networks in an easy, flexible and quick manner, and this software is freely available on the NITRC website (www.nitrc.org/projects/bnv/).<br><br>Citation: Xia M, Wang J, He Y (2013) BrainNet Viewer: A Network Visualization Tool for Human Brain Connectomics. PLoS ONE 8(7): e68910. doi:10.1371/ journal.pone.0068910<br><br>Editor: Peter Csermely, Semmelweis University, Hungary Received April 19, 2013; Accepted June 8, 2013; Published July 4, 2013 Copyright: 2013 Xia et al. This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.<br><br>Funding: This study was supported by the Natural Science Foundation (Grant Nos. 81030028 and 30870667), the National Science Fund for Distinguished Young Scholars (Grant No. 81225012, YH), and Beijing Natural Science Foundation (Grant No. Z111107067311036 and 7102090). The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.<br><br>Competing Interests: The authors have declared that no competing interests exist.<br><br>* E-mail: mxia@mail.bnu.edu.cn (MX); yong.he@bnu.edu.cn (YH)|
|---|

Introduction

The human brain is naturally organized into a complex system whose topological descriptions have been represented as a structural connectome [1] of interconnected cortico-cortical axonal pathways and a functional connectome [2] of synchronized interregional neural activity. Mapping the human brain connectome and uncovering its underlying organizational principles are fundamentally important in neuroanatomy, neurodevelopment, cognitive neuroscience and neuropsychology. Recent studies have suggested that the human brain connectome can be mapped using neuroimaging data and further characterized through sophisticated analytic strategies based on graph theory [3–5].

Graph theoretical approaches model the human brain as collectives of nodes linked by edges, of which the nodes typically represent brain regions or voxels in neuroimaging data, while the edges are often estimated by gray matter morphological correlation [6,7] or white matter fiber connections [8,9] in structural data and temporal correlations [10–12] in functional data. Once the brain nodes and edges are extracted from the neuroimaging data, graph theoretical algorithms are further applied to measure the topological properties of the constructed networks. The application of these algorithms revealed many non-trivial topological properties of brain networks, such as small-worldness [13], modularity [14,15], highly connected hubs [8,16] and ‘rich-club’

configurations [17,18]. To date, graph theoretical methods have been used to examine the relationships between human brain network properties and population attributes, such as aging [19– 24], development [25–34], gender [19,34–37], intelligence [34,38,39] and genetic [40–43]. Moreover, these graph-based network analysis methods have been applied to individuals with a variety of neuropsychiatric disorders [44–47], including Alzheimer’s disease (AD) [48–50], mild cognitive impairment (MCI) [51– 53], schizophrenia [54–56] and epilepsy [57,58].

Given the abstract nature of graph theoretical approaches and the huge complexity of brain networks, it is important to develop easy-to-use and efficient toolkits for graph-based network construction, analysis and/or visualization. Recently, several freely available toolkits for extracting brain network topological properties have emerged, including Brain Connectivity Toolbox (BCT) [59], eConnectome [60], Graph-Analysis Toolbox (GAT) [61], Pipeline for Analyzing braiN Diffusion imAges (PANDA) [62], NetworkX (http://networkx.lanl.gov/index.html), Brainwaver (http://cran.r-project.org/web/packages/brainwaver/index. html) and Graph-theoRETical Network Analysis toolkit (GRETNA, http://www.nitrc.org/projects/gretna/), which have greatly assisted with the investigation of the brain connectome. However, toolkits for visualizing the brain connectome as nodes and edges are still lacking.

Here, we developed a MATLAB toolbox, called BrainNet Viewer, with a Graphical User Interface (GUI), to provide a flexible and rapid visualization platform and generate figures for brain connectome studies in a user-friendly and intuitive manner. In this toolbox, the brain surface, node, edge and volume files can be defined as input containing fundamental information about brain networks, and we have designed an easy-to-use optional panel to modify the details of the network display. BrainNet Viewer automatically generates the figures as the user requires, and these figures can be saved as several common image formats for further use. Moreover, interaction functions are available to facilitate the demonstration of more detailed information.

Materials and Methods Toolbox Development

Developing environment. BrainNet Viewer was developed using MATLAB (The MathWorks Inc., Natick, MA, US) as a programming language, with a user-friendly GUI (Figure 1), under a 64-bit Windows (Microsoft Corp., Redmond, WA, US) environment. The toolbox includes functions of Statistical Parametric Mapping 8 (SPM, http://www.fil.ion.ucl.ac.uk/spm/ ) for loading NIfTI and Analyze format files (*.nii; *.img). This toolbox has been successfully tested under a variety of operating systems with MATLAB installed, including Windows (XP, 7, 8 and Server versions), Linux (Ubuntu and CentOS) and Mac OS in both 32- and 64-bit versions.

Visualization procedure. BrainNet Viewer was designed to visualize brain connectomes using the following procedure. First, users upload a combination of files containing connectome information, such as a brain surface, node, edge and volume files. Then, an easy-to-use options panel appears, allowing the adjustment of figure configuration parameters, such as output layout, background color, surface transparency, node color and size, edge color and size and image resolution. Subsequently, BrainNet Viewer draws the brain surface, nodes and edges (depending on the files loaded) in sequence and shows the brain network in multiple views, as required by the user. Finally, the figures are exported to common image file formats for further use (see Figure 2 for a flowchart).

File definition. We defined four types of import files for BrainNet Viewer, namely, brain surface, node, edge and volume files. 1) Brain surface file. The brain surface file is an ASCII text file, with the suffix ‘nv’, containing four fields: the number of vertices, the coordinates of each vertex, the number of triangle faces and the index of the vertices comprising the triangles. Currently, the ‘.pial’ file of hemisphere mesh, generated using FreeSurfer (http://surfer.nmr.mgh.harvard.edu/) [63], and the ‘.mesh’ files, generated using BrainVISA (http://brainvisa.info/) [64], are supported for direct loading and visualization. 2) Node file. The node file is an ASCII text file with the suffix ‘node’. Nodal information is arranged in 6 columns in the node file: columns 1–3 represent the x, y and z coordinates, respectively, of the nodes; column 4 represents the index for node color; column 5 represents the node size; and column 6 represents the node label. A ‘2’ symbol (no ‘’) in column 6 indicates no label for the corresponding node. The values for this file are easily arranged depending on the aspects of the network shown. For example, the modular information for the nodes can be assigned to column 4 to use color to distinguish nodes belonging to different modules. Column 5 could be set as nodal degree, centrality and T-value to emphasize nodal differences according to size. 3) Edge file. The brain edge file is an ASCII text file with the suffix ‘edge’, representing an association (e.g., correlations) matrix among the

nodes, which can be weighted or binarized, and therefore, the size of the matrix must correspond to the number of nodes. Both the node and edge files can be generated or edited using text editors or spreadsheet software. 4) Volume file. BrainNet Viewer facilitates the mapping of volume data to the brain surface, which can be a functional connectivity map, gray matter density map, statistical parametric map or a brain atlas. The volume file should be in the NIfTI or Analyze format, and either a single or paired nii files are acceptable. A text file containing an n61 vector is also acceptable, in which n equals the vertex number of the brain surface (e.g., 81,924 vertices in the International Consortium for Brain Mapping (ICBM) whole brain surface).

In BrainNet Viewer, several brain surface templates and files of example brain networks are provided. 1) The brain surface templates are primarily generated from two commonly used templates, including Ch2 (with/without cerebellum and separated hemispheres) and ICBM152 (smoothed/unsmoothed, MNI/Talaraich and separated hemispheres), which can be found in the folder ‘.\Data\SurfTemplate’. 2) The brain network files, including node and edge files, are generated from various brain parcellations, such as Automated Anatomical Labeling (AAL, 90 regions, only cerebrum) [65], Brodmann areas (82 regions) [66], Harvard-Oxford Atlas (HOA, 112 regions) [67], regions of interest (ROIs) defined by Dosenbach et al.(160 ROIs) [68], ROIs defined by Fair et al. (34 ROIs) [26] and LONI Probabilistic Brain Atlas (40 regions) [69], which are stored in the folder ‘.\Data\ExampleFiles’. Notably, the coordinates in these files are located in the MNI space, unless otherwise noted. Moreover, users are encouraged to create custom files of brain networks for visualizing specific characteristics of the brain connectome. Specifically, the customized brain surface can be extracted from anatomical data using surface reconstruction software, such as the FreeSurfer and BrainVISA. Subsequently, the number of vertices and triangle faces, vertex coordinates, and the index of the vertices in triangles of the resultant surface are stored as ASCII files with the suffix ‘.nv’ to generate a customized brain surface template. The network characteristics can be saved as ASCII files with either the ‘.node’ or ‘.edge’ suffix using text editor or Matlab commands, according to the previously described file rule definitions to generate customized network files.

Core codes. BrainNet Viewer manages brain network visualization in three ways: displaying graph theoretical networks as ball-and-stick models; performing volume-to-surface mapping; and constructing ROI clusters from volume files. Here, we introduce the core graphic functions in MATLAB that BrainNet Viewer uses for the visualization procedure.

The ball-and-stick model of the graph theoretical network includes three elements: brain surface, nodes and edges. 1) For the brain surface, once the vertex coordinates and triangles are loaded, the following function is used to draw the surface in a figure:

surf_h=trisurf(tri, x, y, z);

where surf_h is the handle of the object, tri represents the index of the vertex comprising the triangles, and x, y and z are the coordinates of the vertex on the surface. 2) The network nodes are represented as spheres. The sphere in a specific position (x, y, and z) is generated using the following codes:

[X, Y, Z]=sphere(n); X =X * r+x; Y =Y * r+y; Z=Z * r +z; node_h=mesh(X, Y, Z);

where X, Y and Z represent vertex coordinates of a unit sphere, n is the number of faces (n-by-n) on this sphere (in BrainNet Viewer, n represents the graph detail in the option panels, where 100, 50 and 20 represent high, moderate and low details,

[Figure 1]

- Figure 1. The main window of BrainNet Viewer. BrainNet Viewer is free software available on the NITRC website (www.nitrc.org/projects/bnv/), which runs with MATLAB under Windows, Linux and Mac OS, with either 32- or 64-bit systems. The latest version is 1.41, released September 18, 2012. The main window includes the menu bar, toolbar and contact information.

- doi:10.1371/journal.pone.0068910.g001

respectively), r is the size of the node, and node_h is the handle of the node. 3) Similar to nodes, cylinders are drawn in BrainNet Viewer to represent network edges. The cylinders are first generated and subsequently rotated and moved to the appropriate position in the following manner:

theta=(0:n)/n * 2 * pi; t=ones(100,1) * t; X =t * cos(theta); Y =t * sin(theta); Z=(0:100)’/(10021) *

ones(1,n +1) * length; line_h=mesh(X, Y, Z); rotate(line_h, axis_rot, angle_X1X2, [0 0 0]);

where theta is the radian of sampling points on a circle, n is the number of sampling points (similar to the node sampling detail, 20, 10 and 5 represent high, moderate and low details, respectively), t is the radius of the cylinder, X, Y and Z represent vertex coordinates on the cylinder, length is the distance between the two nodes connected by this edge, line_h is the handle of this edge, and axis_rot and angle_X1X2 are the vector cross product and the included angle between unit vector on the z-axis and the vector of the two nodes connected by this edge, respectively.

The procedure for volume-to-surface mapping first transfers the vertex coordinates on the brain surface to the matrix coordinates in the image file using different mapping algorithms and then assigns vertices with different values. Eight mapping algorithms are provided to determine the vertex values in BrainNet Viewer:

‘Nearest Voxel’, assign the vertex with the value of the voxel in volume that is nearest to it, suitable to display an atlas or mask; ‘Average Vertex’, assign the vertex with the value of the voxel in volume that is nearest to it, and then average the vertex across its neighbors (high time consumption); ‘Average Voxel’, assign the vertex with average value of the voxel and its neighbors in volume that is nearest to it; ‘Gaussian’, the volume first employs convolutions with a Gaussian kernel and then assigns the vertex with the value of the voxel in volume that is nearest to it; ‘Interpolated’, the coordinate of the vertex is determined in the volume space, and a trilinear interpolate method is then used across its neighbors to calculate the value; ‘Maximum Voxel’, assign the vertex with the maximum value of the voxel and its neighbors in volume that is nearest to it; ‘Minimum Voxel’, assign the vertex with the minimum value of the voxel and its neighbors in volume that is nearest to it; ‘Extremum Voxel’, assign the vertex with the extremum value of the voxel and its neighbors in volume that is nearest to it. The mapping code is similar to the surface drawing, which is represented as:

surfmap_h =trisurf(tri, x, y, z, v);

where surfmap_h is the handle of the object, tri represents the index of the vertices comprising the triangles, x, y and z are the coordinates of the vertex on the surface, and v represents the value of each vertex on the surface.

[Figure 2]

- Figure 2. A flowchart for visualization of BrainNet Viewer. First, the combination of the files containing connectome information is loaded. Then, the configuration of the graph is adjusted in an easy-to-use option panel. Next, BrainNet Viewer draws the brain surface, nodes and edges in sequence. Finally, the figure is saved in a common image format for further use.

- doi:10.1371/journal.pone.0068910.g002

BrainNet Viewer also provides functions to construct ROI clusters from volume files. The voxels within the same cluster are labeled with the same index number and are fully connected. Then, the toolbox identifies and constructs the cluster from volume to surface using the following codes:

fv=isosurface(vol); roi_h=trisurf(fv.faces,fv.vertices(:,1),fv.vertices(:,2),fv.verti-

ces(:,3));

where fv represents the surface information, containing vertex coordinates (fv.vertices) and triangle indices (fv.faces), constructed from ROI clusters; vol is the three-dimensional matrix containing ROI clusters; and roi_h is the handle of the ROI object. After these objects are created, several functions controlling object properties are used to adjust the appearance of these elements in the brain network, including EdgeColor, FaceAlpha, material, shading, lighting and camlight.

Functional Brain Network Visualization on Experimental Data

Subjects. To demonstrate the visualization effects of this toolbox on real data, we analyzed a published resting-state fMRI dataset. The dataset was downloaded from the 1000 Functional Connectomes Project (www.nitrc.org/projects/fcon_1000/), which is a worldwide multi-site project with fMRI data sharing for the imaging community. The resting-state images were acquired from 198 healthy right-handed volunteers (males, 76; females, 122; age, 18 - 26 years) at the scanning site of Beijing Normal University. The data for one subject were removed because of an orientation error during scanning. Each participant provided written informed consent before initiating scanning. The study was approved through the Institutional Review Board of the Beijing Normal University Imaging Center for Brain Research.

Image acquisition. The resting-state fMRI data acquisitions were performed on a Siemens 3T scanner. For each participant, functional images were scanned using the following parameters: repetition time=2000 ms, echo time=30 ms, in-plane resolu-

tion=3.125 mm63.125 mm, slice thickness =3 mm, number of slices=33, section gap=0.6 mm, flip angle =90u, field of view=200 mm6200 mm and time points=225. The participants were instructed to remain awake with their eyes closed during the scanning.

Image pre-processing. The image pre-processing was conducted using DPARSF [70] and SPM5 (www.fil.ion.ucl.ac.uk/ spm/). The first 10 volumes of each participant were removed to for the adaptation of the participants to the scanning noise. The following pre-processing steps included slice timing, realignment, spatial normalizing to the standard EPI template in MNI space and resampling to an isotropic 3-mm voxel size, spatially smoothing with a 4-mm FWHM kernel, detrending and bandpass filtering (0.01 - 0.08 Hz). Furthermore, we regressed out the white matter (WM), cerebrospinal fluid (CSF), global signals, and head-motion profiles to reduce the effect of these nuisance signals.

Network construction. We constructed the functional brain networks for each individual using two methods, differentiated according to the node definition, as either a region- or voxel-based network. 1) The region-based networks were constructed following the following manner. First, the AAL atlas was used to parcellate the entire brain into 90 regions (regions in cerebellum were excluded), which were considered as nodes in the network. Then, the mean time courses were extracted from each region and used to obtain a 90690 correlation matrix of Pearson’s correlation coefficients between all possible connections of node pairs. 2) The voxel-based networks were constructed by directly considering GM voxels as nodes. The Pearson’s correlation coefficients were then computed between the time courses of all pairs of voxels to generate a ,50,000650,000 correlation matrix. All correlation matrices were transferred into z-score matrices using Fisher’s r-to-z transformation to improve normality.

Network analysis. We analyzed the region-based networks at the group level. First, we performed one sample t-tests for all possible connections across all subjects, and the t-values were considered as the strength of connections. Then, a Bonferronicorrected significance level of P,0.05 was used to remove the non-significant connections and obtain a group-level weighted functional matrix (network). Notably, the negative correlations were excluded because of biological ambiguity. Subsequently, a modular detection algorithm [14] was applied to the resultant weighted network to identify functional modules. Finally, we calculated the functional connectivity strength (FCS; i.e., nodal strength) for each node by summing the connections (t-score) linked, and the resultant FCS values were further normalized to standard Z-scores (the minus mean and divided by the standard deviation (SD)). The nodes with a Z-score higher than 1 were identified as network hubs.

For the voxel-based network analysis, the FCS in the brain functional network of each subject was calculated. The FCS of a voxel was computed as the sum of the connections (z-score) between the given voxel and all other voxels. We conservatively restricted the analysis to positive correlations above a threshold of r=0.2. The FCS maps were averaged across subjects, and the resultant mean FCS map was further normalized (the minus mean and divided by the SD) to exhibit the hub distribution of brain functional networks on a group level. Given a high computational load, we did not analyze the other network properties, such as modularity.

Results Toolbox Development

Download and installation. The BrainNet Viewer package is available as a free download from the NITRC website

(www.nitrc.org/projects/bnv/), and this software is also listed among the SPM extensions (www.fil.ion.ucl.ac.uk/spm/ ext/#BrainNetViewer). The BrainNet Viewer has been downloaded over 4,400 times from the NITRC website since it was released on July 7, 2011. The installation of BrainNet Viewer is similar to most MATLAB toolboxes. To run this package, open MATLAB, add the BrainNet Viewer folder in the MATLAB search path, and type ‘BrainNet’ in the command window of MATLAB. In addition, a user-friendly manual is also available within the package, providing a detailed guide for using BrainNet Viewer.

Combinations of files. Although four types of input files are defined for BrainNet Viewer, it is not necessary to load all files types at one time. Instead, several combinations are acceptable, and different combinations will generate different network pictures. These combinations include 1) brain surface file only; 2) node file only; 3) brain surface and node files; 4) node and edge files; 5) brain surface, node and edge files; 6) brain surface and volume files for volume-to-surface mapping or ROI cluster drawing; 7) brain surface, node and volume files; and 8) brain surface, node, edge and volume files. Figure 3 shows the sample images generated using these different combinations.

Option setting. We developed an option panel (Figure 4) in BrainNet Viewer for adjusting the details of the figure intuitively and easily. The option panel is divided into seven subpanels, corresponding to different aspects of the figure, including layout, global, surface, node, edge, volume and image, switched from the list box on the left of the panel. In addition, the configuration in this panel can be saved as a.mat file and recalled at next use or in a command line (see Command line section). These panels are briefly defined using the following description.

- 1) Layout panel. The layout panel (Figure 4A) is primarily responsible for setting the output view of the brain model, in which three types of views are provided: the single view shows only one brain model in the figure (Figure 5A); the medium view shows the lateral and medial sides of each hemisphere in the figure (Figure 5B); and the full view shows all sides of the brain surface. Depending on whether the inputted brain surface can be divided into two hemispheres, the layout panel shows brain models in two ways: if not dividable, the left, right, dorsal, ventral, anterior and posterior sides are displayed separately (Figure 5C); otherwise, the lateral and medial sides of each hemisphere, the dorsal and ventral sides, and the anterior and posterior sides of the entire brain are shown (Figure 5D).
- 2) Global panel. The global panel (Figure 4B) provides several different choices for the adjustment of the global figure, particularly the display properties of these objects. Here, users can change the color of the background, select material for the objects (Figure 6A), change shading properties (Figure 6B), select the lighting algorithm (Figure 6C), determine where the light comes from (Figure 6D), change the rendering method and set the graph details (e.g., set the number of sampling points for nodes and edges).
- 3) Surface panel. The surface panel is available for adjusting the properties of the brain surface. The surface panel is simple, with only three options: the surface color, the opacity of the surface and a switch for displaying the interaction of two brains in one figure (Figure 7).
- 4) Nodal panel. The node panel (Figure 4C) is developed with four zones to select node drawing, set labels, and adjust the node size and color, respectively. All settings are dependent on the nodal information in the nodal file. Users can draw all

[Figure 3]

- Figure 3. Pictures generated from different file combinations. The file combinations that BrainNet Viewer accepts include the following: (A) brain surface only; (B) nodes only; (C) brain surface with nodes; (D) nodes and edges; (E) brain surface with nodes and edges; (F) brain surface and volume files for volume-to-surface mapping; (G) brain surface, nodes and volume files for volume-to-surface mapping with nodes; (H) brain surface, nodes, edges and volume files for volume-to-surface mapping with nodes and edges; and (I) brain surface and volume files for regions of interest construction.

- doi:10.1371/journal.pone.0068910.g003

nodes contained in the nodal file or select a subset by setting a threshold for the value of column 4 or column 5 in the nodal file. The nodes with higher values than the threshold will be shown. The labels for these nodes can be added using the text of column 6 in the node file, and the font type and size can be selected. BrainNet Viewer provides three ways to adjust the node size: automatically arrange the sizes of the nodes to a proper range, according to nodal size in the node file; use the original value in the node file; or set all nodes to an equal size defined in the panel ignoring the size value in the file. Node color can be adjusted in four ways: using the same color for all nodes, ignoring the color index in the file; using a color map to display the values of the nodes from low to high, corresponding to the color index in the node file; assigning distinct colors for nodes labeled with different modular indices in column 4 of the node file; or binarizing the color to a given threshold.

5) Edge panel. The edge panel (Figure 4D) is similar to the node panel, with three parts that separately control edge extraction, edge size and edge color. The edges are extracted from the association matrix contained in the edge file by setting a

threshold of either a real value or sparsity (i.e., density or cost). BrainNet Viewer can also extract edges using an absolute value in the matrix or only edges that travel across two hemispheres. In addition, the asymmetric matrix can be used to draw edges with direction. There are three ways to adjust the radius of edges: automatically arrange the sizes of edges to a proper range according to the values in the association matrix in the edge file; use the original value of the association matrix; or set all edges to an equal radius defined in the panel, ignoring the size values in the file. BrainNet Viewer provides five ways to set edge color: adopt the same color for all edges; use a color map to render edges by their values from low to high; binarize the color by a given threshold for edge value; binarize the color by a given threshold of Euclidean distance between two nodes connected by this edge; or assign edge color according to the colors of the nodes that it links.

6) Volume panel. The volume panel (Figure 4E) is set to control the volume-to-surface mapping and draw ROI clusters with brain surface. In the volume-to-surface mapping section, the users perform mapping with positive, negative or both positive and negative values in the volume file. We provide 24 types of

[Figure 4]

- Figure 4. The option panel and its subpanels in BrainNet Viewer. (A) The layout panel is adopted to set the output view of the brain model. (B) The global panel is responsible for the adjustment of the display properties. (C) The node panel is developed to control node label, node size and node color. (D) The edge panel is employed to control edge extraction, edge size and edge color. (E) The volume panel is used for setting volume-tosurface mapping and regions of interest construction. (F) The image panel is applied for determining the parameters of the output image.

- doi:10.1371/journal.pone.0068910.g004

colorbars, including those most commonly used in research, such as jet, hsv, hot, cold, winter and summer. In addition, a custom colorbar can be generated using an n63 matrix. Eight mapping algorithms are available, as described in the Methods section, providing various effects for mapping. In the ROI drawing section, users select the index number and set the color of the ROI clusters that need to be reconstructed and drawn.

7) Image panel. In the image panel (Figure 4F), the configurations are related to the size and resolution of the output images. The width and height of the image can be adjusted in pixel dimensions for screen display or in real units (centimeter or inch) for document use. The resolution of the output image can also be modified in dots per inch (DPI).

User interaction. On the toolbar for the main window, some interactional operation functions, including zoom in, zoom out, move, rotate, data cursor, standard views and demonstration, were developed. The zoom in and zoom out functions help to observe the local or global status of the brain network. With ‘‘move’’ and ‘‘rotate’’ functions, users can move or change the view of the brain model by dragging with the mouse. The data cursor function displays the coordinates and value of the vertex on the surface, and it also provides the corresponding brain region labels in terms of AAL and Brodmann atlases (Figure 8). Shortcuts for three standard views, sagittal, axial and coronal, are available to quickly observe networks from different standard views. The demonstra-

tion function makes the brain model rotate clockwise until terminated by the user.

Output. The brain connectome figures can be saved as several common image formats, including TIFF, BMP, EPS, JPEG and PNG. Moreover, BrainNet Viewer can save the brain networks as videos, generating a 12 second long, 30 FPS, 7356534, AVI file, in which the brain network model rotates clockwise in a circle at one degree per frame. Generating these videos takes approximately 10 minutes (for an example, see www. nitrc.org/docman/view.php/504/1023/Demo%20Video%20of% 20Brain%20Network%20(14M)).

Command line. Considering the growing requirements for batched brain connectome figure mapping, such as dynamic brain functional connectomes, the functionality to generate brain network figures in the command line is provided. The function is called according to the following command line:

BrainNet_MapCfg(filename1, filename2…);

where the variables of filenames can be any one of the brain surface, node, edge and volume files. Once the files are loaded, BrainNet Viewer draws the graphs with default configurations. For instance, a command line of

BrainNet_MapCfg(‘BrainMesh_ICBM152.nv’, ‘Node_AAL90.node’); will draw the brain surface of ‘BrainMesh_ICBM152.nv’ and

nodes in ‘Node_AAL90.node’ files using default settings.

A pre-saved configuration file can also be included in this command line. For example, the command line.

[Figure 5]

- Figure 5. Different layouts of brain models. (A) The single view shows a single brain model in the figure as one of the three standard (sagittal, axial or coronal) views or a custom camera view. (B) The medium view shows the lateral and medial sides of each hemisphere in the figure. (C and D) The full view shows all sides of the brain surface. According to whether the brain surface file can be divided into two hemispheres, this mode displays brain models in two ways: (C) if not divisible, the left, right, dorsal, ventral, anterior and posterior sides are displayed separately; (D) otherwise, the lateral and medial sides of each hemisphere, and the dorsal and ventral sides and the anterior and posterior sides of the entire brain are shown.

- doi:10.1371/journal.pone.0068910.g005

BrainNet_MapCfg(‘BrainMesh_ICBM152_smoothed.nv’, ‘OneSample_T.nii’, ‘Cfg.mat’);

would map the volume ‘OneSample_T.nii’ onto brain surface ‘BrainMesh_ICBM152_smoothed.nv’ using the settings pre-saved in the ‘Cfg.mat’ file.

The command line also supports exporting the brain network figure as image file. The names of the required image files are added to the command line:

BrainNet_MapCfg(‘Node_AAL90.node’,’Edge_AAL90_Binary.edge’, ‘Net.jpg’);

Using this command, BrainNet Viewer draws a network in which the node information is obtained from ‘Node_AAL90.node’ and the edge information is obtained from ‘Edge_AAL90_Binary.edge’ using default settings, and this figure will be saved as a JPEG image as ‘Net.jpg’. The order of these inputted filenames is exchangeable, and the combinations of files are similar to the GUI version.

Functional Brain Network Visualization on Experimental Data

Biological findings and network visualization. Figure 9A illustrates the region-based functional network as ball-and-stick models. The coordinates of the nodes were centroids of the brain regions in the AAL atlas. The sizes of the nodes were assigned with a value for the nodal strength. Several hub regions were identified, including the bilateral Rolandic operculum, bilateral superior temporal gyrus, right supplementary motor area, right temporal pole, right supramarginal gyrus, left medial orbital superior frontal gyrus, bilateral insula and bilateral putamen, which were primarily located at the association and subcortical regions. In addition, five functional modules were identified in this network, and their nodes were rendered using different colors: the module in green comprises the regions in the default-mode network; the module in cyan comprises the regions predominantly involved in the attention and execution control; the module in red comprises the region of the sensorimotor cortex; the module in blue comprises the regions of the visual cortex; and the module in magenta comprises the regions of the subcortical nuclei.

[Figure 6]

- Figure 6. Demonstration of object properties. (A) Material property controls the reflectance properties of the surfaces, including choices of shiny, dull and metal. (B) The shading property controls the color shading for the surface, including choices of flat, faceted and interp. (C) The lighting property changes the lighting algorithm from flat, gouraud and phong. (D) The light direction determines where the light comes from, i.e., headlight, right or left.

- doi:10.1371/journal.pone.0068910.g006

The top 15% connections in strength were displayed as edges in the network. The radius of an edge represented the weight of the connection between the two linked nodes. Through visual inspection, the connections within each module were denser than the connections between two modules. The long-distance connections (.90 mm) were colored in orange. Intriguingly, the longdistance connections were primarily linked the homologous regions in two hemispheres and the anterior and posterior portions of the default-mode network within each hemisphere.

Figure 9B illustrates the FCS map of the voxel-based functional network using volume-to-surface mapping. Hub regions, exhibit-

ing high FCS values, were predominantly observed in the defaultmode network, including the medial prefrontal cortex/ventral anterior cingulate cortex, dorsal prefrontal cortex, precuneus/ posterior cingulate cortex and inferior parietal lobule. Other regions included the visual cortex and the insula. These results were obviously different from those in the region-based network, suggesting that the hub distribution of the brain functional networks was dependent on the spatial scales.

[Figure 7]

- Figure 7. Interactions between two brains. BrainNet Viewer illustrates the interactions between two brains, as demonstrated here. The nodes used in this figure were extracted from the AAL90 template, while the connection between each pair of two nodes was randomly generated.

- doi:10.1371/journal.pone.0068910.g007

Discussion

We developed BrainNet Viewer as a free software for visualizing macro-scale brain networks (or connectomics), which achieved the following major functions: 1) display brain networks in multiviews; 2) display combinations of brain surface, nodes and edges; 3) adjust properties of network elements (i.e., nodes and edges); 4) map the volume image to brain surface; 5) support various types of image format exporting and video making; and 6) provide interactive operations, such as zoom and rotate. In addition, we constructed functional brain networks from a public dataset and further analyzed and visualized the topological properties of the resultant brain networks.

BrainNet Viewer visualizes the topological properties of brain networks constructed through region-based or voxel-based methods, as illustrated in Figure 9. For the region-based network, this toolbox displays the nodes and edges in their positions corresponding to the brain regions and adjusts their color and size according to required properties. Notably, we selected the AAL atlas to build a region-based network and visualize its topological architecture using this software. Given that the AAL atlas is one of the most widely used templates in human brain connectome studies, the use of this atlas is representative for connectome visualization. Notably, other atlases are generated from anatomical [66,69] or functional [26,67,68] parcellations. These different parcellations reflect the different organizational information in the brain, and BrainNet Viewer provides different parcellation choices for network node definition. For the voxel-based network, we used volume-to-surface mapping to demonstrate nodal properties. The

visualization results distinguish the topological differences over the entire brain surface. Moreover, several recent R-fMRI studies have explored the temporal dynamics of the functional brain connectome [71–74]. In these studies, brain networks are often constructed at individual or a period of time points, requiring a series of network figures. With BrainNet Viewer, researchers easily generate batched figures or network videos by writing loop codes. Compared with traditional visualization methods, which illustrate the network as a mosaic-like matrix or a dot-and-line plot in a plane, BrainNet Viewer generates a three-dimensional display of the networks, intuitively provides much more anatomical information for the brain and exhibits diversity using both graph-based network demonstration and volume-to-surface mapping [75]. These advantages make BrainNet Viewer a promising visualization platform for brain connectome studies and might inspire new ideas for understanding the construction principles of brain networks.

With the advent of brain connectome studies, a number of toolboxes were developed to construct and analyze macro-scale brain networks, including PANDA, BCT, GAT, GRETNA, Brainwaver and eConnectome. These toolboxes provide measurements of brain connectome features but lack the visualization options necessary to demonstrate biological findings. NetworkX and Pajek (http://vlado.fmf.uni-lj.si/pub/networks/pajek/) are two popular network visualization toolboxes to demonstrate network topological properties using dots and lines. These programs are suitable for displaying networks constructed from different fields, including the genome, society, traffic and telecom, however, ignoring the specific anatomical information of the brain

[Figure 8]

- Figure 8. The data tip displayed using the ‘Data Cursor’ function. The ‘Data Cursor’ function on the toolbar in BrainNet Viewer is used to interactively obtain information about the vertex on the brain surface. When this function is enabled, clicking anywhere on the brain surface will generate a data tip with the coordinates and values for the selected vertex and the AAL brain region and Brodmann Area where the vertex belongs. The vertex selected in this figure shows an MNI coordinate of x=27.3, y=255.4 and z=25.8, with a statistic T value of 18.47. Furthermore, this vertex belongs to the left precuneus in the AAL template and the Brodmann region 23.

- doi:10.1371/journal.pone.0068910.g008

science. Caret (http://brainvis.wustl.edu/wiki/index.php/Caret: About) is a widely used toolbox for the visualization and analysis of the brain cortex, providing an abundant operation at the brain surface level, but lacking the demonstration for the topology of graph-based networks. Compared with these connectome toolboxes, BrainNet Viewer has an advantage of visualizing the topology of the macro-scale brain networks with detailed, predefined brain anatomical or functional information. Another brain connectome visualization toolkit, Connectome Viewer [76], offers comparable visualization functions, through a python-based, not Matlab-based, toolbox. Considering that most of the graph-based brain network analysis toolboxes were developed in a Matlab environment, our toolbox exhibits better compatibility and usability, such as software for the interfaced and batched generation of images. Notably, there are also simulation and visualization toolboxes for modeling neuronal networks at a micro-scale, including neuroConstruct (www.neuroconstruct.org/) [77], PyNN (neuralensemble.org/ PyNN/) [78] and CPT (Connectivity Pattern Tables) [79]. Because these toolboxes focus on the mechanism of neuronal activities underlying macro-scale brain networks, we can hardly compare these software programs with BrainNet Viewer. The toolboxes

described above facilitate brain network studies from different aspects, and their main features are summarized in Table 1.

Since the BrainNet Viewer was released on the NITRC and SPM websites, many researchers have adopted this toolbox to visualize the characteristics and divergences of brain networks for connectome-based methodological studies [80,81] and under healthy and diseased conditions, such as age [34], gender [34,36], intelligence [34], AD [53,82,83], MCI [51,53,84,85], depression [84,86–88], epilepsy [58,89,90] and addiction [91]. In addition, some of these figures were selected as cover images for several high-level neuroscience journals [51,84,87,92,93]. Moreover, several network analysis toolboxes provide interfaces with network visualization software. For example, BCT generates files for Pajek and Connectome Viewer. Notably, several brain connectome toolboxes, such as GAT [61], GRETNA and RESting-state fMRI data analysis Toolkit (REST, www.restfmri. net), provide user-friendly interfaces to directly call the functions of the BrainNet Viewer. The connections between BrainNet Viewer and these network analysis toolboxes help researchers easily visualize and assess their results.

Although BrainNet Viewer addresses the challenges in the visualization of the brain connectome, a few methodological

[Figure 9]

- Figure 9. Visualization of functional brain networks. (A) The region-based network is shown as a ball-and-stick model. The nodes are brain regions in the AAL atlas and their coordinates, sizes and colors represent the centroids, nodal strengths and modules of the regions, respectively. The edges represent the connections between different brain regions (top 15% are displayed). The functional connectivity strengths are presented as the radius of the edges, and long-distance connections (.90 mm) are colored in orange. (B) The voxel-based network is shown using volume-to-surface mapping. The values of the vertices on the surface indicate the normalized functional connectivity strength of the voxels in the volume data. Several hub regions with high connectivity strength are rendered in warm colors.

- doi:10.1371/journal.pone.0068910.g009

considerations and directions require future study. As with other toolboxes developed in the MATLAB environment, BrainNet Viewer has advantages in development and maintainability. However, the common problems of high memory consumption and slow loop execution for MATLAB programs exist in BrainNet Viewer, similar to other MATLAB packages. Notably, BrainNet Viewer fluently manages networks constructed using hundreds of nodes and lower sparsity of edges. When the number of nodes increases to the level of thousands, the rendering speed becomes slow, and the memory consumption increases quickly. The ‘out of

memory’ error sometimes occurs on 32-bit operating systems when dealing with a large network (e.g., 50,000). There might be two ways to solve this problem. On one hand, the codes of the toolbox could be further optimized to minimize the memory consumption. However, such an optimization is still limited under the MATLAB framework. On the other hand, translating the source code to a more efficient programming language, such as Python or C, might be a more efficient solution. With the rapidly increasing numbers of brain connectome studies, requirements for different manners of visualization are also mushrooming. For

Table 1. Summary of neuroscience networks tools.

Specific file format Website

Name Category Feature Environment

Matlab-based; Windows & Linux

.nv;.node;.edge www.nitrc.org/projects/bnv/

BrainNet Viewer Network visualization

3D graph-based brain network demonstration with nodes and edges; 3D brain surface view

Python-based; Linux only

.cff http://cmtk.org/viewer/

Connectome Viewer Network visualization

3D graph-based brain network demonstration with nodes and edges; 3D brain surface view

C++-based; Windows & Linux

Caret Network visualization

3D surface view and nodes

.spec http://brainvis.wustl.edu/wiki/index.php/Caret:About

NetworkX Network calculation & visualization

Graph-based network analysis; 2D demonstration with dots and lines

Python-based; Windows & Linux

.net http://networkx.github.io/

Pajek Network visualization

Graph-based network analysis; 2D demonstration with dots and lines

Delphi-based; Windows only

.pjk http://vlado.fmf.uni-lj.si/pub/networks/pajek/

PANDA Network construction

Network construction from dMRI data

Matlab-based; Linux only

NA www.nitrc.org/projects/panda/

GRETNA Network construction & calculation

Network construction from Resting-state fMRI data; graph-based network analysis

Matlab-based; Windows & Linux

NA www.nitrc.org/projects/gretna/

BCT Network calculation

Graph-based network analysis

Matlab-based; Windows & Linux

NA https://sites.google.com/site/bctnet/

GAT Network construction & calculation

Network construction from MRI data; graph-based network analysis

Matlab-based; Windows & Linux

NA http://nnl.stanford.edu/tools.html

R-based; Windows & Linux

NA http://cran.r-project.org/web/packages/brainwaver/

Brainwaver Network construction & calculation

Network construction from Restingstate fMRI data (wavelet); graph-based network analysis

eConnectome Connectivity calculation

EEG data preprocessing; connectivity analyze

Matlab-based; Windows & Linux

NA http://econnectome.umn.edu/

neuroConstruct Neuronal network modeling & visualization

Neuronal network analyze; 3D demonstration with neuronal morphology

Java-based; Windows & Linux

NA www.neuroconstruct.org/

PyNN Neuronal network modeling

Neuronal network simulation

Python-based; Linux only

NA neuralensemble.org/PyNN/

CPT Neuronal network visualization

2D demonstration of neuronal network in matrix view

Algorithm only NA NA

Abbreviations: PANDA, Pipeline for Analyzing braiN Diffusion imAges; BCT, Brain Connectivity Toolbox; GAT, Graph-Analysis Toolbox; GRETNA, Graph-theoRETical Network Analysis toolkit; Caret, Computerized Anatomical Reconstruction and Editing Toolkit; CPT, Connectivity Pattern Tables; NA, not available. doi:10.1371/journal.pone.0068910.t001

instance, in BrainNet Viewer, the brain connectome is treated as a brain surface using a ball-and-stick model; however, in reality, the brain regions and interregional connections are typically irregular objects and long thin fibers, instead of simple balls and sticks. Showing the brain connectome in both realistic and abstract ways might enhance our understanding of its underlying principles. Furthermore, we will improve the current version by including more functions, such as automatic placement of the nodal labels without overlapping, statistical analysis, slice image display and improvements to the user experience.

Acknowledgments

We thank Professor Alan Evans for providing us the ICBM152 brain surface. We thank people who provided valuable suggestions during the

References

- 1. Sporns O, Tononi G, Kotter R (2005) The human connectome: A structural description of the human brain. PLoS Comput Biol 1: e42.
- 2. Biswal BB, Mennes M, Zuo XN, Gohel S, Kelly C, et al. (2010) Toward discovery science of human brain function. Proc Natl Acad Sci U S A 107: 4734–4739.
- 3. Bullmore E, Sporns O (2009) Complex brain networks: graph theoretical analysis of structural and functional systems. Nat Rev Neurosci 10: 186–198.
- 4. Bullmore E, Sporns O (2012) The economy of brain network organization. Nat Rev Neurosci 13: 336–349.
- 5. He Y, Evans A (2010) Graph theoretical modeling of brain connectivity. Curr Opin Neurol 23: 341–350.
- 6. He Y, Chen ZJ, Evans AC (2007) Small-world anatomical networks in the human brain revealed by cortical thickness from MRI. Cereb Cortex 17: 2407– 2419.
- 7. Chen ZJ, He Y, Rosa-Neto P, Germann J, Evans AC (2008) Revealing modular architecture of human brain structural networks by using cortical thickness from MRI. Cereb Cortex 18: 2374–2381.
- 8. Hagmann P, Cammoun L, Gigandet X, Meuli R, Honey CJ, et al. (2008) Mapping the structural core of human cerebral cortex. PLoS Biol 6: e159.
- 9. Gong G, He Y, Concha L, Lebel C, Gross DW, et al. (2009) Mapping anatomical connectivity patterns of human cerebral cortex using in vivo diffusion tensor imaging tractography. Cereb Cortex 19: 524–536.
- 10. He Y, Wang J, Wang L, Chen ZJ, Yan C, et al. (2009) Uncovering intrinsic modular organization of spontaneous brain activity in humans. PLoS One 4: e5226.
- 11. Salvador R, Suckling J, Coleman MR, Pickard JD, Menon D, et al. (2005) Neurophysiological architecture of functional magnetic resonance images of human brain. Cereb Cortex 15: 1332–1342.
- 12. Achard S, Salvador R, Whitcher B, Suckling J, Bullmore E (2006) A resilient, low-frequency, small-world human brain functional network with highly connected association cortical hubs. J Neurosci 26: 63–72.
- 13. Watts DJ, Strogatz SH (1998) Collective dynamics of ‘small-world’ networks. Nature 393: 440–442.
- 14. Newman ME (2006) Modularity and community structure in networks. Proc Natl Acad Sci U S A 103: 8577–8582.
- 15. Meunier D, Lambiotte R, Bullmore ET (2010) Modular and hierarchically modular organization of brain networks. Front Neurosci 4: 200.
- 16. Buckner RL, Sepulcre J, Talukdar T, Krienen FM, Liu H, et al. (2009) Cortical hubs revealed by intrinsic functional connectivity: mapping, assessment of stability, and relation to Alzheimer’s disease. J Neurosci 29: 1860–1873.
- 17. van den Heuvel MP, Sporns O (2011) Rich-club organization of the human connectome. J Neurosci 31: 15775–15786.
- 18. van den Heuvel MP, Kahn RS, Goni J, Sporns O (2012) High-cost, highcapacity backbone for global brain communication. Proc Natl Acad Sci U S A 109: 11372–11377.
- 19. Gong G, Rosa-Neto P, Carbonell F, Chen ZJ, He Y, et al. (2009) Age- and gender-related differences in the cortical anatomical network. J Neurosci 29: 15684–15693.
- 20. Meunier D, Achard S, Morcom A, Bullmore E (2009) Age-related changes in modular organization of human brain functional networks. Neuroimage 44: 715–723.
- 21. Tomasi D, Volkow ND (2012) Aging and functional brain networks. Mol Psychiatry 17: 471, 549–458.
- 22. Wang L, Li Y, Metzak P, He Y, Woodward TS (2010) Age-related changes in topological patterns of large-scale brain functional networks during memory encoding and recognition. Neuroimage 50: 862–872.
- 23. Wen W, Zhu W, He Y, Kochan NA, Reppermund S, et al. (2011) Discrete neuroanatomical networks are associated with specific cognitive abilities in old age. J Neurosci 31: 1204–1212.
- 24. Wu K, Taki Y, Sato K, Kinomura S, Goto R, et al. (2012) Age-related changes in topological organization of structural brain networks in healthy individuals. Hum Brain Mapp 33: 552–568.

software development in our laboratory, including Gaolang Gong, Ni Shu, Chaogan Yan, Xia Liang, Teng Xie, Qixiang Lin and Zhengjia Dai. We thank Patrick Clark for helping revise our manual. We also thank the developers of the following softwares and toolboxes whose source codes or file formats were referenced during the development process of BrainNet Viewer: Matlab (www.mathworks.com/products/matlab/), SurfStat (www. math.mcgill.ca/keith/surfstat/), FreeSurfer (http://surfer.nmr.mgh. harvard.edu/), BrainVISA (http://brainvisa.info/) and SPM (www.fil. ion.ucl.ac.uk/spm/).

Author Contributions

Conceived and designed the experiments: MX JW YH. Performed the experiments: MX. Analyzed the data: MX. Contributed reagents/ materials/analysis tools: MX JW YH. Wrote the paper: MX JW YH.

- 25. Fair DA, Dosenbach NU, Church JA, Cohen AL, Brahmbhatt S, et al. (2007) Development of distinct control networks through segregation and integration. Proc Natl Acad Sci U S A 104: 13507–13512.
- 26. Fair DA, Cohen AL, Power JD, Dosenbach NU, Church JA, et al. (2009) Functional brain networks develop from a ‘‘local to distributed’’ organization. PLoS Comput Biol 5: e1000381.
- 27. Fair DA, Cohen AL, Dosenbach NU, Church JA, Miezin FM, et al. (2008) The maturing architecture of the brain’s default network. Proc Natl Acad Sci U S A 105: 4028–4032.
- 28. Fair DA, Bathula D, Nikolas MA, Nigg JT (2012) Distinct neuropsychological subgroups in typically developing youth inform heterogeneity in children with ADHD. Proc Natl Acad Sci U S A 109: 6769–6774.
- 29. Batalle D, Eixarch E, Figueras F, Munoz-Moreno E, Bargallo N, et al. (2012) Altered small-world topology of structural brain networks in infants with intrauterine growth restriction and its association with later neurodevelopmental outcome. Neuroimage 60: 1352–1366.
- 30. Hwang K, Hallquist MN, Luna B (2012) The Development of Hub Architecture in the Human Functional Brain Network. Cereb Cortex.
- 31. Khundrakpam BS, Reid A, Brauer J, Carbonell F, Lewis J, et al. (2012) Developmental Changes in Organization of Structural Brain Networks. Cereb Cortex.
- 32. Supekar K, Musen M, Menon V (2009) Development of large-scale functional brain networks in children. PLoS Biol 7: e1000157.
- 33. Yap PT, Fan Y, Chen Y, Gilmore JH, Lin W, et al. (2011) Development trends of white matter connectivity in the first years of life. PLoS One 6: e24678.
- 34. Wu K, Taki Y, Sato K, Hashizume H, Sassa Y, et al. (2013) Topological organization of functional brain networks in healthy children: differences in relation to age, sex, and intelligence. PLoS One 8: e55347.
- 35. Tian L, Wang J, Yan C, He Y (2011) Hemisphere- and gender-related differences in small-world brain networks: a resting-state functional MRI study. Neuroimage 54: 191–202.
- 36. Liu J, Qin W, Nan J, Li J, Yuan K, et al. (2011) Gender-related differences in the dysfunctional resting networks of migraine suffers. PLoS One 6: e27049.
- 37. Yan C, Gong G, Wang J, Wang D, Liu D, et al. (2011) Sex- and brain sizerelated small-world structural cortical networks in young adults: a DTI tractography study. Cereb Cortex 21: 449–458.
- 38. Li Y, Liu Y, Li J, Qin W, Li K, et al. (2009) Brain anatomical network and intelligence. PLoS Comput Biol 5: e1000395.
- 39. van den Heuvel MP, Stam CJ, Kahn RS, Hulshoff Pol HE (2009) Efficiency of functional brain networks and intellectual performance. J Neurosci 29: 7619– 7624.
- 40. Schmitt JE, Lenroot RK, Wallace GL, Ordaz S, Taylor KN, et al. (2008) Identification of genetically mediated cortical networks: a multivariate study of pediatric twins and siblings. Cereb Cortex 18: 1737–1747.
- 41. van den Heuvel MP, van Soelen IL, Stam CJ, Kahn RS, Boomsma DI, et al.

(2013) Genetic control of functional brain network efficiency in children. Eur Neuropsychopharmacol 23: 19–23.

- 42. Brown JA, Terashima KH, Burggren AC, Ercoli LM, Miller KJ, et al. (2011) Brain network local interconnectivity loss in aging APOE-4 allele carriers. Proc Natl Acad Sci U S A 108: 20760–20765.
- 43. Fornito A, Zalesky A, Bassett DS, Meunier D, Ellison-Wright I, et al. (2011) Genetic influences on cost-efficient organization of human cortical functional networks. J Neurosci 31: 3261–3270.
- 44. Bassett DS, Bullmore ET (2009) Human brain networks in health and disease. Curr Opin Neurol 22: 340–347.
- 45. Guye M, Bettus G, Bartolomei F, Cozzone PJ (2010) Graph theoretical analysis of structural and functional connectivity MRI in normal and pathological brain networks. MAGMA 23: 409–421.
- 46. Xia M, He Y (2011) Magnetic resonance imaging and graph theoretical analysis of complex brain networks in neuropsychiatric disorders. Brain Connect 1: 349– 365.

- 47. Wen W, He Y, Sachdev P (2011) Structural brain networks and neuropsychiatric disorders. Curr Opin Psychiatry 24: 219–225.
- 48. Stam CJ, Jones BF, Nolte G, Breakspear M, Scheltens P (2007) Small-world networks and functional connectivity in Alzheimer’s disease. Cereb Cortex 17: 92–99.
- 49. He Y, Chen Z, Evans A (2008) Structural insights into aberrant topological patterns of large-scale cortical networks in Alzheimer’s disease. J Neurosci 28: 4756–4766.
- 50. Lo CY, Wang PN, Chou KH, Wang J, He Y, et al. (2010) Diffusion tensor tractography reveals abnormal topological organization in structural cortical networks in Alzheimer’s disease. J Neurosci 30: 16876–16885.
- 51. Wang J, Zuo X, Dai Z, Xia M, Zhao Z, et al. (2013) Disrupted functional brain connectome in individuals at risk for Alzheimer’s disease. Biol Psychiatry 73: 472–481.
- 52. Yao Z, Zhang Y, Lin L, Zhou Y, Xu C, et al. (2010) Abnormal cortical networks in mild cognitive impairment and Alzheimer’s disease. PLoS Comput Biol 6: e1001006.
- 53. Seo EH, Lee DY, Lee JM, Park JS, Sohn BK, et al. (2013) Whole-brain functional networks in cognitively normal, mild cognitive impairment, and Alzheimer’s disease. PLoS One 8: e53922.
- 54. Bassett DS, Bullmore E, Verchinski BA, Mattay VS, Weinberger DR, et al.

(2008) Hierarchical organization of human cortical networks in health and schizophrenia. J Neurosci 28: 9239–9248.

- 55. Liu Y, Liang M, Zhou Y, He Y, Hao Y, et al. (2008) Disrupted small-world networks in schizophrenia. Brain 131: 945–961.
- 56. Zalesky A, Fornito A, Seal ML, Cocchi L, Westin CF, et al. (2011) Disrupted axonal fiber connectivity in schizophrenia. Biol Psychiatry 69: 80–89.
- 57. Liao W, Zhang Z, Pan Z, Mantini D, Ding J, et al. (2010) Altered functional connectivity and small-world in mesial temporal lobe epilepsy. PLoS One 5: e8525.
- 58. Zhang Z, Liao W, Chen H, Mantini D, Ding JR, et al. (2011) Altered functionalstructural coupling of large-scale brain networks in idiopathic generalized epilepsy. Brain 134: 2912–2928.
- 59. Rubinov M, Sporns O (2010) Complex network measures of brain connectivity: uses and interpretations. Neuroimage 52: 1059–1069.
- 60. He B, Dai Y, Astolfi L, Babiloni F, Yuan H, et al. (2011) eConnectome: A MATLAB toolbox for mapping and imaging of brain functional connectivity. J Neurosci Methods 195: 261–269.
- 61. Hosseini SM, Hoeft F, Kesler SR (2012) GAT: a graph-theoretical analysis toolbox for analyzing between-group differences in large-scale structural and functional brain networks. PLoS One 7: e40709.
- 62. Cui Z, Zhong S, Xu P, He Y, Gong G (2013) PANDA: a pipeline toolbox for analyzing brain diffusion images. Front Hum Neurosci 7: 42.
- 63. Dale AM, Fischl B, Sereno MI (1999) Cortical surface-based analysis. I. Segmentation and surface reconstruction. Neuroimage 9: 179–194.
- 64. Mangin JF, Riviere D, Cachia A, Duchesnay E, Cointepas Y, et al. (2004) A framework to study the cortical folding patterns. Neuroimage 23 Suppl 1: S129– 138.
- 65. Tzourio-Mazoyer N, Landeau B, Papathanassiou D, Crivello F, Etard O, et al.

(2002) Automated anatomical labeling of activations in SPM using a macroscopic anatomical parcellation of the MNI MRI single-subject brain. Neuroimage 15: 273–289.

- 66. Brodmann K (1909) Vergleichende lokalisationslehre der grobhirnrinde. Barth: Leipzig.
- 67. Smith SM, Jenkinson M, Woolrich MW, Beckmann CF, Behrens TE, et al.

(2004) Advances in functional and structural MR image analysis and implementation as FSL. Neuroimage 23 Suppl 1: S208–219.

- 68. Dosenbach NU, Nardos B, Cohen AL, Fair DA, Power JD, et al. (2010) Prediction of individual brain maturity using fMRI. Science 329: 1358–1361.
- 69. Shattuck DW, Mirza M, Adisetiyo V, Hojatkashani C, Salamon G, et al. (2008) Construction of a 3D probabilistic atlas of human cortical structures. Neuroimage 39: 1064–1080.
- 70. Yan C, Zang Y (2010) DPARSF: A MATLAB Toolbox for ‘‘Pipeline’’ Data Analysis of Resting-State fMRI. Front Syst Neurosci 4: 13.

- 71. Chang C, Glover GH (2010) Time-frequency dynamics of resting-state brain connectivity measured with fMRI. Neuroimage 50: 81–98.
- 72. Kang J, Wang L, Yan C, Wang J, Liang X, et al. (2011) Characterizing dynamic functional connectivity in the resting brain using variable parameter regression and Kalman filtering approaches. Neuroimage 56: 1222–1234.
- 73. Allen EA, Damaraju E, Plis SM, Erhardt EB, Eichele T, et al. (2012) Tracking Whole-Brain Connectivity Dynamics in the Resting State. Cereb Cortex.
- 74. Jones DT, Vemuri P, Murphy MC, Gunter JL, Senjem ML, et al. (2012) NonStationarity in the ‘‘Resting Brain’s’’ Modular Architecture. PLoS One 7: e39731.
- 75. Margulies DS, Bo¨ttger J, Watanabe A, Gorgolewski KJ (2013) Visualizing the Human Connectome. NeuroImage.
- 76. Gerhard S, Daducci A, Lemkaddem A, Meuli R, Thiran JP, et al. (2011) The connectome viewer toolkit: an open source framework to manage, analyze, and visualize connectomes. Front Neuroinform 5: 3.
- 77. Gleeson P, Steuber V, Silver RA (2007) neuroConstruct: a tool for modeling networks of neurons in 3D space. Neuron 54: 219–235.
- 78. Davison AP, Bruderle D, Eppler J, Kremkow J, Muller E, et al. (2008) PyNN: A Common Interface for Neuronal Network Simulators. Front Neuroinform 2: 11.
- 79. Nordlie E, Plesser HE (2010) Visualizing neuronal network connectivity with connectivity pattern tables. Front Neuroinform 3: 39.
- 80. Liang X, Wang J, Yan C, Shu N, Xu K, et al. (2012) Effects of different correlation metrics and preprocessing factors on small-world brain functional networks: a resting-state functional MRI study. PLoS One 7: e32766.
- 81. Liang X, Zou Q, He Y, Yang Y (2013) Coupling of functional connectivity and regional cerebral blood flow reveals a physiological basis for network hubs of the human brain. Proc Natl Acad Sci U S A 110: 1929–1934.
- 82. Liu M, Zhang D, Shen D, the Alzheimer’s Disease Neuroimaging I (2013) Hierarchical fusion of features and classifier decisions for Alzheimer’s disease diagnosis. Hum Brain Mapp.
- 83. Dai Z, Yan C, Wang Z, Wang J, Xia M, et al. (2012) Discriminative analysis of early Alzheimer’s disease using multi-modal imaging and multi-level characterization with multi-classifier (M3). Neuroimage 59: 2187–2195.
- 84. Bai F, Shu N, Yuan Y, Shi Y, Yu H, et al. (2012) Topologically convergent and divergent structural connectivity patterns between patients with remitted geriatric depression and amnestic mild cognitive impairment. J Neurosci 32: 4307–4318.
- 85. Yi L, Wang J, Jia L, Zhao Z, Lu J, et al. (2012) Structural and functional changes in subcortical vascular mild cognitive impairment: a combined voxel-based morphometry and resting-state fMRI study. PLoS One 7: e44758.
- 86. Fang P, Zeng LL, Shen H, Wang L, Li B, et al. (2012) Increased cortical-limbic anatomical network connectivity in major depression revealed by diffusion tensor imaging. PLoS One 7: e45972.
- 87. Zhang J, Wang J, Wu Q, Kuang W, Huang X, et al. (2011) Disrupted brain connectivity networks in drug-naive, first-episode major depressive disorder. Biol Psychiatry 70: 334–342.
- 88. Wang L, Dai Z, Peng H, Tan L, Ding Y, et al. (2013) Overlapping and segregated resting-state functional connectivity in patients with major depressive disorder with and without childhood neglect. Hum Brain Mapp.
- 89. Taylor PN, Goodfellow M, Wang Y, Baier G (2013) Towards a large-scale model of patient-specific epileptic spike-wave discharges. Biol Cybern 107: 83– 94.
- 90. Sequeira KM, Tabesh A, Sainju RK, DeSantis SM, Naselaris T, et al. (2013) Perfusion network shift during seizures in medial temporal lobe epilepsy. PLoS One 8: e53204.
- 91. Hong SB, Zalesky A, Cocchi L, Fornito A, Choi EJ, et al. (2013) Decreased functional brain connectivity in adolescents with internet addiction. PLoS One 8: e57831.
- 92. Shu N, Liu Y, Li K, Duan Y, Wang J, et al. (2011) Diffusion tensor tractography reveals disrupted topological efficiency in white matter structural networks in multiple sclerosis. Cereb Cortex 21: 2565–2577.
- 93. Wang Z, Yan C, Zhao C, Qi Z, Zhou W, et al. (2011) Spatial patterns of intrinsic brain activity in mild cognitive impairment and Alzheimer’s disease: a resting-state functional MRI study. Hum Brain Mapp 32: 1720–1740.

