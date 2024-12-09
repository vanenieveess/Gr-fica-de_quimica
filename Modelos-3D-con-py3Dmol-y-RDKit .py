from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

def generate_3d_model(smiles):
    """
    Genera el modelo 3D de una molécula a partir de su notación SMILES.

    :param smiles: Notación SMILES de la molécula.
    :return: Visualización del modelo 3D interactivo.
    """
    mol = Chem.MolFromSmiles(smiles)
    mol = Chem.AddHs(mol)  
    AllChem.EmbedMolecule(mol, AllChem.ETKDG())  
    
    block = Chem.MolToMolBlock(mol)
    viewer = py3Dmol.view(width=400, height=400)
    viewer.addModel(block, 'mol')
    viewer.setStyle({'stick': {}})
    viewer.zoomTo()
    return viewer

# Lista completa de moléculas con SMILES
molecules = {
    "Agua": "O",
    "Etanol": "CCO",
    "Ciclohexano": "C1CCCCC1",
    "Ácido acético": "CC(=O)O",
    "Benceno": "C1=CC=CC=C1",
    "Metano": "C",
    "Metanol": "CO",
    "Etano": "CC",
    "Propano": "CCC",
    "Butano": "CCCC",
    "Acetona": "CC(=O)C",
    "Glicina": "C(C(=O)O)N",
    "Alanina": "CC(C(=O)O)N",
    "Fenol": "C1=CC=C(C=C1)O",
    "Tetrahidrofurano (THF)": "C1CCOC1",
    "Etanolamina": "NCCO",
    "Ácido aspártico": "C(C(=O)O)(N)C(=O)O",
    "Trietilamina": "CCN(CC)CC",
    "Dietil éter": "CCOCC",
    "Ácido láctico": "C(C(=O)O)O",
    "Naftaleno": "C1=CC=CC2=CC=CC=C12",
    "Dimetilformamida (DMF)": "CN(C)C=O",
    "Ácido cítrico": "C(C(=O)O)C(C(=O)O)O"
}

def display_molecules():
    for name, smiles in molecules.items():
        print(f"Modelo 3D de: {name}")
        viewer = generate_3d_model(smiles)
        viewer.show()
