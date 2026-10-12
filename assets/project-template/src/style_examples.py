"""Summarize genomic windows, align sample metadata, and plot window profiles.

Inputs follow the field and coordinate conventions documented by each function.
Importing this module performs no analysis or file operations.
"""

from datetime import datetime
from time import perf_counter

import pandas as pd
from tqdm.auto import tqdm


def _assign_windows(positions, window_size):
    """Map 1-based positions to 1-based inclusive window starts."""
    return ((positions - 1) // window_size) * window_size + 1


def summarize_variant_windows(variants_df, window_size=500, min_maf=0.05):
    """
    Summarize retained variant counts and mean MAF in occupied genomic windows.

    Workflow
    --------
    1. Select variants meeting the MAF threshold.
    2. Assign 1-based positions to fixed-width windows within each chromosome.
    3. Count variants and calculate mean MAF for each occupied window.

    Parameters
    ----------
    variants_df : pandas.DataFrame
        One row per variant, with columns CHROM, POS, and MAF. POS contains
        positive integer, 1-based coordinates; MAF contains numeric values
        in [0, 0.5] or NaN. Rows are already deduplicated by the caller.
    window_size : int
        Positive window width in bp. Default is 500.
    min_maf : float
        Inclusive MAF threshold in [0, 0.5]. Default is 0.05.

    Returns
    -------
    pandas.DataFrame
        Columns CHROM, WINDOW_START, N_VARIANTS, and MEAN_MAF. Only windows
        containing retained variants appear. Missing MAF values are excluded
        by filtering; means describe retained variants, not all genomic bases.
        No files are read or written, and the input dataframe is not modified.
    """
    # Match the association-analysis background before estimating window summaries.
    retained_df = variants_df.loc[variants_df["MAF"] >= min_maf, ["CHROM", "POS", "MAF"]].copy()
    retained_df["WINDOW_START"] = _assign_windows(retained_df["POS"], window_size)

    summary_df = retained_df.groupby(["CHROM", "WINDOW_START"], as_index=False).agg(
        N_VARIANTS=("POS", "size"), MEAN_MAF=("MAF", "mean"),
    )
    return summary_df


def build_chromosome_summaries(variants_df, window_size=500, min_maf=0.05):
    """
    Calculate chromosome summaries with progress, returning one combined table.

    Workflow
    --------
    1. Group the analysis-ready variant table by chromosome.
    2. Calculate window statistics for each group with a progress bar.
    3. Combine results for the calling notebook cell to save once.

    Parameters
    ----------
    variants_df : pandas.DataFrame
        Input contract of summarize_variant_windows().
    window_size : int
        Positive window width in bp. Default is 500.
    min_maf : float
        Inclusive MAF threshold. Default is 0.05.

    Returns
    -------
    pandas.DataFrame
        Combined output of summarize_variant_windows(). Empty input returns
        an empty summary. Prints timestamps and elapsed time; tqdm reports
        completed chromosomes and rate. No files are read or written.
        The calling cell owns result saving and reuse. If interrupted, the
        calculation can restart from the beginning of that cell.
    """
    start_time = perf_counter()
    chromosome_groups = variants_df.groupby('CHROM', sort=True)
    summaries = []
    print(f'[{datetime.now():%H:%M:%S}] Summarizing {len(chromosome_groups)} chromosomes', flush=True)

    for chromosome, chromosome_df in tqdm(chromosome_groups, desc='Window summaries', unit='chromosome'):
        summary_df = summarize_variant_windows(chromosome_df, window_size=window_size, min_maf=min_maf)
        summaries.append(summary_df)

    if summaries:
        summary_df = pd.concat(summaries, ignore_index=True)
    else:
        summary_df = summarize_variant_windows(variants_df, window_size=window_size, min_maf=min_maf)
    print(f'[{datetime.now():%H:%M:%S}] Finished in {perf_counter() - start_time:.1f}s', flush=True)
    return summary_df


def align_sample_metadata(metadata_df, sample_ids, columns):
    """
    Select metadata columns in the exact genotype sample order.

    Parameters
    ----------
    metadata_df : pandas.DataFrame
        Contains a SAMPLE_ID column and the requested metadata columns.
    sample_ids : sequence of str
        Unique sample IDs in genotype row order. All must occur in metadata.
    columns : sequence of str
        Metadata columns to return, excluding SAMPLE_ID.

    Returns
    -------
    pandas.DataFrame
        Selected columns indexed by SAMPLE_ID, ordered exactly as sample_ids.
        Reads no files and does not modify the input dataframe.

    Raises
    ------
    ValueError
        Metadata or genotype IDs are duplicated, making sample alignment ambiguous.
    KeyError
        Required columns or requested sample IDs are missing (pandas exception).
    """
    sample_index = pd.Index(sample_ids, name="SAMPLE_ID")
    metadata_by_id = metadata_df.set_index("SAMPLE_ID")
    # Duplicate IDs can silently change row counts and mismatch phenotypes to genotypes.
    if not metadata_by_id.index.is_unique or not sample_index.is_unique:
        raise ValueError("Sample IDs must be unique for genotype/metadata alignment.")
    return metadata_by_id.loc[sample_index, columns]


def plot_window_maf(summary_df, chromosome, ax):
    """
    Plot mean retained-variant MAF along one chromosome on an existing axes.

    Parameters
    ----------
    summary_df : pandas.DataFrame
        Output of summarize_variant_windows().
    chromosome : str
        Chromosome identifier matching the CHROM column.
    ax : matplotlib.axes.Axes
        Axes supplied by the caller; plotting does not trigger recomputation.

    Returns
    -------
    matplotlib.axes.Axes
        The supplied axes with a line added. No files are saved or displayed.
    """
    plot_df = summary_df.loc[summary_df["CHROM"] == chromosome].sort_values("WINDOW_START")
    ax.plot(plot_df["WINDOW_START"] / 1e6, plot_df["MEAN_MAF"])
    ax.set(xlabel="Position (Mb)", ylabel="Mean MAF", title=chromosome)
    return ax
