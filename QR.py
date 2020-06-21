import pyqrcode  
import pandas as pd


def createQRCode():


    df = pd.read_csv("Data.csv")

    for index, values in df.iterrows():

        PN = values["PN"]
        AO = values["AO"]
        PO = values["PO"]
        QTY = values["QTY"]

        data = f'''
        PN: {PN} \n
        AO: {AO} \n
        PO: {PO} \n
        QTY: {QTY}
        '''
        image = pyqrcode.create(data)
        image.svg(f"{PN}.svg", scale="5")
        print(data)



createQRCode()
