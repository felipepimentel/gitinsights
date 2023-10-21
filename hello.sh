#!/bin/bash

# Obtendo o caminho para o diretório raiz do seu projeto dotfiles da variável de ambiente
DOTFILES_DIR="${DOTFILES_DIR_ENV:-}"

# Verificando se a variável de ambiente está definida
if [[ -z $DOTFILES_DIR ]]; then
    echo "Error: DOTFILES_DIR_ENV is not set." >&2
    exit 1
fi

# Função para criar symlinks a partir do arquivo de mapeamento
create_symlinks() {
    local mapping_file="$1"
    while IFS=' ' read -r source target; do
        # Construindo o caminho completo para o arquivo fonte
        local full_source_path="$DOTFILES_DIR/$source"
        # Verificando se o symlink já existe
        if [[ -L $target ]]; then
            echo "Symlink already exists: $target -> $(readlink "$target")"
        else
            # Verificando se o destino é um arquivo regular (não symlink)
            if [[ -f $target ]]; then
                # Fazendo backup e removendo o arquivo
                mv "$target" "$target.bak"
                echo "Moved existing file to $target.bak"
            fi
            # Criando o symlink
            ln -s "$full_source_path" "$target"
            echo "Created symlink: $full_source_path -> $target"
        fi
    done < "$mapping_file"
}

# Iterando através de cada diretório no projeto dotfiles
find "$DOTFILES_DIR" -type d | while read -r dir; do
    # Verificando se o arquivo de mapeamento existe no diretório
    local mapping_file="$dir/mapping.txt"
    if [[ -f "$mapping_file" ]]; then
        # Chamando a função para criar symlinks
        create_symlinks "$mapping_file"
    fi
done
