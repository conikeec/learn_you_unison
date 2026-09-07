#!/usr/bin/env python3
"""Check the Git/TypeScript and UCM walkthroughs in temporary workspaces."""
import argparse
import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FLAGS = ['--strict', '--noEmitOnError', '--target', 'ES2022', '--module', 'commonjs', '--outDir', 'dist']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tsc', default='tsc', help='TypeScript compiler executable; use 5.9.3 to match the guide')
    args = parser.parse_args()
    compiler = shutil.which(args.tsc)
    if not compiler:
        parser.error('Install TypeScript 5.9.3 and pass its tsc executable with --tsc')
    compiler = str(Path(compiler).resolve())
    evidence = ROOT / '.validation'
    evidence.mkdir(exist_ok=True)
    log = []

    def run(command, cwd, expected=0, stdin=None):
        result = subprocess.run(command, cwd=cwd, capture_output=True, text=True, input=stdin, timeout=120, env={k: v for k, v in os.environ.items() if k != "FORCE_COLOR"})
        log.append('$ ' + ' '.join(map(str, command)) + '\n' + result.stdout + result.stderr)
        if (expected == 0 and result.returncode != 0) or (expected != 0 and result.returncode == 0):
            raise RuntimeError(log[-1])
        return result.stdout

    results = []
    try:
        with tempfile.TemporaryDirectory(prefix='learn-you-unison-orientation-') as directory:
            work = Path(directory)
            project = work / 'star-game-ts'
            (project / 'src').mkdir(parents=True)
            guide = (ROOT / 'docs/01-code-that-knows-its-own-name.md').read_text()
            blocks = re.findall(r'```typescript\n(.*?)```', guide, re.S)
            if len(blocks) != 5:
                raise RuntimeError('Expected five TypeScript example blocks; review the walkthrough checker when changing them')
            paths = ['src/rewards.ts', 'src/celebrate.ts', 'src/main.ts']
            for name, code in zip(paths, blocks):
                (project / name).write_text(code)
            (project / '.gitignore').write_text('dist/\nnode_modules/\n')
            run(['git', 'init', '-b', 'main'], project)
            run(['git', 'config', 'user.name', 'Orientation Test'], project)
            run(['git', 'config', 'user.email', 'orientation@example.invalid'], project)
            run([compiler, *FLAGS, *paths], project)
            assert run(['node', 'dist/main.js'], project).strip() == '12'
            run(['git', 'add', '.gitignore', 'src'], project)
            run(['git', 'commit', '-m', 'Give a player two stars'], project)
            remote = work / 'remote.git'
            run(['git', 'init', '--bare', str(remote)], work)
            run(['git', 'remote', 'add', 'origin', str(remote)], project)
            run(['git', 'push', '-u', 'origin', 'main'], project)
            teammate = work / 'teammate-game'
            run(['git', 'clone', '--branch', 'main', str(remote), str(teammate)], work)
            run([compiler, *FLAGS, *paths], teammate)
            assert run(['node', 'dist/main.js'], teammate).strip() == '12'
            results.append('TypeScript build prints 12 in original and cloned Git repositories')
            run(['git', 'switch', '-c', 'rename-reward'], project)
            (project / paths[0]).write_text(blocks[3])
            failure = run([compiler, *FLAGS, *paths], project, expected=1)
            assert "has no exported member 'addStar'" in failure
            (project / paths[1]).write_text(blocks[4])
            run([compiler, *FLAGS, *paths], project)
            assert run(['node', 'dist/main.js'], project).strip() == '12'
            run(['git', 'add', *paths[:2]], project)
            run(['git', 'commit', '-m', 'Rename the reward and update its caller'], project)
            run(['git', 'switch', 'main'], project)
            run(['git', 'merge', 'rename-reward'], project)
            run(['git', 'push'], project)
            run(['git', 'pull', '--ff-only'], teammate)
            run([compiler, *FLAGS, *paths], teammate)
            assert run(['node', 'dist/main.js'], teammate).strip() == '12'
            results.append('Partial rename fails with missing export; repaired rename builds and propagates through Git')

            transcript = work / 'orientation.md'
            transcript.write_text((ROOT / 'examples/checks/orientation.md').read_text())
            codebase = work / 'codebase'
            run(['ucm', 'transcript', '-S', str(codebase), str(transcript)], work)
            rendered = transcript.with_suffix('.output.md').read_text()
            (evidence / 'orientation.output.md').write_text(rendered)
            assert 'celebrate score = giveStar (giveStar score)' in rendered
            for branch, expected in [('main', '12'), ('bonus', '14'), ('merge-check', '14')]:
                output = run(['ucm', '-c', str(codebase), '-p', f'star-game/{branch}', '--no-file-watch'], work, stdin='run main\nquit\n')
                clean = re.sub(r'\x1b\[[0-?]*[ -/]*[@-~]', '', output)
                clean = clean.replace('\x01', '').replace('\x02', '')
                assert re.search(r'(?m)(?:^|> )' + expected + r'\s*$', clean), (branch, clean)
            results.append('UCM load/update/run, stored rename, regenerated source, branch isolation, and merge pass')
            results.append('Fresh UCM processes print main=12, bonus=14, merge-check=14 from the saved codebase')
        report = {
            'verified_on': '2026-09-06',
            'typescript': subprocess.check_output([compiler, '--version'], text=True).strip(),
            'node': subprocess.check_output(['node', '--version'], text=True).strip(),
            'ucm': subprocess.check_output(['ucm', '--version'], text=True).strip(),
            'passed': True, 'checks': results,
            'limits': 'Git remote was a local bare repository; base fetched from Share; no Cloud deployment or remote compute executed.'
        }
        (evidence / 'orientation-results.json').write_text(json.dumps(report, indent=2) + '\n')
        for result in results:
            print('PASS', result)
    finally:
        (evidence / 'orientation-check.log').write_text('\n'.join(log))


if __name__ == '__main__':
    main()
