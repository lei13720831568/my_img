FROM continuumio/anaconda

EXPOSE 8888
VOLUME ["/data/notebooks"]
COPY jupyterNoteBooks.sh /jupyterNoteBooks.sh
COPY jypyter_config.py /jypyter_config.py
COPY mycert.pem /mycert.pem

#use shell 
CMD bash jupyterNoteBooks.sh


