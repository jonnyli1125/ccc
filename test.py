import argparse
import glob
import importlib.util

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('year')
    parser.add_argument('problem')
    args = parser.parse_args()

    spec = importlib.util.spec_from_file_location(args.problem,
        f'{args.year}/{args.problem}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    in_fnames = glob.glob(f'{args.year}/data/{args.problem}/*.in')
    n_correct = 0
    for in_fname in in_fnames:
        out_fname = in_fname.replace('.in', '.out')
        with open(in_fname, 'r') as f:
            in_lines = [l.strip() for l in f]
        with open(out_fname, 'r') as f:
            exp_out_lines = [l.strip() for l in f]
        act_out_lines = [str(module.solution(in_lines))]
        if act_out_lines == exp_out_lines:
            n_correct += 1
            print(f'{in_fname}: passed')
        else:
            print(f'{in_fname}: failed')
    print(f'Total: {n_correct}/{len(in_fnames)} correct')

if __name__ == '__main__':
    main()
