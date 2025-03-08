# Sample Size Calculation for Meta-Epidemiologic Studies of PROGRESS-PLUS Characteristics

This repository contains code for calculating the required sample size in meta-epidemiologic studies examining equity-related factors in clinical trials using the PROGRESS-PLUS framework.

## Background

Meta-epidemiologic studies examining diversity and equity in clinical trials require appropriate sample size calculations. This code provides a precision-based approach to estimate the required number of trials and participants to make meaningful inferences about the representation of various demographic groups.

## Methodology

The approach uses three key functions:

1. `sample_size_for_proportion_precision()`: Calculates the basic sample size needed to estimate a proportion with a desired precision at a specific confidence level
2. `adjust_for_heterogeneity()`: Adjusts the sample size to account for between-study heterogeneity (I²)
3. `trials_needed()`: Converts the required sample size to the number of trials needed based on average trial size

### Formulas Used

The sample size calculation is based on the formula:

```
n = (z² × p × (1-p)) / d²
```

Where:
- n = required sample size
- z = standard normal deviate (1.96 for 95% confidence)
- p = expected proportion
- d = desired precision (half-width of confidence interval)

The heterogeneity adjustment uses:

```
n_adjusted = n / (1-I²)
```

Where I² represents the expected between-study heterogeneity (0-1).

## Usage

To use this code for your own meta-epidemiologic study:

1. Set the `expected_proportion` based on the anticipated prevalence of your demographic group of interest
2. Set `desired_precision` to your desired confidence interval half-width (e.g., 0.02 for ±2%)
3. Set `heterogeneity` to your expected I² value (0.5 represents moderate heterogeneity)
4. Set `avg_trial_size` to the expected average number of participants per trial in your field

The code will output:
- A formatted paragraph for your methods section
- Calculations for multiple demographic groups of interest

## Example Output

```
We determined that a minimum of 10 trials with a total of approximately 914 participants would be required to estimate the proportion of Indigenous participants with a precision of ±2% at a 95% confidence level, accounting for anticipated between-study heterogeneity (I² = 0.5). This sample size will allow meaningful inferences about underrepresentation across the PROGRESS-PLUS characteristics.

Sample size requirements for other key groups:
Indigenous (expected proportion 5%): 10 trials, 914 participants
Rural residents (expected proportion 15%): 13 trials, 1276 participants
Preferred language other than English (expected proportion 20%): 16 trials, 1536 participants
Low socioeconomic status (expected proportion 25%): 18 trials, 1800 participants
```

## Customization for Different Studies

This approach can be tailored for different meta-epidemiologic studies by:

1. Modifying the key demographic groups and their expected proportions
2. Adjusting the precision requirements based on study objectives
3. Setting different heterogeneity expectations based on prior literature
4. Changing the average trial size to match your specific research area

## Limitations

These calculations assume:
- Random sampling of trials
- Accurate estimation of expected proportions
- Reasonably accurate estimation of between-study heterogeneity

For very rare characteristics (proportion <1%) or highly heterogeneous fields (I² >80%), additional considerations may be needed.

## References

1. Lin L, Chu H. Meta-analysis of proportions using generalized linear mixed models. Epidemiology. 2020;31(5):713-717.
2. Riley RD, Ensor J, Snell KIE, et al. Calculating the sample size required for developing a clinical prediction model. BMJ. 2020;368:m441.
3. Borenstein M, Hedges LV, Higgins JP, Rothstein HR. Introduction to Meta-Analysis. John Wiley & Sons; 2011.

