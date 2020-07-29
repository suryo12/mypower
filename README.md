# myPower
Supplementary function and port of [MATPOWER](https://github.com/MATPOWER/matpower) in Python. myPower stands for Matlab Python Ported MATPOWER.

## mypower/
Containing original myPower function.

## mypower/matpower_ported
Containing callable ported MATPOWER function .

# Requirements
## Octave (Tutorial for Windows 10)
1. Download [octave](https://www.gnu.org/software/octave/download.html) zip.
2. Add new Environment Variable.

```
Variable name: OCTAVE_EXECUTABLE
Variable value: location:\\of\\octave\\bin\\octave-cli.exe
```

3. Restart computer to make 'os.environ' recognize the new path.
4. To test, open Command Prompt, run python, import oct2py.

```
python
import oct2py
```

## Library
myPower needs [numpy](https://github.com/numpy/numpy) and [oct2py](https://github.com/blink1073/oct2py) to be used.
```
pip install numpy oct2py
```
# Notable of functions
1. losses_kron: Compute losses based on Kron's coefficient
2. makeB_kron: Make B based on Kron's method
3. to_mypc: Revert mypc indexing to start from 1 for octave compatibility
4. to_mypc0: Fix mypc bus indexing to start from 0 for Pyhton compatibility

# Authors
* **Muhammad Yasirroni** - [yasirroni](https://github.com/yasirroni)

See also the list of [contributors](https://github.com/yasirroni/myPower/graphs/contributors) who participated in this project.

Feel free if you want to contribute.