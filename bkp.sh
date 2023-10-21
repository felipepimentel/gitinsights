#!/bin/zsh

# Verifique se a variável de ambiente está definida
if [[ -z "$DOTFILES_DIR_ENV" ]]; then
    echo "Error: DOTFILES_DIR_ENV is not set." >&2
    exit 1
fi

# Função para fazer backup dos symlinks em um arquivo
backup_symlinks() {
    local dir="$1"
    local backup_file="$2"

    # Inicialize o arquivo de backup
    : > "$backup_file"

    for symlink in $(find "$dir" -type l); do
        local target=$(readlink "$symlink")
        local name=$(basename "$symlink")
        local source=$(dirname "$symlink")

        echo "[$name]" >> "$backup_file"
        echo "type=symlink" >> "$backup_file"
        echo "source=$source" >> "$backup_file"
        echo "target=$target" >> "$backup_file"
        echo "" >> "$backup_file"  # linha em branco entre as seções
    done

    echo "Backup completed: $backup_file"
}

# Caminho para o arquivo de backup
backup_file="$DOTFILES_DIR_ENV/symlink_backup.ini"

# Faça backup dos symlinks no diretório especificado
backup_symlinks "$DOTFILES_DIR_ENV" "$backup_file"
