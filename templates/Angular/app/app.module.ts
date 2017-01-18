import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent }  from './app.component';
import { routing } from './app.routing';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';


@NgModule({
	imports:      [ 
	BrowserModule,
    routing,
    FormsModule,
    HttpModule,
	],
	declarations: [ 
		AppComponent 
	],
	bootstrap:    [ 
		AppComponent 
	]
})
export class AppModule { }
