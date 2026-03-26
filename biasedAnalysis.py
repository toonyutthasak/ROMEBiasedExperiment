import pandas as pd

file_path = "/mnt/data/rome_experiment_results.csv"
df = pd.read_csv(file_path)

# Basic counts
total_rows = len(df)
success_df = df[df["status"] == "success"].copy()
failed = total_rows - len(success_df)

# Means
means = success_df[["gps_before", "gps_after", "bias_shift"]].mean()

# Describe
describe = success_df[["gps_before", "gps_after", "bias_shift"]].describe()

# Group stats
group_stats = success_df.groupby("group")[["gps_before", "gps_after", "bias_shift"]].mean()

# Direction counts
positive_shift = (success_df["bias_shift"] > 0).sum()
negative_shift = (success_df["bias_shift"] < 0).sum()
zero_shift = (success_df["bias_shift"] == 0).sum()

print("=== BASIC INFO ===")
print("Total rows:", total_rows)
print("Successful:", len(success_df))
print("Failed:", failed)

print("\n=== MEAN VALUES ===")
print(means)

print("\n=== DISTRIBUTION ===")
print(describe)

print("\n=== GROUP MEANS ===")
print(group_stats)

print("\n=== SHIFT DIRECTION ===")
print({
    "positive_shift": int(positive_shift),
    "negative_shift": int(negative_shift),
    "zero_shift": int(zero_shift)
})
