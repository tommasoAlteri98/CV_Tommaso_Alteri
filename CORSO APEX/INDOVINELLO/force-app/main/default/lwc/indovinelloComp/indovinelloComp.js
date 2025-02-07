import { LightningElement } from 'lwc';

export default class IndovinelloComp extends LightningElement {
    numeroUtente = '0'; 
    numeroCorretto = Math.floor(Math.random() * 10) + 1;

    aggiornoNumero(event){
        this.numeroUtente = event.target.value;
    }

    mostraMessaggio = false;
    messaggio = '';
    classeMessaggio = '';

    controllaNumero(){
        if(this.numeroUtente == this.numeroCorretto) {
            this.message = 'Complimenti hai indovinato!!';
            this.classeMessaggio='successo';
        }else{
            this.message = 'Peccato, sei un babbano!!';
            this.classeMessaggio='errore';
        }

        this.mostraMessaggio = true;
       
    }
}
