from pdf2image import convert_from_path
import fitz


def convert_pdf(pdf_file, output_dir):
    doc = fitz.open(pdf_file)
    for i in range(len(doc)):
        page = doc.load_page(i)
        pixmap = page.get_pixmap(dpi=300)
        img = pixmap.tobytes()

        with open(f"{output_dir}page_{i}.jpg", "wb") as f:
            f.write(img)


if __name__ == "__main__":
    pdf_file = "document/4501202637.PDF"
    output_image = "images/"

    # CONVERSIONE IN IMMAGINE CON PDF2IMG

    # # Store Pdf with convert_from_path function
    # images = convert_from_path(pdf_file)

    # for i in range(len(images)):

    #     # Save pages as images in the pdf
    #     images[i].save(output_image + 'page' + str(i) + '.jpg', 'JPEG')

    # CONVERSIONE IN IMMAGINE CON FITZ (PYMUPDF)

    # doc = fitz.open(pdf_file)
    # page = doc.load_page(0)
    # pixmap = page.get_pixmap(dpi=300)
    # img = pixmap.tobytes()

    doc = fitz.open(pdf_file)
    for i in range(len(doc)):
        page = doc.load_page(i)
        pixmap = page.get_pixmap(dpi=300)
        img = pixmap.tobytes()

        with open(f"{output_image}page_{i}.jpg", "wb") as f:
            f.write(img)
