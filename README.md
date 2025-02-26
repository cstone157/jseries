# jseries
Project for jseries parser

## Pulling the requirements from the MIL-STD-6016G

Attempt to write a jseries parser based upon the MIL-STD-6016G.  This go a little sidetracked by the question of if we could use a AI to generate this code for us.  The original attempt usint ChatGPT & Gemini failed because both of these applications won't parse it since it's a Milspec and some of the specification is classified.  Apparently the RAG/Context that they have is smart enough to block doing this natively.  To get around this the question became is it possible to load all of these documents into our own RAG and then generate the python code from ourself from that RAG.

### Steps

- [x] Prototype using llama/ragdemo (https://pgdash.io/blog/rag-with-postgresql.html) in docker and manually loading the header portion of the document into the rag.  This worked out and generated some basic code, now we need to see if this will work at scale.
- [F] Convert the pdf into text.  The document is to long and complicated to do it manually need a new approach.
- [X] Split the document into a series of individual pages for easier manipulation and working with.
- [ ] Use Excalibur/Camelot library to convert to text.
- [ ] Load parsed text into RAG
- [ ] Use llama to generate the parser

### Side tasks

- [ ] Get Ollama fully working so that it can be used properly (with it's web-gui)


## Links

- https://pgdash.io/blog/rag-with-postgresql.html
- https://github.com/rapidloop/ragdemo
