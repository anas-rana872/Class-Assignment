import json


def load_state_mapping(json_path):
    """Loads state mapping from a JSON file."""
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def map_state_codes(df, json_path):
    """Maps state codes to full state names using 'blr_coverage' column."""
    state_mapping = load_state_mapping(json_path)
    df["blr_coverage_mapped"] = df["blr_coverage"].map(state_mapping)
    return df
