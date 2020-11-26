# Inferfuzzy

> **Autor:** [Leynier Gutiérrez González](https://leynier.github.io)

**Inferfuzzy** es una biblioteca de **Python** para implementar **Sistemas de Inferencia Difusa**.

## Empezando

### Instalación

```bash
pip install inferfuzzy
```

### Uso

Creación de variables lingüísticas y sus conjuntos difusos asociados.

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

Declarar las reglas semánticas y el método de inferencia a utilizar.

```python
mamdani = MamdaniSystem(defuzz_func=centroid_defuzzification)
mamdani += variable_1.into("set_name_1") | variable_1.into("set_name_3"), variable_2.into("set_name_5")
mamdani += variable_1.into("set_name_2"), variable_2.into("set_name_4")
```

Usando el método de inferencia difusa para valores ingresados por el usuario.

```python
variable_1_val = float(input())
mamdani_result: float = mamdani.infer(variable_name_1=variable_1_val)["variable_name_2"]
```
