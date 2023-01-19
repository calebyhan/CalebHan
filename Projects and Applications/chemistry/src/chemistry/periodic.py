import json
from pathlib import Path
import re

def name(ele):
    """
    Inputs either an atomic number or symbol to fetch atomic name.
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return data[ele - 1]["name"]
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return i["name"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def number(ele):
    """
    Inputs atomic symbol to fetch atomic number.
    """

    if type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return int(i["atomicNumber"])
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic symbol.")

def symbol(ele):
    """
    Inputs an atomic number to fetch atomic symbol.
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["atomicNumber"].lower() == ele.lower():
                return i["symbol"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number.")

def mass(ele):
    """
    Inputs either an atomic number or symbol to fetch atomic mass.
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return float(data[ele - 1]["atomicMass"].split("(")[0])
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return float(i["atomicMass"].split("(")[0])
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def elecConfig(ele):
    """
    Inputs either an atomic number or symbol to fetch electronic configuration.
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return data[ele - 1]["electronicConfiguration"]
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return i["electronicConfiguration"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def position(ele):
    """
    Inputs either an atomic number or symbol to fetch atomic position (period, group).
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return (data[ele - 1]["period"], data[ele - 1]["group"])
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return (i["period"], i["group"])
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def elecNeg(ele):
    """
    Inputs either an atomic number or symbol to fetch electron negativity.
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return data[ele - 1]["electronegativity"]
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return i["electronegativity"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def atomRadius(ele):
    """
    Inputs either an atomic number or symbol to fetch atomic radius (pm).
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return data[ele - 1]["atomicRadius"]
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return i["atomicRadius"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def ionRadius(ele):
    """
    Inputs either an atomic number or symbol to fetch ion radius (pm).
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        if data[ele - 1]["ionRadius"] == "unknown":
            return data[ele - 1]["ionRadius"]
        else:
            return int(data[ele - 1]["ionRadius"].split("(")[0])
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                if i["ionRadius"] == "unknown":
                    return i["ionRadius"]
                else:
                    return int(i["ionRadius"].split("(")[0])
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def standardState(ele):
    """
    Inputs either an atomic number or symbol to fetch state of matter at STP.
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return data[ele - 1]["standardState"]
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return i["standardState"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def ionEnergy(ele):
    """
    Inputs either an atomic number or symbol to fetch ionization energy (kJ/mol).
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return data[ele - 1]["ionizationEnergy"]
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return i["ionizationEnergy"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def elecAffinity(ele):
    """
    Inputs either an atomic number or symbol to fetch electron affinity (kJ/mol).
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return data[ele - 1]["electronAffinity"]
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return i["electronAffinity"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def meltingPoint(ele):
    """
    Inputs either an atomic number or symbol to fetch melting point (K).
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return data[ele - 1]["meltingPoint"]
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return i["meltingPoint"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def boilingPoint(ele):
    """
    Inputs either an atomic number or symbol to fetch boiling point (K).
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return data[ele - 1]["boilingPoint"]
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return i["boilingPoint"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def block(ele):
    """
    Inputs either an atomic number or symbol to fetch the block.
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return data[ele - 1]["block"]
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return i["block"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def year(ele):
    """
    Inputs either an atomic number or symbol to fetch the year discovered.
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return data[ele - 1]["yearDiscovered"]
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return i["yearDiscovered"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def groupBlock(ele):
    """
    Inputs either an atomic number or symbol to fetch the type of element by group.
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return data[ele - 1]["groupBlock"]
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return i["groupBlock"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def oxidationStates(ele):
    """
    Inputs either an atomic number or symbol to fetch the type of element by group.
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        if data[ele - 1]["oxidationStates"] == "unknown":
            return data[ele - 1]["oxidationStates"]
        else:
            return list(map(int, data[ele - 1]["oxidationStates"].split(", ")))
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                if i["groupBlock"] == "unknown":
                    return i["oxidationStates"]
                else:
                    return list(map(int, i["oxidationStates"].split(", ")))
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def molar_mass(molecule):
    """
    Inputs a molecule in type string and returns molar mass of that molecule.
    """

    atoms = []
    current_atom = ""
    current_sub = ""
    for i in range(len(molecule)):
        try:
            int(molecule[i])
            if current_atom != "":
                atoms.append(current_atom)
                current_atom = ""
            current_sub += str(molecule[i])
            if len(molecule) - 1 != i:
                try:
                    int(molecule[i + 1])
                    pass
                except:
                    atoms.append(current_sub)
                    current_sub = ""
        except:
            try:
                str(molecule[i])
                if molecule[i].isupper() == True and current_atom == "":
                    current_atom += molecule[i]
                elif molecule[i].islower() == True:
                    current_atom += molecule[i]
                elif molecule[i].isupper() == True and current_atom != "":
                    atoms.append(current_atom)
                    current_atom = molecule[i]
            except:
                raise Exception("Invalid input. Molecule should only contain letters and numbers.")

    if current_atom != "":
        atoms.append(current_atom)
    if current_sub != "":
        atoms.append(current_sub)
    
    sum = 0
    cur_atom = ""
    for i in range(len(atoms)):
        try:
            int(atoms[i])
            sum += mass(cur_atom) * int(atoms[i])
            cur_atom = ""
        except:
            if len(atoms) - 1 != i:
                if cur_atom != "":
                    sum += mass(cur_atom)
                cur_atom = atoms[i]
            else:
                if cur_atom != "":
                    sum += mass(cur_atom)
                sum += mass(atoms[i])
    return sum