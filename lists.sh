#!/bin/bash

# Inicialize uma variável para rastrear se algum symlink foi encontrado
symlink_found=0

for symlink in $(find . -type l); do
    target=$(readlink "$symlink")
    if [[ -e $target ]]; then
        echo "Symlink found: $symlink -> $target"
        symlink_found=1  # Atualize a variável para indicar que um symlink foi encontrado
    else
        echo "Target file does not exist: $symlink -> $target"
    fi
done

# Se algum symlink foi encontrado, lance uma falha
if [[ $symlink_found -eq 1 ]]; then
    echo "Error: Symlinks found. Aborting."
    exit 1  # Saia do script com um código de saída não-zero para indicar um erro
fi

# Se nenhum symlink foi encontrado, continue com o restante do seu script
echo "No symlinks found. Continuing."
# ... o restante do seu script
