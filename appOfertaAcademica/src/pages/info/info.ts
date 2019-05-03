import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { BuscarPage } from '../buscar/buscar';
import { InfoMateriaPage } from '../info-materia/info-materia';

/**
 * Generated class for the InfoPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-info',
  templateUrl: 'info.html',
})
export class InfoPage {
  oferta: any;
  carrera = String;
  buscarPage = BuscarPage;
  infoMateriaPage = InfoMateriaPage;

  constructor(public navCtrl: NavController, public navParams: NavParams) {
    //this.oferta = this.navParams.get('ofertas');
    this.carrera = this.navParams.get('carrera');
    this.oferta = this.navParams.get('ofertas').filter(o => {
      return o.carrera == this.carrera; // V o F
    });

    //console.log(JSON.stringify(this.oferta));
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad InfoPage');
  }

  search()
  {
    console.log("Buscar");
    this.navCtrl.push(this.buscarPage, {ofertas: this.oferta});
  }

  infoMateria(oferta)
  {
    this.navCtrl.push(this.infoMateriaPage, {oferta: oferta})
  }

}
