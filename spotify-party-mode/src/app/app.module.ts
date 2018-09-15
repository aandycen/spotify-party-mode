import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule, Routes } from '@angular/router';
import { RoomComponent } from './room/room.component';
import { IndexComponent } from './index/index.component';

const appRoutes: Routes = [
  { path: 'room/:id', component: RoomComponent },
  { path: '**', component: IndexComponent }
];

@NgModule({
  declarations: [
    AppComponent,
    RoomComponent,
    IndexComponent
  ],
  imports: [
    RouterModule.forRoot(
      appRoutes,
      { enableTracing: true } // <-- debugging purposes only
    ),
    BrowserModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
