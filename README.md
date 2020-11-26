# Inferfuzzy

**Inferfuzzy** is a **Python** library to implement **Fuzzy Inference Systems**.

## Getting started

### Installation

```bash
pip install inferfuzzy
```

### Usage

Creating linguistic variables and their associated fuzzy sets.

```python
variable_1 = Var("variable_name_1")
variable_1 += "set_name_1", ZMembership(1, 2)
variable_1 += "set_name_2", GaussianMembership(3, 2)
variable_1 += "set_name_3", SMembership(4, 6)

variable_2 = Var("variable_name_2")
variable_2 += "set_name_4", GammaMembership(70, 100)
variable_2 += "set_name_5", LambdaMembership(40, 60, 80)
variable_2 += "set_name_6", LMembership(30, 50)
```

Declaring the semantic rules and the inference method to use.

```python
mamdani = MamdaniSystem(defuzz_func=centroid_defuzzification)
mamdani += variable_1.into("set_name_1") | variable_1.into("set_name_3"), variable_2.into("set_name_5")
mamdani += variable_1.into("set_name_2"), variable_2.into("set_name_4")
```

Using fuzzy inference method for user-entered values.

```python
variable_1_val = float(input())
mamdani_result: float = mamdani.infer(variable_name_1=variable_1_val)["variable_name_2"]
```
