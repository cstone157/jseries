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
RUN echo 'export GOPATH=C:\Users\c.stone/go' >> ~/.profile
RUN echo 'export PATH=/bin:/bin:C:\Users\c.stone\bin;C:\Program Files\Git\mingw64\bin;C:\Program Files\Git\usr\local\bin;C:\Program Files\Git\usr\bin;C:\Program Files\Git\usr\bin;C:\Program Files\Git\mingw64\bin;C:\Program Files\Git\usr\bin;C:\Users\c.stone\bin;C:\Program Files\Common Files\Oracle\Java\javapath;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0;C:\Windows\System32\OpenSSH;C:\Program Files\dotnet;C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\170\Tools\Binn;C:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit;C:\Program Files\Git\cmd;C:\Program Files\nodejs;C:\Program Files (x86)\Microsoft SQL Server\160\DTS\Binn;C:\Program Files\Kubernetes\Minikube;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0;C:\WINDOWS\System32\OpenSSH;C:\Program Files\Docker\Docker\resources\bin;C:\Users\c.stone\.cargo\bin;C:\Users\c.stone\.local\bin;C:\Users\c.stone\AppData\Local\Programs\Python\Launcher;C:\Users\c.stone\AppData\Local\Microsoft\WindowsApps;C:\Users\c.stone\AppData\Local\Programs\Microsoft VS Code\bin;C:\Users\c.stone\.dotnet\tools;C:\Users\c.stone\AppData\Roaming\npm;C:\Users\c.stone\AppData\Local\GitHubDesktop\bin;C:\Users\c.stone\Desktop\805_projects\scaffold;C:\Users\c.stone\AppData\Local\Microsoft\WindowsApps;C:\Program Files\Git\usr\bin\vendor_perl;C:\Program Files\Git\usr\bin\core_perl' >> ~/.profile
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