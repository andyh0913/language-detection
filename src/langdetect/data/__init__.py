from pathlib import Path

# TODO: only load the data user want.
def loader(target_module: str=None, sub_module: str=None):
    module_root = Path(__file__).parent / target_module /  sub_module
    datapack = {}
    for dpf in module_root.glob('*.txt'): 
        # datapack file
        datapack[dpf.stem] = dpf.read_text().split('\n')
    return datapack