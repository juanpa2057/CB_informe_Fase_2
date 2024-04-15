import os
from pyhtml2pdf import converter
from PyPDF2 import PdfMerger

# Lista de enlaces a los archivos HTML que deseas convertir a PDF
lista = [
         "https://juanpa2057.github.io/CB_informe_Fase_2/intro.html",
         "https://juanpa2057.github.io/CB_informe_Fase_2/Hallazgos.html",
         "https://juanpa2057.github.io/CB_informe_Fase_2/notebooks/individual/Notebook%20BC%2073%20-%20Pereira.html",
         "https://juanpa2057.github.io/CB_informe_Fase_2/notebooks/individual/Notebook%20BC%2081%20-%20Avenida%20Kennedy.html",
         "https://juanpa2057.github.io/CB_informe_Fase_2/notebooks/individual/Notebook%20BC%20111%20-%20Corozal.html",
         "https://juanpa2057.github.io/CB_informe_Fase_2/notebooks/individual/Notebook%20BC%20115%20-%20Circunvalar%20Pereira.html",
         "https://juanpa2057.github.io/CB_informe_Fase_2/notebooks/individual/Notebook%20BC%20265%20-%20Valle%20de%20Lili.html",
         "https://juanpa2057.github.io/CB_informe_Fase_2/notebooks/individual/Notebook%20BC%20332%20-%20Zipaquira.html",
         "https://juanpa2057.github.io/CB_informe_Fase_2/notebooks/individual/Notebook%20BC%20367%20-%20Granada%20Meta.html",
         "https://juanpa2057.github.io/CB_informe_Fase_2/notebooks/individual/Notebook%20BC%20384%20-%20Anapoima.html",
         "https://juanpa2057.github.io/CB_informe_Fase_2/notebooks/individual/Notebook%20BC%20388%20-%20CC%20Hayuelos.html",
         "https://juanpa2057.github.io/CB_informe_Fase_2/notebooks/individual/Notebook%20BC%20478%20-%20Mix%20V%C3%ADa%2040.html",
         "https://juanpa2057.github.io/CB_informe_Fase_2/notebooks/individual/Notebook%20BC%20513%20-%20El%20Dificil.html",
         "https://juanpa2057.github.io/CB_informe_Fase_2/notebooks/individual/Notebook%20BC%20516%20-%20Santa%20Marta.html",
         "https://juanpa2057.github.io/CB_informe_Fase_2/notebooks/individual/Notebook%20BC%20517%20-%20El%20Rodadero.html",
         "https://juanpa2057.github.io/CB_informe_Fase_2/notebooks/individual/Notebook%20BC%20554%20-%20Mall%20Plaza%20Buenavista.html",
         "https://juanpa2057.github.io/CB_informe_Fase_2/notebooks/individual/Notebook%20BC%20681%20-%20Cerete.html",
         "https://juanpa2057.github.io/CB_informe_Fase_2/notebooks/individual/Notebook%20BC%20%20687%20-%20Planeta%20Rica.html",
         "https://juanpa2057.github.io/CB_informe_Fase_2/notebooks/individual/Notebook%20BC%20689%20-%20Metropolis.html",
         "https://juanpa2057.github.io/CB_informe_Fase_2/notebooks/individual/Notebook%20BC%20733%20-%20La%20Uni%C3%B3n%20Valle.html",
         "https://juanpa2057.github.io/CB_informe_Fase_2/notebooks/individual/Notebook%20BC%20772%20-%20Caicedonia.html",
         "https://juanpa2057.github.io/CB_informe_Fase_2/notebooks/individual/Notebook%20BC%20775%20-%20Bulevar%2054.html",
         "https://juanpa2057.github.io/CB_informe_Fase_2/notebooks/individual/Notebook%20BC%20777%20-%20Parque%20Washington.html",
         "https://juanpa2057.github.io/CB_informe_Fase_2/notebooks/individual/Notebook%20BC%20781%20-%20Prado%20Plaza.html",
         "https://juanpa2057.github.io/CB_informe_Fase_2/notebooks/individual/Notebook%20BC%20802%20-%20Puerto%20Lopez.html"
         

]

# Ruta de la carpeta donde se guardarán los archivos PDF
pdf_folder = r"C:\Digitalización\Informe"

# Convertir cada HTML a PDF y guardarlos individualmente
for index, url in enumerate(lista, start=1):
    output_pdf_path = os.path.join(pdf_folder, f"{index}.pdf")
    converter.convert(url, output_pdf_path)
    print(f"Convertido: {url} -> {output_pdf_path}")

# Fusionar todos los archivos PDF en uno solo
merger = PdfMerger()

pdf_files = os.listdir(pdf_folder)
pdf_files.sort(key=lambda x: int(x.split('.')[0]))

for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_folder, pdf_file)
    merger.append(pdf_path)

merged_pdf_path = os.path.join(pdf_folder, "informe.pdf")
merger.write(merged_pdf_path)
merger.close()

print(f"Se han fusionado todos los archivos PDF en: {merged_pdf_path}")