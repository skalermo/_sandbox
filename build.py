from pathlib import Path
import platform
import subprocess

# import PyInstaller.__main__
import nuitka.__main__


if __name__ == '__main__':
    entry_point = Path(__file__).parent / 'main.py'

    with open('__init__.py') as f:
        version = f.readlines()[0].split()[2].strip("'")

    extension = {
        'Linux': 'AppImage',
        'Windows': 'exe',
    }.get(platform.system(), 'bin')
    app_name = f'app-{version}.{extension}'

    # PyInstaller.__main__.run([
    #     str(entry_point),
    #     f'--name={app_name}',
    #     '--noconfirm',
    #     '--log-level=WARN',
    #     '--onefile',
    #     '--noconsole',
    # ])
    subprocess.run([
        'python', '-m', 'nuitka',
        '--onefile',
        f'--output-filename={app_name}',
        '--disable-console',
        f'--assume-yes-for-downloads',
        str(entry_point),
    ])
