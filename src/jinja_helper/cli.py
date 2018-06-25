from jinja2schema import infer, to_json_schema
import sys
import fire
import click

def sample(jinjafile=None):
    _process(jinjafile, True)

def schema(jinjafile=None):
    _process(jinjafile, False)

def _process(jinjafile, sample_or_schema=True):
    #click.open_file(jinjafile)
    #if sys.stdin.isatty():
    if jinjafile is None:
        lines = sys.stdin.readlines()
        sample = infer('\n'.join(lines))
        if sample_or_schema is True:
            print(sample)
        else:
            print(to_json_schema(sample))
    else:
        with click.open_file(jinjafile) as f:
            lines = f.readlines()
            sample = infer('\n'.join(lines))
            if sample_or_schema is True:
                print(sample)
            else:
                print(to_json_schema(sample))


if __name__ == '__main__':
    fire.Fire()
