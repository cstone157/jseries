#!/bin/sh

## Make sure our enviroment variables are loaded
. ~/.profile

## Deploy the actual ollama AI
/bin/ollama serve &

## Pull down the lamma 3 AI
ollama pull llama3

## Build the ragdemo go enviroment
cd /ragdemo
go build
