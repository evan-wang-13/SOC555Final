# File for basic processing functions


# function for cleaning submissions dataframe
def clean_for_eviction(df):
    eviction_df = df[df["outcome"] == "eviction"]

    eviction_df = eviction_df[eviction_df["truth"].notna()]
    eviction_df = eviction_df[
        (eviction_df["prediction"] <= 1) & (eviction_df["prediction"] >= 0)
    ]  # four models have invalid predictions (>1 or < 0 outputs)

    return eviction_df


def clean_for_layoff(df):
    eviction_df = df[df["outcome"] == "layoff"]

    eviction_df = eviction_df[eviction_df["truth"].notna()]
    eviction_df = eviction_df[
        (eviction_df["prediction"] <= 1) & (eviction_df["prediction"] >= 0)
    ]  # four models have invalid predictions (>1 or < 0 outputs)

    return eviction_df
