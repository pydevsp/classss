import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { FirstAppComponent } from './components/first-app.component';
import { MeanComponent } from './components/mean.component';
import { MernComponent } from './components/mern.component';
@NgModule({
  declarations: [
    AppComponent,
    FirstAppComponent,
    MernComponent,
    MeanComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [MernComponent]
})
export class AppModule { }
