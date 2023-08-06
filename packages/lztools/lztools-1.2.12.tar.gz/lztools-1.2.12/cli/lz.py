#!/usr/bin/env python3

import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

colorizations = ['none', 'rainbow', 'altbow', 'metal']

@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    """A collection of python tools and bash commands by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙"""
