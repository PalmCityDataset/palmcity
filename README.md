<div align="center">

# 🌴 PalmCity

### A Benchmark Dataset for Semantic Segmentation of Panoramic Urban Street View Images

**Urban Scene Understanding • Panoramic Street View Imagery • Semantic Segmentation • GeoAI**

`[Project Website: https://palmcity-dataset.com/]`  `[ Download Dataset ]`  `[ Paper ]`  `[ Benchmark ]`

---

**PalmCity** is a large-scale urban scene understanding dataset designed for semantic segmentation of panoramic street-level imagery, with a particular focus on urban environments that are under-represented in conventional computer vision benchmarks.

The dataset was collected in **Mersin, Türkiye**, and provides detailed pixel-level semantic annotations covering transportation infrastructure, buildings, vegetation, street furniture, vehicles, pedestrians, and other elements of the urban environment.

</div>

---

## 🏙️ About PalmCity

Existing urban scene understanding datasets such as Cityscapes have played a central role in the development of semantic segmentation algorithms. However, models trained predominantly on cities from developed countries may not fully represent the architectural characteristics, street morphology, transportation patterns, vegetation, street furniture, and heterogeneous urban structures encountered in other geographic regions.

PalmCity was developed to help address this gap.

The dataset provides densely annotated panoramic street-view imagery representing the visual and semantic complexity of a Mediterranean urban environment in Türkiye. It is intended to support research on:

- Semantic segmentation
- Urban scene understanding
- Panoramic image analysis
- GeoAI and urban analytics
- Domain adaptation and domain generalization
- Cross-dataset evaluation
- Urban morphology analysis
- Street-level environmental indicators

PalmCity can also be used to investigate the transferability of models trained on established benchmarks such as Cityscapes and ADE20K to geographically distinct urban environments.

---

## 📊 Dataset Characteristics

| Property | PalmCity |
|---|---|
| Location | Mersin, Türkiye |
| Image Type | Panoramic Street View Imagery |
| Acquisition | 360° street-level imaging |
| Primary Task | Semantic Segmentation |
| Annotation Type | Dense pixel-level semantic masks |
| Number of Classes | **32 semantic classes** |
| Number of Images | `{TOTAL_IMAGES}` |
| Training Images | `{TRAIN_IMAGES}` |
| Validation Images | `{VAL_IMAGES}` |
| Test Images | `{TEST_IMAGES}` |
| Image Resolution | `{ORIGINAL_RESOLUTION}` |
| Geographic Context | Mediterranean / developing-country urban environment |

---

## 🎨 Semantic Classes

PalmCity contains **32 semantic classes** representing major components of the urban environment.

A detailed class definition table should be provided here using the official PalmCity label IDs.

| ID | Class | Category | Color |
|---:|---|---|---|
| 0 | Road | Flat Surface | ![#804080](https://placehold.co/15x15/804080/804080.png) `Road` |
| 1 | Sidewalk | Flat Surface | ![#F423E8](https://placehold.co/15x15/F423E8/F423E8.png) `Sidewalk` |
| 2 | Parking Lot | Flat Surface | ![#FAAAA0](https://placehold.co/15x15/FAAAA0/FAAAA0.png) `Parking Lot` |
| 3 | Soil | Flat Surface | ![#C0B69A](https://placehold.co/15x15/C0B69A/C0B69A.png) `Soil` |
| 4 | Pedestrian | Person | ![#DC143C](https://placehold.co/15x15/DC143C/DC143C.png) `Pedestrian` |
| 5 | Driver | Person | ![#FF0000](https://placehold.co/15x15/FF0000/FF0000.png) `Driver` |
| 6 | Car | Vehicle | ![#00008E](https://placehold.co/15x15/00008E/00008E.png) `Car` |
| 7 | Truck | Vehicle | ![#000046](https://placehold.co/15x15/000046/000046.png) `Truck` |
| 8 | Bus | Vehicle | ![#003C64](https://placehold.co/15x15/003C64/003C64.png) `Bus` |
| 9 | Motorcycle | Vehicle | ![#0000E6](https://placehold.co/15x15/0000E6/0000E6.png) `Motorcycle` |
| 10 | Bicycle | Vehicle | ![#770B20](https://placehold.co/15x15/770B20/770B20.png) `Bicycle` |
| 11 | Traffic Light | Object | ![#FAAA1E](https://placehold.co/15x15/FAAA1E/FAAA1E.png) `Traffic Light` |
| 12 | Traffic Sign | Object | ![#DCDC00](https://placehold.co/15x15/DCDC00/DCDC00.png) `Traffic Sign` |
| 13 | Pole | Object | ![#999999](https://placehold.co/15x15/999999/999999.png) `Pole` |
| 14 | Garbage Box | Object | ![#8991A9](https://placehold.co/15x15/8991A9/8991A9.png) `Garbage Box` |
| 15 | Sitting Bench | Object | ![#91A199](https://placehold.co/15x15/91A199/91A199.png) `Sitting Bench` |
| 16 | Infrastructure Cover | Object | ![#4A442A](https://placehold.co/15x15/4A442A/4A442A.png) `Infrastructure Cover` |
| 17 | Infrastructure Box | Object | ![#365F91](https://placehold.co/15x15/365F91/365F91.png) `Infrastructure Box` |
| 18 | Parking Barrier | Object | ![#FF8100](https://placehold.co/15x15/FF8100/FF8100.png) `Parking Barrier` |
| 19 | Building | Construction | ![#464646](https://placehold.co/15x15/464646/464646.png) `Building` |
| 20 | Wall | Construction | ![#66669C](https://placehold.co/15x15/66669C/66669C.png) `Wall` |
| 21 | Fence | Construction | ![#BE9999](https://placehold.co/15x15/BE9999/BE9999.png) `Fence` |
| 22 | Stairs | Construction | ![#D99594](https://placehold.co/15x15/D99594/D99594.png) `Stairs` |
| 23 | Railing | Construction | ![#B4A5B4](https://placehold.co/15x15/B4A5B4/B4A5B4.png) `Railing` |
| 24 | Overpass | Construction | ![#B2A1C7](https://placehold.co/15x15/B2A1C7/B2A1C7.png) `Overpass` |
| 25 | Water Surface | Water Surface | ![#3366FF](https://placehold.co/15x15/3366FF/3366FF.png) `Water Surface` |
| 26 | Sky | Sky | ![#4682B4](https://placehold.co/15x15/4682B4/4682B4.png) `Sky` |
| 27 | Tree | Green Area | ![#6B8E23](https://placehold.co/15x15/6B8E23/6B8E23.png) `Tree` |
| 28 | Grass | Green Area | ![#C2D69B](https://placehold.co/15x15/C2D69B/C2D69B.png) `Grass` |
| 29 | Pruned Tree | Green Area | ![#00B050](https://placehold.co/15x15/00B050/00B050.png) `Pruned Tree` |
| 30 | Operator and Shadow | Operator and Shadow | ![#00001E](https://placehold.co/15x15/00001E/00001E.png) `Operator and Shadow` |
| 31 | Void | Void | ![#000000](https://placehold.co/15x15/000000/000000.png) `Void` |

The complete class definitions, label IDs, training IDs, visualization colors, and ignored labels are available in:

`palmcity/labels.py`

---

## 🖼️ Sample Annotations

<div align="center">

### Original Image

`[ PLACE ORIGINAL PANORAMIC IMAGE HERE ]`

### Ground-Truth Semantic Annotation

`[ PLACE COLORIZED SEMANTIC MASK HERE ]`

### Image + Annotation

`[ PLACE SIDE-BY-SIDE / OVERLAY EXAMPLE HERE ]`

</div>

We strongly recommend including at least **three different urban scenes** here so that visitors immediately understand the visual diversity of PalmCity.

---

## 📁 Dataset Structure

PalmCity follows a simple Cityscapes-inspired organization.

```text
PalmCity/
│
├── images/
│   ├── train/
│   ├── val/
│   └── test/
│
├── annotations/
│   ├── train/
│   ├── val/
│   └── test/
│
├── splits/
│   ├── train.txt
│   ├── val.txt
│   └── test.txt
│
├── palmcity/
│   ├── labels.py
│   ├── visualization.py
│   ├── preparation.py
│   └── evaluation.py
│
└── README.md
```

Each semantic annotation image contains the pixel-wise class labels corresponding to its associated panoramic RGB image.

---

## ⬇️ Download

The PalmCity dataset can be downloaded from the official dataset distribution page.

### Dataset

**PalmCity Images**

`<DATASET_IMAGE_DOWNLOAD_LINK>`

**PalmCity Semantic Annotations**

`<ANNOTATION_DOWNLOAD_LINK>`

**Complete Dataset**

`<FULL_DATASET_DOWNLOAD_LINK>`

### Additional Resources

**Official Project Website**

`<PROJECT_WEBSITE_URL>`

**Label Definitions**

`palmcity/labels.py`

**Train / Validation / Test Splits**

`splits/`

Please read the **License and Terms of Use** before downloading or using PalmCity.

---

## 🚀 Getting Started

Clone the repository:

```bash
git clone <PALMCITY_GITHUB_REPOSITORY>
cd PalmCity
```

After downloading the dataset, define the PalmCity root directory:

```text
PALMCITY_ROOT=/path/to/PalmCity
```

A typical training configuration can then reference:

```text
images/train/
annotations/train/

images/val/
annotations/val/
```

PalmCity can be integrated into common semantic segmentation frameworks such as:

**PaddleSeg • MMSegmentation • PyTorch • TensorFlow**

Example configuration files and data loaders will be provided in this repository.

---

## 🧠 Benchmark

PalmCity is intended to serve not only as a dataset but also as a benchmark for urban semantic segmentation.

The benchmark evaluates representative CNN- and Transformer-based semantic segmentation architectures.

| Model | Backbone | mIoU | mAcc | OA |
|---|---|---:|---:|---:|
| FCN | `{backbone}` | `{score}` | `{score}` | `{score}` |
| PSPNet | `{backbone}` | `{score}` | `{score}` | `{score}` |
| DeepLabV3+ | `{backbone}` | `{score}` | `{score}` | `{score}` |
| SegFormer | MiT-B3 | `{score}` | `{score}` | `{score}` |
| `{Model}` | `{backbone}` | `{score}` | `{score}` | `{score}` |

Detailed benchmark configurations and pretrained models will be released under:

```text
configs/
checkpoints/
benchmark/
```

---

## 🌍 Why PalmCity?

Computer vision datasets inevitably reflect the environments in which they were collected.

Urban segmentation benchmarks developed primarily from European, North American, or other highly represented environments may not sufficiently capture the visual characteristics of cities with different architectural styles, street layouts, vegetation patterns, infrastructure, transportation behaviour, and urban morphology.

PalmCity provides a geographically distinct benchmark for studying this problem.

The dataset therefore enables researchers to investigate:

**Cross-city generalization**

Cityscapes → PalmCity

**Cross-domain robustness**

Models trained on conventional street-scene datasets → panoramic Turkish urban scenes

**Dataset-specific training**

PalmCity → PalmCity

**Multi-dataset learning**

PalmCity + Cityscapes + other urban segmentation datasets

---

## 🔬 Research

The PalmCity project was introduced in:

**PalmCity: An Emerging Benchmark Dataset for Semantic Segmentation of Panoramic Street View Images in Under-Represented Developing Countries**

M. C. Iban, O. C. Bayrak, S. Kartal, D. Ilmak, and D. Z. Seker

*Computational Science and Its Applications – ICCSA 2025 Workshops, Lecture Notes in Computer Science.*

DOI:

`10.1007/978-3-031-97663-6_14`

---

## 📝 Citation

If you use PalmCity in your research, please cite:

```bibtex
@inproceedings{palmcity2026,
  title     = {PalmCity: An Emerging Benchmark Dataset for Semantic Segmentation
               of Panoramic Street View Images in Under-Represented
               Developing Countries},
  author    = {Iban, Muzaffer Can and
               Bayrak, Onur Can and
               Kartal, Serkan and
               Ilmak, Dogu and
               Seker, Dursun Zafer},
  booktitle = {Computational Science and Its Applications -- ICCSA 2025 Workshops},
  series    = {Lecture Notes in Computer Science},
  volume    = {15899},
  pages     = {165--175},
  publisher = {Springer},
  year      = {2026},
  doi       = {10.1007/978-3-031-97663-6_14}
}
```

---



---

## 📜 License

PalmCity is released for research and academic use according to the terms described in:

`LICENSE.md`

Users must review and accept the dataset license before redistribution or commercial use.

Please note that the license governing the **dataset** and the license governing the **source code / utilities** may be different.

---

## 🤝 Contributing

We welcome reports regarding:

- Incorrect annotations
- Dataset loading problems
- Evaluation issues
- Documentation
- Benchmark reproduction
- New framework integrations

Please use the GitHub **Issues** section for technical questions and bug reports.

---

## 📬 Contact

For questions related to PalmCity, dataset access, licensing, or research collaboration:

**PalmCity Research Team**

Project Website:  
[`PalmCity Website`](https://palmcity-dataset.com/)

Dataset Repository:  
`<GITHUB_REPOSITORY_URL>`

Contact:  
`<OFFICIAL_PROJECT_EMAIL>`

---

<div align="center">

### 🌴 PalmCity

**Understanding cities beyond conventional benchmarks.**

Panoramic Street View Imagery · Semantic Segmentation · GeoAI · Urban Analytics

</div>
