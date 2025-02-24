#!/bin/sh

## ======================== Begin Enviroment Check ========================
# Check if the commands we need to run are installed
if ! command -v envsubst &> /dev/null
then
    printf "envsubst could not be found, used for substitutions.  Please install with something like:\n     $ apt-getg y install getext-base\nInstallation, with vary based on distro.\n"
    exit 1
fi

# Check if we have kubectl or minikube enabled
if ! command -v kubectl &> /dev/null
then
    if ! command -v minikube &> /dev/null
    then
        printf "kubectl and minikube not found, please fix"
        exit 1
    else
        kubectl="minikube kubectl --"
    fi
else
    kubectl="kubectl"
fi
## ========================= End Enviroment Check =========================

# What is the name of our properties file
FILE="./scripts/config.properties"

## Read in our properties file and store the values
function read_properties {
    source $FILE
    # echo "What are the properties we are reading in"
    # while IFS='=' read -r key value; do
    #     echo "key: '$key', value: $value"
    #     if [ $key != "" ]; then
    #         #key=$(echo "$key" | tr '.' '_') # Replace dots in keys with underscores (optional)
    #         eval "${key}=\"${value}\""
    #     fi
    # done < "$FILE"
    # printf  "\n\n"
}

## Build / Delete the registry 
function registry_function {
    if [ -z ${1+x} ] || [ $1 == "--help" ]; then
        registry_error

    elif [ $1 == "clean" ]; then
        echo "Attempting to delete registry from docker"
        docker container stop registry
        docker container rm registry

    elif [ $1 == "build" ]; then
        registry_status="$(docker ps -f 'name=registry')"
        if [[ "$registry_status" =~ "registry" ]]; then
            printf "Registry container already exists.\n"
        else
            printf "Creating Docker registry container:\n"
            docker run -d -p $registry_port:$registry_image_port --restart=always --name registry registry:2
        fi

    else
        registry_error
    fi

    printf "\n\n"
}
function registry_error {
    printf "When using the registry function, you need to 'clean' or 'build'"
    exit 0
}

## Build / Images and load them into the local registry
function images_function {
    if [ -z ${1+x} ] || [ $1 == "--help" ]; then
        images_error
        exit 0

    elif [ $1 == "clean" ]; then
        echo "Images clean up not implemented"
        exit 0

    elif [ $1 == "build" ]; then
        registry_function build
        printf "Attempting to build docker images:"

        ## Build the ollama docker image and add to the registry
        #touch "$ollama_docker_image_folder/Dockerfile"
        #envsubst < "$ollama_docker_image_folder/$ollama_docker_image_template" > "$ollama_docker_image_folder/Dockerfile"
        #docker build "$ollama_docker_image_folder/" -t localhost:$registry_port/$ollama_docker_image_name
        build_image_registry $ollama_docker_image_folder $ollama_docker_image_template $ollama_docker_image_name $registry_port

        ## Build the postgres docker image and add to the registry
        #touch "$postgres_docker_image_folder/Dockerfile"
        #envsubst < "$postgres_docker_image_folder/$postgres_docker_image_template" > "$postgres_docker_image_folder/Dockerfile"
        #docker build "$postgres_docker_image_folder/" -t localhost:$registry_port/$postgres_docker_image_name
        build_image_registry $postgres_docker_image_folder $postgres_docker_image_template $postgres_docker_image_name $registry_port

        ## Delete the temporary dockerfiles
        #rm "$ollama_docker_image_folder/Dockerfile"
        #rm "$postgres_docker_image_folder/Dockerfile"
    else
        images_error
        exit 0
    fi
}
function build_image_registry {
    ## Build and load an image to the registry
    ##      $1 = docker image folder path
    ##      $2 = docker image image template
    ##      $3 = docker image name
    ##      $4 = registry port
    touch "$1/Dockerfile"
    envsubst < "$1/$2" > "$1/Dockerfile"
    docker build "$1/" -t localhost:$4/$3
    rm "$1/Dockerfile"
}
function images_error {
    printf "When using the images_error function, you need to 'clean' or 'build'"
}

## Read our properties
read_properties

