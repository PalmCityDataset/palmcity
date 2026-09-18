#!/usr/bin/env python3
"""
PalmCity Codabench scoring program.

Expected participant submission
-------------------------------
A ZIP containing one single-channel PNG prediction mask per test image.
After Codabench extracts the submission, the masks are available under:

    /app/input/res/

Hidden PalmCity test ground-truth masks are available only to the scorer under:

    /app/input/ref/

Prediction filenames must match the corresponding ground-truth filenames.

Example:
    /app/input/ref/GS__0772.png
    /app/input/res/GS__0772.png

Label definition
----------------
PalmCity uses 32 semantic classes with IDs 0..31.
Road = 0 and the remaining classes increase sequentially to Void = 31.

No class is ignored. All 32 classes are evaluated.

Leaderboard outputs
-------------------
scores.json:
    {
        "miou": ...,
        "mf1": ...
    }

Scores are written as percentages, e.g. 46.02 rather than 0.4602.
"""

import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image


NUM_CLASSES = 32

CLASS_NAMES = [
    "Road",                    # 0
    "Sidewalk",                # 1
    "Parking Lot",             # 2
    "Soil",                    # 3
    "Pedestrian",              # 4
    "Driver",                  # 5
    "Car",                     # 6
    "Truck",                   # 7
    "Bus",                     # 8
    "Motorcycle",              # 9
    "Bicycle",                 # 10
    "Traffic Light",           # 11
    "Traffic Sign",            # 12
    "Pole",                    # 13
    "Garbage Box",             # 14
    "Sitting Bench",           # 15
    "Infrastructure Cover",    # 16
    "Infrastructure Box",      # 17
    "Parking Barrier",         # 18
    "Building",                # 19
    "Wall",                    # 20
    "Fence",                   # 21
    "Stairs",                  # 22
    "Railing",                 # 23
    "Overpass",                # 24
    "Water Surface",           # 25
    "Sky",                     # 26
    "Tree",                    # 27
    "Grass",                   # 28
    "Pruned Tree",             # 29
    "Operator and Shadow",     # 30
    "Void",                    # 31
]


def collect_pngs(folder: Path):
    """
    Recursively collect PNG files and index them by filename.

    This allows a participant ZIP to contain a folder such as:
        predictions/GS__0772.png

    while still matching the hidden reference:
        GS__0772.png
    """
    files = {}
    for path in folder.rglob("*.png"):
        name = path.name

        if name in files:
            raise RuntimeError(
                f"Duplicate PNG filename found: {name}. "
                "Every prediction filename must be unique."
            )

        files[name] = path

    return files


def read_mask(path: Path):
    """Read and validate a PalmCity class-ID PNG mask."""
    with Image.open(path) as image:
        mask = np.asarray(image)

    if mask.ndim != 2:
        raise ValueError(
            f"{path.name}: expected a single-channel class-ID PNG, "
            f"but received shape {mask.shape}. "
            "Do not submit RGB/colorized masks."
        )

    mask = mask.astype(np.int64, copy=False)

    invalid = (mask < 0) | (mask >= NUM_CLASSES)

    if np.any(invalid):
        bad_ids = np.unique(mask[invalid]).tolist()
        raise ValueError(
            f"{path.name}: invalid class IDs {bad_ids}. "
            f"PalmCity class IDs must be between 0 and {NUM_CLASSES - 1}."
        )

    return mask


def update_confusion_matrix(confusion, gt, pred, filename):
    if gt.shape != pred.shape:
        raise ValueError(
            f"{filename}: size mismatch. "
            f"Ground truth shape = {gt.shape}, "
            f"prediction shape = {pred.shape}."
        )

    encoded = NUM_CLASSES * gt.reshape(-1) + pred.reshape(-1)

    confusion += np.bincount(
        encoded,
        minlength=NUM_CLASSES * NUM_CLASSES
    ).reshape(NUM_CLASSES, NUM_CLASSES)


def calculate_metrics(confusion):
    """
    Compute IoU and F1 from the dataset-level confusion matrix.

    All PalmCity classes 0..31 are used. There is no ignore class.
    """
    true_positive = np.diag(confusion).astype(np.float64)
    gt_count = confusion.sum(axis=1).astype(np.float64)
    pred_count = confusion.sum(axis=0).astype(np.float64)

    false_positive = pred_count - true_positive
    false_negative = gt_count - true_positive

    iou_denominator = (
        true_positive + false_positive + false_negative
    )

    f1_denominator = (
        2.0 * true_positive + false_positive + false_negative
    )

    iou = np.zeros(NUM_CLASSES, dtype=np.float64)
    f1 = np.zeros(NUM_CLASSES, dtype=np.float64)

    valid_iou = iou_denominator > 0
    valid_f1 = f1_denominator > 0

    iou[valid_iou] = (
        true_positive[valid_iou] /
        iou_denominator[valid_iou]
    )

    f1[valid_f1] = (
        2.0 * true_positive[valid_f1] /
        f1_denominator[valid_f1]
    )

    # Exactly 32 classes are included in both macro averages.
    miou = float(iou.mean())
    mf1 = float(f1.mean())

    return iou, f1, miou, mf1


def write_detailed_results(output_path, iou, f1, miou, mf1):
    rows = []

    for class_id, class_name in enumerate(CLASS_NAMES):
        rows.append(
            "<tr>"
            f"<td>{class_id}</td>"
            f"<td>{class_name}</td>"
            f"<td>{iou[class_id] * 100.0:.2f}</td>"
            f"<td>{f1[class_id] * 100.0:.2f}</td>"
            "</tr>"
        )

    html = f"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>PalmCity Evaluation</title>
<style>
body {{ font-family: Arial, sans-serif; }}
table {{ border-collapse: collapse; }}
th, td {{ border: 1px solid #ccc; padding: 6px 10px; text-align: center; }}
</style>
</head>
<body>
<h2>PalmCity Evaluation</h2>
<p><strong>mIoU:</strong> {miou * 100.0:.2f}%</p>
<p><strong>mF1:</strong> {mf1 * 100.0:.2f}%</p>
<p>All 32 PalmCity classes (IDs 0-31) are evaluated. No class is ignored.</p>
<table>
<tr>
<th>ID</th>
<th>Class</th>
<th>IoU (%)</th>
<th>F1 (%)</th>
</tr>
{''.join(rows)}
</table>
</body>
</html>
"""

    output_path.write_text(
        html,
        encoding="utf-8"
    )


def main():
    # metadata.yaml calls:
    # python3 /app/program/scoring.py /app/input /app/output
    input_root = (
        Path(sys.argv[1])
        if len(sys.argv) > 1
        else Path("/app/input")
    )

    output_root = (
        Path(sys.argv[2])
        if len(sys.argv) > 2
        else Path("/app/output")
    )

    reference_dir = input_root / "ref"
    prediction_dir = input_root / "res"

    output_root.mkdir(
        parents=True,
        exist_ok=True
    )

    if not reference_dir.exists():
        raise RuntimeError(
            f"Reference directory not found: {reference_dir}"
        )

    if not prediction_dir.exists():
        raise RuntimeError(
            f"Prediction directory not found: {prediction_dir}"
        )

    gt_files = collect_pngs(reference_dir)
    pred_files = collect_pngs(prediction_dir)

    if not gt_files:
        raise RuntimeError(
            "No hidden reference PNG masks were found."
        )

    if not pred_files:
        raise RuntimeError(
            "The submission contains no PNG prediction masks."
        )

    gt_names = set(gt_files)
    pred_names = set(pred_files)

    missing = sorted(gt_names - pred_names)
    extra = sorted(pred_names - gt_names)

    if missing:
        example = ", ".join(missing[:10])
        raise RuntimeError(
            f"Submission is missing {len(missing)} prediction mask(s). "
            f"Example: {example}"
        )

    if extra:
        example = ", ".join(extra[:10])
        raise RuntimeError(
            f"Submission contains {len(extra)} unexpected PNG mask(s). "
            f"Example: {example}"
        )

    confusion = np.zeros(
        (NUM_CLASSES, NUM_CLASSES),
        dtype=np.int64
    )

    filenames = sorted(gt_names)

    for index, filename in enumerate(filenames, start=1):
        gt = read_mask(
            gt_files[filename]
        )

        pred = read_mask(
            pred_files[filename]
        )

        update_confusion_matrix(
            confusion,
            gt,
            pred,
            filename
        )

        print(
            f"Evaluated {index}/{len(filenames)}: {filename}"
        )

    iou, f1, miou, mf1 = calculate_metrics(
        confusion
    )

    # Leaderboard values are percentages.
    scores = {
        "miou": round(miou * 100.0, 6),
        "mf1": round(mf1 * 100.0, 6)
    }

    scores_path = output_root / "scores.json"

    scores_path.write_text(
        json.dumps(scores),
        encoding="utf-8"
    )

    write_detailed_results(
        output_root / "detailed_results.html",
        iou,
        f1,
        miou,
        mf1
    )

    print("\nPalmCity final scores")
    print("---------------------")
    print(f"mIoU : {scores['miou']:.2f}%")
    print(f"mF1  : {scores['mf1']:.2f}%")
    print(f"\nSaved: {scores_path}")


if __name__ == "__main__":
    main()
