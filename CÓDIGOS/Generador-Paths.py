import os

paths =[]
for root, dirs, files in os.walk(os.path.abspath("/Users/rudiks/Desktop/AVR - penúltima")):
    for file in files:
        paths.append(os.path.join(root, file))

paths=sorted(paths, key=lambda i: str(os.path.splitext(os.path.basename(i))[0]))

def query(path):
    instruccion = f"{{" \
                  f"\\usebackgroundtemplate{{\\includegraphics[width=\\paperwidth]{{\"{path}\"}}}}\\begin{{frame}}[plain]\end{{frame}}}}"
    return instruccion

for path in paths:
    print(query(path))