No Git, um symlink é armazenado como um arquivo regular que contém o caminho para o qual o symlink aponta. Isso significa que o Git não armazena o conteúdo do arquivo para o qual o symlink aponta, apenas o caminho. Se o conteúdo real desses arquivos também precisa ser rastreado, eles precisarão ser adicionados ao repositório Git separadamente.

Aqui estão algumas etapas que você pode seguir para garantir que os arquivos fonte estejam presentes e rastreados em seu repositório Git, e não apenas os symlinks:

Identifique Symlinks:
Você pode usar o comando find para identificar symlinks em seu repositório:

bash
Copy code
find . -type l
Verifique o Status do Git:
Use o comando git status para ver quais arquivos foram modificados, adicionados ou removidos. Você pode verificar se os arquivos fonte estão listados.

Adicione Arquivos Fonte ao Git:
Se os arquivos fonte não estiverem sendo rastreados, você pode adicioná-los ao repositório Git usando o comando git add. Por exemplo:

bash
Copy code
git add /path/to/source/file
Use um Script para Verificar:
Você pode escrever um script que itera sobre todos os symlinks, verifica se o arquivo fonte está sendo rastreado pelo Git e, se não, adiciona o arquivo fonte ao Git.

Por exemplo, aqui está um script shell simples que você poderia usar:

bash
Copy code
#!/bin/bash

# Encontre todos os symlinks
for symlink in $(find . -type l); do
    # Obtenha o caminho do arquivo fonte
    source_file=$(readlink "$symlink")
    # Verifique se o arquivo fonte está sendo rastreado pelo Git
    git ls-files --error-unmatch "$source_file" &>/dev/null
    if [[ $? -ne 0 ]]; then
        # Se não, adicione o arquivo fonte ao Git
        git add "$source_file"
        echo "Added source file $source_file to Git."
    fi
done
Configuração do .gitignore:
Certifique-se de que seu arquivo .gitignore não está configurado para ignorar os arquivos fonte que você deseja rastrear.

Revise as Mudanças:
Antes de fazer um commit, revise todas as suas mudanças com git status e git diff para garantir que você está adicionando os arquivos corretos.

Faça o Commit:
Uma vez que você tenha certeza de que todos os arquivos fonte estão sendo rastreados corretamente, faça um commit das mudanças:

bash
Copy code
git commit -m "Add source files for symlinks"
Essas etapas ajudarão a garantir que os arquivos fonte estejam presentes e sendo rastreados em seu repositório Git.