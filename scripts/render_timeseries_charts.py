#!/usr/bin/env python3
"""Generate time-series PNG charts from data/metrics/timeseries.jsonl."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

from leaderboard_common import die, load_json

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TIMESERIES = REPO_ROOT / "data" / "metrics" / "timeseries.jsonl"
DEFAULT_LEADERBOARD = REPO_ROOT / "output" / "leaderboard.json"
DEFAULT_OUT_DIR = REPO_ROOT / "docs" / "charts"
FIG_DPI = 150


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--timeseries", type=Path, default=DEFAULT_TIMESERIES)
    p.add_argument("--leaderboard", type=Path, default=DEFAULT_LEADERBOARD)
    p.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    p.add_argument(
        "--top-models",
        type=int,
        default=15,
        help="Number of model lines to plot (selected by latest-day volume)",
    )
    p.add_argument(
        "--top-orgs",
        type=int,
        default=10,
        help="Number of organization lines to plot (selected by latest-day volume)",
    )
    return p.parse_args()


def load_timeseries(path: Path) -> list[dict]:
    if not path.is_file():
        die(f"Timeseries not found: {path}")
    records: list[dict] = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as exc:
                die(f"Invalid JSON in {path} line {line_no}: {exc}")
    records.sort(key=lambda r: r["snapshot_date"])
    return records


def row_metadata(leaderboard: dict) -> dict[str, dict[str, str | None]]:
    meta: dict[str, dict[str, str | None]] = {}
    for row in leaderboard.get("rows") or []:
        row_id = row.get("row_id")
        if not row_id:
            continue
        meta[row_id] = {
            "display_name": row.get("display_name") or row_id,
            "official_org": row.get("official_org"),
        }
    return meta


def parse_date(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%d")


def save_fig(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=FIG_DPI, bbox_inches="tight")
    plt.close()
    print(f"Wrote {path}", file=sys.stderr)


def format_axis_dates(ax: plt.Axes) -> None:
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    ax.xaxis.set_major_locator(mdates.AutoDateLocator(minticks=4, maxticks=10))
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=30, ha="right")


def top_model_ids_by_latest_30d(records: list[dict], *, top_n: int) -> list[str]:
    latest_rows = records[-1]["rows"]
    ranked = sorted(latest_rows.items(), key=lambda kv: -kv[1]["downloads_30d"])
    return [row_id for row_id, _ in ranked[:top_n]]


def top_orgs_by_latest_30d(records: list[dict], meta: dict[str, dict]) -> list[str]:
    totals: dict[str, int] = defaultdict(int)
    for row_id, row in records[-1]["rows"].items():
        org = meta.get(row_id, {}).get("official_org")
        if org:
            totals[org] += row["downloads_30d"]
    return [org for org, _ in sorted(totals.items(), key=lambda kv: -kv[1])]


def model_series(
    records: list[dict],
    row_id: str,
    *,
    value_key: str,
) -> tuple[list[datetime], list[int | None]]:
    dates: list[datetime] = []
    values: list[int | None] = []
    for rec in records:
        dates.append(parse_date(rec["snapshot_date"]))
        row = rec["rows"].get(row_id)
        values.append(row[value_key] if row and row.get("complete", True) else None)
    return dates, values


def comparable_catalogs(previous: dict, current: dict) -> bool:
    """Lifetime differences need the same catalog and complete observations."""
    identity = previous.get("manifest_hash")
    return (bool(identity) and identity == current.get("manifest_hash")
            and all(row.get("complete", True) for record in (previous, current)
                    for row in record["rows"].values()))


def model_daily_delta_series(
    records: list[dict],
    row_id: str,
) -> tuple[list[datetime], list[int | None]]:
    dates: list[datetime] = []
    values: list[int | None] = []
    for i, rec in enumerate(records):
        dates.append(parse_date(rec["snapshot_date"]))
        row = rec["rows"].get(row_id)
        previous = records[i - 1] if i else None
        previous_row = previous["rows"].get(row_id) if previous else None
        if (not row or not previous_row or not comparable_catalogs(previous, rec)):
            values.append(None)
        else:
            values.append(max(row["downloads_all_time"] - previous_row["downloads_all_time"], 0))
    return dates, values


def org_totals_per_day(
    records: list[dict],
    meta: dict[str, dict],
) -> tuple[list[datetime], dict[str, list[int | None]], dict[str, list[int | None]]]:
    dates: list[datetime] = []
    known_orgs = {
        meta[row_id]["official_org"]
        for rec in records for row_id in rec["rows"]
        if meta.get(row_id, {}).get("official_org")
    }
    org_30d: dict[str, list[int | None]] = {org: [] for org in sorted(known_orgs)}
    org_all: dict[str, list[int | None]] = {org: [] for org in sorted(known_orgs)}

    for rec in records:
        dates.append(parse_date(rec["snapshot_date"]))
        day_30d: dict[str, int] = defaultdict(int)
        day_all: dict[str, int] = defaultdict(int)
        incomplete_orgs: set[str] = set()
        for row_id, row in rec["rows"].items():
            org = meta.get(row_id, {}).get("official_org")
            if not org:
                continue
            if not row.get("complete", True):
                incomplete_orgs.add(org)
            day_30d[org] += row["downloads_30d"]
            day_all[org] += row["downloads_all_time"]
        for org in known_orgs:
            org_30d[org].append(None if org in incomplete_orgs else day_30d.get(org))
            org_all[org].append(None if org in incomplete_orgs else day_all.get(org))

    return dates, org_30d, org_all


def org_daily_deltas(records: list[dict], org_all: dict[str, list[int | None]]) -> dict[str, list[int | None]]:
    out: dict[str, list[int | None]] = {}
    for org, totals in org_all.items():
        deltas: list[int | None] = []
        for i, total in enumerate(totals):
            if (i == 0 or total is None or totals[i - 1] is None
                    or not comparable_catalogs(records[i - 1], records[i])):
                deltas.append(None)
            else:
                deltas.append(max(total - totals[i - 1], 0))
        out[org] = deltas
    return out


def values_for_plot(values: list[int | None], *, log_y: bool) -> list[float | None]:
    if not log_y:
        return values
    out: list[float | None] = []
    for value in values:
        if value is None:
            out.append(None)
        else:
            out.append(float(value))
    return out


def plot_multiline(
    path: Path,
    *,
    dates: list[datetime],
    series: dict[str, list[int | None]],
    title: str,
    ylabel: str,
    skip_first: bool = False,
    log_y: bool = False,
) -> None:
    fig, ax = plt.subplots(figsize=(11, 6))
    for label, values in series.items():
        xs = dates
        ys = values_for_plot(values, log_y=log_y)
        if skip_first and len(ys) > 1:
            xs = dates[1:]
            ys = ys[1:]
        ax.plot(xs, ys, marker="o", markersize=3, linewidth=1.5, label=label)

    ax.set_title(title, loc="left", fontsize=12)
    ax.set_xlabel("Snapshot date")
    ax.set_ylabel(ylabel)
    if log_y:
        # symlog: 0 stays at 0; values >= linthresh use log10 compression
        ax.set_yscale("symlog", linthresh=1, base=10)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1), borderaxespad=0, fontsize=8)
    format_axis_dates(ax)
    save_fig(path)


def chart_top_models_30d(
    records: list[dict],
    meta: dict[str, dict],
    out_dir: Path,
    *,
    top_n: int,
) -> None:
    row_ids = top_model_ids_by_latest_30d(records, top_n=top_n)
    series: dict[str, list[int | None]] = {}
    for row_id in row_ids:
        _, values = model_series(records, row_id, value_key="downloads_30d")
        label = meta.get(row_id, {}).get("display_name") or row_id
        series[str(label)] = values

    first = records[0]["snapshot_date"]
    last = records[-1]["snapshot_date"]
    plot_multiline(
        out_dir / "timeseries-top-models-30d.png",
        dates=[parse_date(r["snapshot_date"]) for r in records],
        series=series,
        title=f"Top {len(row_ids)} models: rolling 30-day downloads ({first} → {last})",
        ylabel="Downloads (HF rolling last 30 days, log scale)",
        log_y=True,
    )


def chart_top_models_daily(
    records: list[dict],
    meta: dict[str, dict],
    out_dir: Path,
    *,
    top_n: int,
) -> None:
    row_ids = top_model_ids_by_latest_30d(records, top_n=top_n)
    dates = [parse_date(r["snapshot_date"]) for r in records]
    series: dict[str, list[int | None]] = {}
    for row_id in row_ids:
        _, values = model_daily_delta_series(records, row_id)
        label = meta.get(row_id, {}).get("display_name") or row_id
        series[str(label)] = values

    first = records[0]["snapshot_date"]
    last = records[-1]["snapshot_date"]
    plot_multiline(
        out_dir / "timeseries-top-models-daily.png",
        dates=dates,
        series=series,
        title=f"Top {len(row_ids)} models: estimated daily downloads ({first} → {last})",
        ylabel="Δ all-time downloads (catalog-change/incomplete intervals omitted)",
        skip_first=True,
    )


def chart_orgs_30d(
    records: list[dict],
    meta: dict[str, dict],
    out_dir: Path,
    *,
    top_n: int,
) -> None:
    dates, org_30d, _ = org_totals_per_day(records, meta)
    orgs = top_orgs_by_latest_30d(records, meta)[:top_n]
    series = {org: org_30d[org] for org in orgs if org in org_30d}

    first = records[0]["snapshot_date"]
    last = records[-1]["snapshot_date"]
    plot_multiline(
        out_dir / "timeseries-orgs-30d.png",
        dates=dates,
        series=series,
        title=f"Top {len(series)} organizations: summed rolling 30-day downloads ({first} → {last})",
        ylabel="Sum of downloads (HF rolling last 30 days, log scale)",
        log_y=True,
    )


def chart_orgs_daily(
    records: list[dict],
    meta: dict[str, dict],
    out_dir: Path,
    *,
    top_n: int,
) -> None:
    dates, _, org_all = org_totals_per_day(records, meta)
    orgs = top_orgs_by_latest_30d(records, meta)[:top_n]
    deltas = org_daily_deltas(records, org_all)
    series = {org: deltas[org] for org in orgs if org in deltas}

    first = records[0]["snapshot_date"]
    last = records[-1]["snapshot_date"]
    plot_multiline(
        out_dir / "timeseries-orgs-daily.png",
        dates=dates,
        series=series,
        title=f"Top {len(series)} organizations: estimated daily downloads ({first} → {last})",
        ylabel="Δ summed all-time downloads (catalog-change/incomplete intervals omitted)",
        skip_first=True,
    )


def main() -> None:
    args = parse_args()
    if args.top_models < 1:
        die("--top-models must be >= 1")
    if args.top_orgs < 1:
        die("--top-orgs must be >= 1")

    records = load_timeseries(args.timeseries)
    if len(records) < 2:
        print(
            f"Skipping time-series charts: need at least 2 snapshots in {args.timeseries}, "
            f"found {len(records)}",
            file=sys.stderr,
        )
        return

    if not args.leaderboard.is_file():
        die(f"Leaderboard JSON not found: {args.leaderboard}")

    meta = row_metadata(load_json(args.leaderboard))
    args.out_dir.mkdir(parents=True, exist_ok=True)

    chart_top_models_30d(records, meta, args.out_dir, top_n=args.top_models)
    chart_top_models_daily(records, meta, args.out_dir, top_n=args.top_models)
    chart_orgs_30d(records, meta, args.out_dir, top_n=args.top_orgs)
    chart_orgs_daily(records, meta, args.out_dir, top_n=args.top_orgs)


if __name__ == "__main__":
    main()
