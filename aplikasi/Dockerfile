# Pilih python base image yang low configuration 
FROM python:3.9.14-alpine3.16

#  Expose port 5000 pada docker container
EXPOSE 5000

# Memilih direktori kerja
WORKDIR /aplikasi

# Install flask
RUN pip3 install flask

# Copy semua project file flask ke WORKDIR
COPY . .

# Eksekusi aplikasi flask dalam container ketika dijalankan
# CMD python3 aplikasi.py
ENTRYPOINT ["python3","aplikasi.py"]

#!/bin/sh
# while true; do
#     docker stats --no-stream
#     sleep 1
# done
