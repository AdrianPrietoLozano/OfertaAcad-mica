import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { HttpClient } from '@angular/common/http';
import { InfoPage } from '../info/info';
import { BuscarPage } from '../buscar/buscar';


@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
  ofertas: any;
  ofertaInni: any;
  infoPage = InfoPage;
  buscarPage = BuscarPage;

  constructor(public navCtrl: NavController, public http: HttpClient) {
    this.http.get("/v1/api/v1/oferta/")
    .subscribe(data => {
      this.ofertas = data;
    }, error => {
      console.log(JSON.stringify(error));
    });
  }

  info(carrera)
  {
    this.navCtrl.push(this.infoPage, {ofertas: this.ofertas, carrera: carrera});
  }

  search()
  {
    console.log("Buscar");
    this.navCtrl.push(this.buscarPage, {ofertas: this.ofertas});
  }

}
