import os

# Where to output the LaTeX.
mainAPI = "software/code/api.tex"
implementation = "software/code/implementation.tex"

# Where to look for the files.
apiDir = "software/code/files/api"
implDir = "software/code/files/impl"

def getRootsAndFiles(dirname):
    rootsAndFiles = []
    for root, _, files in os.walk(dirname):
        for file in files:
            rootsAndFiles.append((root, file))
    return rootsAndFiles

# Rust uses multiple mod.rs files which can be confusing to differentiate
# Add the name of the folder in which the file is in
def disimbiguate_file(root: str, file):
    if "mod.rs" in file or "main.rs" in file:
        last_root = root.rfind("/")
        file = root[last_root + 1:] + "/" + file

    return file

def inputFile(root, file, output):
    fixed_file = disimbiguate_file(root, file)
    # use escape sequence to avoid subscripting with _
    fixed_file = file.replace("_", "\\_")
    output.write(f"\\subsection{{{fixed_file}}}\n")
    output.write(f"\\lstinputlisting[language=Rust]{{{root + '/' + file}}}\n")
    
def handleDirs(dirname, output):
    files = getRootsAndFiles(dirname)
    for root, file in sorted(files):
        inputFile(root, file, output)

with open(mainAPI, 'w') as output: 
    handleDirs(apiDir, output)

with open(implementation, 'w') as output:
    handleDirs(implDir, output)