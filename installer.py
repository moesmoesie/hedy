import PyInstaller.__main__

PyInstaller.__main__.run([
    'runhedy.py',
    '--onefile',
    '--add-data',
    'grammars-Total:grammars-Total',
    '--add-data',
    'grammars:grammars'
])
