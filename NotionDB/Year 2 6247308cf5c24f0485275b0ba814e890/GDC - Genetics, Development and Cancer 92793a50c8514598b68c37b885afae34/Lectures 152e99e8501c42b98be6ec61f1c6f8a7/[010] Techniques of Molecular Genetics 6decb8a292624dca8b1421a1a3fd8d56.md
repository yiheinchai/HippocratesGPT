# [010] Techniques of Molecular Genetics

# Molecular Genetics

- Molecular Genetics is the study and manipulation of the genome and its expression

---

# Polymerase Chain Reaction

- Most used technique used to analyse genetic information
- PCR is used to amplify specific regions of DNA so that the amplified DNA region (Amplicon) can be visualised on an agarose gel
- A Negative control is needed for the PCR reaction (PCR Without DNA) to ensure that PCR Mixture is correct/functional
- For PCR, you need:
1. Thermal Cycle
2. DNA Sample containing region of Interest
3. dNTPs
4. Tau Polymerase
5. Sense and Antisense Primers to which are complementary to and hence, demarcate the 5’ and 3’ region of the DNA Sequence of Interest so only the relevant section of DNA is amplified
- A Positive Control is also needed for the PCR (PCR with known specific DNA Region of Interest) so that the band produced by the Amplicon can be compared to the Positive Control to identify the Amplicon
- Denaturation: DNA is heated so that double stranded structure
separates into 2 separate strands (95°C).
- Annealing: primers hybridise to 5’ end of both DNA strands (55-60°C).
- If temperature is too high, primers will not bind. If too low, will bind non-specifically.
- Extension: DNA polymerase synthesises new complementary strand in 5’ → 3’ direction from the Primer by adding dNTPs (72°C) to create copies of both DNA strands from the start of the DNA Region of Interest to the 5’ end of the entire DNA Sample.
- Cycle is repeated about 35-40 times. As DNA is amplified, more template becomes available, leading to exponential ↑ in copies.
- Reaction can be held at 4°C for an extended period of time, until the amplicon is required
- Thermal Cycle is programmed to rapidly alternate between the temperatures needed for Denaturation, Annealing and Extension to allow for rapid proliferation of the DNA region of interest
- This allows DNA to be amplified from 100 bp to 100kb very rapidly

![Screenshot 2022-02-28 at 14.29.29.png](%5B010%5D%20Techniques%20of%20Molecular%20Genetics%206decb8a292624dca8b1421a1a3fd8d56/Screenshot_2022-02-28_at_14.29.29.png)

### Examples of PCR Application

- Forensic genetic tests.
- Paternity testing
- Diagnosis of genetic disease.
- Tumour typing
- Tissue typing for transplants.
- Microbe identification
- Following disease spread.
- Ancestry studies

---

# Derived Techniques from PCR

### Reverse Transcription

- This is used to amplify RNA Sequences (E.g from RNA Viruses)
- Instead of using sequence specific Primers, an Oligo(dT) Primer is used which is complementary to the 3’ Poly A RNA Tail (8 As long)
- Reverse Transcriptase is then used to convert the RNA into cDNA, starting from the Oligo(dT) Primer to synthesise a cDNA-RNA Hybrid Helix using dNTPs within a Buffer Solution
- cDNA is then replicated as normal using Primers, and Taq Polymerase to amplify the cDNA Target Region to generate an Amplicon of sufficient size
- These two processes of Reverse Transcriptase and cDNA PCR can occur simultaneously in the same solution despite Taq Polymerase and Reverse Transcriptase having different functional temperature ranges by rapidly alternating the temperature of the solution between the two optimal temperature ranges
- Alternatively, Reverse Transcription and cDNA PCR can occur separately in two different solutions that are maintained at the optimal temperature for each reaction process, with the products of Reverse Transcription then being used in the cDNA PCR

![Screenshot 2022-02-26 at 11.36.42.png](%5B010%5D%20Techniques%20of%20Molecular%20Genetics%206decb8a292624dca8b1421a1a3fd8d56/Screenshot_2022-02-26_at_11.36.42.png)

![Screenshot 2022-02-26 at 11.36.54.png](%5B010%5D%20Techniques%20of%20Molecular%20Genetics%206decb8a292624dca8b1421a1a3fd8d56/Screenshot_2022-02-26_at_11.36.54.png)

### Real-Time Quantitative PCR

- SYBR is a fluorescent compound that only binds to dsDNA and once it is bound, it emits fluorescent light
- Therefore, if there is little to no amplification, there will be very little SYBR Green signalling (indicated by fluorescence levels)
- SYBR Green is commonly used when PCR is occurring for identifying/amplifying multiple different amplicons/target DNA Sequences that require different primers as SYBR is not specific for a given primer (it just measures the rate of PCR Amplification)
- TaqMan Assays is where Primers are added to the solution  which bind to the 3’ end of the Amplicon alongside a TaqMan probe (Fluorescence Labelled) that binds to the 5’ region of the Amplicon (at the 3’ end of the Probe)
- When DNA Polymerase extends the amplicon from the 3’ end and reaches the TaqMan Probe, it cleaves the Probe from the 5’ Region of the Amplicon, causing it to emit fluorescence
- Therefore, the use of the TaqMan probe means that unlike SYBR Green, TaqMan is specific to a single Amplicon and hence, only used when one amplicon is to be analysed
- For both of these methods, a graph of Fluorescence Emitted against Cycle Number, with a Threshold Fluorescence being established that is the Fluorescence seen when the PCR Reaction is part way through its maximum rate of reaction, when this rate is exponential
- Using the Threshold Value, the Fluorescence Signal can be converted into a number of Amplicon Copies to determine the amount of DNA of Interest present in the Initial Sample

![Screenshot 2022-02-26 at 11.37.17.png](%5B010%5D%20Techniques%20of%20Molecular%20Genetics%206decb8a292624dca8b1421a1a3fd8d56/Screenshot_2022-02-26_at_11.37.17.png)

---

# Genetic Variants

- Genetic Variant = variation between two genomes
- SNP: Single Nucleotide Polymorphism (Substitution) which does not impact the synthesis or the function of the protein enough to create a disease
- Mutation: usually a rare event with a frequency of < 1/100. It changes the genetic code to such an extent that it impacts the protein synthesis or function but often, not enough to create a disease

![Screenshot 2022-02-26 at 11.36.15.png](%5B010%5D%20Techniques%20of%20Molecular%20Genetics%206decb8a292624dca8b1421a1a3fd8d56/Screenshot_2022-02-26_at_11.36.15.png)

---

# Human Genetic Investigations

- Genome Wide Association Studies (GWAS) - Identify common variants with Modest impact (Analyses SNPs)
- GWAS analyse the genotype of an entire population in an attempt to attribute a common genetic mutation to a specific disease phenotype
- Next Generation Sequencing (WES/WGS) - Identify Rare variants
with High impact and hence, can cause disease (Analyses Mutations)

### Analysing Genomic DNA

- Following DNA Amplification via PCR, Sanger Method can used Chain Termination by using Fluorescently labelled ddNTPs (Do not have 3’ OH and hence, another nucleotide cannot be added to the ddNTP, leading to Chain Termination) to identify the location of all the nucleotide bases found within a DNA Sequence
- The ddNTPs will compete with a dNTP at a complementary bases randomly along the DNA Strand of Interest and cause chain termination here, emitting fluorescence of a specific colour to allow for the identification of the final base of the Terminated Chain based on the Fluorescence Colour
- After this, Gel Electrophoresis can be used to separate all the Chain Terminated Sequences based on Chain Length, causing the DNA to be ordered from smallest to largest size whilst their fluorescence colours are known, allowing the identity of each base in the DNA target sequence to be identified (Colour = Type of Base and Reading Short to Long Chain moves in the 3’ to 5’ direction down the DNA strand of Interest to allow the position of the Nucleotide in the DNA Sequence to be identified)
- In Second Generation Sequencing, Genomic DNA is sheared into small pieces and then Adaptors are ligated to the end of the DNA Fragments
- The adaptors allow for the Hybridisation of DNA Fragments onto a Solid Surface, where fragments are then amplified using Fluorescent Nucleotides to form DNA Clusters formed of identical copies of the Original Ligated DNA Fragment
- Each Nucleotide is fluorescently labelled with a different colour and as the Fluorescently Labelled nucleotides are incorporated into the cluster, highly sensitive cameras record the sequence of light to identify the identity of each nucleotide in the order that they are added (allows identification of the original Ligated DNA Fragment)
- These sequences are then assembled and then mapped to a known genome to identify the entirety of the DNA Sequence and its location within the Human Genome

![Screenshot 2022-02-26 at 11.39.14.png](%5B010%5D%20Techniques%20of%20Molecular%20Genetics%206decb8a292624dca8b1421a1a3fd8d56/Screenshot_2022-02-26_at_11.39.14.png)

---

# Sanger Vs Next Generation Sequencing

- Sanger is used to analyse a single gene of interest to identify a mutation from a DNA Sample (when the mutation identity and gene of interest is already known but its presence in the Px needs to be confirmed)
- NGS is used to analyse multiple genes of interest or when the DNA Sequence of Interest is not known (AKA Discovering new genetic variations)
- NGS can also be used to sequence the Exome or Whole Genome

![Screenshot 2022-02-26 at 11.41.48.png](%5B010%5D%20Techniques%20of%20Molecular%20Genetics%206decb8a292624dca8b1421a1a3fd8d56/Screenshot_2022-02-26_at_11.41.48.png)

- If there is a large number of samples but a small number of different gene targets need to be analysed, Sanger Method may be more cost efficient however, when there is a large number of samples but a large number of different gene targets need to be analysed, Targeted NGS is more cost efficient
- Therefore, Sanger Sequencing is generally more cost effective for analysing/sequencing a small number of gene targets whereas NGS is generally more cost effective for analysing/sequencing a large number of gene targets

![Screenshot 2022-02-26 at 11.42.34.png](%5B010%5D%20Techniques%20of%20Molecular%20Genetics%206decb8a292624dca8b1421a1a3fd8d56/Screenshot_2022-02-26_at_11.42.34.png)

## Sanger Vs NGS

### Sanger Sequencing

| Benefits | Challenges |
| --- | --- |
| Fast, cost-effective sequencing for a low number of targets (1-20 targets) | Low Sensitivity (Limit of detection is around 15-20%) |
| Familiar Workflow | Low discovery power |
|  | Not as cost-effective for high numbers of targets (>20 targets) |
|  | Low scalability due to increasing sample input requirements |

### Targeted NGS

| Benefits | Challenges |
| --- | --- |
| Higher sequencing depth enables higher sensitivity (down to 1%) | Less cost-effective for sequencing low numbers of targets (1-20 targets) |
| Higher discovery power as can sequences larger and more samples (mainly as it does not require the use of primers) | Time-consuming for sequencing low number of targets (1-20 targets) |
| Higher Mutation resolution, especially when attempting to identify an unknown mutation |  |
| More data produced with the same amount of input DNA vs Sanger Sequencing |  |
| Higher sample throughput so more efficient when numerous samples need to be analysed |  |
- Discovery Power = Ability of the sequencing method to identify novel/new variants
- Mutation Resolution = Size of the mutation identified (NGS can identify large chromosomal rearrangements down to single nucleotide variant)

---

# Sanger Sequencing

- Homozygous Mutations can be identified by a single different coloured fluorescence peak on the Spectrum produced by Sanger Sequencing when compared to that at the same position in the Wild Type Sanger Spectrum
- Heterozygous Mutations can be identified by 2 fluorescence peaks (one the same colour and one a different colour as that seen in the Sanger Spectrum of the Wild Type DNA) instead of 1 fluorescence peak at the same position on the Sanger Spectrums

![Screenshot 2022-02-26 at 11.48.32.png](%5B010%5D%20Techniques%20of%20Molecular%20Genetics%206decb8a292624dca8b1421a1a3fd8d56/Screenshot_2022-02-26_at_11.48.32.png)

---

# Application of Sanger Sequencing and Next Generation Sequencing

### Candidate Approach (When Mutation is Known) - Sanger Sequencing

- 1 in 15,000 approximately.
- Autosomal dominant mutation in FGFR3 gene.
- Same nucleotide is mutated in 98%.
- Gain of function mutation.
- 90% of mutations occur spontaneously and are not inherited.
- Disproportionate short statue, with rhizomelic shortening, frontal bossing, normal intelligence.

### Genome-Wide Approach (When Mutation is Not Known) - NGS

- Diagnostics– Exome and whole genome sequencing
- Gene expression analysis and other omics
- E.g NGS has been used to Identify gene for Miller syndrome
- Looked at only 4 individuals
- 2 sibs, 2 other unrelated
- Found additional diagnosis in sibs
- Changed how we do research and diagnostics

---

# GWAS Studies - Microarray

- This is used to identify whether an individual has a specific mutation or not in one of their cells
- A Normal/Reference/Control Cell and a Cell of Interest (that may contain the mutation) are isolated, cultured and then mRNA from the Cells is harvested
- This mRNA is reverse transcribed into cDNA (used to analyse the Transcriptome for cases like cancer) or Genomic DNA is directly harvested (to look at SNPs to assess Polygenic Diseases), which is then labelled with a fluorescent probe
- Specific oligosequences are adhered to the bottom each well of the Microarray which are specific to the Normal Genomic DNA/cDNA of interest from the Cell and the Mutated Genomic cDNA/DNA whose presence in the Cell of Interest is to be investigated
- The cDNA or Genomic DNA from the Reference and Cell of Interest is then added to each well and if the cDNA or DNA binds to the oligosequence, then the probe fluoresces a different colour depending on which cDNA Segments bind to the Oligosequence
- If the Px does not have the mutation, then cDNA/Genomic DNA from both cells will bind to the Oligosequence complementary to the normal DNA Sequence, indicating that the mutation is not present
- If the Px Cell does have the mutation, then the cDNA/Genomic DNA will bind to 2 different oligosequences (one complementary to the Mutated DNA Sequence and one to the Wild Type Sequence), producing a mixed fluorescence colour that indicates the presence of the mutation within the Px Cell
- The Amount of Fluorescence emitted can then be used to quantify the amount of DNA in the sample and hence, when repeated for a population, it can be used to assess the prevalence of the mutation in a population

![Screenshot 2022-02-26 at 11.53.00.png](%5B010%5D%20Techniques%20of%20Molecular%20Genetics%206decb8a292624dca8b1421a1a3fd8d56/Screenshot_2022-02-26_at_11.53.00.png)

- When analysing the Microarrays produced from a population of Px together, If Multiple Oligosequences are targeted against different DNA Sequences (to analyse the entire genome), the presence of a high magnitude fluorescence signal in one well for Cases that is not present in the Controls (Large Fluorescence Difference) indicates the presence of a common mutation/DNA Sequence in the Cases that is not present in the Controls which may be the cause of the Disease

![Screenshot 2022-02-26 at 11.53.27.png](%5B010%5D%20Techniques%20of%20Molecular%20Genetics%206decb8a292624dca8b1421a1a3fd8d56/Screenshot_2022-02-26_at_11.53.27.png)

### Clinical Applications of Microarrays

- First line for investigating children with dysmorphism and developmental delay
- Have replaced karyotyping in many situations
- Now routinely used in prenatal
- Currently can take a long time to get results especially if parental studies are needed as it requires the collection of cDNA from a large number of people - a problem in prenatals
- Ethical issues- what if there is an unexpected result, what if it is uncertain what the result means

### Microdeletion Syndrome - del22q11

- Velo-Cardio-Facial/ DiGeorge/ Sphrintzen Syndrome caused by microdeletion of 22q11
- Affects 1 in 2000 children approx
- Commonest chromosomal deletion
- It is very variable - even within families
- Autosomal dominant inheritance when inherited but 93% of mutations are spontaneous
- Critical region is around 3Mb in size and contains TBX1
- Cleft palate, congenital heart disease, learning difficulties
- The Specific Mutation which underlies DiGeorge’s Syndrome was identified using Microassays

![Screenshot 2022-02-26 at 11.57.48.png](%5B010%5D%20Techniques%20of%20Molecular%20Genetics%206decb8a292624dca8b1421a1a3fd8d56/Screenshot_2022-02-26_at_11.57.48.png)

---

# Arrays for SNP Genotyping

- Microarrays can be used to identify single nucleotide polymorphisms (SNPs), which commonly vary across the population
- UK population mapped by 500,000 SNPs.
- 17 distinct population groups identified.
- This allows for the identification of genetic background of the population included in studies to identify possible risk factors/confounders for disease.

---

# Molecular Cloning

- A method of introducing recombinant DNA and allowing its replication within an organism.
- Old Techniques requires a vector (plasmid or viral).
- Here, the human gene of interest combined with vector DNA and inserted into host (e.g. bacteria with antibacterial resistance due to insertion of Antibacterial Resistance Gene into the same Plasmid as the Gene of Interest)
- To ensure selective and maximal amplification of the Transgenic Bacteria, Specific Antibiotics are applied to the bacteria that are introduced to the Vector to kill Antibiotic Sensitive Bacteria that do not take up and hence, contain the Interest Gene Vector whilst those that have taken up the Gene Vector are antibiotic resistant and survive.
- These Transgenic bacteria (i.e. those expressing desired gene are selected) are then cultured, where they replicate whilst expressing the desired gene, causing the inserted gene of interest to be amplified as the Bacterial Population is amplified
- The Vector is then isolated from the Bacterial Population and the Gene of Interest is then liberated, where the numerous copies of the Gene can now be analysed or inserted into Animal Cells to observe their effects
- Alternatively, the Gene product from the Gene of Interest can be harvested from the Bacteria and then purified to produce large quantities of the protein of interest

![Screenshot 2022-02-26 at 12.01.35.png](%5B010%5D%20Techniques%20of%20Molecular%20Genetics%206decb8a292624dca8b1421a1a3fd8d56/Screenshot_2022-02-26_at_12.01.35.png)

### Applications of Molecular Cloning

- Production of humanised proteins
- Production of model organisms for research (E.g Population of Animal Cells with Gene of Interest inserted into their genome)
- Gene therapy

![Screenshot 2022-02-28 at 16.33.05.png](%5B010%5D%20Techniques%20of%20Molecular%20Genetics%206decb8a292624dca8b1421a1a3fd8d56/Screenshot_2022-02-28_at_16.33.05.png)

---

# Gene Therapy

1. Start with therapeutic transgene.
2. Put transgene in an avirulent viral vector (E.g Adenovirus which has a trophism for the tissue of interest).
3. Administer gene therapy to patient via administration of Viral Vector.
4. Viral vector reaches target cell and releases transgene (i.e. transduces cell) which is then incorporated into the DNA of the Host Cell.
5. Transgene is then expressed within the Host Cell Genome, causing the production of the Therapeutic Protein which can then be used to treat the disease

![Screenshot 2022-02-26 at 12.02.21.png](%5B010%5D%20Techniques%20of%20Molecular%20Genetics%206decb8a292624dca8b1421a1a3fd8d56/Screenshot_2022-02-26_at_12.02.21.png)

![Screenshot 2022-02-26 at 12.02.37.png](%5B010%5D%20Techniques%20of%20Molecular%20Genetics%206decb8a292624dca8b1421a1a3fd8d56/Screenshot_2022-02-26_at_12.02.37.png)

### Gene Editing - CRISPR/Cas9

- A Gene-Specific Guide RNA is used to target the gene of interest that is to be modified and binds to the Gene of Interest
- Cas9 is then added which recognises the Guide RNA and binds to the Gene of Interest to remove the Mutated Gene and insert Donor DNA (Gene of Interest) to directly edit the genome and hence, correct gene mutations to allow for normal Gene Products to be expressed

![Screenshot 2022-02-26 at 12.03.29.png](%5B010%5D%20Techniques%20of%20Molecular%20Genetics%206decb8a292624dca8b1421a1a3fd8d56/Screenshot_2022-02-26_at_12.03.29.png)

---