import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';

/**
 * Generated class for the InfoMateriaPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-info-materia',
  templateUrl: 'info-materia.html',
})
export class InfoMateriaPage {
  oferta = {}

  constructor(public navCtrl: NavController, public navParams: NavParams) {
    this.oferta = this.navParams.get('oferta');
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad InfoMateriaPage');
  }

}
