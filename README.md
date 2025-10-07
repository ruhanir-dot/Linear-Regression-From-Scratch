# Linear Regression From Scratch
This project implements linear regression (gradient descent) from scratch in Python and includes a short LaTeX writeup.
<img width="534" height="415" alt="image" src="https://github.com/user-attachments/assets/1a908826-4b39-4cce-a22e-562becf4040e" />


### Files
- `linear_regression.py` - Python script that reads `Lungs.csv`, runs gradient descent to fit a linear model, and plots the result.
- `Lungs.csv` - Dataset (age vs FEV) used by the script.
- `linear_regression.tex` - LaTeX writeup describing the approach.

### Requirements
- Python 3.8+ (or 3.x)
- pip packages: pandas, matplotlib
- (Optional) A LaTeX distribution (MiKTeX or TeX Live) to build the PDF from `linear_regression.tex`.

### Install dependencies (PowerShell)

```powershell
python -m pip install --upgrade pip
python -m pip install pandas matplotlib
```

### Run the script (recommended)

The script expects `Lungs.csv` to be next to `linear_regression.py`. The easiest way to run is from the project folder so relative paths resolve correctly:

```powershell
# from the project folder
python .\linear_regression.py
```

If you run the script from another folder, it may not find `Lungs.csv`. To be robust, edit `linear_regression.py` to read the CSV relative to the script file using pathlib (example included below).

### Robust CSV loading (optional change)

Replace the top of `linear_regression.py` with:

```python
from pathlib import Path
HERE = Path(__file__).resolve().parent
CSV_PATH = HERE / 'Lungs.csv'
print('Reading:', CSV_PATH)
import pandas as pd
data = pd.read_csv(CSV_PATH)
```

### Building the LaTeX writeup (optional)

If you have a LaTeX distribution installed (MiKTeX or TeX Live), you can generate a PDF from `linear_regression.tex`.

PowerShell example using pdflatex:

```powershell
cd path\to\project
pdflatex -interaction=nonstopmode linear_regression.tex
```

For repeated builds and automatic multiple passes, `latexmk` is recommended:

```powershell
latexmk -pdf linear_regression.tex
```

Troubleshooting
- If the Python script reports "file not found" for `Lungs.csv`, confirm your current working directory and run from the project folder, or use the robust CSV loading code above.
- If matplotlib plots do not show, ensure your environment supports GUI windows or save the plot to file using `plt.savefig('output.png')`.
- If LaTeX fails to build, check the `.log` file for missing packages or syntax errors.

License
MIT



