# chemistry-ch

Python library for chemistry equations and formulas.


## Installation
----------------------

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install chemistry-ch.

```bash
pip install chemistry-ch
```


## Usage
----------------------

```python
import chemistry

# returns atomic mass of Hydrogen
chemistry.mass(1)
chemistry.mass("H")

# returns a metric conversion from 1 cm to km
chemistry.Conversions.metric(1, "c", "k")

# returns molarity of a solution with 1 mol in 2 L
chemistry.Formulas(moles=1, volume=1)
```


## Documentation
----------------------


### Functions
----------------------
chemistry-ch offers 3 sub-files as well as constants:

``` python
import chemistry.Conversions
import chemistry.Formulas
import chemistry.Periodic
```


### Conversions
----------------------

``chemistry.Conversions.k_to_c(k)``

Inputs kelvin and converts to celcius.

``chemistry.Conversions.k_to_f(k)``

Inputs kelvin and converts to fahrenheit.

``chemistry.Conversions.c_to_k(c)``

Inputs celcius and converts to kelvin.

``chemistry.Conversions.c_to_f(k)``

Inputs celcius and converts to fahrenheit.

``chemistry.Conversions.f_to_k(k)``

Inputs fahrenheit and converts to kelvin.

``chemistry.Conversions.f_to_c(k)``

Inputs fahrenheit and converts to celcius.

``chemistry.Conversions.metric(num, pre1, pre2)``

Inputs a value and starting prefix and final prefix to return converted value.


### Formulas
----------------------

``chemistry.Formulas.atomicWeight(weights)``

Input 2D array of atomic weights and percentages to find overall atomic weight.

``chemistry.Formulas.molarity(molarity, moles, volume)``

Input two of molarity, moles, and volume and outputs the third.


### Periodic
----------------------

NOTE: All inputs work in element symbol or number.

``chemistry.Periodic.name(ele)``

Input element and return element name.

``chemistry.Periodic.number(ele)``

Input element and return atomic number.

``chemistry.Periodic.symbol(ele)``

Input element and return symbol.

``chemistry.Periodic.mass(ele)``

Input element and return atomic mass.

``chemistry.Periodic.elecConfig(ele)``

Input element and return electron configuration.

``chemistry.Periodic.position(ele)``

Input element and return its position in (period, group).

``chemistry.Periodic.elecNeg(ele)``

Input element and return electronegativty.

``chemistry.Periodic.atomRadius(ele)``

Input element and return atomic radius.

``chemistry.Periodic.ionRadius(ele)``

Input element and return ionic radius.

``chemistry.Periodic.standardState(ele)``

Input element and return its standard state.

``chemistry.Periodic.ionEnergy(ele)``

Input element and return ionization energy.

``chemistry.Periodic.elecAffinity(ele)``

Input element and return electron affinity.

``chemistry.Periodic.meltingPoint(ele)``

Input element and return melting point.

``chemistry.Periodic.boilingPoint(ele)``

Input element and return boiling point.

``chemistry.Periodic.block(ele)``

Input element and return block

``chemistry.Periodic.year(ele)``

Input element and return year discovered

``chemistry.Periodic.groupBlock(ele)``

Input element and return group block

``chemistry.Periodic.oxidationStates(ele)``

Input element and return possible oxidation states in a list

``chemistry.Periodic.molar_mass(molecule)``

Input molecule and return molar mass.


## Contributing
----------------------

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.


## License
----------------------

[MIT](https://choosealicense.com/licenses/mit/)
