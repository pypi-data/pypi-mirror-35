from lztools.click import proper_command, proper_group

from lztools.ResourceManager import out_path

@proper_group()
def main():
    pass

@proper_command()
def has_output():
    print(out_path.stat().st_size > 0)