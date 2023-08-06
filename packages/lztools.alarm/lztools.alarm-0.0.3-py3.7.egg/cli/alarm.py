from subprocess import call

import click
import sh

from lztools.utils.alarm import run_timer, to_timespan

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
gnome_terminal = sh.gnome_terminal.bake()

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("time")
@click.option("-h", "--hide-window", is_flag=True, default=False)
def main(time, hide_window):
    """Template bash command by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙"""
    if not hide_window:
        print("window")
        gnome_terminal("--hide-menubar", "--geometry=40x8", "--", "alarm", time, "-h")
    else:
        run_timer(to_timespan(time))
