import numpy as np
from scipy import stats

def sample_size_for_proportion_precision(expected_proportion, desired_precision, confidence_level=0.95):
    """
    Calculate sample size needed to estimate a proportion with desired precision.
    
    Parameters:
    expected_proportion: Anticipated proportion (0-1)
    desired_precision: Half-width of desired confidence interval
    confidence_level: Confidence level (default 0.95)
    
    Returns:
    Required sample size
    """
    z = stats.norm.ppf(1 - (1 - confidence_level) / 2)
    n = (z**2 * expected_proportion * (1 - expected_proportion)) / (desired_precision**2)
    return np.ceil(n)

def adjust_for_heterogeneity(sample_size, expected_i_squared):
    """
    Adjust sample size for expected heterogeneity in meta-analysis.
    
    Parameters:
    sample_size: Initial sample size calculation
    expected_i_squared: Expected I² (0-1)
    
    Returns:
    Adjusted sample size
    """
    return np.ceil(sample_size / (1 - expected_i_squared))

def trials_needed(total_sample_size, avg_trial_size):
    """
    Calculate number of trials needed.
    
    Parameters:
    total_sample_size: Required total sample
    avg_trial_size: Average number of participants per trial
    
    Returns:
    Number of trials needed
    """
    return np.ceil(total_sample_size / avg_trial_size)

# Define parameters
key_group = "Indigenous"
expected_proportion = 0.05  # Expected proportion of Indigenous participants
desired_precision = 0.02    # Precision of ±2%
heterogeneity = 0.5         # Expected I² of 0.5
avg_trial_size = 100        # Average participants per pediatric RCT in Canada

# Calculate required sample size
required_n = sample_size_for_proportion_precision(expected_proportion, desired_precision)
adjusted_n = adjust_for_heterogeneity(required_n, heterogeneity)
min_trials = trials_needed(adjusted_n, avg_trial_size)

# Format the paragraph
paragraph = f"""We determined that a minimum of {int(min_trials)} trials with a total of approximately {int(adjusted_n)} participants would be required to estimate the proportion of {key_group} participants with a precision of ±{int(desired_precision*100)}% at a 95% confidence level, accounting for anticipated between-study heterogeneity (I² = {heterogeneity}). This sample size will allow meaningful inferences about underrepresentation across the PROGRESS-PLUS characteristics."""

print(paragraph)

# Additional calculations for other key groups
key_groups = {
    "Indigenous": 0.05,
    "Rural residents": 0.15,
    "Preferred language other than English": 0.20,
    "Low socioeconomic status": 0.25
}

print("\nSample size requirements for other key groups:")
for group, prop in key_groups.items():
    req_n = sample_size_for_proportion_precision(prop, desired_precision)
    adj_n = adjust_for_heterogeneity(req_n, heterogeneity)
    trials = trials_needed(adj_n, avg_trial_size)
    print(f"{group} (expected proportion {prop*100}%): {int(trials)} trials, {int(adj_n)} participants")
    