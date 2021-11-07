class Elevador{
    constructor(total_andares, capacidade) {
        this.andar_atual = 0;
        this.total_andares = total_andares;
        this.capacidade = capacidade;
        this.pessoas_abordo = 0;
        this.paradas = [];
    }

    subir(andar){
        if(andar <= this.total_andares && andar < 10){
            var movimento = this.andar_atual-andar;
            var cabines = document.getElementsByClassName('cabine');
            
            while(movimento!=0){
                if(movimento>0){
                    cabines[(10- (this.andar_atual-1))].classList.add('ativo');
                    cabines[(10- this.andar_atual)].classList.remove('ativo');
                    this.andar_atual--;
                    movimento--;
                }else{
                    cabines[(10- (this.andar_atual+1))].classList.add('ativo');
                    cabines[(10- this.andar_atual)].classList.remove('ativo');
                    this.andar_atual++;
                    movimento++;
                }
                alert('O elevador esta no '+ this.andar_atual+'º andar.')
            }
            if (this.paradas.includes(this.andar_atual)){
                this.sair()
            }
            this.entrar()
            
        }else{
            alert('Não é possível subir andares acima do 10º andar')
        }
    }

    descer(andar){
        if(andar <= this.total_andares && andar > 0){
            var movimento = this.andar_atual-andar;
            var cabines = document.getElementsByClassName('cabine');
            
            while(movimento!=0){
                if(movimento>0){
                    cabines[(10- (this.andar_atual-1))].classList.add('ativo');
                    cabines[(10- this.andar_atual)].classList.remove('ativo');
                    this.andar_atual--;
                    movimento--;
                }else{
                    cabines[(10- (this.andar_atual+1))].classList.add('ativo');
                    cabines[(10- this.andar_atual)].classList.remove('ativo');
                    this.andar_atual++;
                    movimento++;
                }
                alert('O elevador esta no '+ this.andar_atual+'º andar.')
            }
            if (this.paradas.includes(this.andar_atual)){
                this.sair()
            }
            this.entrar()
        }else{
            alert('Não é possível descer andares abaixo do térreo')
        }
    }

    aguardar(){
        alert('O elevador esta cheio aguarde');
    }

    entrar(){
        if(this.pessoas_abordo < this.capacidade){
            this.pessoas_abordo++;
            alert(this.pessoas_abordo +' pessoas dentro do elevador');
            var destino = parseInt(prompt("Informe o andar que deseja ir\n 0 - Térreo\n 1 - 1º andar\n 2 - 2º andar\n 3 - 3º andar\n 4 - 4º andar\n 5 - 5º andar\n 6 - 6º andar\n 7 - 7º andar\n 8 - 8º andar\n 9 - 9º andar\n 10 - 10º andar"));
            while(destino==''|| destino<0 || destino>10 || isNaN(destino) || destino ==this.andar_atual){
                alert('Por favor informe um andar de 0 a 10 sem ser o andar que esta agora.')
                destino = prompt("Informe o andar que deseja ir");
                
            }
            this.paradas.push(destino);
        }else{
            this.aguardar();
        }
    }

    sair(){
        for(let i = 0;i <= this.paradas.length; i++){
            if ( this.paradas[i] == this.andar_atual) { 
                this.paradas.splice(i, 1); 
                i--;
                this.pessoas_abordo--;
                alert('Uma pessoa saiu');
            }
        }
    }

}

var elevador = new Elevador(10, 8);
