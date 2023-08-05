import click
from src.cli import pass_context
from src.abs.game import Game


@click.command('generate', short_help='Show a view of 9*9 sudoku map')
@click.option('--coordinate/--no-coordinate', default=True)
@click.option('--check/--no-check', default=True)
@click.option('--mode', type=click.Choice(['easy', 'medium', 'hard', 'extreme']), default='medium')
@pass_context
def cli(ctx, coordinate, check, mode):
    game = Game(
        with_coordinate=coordinate, step_check=check, mode=mode,
        random=6, mutiple=18, lmutiple=8)
    game.fill_random()
    game.flush()
    game.gloop()
