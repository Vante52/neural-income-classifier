# Neural Income Classifier

This project was developed as part of the Introduction to Artificial Intelligence course at Pontificia Universidad Javeriana.

The main purpose of this project is to understand how neural networks learn, how data preparation affects their training, and how different network architectures perform when solving the same classification problem.

## About the dataset

We work with the [Adult Census Income Dataset](https://archive.ics.uci.edu/dataset/2/adult) from the UCI Machine Learning Repository.

The dataset contains 48,842 records with information about people's age, education, occupation, working hours, marital status, and other characteristics.

The goal is to classify whether a person's annual income is:

- **≤ $50,000**
- **> $50,000**

## Data preparation

Before training our models, we explored the dataset to better understand the information we were working with.

We analyzed the distribution of the variables, their correlations, missing values, and outliers. Based on these observations, we prepared the data by:

- Removing redundant features.
- Handling missing values without discarding records.
- Converting categorical variables into numerical values.
- Scaling numerical variables to make their magnitudes comparable.
- Applying logarithmic transformations to capital gains and losses.

After preprocessing, we obtained 91 input features for our neural networks.

## Neural network architectures

We implemented three different architectures using Scikit-learn, starting with the simplest neural model and progressively introducing hidden layers.

### 1. Perceptron

**Architecture:** 91 → 1

The perceptron is the simplest model implemented in this project. It receives the 91 input features, multiplies them by their corresponding weights, adds a bias, and determines the output class using a step function.

During training, the perceptron adjusts its weights and bias based on its classification errors.

Since it does not contain hidden layers, it can only create a linear decision boundary. We used this model as a starting point to understand the limitations of a simple neural architecture.

- Input features: 91
- Hidden layers: 0
- Output neurons: 1
- Trainable parameters: 92

### 2. Neural network with one hidden layer

**Architecture:** 91 → 91 → 1

For our second model, we introduced a hidden layer containing the same number of neurons as the input features.

Unlike the perceptron, this network uses multiple neurons to process the input information before making a prediction. Each hidden neuron learns a different combination of the input features.

The hidden layer uses the ReLU activation function, allowing the network to learn nonlinear relationships that the simple perceptron cannot represent.

The output neuron uses a sigmoid function to determine the probability of belonging to the positive income class.

During training, the weights and biases are updated through backpropagation using the Adam optimizer.

- Input features: 91
- Hidden layers: 1
- Neurons in the hidden layer: 91
- Output neurons: 1
- Trainable parameters: 8,464

This architecture allows us to explore how increasing the number of neurons affects the learning capacity and classification performance of the model.

### 3. Neural network with two hidden layers

**Architecture:** 91 → 2 → 2 → 1

Our third model introduces an additional hidden layer but significantly reduces the number of neurons in each layer.

The first hidden layer receives the 91 input features and transforms them into two intermediate values. These values are then processed by the second hidden layer before reaching the output neuron.

Like the previous model, it uses ReLU in its hidden layers, a sigmoid output function, and the Adam optimizer.

- Input features: 91
- Hidden layers: 2
- Neurons per hidden layer: 2
- Output neurons: 1
- Trainable parameters: 193

What makes this architecture interesting is that it is deeper than the previous network but contains considerably fewer parameters. We wanted to understand whether a smaller network could achieve similar results while learning a more compact representation of the data.

## Training and evaluation

Each architecture was trained using three different train-test splits:

| Experiment | Training | Testing |
|---|---:|---:|
| 1 | 70% | 30% |
| 2 | 80% | 20% |
| 3 | 90% | 10% |

This gave us nine training configurations and allowed us to compare how the architecture and the amount of available training data affect the results.

We evaluated each model using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrices

Since most people in the dataset belong to the same income class, we paid special attention to precision, recall, and F1-score rather than relying only on accuracy.

## Results

The following results correspond to the 90/10 train-test split.

| Model | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Perceptron | 76.01% | 49.91% | 72.97% | 59.28% |
| One hidden layer | 85.57% | 72.14% | 64.67% | **68.20%** |
| Two hidden layers | 85.57% | 74.58% | 60.22% | 66.64% |

One of the most interesting results was how close the performance of the two multilayer networks was, despite their differences in size.

| Model | Trainable parameters |
|---|---:|
| Perceptron | 92 |
| One hidden layer | 8,464 |
| Two hidden layers | 193 |

The network with two hidden layers achieved a similar performance while using approximately 97.7% fewer parameters than the network with one hidden layer.

This helped us understand that a larger or deeper neural network does not necessarily guarantee better results.

## Project structure

- `data/raw/` — Original Adult dataset files.
- `src/` — Dataset loading functions.
- `notebooks/01_data_exploration.ipynb` — Understanding and exploring the dataset.
- `notebooks/02_neural_networks.ipynb` — Data preprocessing, neural network training, and performance comparison.

Each notebook includes visualizations and short explanations of our observations and their relevance to the project.

## Getting started

Create a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Make sure `adult.data` and `adult.test` are available inside `data/raw/`.

Open the project in VS Code, select the virtual environment as your Jupyter kernel, and run the notebooks in order.

## Tools

- Python
- Scikit-learn
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Plotly
- Jupyter Notebook
- Visual Studio Code

## What we learned

This project helped us go from understanding the basic concept of a perceptron to working with multilayer neural networks.

More importantly, we learned that training a neural network is not only about choosing an architecture. Understanding the data, preparing the inputs, and interpreting the results are equally important parts of the process.

---

Pontificia Universidad Javeriana

Introduction to Artificial Intelligence — 2026