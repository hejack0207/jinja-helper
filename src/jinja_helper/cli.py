from jinja2schema import infer, to_json_schema
import fire

def sample(jinjafile):
    with open(jinjafile) as f:
        lines = f.readlines()
        print(infer('\n'.join(lines)))

def schema(jinjafile):
    with open(jinjafile) as f:
        lines = f.readlines()
        sample = infer('\n'.join(lines))
        print(to_json_schema(sample))

if __name__ == '__main__':
    fire.Fire()
