c = get_config()
c.IPKernelApp.pylab = 'inline'
c.NotebookApp.certfile = u'/mycert.pem'
c.NotebookApp.password = u'sha1:5ae3089d6934:3e3540194c0b07cdd329612ef4115c4e259c4ddc'
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False