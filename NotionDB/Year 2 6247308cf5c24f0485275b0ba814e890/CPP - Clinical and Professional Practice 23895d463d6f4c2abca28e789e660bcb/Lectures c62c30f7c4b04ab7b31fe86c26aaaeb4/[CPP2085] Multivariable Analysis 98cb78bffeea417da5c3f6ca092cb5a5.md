# [CPP2085] Multivariable Analysis

Module: DDS

# Recap

- Many epidemiological questions are about the link between an exposure and a disease outcome, in a specific population
- An exposure can be a risk factor or a protective factor

### Types of Variables

- Continuous - Variable can take any value along a scale of values e.g. blood pressure; cholesterol; quality of life scale (0-100)
- Categorical - Variable can only take discrete values/be found in discrete categories e.g. number of children; blood group; socio-economic status
- Binary (special case of categorical where there are only 2 potential values)
e.g. death (alive or dead); HIV infection (yes or no)
- Binary time-to-event (studies with follow-up only) e.g. time to death, time to first heart attack (the event may or may not
occur by the end of the study) → Time from the start of the follow up and when the Binary Outcome occurs (when outcome occurs) or total follow up time (when outcome doesn’t occur)
- The type of outcome variable in the study is one of the main factors that determines which type of statistical analysis is done

### Types of Studies

- Cross-Sectional - Recruit participants and measure exposure and disease status at one point in time (snapshot e.g Survey)
- Cohort - Follow up study where we recruit participants, measure exposure at baseline, and follow-up to identify new cases of disease outcome
- Case Control - Identify a group of people with the disease (cases) and a group of people without the disease (controls) and determine their previous exposure
status
- Randomised Control Trial - Interventional study where we recruit participants, randomly assign them at
baseline into treatment and control groups, and follow-up to identify new cases of disease outcome
- Clinical Cohort Study = Population of Interest is a group of Px with a specific condition, who are followed up to see how Disease changes over time (Mainly used to assess Prognosis and identify Risk Factors)
- Also known as Retrospective Cohort Study as it involves a Cohort that has been created from existing Medical Records, after the events have occurred (Still Cohort Study as it involves an initial assessment of Exposures and follow-up)

### Follow Up

- Graph = Person against Calendar Date
- Duration of Follow Up and when it occurs is indicated by a Horizontal Blue Line (Person Time At Risk AKA Duration of time during which Px is at risk of developing outcome within the study)
- Death/Outcome of Interest = Red Diamond on Right Most Point of the Horizontal Line
- Px lost to follow up = Hollow/Open Blue Circle on Right Most Point of the Horizontal Line
- Solid Blue Circle at the Left most point of the Horizontal Line = Point in Time at which Px enters the Cohort
- If a Cohort consists of Px who enter the Cohort at different points of time, outcome measures should be Binary Time to Event Vs Binary as different Px have different Person Times At Risk and hence, are at risk of the outcome for a different duration of time

![Screenshot 2022-02-13 at 19.28.36.png](%5BCPP2085%5D%20Multivariable%20Analysis%2098cb78bffeea417da5c3f6ca092cb5a5/Screenshot_2022-02-13_at_19.28.36.png)

---

# Measures of Association

| Type of Outcome Variable | Measure of Association Between Exposure and Outcome (Presented with 95% CI) | Formula |
| --- | --- | --- |
| Binary | 1) Odds Ratio 2) Risk Ratio 3) Prevalent Ratio 4) Risk Difference | 1) Odds in exposed / odds in unexposed 2) Risk in exposed / risk in unexposed
3) Prevalence in exposed / Prevalence in unexposed
4) Risk in exposed - risk in unexposed |
| Binary Time-To-Event | 1) Rate Ratio 2) Hazard Ratio | 1) Rate in exposed / rate in unexposed 2) From a Model |
| Continuous | Mean difference | Mean in exposed - mean in unexposed |

---

# Simple, Unadjusted Analysis

- Calculate the Unadjusted Association Measure using the formula as normal
- When calculating a ratio for a variable with >2 categories, one category is defined as Reference/Unexposed and all other categories are compared to the Unexposed Category individually to produce multiple Ratios

---

# Why is Multivariable Analysis Needed?

- Unadjusted analysis alone is not usually sufficient for observational studies due to the problem of confounding from other factors
- A confounding factor is one that is associated with the exposure and with the outcome
- If we fail to control for confounding, we can get a distorted view of the relationship between exposure and outcome due to the effect of the Confounding Factor on both the exposure and the outcome
- In this example, age, SES, place of diagnosis were considered potential confounders in the relationship between gender and mortality
- A multivariable regression model can be used to adjust for the confounding factors that have been measured (Unmeasured Confounding Factors cannot be controlled/adjusted for within the Regression Model)
- A multivariable model estimates the independent effects of several variables on the outcome

---

# Multivariable Model

- In a statistical model, the outcome variable is also called the dependent variable
- The exposure variables in the model are called independent variables (may also be called: explanatory; predictor; covariates)
- In the simple univariable (unadjusted) analysis there is only one independent variable – the single exposure
- In a multivariable (adjusted) analysis there is more than one independent variable – a set of exposure variables (the exposure of interest and other possible confounding factors)
- The ‘independent’ variables are used together to predict the value of the ‘dependent’ variable in a statistical regression model at different values of the independent variables (model the relationship between the Independent Variables together and the dependent variables)
- E.g. Linear Regression: $y=a+b_1x1+b_2x2+b_3x3...$ , where y = Dependent Variable and x1,x2 and x3 are Independent/Exposure Variables
- This regression model is performed using statistical software (e.g. STATA, SPSS, SAS)
- All types of multivariable model can deal
with a combination of binary, categorical or continuous exposure/independent variables considered within one type of model, producing individual adjusted measures of association for each variable and category included in the regression
- The type of outcome variable
determines the type of statistical regression model used

---

# Common Multivariable Models Interpreted Adjusted Association Measures

| Type of Outcome Variable | Multivariable Model | Measure of Adjusted Association Between Exposure and Outcome Produced by the Model (Presented with 95% CI) |
| --- | --- | --- |
| Binary | 1) Logistic Regression 2) Poisson Regression | 1) Adjusted Odds Ratio 2) Adjusted Risk/Prevalence Ratio |
| Binary Time-To-Event | 1) Poisson Regression 2) Cox-Proportional Hazards Regression | 1) Adjusted Rate Ratio 2) Adjusted Hazard Ratio (Obtained from a Model) |
| Continuous | Linear Regression | Adjusted Mean Difference |

---

# Effect of Adjustment in Multivariable Analysis

- When we use a multivariable model to assess the independent associations between a set of exposures and an outcome variable, the adjusted rate ratio for an exposure may be weaker, stronger or the same as the unadjusted rate ratio
- This is because the presence of confounding factors can obscure or even, completely remove a relationship as well as exaggerate it
- Adjusted Measure of Association = Association Measure seen when other independent variables included in the Multivariable Regression Model are controlled
- In some cases of extreme confounding (as for gender here) the direction of the association (increase/decreased risk) can be reversed in the adjusted analysis
- Comparing the Unadjusted and Adjusted Measures of Association can be used to assess the effect of confounding on the association between an Exposure and an Outcome

---

# Exposure/Independent Variables and Reference Categories

- Our example includes binary and categorical exposure (independent) variables
- Each binary or categorical variable has a reference category - conventionally chosen to be the “unexposed” group
- Choice of this reference category is arbitrary – the model and conclusions drawn from the results are identical if a difference category is chosen

---

# Risk, Odds and Rate

![Screenshot 2022-02-12 at 19.07.59.png](%5BCPP2085%5D%20Multivariable%20Analysis%2098cb78bffeea417da5c3f6ca092cb5a5/Screenshot_2022-02-12_at_19.07.59.png)

---

# Types of Study and Measure of Association

- Cross-Sectional and Case Control Studies cannot produce Binary Time to Event Outcomes as they do not have any follow up period, during which PYAR can be determined
- Case Control can only produce Binary Outcomes as the outcomes are selected at the start of the trial as those who are exposed and those who are unexposed

![Screenshot 2022-02-12 at 19.08.30.png](%5BCPP2085%5D%20Multivariable%20Analysis%2098cb78bffeea417da5c3f6ca092cb5a5/Screenshot_2022-02-12_at_19.08.30.png)

---

# RCTs and Multivariable Analyses

- Multivariable models are usually necessary in analysis of observational studies and non-randomised controlled trials to adjust for confounding factors
- In an RCT, the treatment and control groups are very similar with respect to the distribution potentially confounding factors at baseline between the 2 cohorts due to the randomisation – so there is no confounding when assessing the effect of treatment on outcome
- Therefore multivariable models are not usually necessary for comparing treatment groups in an RCT
- Exceptions are:
1. If the randomisation has not worked well and the randomised groups differ at baseline with regard to the distribution of important factors, which can then act as confounders
2. For more complex RCT designs (not covered in this course)

---

# Clinical Prediction Models

- Important application of multivariable analysis is the development of prediction models used in medical care
- A number of Px variables can be used jointly to predict the probability of a disease outcome occurring.
- The outcome may be related to disease incidence or prognosis.
- Often called ‘risk score’ or ‘risk stratification’ - used in almost every area of medicine
- Example: CHD risk scores used routinely to identify patients at high risk of a CHD event, who need preventative treatment (e.g. statins)
- Score is developed from a multivariable model from analysis of large cohort study.
- A limited number of easily measured
explanatory variables are used to predict occurrence of a CHD outcome event
- These are particularly useful to assess overall effect of a number of identified risk factors (alongside their magnitude and strength of association to the disease outcome) on the overall risk of developing a specific disease outcome

---