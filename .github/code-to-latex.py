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

def inputFile(root, file, output):
    output.write(f"\subsection{{{file}}}\n")
    output.write(f"\lstinputlisting[language=Rust]{{{root + '/' + file}}}\n")
    
def handleDirs(dirname, output, keywords = []):
    files = getRootsAndFiles(dirname)
    for root, file in sorted(files):
        inputFile(root, file, output)

with open(mainAPI, 'w') as output: 
    handleDirs(apiDir, output)

with open(implementation, 'w') as output:
    handleDirs(implDir, output)