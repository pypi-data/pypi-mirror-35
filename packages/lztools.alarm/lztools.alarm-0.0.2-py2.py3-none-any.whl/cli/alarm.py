import datetime
import os
import shutil
import time
from time import sleep
import click
import sh
from lztools.dating import hours_minutes_seconds

clear = lambda: os.system('clear')
figlet = sh.figlet.bake()

def to_timespan(time_str:str):
    tt, tf = time_str[:-1], time_str[-1]
    format = tt.isdigit() and tf.isalpha()
    if time_str.isdigit():
        return datetime.timedelta(minutes=int(time_str))
    elif ":" in time_str:
        h, m = time_str.split(":")
        h, m = int(h), int(m)
        n = datetime.datetime.now()
        t = n.replace(hour=h, minute=m)
        if t < n:
            t = t.replace(day=t.day+1)
        return t - datetime.datetime.now()
    elif tf == "m" and format:
        return datetime.timedelta(minutes=int(tt))
    elif tf == "s" and format:
        return datetime.timedelta(seconds=int(tt))
    elif tf == "h" and format:
        return datetime.timedelta(hours=int(tt))
    elif tf == "d" and format:
        return datetime.timedelta(days=int(tt))
    else:
        raise Exception("Unable to parse time argument")

@click.command()
@click.argument("time")
def main(time):
    """Template bash command by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙"""
    run_timer(to_timespan(time))

def beep(length, duration=0.4, freq=440):
    while length > 0:
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
        time.sleep(duration)
        length -= duration * 2

def run_timer(time:datetime.timedelta):
    end = datetime.datetime.now() + time
    while end > datetime.datetime.now():
        l = end - datetime.datetime.now()
        h, m, s = hours_minutes_seconds(l)
        clear()
        e = ""
        if l.days > 0:
            e = f"{e}{l.days} Days and "
        if h > 1:
            e = f"{e}{h:02}:"
        print(figlet(f"{e}{m:02}:{s:2}", w=shutil.get_terminal_size().columns, c=True))
        sleep(0.1)
    beep(9999)
