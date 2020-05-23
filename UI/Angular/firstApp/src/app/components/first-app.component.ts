import { Component} from '@angular/core';

@Component({
  selector: 'app',
  templateUrl: './first-app.component.html',
  styles: []
})
export class FirstAppComponent  {
  public oneName:any ;

  constructor() {
    this.oneName="welcome" ;
   }
public get_oneName():any{
  return this.oneName;
}


}
