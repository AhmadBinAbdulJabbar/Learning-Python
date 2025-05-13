# Learning Python By Building Projects

## Project: Scientific Calculator (Terminal-Based)

This repository contains a collection of Python projects for learning and practice. The main highlight is a robust, terminal-based scientific calculator that supports a wide range of mathematical operations and functions.

### Features

- Basic arithmetic: `+`, `-`, `*`, `/`, `%`
- Parentheses for grouping
- Decimal numbers
- Scientific functions: `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `sinh`, `cosh`, `tanh`, `asinh`, `acosh`, `atanh`, `sqrt`, `log`, `log10`, `log2`, `exp`, `pow`, `fabs`, `floor`, `ceil`, `modf`, `gcd`, `lcm`, `comb`, `perm`, `factorial`, `radians`, `degrees`
- Mathematical constants: `pi`, `e`, `tau`
- Safe evaluation: Only math functions/constants are allowed (no arbitrary code execution)
- Error handling for invalid input, math errors, and division by zero
- ASCII-art calculator UI with help and usage tips
- [H] Help key: Shows function descriptions and usage examples
- [C] Clear, [A] Exit, [H] Help keys

### How to Use

1. Run the calculator script in your terminal (see `1.calculator/scientific_calculator.py`).
2. Enter expressions using numbers, operators, and supported function names (e.g., `sin(3.14/2)`, `sqrt(16)`, `2*pi`).
3. Use `*` for multiplication (e.g., `2*pi`, not `2pi`).
4. Press `[H]` for help, `[C]` to clear, `[A]` to exit.
5. See the on-screen help for a full list of functions and usage examples.

### Example Expressions

- `sin(radians(90))`
- `sqrt(25) + log10(100)`
- `pow(2, 8) - factorial(5)`
- `gcd(12, 18)`
- `comb(5, 2)`
- `2*pi + e`

### Requirements

- Python 3.6+
- No external dependencies for basic/scientific calculator
- For advanced features (like integration), see project notes

### Project Structure

- `1.calculator/` — Calculator scripts (scientific and simple)
- `README.md` — This file

---

**Happy learning and coding!**
