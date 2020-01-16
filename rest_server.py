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
        web.header('Content-Type', 'application/json')
        print("test/" + imageName + "jpeg")
        result = recon.reconocer("test/" + imageName + ".jpeg")
        print(result)
        return result

if __name__ == "__main__":
    app.run()

