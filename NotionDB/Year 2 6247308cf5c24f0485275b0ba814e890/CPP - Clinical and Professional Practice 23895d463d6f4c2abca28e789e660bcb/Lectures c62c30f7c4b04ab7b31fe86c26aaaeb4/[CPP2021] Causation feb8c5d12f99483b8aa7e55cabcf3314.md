# [CPP2021] Causation

Module: DDS

# Causation in Epidemiology

- The central aim of epidemiology is identifying the presence of cause-effect relationships: does A cause B?
- Causal inference is the process of establishing that event B (effect) is the result of the occurrence of the event A (cause)
- Knowledge of the underlying causal structure of relationships between 2 events is important for identifying effective mechanisms for prevention by targetting a cause to prevent the effect from occurring

### Assessing Causality in Observational Studies

1. Conduct Significance Test
2. Consider Bias
3. Use Bradford Hill Criteria to assist in determining whether an association is likely to be causal
- Steps 1 and 2 are undertaken in all epidemiological studies, although some biases are less of an issue in RCTs

---

# P-Values

- Significance test are used to establish evidence against the null
hypothesis that there is no difference between exposure groups in terms of occurrence of the outcome
- P-value is a probability: range 0-1 → This is the probability that there is no difference in the occurrence of the outcome between the 2 groups being tested.
- Smaller P-value:
1. Less likely observed results could occur under null
hypothesis aka due to random variation/chance.
2. Stronger evidence against null hypothesis.
- Use P-value to decide whether to reject null hypothesis.
- The decision is often made to reject H0 if p≤ 0.05
- This means that the probability of finding a difference this large in the sample, if no true difference exists (E.g by Chance), is ≤5% or about 1 in 20 significance tests will be significant when no
true difference exists
- It is better to investigate a single hypothesis of importance rather than assessing all variables within a dataset under different hypotheses as multiple testing is more likely, statistically speaking, to result in erroneous finding as when multiple tests are conducted, the probability of a statistical test concluding a significant result will increase
- About 1 in 20 significance tests will be statistically significant just due to chance

---

# Is Association Due to Other Types of Bias?

- Biases can provide alternative explanations for the association between 2 variables other than a causal association
- These are systematic distortion of data that leads to inaccurate estimates of occurrence and association
1. Selection bias (error in the way the sample is recruited or represented in a follow-up survey, leading to differences in characteristics between those included in the sample and those in the target population that are not included in the study sample)
2. Measurement bias (error in the way information is
collected from the sample, leading to misclassification of exposures, outcomes and other variables)
- Recall bias (Where cases may remember past events differently/more completely than control)
- Observer bias (E.g  E.g Interviewers may probe harder for exposure information, say on smoking, from people with lung cancer)
- Detection bias (E.g Inadequate detection of disease due to the
method of identification.)
1. Confounding bias (a variable causes both the exposure and the outcome and hence, it may partially or fully explain the association between the exposure and the outcome)

---

# Selection Bias

- E.g. a cross-sectional study in patients presenting to hospitals with acute coronary syndrome finds an association between high risk factor burden (smoking, diabetes, hypertension, &/or dyslipidemia) and decreased risk of a major adverse cardiac event (MACE)
- High Risk Factor Burden → Reduced MACE Score
- However this association may be explained by selection bias because this study includes a select group who made it
to hospital alive, it excludes people with acute coronary syndrome who had a major cardiac event and died before getting to hospital, the majority of whom had a high risk factor burden and greater severity of coronary disease. Therefore, this association is not applicable to all people with acute coronary syndrome, only to those alive in the hospital and hence, likely to have a lower risk factor burden

---

# Measurement Bias

- E.g. a case-control study finds an association between maternal exposure to organic solvents during pregnancy and increased risk of congenital malformations
- Maternal Exposure to Solvents → Congenital Malformations
- However this association may be explained by recall bias as there may be a danger of measurement bias in this study since cases may be highly motivated to find out the cause of their babies malformations and they might recall past exposure more completely than controls.
- If this is the case, bias would result in exaggerated risk estimates

---

# Reducing Selection and Measurement Bias

- These types of bias can only be fully addressed at the study design stage.
- Collecting a random sample from the target population can reduce selection bias
- Blinding the study investigator to disease/exposure status to reduce observer bias
- Standardizing diagnostic criteria to reduce diagnostic bias
- It is important to be aware of all potential biases when interpreting the results so that these biases can be minimised and where not possible, identify these biases to assess their impact on causal inference

---

# Confounding Bias

- Confounding can bias the estimate of the causal effect of A on B, by competing with A in explaining B.

![Screenshot 2022-03-13 at 16.43.13.png](%5BCPP2021%5D%20Causation%20feb8c5d12f99483b8aa7e55cabcf3314/Screenshot_2022-03-13_at_16.43.13.png)

### Is the Association Due to Confounding Bias

- A cross-sectional study finds an association between vertebroplasty and increased vertebral fracture risk
- However this association may be explained by other factors as Smoking leads to a higher risk of requiring vertebroplasty
surgery as tobacco decreases bone density and increases
risk for osteoporosis for which vertebroplasty is used to relieve osteoporotic pain, and smoking may lead to a higher risk of vertebral fracture

### Reducing Confounding Bias

- Reducing Confounding Bias is the main method of accurately determining causal relationships
- Minimizing by design
1. Randomization (RCT) - RCTs can remove confounding bias as
randomization should ensure that confounders are equally distributed across intervention and control groups → This means that RCTs can be used to estimate causal effects as confounding is unlikely to affect the association between the exposure and outcome.
2. Restriction in observational studies to make possible confounding factors (E.g Sex and Age) constants so that these variables cannot influence the association between the exposure and the outcome
3. Matching in case-control and cohort studies by potential confounders so that possible confounders that are being matched for can be equally distributed across members in the various cohorts
- Controlling in analysis (assuming the relevant confounding factor has been measured) → This is more common for addressing Confounding in Observational Studies than Altering Study Design
1. Stratification → Results may be presented according to subgroups of the potential confounder so that the confounder is equally distributed within members of this group and hence, less likely to affect the association between the exposure and outcome
2. Multivariable analysis → Adjusting for potential confounders within Analysis remove the effect of the Confoudner on the Association between the Exposure and the Outcome, which will alter the Magnitude of the Measure of Association

---

# Bradford Hill’s Criteria For Assessing Causality

- If an Association between an Exposure and an Outcome is not caused by a type of Bias and Confounding has been sufficiently address in Study Design/Analysis, The Bradford Hill Criteria can be used to assess Causality by considering the wider context of the Association
- These criteria are not needed to assess associations seen from RCTs as this study design should be able to accurately demonstrate causality without the need for additional assessment of the association context due to their complete removal of Confounding and other forms of Bias
1. Strength of association
2. Consistency of findings
3. Temporal sequence → Stronger evidence for causality comes from **longitudinal** studies (E,g Case Control) in which exposure comes before the disease outcome.
4. Biological gradient
5. Biological plausibility
6. Experimental evidence (reversibility) → Strongest evidence for causality comes from **interventional** studies that investigate whether removal of the exposure prevents the outcome.
7. Specificity of association
8. Coherence
9. Analogy
- Criteria 1-5 are commonly used to assess Causality in Observational Studies but for all these various criteria, there is no specific quantify of evidence required to say that the Criteria has been met - This is determined subjectively by the Researcher
- Causal inference in modern epidemiology: compare what actually
happened to a patient with what would have happened if,
contrary to fact, they had received alternative treatment (i.e.
compare actual outcome with counterfactual outcome).

---

# Causal Inference

- Bradford Hill’s ‘viewpoints’ for assessing causality. Usually adopt these criteria once that we have established that association is
unlikely to be due to chance, bias or confounding.

### Strength of Association

- Strong associations are less likely to be caused by chance or bias.
- We expect that causation is reflected in a p-value≤0.05
- But statistical significance is dependent on sample size
- In a small sample, associations only show up as statistically significant if there is a large difference between exposure groups
- Magnitude of association is very important in a smaller sample (regardless of statistical significance) as the smaller the sample, the greater the quantity of evidence supporting a true difference between the outcomes of 2 groups needed for a difference to be classed as statistically significant
- In all studies strong associations (greater magnitude) are less likely to be caused by chance or bias and hence, more likely to be causal
- The further away a RR is from the value of 1 the stronger the association and hence, more likely that there is to be a causal relationship

![Screenshot 2022-03-13 at 18.29.48.png](%5BCPP2021%5D%20Causation%20feb8c5d12f99483b8aa7e55cabcf3314/Screenshot_2022-03-13_at_18.29.48.png)

### Consistency of Findings

- Relationships that are demonstrated in multiple studies that utilise different populations and methods are more likely to be causal
1. Look for consistent findings
2. Across different populations
3. In different circumstances/locations
4. With different study designs

### Temporal Sequence

- Exposure MUST precede disease outcome for the Exposure to cause the Disease Outcome
- Generally easier to establish in cohort studies because participants are disease free at enrolment so therefore, the development of the disease can be attributed to a factor (E.g Exposure) that is known to be present at the baseline
- Difficult to establish in cross-sectional and case-control studies as there is no follow up of Px so the exposure cannot be accurately determined to have occurred before the Outcome

### Biological Gradient

- Evidence of a dose-response relationship whereby the outcome increases in incidence as the magnitude of the exposure increases

### Biological Plausibility

- The proposed causal mechanism should be biologically (or socially) plausible based on current scientific/sociological knowledge
- The relationship may be indirect

**Mediation**

- Mediation occurs when the association between exposure and
outcome operates through an intermediate factor (Exposure → Mediator → Outcome).
- Understanding mechanisms of association assists with causal inference as it helps to establish a temporal sequence of events.
- It is also useful to identify different potential targets to intervene in a disease which may act as mediators in the causal relationship between an exposure and outcome.

### Specificity of The Association

- If a particular exposure increases the risk of a certain disease but not the risk of other diseases (E.g Exposure increases the risk of a single outcome) then this is evidence in favour of a cause-effect relationship e.g. Exposure to asbestos and Lung Cancer
- This is a rare occurrence – typically the same exposure is likely to cause multiple diseases
- e.g. Smoking and various cancers (lung, larynx, oesophagus, mouth and pharynx, bladder, pancreas, etc.) but also CHD

### Coherence

- Coherence between epidemiological and laboratory evidence and  the association between exposure and outcome increases the likelihood of causality as there is more sufficient evidence explaining the association
- E.g. Exposure to asbestos and mesothelioma supported by lung tissue fibre analysis by scanning transmission electron microscopy (STEM)

### Analogy

- The hypothesized cause-effect relationship will be further supported if there are analogies with other (well-established) cause-effect relationships involving similar exposures and similar outcomes
- E.g. SIV causes immunosuppression in certain species of monkeys in a way that resembles what happens in humans infected with HIV

---

# Zika

### Strength of Association

- Using data from surveillance systems in Brazil, CDC reported a substantially elevated prevalence of microcephaly cases in infants born to mothers with laboratory confirmed RT-PCR prenatal Zika virus infections
- A recent retrospective study from French Polynesia (linking 4 datasets) suggests a strong association between prenatal Zika virus infection and microcephaly: risk ratio 53.4 (95% CI: 6.5, 1061.2)

### Consistency of Findings

- Two studies, one from Brazil and one from French Polynesia support the association between prenatal Zika virus infection and microcephaly
- There are case reports of Zika virus infection in foetuses and infants with microcephaly who were born to mothers who travelled to areas of active Zika virus transmission

### Temporal Sequence

- Zika virus infection in mothers during pregnancy precedes the finding of microcephaly in foetuses and infants
- Zika virus outbreaks in Brazil and French Polynesia preceded the increase in the number of cases of microcephaly

### Biological Gradient

- Infection is a phenomenon that is either present or absent; strictly speaking difficult to talk about dose–response relationship in this context
- No data are available as to whether women with an increased viral load have a higher risk of adverse pregnancy or birth outcomes

### Biological Plausibility

- Evidence that Zika virus infects neural progenitor cells and produces cell death and abnormal growth
- Evidence of Zika virus in brains of foetuses and infants with microcephaly (immuno-histochemical staining and identification of Zika virus RNA and live virus)
- The Bradford Hill Criteria should be used as a guide for the likelihood of a causal relationship but they do not give definitive conclusions on whether a relationship is causal or not - If there is still doubt on whether a Causal Relationship is present following the application of this Criteria, where appropriate, an RCT should be conducted to provide conclusive evidence on whether a causal relationship is present or not

---

# Modern Methods to Assist With Causal Inference in Observational Studies By Reducing Confounding Bias

### Causation In Modern Epidemiology

- Directed acyclic graphs (DAGs)
- Instrumental variables for Mendelian randomization

### DAGs

- Causal path diagrams
- Arrows drawn between variables of interest
- Arrows represent possible direct causal effects
- This provides a framework to explicitly define hypothesized causal effects of exposure on disease outcome
- It is clear which variables may be potential confounders which can be adjusted for in multivariable analysis, reducing confounding bias in epidemiological studies
- Supporting causal inference

### Instrumental Variables

- This is a variable that causes the exposure of interest (Exposure Variable therefore acts as a Mediator) but does not share any common causes with the outcome and therefore, the relationship between the Instrumental Variable and the Outcome is not affected by Confounding
- Therefore, assessment of Instrumental Variables are a method for reducing confounding bias in observational studies
- Genetic variants are often plausible instrumental variables as they can influence phenotype/behaviours that present as Exposures

![Screenshot 2022-03-13 at 17.34.50.png](%5BCPP2021%5D%20Causation%20feb8c5d12f99483b8aa7e55cabcf3314/Screenshot_2022-03-13_at_17.34.50.png)

### Mendelian Randomisation Studies

- Use of genetic variants as instrumental variables to investigate effects of modifiable risk factors for disease
- This is a natural randomization process as genetic alleles are allocated at random and hence, less likely to be affected by confounding or reverse causation (Temporality not an issue as inheritance of the gene always preceeds exposure)
- A Weak Instrument Bias can occur when using a genetic variant that only explains a small proportion of variation in the exposure variable, making it difficult to make inferences about the causal link between the exposure and outcome
1. Across different populations.
2. In different circumstances.
3. With different study designs.

### Temporal Sequence

- Exposure must precede disease.
- Generally easier to establish from prospective studies (cohort RCTs), because people can be selected to be disease-free at enrolment.
- Difficult to get from ecological, cross-sectional or case-control studies.

---