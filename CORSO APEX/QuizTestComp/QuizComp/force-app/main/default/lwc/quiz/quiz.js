import { LightningElement, track } from 'lwc';

export default class QuizComponent extends LightningElement {
    @track rispostaDomanda1;
    @track rispostaDomanda2;
    @track rispostaDomanda3;
    @track messaggioRis;
    @track classRis;

    get opzioniDomanda1() {
        return [
            { label: 'for:each', value: 'for:each' },
            { label: 'iterator', value: 'iterator' },
            { label: 'map loop', value: 'map loop' },
        ];
    }

    get opzioniDomanda2() {
        return [
            { label: '.svg', value: '.svg' },
            { label: '.apex', value: '.apex' },
            { label: '.js', value: '.js' },
        ];
    }

    get opzioniDomanda3() {
        return [
            { label: '@track', value: '@track' },
            { label: 'if:true', value: 'if:true' },
            { label: 'for:each', value: 'for:each' },
        ];
    }

    get buttonDisabilitato() {
        return !this.rispostaDomanda1 || !this.rispostaDomanda2 || !this.rispostaDomanda3;
    }

    cambiaD1(event) {
        this.rispostaDomanda1 = event.detail.value;
    }

    cambiaD2(event) {
        this.rispostaDomanda2 = event.detail.value;
    }

    cambiaD3(event) {
        this.rispostaDomanda3 = event.detail.value;
    }

    resetRisposte() {
        this.rispostaDomanda1 = undefined;
        this.rispostaDomanda2 = undefined;
        this.rispostaDomanda3 = undefined;
        this.messaggioRis = null;
        this.classRis = '';
    }

    buttonSubmitt(event) {
        event.preventDefault();
        const risposteCorrette = [
            'iterator',     // 
            '.apex',       
            '@track'       
        ];

        const risposteUser = [
            this.rispostaDomanda1,
            this.rispostaDomanda2,
            this.rispostaDomanda3
        ];
        
        const score = risposteUser.filter((risposte, index) => risposte === risposteCorrette[index]).length;

        if (score === 3) {
            this.messaggioRis = 'Tutte le risposte sono corrette!';
            this.classRis = 'successo';
        } else {
            this.messaggioRis = `${3 - score} risposta/e sbagliata/e. Riprova!`;
            this.classRis = 'errore';
        }
    }
}
