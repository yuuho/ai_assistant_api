FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update \
    && apt-get install -y wget bzip2 ca-certificates libglib2.0-0 libxext6 \
            libsm6 libxrender1 git mercurial subversion cmake libgl1-mesa-dev \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /usr/local/src/* /var/lib/apt/lists/*

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py310_23.3.1-0-Linux-x86_64.sh -O ~/miniconda.sh \
    && /bin/bash ~/miniconda.sh -b -p /opt/conda \
    && rm ~/miniconda.sh \
    && /opt/conda/bin/conda clean -tipy \
    && ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh \
    && echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc \
    && echo "conda activate base" >> ~/.bashrc

RUN conda install -y fastapi uvicorn -c conda-forge \
    && conda clean -afy

# RUN pip install --no-cache-dir responder typesystem==0.2.5 \
#     && rm -rf ~/.cache/pip


