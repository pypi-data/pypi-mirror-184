import click

from . import __version__
from scribe_updater.updater import Updater
from scribe_updater.utils import make_lower, load_json
@click.command()
@click.version_option(version=__version__)
@click.option("-t", "--target", help="financial instutions ground truth", required=True)
@click.option("-g", "--ground", help="master ground truth", required=True)
@click.option("-v", "--variables", help="path for the variables csv", required=False)
@click.option("-o", "--output", help="output path for the result", required=True)
@click.option("-m", "--mappings", help="version mappings json file for finie versions", required=False)
@click.option("-a", "--authtype", help="select pba or vba, default is pba", required=False)
def main(target, ground, output, mappings={}, variables={}, authtype="pba"):
    """A tool to update scribe competency configurations."""
    
    target = make_lower(load_json(target))
    ground = make_lower(load_json(ground))
    
    version_map = load_json(mappings) if mappings else {}
    
    updater = Updater(ground, target, variables, output, version_map)
    
    updater.prep_output_pba() if authtype == "pba" else updater.prep_output_vba
    updater.update()
    updater.output_to_json()
    updater.get_change_log()
    