# Learning Python By Building Projects

## Project: Scientific Calculator (Terminal-Based)

This folder contains a feature-rich, terminal-based scientific calculator project built in Python. The calculator supports a wide range of mathematical operations and functions, and is designed for hands-on learning and practical use.

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

### What I Used and Learned

- **Safe evaluation:** How to use Python's `eval()` securely by restricting available functions and constants.
- **Python math module:** Using a wide range of mathematical functions and constants from the `math` module.
- **String parsing:** Building and validating mathematical expressions as strings.
- **User input handling:** Capturing and processing keyboard input in the terminal.
- **Error handling:** Managing invalid input, math errors, and edge cases gracefully.
- **ASCII art UI:** Designing a user-friendly calculator interface using print statements.
- **Modular programming:** Organizing code into clear, reusable functions.
- **Help/documentation:** Providing in-app help and usage instructions for users.
- **Project structuring:** Separating code and documentation for maintainability.

---

**Happy learning and coding!**
