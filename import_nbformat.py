import nbformat

# Cambia 'tu_cuaderno.ipynb' por el nombre de tu archivo
with open('t_student_simulacion.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Elimina los metadatos de widgets que causan el error
if 'widgets' in nb.metadata:
    del nb.metadata['widgets']

with open('t_student_simulacion_corregido.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
