import {Component} from "@angular/core";

@Component ({
    selector :"mean",
    templateUrl: "./mean.component.html",
    styles: []

})
export class MeanComponent {

    public get_mean():string{

        return  "mean-INDIA";
    }
}