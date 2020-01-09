#!/usr/bin/env python
import web
import xml.etree.ElementTree as ET

import reconocer as recon

urls = (
    '/reconocedor/(.*)', 'reconocer_imagen'
)

app = web.application(urls, globals())

class reconocer_imagen:
    def GET(self, imageName):
        print("test/" + imageName + "jpeg")
        return recon.reconocer("test/" + imageName + ".jpeg")

if __name__ == "__main__":
    app.run()

