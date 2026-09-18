#!/usr/bin/env python3
from pathlib import Path
import argparse
import numpy as np
from PIL import Image

NUM_CLASSES = 32

CLASS_NAMES = [
    "Road","Sidewalk","Parking Lot","Soil","Pedestrian","Driver",
    "Car","Truck","Bus","Motorcycle","Bicycle","Traffic Light",
    "Traffic Sign","Pole","Garbage Box","Sitting Bench",
    "Infrastructure Cover","Infrastructure Box","Parking Barrier",
    "Building","Wall","Fence","Stairs","Railing","Overpass",
    "Water Surface","Sky","Tree","Grass","Pruned Tree",
    "Operator and Shadow","Void"
]

PALETTE = np.array([
    [128,  64, 128],  # 0 Road
    [244,  35, 232],  # 1 Sidewalk
    [250, 170, 160],  # 2 Parking Lot
    [192, 182, 154],  # 3 Soil
    [220,  20,  60],  # 4 Pedestrian
    [255,   0,   0],  # 5 Driver
    [  0,   0, 142],  # 6 Car
    [  0,   0,  70],  # 7 Truck
    [  0,  60, 100],  # 8 Bus
    [  0,   0, 230],  # 9 Motorcycle
    [119,  11,  32],  # 10 Bicycle
    [250, 170,  30],  # 11 Traffic Light
    [220, 220,   0],  # 12 Traffic Sign
    [153, 153, 153],  # 13 Pole
    [137, 145, 169],  # 14 Garbage Box
    [145, 161, 153],  # 15 Sitting Bench
    [ 74,  68,  42],  # 16 Infrastructure Cover
    [ 54,  95, 145],  # 17 Infrastructure Box
    [255, 129,   0],  # 18 Parking Barrier
    [ 70,  70,  70],  # 19 Building
    [102, 102, 156],  # 20 Wall
    [190, 153, 153],  # 21 Fence
    [217, 149, 148],  # 22 Stairs
    [180, 165, 180],  # 23 Railing
    [178, 161, 199],  # 24 Overpass
    [ 51, 102, 255],  # 25 Water Surface
    [ 70, 130, 180],  # 26 Sky
    [107, 142,  35],  # 27 Tree
    [194, 214, 155],  # 28 Grass
    [  0, 176,  80],  # 29 Pruned Tree
    [  0,   0,  30],  # 30 Operator and Shadow
    [  0,   0,   0],  # 31 Void
], dtype=np.uint8)

def read_label(path: Path) -> np.ndarray:
    with Image.open(path) as img:
        label = np.array(img)
    if label.ndim != 2:
        raise ValueError(f"{path.name}: expected single-channel PNG, got {label.shape}")
    label = label.astype(np.int64, copy=False)
    bad = (label < 0) | (label >= NUM_CLASSES)
    if np.any(bad):
        raise ValueError(f"{path.name}: invalid class IDs {np.unique(label[bad]).tolist()}")
    return label

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", required=True)
    parser.add_argument("--output_dir", required=True)
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    files = sorted(input_dir.glob("*.png"))
    if not files:
        raise RuntimeError(f"No PNG files found in: {input_dir}")

    for i, input_path in enumerate(files, start=1):
        label = read_label(input_path)
        rgb = PALETTE[label]

        # Keep exactly the same filename in the output folder.
        output_path = output_dir / input_path.name
        Image.fromarray(rgb.astype(np.uint8), mode="RGB").save(output_path)

        ids = np.unique(label).tolist()
        print(f"[{i}/{len(files)}] {input_path.name} -> {output_path.name} | IDs: {ids}")

    print(f"\nDone. {len(files)} colorized PNG(s) saved to: {output_dir}")

if __name__ == "__main__":
    main()
