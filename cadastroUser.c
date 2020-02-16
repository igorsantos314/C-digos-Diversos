#include <stdio.h>

void exibirInfo(char *nome, char *sobrenome, int ano, int cpf, int rg);
void getInfo();
int getIdade(int ano);
void cabecalho();

void main(void){
    //iniciar pega de informações
    int opc = 0;

    do
    {
        cabecalho();

        printf("            --> Selecione: ");
        scanf("%d", &opc);

        switch (opc)
        {   
            case 0:
                printf("\n\n               Bye Bye !\n");
                break;

            case 1:
                getInfo();
                break;
            
            default:
                printf("\n\n ------> Por favor, selecione alguma opcao! <------\n\n");
                break;
        }

    }while (opc != 0);

    
}

void getInfo(){
    char nome[50];
    char sobrenome[50];
    int ano, cpf, rg;

    printf("Digite seu Nome: ");
    scanf("%s", nome);

    printf("Digite seu Sobrenome: ");
    scanf("%s", sobrenome);

    printf("Digite seu ano de Nascimento: ");
    scanf("%d", &ano);
    
    printf("Digite seu CPF: ");
    scanf("%d", &cpf);

    printf("Digite seu RG: ");
    scanf("%i", &rg);

    //chamar funcao enviando os dados
    exibirInfo(nome, sobrenome, ano, cpf, rg);
}

int getIdade(int ano){
    return 2020 - ano;
}

void exibirInfo(char *nome, char *sobrenome, int ano, int cpf, int rg){

    int idade = getIdade(ano);

    printf("\nNome: %s\n",nome);
    printf("Sobrenome: %s\n",sobrenome);
    printf("Ano de Nascimento: %i\n",ano);
    printf("Idade: %i\n",idade);
    printf("CPF: %i", cpf);
    printf("RG: %i\n\n", rg);
}

void cabecalho(){

    printf("            ===========================\n");
    printf("            == 0 - Sair              ==\n");
    printf("            == 1 - Realizar Cadastro ==\n");
    printf("            ===========================\n");
}