import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { InfoMateriaPage } from '../info-materia/info-materia';

/**
 * Generated class for the BuscarPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-buscar',
  templateUrl: 'buscar.html',
})
export class BuscarPage {
  ofertas: any;
  resultados: any;
  infoMateriaPage = InfoMateriaPage;

  constructor(public navCtrl: NavController, public navParams: NavParams) {
    this.ofertas = this.navParams.get('ofertas');
  }

  getItems(ev: any) {
    let parametro_buscar = ev.target.value.toLowerCase();
  
    this.resultados = this.ofertas.filter(oferta => {
      return oferta.materia.toLowerCase().includes(parametro_buscar) || oferta.profesor.toLowerCase().includes(parametro_buscar); // V o F
    });
    console.log(JSON.stringify(this.resultados));
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad BuscarPage');
  }

  infoMateria(oferta)
  {
    this.navCtrl.push(this.infoMateriaPage, {oferta: oferta})
  }

}
