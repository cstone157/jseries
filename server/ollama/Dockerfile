FROM ollama/ollama:0.5.11

## Download and install the llama3 model
RUN ollama pull llama3

## ====================================================== 

## TO-DO: delete me, shouldn't be necissary after we get this up and running
RUN apt-get update && apt-get install
RUN apt-get install -y curl git wget source

## Manually install golang-go, but we need to make sure we use a version higher that 18
WORKDIR /tmp
RUN wget https://go.dev/dl/go1.22.0.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf go1.22.0.linux-amd64.tar.gz

## TO-DO: code for the rag demo (pgdash.io)
WORKDIR /
RUN git clone https://github.com/rapidloop/ragdemo.git
WORKDIR /ragdemo
RUN go build

## Update enviroment variables
RUN echo 'export GOROOT=/usr/local/go' >> ~/.profile
RUN echo 'export GOPATH=$HOME/go' >> ~/.profile
RUN echo 'export PATH=$GOPATH/bin:$GOROOT/bin:$PATH' >> ~/.profile
RUN . ~/.profile

## Connection information to our database
RUN export DATABASE_URL=postgres:///ragdemo?host=postgres-svc
RUN export DATABASE_URL=postgres://postgres@postgres-svc:5432/ragdemo
RUN export PGPASSWORD=password
RUN export OLLAMA_HOST=localhost:11434

## How to add a document to ragdemo
#go run main.go -insert doc_milstd_6061g
## How to actually ask questions of the ragdemo
#go run main.go -query "What was the verdict of McCarthy's inquest?"
COPY doc-5-header /ragdemo/doc-5-header