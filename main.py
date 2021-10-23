#-------------------------------------------------------------------------------------------
# 1) install PyMuPDF
# pip install PyMuPDF


import fitz

file = fitz.open('report.pdf')


#-------------------------------------------------------------------------------------------
#2) extract text
for pageNumber, page in enumerate(file.pages(), start=1):
        
    text = page.getText()
    txt = open(f'extract_Page_{pageNumber}.json','a', encoding="utf-8")
    txt.writelines(text)
    txt.close()

    #-------------------------------------------------------------------------------------------
    # extract image

for pageNumber, page in enumerate(file.pages(), start=1):
    for imgNumber, img in enumerate(page.getImageList(), start=1):
            
        xref = img[0]
        pix = fitz.Pixmap(file, xref)

        # from documentation: pix.n => byte per pixel
        if pix.n > 4: # since tis is non GRAY or RGB
            pix = fitz.Pixmap(fitz.csRGB, pix)
        pix.writePNG(f'image_Page{pageNumber}_{imgNumber}.png')