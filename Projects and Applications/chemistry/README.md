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
import chemistry.conversions
import chemistry.formulas
import chemistry.periodic
```


### Conversions
----------------------

``chemistry.conversions.k_to_c(k)``

Inputs kelvin and converts to celcius.

``chemistry.conversions.k_to_f(k)``

Inputs kelvin and converts to fahrenheit.

``chemistry.conversions.c_to_k(c)``

Inputs celcius and converts to kelvin.

``chemistry.conversions.c_to_f(k)``

Inputs celcius and converts to fahrenheit.

``chemistry.conversions.f_to_k(k)``

Inputs fahrenheit and converts to kelvin.

``chemistry.conversions.f_to_c(k)``

Inputs fahrenheit and converts to celcius.

``chemistry.conversions.metric(num, pre1, pre2)``

Inputs a value and starting prefix and final prefix to return converted value.


### Formulas
----------------------

``chemistry.forumulas.atomicWeight(weights)``

Input 2D array of atomic weights and percentages to find overall atomic weight.

``chemistry.forumulas.molarity(molarity, moles, volume)``

Input two of molarity, moles, and volume and outputs the third.


### Periodic
----------------------

NOTE: All inputs work in element symbol or number.

``chemistry.periodic.name(ele)``

Input element and return element name.

``chemistry.periodic.number(ele)``

Input element and return atomic number.

``chemistry.periodic.symbol(ele)``

Input element and return symbol.

``chemistry.periodic.mass(ele)``

Input element and return atomic mass.

``chemistry.periodic.elecConfig(ele)``

Input element and return electron configuration.

``chemistry.periodic.position(ele)``

Input element and return its position in (period, group).

``chemistry.periodic.elecNeg(ele)``

Input element and return electronegativty.

``chemistry.periodic.atomRadius(ele)``

Input element and return atomic radius.

``chemistry.periodic.ionRadius(ele)``

Input element and return ionic radius.

``chemistry.periodic.standardState(ele)``

Input element and return its standard state.

``chemistry.periodic.ionEnergy(ele)``

Input element and return ionization energy.

``chemistry.periodic.elecAffinity(ele)``

Input element and return electron affinity.

``chemistry.periodic.meltingPoint(ele)``

Input element and return melting point.

``chemistry.periodic.boilingPoint(ele)``

Input element and return boiling point.

``chemistry.periodic.block(ele)``

Input element and return block

``chemistry.periodic.year(ele)``

Input element and return year discovered

``chemistry.periodic.groupBlock(ele)``

Input element and return group block

``chemistry.periodic.oxidationStates(ele)``

Input element and return possible oxidation states in a list

``chemistry.periodic.molar_mass(molecule)``
Input molecule and return molar mass.


## Contributing
----------------------

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.


## License
----------------------

[MIT](https://choosealicense.com/licenses/mit/)
