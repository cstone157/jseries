#!/bin/sh

## Pull down the lamma 3 AI
ollama pull llama3

## Build the ragdemo go enviroment
cd /ragdemo
go build

## Deploy the actual ollama AI
/bin/ollama serve
