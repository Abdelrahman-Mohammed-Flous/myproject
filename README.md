# Numerical Methods in Python

A collection of Python programs that implement classic numerical methods from scratch. Each method is a standalone script that runs in the terminal and asks for its inputs interactively.

## Methods

| File | Method | Purpose |
|---|---|---|
| `Project_BiSection.py` | Bisection Method | Finds a root of an equation by repeatedly halving an interval that contains the root |
| `Project_Secant.py` | Secant Method | Finds a root using a secant line through two points, with no derivative needed |
| `Project_Modified_Secant.py` | Modified Secant Method | A variation of the secant method that uses a small perturbation of a single point |
| `Project_Newton_Raphson.py` | Newton-Raphson Method | Finds a root using the function and its derivative, usually converging quickly |
| `Project_Linear_Regression.py` | Linear Regression | Fits a straight line `y = a + bx` to a set of data points using least squares |

## Requirements

- Python 3.x
- No external libraries are needed for the core scripts

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/Abdelrahman-Mohammed-Flous/myproject.git
cd myproject
```

2. Run any script:

```bash
python Project_BiSection.py
```

3. Follow the prompts in the terminal. For example, Linear Regression first asks for the number of points, then the `x` and `y` values.

## Project Structure

```
myproject/
├── Project_BiSection.py
├── Project_Secant.py
├── Project_Modified_Secant.py
├── Project_Newton_Raphson.py
├── Project_Linear_Regression.py
├── .gitignore
└── README.md
```

## Author

**Abdelrahman Mohammed**
GitHub: [@Abdelrahman-Mohammed-Flous](https://github.com/Abdelrahman-Mohammed-Flous)

## Contributing

Suggestions and improvements are welcome. Feel free to open an issue or submit a pull request.