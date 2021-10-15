/* Máscaras ER */
function mascara(o,f){
    v_obj=o
    v_fun=f
    setTimeout("execmascara()",1)
}
function execmascara(){
    v_obj.value=v_fun(v_obj.value)
}
function mtel(v){
    v=v.replace(/D/g,"");             //Remove tudo o que não é dígito
    v=v.replace(/(d)(d{4})$/,"$1-$2");    //Coloca hífen entre o quarto e o quinto dígitos
    return v;
}
function id( el ){
    return document.getElementById( el );
}

window.onload = function(){
    document.getElementById('id_cep').onkeydown = function(){
        var key = event.keyCode || event.charCode;
        if( !(key == 8) && !(key == 46) ){
            if(this.value.length === 5){
                this.value += '-'
            }
        }
    };
    
}