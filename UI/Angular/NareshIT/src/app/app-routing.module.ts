import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from "Home-component/home.component" ;
import { CoursesComponent } from "Courses-component/courses.component" ;
import { ContactComponent } from "Contact-component/contact.component" ;


const routes: Routes = [
  { path: "home", component: HomeComponent },
  { path: "courses", component: CoursesComponent },
  { path: "contact", component: ContactComponent },
  { path: "", component: CoursesComponent },
  { path: "**", component: HomeComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
