# MediDiagEval: Medical Diagnosis Evaluation Benchmark

## Overview

MediDiagEval stands as a pioneering benchmark dataset focused on evaluating the diagnostic capabilities of language models within the medical domain. This benchmark is designed to bridge the gap in the availability of large-scale, reliable datasets that map patient histories to diagnoses. By leveraging advanced NLP techniques, including GPT-4 annotations and BioGPT embeddings, MediDiagEval enhances the reliability and consistency of the mapped data. The primary goal is to provide a robust framework for assessing the performance of medical vertical language models in accurately diagnosing based on unstructured medical text.

Patient history data is from [PMC-Patients](https://github.com/zhao-zy15/PMC-Patients). PMC-Patients is a first-of-its-kind dataset consisting of 167k patient summaries extracted from case reports in PubMed Central (PMC).

Model used to generate embedding is [BioGPT](https://github.com/microsoft/BioGPT). Their paper: [BioGPT: generative pre-trained transformer for biomedical text generation and mining ](https://academic.oup.com/bib/article/23/6/bbac409/6713511?guestAccessKey=a66d9b5d-4f83-4017-bb52-405815c907b9&login=false)

## Key Features

- **Comprehensive Evaluation Dataset**: Offers a structured dataset for evaluating the diagnostic accuracy of language models in the medical field.
- **Advanced NLP Techniques**: Utilizes GPT-4 for precise text annotation and BioGPT for semantic embedding generation, ensuring high data fidelity.
- **ICD-10 Code Matching**: Incorporates embedding-based matching with ICD-10 codes to validate and enhance the dataset's reliability.
- **Open Framework for Benchmarking**: Provides a standardized method for benchmarking language models, facilitating advancements in medical NLP.

## Project Components

The project consists of several scripts, each fulfilling a specific role in the data preparation and evaluation pipeline:

1. **GPT Annotation (`sample_and_prompt.py` `gptAnnotate.py` `ExtractGptLabels.py` )**: Applies GPT-4 to annotate diagnosis and extract labels with code

2. **BioGPT Embedding Generation (`BioGptEmbedding.py`)**: Produces semantic embeddings for given text list using BioGPT.

3. **ICD-10 Embedding Generation (`get_icd10_embedding.py`)**: Produces semantic embeddings for ICD-10 descriptions.

4. **ICD-10 Embedding Matching (`MostLikelyICD10.py`)**: Matches patient diagnosis embeddings with ICD-10 codes based on similarity metrics.

## Prerequisites

- see requirements.txt

## Setup and Installation

1. Clone the repository to get started:

```bash
git clone https://github.com/jabberwockyang/MediDiagEval.git
cd MediDiagEval
```

2. Install necessary dependencies:

```bash
pip install -r requirements.txt
```

## Usage Guide

1. Prepare your dataset as per the guidelines mentioned in `sample_and_prompt.py`.

2. Execute `sample_and_prompt.py` to generate GPT-4 prompts for annotation:

```bash
python sample_and_prompt.py
```

3. Annotate the prompts and extract labels by running `gptAnnotate.py` and `ExtractGptLabels.py`:

```bash
python gptAnnotate.py
```

```bash
python ExtractGptLabels.py
```

4. Generate embeddings for ICD-10 codes using `get_icd10_embedding.py`:

```bash
python get_icd10_embedding.py
```

5. Perform embedding matching with ICD-10 codes through `MostLikelyICD10.py`:

```bash
python MostLikelyICD10.py
```

## Contributing

We welcome contributions to the MediDiagEval project. To contribute, please fork the repository, make your changes, and submit a pull request.


---

Afterall, this README as well as the project name are written by GPT4 😝