import pandas as pd
from pytrends.request import TrendReq


CATEGORY_KEYWORD_MAP = {
    1: "film & animation",
    2: "autos & vehicles",
    10: "music",
    15: "pets & animals",
    17: "sports",
    19: "travel & events",
    20: "gaming",
    22: "vlog",
    23: "comedy",
    24: "entertainment",
    25: "news",
    26: "how to",
    27: "education",
    28: "technology",
}


def fix_trending_date(x: str) -> str:
    yy, dd, mm = x.split(".")
    return f"20{yy}-{mm}-{dd}"


def get_trends_for_keywords(keywords, start_date, end_date, geo="US"):
    """Fetch daily Google Trends scores for a list of keywords."""
    pytrends = TrendReq(hl="en-US", tz=0)
    timeframe = f"{start_date} {end_date}"

    all_frames = []
    for kw in keywords:
        pytrends.build_payload([kw], cat=0, timeframe=timeframe, geo=geo, gprop="")
        df = pytrends.interest_over_time()
        if df.empty:
            continue
        df = df.reset_index()
        df = df.rename(columns={kw: "trend_score", "date": "date"})
        df["keyword"] = kw
        if "isPartial" in df.columns:
            df = df.drop(columns=["isPartial"])
        all_frames.append(df)

    if not all_frames:
        return pd.DataFrame(columns=["date", "keyword", "trend_score"])

    result = pd.concat(all_frames, ignore_index=True)
    return result


def build_category_trends(usvideos_path: str, output_path: str, geo: str = "US"):
    """
    Read USvideos.csv, infer the trending_date range, and fetch
    category-level daily Google Trends scores based on CATEGORY_KEYWORD_MAP.

    Creates a long-format CSV with columns:
    - date
    - category_id
    - keyword
    - trend_score
    """
    df = pd.read_csv(usvideos_path)
    df["trending_date_fixed"] = df["trending_date"].apply(fix_trending_date)
    df["trending_date"] = pd.to_datetime(df["trending_date_fixed"], errors="coerce")
    df = df.drop(columns=["trending_date_fixed"])

    min_date = df["trending_date"].min().date()
    max_date = df["trending_date"].max().date()

    keywords = sorted(set(CATEGORY_KEYWORD_MAP.values()))
    trends_df = get_trends_for_keywords(
        keywords=keywords,
        start_date=min_date.strftime("%Y-%m-%d"),
        end_date=max_date.strftime("%Y-%m-%d"),
        geo=geo,
    )

    if trends_df.empty:
        print("Warning: No trends data fetched.")
        empty = pd.DataFrame(columns=["date", "category_id", "keyword", "trend_score"])
        empty.to_csv(output_path, index=False)
        return

    rows = []
    for cat_id, kw in CATEGORY_KEYWORD_MAP.items():
        subset = trends_df[trends_df["keyword"] == kw].copy()
        if subset.empty:
            continue
        subset["category_id"] = cat_id
        rows.append(subset)

    if not rows:
        print("Warning: No matching keywords found for categories.")
        empty = pd.DataFrame(columns=["date", "category_id", "keyword", "trend_score"])
        empty.to_csv(output_path, index=False)
        return

    cat_trends = pd.concat(rows, ignore_index=True)
    cat_trends = cat_trends[["date", "category_id", "keyword", "trend_score"]]
    cat_trends.to_csv(output_path, index=False)
    print(f"Saved category trends to {output_path}")


if __name__ == "__main__":
    us_path = "data/raw/USvideos.csv"
    out_path = "data/raw/google_trends_category.csv"
    build_category_trends(us_path, out_path)
