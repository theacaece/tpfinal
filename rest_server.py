#!/usr/bin/env python
import web
import xml.etree.ElementTree as ET

import reconocer as recon

urls = (
    '/reconocedor/(.*)', 'reconocer_imagen'
)

app = web.application(urls, globals())

class reconocer_imagen:
    def POST(self, dato):
        image = web.data() #.read()

        print(type(image))
        
        result = recon.reconocer(image)

        print(result)
        web.header('Content-Type', 'application/json')
        return result

if __name__ == "__main__":
    app.run()

