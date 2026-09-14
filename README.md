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

## 📊 Dataset at a Glance

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
| 0 | `{class_0}` | `{category}` | 🟪 |
| 1 | `{class_1}` | `{category}` | 🟦 |
| 2 | `{class_2}` | `{category}` | 🟩 |
| ... | ... | ... | ... |
| 31 | `{class_31}` | `{category}` | 🟥 |

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
[`<PROJECT_WEBSITE_URL>`](https://palmcity-dataset.com/)

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
